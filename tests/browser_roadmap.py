"""Optional Chromium check for MAP-T-101/103. Run with Python that has Playwright."""

import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
from tempfile import TemporaryDirectory

from playwright.sync_api import expect, sync_playwright


# Let the OS assign a loopback port; update Orbit's Host check to match it.
SERVER = """
from werkzeug.serving import make_server
from orbit import create_app
app = create_app()
server = make_server("127.0.0.1", 0, app)
app.config["PORT"] = server.server_port
print(server.server_port, flush=True)
server.serve_forever()
"""


def tab_to(page, control):
    for _ in range(120):
        if control.evaluate("(el) => el === document.activeElement"):
            return
        page.keyboard.press("Tab")
    raise AssertionError("Control unreachable via Tab: " + control.evaluate("el => el.outerHTML"))


def revision(database):
    with sqlite3.connect(database) as db:
        return db.execute("SELECT state_revision FROM workspace").fetchone()[0]


def browser_check(base, database):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=shutil.which("chromium"))
        page = browser.new_page(viewport={"width": 1280, "height": 850})
        page.goto(base)
        tab_to(page, page.get_by_role("navigation").get_by_role("link", name="Academic Roadmap"))
        page.keyboard.press("Enter")
        tab_to(page, page.get_by_role("button", name="Gunakan katalog contoh"))
        page.keyboard.press("Enter")
        expect(page.get_by_text("Katalog contoh aktif.", exact=True)).to_be_visible()
        course = page.locator(".map-course").nth(1)
        tab_to(page, course.locator("summary"))
        page.keyboard.press("Enter")
        expect(course.get_by_text("Lulus Demo A", exact=False)).to_be_visible()
        page.keyboard.press("Escape")
        page.set_viewport_size({"width": 360, "height": 800})
        cap = page.get_by_label("Batas SKS personal (opsional)")
        tab_to(page, cap)
        page.keyboard.type("6")
        for course in ("A", "B"):
            tab_to(page, page.get_by_label("Semester rencana Demo " + course))
            page.keyboard.type("1")
        button = page.get_by_role("button", name="Simpan dan hitung rencana")
        tab_to(page, button)
        before = revision(database)

        def drop_ack(route):
            assert route.fetch().ok, "Server did not commit the plan"
            route.abort("failed")

        page.route("**/roadmap/plan", drop_ack)
        page.keyboard.press("Enter")
        expect(page.locator("#save-error")).to_contain_text("Konfirmasi simpan belum diterima")
        expect(cap).to_have_value("6")
        assert revision(database) == before + 1
        page.unroute("**/roadmap/plan")
        tab_to(page, button)
        page.keyboard.press("Enter")
        expect(page.get_by_text("Melebihi batas personal 6 SKS", exact=True)).to_be_visible()
        assert revision(database) == before + 1
        for width in (320, 360, 768, 1280):
            page.set_viewport_size({"width": width, "height": 850})
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), f"Overflow at {width}px"
        print("MAP-T-101/103 passed: keyboard navigation and save, mobile layout, lost acknowledgement and retry.")
        browser.close()


def main():
    with TemporaryDirectory() as folder:
        database = Path(folder) / "browser.sqlite3"
        python = os.environ.get("ORBIT_APP_PYTHON", sys.executable)
        with subprocess.Popen([python, "-c", SERVER], cwd=Path(__file__).resolve().parents[1],
                              env={**os.environ, "ORBIT_DATABASE": str(database)},
                              stdout=subprocess.PIPE, text=True) as server:
            try:
                port = int(server.stdout.readline())
                browser_check(f"http://127.0.0.1:{port}", database)
            finally:
                server.terminate()


if __name__ == "__main__":
    main()
