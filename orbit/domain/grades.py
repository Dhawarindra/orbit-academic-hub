"""Exact calculations for a linear assessment plan. No web or storage dependencies."""

import re
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from math import ceil


class InvalidInput(ValueError):
    """A message suitable for the person editing the form."""


def decimal_input(raw, field, *, maximum=None, positive=False, places=12):
    raw = raw.strip().replace(",", ".")
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", raw) or len(raw.replace(".", "").lstrip("0")) > 24:
        raise InvalidInput(f"{field}: gunakan angka positif atau nol, hingga 24 digit.")
    value = Decimal(raw)
    if -value.as_tuple().exponent > places:
        raise InvalidInput(f"{field}: gunakan maksimal {places} angka desimal.")
    if positive and value == 0:
        raise InvalidInput(f"{field}: harus lebih dari nol.")
    if maximum is not None and value > maximum:
        raise InvalidInput(f"{field}: maksimal {maximum}.")
    return value


def display(value):
    if value is None:
        return "Belum tersedia"
    ratio = Fraction(value)
    rounded = (2 * abs(ratio.numerator) * 100 + ratio.denominator) // (2 * ratio.denominator)
    whole, part = divmod(rounded, 100)
    return f"{'-' if ratio < 0 else ''}{whole},{part:02d}"


def exact_score(value):
    """A multiple of a finite decimal quantum has a finite decimal expansion."""
    with localcontext() as ctx:
        ctx.prec = 70
        result = Decimal(value.numerator) / Decimal(value.denominator)
    return format(result, "f").replace(".", ",")


@dataclass
class Component:
    path: str
    weight_bp: int
    maximum: Decimal | None
    quantum: Decimal | None
    effective: Fraction
    earned: Decimal | None = None
    node_id: str = ""


def validate_structure(rows):
    """Slash-delimited paths give every node exactly one parent and preclude cycles."""
    specs = {}
    totals = {}
    for index, row in enumerate(rows, start=1):
        parts = [part.strip() for part in row["path"].split("/")]
        path = " / ".join(parts)
        if not all(parts) or len(parts) > 16 or len(path) > 240 or path in specs:
            raise InvalidInput(f"Komponen {index}: gunakan jalur unik dengan 1–16 tingkat.")
        parent = " / ".join(parts[:-1])
        bp = int(decimal_input(row["weight"], f"Bobot {path}", maximum=100, places=2) * 100)
        specs[path] = (parent, bp, row)
        totals[parent] = totals.get(parent, 0) + bp
    if not specs:
        raise InvalidInput("Tambahkan sedikitnya satu komponen.")
    for parent, total in totals.items():
        if parent and parent not in specs:
            raise InvalidInput(f"Tambahkan baris kelompok “{parent}” dan isi bobotnya.")
        if total != 10000:
            raise InvalidInput(f"Total bobot {parent or 'tingkat utama'} harus 100% (sekarang {display(Fraction(total, 100))}%).")

    effective = {"": Fraction(1)}
    components = []
    for path in sorted(specs, key=lambda key: key.count(" / ")):
        parent, bp, row = specs[path]
        effective[path] = effective[parent] * Fraction(bp, 10000)
        maximum = quantum = earned = None
        if path not in totals:
            maximum = decimal_input(row["maximum"], f"Skor maksimum {path}", positive=True)
            quantum = decimal_input(row["quantum"], f"Langkah skor {path}", positive=True)
            earned = parse_score(row.get("earned", ""), maximum, path)
        elif any(row.get(key, "").strip() for key in ("maximum", "quantum", "earned")):
            raise InvalidInput(f"{path} adalah kelompok. Kosongkan maksimum, langkah, dan skor kelompok.")
        components.append(Component(path, bp, maximum, quantum, effective[path], earned))
    return components


def parse_score(raw, maximum, label):
    if not raw.strip():
        return None
    return decimal_input(raw, f"Skor {label}", maximum=maximum)


@dataclass
class Summary:
    known: Fraction
    observed_weight: Fraction
    average: Fraction | None
    upper: Fraction
    missing: list
    assumed_weight: Fraction


def summarize(components, overlay=None):
    overlay = overlay or {}
    known = observed = assumed = Fraction(0)
    missing = []
    for item in components:
        if item.maximum is None:
            continue
        earned = item.earned
        if item.node_id in overlay:
            earned = Decimal(overlay[item.node_id])
            assumed += item.effective
        if earned is None:
            if item.effective:
                missing.append(item)
        else:
            observed += item.effective
            known += item.effective * 100 * Fraction(earned) / Fraction(item.maximum)
    return Summary(known, observed, known / observed if observed else None,
                   known + 100 * (1 - observed), missing, assumed)


# This policy is opt-in per offering, and only labels synthetic demo results.
DEMO_THRESHOLDS = {"A": 85, "B": 70, "C": 0}


def classify(value, thresholds):
    for letter, threshold in sorted(thresholds.items(), key=lambda item: item[1], reverse=True):
        if value >= threshold:
            return letter
    return None


def parse_target(raw):
    raw = raw.strip().upper()
    if re.fullmatch(r"[A-Z][+\-]?", raw):
        return None, raw
    return decimal_input(raw, "Target angka", maximum=100), None


def solve_target(summary, numeric, letter, policy):
    if numeric is None:
        if not letter:
            return None
        if not policy or letter not in policy:
            return {"status": "Kebijakan huruf belum tersedia", "required": None}
        numeric = policy[letter]
    remaining = 1 - summary.observed_weight
    if not remaining:
        label = "Target tercapai" if summary.known >= numeric else "Target tidak tercapai"
        return {"status": label, "required": None}
    required = (Fraction(numeric) - summary.known) / remaining
    label = "Dapat dicapai"
    if required <= 0:
        label = "Target sudah terpenuhi dalam model"
    elif required > 100:
        label = "Tidak dapat dicapai"
    result = {"status": label, "required": required}
    if len(summary.missing) == 1 and 0 < required <= 100:
        item = summary.missing[0]
        step = Fraction(item.quantum)
        minimum = ceil(required * Fraction(item.maximum) / (100 * step)) * step
        result.update(minimum=minimum, component=item.path)
        if minimum > item.maximum:
            result["status"] = "Tidak tercapai pada langkah skor ini"
    return result
