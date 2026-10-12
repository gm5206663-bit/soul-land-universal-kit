#!/usr/bin/env python3
"""Validate the public Chapter 53 preparation package.

This tool checks package consistency and can scan a candidate story body for high-signal
Chapter 179 spillover/currentisation. It is NOT the authoritative private-project gate.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "00_SOURCE_AUTHORITY_RECONCILIATION.md",
    "01_LIVE_CONTINUITY_CARD.md",
    "02_HARD_LOCKS_AND_GUARDS.md",
    "03_CANON_COVERAGE_CHAPTER_53.md",
    "04_CHAPTER_53_BLUEPRINT.md",
    "05_VALIDATION_GATE.md",
    "SOURCE_LOG.md",
]

PACKAGE_EXPECTATIONS = {
    "00_SOURCE_AUTHORITY_RECONCILIATION.md": ["after Chapter 52", "Chapter 178", "Chapter 31"],
    "01_LIVE_CONTINUITY_CARD.md": ["Rank39 / SP962", "Purple Zoysia", "no offer"],
    "02_HARD_LOCKS_AND_GUARDS.md": ["Ultimate Fire", "Chapter 179", "scoped"],
    "03_CANON_COVERAGE_CHAPTER_53.md": ["Permitted source", "Stop there", "Palm Tree Bear"],
    "04_CHAPTER_53_BLUEPRINT.md": ["No Prose", "Movement 5", "Mandatory stop"],
}

# Applied only to candidate prose before a footer. These are deliberately narrower than
# permanent project bans because the herb retrieval is now a permitted Chapter 178 event.
BODY_FORBIDDEN = {
    "source-number/title leak": r"\b(?:Chapter\s*178|Chapter178|Collaborate|Chapter\s*179|Chapter179|Initial alliance)\b",
    "future Yan route": r"\b(?:Rainbow Dragon|Dragon Queen necklace|Phoenix God authority|Phoenix Domain|Nirvana|Martial Soul True Body|five[- ]colou?red Phoenix|Yan(?:'s)? Emerald Demon Bird|external soul bone)\b",
    "stale stat": r"\bSP526\b",
    "Platform progression": r"\b(?:Lan[^\n]{0,120}\b(?:entered|used)\b[^\n]{0,80}Platform|Platform[^\n]{0,80}(?:improvement|growth)[^\n]{0,80}(?:occurred|happened|completed))\b",
    "Qian invented ring result": r"\bQian[^\n]{0,160}(?:purple breakthrough|purple-ring breakthrough|exact[^\n]{0,40}ring age)\b",
    "Silver Edge premature feat": r"\bSilver Edge[^\n]{0,120}(?:mastered|combat victory|killed|defeated)\b",
    "Palm Tree Bear outcome belongs to Chapter 179": r"\bPalm Tree Bear[^\n]{0,100}(?:died|dead|neck\s+(?:snapped|was broken)|killed)\b",
    "premature finishing/points": r"\b(?:finishing blow|final kill|points? (?:were|was|are|is) (?:awarded|received|gained)|score (?:rose|increased|was))\b",
    "premature Gold Silk Ape alliance": r"\b(?:alliance|six days|Gold Silk Ape[^\n]{0,120}\b(?:agreed|nodded|allied)\b)\b",
    "premature herb consumption": r"\b(?:Purple Zoysia|the herb)[^\n]{0,120}\b(?:eaten|consumed|swallowed)\b",
    "premature wound treatment": r"\b(?:heal(?:ed|ing)?|clean(?:ed|ing)?)[^\n]{0,100}\b(?:ape|Gold Silk Ape|wound)\b",
}


def story_body(text: str) -> str:
    """Ignore a conventional footer so a validation checklist can name forbidden material."""
    return re.split(r"\n---\s*\n##\s*Footer\b", text, maxsplit=1, flags=re.I)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--body", type=Path, help="Optional candidate Chapter 53 Markdown file to scan")
    args = parser.parse_args()

    errors: list[str] = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"missing package file: {name}")

    for name, phrases in PACKAGE_EXPECTATIONS.items():
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{name} lacks expected continuity marker: {phrase!r}")

    if args.body:
        if not args.body.is_file():
            errors.append(f"candidate body does not exist: {args.body}")
        else:
            body = story_body(args.body.read_text(encoding="utf-8"))
            for label, pattern in BODY_FORBIDDEN.items():
                if re.search(pattern, body, flags=re.I | re.S):
                    errors.append(f"candidate body violates guard: {label}")

    if errors:
        print("FIRE_PHOENIX_CH53_PREPARATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("FIRE_PHOENIX_CH53_PREPARATION: PASS")
    print("- source authority reconciled: live edge after Chapter52")
    print("- next source boundary: Chapter178 only")
    print("- Chapter179 containment and current-state guards are present")
    if args.body:
        print(f"- candidate body scan passed: {args.body}")
    else:
        print("- no prose body supplied; package-only validation completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
