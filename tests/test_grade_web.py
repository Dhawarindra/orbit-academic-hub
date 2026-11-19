import os
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from uuid import uuid4

from orbit import create_app
from orbit.repositories.sqlite_store import open_database
from test_grade_domain import grade_rows


class GradeWorkflowTests(unittest.TestCase):
    base = "http://127.0.0.1:5000"

    def setUp(self):
        folder = self.enterContext(tempfile.TemporaryDirectory())
        self.path = Path(folder) / "test.sqlite3"
        self.enterContext(patch.dict(os.environ, {"ORBIT_DATABASE": str(self.path), "ORBIT_PORT": "5000"}))
        self.client = create_app().test_client()
        self.url = "/grades/new"

    def tokens(self):
        html = self.client.get(self.url, base_url=self.base).get_data(as_text=True)
        fields = {k: re.search(f'name="{k}" value="([^"]+)"', html)[1] for k in ("csrf", "epoch", "revision")}
        return dict(fields, operation=uuid4().hex)

    def post(self, url, data, status=303, *, token=None):
        response = self.client.post(url, data={**(token or self.tokens()), **data}, base_url=self.base)
        self.assertEqual(response.status_code, status, response.get_data(as_text=True)[:5000])
        return response

    def rows(self, sql):
        with open_database(self.path) as db:
            return db.execute(sql).fetchall()

    def add_course(self, scored=True, policy="demo"):
        rows = grade_rows()
        if not scored:
            for r in rows:
                r["earned"] = ""
        fields = {k:[r[k] for r in rows] for k in rows[0]}
        data = dict(name="Sampel", term="Ganjil demo", class_name="A", policy=policy, **fields)
        self.url = self.post("/grades/new", data).location
        return data

    def scores(self, uas):
        return {"score_"+n: uas if label == "UAS" else "" for n,label in self.rows(
            "SELECT node_id,label FROM assessment_node WHERE kind='leaf' AND brp_id IN "
            "(SELECT brp_id FROM brp_version WHERE status='active')")}

    def test_grd_t_001_atomic_structure_versions_and_permanent_lock(self):
        data = self.add_course(scored=False)
        self.post(self.url + "/structure", data)
        self.assertEqual(self.rows("SELECT version_no,status FROM brp_version ORDER BY version_no"),
                         [(1,"superseded"), (2,"active")])
        self.post(self.url + "/scores", self.scores("0"))
        self.post(self.url + "/scores", self.scores(""))
        self.post(self.url + "/structure", data, 409)
        self.assertEqual(self.rows("SELECT locked FROM brp_version WHERE status='active'"), [(1,)])
        self.assertEqual(self.rows("SELECT count(*) FROM brp_version"), [(2,)])

    def test_invalid_form_preserves_draft_and_rolls_back(self):
        rows = grade_rows()
        rows[0]["weight"] = "21"
        data = {k:[r[k] for r in rows] for k in rows[0]}
        response = self.post(self.url, dict(data,name="Keep this",term="Ganjil"), 422)
        html = response.get_data(as_text=True)
        self.assertIn("Keep this", html)
        self.assertIn("101,00%", html)
        self.assertEqual(self.rows("SELECT count(*) FROM enrollment"), [(0,)])
        self.assertEqual(self.rows("SELECT state_revision FROM workspace"), [(0,)])

    def test_grd_t_011_simulation_survives_restart_without_changing_actual(self):
        self.add_course()
        scores_before = self.rows("SELECT * FROM assessment_score ORDER BY node_id")
        self.post(self.url + "/target", {"target":"75"})
        self.post(self.url + "/simulation", dict(self.scores("90"), sim_target="90"))
        self.client = create_app().test_client()
        html = self.client.get(self.url, base_url=self.base).get_data(as_text=True)
        for text in ("36,00–86,00", "81,00–81,00", "78,00%", "Target tidak tercapai"):
            self.assertIn(text, html)
        self.assertEqual(self.rows("SELECT * FROM assessment_score ORDER BY node_id"), scores_before)
        self.assertEqual(self.rows("SELECT count(*) FROM actual_final_revision"), [(0,)])
        self.assertEqual(self.rows("SELECT numeric_target FROM course_target"), [("75",)])
        self.post(self.url + "/target", {"target":"A"})
        self.post(self.url + "/simulation", self.scores("89"), 409)
        self.post(self.url + "/reset", {})
        self.assertEqual(self.rows("SELECT score_overlay,target_overlay FROM scenario"), [("{}", "{}")])

    def test_score_form_rejects_bad_batch_and_foreign_node(self):
        self.add_course()
        before = self.rows("SELECT * FROM assessment_score ORDER BY node_id")
        self.post(self.url + "/scores", self.scores("101"), 422)
        self.post(self.url + "/scores", dict(self.scores("50"), score_foreign="99"), 422)
        self.assertEqual(self.rows("SELECT * FROM assessment_score ORDER BY node_id"), before)

    def test_grd_t_010_preview_correction_history_and_replay(self):
        self.add_course()
        fields = dict(numeric="84.995", letter="B", outcome="unresolved", note="Lembar demo")
        def preview(data):
            response = self.post(self.url + "/preview", data, 200)
            return re.search('name="proof" value="([^"]+)"', response.get_data(as_text=True))[1]
        proof = preview(fields)
        self.assertEqual(self.rows("SELECT count(*) FROM actual_final_revision"), [(0,)])
        self.post(self.url + "/target", {"target":"75"})
        self.post(self.url + "/confirm", {"proof":proof}, 409)
        proof = preview(fields)
        original = self.tokens()
        for _ in range(2):
            self.post(self.url + "/confirm", {"proof":proof}, token=original)
        self.post(self.url + "/confirm", {"proof":"edited"}, 422)
        self.post(self.url + "/preview", fields, 422)
        self.post(self.url + "/preview", dict(fields,letter="A",reason="Koreksi"), 422)
        correction = preview(dict(fields,numeric="85",letter="A",reason="Lembar diperbarui"))
        self.post(self.url + "/confirm", {"proof":correction})
        self.assertEqual(self.rows("SELECT revision_no,numeric_value,letter_value,outcome,correction_reason "
                                   "FROM actual_final_revision ORDER BY revision_no"),
                         [(1,"84.995","B","unresolved",None), (2,"85","A","unresolved","Lembar diperbarui")])

    def test_policy_scope_and_stale_or_forged_submission(self):
        self.add_course(policy="")
        token = self.tokens()
        self.post(self.url + "/target", {"target":"A", "csrf":"invalid"}, 403, token=token)
        self.post(self.url + "/target", {"target":"A"}, token=token)
        html = self.client.get(self.url, base_url=self.base).get_data(as_text=True)
        self.assertIn("Kebijakan huruf belum tersedia", html)
        self.post(self.url + "/target", {"target":"70"}, 409, token=token)
        self.post(self.url + "/target", {"target":"70"}, 409, token=dict(token,operation=uuid4().hex))
        self.assertEqual(self.rows("SELECT numeric_target,letter_target FROM course_target"), [(None,"A")])
