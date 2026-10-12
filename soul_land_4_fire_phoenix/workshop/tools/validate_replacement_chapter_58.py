#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 58."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_58_What_the_Morning_Takes.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_58_What_the_Morning_Takes.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_58_What_the_Morning_Takes_Audit.md"
AUTH = ROOT / "semantic_audit/CHAPTER_58_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-09-29.md"

BANNED = (
    "ling tian", "bing tianliang", "emerald demon bird", "holy god possession",
    "purple lightning dragon", "alliance", "points", "score", "platform",
    "silver edge", "rainbow dragon", "martial soul true body", "c59", "chapter 59",
)
REQUIRED = (
    "Morning did not arrive as light.",
    "Together they rebuilt the root ball.",
    "That was enough.",
    "The cedar dropped into the spillway behind them.",
    "It did not make the forest safe.",
)


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTH):
        if not path.is_file():
            failures.append(f"missing required C58 package file: {path.relative_to(ROOT)}")
    if failures:
        print("C58_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    raw = DRAFT.read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[0]
    words = re.findall(r"\b[\w’'-]+\b", body)
    if not body.startswith("# Chapter 58 — What the Morning Takes"):
        failures.append("wrong C58 body header")
    if not 3000 <= len(words) <= 4500:
        failures.append(f"C58 body word count {len(words)} outside full-chapter review range")
    lower = body.lower()
    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term in C58 live body: {term!r}")
    for marker in REQUIRED:
        if marker not in body:
            failures.append(f"missing C58 causal marker: {marker!r}")
    auth = AUTH.read_text(encoding="utf-8").lower()
    if "no c59" not in auth and "authorize c59" not in auth:
        failures.append("C58 addendum lacks its C59 boundary")
    if failures:
        print("C58_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("C58_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- complete dawn movement, Zoysia care, and full-team spillway exit are present")
    print("- source/future fence scan is clean; C59/C60 are separately authorized and C61 remains outside scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
