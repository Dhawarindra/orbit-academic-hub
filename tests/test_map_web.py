import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
from uuid import uuid4

from werkzeug.datastructures import MultiDict

from orbit import create_app
from orbit.domain.roadmap import RoadmapError
from orbit.repositories.sqlite_store import open_database
from orbit.services import academic_roadmap as service, gradebook as book


class RoadmapWorkflowTests(unittest.TestCase):
    base = "http://127.0.0.1:5000"
    version = "orbit-demo-abc-v1"

    def setUp(self):
        self.path = Path(self.enterContext(tempfile.TemporaryDirectory())) / "test.sqlite3"
        self.enterContext(patch.dict(os.environ, {"ORBIT_DATABASE":str(self.path), "ORBIT_PORT":"5000"}))
        self.client = create_app().test_client()

    def get(self, url="/roadmap/"):
        response = self.client.get(url, base_url=self.base)
        self.assertEqual(response.status_code, 200)
        return response.get_data(as_text=True)

    def token(self):
        html = self.get("/grades/new")
        return {k:re.search(f'name="{k}" value="([^"]+)"', html)[1] for k in ("csrf","epoch","revision","operation")}

    def post(self, url, fields=None, status=303, token=None):
        response = self.client.post(url, data={**(token or self.token()), "catalog":self.version, **(fields or {})},
                                    base_url=self.base)
        self.assertEqual(response.status_code, status, response.get_data(as_text=True)[-5000:])
        return response

    def rows(self, sql):
        with open_database(self.path) as db:
            return db.execute(sql).fetchall()

    def view(self):
        with book.snapshot(self.path) as db:
            return service.read(db)

    def activate(self):
        self.post("/roadmap/activate")

    def plan(self, **extra):
        return self.post("/roadmap/plan", dict({"horizon":"4","term_A":"1","term_B":"2","term_C":"3",
                                                "assumed":["A","B"],"delay_course":"A","delay_term":"2"}, **extra))

    def add_grade(self, term="Semester demo"):
        form = dict(name="Demo A", term=term, class_name="X", path="Ujian", weight="100", maximum="100",
                    quantum="1", earned="")
        return self.post("/grades/new", form).location

    def bind(self, grade, status=303):
        self.post("/roadmap/bind", {"enrollment":grade.split("/")[-1],"course":"A"}, status)

    def final(self, grade, outcome, reason=""):
        response = self.post(grade+"/preview", dict(numeric="90",outcome=outcome,note="Lembar sintetis",reason=reason), 200)
        proof = re.search('name="proof" value="([^"]+)"', response.get_data(as_text=True))[1]
        self.post(grade+"/confirm", {"proof":proof})

    def candidate(self, data):
        token = self.token()
        return book.command(self.path, MultiDict(token), "catalog-activate", data["curriculum_id"],
                            lambda db, state: service.activate_catalog(db, data))

    def test_map_t_001_008_opt_in_navigation_catalog_and_restart(self):
        self.assertIn("Academic Roadmap", self.get("/"))
        self.assertIn("Gunakan katalog contoh", self.get())
        self.assertIsNone(self.view()["catalog"])
        self.activate()
        self.client = create_app().test_client()
        html = self.get()
        for text in ["Semester rekomendasi 3","Demo C","4 SKS","Menjadi prasyarat untuk Demo B",
                     "Lulus Demo A", "PRD-02", "Belum diketahui","Memenuhi syarat"]:
            self.assertIn(text, html)
        self.assertEqual(self.rows("PRAGMA user_version"), [(2,)])
        self.assertEqual(self.rows("SELECT COUNT(*) FROM scenario"), [(0,)])

    def test_map_t_002_grade_projection_correction_and_repeat_evidence(self):
        self.activate()
        grade = self.add_grade()
        self.final(grade,"unresolved")
        self.assertEqual(self.view()["credits"]["excluded"], 1)
        self.bind(grade)
        node = self.rows("SELECT node_id FROM assessment_node WHERE kind='leaf'")[0][0]
        self.post(grade+"/simulation", {"score_"+node:"90","sim_target":"90"})
        self.assertEqual(self.view()["reasons"]["B"]["status"], "unknown")
        self.post(grade+"/scores", {"score_"+node:"90"})
        self.assertEqual(self.view()["reasons"]["B"]["status"], "unknown")
        self.final(grade,"passed","Konfirmasi ulang")
        self.assertEqual(self.view()["reasons"]["B"]["status"], "met")
        self.assertEqual(self.view()["reasons"]["C"]["status"], "unknown")
        self.assertEqual(self.view()["credits"]["completed"], 3)
        self.final(grade,"failed","Koreksi hasil")
        self.assertEqual(self.view()["reasons"]["B"]["status"], "unmet")
        repeat = self.add_grade("Semester ulang")
        self.bind(repeat)
        self.final(repeat,"passed")
        view = self.view()
        self.assertEqual(view["reasons"]["B"]["status"], "unknown")
        self.assertIn("kebijakan pengulangan", view["reasons"]["B"]["text"])
        self.assertEqual(view["credits"]["completed"], 0)

    def test_map_t_004_005_persisted_delay_warnings_and_form_errors(self):
        self.activate()
        self.plan()
        self.client = create_app().test_client()
        self.assertEqual(self.view()["timing"], {"A":(2,""),"B":(3,""),"C":(4,"")})
        self.assertIn("Ditunda ke S2", self.get())
        self.post("/roadmap/plan", {"term_A":"1","term_B":"1","cap":"6","horizon":"4"})
        self.assertIn("Melebihi batas personal 6 SKS", self.get())
        self.assertEqual(self.view()["selected"], {"A":1,"B":1})
        for values in [{"term_A":"-2"},{"term_X":"2"},{"delay_course":"C","delay_term":"3"},{"assumed":["A"]},
                       {"choice_fake":"branch"},{"term_A":"1","delay_course":"A","delay_term":"1"}]:
            response = self.post("/roadmap/plan", dict(horizon="4", cap="7", **values), 422)
            self.assertIn('value="7"', response.get_data(as_text=True))
        self.assertEqual(self.view()["plan"]["cap"], 6)
        self.post("/roadmap/plan", {"term_A":"2","horizon":"4","csrf":"wrong"}, 403)
        self.post("/roadmap/plan", {"horizon":"4","catalog":"incorrect"}, 422)

    def test_attempt_binding_rejects_rebinding_and_duplicate_course_term_attempt(self):
        self.activate()
        first = self.add_grade()
        self.bind(first)
        self.bind(first, 422)
        second = self.post("/grades/new", dict(name="Pengambilan lain", term="Semester demo", class_name="Y",
                            path="Ujian", weight="100", maximum="100", quantum="1", earned="")).location
        self.bind(second, 422)
        self.assertEqual(self.rows("SELECT COUNT(*) FROM offering_binding"), [(1,)])
        self.assertEqual(self.view()["credits"]["active"], 3)
        self.assertEqual(self.view()["credits"]["excluded"], 1)

    def test_map_t_006_011_full_shared_reset_after_final(self):
        self.activate()
        grade = self.add_grade()
        self.bind(grade)
        node = self.rows("SELECT node_id FROM assessment_node WHERE kind='leaf'")[0][0]
        self.post(grade+"/simulation", {"score_"+node:"90","sim_target":"75"})
        self.plan()
        old_view = self.view()
        self.assertTrue(json.loads(old_view["scenario"]["score_overlay"]))
        self.post(grade+"/simulation", {"score_"+node:"95","sim_target":"80"})
        self.assertEqual(self.view()["plan"], old_view["plan"])
        self.final(grade,"passed")
        original = self.rows("SELECT * FROM actual_final_revision")
        enrollment = self.rows("SELECT * FROM enrollment")
        view = self.view()
        self.assertTrue(view["stale"])
        self.assertEqual(view["timing"], {})
        self.assertIn("Hasil final", self.get())
        self.assertNotIn('id="hasil"', self.get())
        self.post("/roadmap/plan", {"horizon":"4"}, 409)
        self.post("/roadmap/reset", {}, 422)
        self.post("/roadmap/reset", {"confirm":"yes"})
        for reset_from_grade in [False,True]:
            if reset_from_grade:
                self.plan()
                self.post(grade+"/reset")
            view = self.view()
            self.assertFalse(view["stale"])
            self.assertEqual(view["scenario"]["base_source_revision"], view["state"]["source_revision"])
            self.assertEqual(self.rows("SELECT plan,assumptions,score_overlay,target_overlay FROM scenario"),
                             [("{}","{}","{}","{}")])
            self.assertEqual(self.rows("SELECT * FROM actual_final_revision"), original)
            self.assertEqual(self.rows("SELECT * FROM enrollment"), enrollment)

    def test_map_t_001_007_012_failed_activation_and_immutable_version_binding(self):
        self.activate()
        grade = self.add_grade()
        self.bind(grade)
        self.final(grade,"passed")
        self.plan()
        before = self.rows("SELECT state_revision FROM workspace")
        for rule, code in [(dict(id="cycle",op="passed",course_id="C"), "GRAPH_CYCLE"),
                           (dict(id="missing",op="passed",course_id="Z"), "DANGLING_REFERENCE"),
                           (dict(id="scope",op="passed",course_id="A",curriculum_id=self.version), "SCOPE_MISMATCH")]:
            other = dict(service.demo_catalog(), curriculum_id="other-demo", version="2")
            other["courses"][0]["rule"] = rule
            with self.assertRaisesRegex(RoadmapError,code):
                self.candidate(other)
        conflict = service.demo_catalog()
        conflict["courses"][0]["sks"] = 4
        with self.assertRaisesRegex(RoadmapError,"VERSION_CONFLICT"):
            self.candidate(conflict)
        self.assertEqual(self.rows("SELECT state_revision FROM workspace"), before)
        self.assertEqual(self.view()["catalog"].meta["curriculum_id"], self.version)
        other = dict(service.demo_catalog(),curriculum_id="other-demo",version="2")
        other["courses"][0]["sks"] = 4
        self.candidate(other)
        view = self.view()
        self.assertTrue(view["stale"])
        self.assertEqual(view["catalog"].courses["A"]["sks"], 4)
        self.assertEqual(view["credits"]["excluded"], 1)
        self.assertEqual(view["reasons"]["B"]["status"], "unknown")
        self.assertEqual(self.rows("SELECT curriculum_id FROM offering_binding"), [(self.version,)])

    def test_map_t_009_008_other_supported_catalogs_render_nested_and_unsupported_reasons(self):
        data = service.demo_catalog()
        data["courses"][2]["rule"] = dict(id="option",op="or",children=[
            dict(id="pass-A",op="passed",course_id="A"),
            dict(id="special",op="unsupported",raw="Izin pengajar",reason="Belum diverifikasi",refs=[])])
        self.candidate(data)
        self.assertIn("Izin pengajar", self.get())
        self.plan(choice_option="pass-A")
        self.assertEqual(self.view()["timing"]["C"][0], 3)
        self.plan(choice_option="special")
        self.assertIsNone(self.view()["timing"]["C"][0])
        self.assertIn("Izin pengajar", self.get())

    def test_catalog_file_reports_all_reference_errors_and_preserves_active_version(self):
        self.activate()
        runner = create_app().test_cli_runner()
        path = self.path.with_suffix(".json")
        candidate = dict(service.demo_catalog(), curriculum_id="other", version="2")
        a, b, _ = candidate["courses"]
        a["rule"] = dict(id="absent", op="passed", course_id="Z")
        b["rule"]["curriculum_id"] = self.version
        path.write_text(json.dumps(candidate))
        result = runner.invoke(args=["roadmap","activate-catalog",str(path)])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("DANGLING_REFERENCE", result.output)
        self.assertIn("SCOPE_MISMATCH", result.output)
        self.assertEqual(self.view()["catalog"].meta["curriculum_id"], self.version)
        a["rule"] = None
        del b["rule"]["curriculum_id"]
        b.update(category="Contoh", source_ref="Lampiran sintetis", rule_version="khusus-2")
        path.write_text(json.dumps(candidate))
        result = runner.invoke(args=["roadmap","activate-catalog",str(path)])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("Lampiran sintetis · Aturan khusus-2 · Contoh", self.get())

    def test_map_t_103_replay_lost_ack_and_rollback_partial_write(self):
        self.activate()
        token = self.token()
        fields = {"term_A":"1","cap":"6","horizon":"4"}
        rev = self.view()["state"]["state_revision"]
        for _ in range(2):
            self.post("/roadmap/plan",fields,token=token)
        self.assertEqual(self.view()["state"]["state_revision"], rev+1)
        self.post("/roadmap/plan",dict(fields,cap="7"),409,token=token)
        self.post("/roadmap/plan",fields,409,token=dict(token,operation=uuid4().hex))
        def fail(db, state, form, catalog):
            book.save_scenario(db,state,{"plan":{"partial":True}})
            raise sqlite3.OperationalError("injected write failure")
        with patch.object(service,"save_plan",fail):
            response = self.post("/roadmap/plan", dict(fields,cap="8"),503)
        self.assertIn('value="8"', response.get_data(as_text=True))
        self.assertEqual(self.view()["plan"]["cap"], 6)
        self.assertEqual(self.view()["state"]["state_revision"], rev+1)

    def test_v1_migration_preserves_existing_grade_history_and_identity(self):
        # Construct the exact on-disk v1 schema to exercise an upgrade on restart.
        legacy = self.path.with_name("legacy.sqlite3")
        schema = Path(book.__file__).parents[1] / "repositories" / "grades.sql"
        with open_database(legacy) as db:
            db.executescript(schema.read_text())
            db.execute("INSERT INTO workspace(singleton,owner_scope,epoch) VALUES(1,'owner','epoch')")
            db.execute("INSERT INTO academic_term VALUES('t','Term',1)")
            db.execute("INSERT INTO offering VALUES('o','owner','t','Demo A','','{}')")
            db.execute("INSERT INTO enrollment(enrollment_id,offering_id,owner_scope,attempt_key,source) "
                       "VALUES('e','o','owner','o:1','{}')")
            db.execute("INSERT INTO actual_final_revision(final_revision_id,enrollment_id,revision_no,outcome,"
                       "source,committed_revision) VALUES('f','e',1,'passed','{}',1)")
            db.execute("PRAGMA user_version=1")
            history = db.execute("SELECT * FROM actual_final_revision").fetchall()
        with patch.dict(os.environ, {"ORBIT_DATABASE":str(legacy)}):
            create_app()
        with open_database(legacy) as db:
            self.assertEqual(db.execute("SELECT * FROM actual_final_revision").fetchall(), history)
            self.assertEqual(db.execute("SELECT owner_scope,epoch,schema_version FROM workspace").fetchone(), ("owner","epoch",2))
            self.assertEqual(db.execute("SELECT COUNT(*) FROM offering_binding").fetchone(), (0,))
            self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])
