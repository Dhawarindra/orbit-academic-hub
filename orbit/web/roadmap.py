"""Local, server-rendered Roadmap. Every mutation uses the shared revision token."""

import json
from pathlib import Path
import sqlite3
from uuid import uuid4

import click
from flask import Blueprint, abort, current_app, flash, jsonify, redirect, render_template, request, url_for
from werkzeug.datastructures import MultiDict

from orbit.domain.roadmap import RoadmapError, require
from orbit.services import academic_roadmap as service
from orbit.services import gradebook as book
from orbit.web.grades import message

roadmap = Blueprint("roadmap", __name__, url_prefix="/roadmap")


@roadmap.cli.command("activate-catalog")
@click.argument("path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
def activate_file(path):
    """Validate and activate a versioned synthetic catalog from a local JSON file."""
    database = current_app.config["DATABASE"]
    with book.snapshot(database) as db:
        state = book.workspace(db)
    try:
        contents = path.read_text(encoding="utf-8")
        candidate = json.loads(contents)
        token = MultiDict(dict(epoch=state["epoch"], revision=str(state["state_revision"]),
                               operation=uuid4().hex, catalog_file=contents))
        result = book.command(database, token, "catalog-activate", None,
                              lambda db, current: service.activate_catalog(db, candidate))
    except (ValueError, OSError, sqlite3.Error) as exc:
        raise click.ClickException(str(exc)) from exc
    click.echo(f"Katalog sintetis aktif: {result}")


def page(error=None, status=200, action=None):
    with book.snapshot(current_app.config["DATABASE"]) as db:
        view = service.read(db)
    return render_template("roadmap.html", **view, error=error, action=action, form=request.form), status


@roadmap.get("/")
@roadmap.get("")
def index():
    return page()


@roadmap.post("/<action>")
def update(action):
    commands = {"activate": "catalog-activate", "bind": "course-bind", "plan": "roadmap-plan", "reset": "reset"}
    if action not in commands:
        abort(404)
    form = request.form

    def write(db, state):
        if action == "activate":
            return service.activate_catalog(db, service.demo_catalog())
        catalog = service.active_catalog(db)
        require(catalog and catalog.meta["curriculum_id"] == form.get("catalog"), "Versi katalog berubah. Muat ulang.")
        if action == "bind":
            return service.bind_offering(db, state, form, catalog)
        if action == "plan":
            return service.save_plan(db, state, form, catalog)
        require(form.get("confirm") == "yes", "Konfirmasikan penghapusan seluruh skenario.")
        book.save_scenario(db, state, {}, reset=True)
        return catalog.meta["curriculum_id"]

    try:
        book.command(current_app.config["DATABASE"], form, commands[action], form.get("catalog"), write)
    except (RoadmapError, book.InvalidInput, sqlite3.Error) as exc:
        error, status = message(exc)
        if request.accept_mimetypes.best == "application/json":
            return jsonify(error=error), status
        return page(error, status, action)
    flash({"activate": "Katalog contoh aktif.", "bind": "Pengambilan terhubung ke mata kuliah katalog.",
           "plan": "Rencana semester tersimpan.", "reset": "Skenario direset ke revisi sumber terbaru."}[action])
    anchor = {"plan": "hasil", "bind": "katalog", "reset": "rencana"}.get(action, "katalog")
    location = url_for("roadmap.index", _anchor=anchor)
    if request.accept_mimetypes.best == "application/json":
        return jsonify(location=location)
    return redirect(location, code=303)
