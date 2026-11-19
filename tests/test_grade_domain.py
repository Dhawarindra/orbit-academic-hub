import unittest
from decimal import Decimal
from fractions import Fraction

from orbit.domain.grades import (
    InvalidInput, classify, decimal_input, display, parse_target, solve_target, summarize, validate_structure,
)


def grade_rows():
    headings = ("path", "weight", "maximum", "quantum", "earned")
    data = [
        ("Kuis", "20", "", "", ""),
        ("Kuis / Q1", "50", "100", "1", "80"),
        ("Kuis / Q2", "50", "100", "1", "100"),
        ("UTS", "30", "100", "1", "60"),
        ("UAS", "50", "100", "1", ""),
    ]
    return [dict(zip(headings, values)) for values in data]


class GradeDomainTests(unittest.TestCase):
    def test_grd_t_002_nested_weights(self):
        items = validate_structure(grade_rows())
        self.assertEqual({i.path: i.effective * 100 for i in items if i.maximum},
                         {"Kuis / Q1": 10, "Kuis / Q2": 10, "UTS": 30, "UAS": 50})

    def test_invalid_weights_duplicate_paths_and_missing_parents(self):
        for index, key, bad in [(0, "weight", "19.99"), (1, "weight", "50.01"), (1, "path", "Kuis"),
                                (4, "path", "Proyek / UAS"), (0, "maximum", "100")]:
            with self.subTest(bad=bad):
                rows = grade_rows()
                rows[index][key] = bad
                with self.assertRaises(InvalidInput):
                    validate_structure(rows)

    def test_grd_t_003_014_unknown_and_zero(self):
        rows = grade_rows()
        for row in rows:
            row["earned"] = ""
        empty = summarize(validate_structure(rows))
        self.assertEqual((empty.known, empty.upper, empty.average), (0, 100, None))
        rows[-1]["earned"] = "0"
        zero = summarize(validate_structure(rows))
        self.assertEqual((zero.observed_weight, zero.average, zero.upper), (Fraction(1, 2), 0, 50))

    def test_grd_t_004_005_006_partial_bounds_and_targets(self):
        stats = summarize(validate_structure(grade_rows()))
        self.assertEqual((stats.known, stats.observed_weight, stats.average, stats.upper),
                         (36, Fraction(1, 2), 72, 86))
        self.assertEqual(solve_target(stats, 75, None, None)["minimum"], 78)
        result = solve_target(stats, 90, None, None)
        self.assertEqual((result["required"], result["status"]), (108, "Tidak dapat dicapai"))
        self.assertLessEqual(solve_target(stats, 30, None, None)["required"], 0)

    def test_grd_t_007_zero_remaining_weight(self):
        rows = grade_rows()
        rows[-1]["earned"] = "78"
        stats = summarize(validate_structure(rows))
        self.assertEqual(stats.known, 75)
        self.assertEqual(solve_target(stats, 75, None, None)["status"], "Target tercapai")
        self.assertEqual(solve_target(stats, 80, None, None)["status"], "Target tidak tercapai")
        self.assertIsNone(solve_target(stats, 80, None, None)["required"])

    def test_grd_t_012_016_thresholds_and_ceiling(self):
        rows = grade_rows()
        for quantum, minimum in [("1", 79), ("0,01", Fraction(7802, 100))]:
            rows[-1]["quantum"] = quantum
            stats = summarize(validate_structure(rows))
            self.assertEqual(solve_target(stats, Decimal("75.01"), None, None)["minimum"], minimum)
        boundary = Decimal("84.995")
        policy = {"A": 85, "B": 70, "C": 0}
        self.assertEqual((display(boundary), classify(boundary, policy), classify(85, policy)), ("85,00", "B", "A"))
        self.assertIsNone(solve_target(stats, *parse_target("A"), None)["required"])
        self.assertEqual(solve_target(stats, *parse_target("A"), policy)["required"], 98)

    def test_multi_component_target_is_average_and_granularity_can_be_unattainable(self):
        rows = grade_rows()
        rows[1]["earned"] = ""
        result = solve_target(summarize(validate_structure(rows)), 75, None, None)
        self.assertNotIn("minimum", result)
        rows = grade_rows()
        rows[-1]["quantum"] = "3"
        result = solve_target(summarize(validate_structure(rows)), 86, None, None)
        self.assertEqual(result["status"], "Tidak tercapai pada langkah skor ini")

    def test_grd_t_018_rejects_numeric_errors(self):
        for field, value in [("maximum","0"), ("earned","101"), ("earned","-1"), ("earned","NaN"),
                             ("weight","Infinity"), ("quantum","0"), ("weight","50.001")]:
            with self.subTest(field=field, value=value):
                rows = grade_rows()
                rows[-1][field] = value
                with self.assertRaises(InvalidInput):
                    validate_structure(rows)
        for value in ("101", "-1", "1,000.5", "1e3", "0.1234567890123"):
            with self.subTest(target=value), self.assertRaises(InvalidInput):
                parse_target(value)
        self.assertEqual(decimal_input("0,125", "Nilai"), Decimal(".125"))
