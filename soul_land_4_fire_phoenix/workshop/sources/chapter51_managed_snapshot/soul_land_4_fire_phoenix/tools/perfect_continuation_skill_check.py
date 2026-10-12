#!/usr/bin/env python3
"""
Perfect Continuation Skill Check — Level 2

Reusable project-integrity validator for the Soul Land 4 Fire Phoenix fic.

Level-2 upgrades:
- Loads foundation/CURRENT_STATE_MANIFEST.json.
- Infers latest fic chapter / consumed source / next source from STATUS_PANEL if args are omitted.
- Uses dynamic stale detection instead of Chapter51-only hard-coding.
- Scans active foundation/bible/codex/top-level files for stale current-state, stale next-protocol, and stale reward-state text.
- Separates story body from footer when checking forbidden future-route/currentization leakage.
- Supports report writing for audit receipts.

Usage:
    python3 tools/perfect_continuation_skill_check.py
    python3 tools/perfect_continuation_skill_check.py --latest 51 --next-source 174
    python3 tools/perfect_continuation_skill_check.py --phase post --write-report audits/CHECK_REPORT.md

Exit code:
- 0 = PASS
- 1 = FAIL
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "foundation/CURRENT_STATE_MANIFEST.json"
STATUS_REL = "foundation/STATUS_PANEL.md"

DEFAULT_ACTIVE_DIRS = ["foundation", "bible", "codex"]
DEFAULT_TOP_LEVEL_ACTIVE = [
    "README.md",
    "HANDOFF.md",
    "MASTER_PROJECT_BIBLE.md",
    "PROJECT_FILE_CLASSIFICATION_AND_SOURCE_OF_TRUTH.md",
    "YAN_SHUO_CURRENT_STATUS_PANEL.md",
    "YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md",
]

CORE_REGISTRATION_FILES = [
    "foundation/STATUS_PANEL.md",
    "README.md",
    "HANDOFF.md",
    "PROJECT_FILE_CLASSIFICATION_AND_SOURCE_OF_TRUTH.md",
]

STATIC_BODY_FORBIDDEN = [
    "SP526",
    "Rainbow Dragon",
    "Dragon Queen necklace",
    "Phoenix God authority",
    "Phoenix Domain",
    "Nirvana",
    "Martial Soul True Body",
    "five-coloured Phoenix",
    "five-colored Phoenix",
    "public Yan Shuo’er reveal",
    "public Yan Shuo'er reveal",
]

DEFAULT_ALLOWED_HISTORICAL_CONTEXT_PATTERNS = [
    r"historical",
    r"old",
    r"superseded",
    r"endpoint",
    r"Chapter\d+ completed",
    r"Chapter_\d+\.md \|",
    r"at the Chapter\d+ endpoint",
    r"Coverage table",
    r"As of this skill creation",
    r"Example after Chapter\d+",
    r"For future chapters",
]


@dataclass
class ProjectState:
    latest_fic: int
    next_fic: int
    consumed_source: int
    next_source: int
    latest_title: str | None = None
    consumed_title: str | None = None
    next_title: str | None = None


def rel_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="ignore")


def load_manifest() -> dict[str, Any]:
    path = ROOT / MANIFEST_REL
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # keep checker useful even if JSON breaks
        return {"__manifest_error__": str(exc)}


def infer_state_from_status(status: str) -> ProjectState | None:
    latest = None
    latest_title = None
    m = re.search(r"Latest prose:\s*`chapters/Chapter_(\d+)\.md`\s*—\s*\*\*(.*?)\*\*", status)
    if m:
        latest = int(m.group(1))
        latest_title = m.group(2).strip()
    else:
        m = re.search(r"Live edge:\s*\*\*after Chapter(\d+)\b", status)
        if m:
            latest = int(m.group(1))

    consumed = None
    consumed_title = None
    m = re.search(r"Canon consumed through[^\n]*?Chapter(\d+)\s*`([^`]+)`", status, re.I)
    if m:
        consumed = int(m.group(1))
        consumed_title = m.group(2)
    else:
        m = re.search(r"Canon consumed through[^\n]*?Chapter(\d+)", status, re.I)
        if m:
            consumed = int(m.group(1))

    next_source = None
    next_title = None
    m = re.search(r"Next source(?: boundary)?:[^\n]*?Chapter(\d+)\s*`([^`]+)`", status, re.I)
    if m:
        next_source = int(m.group(1))
        next_title = m.group(2)
    else:
        m = re.search(r"Next source(?: boundary)?:[^\n]*?Chapter(\d+)", status, re.I)
        if m:
            next_source = int(m.group(1))

    if latest is None or next_source is None:
        return None
    if consumed is None:
        consumed = next_source - 1
    return ProjectState(
        latest_fic=latest,
        next_fic=latest + 1,
        consumed_source=consumed,
        next_source=next_source,
        latest_title=latest_title,
        consumed_title=consumed_title,
        next_title=next_title,
    )


def state_from_manifest(manifest: dict[str, Any]) -> ProjectState | None:
    try:
        latest = int(manifest["latest_fic_chapter"])
        next_fic = int(manifest.get("next_fic_chapter", latest + 1))
        consumed = int(manifest.get("canon_consumed_through", {}).get("chapter"))
        next_source = int(manifest.get("next_source", {}).get("chapter"))
        return ProjectState(
            latest_fic=latest,
            next_fic=next_fic,
            consumed_source=consumed,
            next_source=next_source,
            latest_title=manifest.get("latest_fic_title"),
            consumed_title=manifest.get("canon_consumed_through", {}).get("title"),
            next_title=manifest.get("next_source", {}).get("title"),
        )
    except Exception:
        return None


def merge_state(cli_latest: int | None, cli_next_source: int | None, manifest: dict[str, Any], status: str) -> tuple[ProjectState | None, list[str]]:
    notes: list[str] = []
    m_state = state_from_manifest(manifest) if manifest else None
    s_state = infer_state_from_status(status)
    state = m_state or s_state
    if state is None:
        return None, ["Could not infer state from manifest or STATUS_PANEL"]

    if cli_latest is not None:
        state.latest_fic = cli_latest
        state.next_fic = cli_latest + 1
    if cli_next_source is not None:
        state.next_source = cli_next_source
        state.consumed_source = cli_next_source - 1

    if m_state and s_state:
        if m_state.latest_fic != s_state.latest_fic:
            notes.append(f"manifest/status latest mismatch: manifest Chapter{m_state.latest_fic}, status Chapter{s_state.latest_fic}")
        if m_state.next_source != s_state.next_source:
            notes.append(f"manifest/status next-source mismatch: manifest Chapter{m_state.next_source}, status Chapter{s_state.next_source}")
        if m_state.consumed_source != s_state.consumed_source:
            notes.append(f"manifest/status consumed-source mismatch: manifest Chapter{m_state.consumed_source}, status Chapter{s_state.consumed_source}")
    return state, notes


def active_files(manifest: dict[str, Any]) -> list[Path]:
    dirs = manifest.get("active_markdown_dirs") or DEFAULT_ACTIVE_DIRS
    tops = manifest.get("top_level_active_files") or DEFAULT_TOP_LEVEL_ACTIVE
    files: list[Path] = []
    for folder in dirs:
        d = ROOT / folder
        if d.exists():
            files.extend(sorted(d.rglob("*.md")))
    for rel in tops:
        p = ROOT / rel
        if p.exists() and p not in files:
            files.append(p)
    return files


def story_body(chapter_path: Path) -> str:
    txt = chapter_path.read_text(encoding="utf-8", errors="ignore")
    marker = "\n---\n\n## Footer"
    return txt.split(marker, 1)[0] if marker in txt else txt


def context_for(lines: list[str], index: int, radius: int = 4) -> str:
    return "\n".join(lines[max(0, index - radius): min(len(lines), index + radius + 1)])


def compile_patterns(patterns: list[str]) -> list[re.Pattern[str]]:
    compiled = []
    for pat in patterns:
        try:
            compiled.append(re.compile(pat, re.I))
        except re.error:
            # Treat broken manifest regex as a checker issue elsewhere; don't crash here.
            pass
    return compiled


def allowed_historical(rel: str, line: str, context: str, manifest: dict[str, Any]) -> bool:
    # Canon ledger is an event ledger; old per-event "Current after ChapterN" lines are historical receipts,
    # not live-state instructions. The top current block is still checked normally when it matches latest.
    if rel == "foundation/CANON_LEDGER.md" and re.search(r"Current after Chapter\d+", line, re.I):
        return True
    patterns = list(DEFAULT_ALLOWED_HISTORICAL_CONTEXT_PATTERNS)
    patterns.extend(manifest.get("allowed_historical_context_patterns") or [])
    hay = f"{rel}\n{context}\n{line}"
    return any(re.search(pat, hay, re.I) for pat in patterns)


def add(issues: list[str], rel: str, detail: str) -> None:
    issues.append(f"{rel}: {detail}")


def check_file_exists_and_pass(issues: list[str], rel: str, label: str) -> None:
    p = ROOT / rel
    if not p.exists():
        add(issues, rel, f"{label} missing")
        return
    if "PASS" not in p.read_text(encoding="utf-8", errors="ignore"):
        add(issues, rel, f"{label} lacks PASS")


def check_artifacts(issues: list[str], state: ProjectState, manifest: dict[str, Any], phase: str) -> None:
    latest_file = manifest.get("latest_fic_file") or f"chapters/Chapter_{state.latest_fic}.md"
    coverage_file = manifest.get("latest_coverage_file") or f"canon_coverage/Canon_Coverage_Chapter_{state.latest_fic}.md"
    for rel, label in [(latest_file, "latest prose"), (coverage_file, "latest coverage")]:
        if not (ROOT / rel).exists():
            add(issues, rel, f"{label} missing")
    if (ROOT / coverage_file).exists() and "PASS" not in read_text(coverage_file):
        add(issues, coverage_file, "latest coverage lacks PASS")

    # In post/audit phase, latest validation and support-sync must exist and PASS.
    if phase in {"post", "audit"}:
        val_glob = manifest.get("validation_audit_glob") or f"audits/CHAPTER_{state.latest_fic}_VALIDATION_*.md"
        sync_glob = manifest.get("support_sync_audit_glob") or f"audits/CHAPTER_{state.latest_fic}_SUPPORT_SYNC_*.md"
        for glob_pat, label in [(val_glob, "validation audit"), (sync_glob, "support sync audit")]:
            matches = sorted(ROOT.glob(glob_pat))
            if not matches:
                add(issues, glob_pat, f"{label} missing")
            elif not any("PASS" in p.read_text(encoding="utf-8", errors="ignore") for p in matches):
                add(issues, glob_pat, f"no {label} contains PASS")


def check_manifest_and_status(issues: list[str], state: ProjectState, manifest: dict[str, Any], status: str, state_notes: list[str]) -> None:
    if manifest.get("__manifest_error__"):
        add(issues, MANIFEST_REL, f"manifest JSON error: {manifest['__manifest_error__']}")
    if not manifest:
        add(issues, MANIFEST_REL, "manifest missing; Level-2 checker requires it")

    for note in state_notes:
        add(issues, f"{MANIFEST_REL} / {STATUS_REL}", note)

    required = manifest.get("required_status_patterns") or []
    if not required:
        required = [
            rf"Live edge:.*after Chapter{state.latest_fic}",
            rf"Chapter_{state.latest_fic}\.md",
            rf"Chapter{state.consumed_source}",
            rf"Chapter{state.next_source}",
            r"low Soul King-class effective threat floor",
        ]
    for pat in required:
        try:
            if not re.search(pat, status, re.I | re.S):
                add(issues, STATUS_REL, f"missing required status pattern `{pat}`")
        except re.error as exc:
            add(issues, MANIFEST_REL, f"bad required_status_patterns regex `{pat}`: {exc}")

    # Hard status sanity independent of manifest.
    hard = [
        rf"Live edge:\s*\*\*after Chapter{state.latest_fic}\b",
        rf"Latest prose:\s*`chapters/Chapter_{state.latest_fic}\.md`",
        rf"Canon consumed through[^\n]*Chapter{state.consumed_source}",
        rf"Next source(?: boundary)?:[^\n]*Chapter{state.next_source}",
    ]
    for pat in hard:
        if not re.search(pat, status, re.I):
            add(issues, STATUS_REL, f"missing hard status pattern `{pat}`")


def check_mirrors(issues: list[str], status: str) -> None:
    for rel in ["YAN_SHUO_CURRENT_STATUS_PANEL.md", "YAN_SHUO_COMPLETE_CURRENT_STATUS_PANEL.md"]:
        p = ROOT / rel
        if not p.exists():
            add(issues, rel, "status mirror missing")
        elif p.read_text(encoding="utf-8", errors="ignore") != status:
            add(issues, rel, "does not exactly mirror foundation/STATUS_PANEL.md")


def check_registration(issues: list[str]) -> None:
    needed = [
        "foundation/PERFECT_CONTINUATION_SKILL.md",
        "foundation/CURRENT_STATE_MANIFEST.json",
        "tools/perfect_continuation_skill_check.py",
    ]
    for rel in needed:
        if not (ROOT / rel).exists():
            add(issues, rel, "registered skill asset missing")
    for rel in CORE_REGISTRATION_FILES:
        p = ROOT / rel
        if not p.exists():
            add(issues, rel, "core registration file missing")
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for needle in needed:
            if needle not in txt:
                add(issues, rel, f"does not reference `{needle}`")


def dynamic_stale_checks_for_line(line: str, context: str, state: ProjectState) -> list[str]:
    problems: list[str] = []

    def chapter_num(regex: str) -> int | None:
        m = re.search(regex, line, re.I)
        return int(m.group(1)) if m else None

    n = chapter_num(r"Live edge:[^\n]*Chapter(\d+)")
    if n is not None and n != state.latest_fic:
        problems.append(f"live edge points to Chapter{n}, expected Chapter{state.latest_fic}")

    n = chapter_num(r"Latest (?:prose|chapter):[^\n]*Chapter_(\d+)\.md")
    if n is not None and n != state.latest_fic:
        problems.append(f"latest prose/chapter points to Chapter_{n}.md, expected Chapter_{state.latest_fic}.md")

    n = chapter_num(r"Latest coverage:[^\n]*Canon_Coverage_Chapter_(\d+)\.md")
    if n is not None and n != state.latest_fic:
        problems.append(f"latest coverage points to Chapter{n}, expected Chapter{state.latest_fic}")

    n = chapter_num(r"Latest validation:[^\n]*CHAPTER_(\d+)_VALIDATION")
    if n is not None and n != state.latest_fic:
        problems.append(f"latest validation points to Chapter{n}, expected Chapter{state.latest_fic}")

    n = chapter_num(r"Latest support sync:[^\n]*CHAPTER_(\d+)_SUPPORT_SYNC")
    if n is not None and n != state.latest_fic:
        problems.append(f"latest support sync points to Chapter{n}, expected Chapter{state.latest_fic}")

    # Current after old/future chapter is stale unless clearly historical.
    for m in re.finditer(r"Current(?:-| )?(?:controlling state |status |scene |values |valid measurements |state rule )?after Chapter(\d+)\b", line, re.I):
        n = int(m.group(1))
        if n != state.latest_fic:
            problems.append(f"current-state heading/block says after Chapter{n}, expected Chapter{state.latest_fic}")

    n = chapter_num(r"Current Chapter(\d+) state summary")
    if n is not None and n != state.latest_fic:
        problems.append(f"current-state summary says Chapter{n}, expected Chapter{state.latest_fic}")

    # Source boundary lines.
    for m in re.finditer(r"Canon consumed through[^\n]*?Chapter(\d+)", line, re.I):
        n = int(m.group(1))
        if n != state.consumed_source:
            problems.append(f"canon-consumed line says Chapter{n}, expected Chapter{state.consumed_source}")

    for m in re.finditer(r"Latest consumed source:[^\n]*?Chapter(\d+)", line, re.I):
        n = int(m.group(1))
        if n != state.consumed_source:
            problems.append(f"latest-consumed-source line says Chapter{n}, expected Chapter{state.consumed_source}")

    for m in re.finditer(r"Next (?:canon )?source(?: boundary)?:[^\n]*?Chapter(\d+)", line, re.I):
        n = int(m.group(1))
        if n != state.next_source:
            problems.append(f"next-source line says Chapter{n}, expected Chapter{state.next_source}")

    # Next fic chapter protocol lines.
    for m in re.finditer(r"Chapter(\d+) should (?:continue|consume|start|begin|use)", line, re.I):
        n = int(m.group(1))
        if n != state.next_fic:
            problems.append(f"next-fic instruction says Chapter{n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"For Chapter(\d+):", line, re.I):
        n = int(m.group(1))
        if n != state.next_fic:
            problems.append(f"protocol says For Chapter{n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"Chapter(\d+) (?:is|was)? ?(?:the )?next required source for Chapter(\d+)|Next source for Chapter(\d+)", line, re.I):
        # Handles old phrases like "Chapter172 is the next required source for Chapter50" or "Next source for Chapter50".
        nums = [int(g) for g in m.groups() if g]
        if nums:
            if len(nums) >= 2:
                source_n, fic_n = nums[0], nums[1]
                if source_n != state.next_source or fic_n != state.next_fic:
                    problems.append(f"next-source/protocol pair says source Chapter{source_n} for fic Chapter{fic_n}, expected source Chapter{state.next_source} for fic Chapter{state.next_fic}")
            else:
                fic_n = nums[0]
                if fic_n != state.next_fic:
                    problems.append(f"next-source protocol says fic Chapter{fic_n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"Chapter(\d+).*guard|Before writing Chapter(\d+)|only active next-chapter prose guard is Chapter(\d+)", line, re.I):
        nums = [int(g) for g in m.groups() if g]
        for n in nums:
            if n != state.next_fic:
                problems.append(f"chapter guard/protocol points to Chapter{n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"Current open item for Chapter(\d+)", line, re.I):
        n = int(m.group(1))
        if n != state.next_fic:
            problems.append(f"open item says Chapter{n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"Fetch(?:/verify)? Chapter(\d+)", line, re.I):
        n = int(m.group(1))
        if n != state.next_source:
            problems.append(f"fetch instruction says source Chapter{n}, expected Chapter{state.next_source}")

    for m in re.finditer(r"Canon_Coverage_Chapter_(\d+)\.md`? before prose", line, re.I):
        n = int(m.group(1))
        if n != state.next_fic:
            problems.append(f"coverage-before-prose instruction says Chapter{n}, expected Chapter{state.next_fic}")

    for m in re.finditer(r"chapters/Chapter_(\d+)\.md`? (?:only )?(?:from|before|after|using)", line, re.I):
        n = int(m.group(1))
        # latest artifact lines say Latest prose and are handled above; protocol lines should be next fic.
        if "Latest prose" not in line and "Latest chapter" not in line and n <= state.latest_fic:
            problems.append(f"chapter-writing protocol points to already-written Chapter{n}, expected future Chapter{state.next_fic}")

    return problems


def check_active_files(issues: list[str], state: ProjectState, manifest: dict[str, Any]) -> None:
    stale_specs = manifest.get("active_stale_regexes") or []
    compiled_stale: list[tuple[str, re.Pattern[str]]] = []
    for spec in stale_specs:
        try:
            compiled_stale.append((spec.get("id", "manifest_stale_regex"), re.compile(spec["regex"], re.I)))
        except Exception as exc:
            add(issues, MANIFEST_REL, f"bad active_stale_regex spec {spec}: {exc}")

    for path in active_files(manifest):
        rel = rel_path(path)
        txt = path.read_text(encoding="utf-8", errors="ignore")
        lines = txt.splitlines()
        for idx, line in enumerate(lines):
            context = context_for(lines, idx)
            if allowed_historical(rel, line, context, manifest):
                continue

            for problem in dynamic_stale_checks_for_line(line, context, state):
                add(issues, rel, f"L{idx+1}: {problem}: {line[:260]}")

            for name, regex in compiled_stale:
                if regex.search(line):
                    add(issues, rel, f"L{idx+1}: {name}: {line[:260]}")


def check_key_support(issues: list[str], state: ProjectState, manifest: dict[str, Any]) -> None:
    files = manifest.get("key_support_files") or [
        "README.md",
        "HANDOFF.md",
        "MASTER_PROJECT_BIBLE.md",
        "PROJECT_FILE_CLASSIFICATION_AND_SOURCE_OF_TRUTH.md",
        "foundation/OPEN.md",
        "foundation/CANON_SOURCE_NUMBERING_MAP.md",
        "canon_coverage/CANON_COVERAGE_INDEX.md",
        "codex/CHAPTER_PROGRESS.md",
    ]
    patterns = manifest.get("key_support_priority_patterns") or [
        rf"Chapter_{state.latest_fic}\.md",
        rf"Chapter{state.consumed_source}",
        rf"Chapter{state.next_source}",
        r"low Soul King-class effective threat floor",
    ]
    for rel in files:
        p = ROOT / rel
        if not p.exists():
            add(issues, rel, "key support file missing")
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for pat in patterns:
            try:
                if not re.search(pat, txt, re.I | re.S):
                    add(issues, rel, f"missing key support pattern `{pat}`")
            except re.error as exc:
                add(issues, MANIFEST_REL, f"bad key_support_priority_patterns regex `{pat}`: {exc}")


def check_latest_story_body(issues: list[str], state: ProjectState, manifest: dict[str, Any]) -> None:
    rel = manifest.get("latest_fic_file") or f"chapters/Chapter_{state.latest_fic}.md"
    path = ROOT / rel
    if not path.exists():
        return
    body = story_body(path)

    # Manifest + static literal bans.
    forbidden_literals = list(dict.fromkeys(STATIC_BODY_FORBIDDEN + (manifest.get("latest_story_body_forbidden_literals") or [])))
    for literal in forbidden_literals:
        if literal and literal in body:
            add(issues, rel, f"forbidden story-body literal `{literal}`")

    # Dynamic next-source spillover ban in story body.
    for literal in [f"Chapter{state.next_source}", f"Chapter {state.next_source}", state.next_title or ""]:
        if literal and literal in body:
            add(issues, rel, f"next-source spillover in story body `{literal}`")

    if "Yan Shuo’er" in body or "Yan Shuo'er" in body:
        add(issues, rel, "private Yan Shuo'er name appears in story body")

    # Manifest body regex bans.
    for pat in manifest.get("latest_story_body_forbidden_regexes") or []:
        try:
            if re.search(pat, body, re.I | re.S):
                add(issues, rel, f"forbidden story-body regex `{pat}`")
        except re.error as exc:
            add(issues, MANIFEST_REL, f"bad latest_story_body_forbidden_regexes `{pat}`: {exc}")

    # Manifest body required patterns for the latest chapter.
    for pat in manifest.get("latest_story_body_required_patterns") or []:
        try:
            if not re.search(pat, body, re.I | re.S):
                add(issues, rel, f"missing required latest-story-body pattern `{pat}`")
        except re.error as exc:
            add(issues, MANIFEST_REL, f"bad latest_story_body_required_patterns `{pat}`: {exc}")


def write_report(path: str, passed: bool, state: ProjectState | None, issues: list[str], phase: str) -> None:
    p = ROOT / path if not Path(path).is_absolute() else Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Perfect Continuation Skill Check Report",
        "",
        f"Phase: `{phase}`",
        f"Result: **{'PASS' if passed else 'FAIL'}**",
        "",
    ]
    if state:
        lines.extend([
            f"- Latest fic chapter: Chapter{state.latest_fic}",
            f"- Next fic chapter: Chapter{state.next_fic}",
            f"- Canon consumed through: Chapter{state.consumed_source}",
            f"- Next source: Chapter{state.next_source}",
            "",
        ])
    lines.append(f"Issues: {len(issues)}")
    if issues:
        lines.append("")
        for item in issues:
            lines.append(f"- {item}")
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--latest", type=int, default=None, help="expected latest fic chapter number; overrides manifest/status")
    ap.add_argument("--next-source", type=int, default=None, help="expected next NovelFull/WebNovel source chapter number; overrides manifest/status")
    ap.add_argument("--phase", choices=["pre", "post", "audit"], default="post", help="pre=before drafting next chapter; post=after support sync; audit=full audit receipt")
    ap.add_argument("--write-report", default=None, help="optional markdown report path")
    args = ap.parse_args()

    issues: list[str] = []

    status_path = ROOT / STATUS_REL
    if not status_path.exists():
        issues.append(f"{STATUS_REL}: missing")
        print("PERFECT_CONTINUATION_SKILL_CHECK_V2: FAIL")
        print("issues=1")
        print("ISSUE", issues[0])
        return 1

    manifest = load_manifest()
    status = read_text(STATUS_REL)
    state, notes = merge_state(args.latest, args.next_source, manifest, status)
    if state is None:
        issues.extend(notes)
        if args.write_report:
            write_report(args.write_report, False, None, issues, args.phase)
        print("PERFECT_CONTINUATION_SKILL_CHECK_V2: FAIL")
        print(f"issues={len(issues)}")
        for item in issues:
            print("ISSUE", item)
        return 1

    check_manifest_and_status(issues, state, manifest, status, notes)
    check_artifacts(issues, state, manifest, args.phase)
    check_mirrors(issues, status)
    check_registration(issues)
    check_active_files(issues, state, manifest)
    check_key_support(issues, state, manifest)
    check_latest_story_body(issues, state, manifest)

    passed = not issues
    if args.write_report:
        write_report(args.write_report, passed, state, issues, args.phase)

    if not passed:
        print("PERFECT_CONTINUATION_SKILL_CHECK_V2: FAIL")
        print(f"issues={len(issues)}")
        for item in issues:
            print("ISSUE", item)
        return 1

    print("PERFECT_CONTINUATION_SKILL_CHECK_V2: PASS")
    print(f"phase={args.phase}")
    print(f"latest=Chapter{state.latest_fic}")
    print(f"next_fic=Chapter{state.next_fic}")
    print(f"consumed_source=Chapter{state.consumed_source}")
    print(f"next_source=Chapter{state.next_source}")
    print("manifest_loaded=YES")
    print("active_stale_issues=0")
    print("mirrors_match=YES")
    print("future_route_body_leaks=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
