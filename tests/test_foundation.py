import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from orbit import create_app
from orbit.__main__ import main
from orbit.repositories.sqlite_store import open_database


class FoundationTests(unittest.TestCase):
    def setUp(self):
        directory = self.enterContext(tempfile.TemporaryDirectory())
        self.database = Path(directory) / "runtime" / "demo.sqlite3"
        self.url = "http://127.0.0.1:5000"
        self.enterContext(patch.dict(os.environ, {
            "ORBIT_DATABASE": str(self.database),
            "ORBIT_HOST": "127.0.0.1",
            "ORBIT_PORT": "5000",
            "FLASK_DEBUG": "0",
            "FLASK_RUN_FROM_CLI": "",
        }))

    def test_runner_opens_empty_database_and_selects_local_settings(self):
        with patch("flask.Flask.run") as run:
            main()
        run.assert_called_once_with(host="127.0.0.1", port=5000, debug=False,
                                    use_reloader=False, load_dotenv=False)
        self.assertTrue(self.database.is_file())
        with open_database(self.database) as db:
            self.assertEqual(db.execute("SELECT count(*) FROM enrollment").fetchone(), (0,))

    def test_home_renders_milestone_and_local_stylesheet(self):
        client = create_app().test_client()
        response = client.get("/", base_url=self.url)
        self.assertEqual(response.status_code, 200)
        page = response.get_data(as_text=True)
        self.assertIn("Orbit Academic Hub", page)
        self.assertIn("Buka Grade Rescue", page)
        self.assertNotIn("{{", page)
        self.assertIn("Demo lokal untuk data sintetis.", page)
        self.assertIn('href="/static/orbit.css"', page)
        with client.get("/static/orbit.css", base_url=self.url) as css:
            self.assertEqual(css.status_code, 200)
            self.assertEqual(css.mimetype, "text/css")
        self.assertEqual(client.post("/", base_url=self.url).status_code, 405)

    def test_local_request_boundary(self):
        client = create_app().test_client()
        self.assertEqual(client.get("/", base_url="http://localhost:5000").status_code, 200)
        for url in ("http://example.invalid:5000", "http://localhost:5001"):
            with self.subTest(url=url):
                self.assertEqual(client.get("/", base_url=url).status_code, 400)
        foreign_peer = client.get("/", base_url=self.url,
                                  environ_overrides={"REMOTE_ADDR": "192.0.2.1"})
        self.assertEqual(foreign_peer.status_code, 403)
        foreign_origin = client.get("/", base_url=self.url,
                                    headers={"Origin": "http://localhost:5001"})
        self.assertEqual(foreign_origin.status_code, 403)

    def test_invalid_settings_fail_before_creating_database(self):
        cases = [
            ("ORBIT_HOST", "0.0.0.0"), ("ORBIT_HOST", "::"),
            ("ORBIT_PORT", "abc"), ("ORBIT_PORT", "0"), ("ORBIT_PORT", "65536"),
            ("FLASK_DEBUG", "1"), ("ORBIT_DATABASE", ""),
        ]
        for variable, value in cases:
            with self.subTest(variable=variable, value=value), patch.dict(os.environ, {variable: value}):
                with self.assertRaisesRegex(ValueError, variable):
                    create_app()
        self.assertFalse(self.database.exists())

    def test_committed_data_survives_reopen_and_unfinished_write_rolls_back(self):
        with open_database(self.database) as db:
            self.assertEqual(db.execute("PRAGMA foreign_keys").fetchone(), (1,))
            db.execute("CREATE TABLE probe (value TEXT)")
            db.execute("BEGIN IMMEDIATE")
            db.execute("INSERT INTO probe VALUES (?)", ("saved",))
            db.execute("COMMIT")
            db.execute("BEGIN IMMEDIATE")
            db.execute("INSERT INTO probe VALUES (?)", ("unfinished",))
        with self.assertRaises(sqlite3.ProgrammingError):
            db.execute("SELECT 1")
        create_app()
        with open_database(self.database) as reopened:
            self.assertEqual(reopened.execute("SELECT value FROM probe").fetchall(), [("saved",)])

    def test_corrupt_file_is_preserved(self):
        self.database.parent.mkdir()
        contents = b"not a SQLite database" * 10
        self.database.write_bytes(contents)
        with self.assertRaisesRegex(ValueError, "database"):
            create_app()
        self.assertEqual(self.database.read_bytes(), contents)

    def test_unknown_schema_version_is_preserved(self):
        with open_database(self.database) as db:
            db.execute("PRAGMA user_version = 7")
        with self.assertRaisesRegex(ValueError, "schema version"):
            create_app()
        with open_database(self.database) as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (7,))
