"""HTML forms for entering, inspecting and simulating a synthetic course."""

import hmac
import json
import os
import secrets
import sqlite3
from pathlib import Path
from tempfile import NamedTemporaryFile
from uuid import uuid4

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, session, url_for
from itsdangerous import BadSignature, URLSafeSerializer

from orbit.domain.grades import InvalidInput, classify, display, parse_target, solve_target, summarize, validate_structure
from orbit.services import gradebook as book

grades = Blueprint("grades", __name__, url_prefix="/grades")


def signing_key(directory):
    """Publish a complete, private key atomically, including on concurrent starts."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    key = directory / "grade-signing.key"
    if not key.exists():
        with NamedTemporaryFile(dir=directory, delete=False) as tmp:
            tmp.write(secrets.token_bytes(32))
        try:
            os.link(tmp.name, key)
        except FileExistsError:
            pass
        finally:
            Path(tmp.name).unlink()
    return key.read_bytes()


@grades.app_context_processor
def helpers():
    if "csrf" not in session:
        session["csrf"] = secrets.token_urlsafe(32)
    return dict(operation_id=lambda: uuid4().hex, fmt=display)


@grades.before_app_request
def csrf_check():
    if request.method == "POST" and request.blueprint in ("grades", "roadmap"):
        token = session.get("csrf")
        if not token or not hmac.compare_digest(request.form.get("csrf", "").encode(), token.encode()):
            abort(403, "Formulir kedaluwarsa. Muat ulang halaman.")


def database():
    return current_app.config["DATABASE"]


def listed():
    with book.snapshot(database()) as db:
        return book.courses(db)


@grades.get("")
@grades.get("/")
def index():
    return render_template("grade_index.html", courses=listed())


def new_rows(example=False):
    default = [("UTS", "50", "100", "1", ""), ("UAS", "50", "100", "1", "")]
    if example:
        default = [("Kuis", "20", "", "", ""), ("Kuis / Q1", "50", "100", "1", "80"),
                   ("Kuis / Q2", "50", "100", "1", "100"), ("UTS", "30", "100", "1", "60"),
                   ("UAS", "50", "100", "1", "")]
    return [dict(zip(ROW_FIELDS, row)) for row in default]


ROW_FIELDS = ("path", "weight", "maximum", "quantum", "earned")


def structure_rows(form):
    columns = [form.getlist(key) for key in ROW_FIELDS]
    if len(set(map(len, columns))) != 1:
        raise InvalidInput("Kolom komponen tidak lengkap.")
    return [dict(zip(ROW_FIELDS, values)) for values in zip(*columns)]


def component_row(i):
    return dict(path=i.path, weight=display_ratio_bp(i.weight_bp),
                maximum=str(i.maximum) if i.maximum is not None else "",
                quantum=str(i.quantum) if i.quantum is not None else "",
                earned=str(i.earned) if i.earned is not None else "")


def display_ratio_bp(bp):
    return f"{bp // 100}.{bp % 100:02d}".rstrip("0").rstrip(".")


def editor(course_id=None):
    with book.snapshot(database()) as db:
        state = book.workspace(db)
        row = book.course(db, course_id) if course_id else None
        if row and row["locked"] and request.method == "GET":
            return redirect(url_for("grades.detail", course_id=course_id))
        example = request.args.get("example") == "1"
        entries = ([component_row(i) for i in book.components(db, row["brp_id"])]
                   if row else new_rows(example))
    form = request.form
    values = form if request.method == "POST" else (row or {"name": "Dasar Pemrograman" if example else "",
                                                           "term": "Semester demo" if example else ""})
    error, status = None, 200
    if request.method == "POST":
        try:
            entries = structure_rows(form)
            action = form.get("edit", "save")
            if action == "add":
                entries.append(dict(path="", weight="", maximum="100", quantum="1", earned=""))
            elif action.startswith("remove:") and action[7:].isdigit():
                number = int(action[7:])
                if number < len(entries):
                    entries.pop(number)
            else:
                def write(db, current):
                    items = validate_structure(entries)
                    enrollment = course_id or book.create_course(db, current, form)
                    book.save_structure(db, current, enrollment, items, form.get("rule_note", "").strip())
                    return enrollment
                saved = book.command(database(), form, "structure", course_id, write)
                flash("Struktur penilaian tersimpan.")
                return redirect(url_for("grades.detail", course_id=saved), code=303)
        except (InvalidInput, sqlite3.Error) as exc:
            error, status = message(exc)
    return render_template("grade_editor.html", course=row, values=values, entries=entries, state=state,
                           form=form, error=error, example=example,
                           rules=json.loads(row["unsupported_rules"]) if row else []), status


@grades.route("/new", methods=["GET", "POST"])
def new():
    return editor()


@grades.route("/<course_id>/structure", methods=["GET", "POST"])
def edit(course_id):
    return editor(course_id)


def message(exc):
    if isinstance(exc, sqlite3.Error):
        return "Penyimpanan lokal gagal. Periksa ruang disk dan coba kembali.", 503
    return str(exc), 409 if isinstance(exc, book.Conflict) else 422


@grades.errorhandler(KeyError)
def missing_course(exc):
    return render_template("grade_missing.html"), 404


def course_page(course_id, *, error=None, status=200, action="", preview=None):
    with book.snapshot(database()) as db:
        state = book.workspace(db)
        row = book.course(db, course_id)
        items = book.components(db, row["brp_id"])
        target = db.execute("SELECT * FROM course_target WHERE enrollment_id=?", (course_id,)).fetchone()
        finals = book.history(db, course_id)
        scenario = book.scenario(db)
    is_stale = bool(book.stale(scenario, state))
    overlay = json.loads(scenario["score_overlay"]) if scenario else {}
    here = {i.node_id: overlay[i.node_id] for i in items if i.node_id in overlay}
    overlay_target = json.loads(scenario["target_overlay"]).get(course_id) if scenario else None
    actual = summarize(items)
    projection = summarize(items, here) if (here or overlay_target) and not is_stale else None
    numeric = letter = None
    if target:
        numeric, letter = parse_target(target["numeric_target"] or target["letter_target"])
    rules = json.loads(row["unsupported_rules"])
    policy = book.bound_policy(row) if not rules else None
    result = solve_target(actual, numeric, letter, policy)
    sim_target = parse_target(overlay_target) if overlay_target else (numeric, letter)
    projected_target = solve_target(projection, *sim_target, policy) if projection else None
    return render_template("grade_detail.html", course=row, items=items, actual=actual, projection=projection,
                           target=target, result=result, projected_target=projected_target, overlay=here, state=state,
                           stale=is_stale, scenario=scenario, finals=finals, form=request.form, classify=classify,
                           source_note=lambda data: json.loads(data)["source_ref"], action=action,
                           preview=preview, error=error, overlay_target=overlay_target, rules=rules, policy=policy), status


@grades.get("/<course_id>")
def detail(course_id):
    return course_page(course_id)


@grades.post("/<course_id>/<action>")
def update(course_id, action):
    form = request.form
    signer = URLSafeSerializer(current_app.secret_key, salt="grade-final-v1")
    if action not in ("scores", "target", "simulation", "reset", "preview", "confirm"):
        abort(404)

    try:
        if action == "preview":
            with book.snapshot(database()) as db:
                state = book.workspace(db)
                row = book.course(db, course_id)
                if (form.get("epoch"), form.get("revision")) != (state["epoch"], str(state["state_revision"])):
                    raise book.Conflict("Data berubah. Muat ulang sebelum meninjau nilai final.")
                data = book.final_input(form, book.bound_policy(row), book.history(db, course_id))
                proof = signer.dumps([course_id, state["epoch"], state["state_revision"], data])
            return course_page(course_id, action=action, preview={"data": data, "proof": proof})

        def write(db, state):
            row = book.course(db, course_id)
            if action in ("scores", "simulation"):
                values = book.score_inputs(book.components(db, row["brp_id"]), form)
                if action == "scores":
                    book.save_scores(db, state, row["brp_id"], values)
                else:
                    target = form.get("sim_target", "").strip()
                    if target:
                        parse_target(target)
                    book.save_overlay(db, state, values, course_id, target)
            elif action == "target":
                numeric, letter = parse_target(form.get("target", ""))
                db.execute("""INSERT INTO course_target VALUES(?,?,?,?,?,?) ON CONFLICT(enrollment_id)
                              DO UPDATE SET numeric_target=excluded.numeric_target,letter_target=excluded.letter_target,
                              policy_id=excluded.policy_id,source=excluded.source,saved_revision=excluded.saved_revision""",
                           (course_id, str(numeric) if numeric is not None else None, letter, row["policy"],
                            book.source(), state["state_revision"]+1))
            elif action == "reset":
                book.save_overlay(db, state, {}, course_id, reset=True)
            elif action == "confirm":
                try:
                    enrollment, epoch, rev, data = signer.loads(form.get("proof", ""))
                except BadSignature:
                    raise InvalidInput("Pratinjau konfirmasi tidak valid. Tinjau ulang nilai.") from None
                if (enrollment, epoch, rev) != (course_id, state["epoch"], state["state_revision"]):
                    raise book.Conflict("Pratinjau sudah kedaluwarsa. Tinjau ulang nilai terbaru.")
                book.confirm_final(db, state, row, data)
            return course_id

        book.command(database(), form, action, course_id, write)
        flash("Perubahan tersimpan di perangkat ini.")
        return redirect(url_for("grades.detail", course_id=course_id), code=303)
    except (InvalidInput, sqlite3.Error) as exc:
        error, status = message(exc)
        return course_page(course_id, error=error, status=status, action=action)
