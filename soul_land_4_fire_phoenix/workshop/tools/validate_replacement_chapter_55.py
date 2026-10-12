#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 55."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_55_What_We_Leave_Open.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_55_What_We_Leave_Open.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_55_What_We_Leave_Open_Audit.md"
AUTHORIZATION = ROOT / "semantic_audit/CHAPTER_55_AUTHORIZATION_AND_SOURCE_UNIT_ADDENDUM_2026-09-27.md"
RELATIONSHIP_ADDENDUM = ROOT / "semantic_audit/YAN_YE_RELATIONSHIP_CONTINUITY_ADDENDUM_2026-09-29.md"

# These are forbidden as actual C55 body material, not merely discouraged future ideas.
BANNED = (
    "ling tian",
    "holy god possession",
    "emerald demon bird",
    "bing tianliang",
    "dong qianqiu",
    "rainbow dragon",
    "martial soul true body",
    "lan platform",
    "fourth ring",
    "nirvana",
    "domain",
    "chapter 184",
    "chapter 185",
    "chapter 186",
    "chapter 187",
    "chapter 188",
    "chapter 189",
    "chapter 190",
    "alliance",
    "team merger",
    "score",
    "points",
)


def body_of(text: str) -> str:
    return text.split("\n---\n", 1)[0]


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTHORIZATION, RELATIONSHIP_ADDENDUM):
        if not path.is_file():
            failures.append(f"required C55 package file is missing: {path.relative_to(ROOT)}")

    if failures:
        print("C55_REPLACEMENT_VALIDATION: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    draft = DRAFT.read_text(encoding="utf-8")
    body = body_of(draft)
    lower = body.lower()
    words = re.findall(r"\b[\w’'-]+\b", body)

    if not body.startswith("# Chapter 55 — What We Leave Open"):
        failures.append("draft title/body header is not the approved C55 replacement header")
    if not 2500 <= len(words) <= 4500:
        failures.append(f"body word count {len(words)} is outside the focused review range")

    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term appears in body: {term!r}")

    # Required on-page causal roles, checked as a guard against a tokenized parallel route.
    required_markers = {
        "Dorm333 Zoysia burden": ("purple zoysia", "qian", "lan", "liu"),
        "Dorm336 bounded exit": ("song", "luo", "yan", "ye lingtong"),
        "established class recognition": ("same class",),
        "Yan/Ye private emotional continuity": ("private, stupid warmth", "old private wish"),
        "Ye agency": ("the choice is yours", "the wash"),
        "separate endpoints": ("no one followed her", "the plant still lay against lan’s side"),
    }
    if "you know her?" in lower:
        failures.append("C55 retains the superseded implication that Song/Luo do not recognize Ye")
    for label, markers in required_markers.items():
        absent = [marker for marker in markers if marker not in lower]
        if absent:
            failures.append(f"missing C55 causal marker for {label}: {', '.join(absent)}")

    authorization = AUTHORIZATION.read_text(encoding="utf-8").lower()
    if "does not authorize c56" not in authorization:
        failures.append("C55 authorization no longer contains the C56 hard boundary")

    contract = CONTRACT.read_text(encoding="utf-8").lower()
    relationship_addendum = RELATIONSHIP_ADDENDUM.read_text(encoding="utf-8").lower()
    if "private, age-appropriate crush" not in contract:
        failures.append("C55 contract no longer preserves Ye’s private, age-appropriate crush continuity")
    if "private, age-appropriate crush" not in relationship_addendum:
        failures.append("Yan/Ye relationship addendum is missing its active author characterization lock")

    if failures:
        print("C55_REPLACEMENT_VALIDATION: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("C55_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- contract, authorization, draft, audit, and Yan/Ye relationship addendum are present")
    print("- source/future fence scan is clean")
    print("- Dorm333 burden, Dorm336/Ye agency, and Yan/Ye private-continuity markers are present")
    print("- C55’s own authorization remains bounded; C56 requires its separate addendum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
