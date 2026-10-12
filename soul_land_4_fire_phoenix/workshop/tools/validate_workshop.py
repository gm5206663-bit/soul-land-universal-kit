#!/usr/bin/env python3
"""High-level consistency checks for Sara's locally recovered Fire Phoenix workshop."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    manifest_path = ROOT / "provenance/PUBLIC_RECOVERY_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["summary"]["files_expected"] != 1115 or manifest["summary"]["files_failed"] != 0:
        failures.append("public recovery manifest is incomplete")

    snapshot = ROOT / "sources/chapter51_managed_snapshot/soul_land_4_fire_phoenix/chapters"
    published = ROOT / "sources/storyos_current_public_layer/published-site/soul_land_4/chapters"
    for number in range(1, 52):
        old = snapshot / f"Chapter_{number:02d}.md"
        new = published / f"Chapter_{number:02d}.md"
        if not old.is_file() or not new.is_file() or sha256(old) != sha256(new):
            failures.append(f"Chapter {number:02d} diverges or is missing between snapshot and published layer")

    chapter52 = published / "Chapter_52.md"
    state = (ROOT / "sources/storyos_current_public_layer/published-site/soul_land_4/state.json").read_text(encoding="utf-8")
    pointer = (ROOT / "sources/soul_land_universal_kit_main_related/SOUL_LAND_4_FIRE_PHOENIX_NEXT_STEPS_FOR_CONTINUATION.md").read_text(encoding="utf-8")
    if not chapter52.is_file():
        failures.append("accepted Chapter 52 is missing")
    if '"fic_chapter": 52' not in state or '"next_source": 178' not in state:
        failures.append("StoryOS state does not establish Chapter 52 / Chapter 178")
    if "after Chapter52" not in pointer or "Chapter53" not in pointer:
        failures.append("root next-steps pointer does not establish the Chapter 52 edge")

    prep = ROOT / "continuation_preparation/03_CANON_COVERAGE_CHAPTER_53.md"
    if not prep.is_file() or "Stop there" not in prep.read_text(encoding="utf-8"):
        failures.append("Chapter 53 coverage or its Chapter 179 boundary is missing")

    if failures:
        print("SARA_FIRE_PHOENIX_WORKSHOP: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("SARA_FIRE_PHOENIX_WORKSHOP: PASS")
    print("- 1,115 public source files recovered with zero failures")
    print("- Chapters 1–51 are byte-identical across full snapshot and public current layer")
    print("- Chapter 52/current source boundary agrees across public authority layers")
    print("- Chapter 53 preparation includes a Chapter 179 containment stop")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
