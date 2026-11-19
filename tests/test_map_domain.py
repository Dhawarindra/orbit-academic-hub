import copy
from itertools import combinations, product
from time import perf_counter
import unittest

from orbit.domain import roadmap as m
from orbit.services.academic_roadmap import demo_catalog


def leaf(course, node=None):
    return dict(id=node or "pass-" + course, op="passed", course_id=course)


def group(op, *children):
    return dict(id="group-" + op, op=op, children=list(children))


def attempt(outcome):
    return m.Attempt("enrollment-" + str(outcome), outcome, 1 if outcome else None, "Demo", True)


def simulation(candidate=None, *, passed=("A", "B"), choices=None, evidence=None, horizon=4):
    catalog = m.validate_catalog(candidate or demo_catalog())
    return m.simulate(catalog, evidence or {}, {"A": 1, "B": 2, "C": 3},
                      dict(horizon=horizon, passed=passed, choices=choices or {}, delay={"A": 2}))


class RoadmapDomainTests(unittest.TestCase):
    def test_map_t_003_all_truth_table_pairs_and_complete_reasons(self):
        outcomes = ("passed", "failed", None)
        expected = {"and": ("met","unmet","unknown","unmet","unmet","unmet","unknown","unmet","unknown"),
                    "or": ("met","met","met","met","unmet","unknown","met","unknown","unknown")}
        for op, (index, pair) in product(expected, enumerate(product(outcomes, repeat=2))):
            a, b = pair
            with self.subTest(op=op, a=a, b=b):
                result = m.evaluate(group(op, leaf("A"), leaf("B")), {"A":[attempt(a)], "B":[attempt(b)]}, "demo")
                self.assertEqual(result["status"], expected[op][index])
                self.assertEqual([c["id"] for c in result["children"]], ["pass-A", "pass-B"])

    def test_map_t_003_nested_known_failed_and_unknown(self):
        rule = group("and", leaf("A"), group("or", leaf("B"), leaf("C")))
        result = m.evaluate(rule, {"A":[attempt("passed")], "B":[attempt("failed")]}, "demo")
        self.assertEqual(result["status"], "unknown")
        self.assertEqual(result["children"][0]["status"], "met")
        self.assertEqual([c["status"] for c in result["children"][1]["children"]], ["unmet","unknown"])

    def test_map_t_002_repeated_attempts_and_incomplete_results(self):
        for outcomes, expected in [([], "unknown"), ([None], "unknown"), (["unresolved"], "unknown"),
                                   (["passed","passed"], "met"), (["failed","passed"], "unknown")]:
            with self.subTest(outcomes=outcomes):
                result = m.evaluate(leaf("A"), {"A":[attempt(o) for o in outcomes]}, "demo")
                self.assertEqual(result["status"], expected)
                self.assertEqual(len(result["attempts"]), len(outcomes))
        self.assertEqual(m.evaluate(None, {}, "demo")["status"], "unknown")

    def test_map_t_004_credit_categories_coverage_and_personal_cap(self):
        catalog = m.validate_catalog(demo_catalog())
        evidence = {"C":[attempt("passed"),attempt("passed")], "A":[attempt(None)]}
        result = m.credits(catalog, evidence, {"A":1,"B":1}, 6, 2)
        self.assertEqual(result, dict(completed=3, active=3, totals={1:7}, excluded=2, over={1}))
        self.assertFalse(m.credits(catalog, evidence, {"A":1,"B":1}, None, 0)["over"])

    def test_map_t_005_golden_delay_and_explicit_assumptions(self):
        self.assertEqual(simulation(), {"A":(2,""),"B":(3,""),"C":(4,"")})
        self.assertIsNone(simulation(passed=())["B"][0])
        self.assertEqual(simulation(evidence={"A":[attempt("passed")]})["B"], (2, ""))

    def test_ddp_t_013_availability_and_horizon(self):
        catalog = demo_catalog()
        b = catalog["courses"][1]
        for avail, horizon, expected in [("unknown",4,None),("even",5,4),("odd",4,3),([4],5,4),([6],4,None)]:
            b["availability"] = avail
            timing = simulation(catalog, horizon=horizon)
            self.assertEqual(timing["B"][0], expected)
            self.assertEqual(timing["C"][0], expected+1 if expected and expected < horizon else None)
            if not expected:
                self.assertIn("penawaran" if avail == "unknown" else "slot", timing["C"][1])

    def test_ddp_t_013_and_waits_for_latest_or_needs_an_explicit_choice(self):
        candidate = demo_catalog()
        candidate["courses"][2]["rule"] = group("and", leaf("A"), group("or", leaf("B"), leaf("A","alt-A")))
        self.assertIsNone(simulation(candidate)["C"][0])
        self.assertEqual(simulation(candidate, choices={"group-or":"pass-B"})["C"][0], 4)
        self.assertEqual(simulation(candidate, choices={"group-or":"alt-A"})["C"][0], 3)

    def test_map_t_007_cycles_include_unselected_branches_and_exclude_blocked_courses(self):
        for rule, expected in [(leaf("A"), r"A → A"), (group("or", leaf("B"), leaf("C")), "GRAPH_CYCLE")]:
            candidate = demo_catalog()
            candidate["courses"][0]["rule"] = rule
            with self.assertRaisesRegex(m.RoadmapError, expected):
                m.validate_catalog(candidate)
        candidate["courses"][0]["rule"] = leaf("B")
        with self.assertRaisesRegex(m.RoadmapError, "A → B → A") as caught:
            m.validate_catalog(candidate)
        self.assertNotIn("C →", str(caught.exception))
        candidate["courses"][0]["rule"] = candidate["courses"][2]["rule"] = None
        self.assertCountEqual(m.validate_catalog(candidate).order, ["A","B","C"])

    def test_map_t_009_unsupported_rules_keep_raw_refs_and_unknown_time(self):
        candidate = demo_catalog()
        rule = {"id":"permit","op":"unsupported","raw":"Izin pengajar","reason":"Izin belum terverifikasi","refs":["A"]}
        candidate["courses"][1]["rule"] = rule
        result = m.evaluate(rule, {"A":[attempt("passed")]}, "Demo")
        self.assertEqual(result["status"], "unknown")
        self.assertIn("Izin pengajar", result["text"])
        self.assertIn("Izin belum terverifikasi", result["text"])
        self.assertEqual(m.validate_catalog(candidate).dependencies["B"], {"A"})
        self.assertIsNone(simulation(candidate)["C"][0])

    def test_map_t_012_broken_refs_metadata_and_schema(self):
        invalid = [("rule",leaf("Z"),"DANGLING_REFERENCE"),("rule",dict(leaf("A"),curriculum_id="else"),"SCOPE_MISMATCH"),
                   ("sks",True,"SKS"), ("sks",0,"SKS"), ("recommended",0,"semester"), ("availability",[0],"penawaran"),
                   ("rule",group("and"),"kosong"), ("rule",group("and",leaf("A"),leaf("A")),"terpakai"),
                   ("rule",dict(id="none",op="none"),"sumber"),("id","A","ganda")]
        for key, value, error in invalid:
            with self.subTest(key=key, error=error):
                candidate = demo_catalog()
                candidate["courses"][1][key] = value
                with self.assertRaisesRegex(m.RoadmapError, error):
                    m.validate_catalog(candidate)
        candidate = demo_catalog()
        candidate["is_synthetic"] = False
        with self.assertRaisesRegex(m.RoadmapError, "sintetis"):
            m.validate_catalog(candidate)

    def test_map_t_102_validate_100_courses_300_edges(self):
        base = demo_catalog()
        nodes = [dict(id=str(i),label=f"Benchmark {i}",sks=1,rule=None) for i in range(100)]
        # Span all 100 courses, then add distinct forward edges.
        edges = [(i-1, i) for i in range(1, 100)]
        edges += [(a,b) for a,b in combinations(range(100),2) if b-a>1][:201]
        for parent, child in edges:
            if nodes[child]["rule"] is None:
                nodes[child]["rule"] = dict(id=f"group-{child}", op="and", children=[])
            nodes[child]["rule"]["children"].append(leaf(str(parent),f"edge-{parent}-{child}"))
        base["courses"] = nodes
        self.assertEqual(sum(map(len, m.validate_catalog(base).dependencies.values())), 300)
        cyclic = copy.deepcopy(base)
        cyclic["courses"][0]["rule"] = leaf("99","back")
        # Keep the chain to 99 intact and remove a redundant forward edge instead.
        cyclic["courses"][2]["rule"]["children"].pop()
        for name, candidate in [("DAG",base),("cycle",cyclic)]:
            durations = []
            for _ in range(30):
                start = perf_counter()
                if name == "DAG":
                    m.validate_catalog(candidate)
                else:
                    with self.assertRaisesRegex(m.RoadmapError, "GRAPH_CYCLE"):
                        m.validate_catalog(candidate)
                durations.append((perf_counter() - start)*1000)
            p95 = sorted(durations)[28]
            print(f"MAP-T-102 {name}: 100/300 · n=30 · p95 {p95:.3f} ms")
            self.assertLessEqual(p95, 300)
