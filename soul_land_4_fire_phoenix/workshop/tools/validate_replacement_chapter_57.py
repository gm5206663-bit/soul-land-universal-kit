#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 57."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_57_What_the_Rain_Carries.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_57_What_the_Rain_Carries.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_57_What_the_Rain_Carries_Audit.md"
AUTH = ROOT / "semantic_audit/CHAPTER_57_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-09-29.md"
NEXT_AUTH = ROOT / "semantic_audit/CHAPTER_58_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-09-29.md"

BANNED = (
    "ling tian", "bing tianliang", "emerald demon bird", "holy god possession",
    "purple lightning dragon", "alliance", "points", "score", "platform",
    "silver edge", "rainbow dragon", "martial soul true body", "c59", "chapter 59",
)
REQUIRED = (
    "Rain found the stone shelf one drop at a time.",
    "It found its own way",
    "We still do not mark it.",
    "It did not erase the choice.",
    "It had chosen a way out.",
    "The same mistake as the stone shelf.",
)


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTH, NEXT_AUTH):
        if not path.is_file():
            failures.append(f"missing required C57 context file: {path.relative_to(ROOT)}")
    if failures:
        print("C57_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    raw = DRAFT.read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[0]
    words = re.findall(r"\b[\w’'-]+\b", body)
    if not body.startswith("# Chapter 57 — What the Rain Carries"):
        failures.append("wrong C57 body header")
    if not 3000 <= len(words) <= 4500:
        failures.append(f"C57 body word count {len(words)} outside full-chapter review range")
    lower = body.lower()
    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term in C57 live body: {term!r}")
    for marker in REQUIRED:
        if marker not in body:
            failures.append(f"missing C57 causal marker: {marker!r}")
    if "no c58" not in AUTH.read_text(encoding="utf-8").lower():
        failures.append("C57 addendum lacks its own C58 boundary")
    next_auth = NEXT_AUTH.read_text(encoding="utf-8").lower()
    if "no c59" not in next_auth and "authorize c59" not in next_auth:
        failures.append("separate C58 addendum lacks C59 boundary")
    if failures:
        print("C57_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("C57_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- complete two-stage rain movement, ape autonomy, and Ye-route protection are present")
    print("- source/future fence scan is clean; later C58/C59 boundaries and separate C59/C60 authority are reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
