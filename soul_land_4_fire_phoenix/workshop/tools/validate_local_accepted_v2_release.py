#!/usr/bin/env python3
"""Validate the locally accepted, non-public Option A V2 C48–C55 release layer."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCEPTED = ROOT / "accepted_replacement_layers/2026-10-03_option_A_v2_contiguous_C48_C55"
STAGING = ROOT / "late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03/staging_option_A_contiguous_public_C48_C55"
PROPOSAL = ROOT / "late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03"

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    manifest_path = ACCEPTED / "acceptance_manifest.json"
    if not manifest_path.is_file():
        failures.append("missing accepted-layer manifest")
        manifest: dict = {}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    if manifest.get("status") != "LOCAL_ACCEPTED_NOT_PUBLIC":
        failures.append("accepted-layer status must remain LOCAL_ACCEPTED_NOT_PUBLIC")
    if manifest.get("public_layer_mutated") is not False:
        failures.append("accepted-layer manifest must state public layer was not mutated")
    if manifest.get("github_push_authorized") is not False:
        failures.append("accepted-layer manifest must state GitHub push is not authorized")
    if manifest.get("hard_boundary", "").lower().find("c61") < 0:
        failures.append("accepted-layer manifest lacks explicit C61 boundary")

    staged_manifest = json.loads((STAGING / "staging_manifest.json").read_text(encoding="utf-8"))
    for public_number, (internal_number, title) in EXPECTED.items():
        accepted = ACCEPTED / "chapters" / f"Chapter_{public_number:02d}.md"
        staged = STAGING / "chapters" / f"Chapter_{public_number:02d}.md"
        if not accepted.is_file():
            failures.append(f"missing accepted C{public_number}")
            continue
        text = accepted.read_text(encoding="utf-8")
        if not text.startswith(f"# Chapter {public_number} — {title}\n"):
            failures.append(f"incorrect accepted header for C{public_number}")
        if "## Draft continuity note" in text or "author-review" in text.lower():
            failures.append(f"review metadata leaked into accepted C{public_number}")
        if "C61" in text or "Chapter 61" in text:
            failures.append(f"C61 leak in accepted C{public_number}")
        if not staged.is_file() or sha256(accepted) != sha256(staged):
            failures.append(f"accepted/staging drift in C{public_number}")

    records = {r["public_number"]: r for r in manifest.get("chapters", [])}
    if set(records) != set(EXPECTED):
        failures.append("accepted manifest chapter inventory does not equal C48–C55")
    for number, record in records.items():
        path = ROOT / record["file"]
        if not path.is_file() or sha256(path) != record["sha256"]:
            failures.append(f"accepted manifest hash drift: C{number}")

    proposal_manifest = json.loads((PROPOSAL / "candidate_manifest.json").read_text(encoding="utf-8"))
    for record in proposal_manifest["public_baseline"]["files_to_archive_if_approved"]:
        path = ROOT / record["public_file"]
        if not path.is_file() or sha256(path) != record["sha256"]:
            failures.append(f"recovered public baseline drift: {record['public_file']}")

    authority = ROOT / "PROJECT_CONTROL.md"
    if not authority.is_file():
        failures.append("missing PROJECT_CONTROL.md")
    elif "LOCAL_ACCEPTED_NOT_PUBLIC" not in authority.read_text(encoding="utf-8"):
        failures.append("PROJECT_CONTROL.md does not expose accepted non-public status")

    if failures:
        print("LOCAL_ACCEPTED_V2_RELEASE: FAIL")
        print(*[f"- {failure}" for failure in failures], sep="\n")
        return 1
    print("LOCAL_ACCEPTED_V2_RELEASE: PASS")
    print("- accepted Option A C48–C55 matches validated staging")
    print("- recovered public C48–C52 baseline remains hash-stable")
    print("- non-public/no-push/C61 boundaries are explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
