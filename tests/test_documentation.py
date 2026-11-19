"""Exercise CORE-T-008 with a real scope decision in the v0.2.1 baseline."""

import unittest
from pathlib import Path


GOVERNANCE = (Path(__file__).resolve().parents[1] / "ORBIT_PRD_v0.2.1"
              / "docs" / "00-governance")


class TraceabilityTests(unittest.TestCase):
    def test_core_t_008_stale_scenario_decision_maps_to_original_test(self):
        def decision_row(filename, row_id):
            document = (GOVERNANCE / filename).read_text(encoding="utf-8")
            rows = [line for line in document.splitlines() if line.startswith(f"| {row_id} |")]
            self.assertEqual(len(rows), 1, f"{filename} must contain one row for {row_id}")
            return rows[0]

        decision = decision_row("GLOSSARY-AND-DECISION-LOG.md", "D-21")
        self.assertIn("MAP-FR-006", decision)
        change = decision_row("PRD-REVISION-CHANGELOG.md", "MAP-FR-006")
        self.assertIn("D-21", change)
        self.assertIn("P2", change)
        mapping = decision_row("REQUIREMENTS-TRACEABILITY-MATRIX.md", "MAP-FR-006")
        for reference in ("| P0 |", "MAP-AC-006", "MAP-T-006"):
            self.assertIn(reference, mapping)
