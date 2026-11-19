import json
import re
import sqlite3
from unittest.mock import patch

from werkzeug.datastructures import MultiDict

from orbit import create_app
from orbit.repositories.sqlite_store import open_database
from orbit.services import academic_roadmap, gradebook
from test_grade_domain import grade_rows
from test_map_web import OrbitWorkflowCase


class DashboardTests(OrbitWorkflowCase):
    def example_grade(self):
        rows = grade_rows()
        form = {key: [r[key] for r in rows] for key in rows[0]}
        return self.post("/grades/new", dict(name="Contoh terintegrasi", term="Ganjil uji", **form)).location

    def summary_status(self, page, course):
        row = re.search(r'prasyarat-' + course + r'">[^<]+</a>\s*<span class="map-status [^"]+">([^<]+)', page)
        self.assertIsNotNone(row, f"Missing eligibility result for {course}")
        return row[1]

    def test_core_t_007_empty_no_implicit_writes_or_dependency_on_optional_modules(self):
        for route in ("/", "/dashboard", "/dashboard/"):
            html = self.get(route)
            self.assertIn("Ringkasan akademik", html)
            self.assertIn("Belum ada pengambilan", html)
            self.assertIn("Katalog belum dipilih", html)
            for feature in ("IPK", "Stress Radar", "Senior Playbook"):
                self.assertNotIn(feature, html)
        self.assertEqual(self.rows("SELECT state_revision,source_revision FROM workspace"), [(0, 0)])
        for table in ("scenario", "enrollment", "curriculum_snapshot", "actual_final_revision"):
            self.assertEqual(self.rows("SELECT COUNT(*) FROM " + table), [(0,)])

    def test_ux_t_002_exact_grade_summary_targets_and_hypothetical_evidence(self):
        self.activate()
        grade = self.example_grade()
        self.bind(grade)
        self.post(grade+"/target", {"target":"75"})
        scores = {"score_"+key: "90" if label == "UAS" else "" for key,label in self.rows(
            "SELECT node_id,label FROM assessment_node WHERE kind='leaf'")}
        self.post(grade+"/simulation", dict(scores, sim_target="88"))
        html = self.get("/")
        for text in ("36,00 poin", "50,00%", "72,00", "36,00–86,00", "Rerata sisa 78,00%",
                     "81,00–81,00", "Target simulasi 88", "Target tidak tercapai", "Belum dikonfirmasi"):
            self.assertIn(text, html)
        for text in ("36,00–86,00", "81,00–81,00", "78,00%"):
            self.assertIn(text, self.get(grade))
        self.assertEqual(self.summary_status(html,"B"), "Belum diketahui")
        self.assertEqual(self.rows("SELECT COUNT(*) FROM actual_final_revision"), [(0,)])
        self.post(grade+"/target", {"target":"90"})
        html = self.get("/")
        self.assertIn("Tidak dapat dicapai", html)
        self.assertIn(grade+"#target", html)
        self.assertNotIn("81,00–81,00", html)

    def test_core_t_002_confirm_correct_restart_and_stale_revision(self):
        self.activate()
        grade = self.add_grade()
        self.bind(grade)
        self.plan()
        self.assertIn("Paling awal S4", self.get("/"))
        self.final(grade, "passed")
        html = self.get("/")
        self.assertEqual(self.summary_status(html,"B"), "Memenuhi syarat")
        self.assertEqual(self.summary_status(html,"C"), "Belum diketahui")
        self.assertIn("Dikonfirmasi pengguna · r1 · Lembar sintetis", html)
        self.assertIn("Sumber skenario berubah", html)
        self.assertNotIn("Paling awal S4", html)
        self.final(grade, "failed", "Koreksi sintetis")
        self.client = create_app().test_client()
        html = self.get("/dashboard/")
        self.assertEqual(self.summary_status(html,"B"), "Belum memenuhi syarat")
        self.assertIn("Dikonfirmasi pengguna · r2 · Lembar sintetis", html)
        self.post("/roadmap/reset", {"confirm":"yes"})
        html = self.get("/")
        self.assertNotIn("Sumber skenario berubah", html)
        self.assertIn("Belum ada pilihan semester", html)
        self.assertEqual(self.summary_status(html,"B"), "Belum memenuhi syarat")

    def test_plan_and_projected_sks_warnings_use_roadmap_results(self):
        self.activate()
        # B1 and C1 have unknown timing. The planned warning still applies.
        self.post("/roadmap/plan", {"horizon":"4","term_B":"1","term_C":"1","cap":"6"})
        html = self.get("/")
        self.assertIn("Semester 1 · 7 SKS melebihi batas personal 6 SKS", html)
        self.assertIn("Waktu belum diketahui", html)
        self.assertIn("memerlukan hasil lulus", html)
        self.assertIn("#hasil", html)
        self.plan(cap="3")
        html = self.get("/")
        self.assertIn("Setelah simulasi, semester 3 memuat 4 SKS", html)
        self.assertIn("Demo B · Paling awal S3", html)
        self.assertEqual(self.summary_status(html,"B"), "Belum diketahui")

    def test_missing_scores_recorded_zero_and_unresolved_letter_policy(self):
        grade = self.add_grade()
        page = self.get("/")
        self.assertIn("0,00–100,00", page)
        self.assertIn("Rerata teramati</dt><dd>Belum tersedia", page)
        self.post(grade+"/target", {"target":"A"})
        self.assertIn("Kebijakan huruf belum tersedia", self.get("/"))
        key = self.rows("SELECT node_id FROM assessment_node WHERE kind='leaf'")[0][0]
        self.post(grade+"/scores", {"score_"+key:"0"})
        page = self.get("/")
        self.assertIn("0,00–0,00", page)
        self.assertIn("Rerata teramati</dt><dd>0,00", page)
        self.assertIn("100,00%", page)

    def test_grade_only_scenario_identifies_changed_sources_without_catalog(self):
        grade = self.add_grade()
        key = self.rows("SELECT node_id FROM assessment_node WHERE kind='leaf'")[0][0]
        self.post(grade+"/simulation", {"score_"+key:"99"})
        self.assertIn("99,00–99,00", self.get("/"))
        self.post(grade+"/scores", {"score_"+key:"81"})
        page = self.get("/")
        for text in ("Sumber skenario berubah","Skor aktual",grade+"#simulasi","81,00–81,00"):
            self.assertIn(text, page)
        self.assertNotIn("99,00–99,00", page)

    def test_ux_t_001_term_scope_survives_module_navigation_and_new_enrollment(self):
        self.activate()
        first = self.add_grade("Periode pertama")
        second = self.add_grade("Periode kedua")
        self.bind(first)
        self.final(first,"passed")
        term_id = self.rows("SELECT term_id FROM academic_term WHERE label='Periode kedua'")[0][0]
        query = "?term_id=" + term_id
        page = self.get("/"+query)
        self.assertNotIn(first+"?", page)
        self.assertIn(second+query, page)
        self.assertEqual(self.summary_status(page,"B"), "Memenuhi syarat")
        for route in ("/grades/"+query, "/roadmap"+query, second+query):
            self.assertIn('href="/'+query+'"', self.get(route))
        self.assertIn('value="Periode kedua"', self.get("/grades/new"+query))
        missing = self.client.get("/?term_id=absent", base_url=self.base)
        self.assertEqual(missing.status_code,404)
        self.assertIn("Tampilkan semua periode",missing.get_data(as_text=True))

    def test_core_t_004_missing_source_and_invalid_catalog_leave_grades_readable(self):
        self.activate()
        self.add_grade()
        with open_database(self.path) as db:
            db.execute("UPDATE curriculum_course SET prerequisite=json_set(prerequisite,'$.source_ref','') "
                       "WHERE course_id='B'")
        html = self.get("/")
        self.assertIn("Demo B · NEEDS_VALIDATION", html)
        self.assertIn("#prasyarat-B", html)
        with open_database(self.path) as db:
            db.execute("UPDATE curriculum_snapshot SET source=?", (json.dumps({"is_synthetic": True}),))
        html = self.get("/")
        self.assertIn("NEEDS_VALIDATION",html)
        self.assertIn("0,00–100,00", html)
        self.assertNotIn("map-status met",html)

    def test_missing_brp_retains_enrollment_and_links_to_recoverable_editor(self):
        grade = self.add_grade()
        self.final(grade, "unresolved")
        with open_database(self.path) as db:
            db.execute("UPDATE brp_version SET status='superseded'")
        page = self.get("/")
        self.assertIn("Struktur penilaian belum tersedia", page)
        self.assertIn("Kelulusan belum diketahui", page)
        self.assertNotIn("0,00–100,00", page)
        self.assertIn('name="weight" value="50"', self.get(grade+"/structure"))
        self.post(grade+"/structure", dict(path="Tes",weight="100",maximum="100",quantum="1",earned=""))
        self.assertIn("0,00–100,00", self.get("/"))

    def test_atomic_read_during_concurrent_final_commit(self):
        self.activate()
        grade = self.add_grade()
        self.bind(grade)
        enrollment = grade.split("/")[-1]
        with open_database(self.path) as db:
            db.execute("PRAGMA journal_mode=WAL")
        token = MultiDict(self.token())
        read_roadmap = academic_roadmap.read

        def interleave(db, context):
            def writer(other, state):
                gradebook.confirm_final(other, state, gradebook.course(other,enrollment),
                                        dict(outcome="passed", note="Demo serentak"))
                return enrollment
            gradebook.command(self.path, token, "confirm", enrollment, writer)
            return read_roadmap(db, context)

        with patch.object(academic_roadmap, "read", interleave):
            before = self.get("/")
        self.assertIn("Belum dikonfirmasi",before)
        self.assertEqual(self.summary_status(before,"B"), "Belum diketahui")
        after = self.get("/")
        self.assertIn("Demo serentak",after)
        self.assertEqual(self.summary_status(after,"B"), "Memenuhi syarat")

    def test_sqlite_read_failure_shows_retry_and_recovers(self):
        with patch.object(gradebook, "courses", side_effect=sqlite3.OperationalError("private diagnostic")):
            response = self.client.get("/", base_url=self.base)
        self.assertEqual(response.status_code,503)
        html = response.get_data(as_text=True)
        self.assertIn("Muat ulang Dashboard", html)
        self.assertNotIn("private diagnostic",html)
        self.assertIn("Ringkasan akademik",self.get("/"))
