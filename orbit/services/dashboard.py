"""Read the Grade Rescue and Roadmap views at the same committed workspace revision."""

import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from orbit.domain.roadmap import RoadmapError
from orbit.services import academic_roadmap, gradebook


class UnknownTerm(LookupError):
    pass


@dataclass(frozen=True)
class Notice:
    text: str
    endpoint: str
    anchor: str
    course_id: str | None = None


def _rule_sources(reason):
    """A leaf may explicitly carry an empty reference even in a versioned catalog."""
    if "children" in reason:
        for child in reason["children"]:
            yield from _rule_sources(child)
    else:
        yield reason.get("source")


def read(path: Path, term_id: str | None = None) -> dict:
    with gradebook.snapshot(path) as db:
        context = academic_roadmap.scenario_context(db)
        terms = db.execute("SELECT term_id,label FROM academic_term ORDER BY sequence_no DESC").fetchall()
        term = next((row for row in terms if row["term_id"] == term_id), None)
        if term_id and term is None:
            raise UnknownTerm
        data_notices, target_notices, plan_notices = [], [], []
        cards = []
        for row in gradebook.courses(db, term_id):
            card = gradebook.read_summary(db, row, context["scenario"], context["stale"])
            cards.append(card)
            name, course_id = row["name"], row["id"]
            card["source"] = json.loads(row["offering_source"]).get("source_ref")
            latest = card["finals"][0] if card["finals"] else None
            card["final"] = latest
            card["final_source"] = json.loads(latest["source"]).get("source_ref") if latest else None
            if card["actual"] is None:
                data_notices.append(Notice(f"{name} · Struktur penilaian belum tersedia.", "grades.edit", "", course_id))
            elif card["actual"].average is None:
                data_notices.append(Notice(f"{name} · Belum ada skor berbobot yang tercatat.", "grades.detail", "skor", course_id))
            if card["rules"]:
                data_notices.append(Notice(f"{name} · Aturan tambahan di luar model linear.", "grades.detail", "skor", course_id))
            result = card["result"]
            if result and result["needs_review"]:
                target_notices.append(Notice(f"{name} · {result['status']}.", "grades.detail", "target", course_id))

        catalog_error = None
        try:
            road = academic_roadmap.read(db, context)
        except (RoadmapError, json.JSONDecodeError):
            # Grades and the scenario token are still readable at this revision.
            road = dict(context, catalog=None)
            catalog_error = "NEEDS_VALIDATION · Periksa versi, sumber, dan aturan pada berkas katalog sintetis."

        eligibility_counts = Counter()
        if road["catalog"]:
            for key, reason in road["reasons"].items():
                label = road["catalog"].courses[key]["label"]
                eligibility_counts[reason["status"]] += 1
                if not all(_rule_sources(reason)):
                    data_notices.append(Notice(f"{label} · NEEDS_VALIDATION · Periksa sumber aturan prasyarat.",
                                               "roadmap.index", f"prasyarat-{key}"))
            if road["credits"]["excluded"]:
                count = road["credits"]["excluded"]
                data_notices.append(Notice(f"{count} pengambilan di luar cakupan SKS katalog aktif.",
                                           "roadmap.index", "pengambilan"))
            for semester in sorted(road["credits"]["over"]):
                total = road["credits"]["totals"][semester]
                plan_notices.append(Notice(f"Semester {semester} · {total} SKS melebihi batas personal "
                                           f"{road['plan']['cap']} SKS.", "roadmap.index", "hasil"))
            for semester in sorted(road["projected"]["over"]):
                total = road["projected"]["totals"][semester]
                plan_notices.append(Notice(f"Setelah simulasi, semester {semester} memuat {total} SKS "
                                           f"dan melebihi batas personal {road['plan']['cap']} SKS.",
                                           "roadmap.index", "hasil"))

        scenario = context["scenario"]
        has_overlay = bool(scenario and any(json.loads(scenario[key]) for key in
                                           ("plan", "assumptions", "score_overlay", "target_overlay")))
        return dict(**context, has_overlay=has_overlay, terms=terms, term=term, cards=cards, road=road, catalog_error=catalog_error,
                    eligibility_counts=eligibility_counts, notices=data_notices + target_notices + plan_notices,
                    calculated_at=datetime.now(timezone(timedelta(hours=7), "WIB")))
