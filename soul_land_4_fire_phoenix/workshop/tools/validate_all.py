#!/usr/bin/env python3
"""Run the complete Fire Phoenix local validation suite in preservation and governance order."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ("GitHub governance and credential screen", ("tools/validate_github_governance.py",)),
    ("Recovered public evidence", ("tools/verify_public_recovery.py",)),
    ("Recovered workshop baseline", ("tools/validate_workshop.py",)),
    ("Frozen V1 historical package", ("tools/validate_replacement_line_48_60.py",)),
    ("Current protected V2 line", ("tools/validate_current_v2_line.py",)),
    (
        "Option A V2 staging package",
        ("late_arc_rebuild/rebuild_v2/promotion_proposal_2026-10-03/staging_option_A_contiguous_public_C48_C55/validate_option_a_staging.py",),
    ),
    ("Locally accepted V2 snapshot", ("tools/validate_local_accepted_v2_release.py",)),
)


def main() -> int:
    failed: list[str] = []
    for label, command in CHECKS:
        print(f"\n=== {label} ===", flush=True)
        result = subprocess.run((sys.executable, *command), cwd=ROOT)
        if result.returncode:
            failed.append(label)
    print("\n=== Summary ===")
    if failed:
        print("FIRE_PHOENIX_VALIDATION_SUITE: FAIL")
        print("Failed:", ", ".join(failed))
        return 1
    print("FIRE_PHOENIX_VALIDATION_SUITE: PASS")
    print(f"{len(CHECKS)} checks passed in preservation and governance order.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
