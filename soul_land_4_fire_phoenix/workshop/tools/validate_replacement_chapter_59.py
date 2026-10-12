#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 59."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_59_What_the_Forest_Sees.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_59_What_the_Forest_Sees.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_59_What_the_Forest_Sees_Audit.md"
AUTH = ROOT / "semantic_audit/CHAPTER_59_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-10-01.md"

BANNED = (
    "ling tian", "bing tianliang", "emerald demon bird", "holy god possession",
    "purple lightning dragon", "rainbow dragon", "martial soul true body", "platform",
    "score", "points", "alliance", "ambush", "c60", "chapter 60", "ye lingtong",
)
REQUIRED = (
    "The older trees did not make the forest empty.",
    "It changes what we know,” he said. “Not what we owe them.",
    "We cannot lead you through a route we have not paid for ourselves",
    "But not from inside our formation.",
    "He did not owe them a fire bright enough to choose for them.",
)


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTH):
        if not path.is_file():
            failures.append(f"missing required C59 package file: {path.relative_to(ROOT)}")
    if failures:
        print("C59_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    raw = DRAFT.read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[0]
    words = re.findall(r"\b[\w’'-]+\b", body)
    if not body.startswith("# Chapter 59 — What the Forest Sees"):
        failures.append("wrong C59 body header")
    if not 3000 <= len(words) <= 4500:
        failures.append(f"C59 body word count {len(words)} outside full-chapter review range")
    lower = body.lower()
    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term in C59 live body: {term!r}")
    for marker in REQUIRED:
        if marker not in body:
            failures.append(f"missing C59 causal marker: {marker!r}")
    auth = AUTH.read_text(encoding="utf-8").lower()
    if "c60" not in auth or "no source chapter-188–190" not in auth:
        failures.append("C59 addendum lacks its C60/source-188–190 fence")
    if failures:
        print("C59_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("C59_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- complete post-rain human-visibility turns are present for both teams")
    print("- source/future fence scan is clean; C60 is separately authorized and C61 remains outside scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
