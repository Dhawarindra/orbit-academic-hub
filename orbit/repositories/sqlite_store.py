"""Short-lived SQLite connections and transactional upgrade of the M0 database."""

import sqlite3
from collections.abc import Iterator
from contextlib import closing, contextmanager
from pathlib import Path
from uuid import uuid4


@contextmanager
def open_database(path: Path) -> Iterator[sqlite3.Connection]:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Keep transaction boundaries explicit. Closing also rolls back an open transaction.
    with closing(sqlite3.connect(path, autocommit=True)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        yield connection


def check_database(path: Path) -> None:
    try:
        with open_database(path) as connection:
            connection.execute("BEGIN IMMEDIATE")
            version = connection.execute("PRAGMA user_version").fetchone()[0]
            if version not in (0, 1, 2):
                raise ValueError("Unsupported SQLite schema version.")
            if connection.execute("PRAGMA quick_check(1)").fetchone()[0] != "ok":
                raise ValueError("SQLite integrity check failed.")
            if version == 0:
                schema = Path(__file__).with_name("grades.sql").read_text(encoding="utf-8")
                for statement in schema.split(";"):
                    if statement.strip():
                        connection.execute(statement)
                connection.execute(
                    "INSERT INTO workspace(singleton,owner_scope,epoch) VALUES(1,?,?)",
                    (uuid4().hex, uuid4().hex),
                )
                connection.execute("PRAGMA user_version=1")
            if version < 2:
                schema = Path(__file__).with_name("roadmap.sql").read_text(encoding="utf-8")
                for statement in schema.split(";"):
                    if statement.strip():
                        connection.execute(statement)
                connection.execute("UPDATE workspace SET schema_version=2")
                connection.execute("PRAGMA user_version=2")
            connection.execute("COMMIT")
    except (OSError, sqlite3.Error) as error:
        raise ValueError(
            "Cannot read the local SQLite database. Check ORBIT_DATABASE, "
            "the file format, and directory permissions."
        ) from error
