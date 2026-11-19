"""Read-only foundation screen and local request boundary."""

from flask import Blueprint, abort, current_app, render_template, request

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


@foundation.get("/")
def home():
    return render_template("foundation.html")
