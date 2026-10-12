#!/usr/bin/env python3
"""Validate the current protected V2 and locally accepted Option A Fire Phoenix line."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "late_arc_rebuild/rebuild_v2"
DRAFTS = V2 / "drafts"
ACCEPTED = ROOT / "accepted_replacement_layers/2026-10-03_option_A_v2_contiguous_C48_C55"

EXPECTED = {
    48: ("Chapter_48_The_Line_We_Keep.md", "The Line We Keep"),
    49: ("Chapter_49_What_They_Carry.md", "What They Carry"),
    50: ("Chapter_50_Two_Maps_of_the_Forest.md", "Two Maps of the Forest"),
    51: ("Chapter_51_The_Cost_of_Quiet.md", "The Cost of Quiet"),
    52: ("Chapter_52_What_the_Ground_Keeps.md", "What the Ground Keeps"),
    54: ("Chapter_54_What_a_Favor_Costs.md", "What a Favor Costs"),
    55: ("Chapter_55_What_We_Leave_Open.md", "What We Leave Open"),
    60: ("Chapter_60_The_Price_of_Keeping.md", "The Price of Keeping"),
}

FORBIDDEN = (
    "c61", "chapter 61", "emerald demon bird", "ling tian", "holy god possession",
    "purple lightning dragon", "martial soul true body", "nirvana", "phoenix domain",
    "external soul bone", "fourth ring", "rainbow dragon",
)


def body(raw: str) -> str:
    return raw.split("\n---\n", 1)[0]


def main() -> int:
    failures: list[str] = []
    bodies: dict[int, str] = {}

    for number, (filename, title) in EXPECTED.items():
        path = DRAFTS / filename
        if not path.is_file():
            failures.append(f"missing protected V2 C{number}: {path.relative_to(ROOT)}")
            continue
        raw = path.read_text(encoding="utf-8")
        live = body(raw)
        bodies[number] = live
        if not live.startswith(f"# Chapter {number} — {title}\n"):
            failures.append(f"malformed V2 C{number} header")
        if "## Draft continuity note" not in raw:
            failures.append(f"missing V2 continuity note in C{number}")
        words = re.findall(r"\b[\w’'-]+\b", live)
        if len(words) < 1400:
            failures.append(f"V2 C{number} body is unexpectedly short ({len(words)} words)")
        lower = live.lower()
        for term in FORBIDDEN:
            if term in lower:
                failures.append(f"forbidden future/source leak {term!r} in V2 C{number}")

    expected_files = {filename for filename, _title in EXPECTED.values()}
    found_files = {p.name for p in DRAFTS.glob("Chapter_*.md")}
    if found_files != expected_files:
        failures.append(f"V2 draft inventory drift: expected {sorted(expected_files)}, found {sorted(found_files)}")

    # Mechanics checks that should remain visible in current bodies, rather than relying on old V1 controls.
    if "Six days." not in bodies.get(52, ""):
        failures.append("V2 C52 does not visibly establish the six-day condition")
    if "skull bone" not in bodies.get(54, "").lower():
        failures.append("V2 C54 does not retain unstable skull-bone consequence")
    if "fifth evening of the six-day term" not in bodies.get(60, "").lower():
        failures.append("V2 C60 no longer anchors the held condition before expiry")
    all_v2 = "\n".join(bodies.values()).lower()
    for unsupported in ("thin place", "human radar", "remote image", "passive tether"):
        if unsupported in all_v2:
            failures.append(f"unsupported Qian-perception phrase leaked into V2 body: {unsupported!r}")
    if re.search(r"qian[^\n]{0,160}spirit sea|spirit sea[^\n]{0,160}qian", all_v2, re.I):
        failures.append("Qian Spirit Sea claim leaked into V2 body")

    for required in (
        V2 / "README_REBUILD_MAP.md",
        V2 / "V2_CLAIM_AND_CAUSAL_AUDIT_2026-10-01.md",
        V2 / "LINE_AND_CONTINUITY_PASS_2026-10-03.md",
        ROOT / "PROJECT_CONTROL.md",
        ACCEPTED / "acceptance_manifest.json",
    ):
        if not required.is_file():
            failures.append(f"missing current-control artifact: {required.relative_to(ROOT)}")

    control = (ROOT / "PROJECT_CONTROL.md").read_text(encoding="utf-8") if (ROOT / "PROJECT_CONTROL.md").is_file() else ""
    for marker in ("LOCAL_ACCEPTED_NOT_PUBLIC", "C61", "V2"):
        if marker not in control:
            failures.append(f"PROJECT_CONTROL.md lacks {marker!r}")

    if failures:
        print("CURRENT_V2_LINE_VALIDATION: FAIL")
        print(*[f"- {failure}" for failure in failures], sep="\n")
        return 1

    print("CURRENT_V2_LINE_VALIDATION: PASS")
    print("- eight protected V2 causal units present and line-audited")
    print("- current local accepted Option A control layer is present")
    print("- held-Zoysia/unstable-ape and no-C61 fences remain visible")
    print("- no forbidden future/source or unsupported Qian-perception leakage found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
