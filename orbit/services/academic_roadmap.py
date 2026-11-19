"""Roadmap commands and version-scoped reads in the shared workspace transaction."""

import hashlib
import json
from collections import defaultdict
from importlib.resources import files

from orbit.domain import roadmap as engine
from orbit.domain.roadmap import require
from orbit.services import gradebook as book


def demo_catalog():
    return json.loads(files("orbit.repositories").joinpath("roadmap_demo.json").read_text(encoding="utf-8"))


def activate_catalog(db, candidate):
    catalog = engine.validate_catalog(candidate)
    meta = catalog.meta
    key = meta["curriculum_id"]
    digest = hashlib.sha256(json.dumps(candidate, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    existing = db.execute("SELECT curriculum_id,content_hash FROM curriculum_snapshot WHERE curriculum_id=? "
                          "OR (program=? AND version=?)", (key, meta["program"], meta["version"])).fetchall()
    require(all(row["curriculum_id"] == key and row["content_hash"] == digest for row in existing),
            f"VERSION_CONFLICT {key}: isi versi tersimpan berbeda.")
    db.execute("UPDATE curriculum_snapshot SET status='superseded' WHERE status='active'")
    if existing:
        db.execute("UPDATE curriculum_snapshot SET status='active' WHERE curriculum_id=?", (key,))
    else:
        source = json.dumps({"source_ref": meta["source_ref"], "is_synthetic": True})
        db.execute("INSERT INTO curriculum_snapshot VALUES(?,?,?,?,?,?,?,'active')",
                   (key, meta["program"], meta["version"], meta["applicability"], source, meta["rule_version"], digest))
        for course in catalog.courses.values():
            db.execute("INSERT OR IGNORE INTO course VALUES(?)", (course["id"],))
            db.execute("INSERT INTO curriculum_course VALUES(?,?,?,?,?,?,?,?,?,?)",
                       (key, course["id"], course["label"], course["sks"], course.get("category"),
                        course.get("source_ref", meta["source_ref"]), course.get("rule_version", meta["rule_version"]),
                        course.get("recommended"),
                        json.dumps(course.get("rule")), json.dumps(course.get("availability", "unknown"))))
    return key


def active_catalog(db):
    row = db.execute("SELECT * FROM curriculum_snapshot WHERE status='active'").fetchone()
    if not row:
        return None
    candidate = {k: row[k] for k in ("curriculum_id", "program", "version", "applicability", "rule_version")}
    candidate.update(json.loads(row["source"]))
    candidate["courses"] = []
    rows = db.execute("SELECT * FROM curriculum_course WHERE curriculum_id=? "
                      "ORDER BY recommended_sequence IS NULL,recommended_sequence,course_id", (row["curriculum_id"],))
    for c in rows:
        course = dict(id=c["course_id"], label=c["label"], sks=c["sks"], recommended=c["recommended_sequence"],
                      source_ref=c["source_ref"], rule_version=c["rule_version"],
                      rule=json.loads(c["prerequisite"]), availability=json.loads(c["availability"]))
        if c["category"]:
            course["category"] = c["category"]
        candidate["courses"].append(course)
    return engine.validate_catalog(candidate)


def actual_attempts(db, state, catalog):
    rows = db.execute("""SELECT e.enrollment_id,e.status,o.personal_label,o.class_label,t.label AS term,b.curriculum_id,b.course_id,
                         f.outcome,f.revision_no,f.source FROM enrollment e JOIN offering o USING(offering_id)
                         JOIN academic_term t USING(term_id) LEFT JOIN offering_binding b USING(offering_id)
                         LEFT JOIN actual_final_revision f ON f.final_revision_id=(
                             SELECT final_revision_id FROM actual_final_revision WHERE enrollment_id=e.enrollment_id
                             ORDER BY revision_no DESC LIMIT 1)
                         WHERE e.owner_scope=? ORDER BY t.sequence_no,o.personal_label""", (state["owner_scope"],))
    evidence, unbound, excluded = defaultdict(list), [], 0
    for row in rows:
        if row["curriculum_id"] != catalog.meta["curriculum_id"]:
            excluded += 1
            if row["curriculum_id"] is None:
                unbound.append(row)
            continue
        evidence[row["course_id"]].append(engine.Attempt(
            row["enrollment_id"], row["outcome"], row["revision_no"],
            json.loads(row["source"]).get("source_ref") if row["source"] else None, row["status"] == "active"))
    return evidence, unbound, excluded


def bind_offering(db, state, form, catalog):
    enrollment = form.get("enrollment", "")
    key = form.get("course", "")
    require(key in catalog.courses, "Pilih mata kuliah dari katalog aktif.")
    attempt = db.execute("""SELECT e.*,o.term_id,b.curriculum_id FROM enrollment e JOIN offering o USING(offering_id)
                            LEFT JOIN offering_binding b USING(offering_id) WHERE enrollment_id=? AND e.owner_scope=?""",
                         (enrollment, state["owner_scope"])).fetchone()
    require(attempt is not None and attempt["curriculum_id"] is None,
            "Pilih pengambilan Grade Rescue yang belum terhubung.")
    version = catalog.meta["curriculum_id"]
    identity = json.dumps([version, key, attempt["term_id"], attempt["attempt_no"]])
    require(not db.execute("SELECT 1 FROM enrollment WHERE attempt_key=?", (identity,)).fetchone(),
            "Mata kuliah dan pengambilan ini sudah terhubung pada periode tersebut.")
    db.execute("INSERT INTO offering_binding VALUES(?,?,?)", (attempt["offering_id"], version, key))
    db.execute("UPDATE enrollment SET attempt_key=? WHERE enrollment_id=?", (identity, enrollment))
    return enrollment


def number(value, label):
    require(isinstance(value, str) and value.isascii() and value.isdecimal() and len(value) <= 4 and int(value) > 0,
            f"{label}: masukkan bilangan bulat 1–9999.")
    return int(value)


def save_plan(db, state, form, catalog):
    if book.stale(book.scenario(db), state):
        raise book.Conflict("Sumber berubah. Tinjau perubahan dan reset skenario sebelum memilih ulang.")
    cap = number(form["cap"], "Batas SKS") if form.get("cap") else None
    horizon = number(form.get("horizon", ""), "Semester akhir")
    selected, choices = {}, {}
    for field in form:
        if field.startswith("term_"):
            key = field[5:]
            require(key in catalog.courses, f"Mata kuliah di luar katalog: {key}.")
            if form[field]:
                term = number(form[field], f"Semester {key}")
                require(term <= horizon, f"Semester {key} melewati akhir rentang simulasi.")
                selected[key] = term
        if field.startswith("choice_") and form[field]:
            key = field[7:]
            require(key in catalog.alternatives and form[field] in catalog.alternatives[key][1],
                    "Cabang OR tidak cocok dengan aturan katalog.")
            choices[key] = form[field]
    require(all(catalog.alternatives[key][0] in selected for key in choices), "Rencanakan mata kuliah pemilik cabang OR.")
    assumed = form.getlist("assumed")
    require(set(assumed) <= selected.keys(), "Isi semester untuk setiap mata kuliah yang diasumsikan lulus.")
    delay_key, delay_value = form.get("delay_course", ""), form.get("delay_term", "")
    delay = {}
    if delay_key or delay_value:
        require(delay_key in selected, "Pilih mata kuliah dengan semester rencana untuk ditunda.")
        term = number(delay_value, "Semester setelah ditunda")
        require(term > selected[delay_key], "Semester penundaan harus sesudah semester rencana.")
        delay[delay_key] = term
    plan = dict(curriculum_id=catalog.meta["curriculum_id"], selected=selected, cap=cap)
    assumptions = dict(horizon=horizon, passed=sorted(set(assumed)), choices=choices, delay=delay)
    book.save_scenario(db, state, {"plan": plan, "assumptions": assumptions})
    return catalog.meta["curriculum_id"]


def read(db):
    state, catalog, scenario = book.workspace(db), active_catalog(db), book.scenario(db)
    view = dict(state=state, catalog=catalog, scenario=scenario)
    if not catalog:
        return view
    evidence, unbound, excluded = actual_attempts(db, state, catalog)
    plan = json.loads(scenario["plan"]) if scenario else {}
    assumptions = json.loads(scenario["assumptions"]) if scenario else {}
    stale = bool(book.stale(scenario, state))
    changes = []
    if stale:
        changes = db.execute("""SELECT event_type,entity_id,source_revision FROM change_log
                                WHERE epoch=? AND source_revision>? AND event_type NOT IN ('simulation','roadmap-plan','reset')
                                ORDER BY state_revision""", (state["epoch"], scenario["base_source_revision"])).fetchall()
    selected = plan.get("selected", {}) if not stale else {}
    timing = engine.simulate(catalog, evidence, selected, assumptions) if selected else {}
    reasons = {k: engine.evaluate(c.get("rule"), evidence, c["source_ref"], catalog.courses)
               for k, c in catalog.courses.items()}
    credits = engine.credits(catalog, evidence, selected, plan.get("cap"), excluded)
    projected = {key: term for key, (term, _) in timing.items() if term is not None}
    view.update(reasons=reasons, progress={k: engine.progress(evidence[k]) for k in catalog.courses},
                evidence=evidence, unbound=unbound, plan=plan, assumptions=assumptions, stale=stale, changes=changes,
                timing=timing, credits=credits, selected=selected,
                projected=engine.credits(catalog, {}, projected, plan.get("cap"), 0))
    return view
