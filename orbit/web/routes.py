"""Read-only Dashboard and local request boundary."""

import sqlite3

from flask import Blueprint, abort, current_app, has_request_context, render_template, request

from orbit.services import dashboard

foundation = Blueprint("foundation", __name__)


@foundation.before_app_request
def require_local_request() -> None:
    if request.remote_addr != "127.0.0.1":
        abort(403)

    port = current_app.config["PORT"]
    suffix = "" if port == 80 else f":{port}"
    if request.host not in {f"127.0.0.1{suffix}", f"localhost{suffix}"}:
        abort(400)

    origin = request.headers.get("Origin")
    if origin is not None and origin != f"http://{request.host}":
        abort(403)


@foundation.app_url_defaults
def retain_term_scope(endpoint, values):
    # Carry the explicit filter through links, form actions and post-save redirects.
    if (has_request_context() and endpoint.split(".")[0] in {"foundation", "roadmap", "grades"}
            and request.args.get("term_id")):
        values.setdefault("term_id", request.args["term_id"])


@foundation.get("/dashboard", strict_slashes=False)
@foundation.get("/")
def home():
    try:
        view = dashboard.read(current_app.config["DATABASE"], request.args.get("term_id"))
    except dashboard.UnknownTerm:
        return render_template("foundation.html", error="Periode yang dipilih tidak ditemukan.", missing_term=True), 404
    except sqlite3.Error:
        return render_template("foundation.html", error="Data lokal belum bisa dibaca. Coba muat ulang ringkasan."), 503
    return render_template("foundation.html", **view)
