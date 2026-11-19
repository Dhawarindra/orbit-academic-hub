"""Read the settings used by the local demo runner and request checks."""

import os
from pathlib import Path


def local_settings(instance_path: Path) -> dict:
    host = os.getenv("ORBIT_HOST", "127.0.0.1")
    if host != "127.0.0.1":
        raise ValueError("ORBIT_HOST must be 127.0.0.1 for the local demo.")
    if os.getenv("FLASK_DEBUG", "").lower() not in {"", "0", "false", "no"}:
        raise ValueError("Disable FLASK_DEBUG for the local demo.")
    if os.getenv("FLASK_RUN_FROM_CLI") == "true":
        raise ValueError("Start the local demo with python -m orbit.")

    port = os.getenv("ORBIT_PORT", "5000")
    if not port.isascii() or not port.isdecimal() or not 1 <= int(port) <= 65535:
        raise ValueError("ORBIT_PORT must be an integer from 1 to 65535.")

    database = os.getenv("ORBIT_DATABASE", str(instance_path / "orbit.sqlite3"))
    if not database.strip() or database == ":memory:":
        raise ValueError("ORBIT_DATABASE must name a local SQLite file.")
    path = Path(database).resolve()
    if path.is_relative_to(Path(__file__).parent / "static"):
        raise ValueError("Keep ORBIT_DATABASE outside the public static directory.")
    return {"HOST": host, "PORT": int(port), "DATABASE": path, "DEBUG": False}
