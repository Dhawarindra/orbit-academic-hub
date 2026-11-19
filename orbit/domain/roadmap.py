"""Version-scoped synthetic catalogs, actual evidence and conditional semester planning."""

from collections import Counter, defaultdict
from dataclasses import dataclass
import re


class RoadmapError(ValueError):
    pass


def positive(value):
    return type(value) is int and value > 0


def identifier(value):
    return isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9_.-]{1,80}", value)


def require(condition, message):
    if not condition:
        raise RoadmapError(message)


@dataclass
class Catalog:
    meta: dict
    courses: dict
    order: list
    dependencies: dict
    dependents: dict
    alternatives: dict


def validate_catalog(candidate):
    """Validate the entire candidate, including references on unselected OR branches."""
    require(isinstance(candidate, dict), "Format katalog tidak valid.")
    require(all(isinstance(candidate.get(k), str) and candidate[k].strip() for k in
                ("program", "version", "applicability", "source_ref", "rule_version"))
            and identifier(candidate.get("curriculum_id")) and candidate.get("is_synthetic") is True,
            "Identitas, versi, cakupan, atau sumber sintetis katalog belum lengkap.")
    records = candidate.get("courses")
    require(isinstance(records, list) and records, "Katalog belum berisi mata kuliah.")
    courses, dependencies, alternatives = {}, {}, {}
    reference_errors = []
    seen_nodes = set()
    for row in records:
        require(isinstance(row, dict) and identifier(row.get("id")), "ID mata kuliah tidak valid.")
        key = row["id"]
        if row.get("curriculum_id", candidate["curriculum_id"]) != candidate["curriculum_id"]:
            reference_errors.append(f"SCOPE_MISMATCH {key} @ {row['curriculum_id']}")
        require(key not in courses, f"ID mata kuliah ganda: {key}.")
        require(isinstance(row.get("label"), str) and row["label"].strip() and positive(row.get("sks")),
                f"{key}: nama dan SKS positif diperlukan.")
        for field in ("source_ref", "rule_version", "category"):
            if field in row:
                require(isinstance(row[field], str) and row[field].strip(), f"{key}: {field} tidak valid.")
        term = row.get("recommended")
        require(term is None or positive(term), f"{key}: rekomendasi semester tidak valid.")
        availability = row.get("availability", "unknown")
        require(availability in ("every_term", "unknown", "odd", "even") or
                isinstance(availability, list) and all(positive(i) for i in availability)
                and len(set(availability)) == len(availability), f"{key}: penawaran semester tidak valid.")
        courses[key] = row
        dependencies[key] = set()

    def reference(owner, ref, node_id):
        if isinstance(ref, dict):
            if ref.get("curriculum_id") != candidate["curriculum_id"]:
                reference_errors.append(f"SCOPE_MISMATCH {owner}/{node_id}: {ref.get('course_id')} @ {ref.get('curriculum_id')}")
            ref = ref.get("course_id")
        if identifier(ref) and ref in courses:
            dependencies[owner].add(ref)
        else:
            reference_errors.append(f"DANGLING_REFERENCE {owner}/{node_id}: {ref}")

    def visit_rule(owner, node):
        require(isinstance(node, dict) and identifier(node.get("id")), f"{owner}: ID aturan tidak valid.")
        key = node["id"]
        require(key not in seen_nodes, f"{owner}: ID aturan terpakai kembali: {key}.")
        seen_nodes.add(key)
        if node.get("curriculum_id", candidate["curriculum_id"]) != candidate["curriculum_id"]:
            reference_errors.append(f"SCOPE_MISMATCH {owner}/{key}: {node.get('course_id', '')} @ {node['curriculum_id']}")
        op = node.get("op")
        require(op in ("and", "or") or "children" not in node, f"{owner}/{key}: hanya grup boleh memiliki cabang.")
        if op in ("and", "or"):
            children = node.get("children")
            require(isinstance(children, list) and children, f"{owner}/{key}: grup prasyarat kosong.")
            for child in children:
                visit_rule(owner, child)
            if op == "or":
                alternatives[key] = (owner, [child["id"] for child in children])
        elif op == "passed":
            require(identifier(node.get("course_id")), f"{owner}/{key}: ID mata kuliah tidak valid.")
            reference(owner, node.get("course_id"), key)
        elif op == "none":
            require(isinstance(node.get("source_ref"), str) and node["source_ref"].strip(),
                    f"{owner}/{key}: sumber untuk aturan tanpa prasyarat diperlukan.")
        elif op == "unsupported":
            require(all(isinstance(node.get(k), str) and node[k].strip() for k in ("raw", "reason"))
                    and isinstance(node.get("refs", []), list), f"{owner}/{key}: catatan aturan tidak lengkap.")
            for ref in node.get("refs", []):
                reference(owner, ref, key)
        else:
            raise RoadmapError(f"{owner}/{key}: tandai aturan yang belum didukung sebagai unsupported.")

    for key, course in courses.items():
        if course.get("rule") is not None:
            visit_rule(key, course["rule"])
    if reference_errors:
        raise RoadmapError(" · ".join(reference_errors))

    order, visiting, done = [], {}, set()

    def visit_course(key):
        if key in visiting:
            cycle = list(visiting)[visiting[key]:] + [key]
            raise RoadmapError("GRAPH_CYCLE " + " → ".join(cycle))
        if key not in done:
            visiting[key] = len(visiting)
            for parent in dependencies[key]:
                visit_course(parent)
            del visiting[key]
            done.add(key)
            order.append(key)

    for key in courses:
        visit_course(key)
    dependents = defaultdict(list)
    for key, parents in dependencies.items():
        for parent in parents:
            dependents[parent].append(key)
    return Catalog({k: v for k, v in candidate.items() if k != "courses"}, courses, order,
                   dependencies, dependents, alternatives)


@dataclass(frozen=True)
class Attempt:
    enrollment: str
    outcome: str | None
    revision: int | None
    source: str | None
    active: bool


def progress(attempts):
    if not attempts:
        return "not_started"
    outcomes = {a.outcome for a in attempts}
    if outcomes == {"passed"} or outcomes == {"failed"}:
        return next(iter(outcomes))
    if len(outcomes) > 1 or "unresolved" in outcomes:
        return "unresolved"
    return "active"


def evaluate(rule, evidence, source, courses=None):
    """Produce the complete reason tree, including leaves irrelevant to a short circuit."""
    if rule is None:
        return dict(status="unknown", text="Sumber belum mencantumkan prasyarat.", source=source)
    op = rule["op"]
    if op in ("and", "or"):
        children = [evaluate(child, evidence, source, courses) for child in rule["children"]]
        states = {c["status"] for c in children}
        decisive, opposite = ("unmet", "met") if op == "and" else ("met", "unmet")
        status = decisive if decisive in states else opposite if states == {opposite} else "unknown"
        return dict(id=rule["id"], status=status, text="Semua syarat (AND)" if op == "and" else "Salah satu syarat (OR)",
                    children=children)
    status, attempts = "unknown", []
    if op == "none":
        status, reason = "met", "Tanpa prasyarat pada contoh ini."
    elif op == "unsupported":
        reason = f"Aturan belum didukung: {rule['raw']} · {rule['reason']}"
        if rule.get("refs"):
            reason += " · " + ", ".join(r if isinstance(r, str) else r["course_id"] for r in rule["refs"])
    else:
        course = rule["course_id"]
        attempts = evidence.get(course, [])
        result = progress(attempts)
        if result in ("passed", "failed"):
            status = "met" if result == "passed" else "unmet"
            detail = "lulus terkonfirmasi" if result == "passed" else "gagal terkonfirmasi"
        elif len({a.outcome for a in attempts}) > 1:
            detail = "hasil antar-pengambilan berbeda dan kebijakan pengulangan belum tersedia"
        elif any(a.revision for a in attempts):
            detail = "hasil kelulusan belum dipastikan"
        else:
            detail = "belum ada hasil final terkonfirmasi"
        label = courses[course]["label"] if courses else course
        reason = f"Lulus {label} — {detail}."
    return dict(id=rule["id"], status=status, text=reason, attempts=attempts, source=rule.get("source_ref", source))


def credits(catalog, evidence, selected, cap, excluded):
    completed = active = 0
    totals = Counter()
    for key, course in catalog.courses.items():
        attempts = evidence.get(key, [])
        sks = course["sks"]
        if progress(attempts) == "passed":
            completed += sks
        active += sum(sks for attempt in attempts if attempt.active and attempt.revision is None)
        if key in selected:
            totals[selected[key]] += sks
    return dict(completed=completed, active=active, totals=dict(sorted(totals.items())), excluded=excluded,
                over={term for term, total in totals.items() if cap is not None and total > cap})


def next_slot(availability, start, horizon):
    if availability == "unknown":
        return None, "Waktu penawaran perlu dikonfirmasi."
    for term in range(start, horizon + 1):
        if (availability == "every_term" or availability == "odd" and term % 2 == 1
                or availability == "even" and term % 2 == 0
                or isinstance(availability, list) and term in availability):
            return term, ""
    return None, f"Tidak ada slot hingga semester {horizon}."


def simulate(catalog, evidence, selected, assumptions):
    """Earliest conditional semester per selection. Never change the requested plan."""
    result = {}
    assumed = set(assumptions.get("passed", []))
    choices = assumptions.get("choices", {})
    delay = assumptions.get("delay", {})
    horizon = assumptions["horizon"]

    def ready(rule):
        if rule is None:
            return None, "Aturan prasyarat belum tersedia."
        op = rule["op"]
        if op == "none":
            return 1, ""
        if op == "unsupported":
            return None, f"Aturan belum didukung: {rule['raw']}."
        if op == "passed":
            key = rule["course_id"]
            if progress(evidence.get(key, [])) == "passed":
                return 1, ""
            if key not in selected or key not in assumed:
                return None, f"{catalog.courses[key]['label']} memerlukan hasil lulus atau pilihan semester dan asumsi lulus."
            term, reason = result[key]
            return (term + 1, "") if term else (None, f"{catalog.courses[key]['label']}: {reason}")
        children = rule["children"]
        if op == "or":
            child = next((c for c in children if c["id"] == choices.get(rule["id"])), None)
            return ready(child) if child else (None, "Pilih cabang OR untuk simulasi.")
        constraints = [ready(c) for c in children]
        for term, reason in constraints:
            if term is None:
                return None, reason
        return max(term for term, _ in constraints), ""

    for key in catalog.order:
        if key in selected:
            course = catalog.courses[key]
            earliest, reason = ready(course.get("rule"))
            if earliest is None:
                result[key] = None, reason
            else:
                start = max(selected[key], delay.get(key, 1), earliest)
                result[key] = next_slot(course.get("availability", "unknown"), start, horizon)
    return result
