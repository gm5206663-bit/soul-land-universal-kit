#!/usr/bin/env python3
"""Validate the non-applying Option A V2 public staging candidate."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

STAGE = Path(__file__).resolve().parent
ROOT = STAGE.parents[3]
PACKAGE = STAGE.parent
CHAPTERS = STAGE / "chapters"

EXPECTED = {
    48: (48, "The Line We Keep"),
    49: (49, "What They Carry"),
    50: (50, "Two Maps of the Forest"),
    51: (51, "The Cost of Quiet"),
    52: (52, "What the Ground Keeps"),
    53: (54, "What a Favor Costs"),
    54: (55, "What We Leave Open"),
    55: (60, "The Price of Keeping"),
}

LITERALS = (
    "Chapter 178", "Chapter178", "Chapter179", "Collaborate",
    "Dragon Queen necklace", "Fire Phoenix output-calibration cuff",
    "Initial alliance", "Martial Soul True Body", "Nirvana", "Phoenix Domain",
    "Phoenix God authority", "Rainbow Dragon", "SP526",
    "Second place is not nothing", "Yan Emerald Demon Bird",
    "Yan's Emerald Demon Bird", "external soul bone", "five-colored Phoenix",
    "five-coloured Phoenix", "public Yan Shuo'er reveal",
    "public Yan Shuo’er reveal", "shield-load impact matrix",
    "special observation file", "wind-line reaction threads",
)
PATTERNS = (
    r"Lan[^\n]{0,120}\b(entered|used)\b[^\n]{0,80}Platform",
    r"Platform[^\n]{0,80}(improvement|growth)[^\n]{0,80}(occurred|happened|completed)",
    r"Qian[^\n]{0,160}(purple breakthrough|purple-ring breakthrough|exact.*ring age)",
    r"Silver Edge[^\n]{0,120}(mastered|enemy|combat victory|killed|defeated)",
    r"(?:Purple Zoysia|the herb)[^\n]{0,120}\?(?:taken|grabbed|snatched|stolen|in (?:his|Lan)'s hand)",
    r"Gold Silk Ape[^\n]{0,120}\b(?:allied|alliance|agreed|nodded)\b",
    r"Palm Tree Bear[^\n]{0,80}\b(?:died|dead|neck snapped|neck was broken|killed)\b",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    manifest = json.loads((STAGE / "staging_manifest.json").read_text(encoding="utf-8"))
    if manifest.get("status") != "STAGED_OPTION_A_NOT_APPLIED":
        failures.append("staging manifest does not carry non-applying Option A status")
    if manifest.get("apply_authorization") != "NOT_GRANTED":
        failures.append("staging manifest improperly implies apply authorization")

    files = sorted(CHAPTERS.glob("Chapter_*.md"))
    if len(files) != len(EXPECTED):
        failures.append(f"expected {len(EXPECTED)} staged chapters, found {len(files)}")

    for public_number, (internal_number, title) in EXPECTED.items():
        path = CHAPTERS / f"Chapter_{public_number:02d}.md"
        if not path.is_file():
            failures.append(f"missing staged C{public_number}")
            continue
        raw = path.read_text(encoding="utf-8")
        expected_header = f"# Chapter {public_number} — {title}"
        if not raw.startswith(expected_header + "\n"):
            failures.append(f"bad staged header for C{public_number}")
        if "## Draft continuity note" in raw or "author-review" in raw.lower():
            failures.append(f"V2 review metadata leaked into staged C{public_number}")
        if "C61" in raw or "Chapter 61" in raw:
            failures.append(f"C61 leak in staged C{public_number}")
        for literal in LITERALS:
            if literal.lower() in raw.lower():
                failures.append(f"banned literal {literal!r} in staged C{public_number}")
        for pattern in PATTERNS:
            if re.search(pattern, raw, re.I):
                failures.append(f"banned pattern {pattern!r} in staged C{public_number}")

    # Candidate manifest pins both the unmodified public baseline and the V2 sources.
    proposal_manifest = json.loads((PACKAGE / "candidate_manifest.json").read_text(encoding="utf-8"))
    for record in proposal_manifest["public_baseline"]["files_to_archive_if_approved"]:
        path = ROOT / record["public_file"]
        if not path.is_file() or digest(path) != record["sha256"]:
            failures.append(f"recovered public baseline drifted: {record['public_file']}")
    for record in manifest["candidate_files"]:
        staged = ROOT / record["public_file"]
        source = ROOT / record["internal_v2_file"]
        if not staged.is_file() or digest(staged) != record["candidate_sha256"]:
            failures.append(f"staged candidate hash drifted: {record['public_file']}")
        if not source.is_file() or digest(source) != record["internal_v2_sha256"]:
            failures.append(f"protected V2 source hash drifted: {record['internal_v2_file']}")

    if failures:
        print("OPTION_A_V2_PUBLIC_STAGING: FAIL")
        print(*[f"- {x}" for x in failures], sep="\n")
        return 1
    print("OPTION_A_V2_PUBLIC_STAGING: PASS")
    print("- eight contiguous candidate files C48–C55")
    print("- recovered public C48–C52 baseline hashes unchanged")
    print("- protected V2 source hashes and staged candidate hashes agree")
    print("- current literal/pattern fence screen is clean")
    print("- staging remains non-applying; C61 absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
