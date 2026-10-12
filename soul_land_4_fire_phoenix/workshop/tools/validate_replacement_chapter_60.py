#!/usr/bin/env python3
"""Focused continuity/fence validation for author-review replacement Chapter 60."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "late_arc_rebuild/drafts/Chapter_60_What_We_Will_Not_Spend.md"
CONTRACT = ROOT / "late_arc_rebuild/contracts/Chapter_60_What_We_Will_Not_Spend.md"
AUDIT = ROOT / "late_arc_rebuild/audit/Chapter_60_What_We_Will_Not_Spend_Audit.md"
AUTH = ROOT / "semantic_audit/CHAPTER_60_AUTHORIZATION_AND_CAUSAL_SCOPE_ADDENDUM_2026-10-01.md"

BANNED = (
    "ling tian", "bing tianliang", "liang shushi", "niu yiwei", "dong qianqiu",
    "emerald demon bird", "holy god possession", "purple lightning dragon",
    "golden dragon soar", "blue halberd", "double crescent halberd", "button bomb",
    "rainbow dragon", "martial soul true body", "platform", "score", "points",
    "alliance", "ambush", "c61", "chapter 61", "ye lingtong",
)
REQUIRED = (
    "We do not make our condition into someone else’s fall.",
    "The decision did not make the lower route less difficult.",
    "We are not making the wrong way bright",
    "They had lost the quick way when they decided it could not belong to them alone.",
    "The shelf was not ours to spend", 
)


def main() -> int:
    failures: list[str] = []
    for path in (DRAFT, CONTRACT, AUDIT, AUTH):
        if not path.is_file():
            failures.append(f"missing required C60 package file: {path.relative_to(ROOT)}")
    if failures:
        print("C60_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    raw = DRAFT.read_text(encoding="utf-8")
    body = raw.split("\n---\n", 1)[0]
    words = re.findall(r"\b[\w’'-]+\b", body)
    if not body.startswith("# Chapter 60 — What We Will Not Spend"):
        failures.append("wrong C60 body header")
    if not 3000 <= len(words) <= 4500:
        failures.append(f"C60 body word count {len(words)} outside full-chapter review range")
    lower = body.lower()
    for term in BANNED:
        if term in lower:
            failures.append(f"fenced term in C60 live body: {term!r}")
    for marker in REQUIRED:
        if marker not in body:
            failures.append(f"missing C60 causal marker: {marker!r}")
    auth = AUTH.read_text(encoding="utf-8").lower()
    if "c61" not in auth or "chapter-191–194" not in auth:
        failures.append("C60 addendum lacks its C61/source-191–194 fence")
    if failures:
        print("C60_REPLACEMENT_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("C60_REPLACEMENT_VALIDATION: PASS")
    print(f"- author-review body: {len(words)} words")
    print("- complete trace-ethics turns are present for both teams")
    print("- source/future fence scan is clean; C61 remains outside scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
