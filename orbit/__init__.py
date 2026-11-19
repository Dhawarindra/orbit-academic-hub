"""Create the Flask application used by the local runner and tests."""

from pathlib import Path

from flask import Flask

from .config import local_settings
from .domain.grades import exact_score
from .repositories.sqlite_store import check_database
from .web.routes import foundation
from .web.grades import grades, signing_key


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update(local_settings(Path(app.instance_path)))
    check_database(app.config["DATABASE"])
    app.secret_key = signing_key(Path(app.instance_path))
    app.config.update(SESSION_COOKIE_SAMESITE="Strict", MAX_CONTENT_LENGTH=1024 * 1024)
    app.register_blueprint(foundation)
    app.register_blueprint(grades)
    app.add_template_filter(exact_score)
    return app
