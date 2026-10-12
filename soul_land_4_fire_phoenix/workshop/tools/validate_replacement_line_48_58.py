#!/usr/bin/env python3
"""Integrated structural/fence validation for the historical C48–C58 segment of the active line.

C59 and C60 are separately authorized and validated by later integrated tools; this receipt preserves the
C48–C58 segment's own source/future fence scan without treating later package files as artifact leaks.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "late_arc_rebuild/drafts"
CONTRACTS = ROOT / "late_arc_rebuild/contracts"
AUDITS = ROOT / "late_arc_rebuild/audit"

CHAPTERS = {
    48: "The_Line_We_Keep", 49: "What_They_Carry", 50: "Two_Maps_of_the_Forest",
    51: "The_Cost_of_Quiet", 52: "What_the_Ground_Keeps", 53: "Where_They_Stand",
    54: "What_a_Favor_Costs", 55: "What_We_Leave_Open", 56: "What_Returns",
    57: "What_the_Rain_Carries", 58: "What_the_Morning_Takes",
}
LATER_BANNED = (
    "ling tian", "bing tianliang", "emerald demon bird", "holy god possession",
    "purple lightning dragon", "rainbow dragon", "martial soul true body", "platform",
    "silver edge", "c59", "chapter 59",
)


def body(text: str) -> str:
    return text.split("\n---\n", 1)[0]


def main() -> int:
    failures: list[str] = []
    counts: dict[int, int] = {}
    bodies: dict[int, str] = {}
    draft_texts: dict[int, str] = {}
    for number, slug in CHAPTERS.items():
        stem = f"Chapter_{number}_{slug}.md"
        draft = DRAFTS / stem
        contract = CONTRACTS / stem
        audit = AUDITS / f"Chapter_{number}_{slug}_Audit.md"
        for path in (draft, contract, audit):
            if not path.is_file():
                failures.append(f"missing C{number} package file: {path.relative_to(ROOT)}")
        if not draft.is_file():
            continue
        raw = draft.read_text(encoding="utf-8")
        draft_texts[number] = raw
        contract_text = contract.read_text(encoding="utf-8") if contract.is_file() else ""
        live = body(raw)
        bodies[number] = live
        words = re.findall(r"\b[\w’'-]+\b", live)
        counts[number] = len(words)
        if not live.startswith(f"# Chapter {number} — "):
            failures.append(f"C{number} live header missing/malformed")
        if "## Governing question" not in contract_text:
            failures.append(f"C{number} contract lacks a governing question")
        if "endpoint" not in contract_text.lower():
            failures.append(f"C{number} contract lacks a defined endpoint")
        if "\n---\n" not in raw:
            failures.append(f"C{number} missing body/continuity separator")
        if not 2700 <= len(words) <= 4500:
            failures.append(f"C{number} word count {len(words)} outside active full-chapter band")
        for leak in ("author-review", "validator", "workshop", "source chapter"):
            if leak in live.lower():
                failures.append(f"C{number} metadata leak in live body: {leak!r}")
        if number >= 55:
            for term in LATER_BANNED:
                if term in live.lower():
                    failures.append(f"C{number} later-source/future fence leak: {term!r}")
    # The core altered-line lock must be unambiguous in both the controlling contract and prose.
    c53_contract = (CONTRACTS / "Chapter_53_Where_They_Stand.md").read_text(encoding="utf-8").lower()
    if "zoysia remains held by dorm333 for the six days" not in c53_contract:
        failures.append("C53 contract does not explicitly preserve held Zoysia through the six-day term")
    for number in (53, 54, 56, 57, 58):
        late_package = draft_texts.get(number, "").lower()
        if "six-day" not in late_package and "six days" not in late_package:
            failures.append(f"C{number} package does not carry the six-day Zoysia term")
    c55_body = bodies.get(55, "").lower()
    if "condition" not in c55_body or "terms" not in c55_body:
        failures.append("C55 live body does not carry the held-Zoysia condition forward")
    # Current navigation must describe the actual active endpoint, not a superseded one.
    navigation = {
        ROOT / "ACTIVE_START_HERE.md": ("Chapters 48–60", "C61 is not authorized"),
        ROOT / "CURRENT_PUBLIC_VIEW.md": ("through Chapter 60", "C61"),
        ROOT / "README.md": ("complete through Chapter 60", "C61"),
        ROOT / "SARA_COMPREHENSION_LEDGER.md": ("through Chapter 60", "C61 is not authorized"),
        ROOT / "SARA_WORKING_CONTEXT.md": ("through C60", "C61"),
        ROOT / "continuation_preparation/README.md": ("completed through C60", "C61 remains unauthorized"),
        ROOT / "late_arc_rebuild/README.md": ("Chapters 48–60", "C61 is not authorized"),
        ROOT / "semantic_audit/FORWARD_PLAN_RECONCILIATION_2026-09-27.md": ("C60", "C61"),
        ROOT / "semantic_audit/POST_C54_SOURCE_CAUSAL_ATLAS_183_200_2026-09-27.md": ("C60", "C61"),
        ROOT / "semantic_audit/WRITING_STYLE_AND_CRAFT_LEDGER_2026-09-27.md": ("C60", "C61"),
        ROOT / "semantic_audit/YAN_YE_RELATIONSHIP_CONTINUITY_ADDENDUM_2026-09-29.md": ("C55–C60", "C61"),
    }
    for path, required in navigation.items():
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        for marker in required:
            if marker not in text:
                failures.append(f"stale/missing navigation marker {marker!r} in {path.relative_to(ROOT)}")
    if any("61" in p.name for p in list(DRAFTS.glob("*")) + list(CONTRACTS.glob("*")) + list(AUDITS.glob("*"))):
        failures.append("C61 artifact exists in active replacement lane")
    if failures:
        print("C48_C58_REPLACEMENT_LINE_VALIDATION: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("C48_C58_REPLACEMENT_LINE_VALIDATION: PASS")
    print("- active bodies:", ", ".join(f"C{k}={v}" for k, v in counts.items()))
    print("- all 11 historical-segment contract/draft/audit packages exist and have full-chapter bodies")
    print("- C55–C58 source/future fences remain clean; C59/C60 are separately packaged")
    print("- current navigation recognizes C60 as endpoint and C61 as unauthorized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
