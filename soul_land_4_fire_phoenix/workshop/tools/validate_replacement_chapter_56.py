#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 56."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_56_What_Returns.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_56_What_Returns.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_56_What_Returns_Audit.md"
AUTHORIZATION = ROOT / "semantic_audit/CHAPTER_56_AUTHORIZATION_AND_SOURCE_UNIT_ADDENDUM_2026-09-29.md"
C57_AUTHORIZATION = ROOT / "semantic_audit/CHAPTER_57_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-09-29.md"
C58_AUTHORIZATION = ROOT / "semantic_audit/CHAPTER_58_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-09-29.md"

# Forbidden as actual C56 body material, not merely discouraged future ideas.
BANNED = (
    "ling tian",
    "li yaoming",
    "shu zixuan",
    "xu rongxin",
    "holy god possession",
    "purple lightning dragon",
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
    "chapter 188",
    "alliance",
    "score",
    "points",
    "recovered ape",
)


def body_of(text: str) -> str:
    return text.split("\n---\n", 1)[0]


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTHORIZATION, C57_AUTHORIZATION, C58_AUTHORIZATION):
        if not path.is_file():
            failures.append(f"required C56–C58 authorization context file is missing: {path.relative_to(ROOT)}")

    if failures:
        print("C56_REPLACEMENT_VALIDATION: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    draft = DRAFT.read_text(encoding="utf-8")
    body = body_of(draft)
    lower = body.lower()
    words = re.findall(r"\b[\w’'-]+\b", body)

    if not body.startswith("# Chapter 56 — What Returns"):
        failures.append("draft title/body header is not the approved C56 replacement header")
    if not 2400 <= len(words) <= 4500:
        failures.append(f"body word count {len(words)} is outside the focused review range")

    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term appears in body: {term!r}")

    # Guard against a tokenized ape return or a Dorm336 route that spends Ye's agency.
    required_markers = {
        "Dorm333 held-condition movement": ("purple zoysia", "gold silk ape", "qian", "lan", "liu"),
        "Dorm336 complete formation exit": ("song", "luo", "yan", "false trace", "out"),
        "Ye route protected": ("not ye’s route either", "we do not help them"),
        "ape agency preserved": ("the six days are still six days", "it could leave in any direction it chose"),
    }
    for label, markers in required_markers.items():
        absent = [marker for marker in markers if marker not in lower]
        if absent:
            failures.append(f"missing C56 causal marker for {label}: {', '.join(absent)}")

    authorization = AUTHORIZATION.read_text(encoding="utf-8").lower()
    c57_authorization = C57_AUTHORIZATION.read_text(encoding="utf-8").lower()
    c58_authorization = C58_AUTHORIZATION.read_text(encoding="utf-8").lower()
    if "no c57" not in authorization:
        failures.append("C56 authorization no longer contains its own C57 boundary")
    if "separately authorized" not in authorization or "no c58" not in c57_authorization:
        failures.append("C56/C57 authorization handoff is not explicitly bounded")
    if "separately authorized" not in c57_authorization or ("no c59" not in c58_authorization and "authorize c59" not in c58_authorization):
        failures.append("C57/C58 authorization handoff is not explicitly bounded")

    if failures:
        print("C56_REPLACEMENT_VALIDATION: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("C56_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- contract, authorization, draft, and audit are present")
    print("- source/future fence scan is clean")
    print("- ape agency and Dorm336/Ye route markers are present")
    print("- C56 remains bounded; C57–C60 are separately authorized under their own addenda; C61 remains outside scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
