"""Grade Rescue commands and consistent reads for the local workspace."""

import hashlib
import json
import sqlite3
from contextlib import contextmanager
from decimal import Decimal
from fractions import Fraction
from uuid import uuid4

from orbit.domain.grades import Component, DEMO_THRESHOLDS, InvalidInput, classify, decimal_input, parse_score
from orbit.repositories.sqlite_store import open_database


class Conflict(InvalidInput):
    pass


def source(note="Input manual demo"):
    return json.dumps({"source_kind": "manual_demo", "source_ref": note, "is_synthetic": True})


@contextmanager
def snapshot(path):
    with open_database(path) as db:
        db.row_factory = sqlite3.Row
        db.execute("BEGIN")
        yield db


def workspace(db):
    return db.execute("SELECT * FROM workspace WHERE singleton=1").fetchone()


def command(path, form, action, course_id, writer):
    """Replay a successful submission before checking its original revision."""
    operation = form.get("operation", "")
    if not operation or len(operation) > 64:
        raise InvalidInput("Formulir tidak lengkap. Muat ulang halaman.")
    fields = [(key, form.getlist(key)) for key in sorted(form) if key != "csrf"]
    digest = hashlib.sha256(json.dumps([action, course_id, fields]).encode()).hexdigest()
    with open_database(path) as db:
        db.row_factory = sqlite3.Row
        db.execute("BEGIN IMMEDIATE")
        state = workspace(db)
        replay = db.execute("SELECT * FROM operation_receipt WHERE epoch=? AND operation_id=?",
                            (state["epoch"], operation)).fetchone()
        if replay:
            if digest != replay["request_hash"]:
                raise Conflict("Formulir ini sudah dipakai. Muat ulang sebelum menyimpan perubahan.")
            return replay["result"]
        if (form.get("epoch"), form.get("revision")) != (state["epoch"], str(state["state_revision"])):
            raise Conflict("Data berubah sejak halaman dibuka. Tinjau versi terbaru lalu ulangi.")
        result = writer(db, state)
        revision = state["state_revision"] + 1
        source_rev = state["source_revision"] + int(action not in ("simulation", "roadmap-plan", "reset"))
        db.execute("UPDATE workspace SET state_revision=?,source_revision=?", (revision, source_rev))
        db.execute("""INSERT INTO change_log(event_id,epoch,owner_scope,state_revision,source_revision,
                      entity_id,event_type) VALUES(?,?,?,?,?,?,?)""",
                   (uuid4().hex, state["epoch"], state["owner_scope"], revision, source_rev, result, action))
        db.execute("INSERT INTO operation_receipt VALUES(?,?,?,?,?)",
                   (state["epoch"], operation, digest, result, revision))
        db.execute("COMMIT")
        return result


COURSES = """SELECT e.enrollment_id AS id, o.personal_label AS name, o.class_label AS class_name,
             t.label AS term, p.policy_id AS policy, p.thresholds, b.brp_id, b.version_no, b.locked, b.unsupported_rules
             FROM enrollment e JOIN offering o USING(offering_id) JOIN academic_term t USING(term_id)
             JOIN brp_version b ON b.enrollment_id=e.enrollment_id AND b.status='active'
             LEFT JOIN grade_policy p ON p.offering_id=o.offering_id"""


def courses(db):
    return db.execute(COURSES + " ORDER BY o.personal_label,t.sequence_no,o.class_label").fetchall()


def course(db, course_id):
    row = db.execute(COURSES + " WHERE e.enrollment_id=?", (course_id,)).fetchone()
    if row is None:
        raise KeyError(course_id)
    return row


def components(db, brp_id):
    rows = db.execute("""SELECT n.*,s.earned FROM assessment_node n LEFT JOIN assessment_score s USING(node_id)
                         WHERE brp_id=? ORDER BY position""", (brp_id,))
    parents = {}
    result = []
    for row in rows:
        if row["parent_id"] is None:
            parents[row["node_id"]] = ("", Fraction(1))
            continue
        prefix, weight = parents[row["parent_id"]]
        path = prefix + " / " + row["label"] if prefix else row["label"]
        effective = weight * Fraction(row["weight_bp"], 10000)
        parents[row["node_id"]] = (path, effective)
        item = Component(path, row["weight_bp"], None, None, effective, node_id=row["node_id"])
        if row["kind"] == "leaf":
            item.maximum = Decimal(row["max_score"])
            item.quantum = Decimal(row["granularity"])
            item.earned = Decimal(row["earned"]) if row["earned"] is not None else None
        result.append(item)
    return result


def create_course(db, state, form):
    name, term, group = (form.get(key, "").strip() for key in ("name", "term", "class_name"))
    if not name or not term or max(map(len, (name, term, group))) > 100:
        raise InvalidInput("Isi nama mata kuliah dan periode. Maksimal 100 karakter per kolom.")
    if db.execute("""SELECT 1 FROM offering JOIN academic_term USING(term_id)
                     WHERE personal_label=? AND label=? AND class_label=?""", (name, term, group)).fetchone():
        raise InvalidInput("Mata kuliah dengan periode dan kelas ini sudah tersedia.")
    term_row = db.execute("SELECT term_id FROM academic_term WHERE label=?", (term,)).fetchone()
    term_id = term_row[0] if term_row else uuid4().hex
    if not term_row:
        db.execute("INSERT INTO academic_term SELECT ?,?,COALESCE(MAX(sequence_no),0)+1 FROM academic_term",
                   (term_id, term))
    offering, enrollment = uuid4().hex, uuid4().hex
    db.execute("INSERT INTO offering VALUES(?,?,?,?,?,?)",
               (offering, state["owner_scope"], term_id, name, group, source()))
    db.execute("INSERT INTO enrollment(enrollment_id,offering_id,owner_scope,attempt_key,source) VALUES(?,?,?,?,?)",
               (enrollment, offering, state["owner_scope"], offering + ":1", source()))
    if form.get("policy") == "demo":
        db.execute("INSERT INTO grade_policy VALUES(?,?,?,?,?)",
                   (uuid4().hex, offering, "demo-1", json.dumps(DEMO_THRESHOLDS), source("Kebijakan contoh A/B/C v1")))
    return enrollment


def save_structure(db, state, course_id, items, rule_note):
    previous = db.execute("SELECT * FROM brp_version WHERE enrollment_id=? AND status='active'",
                          (course_id,)).fetchone()
    if previous and previous["locked"]:
        raise Conflict("Struktur terkunci karena skor pernah disimpan.")
    brp = uuid4().hex
    db.execute("UPDATE brp_version SET status='superseded' WHERE enrollment_id=?", (course_id,))
    if len(rule_note) > 300:
        raise InvalidInput("Batasi catatan aturan tambahan hingga 300 karakter.")
    db.execute("INSERT INTO brp_version VALUES(?,?,?,'active',?,?,?,?)",
               (brp, course_id, previous["version_no"]+1 if previous else 1,
                int(any(i.earned is not None for i in items)), source(), "linear-1",
                json.dumps([rule_note] if rule_note else [])))
    root = uuid4().hex
    db.execute("INSERT INTO assessment_node VALUES(?,?,NULL,'group','BRP',10000,NULL,NULL,0)", (root, brp))
    ids = {"": root}
    for position, item in enumerate(items, 1):
        parent, _, label = item.path.rpartition(" / ")
        node = ids[item.path] = uuid4().hex
        leaf = item.maximum is not None
        db.execute("INSERT INTO assessment_node VALUES(?,?,?,?,?,?,?,?,?)",
                   (node, brp, ids[parent], "leaf" if leaf else "group", label, item.weight_bp,
                    str(item.maximum) if leaf else None, str(item.quantum) if leaf else None, position))
        if item.earned is not None:
            db.execute("INSERT INTO assessment_score VALUES(?,?,?,?)",
                       (node, str(item.earned), source(), state["state_revision"] + 1))


def score_inputs(items, form):
    values = {}
    expected = {"score_" + i.node_id for i in items if i.maximum is not None}
    if {key for key in form if key.startswith("score_")} != expected:
        raise InvalidInput("Daftar komponen berubah atau belum lengkap. Tinjau struktur terbaru.")
    for item in items:
        if item.maximum is not None:
            value = parse_score(form["score_" + item.node_id], item.maximum, item.path)
            values[item.node_id] = str(value) if value is not None else None
    return values


def save_scores(db, state, brp_id, values):
    db.executemany("""INSERT INTO assessment_score VALUES(?,?,?,?) ON CONFLICT(node_id) DO UPDATE SET
                      earned=excluded.earned,source=excluded.source,saved_revision=excluded.saved_revision""",
                   [(node, value, source(), state["state_revision"]+1) for node, value in values.items()])
    db.execute("UPDATE brp_version SET locked=1 WHERE brp_id=?", (brp_id,))


def scenario(db):
    return db.execute("SELECT * FROM scenario WHERE singleton=1").fetchone()


def stale(scenario_row, state):
    return scenario_row and (scenario_row["base_epoch"], scenario_row["base_source_revision"]) != (
        state["epoch"], state["source_revision"])


def save_scenario(db, state, changes, reset=False):
    """One aggregate shared by both modules. A reset clears all four overlay fields."""
    old = scenario(db)
    if not reset and stale(old, state):
        raise Conflict("Sumber simulasi berubah. Reset simulasi sebelum mengisi asumsi baru.")
    fields = ("score_overlay", "target_overlay", "plan", "assumptions")
    payload = {field: old[field] if old and not reset else "{}" for field in fields}
    payload.update({field: json.dumps(value) for field, value in changes.items()})
    db.execute("""INSERT INTO scenario(singleton,scenario_id,owner_scope,base_epoch,base_source_revision,
                  scenario_revision,score_overlay,target_overlay,plan,assumptions) VALUES(1,?,?,?,?,1,?,?,?,?)
                  ON CONFLICT(singleton) DO UPDATE SET base_epoch=excluded.base_epoch,
                  base_source_revision=excluded.base_source_revision,scenario_revision=scenario_revision+1,
                  score_overlay=excluded.score_overlay,target_overlay=excluded.target_overlay,
                  plan=excluded.plan,assumptions=excluded.assumptions""",
               (uuid4().hex, state["owner_scope"], state["epoch"], state["source_revision"],
                *(payload[field] for field in fields)))


def save_overlay(db, state, values, course_id, target="", reset=False):
    if reset:
        save_scenario(db, state, {}, reset=True)
        return
    old = scenario(db)
    overlay = json.loads(old["score_overlay"]) if old else {}
    targets = json.loads(old["target_overlay"]) if old else {}
    if target:
        targets[course_id] = target
    else:
        targets.pop(course_id, None)
    for key, value in values.items():
        if value is None:
            overlay.pop(key, None)
        else:
            overlay[key] = value
    save_scenario(db, state, {"score_overlay": overlay, "target_overlay": targets})


def bound_policy(row):
    return json.loads(row["thresholds"]) if row["policy"] else None


def final_input(form, policy, previous):
    numeric = form.get("numeric", "").strip()
    letter = form.get("letter", "").strip().upper()
    outcome = form.get("outcome", "unresolved")
    reason = form.get("reason", "").strip()
    note = form.get("note", "").strip()
    if not note or len(note) > 200 or len(reason) > 400:
        raise InvalidInput("Cantumkan sumber (maks. 200 karakter) dan batasi alasan hingga 400 karakter.")
    if previous and not reason:
        raise InvalidInput("Cantumkan alasan koreksi nilai final.")
    if outcome not in {"unresolved", "passed", "failed"} or not (numeric or letter or outcome != "unresolved"):
        raise InvalidInput("Isi nilai angka, nilai huruf, atau hasil aktual yang diketahui.")
    value = decimal_input(numeric, "Nilai final", maximum=100) if numeric else None
    if letter and (len(letter) > 2 or letter[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or
                   (len(letter) == 2 and letter[1] not in "+-")):
        raise InvalidInput("Nilai huruf tidak valid.")
    if policy and letter and (letter not in policy or (value is not None and classify(value, policy) != letter)):
        raise InvalidInput("Nilai huruf tidak cocok dengan kebijakan contoh pada kelas ini.")
    return dict(numeric=str(value) if value is not None else None, letter=letter or None,
                outcome=outcome, note=note, reason=reason or None)


def history(db, course_id):
    return db.execute("SELECT * FROM actual_final_revision WHERE enrollment_id=? ORDER BY revision_no DESC",
                      (course_id,)).fetchall()


def confirm_final(db, state, row, data):
    old = history(db, row["id"])
    final = final_input({key: value or "" for key, value in data.items()}, bound_policy(row), old)
    db.execute("""INSERT INTO actual_final_revision(final_revision_id,enrollment_id,revision_no,supersedes_id,
                  numeric_value,letter_value,policy_id,outcome,source,correction_reason,committed_revision)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?)""",
               (uuid4().hex, row["id"], len(old)+1, old[0]["final_revision_id"] if old else None,
                final["numeric"], final["letter"], row["policy"], final["outcome"], source(final["note"]),
                final["reason"], state["state_revision"]+1))
