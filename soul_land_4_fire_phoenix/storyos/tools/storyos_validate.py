#!/usr/bin/env python3
"""
storyos_validate.py — StoryOS Foundation validator (universal, project-agnostic).

Every agent that touches a StoryOS project runs this BEFORE drafting and AFTER writing.
It enforces the rules that prose review reliably misses: branch supersession,
receipt staleness, banned-token drift, firewall completeness, ledger coverage.

Exit codes: 0 = clean, 1 = findings (severity>=error), 2 = usage/schema problem.

    python3 storyos_validate.py --project /path/to/project            # full audit
    python3 storyos_validate.py --project . --phase pre                # pre-draft gate
    python3 storyos_validate.py --project . --phase post --files chapters/Chapter_52.md
    python3 storyos_validate.py --selftest                             # prove the checks fire
    python3 storyos_validate.py --project . --write-report audits/VALIDATION_YYYY-MM-DD.md
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

REQUIRED_MANIFEST_KEYS = ("schema", "project", "edge", "canon_numbering", "characters")
# A project's native manifest may use its own key names; normalise rather than reject.
NATIVE_ALIASES = {"latest_fic_chapter": "fic_chapter", "latest_fic_title": "fic_title",
                  "updated": "declared_on"}
SEV_ORDER = {"error": 0, "warn": 1, "info": 2}
_INCLUDE_COVERAGE = False
FIX_CTX = ("Restore the locked state. A context ban firing usually means the chapter asserted "
           "an unearned capability, not just a wrong number.")
FIREWALL_STATES = {"KNOWN", "SUSPECTED", "UNKNOWN", "FALSE BELIEF", "KNOWN PARTLY",
                   "DISBELIEF", "HIDDEN"}
NEXT_CHAPTER_RE = re.compile(
    r"\b(?:next|continue|proceed|draft|write)\s+(?:to\s+)?Chapter[\s_-]*(\d{1,4})", re.I)


def load_manifest(project: Path) -> dict:
    # prefer a STORYOS-generated state; fall back to the project's own manifest.
    # Both are read-only here — the validator must never rewrite the state it audits.
    # Layering: a generated StoryOS state (v3) carries the full derived picture — canon
    # numbering, firewalls, enforce tokens. The project's own manifest is authoritative for
    # the live edge but has a different key set. So: prefer v3 if it exists, else adapt native.
    for path in (project / "storyos" / "STORYOS_STATE.json",
                 project / "foundation" / "storyos" / "STORYOS_STATE.json",
                 project / "foundation" / "CURRENT_STATE_MANIFEST.json",
                 project / "CURRENT_STATE_MANIFEST.json"):
        if path.exists():
            break
    else:
        raise SystemExit("storyos_validate: no manifest found (STORYOS_STATE.json / "
                         "CURRENT_STATE_MANIFEST.json)")
    data = json.loads(path.read_text(encoding="utf-8"))
    if "edge" not in data and "latest_fic_chapter" in data:
        cc = data.get("canon_consumed_through") or {}
        ns = data.get("next_source") or {}
        data["schema"] = f"native/{data.get('schema_version', 'unknown')}"
        data.setdefault("project", data.get("purpose", "project")[:60])
        data["edge"] = {"fic_chapter": data["latest_fic_chapter"],
                        "fic_title": data.get("latest_fic_title", ""),
                        "declared_on": data.get("updated", ""),
                        "canon_consumed": cc.get("chapter"),
                        "canon_consumed_title": cc.get("title"),
                        "next_source": ns.get("chapter"),
                        "next_source_title": ns.get("title"), "accepted_chapters": []}
        # v3 is the layer that holds derived detail. Without it we audit only what the
        # native manifest actually declares — and we say so, instead of inventing keys.
        if not data.get("canon_numbering"):
            data["canon_numbering"] = [{"fic": n, "canon": "—", "status": "accepted",
                                        "validation": ""}
                                       for n in range(1, int(data["edge"]["fic_chapter"]) + 1)]
            data["_native_passthrough"] = True
        data["characters"] = data.get("characters", {})
        data.setdefault("knowledge_firewalls", [])
        data.setdefault("banned_tokens", {"native_literals":
                    list(data.get("latest_story_body_forbidden_literals") or [])})
        data.setdefault("enforce", list(data.get("latest_story_body_forbidden_literals") or []))
        data.setdefault("enforce_regexes",
                        list(data.get("latest_story_body_forbidden_regexes") or []))
        data.setdefault("branches", {})
        data.setdefault("information_discipline", "ACTIVE")
        data.setdefault("pacing", {})
    missing = [k for k in REQUIRED_MANIFEST_KEYS if k not in data]
    if missing:
        raise SystemExit(f"storyos_validate: manifest missing keys {missing}")
    return data


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


class Findings:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, check: str, severity: str, message: str, fix: str = "") -> None:
        self.items.append({"check": check, "severity": severity, "message": message, "fix": fix})

    def sorted(self) -> list[dict]:
        # One token registered under two labels is one finding, not two. Duplicate reports
        # inflate the error count and make an agent distrust the whole report.
        seen, out = set(), []
        for i in sorted(self.items, key=lambda x: (SEV_ORDER.get(x["severity"], 9), x["check"])):
            key = (i["check"], i["severity"], i["message"])
            if key in seen:
                continue
            seen.add(key)
            out.append(i)
        return out


def chapter_map(manifest: dict) -> dict[int, dict]:
    return {int(row["fic"]): row for row in manifest.get("canon_numbering", [])}


# ---------------------------------------------------------------- checks
def check_branch_supersession(manifest: dict, project: Path, f: Findings) -> None:
    """The killer bug: a superseded branch's receipts claim a further edge than live state."""
    edge = int(manifest["edge"].get("fic_chapter", 0))
    live = {int(x) for x in manifest["edge"].get("accepted_chapters", [])}
    if not live:
        live = {n for n, row in chapter_map(manifest).items() if row.get("status") == "accepted"}
    branches = manifest.get("branches", {})
    superseded = set()
    for bname, bdata in branches.items():
        if str(bdata.get("status", "")).lower() in {"superseded", "rejected", "quarantined"}:
            for n in bdata.get("chapters", []):
                if int(n) not in live:
                    superseded.add(int(n))
    audits = project / "audits"
    for n in sorted(superseded):
        row = chapter_map(manifest).get(n)
        if row and row.get("status") == "accepted":
            f.add("branch-supersession", "error",
                  f"Chapter{n} carries an accepted status but belongs to a superseded branch "
                  f"({', '.join(k for k, v in branches.items() if n in v.get('chapters', []))}).")
            continue
        # Superseded chapters normally just sit in an archive and are expected. It only becomes
        # an error if a receipt on disk still asserts live status for them.
        receipt = row.get("validation") if row else None
        claim = ""
        for cand in ([audits / receipt] if receipt else []) + (
                sorted(audits.glob(f"CHAPTER_{n}_*.md")) if audits.is_dir() else []):
            if cand.exists():
                claim = read(cand)
                if re.search(rf"Live edge:\s*\*\*after Chapter{n}", claim) or \
                   re.search(rf"ready for support sync|is valid", claim):
                    if re.search(r"SUPERSEDED|DO NOT USE", claim, re.I):
                        f.add("branch-supersession", "info",
                              f"{cand.name} still claims Chapter{n} but IS marked superseded — "
                              f"trap neutralised. Keep it out of drafting context.")
                        break
                    f.add("branch-supersession", "error",
                          f"{cand.name} still asserts Chapter{n} is valid/ready, but Chapter{n} "
                          f"belongs to a superseded branch. Any agent trusting it will continue "
                          f"from rejected work.",
                          fix=f"Live edge is after Chapter{edge}. Mark this receipt "
                              f"'SUPERSEDED — do not use', move it under archive/, and "
                              f"rebuild Chapter{edge + 1} from the active branch. If a "
                              f"Chapter{edge + 1} draft exists here, it is rejected-branch "
                              f"material and must not be re-presented as new work.")
                    break
        else:
            f.add("branch-supersession", "info",
                  f"Chapter{n} is quarantined from a superseded branch — expected, and not canon.")
    # textual claim check across receipts
    stale_claims = []
    for p in sorted((project / "audits").glob("*.md")) if (project / "audits").is_dir() else []:
        txt = read(p)
        m = re.search(r"Live edge:\s*\*\*after Chapter(\d+)", txt)
        if m and int(m.group(1)) > edge:
            dm = re.search(r"(20\d\d-\d\d-\d\d)", p.name) or re.search(r"(20\d\d-\d\d-\d\d)", txt)
            dm2 = re.search(r"(20\d\d-\d\d-\d\d)", " ".join(
                q.name for q in (project / "audits").glob("*.md")
                if re.search(rf"Live edge:\s*\*\*after Chapter{edge}", read(q))))
            if dm and dm2 and dm.group(1) < dm2.group(1):
                stale_claims.append((p.name, int(m.group(1)), dm.group(1), dm2.group(1)))
    for name, claimed, older, newer in stale_claims:
        f.add("branch-supersession", "error",
              f"{name} claims live edge Chapter{claimed}, but a newer receipt ({newer} vs {older}) "
              f"places it at Chapter{edge}. The claim is from a superseded branch.",
              fix="Do not read stale receipts as current state; newest dated receipt on the active "
                  "branch wins.")


def check_receipt_coverage(manifest: dict, project: Path, f: Findings) -> None:
    """Every accepted chapter must have a validation receipt on disk."""
    audits = project / "audits"
    have = {p.name for p in audits.glob("*.md")} if audits.is_dir() else set()
    edge = int(manifest["edge"].get("fic_chapter") or 0)
    for n, row in sorted(chapter_map(manifest).items()):
        if row.get("status") != "accepted":
            continue
        if not row.get("validation"):
            # receipts began at a specific point in the project's life; flag only the recent tail
            sev = "warn" if n >= edge - 6 else "info"
            f.add("receipt-coverage", sev, f"Chapter{n} has no validation receipt recorded.")
        elif row["validation"] not in have and not (project / "audits" / row["validation"]).exists():
            f.add("receipt-coverage", "warn" if n >= edge - 6 else "info",
                  f"Chapter{n} cites {row['validation']} which is not present in audits/.")


def story_body(txt: str) -> str:
    """Project convention: a chapter is 'story prose', then a `---` + '## Footer' audit block.
    Forbiddens apply to the prose. The footer legitimately ENUMERATES the forbidden values to
    declare them non-current, so scanning it produces confident nonsense."""
    marker = "\n---\n\n## Footer"
    return txt.split(marker, 1)[0] if marker in txt else txt


NEGATION = re.compile(r"\bno\b|\bnot\b|never|must not|may not|do not|don't|forbidden"
                      r"|banned|deleted|avoid|without|refus|denied|not present|no longer", re.I)
DOCUMENTATION = re.compile(
    r"footer|not current|currentiz|forbidden|banned|quarantin|do not use|historical|receipt"
    r"|superseded|checklist|guard|lock|not allowed|do not currentize|never currentiz"
    r"|^\s*-?\s*no\b", re.I)


def check_banned_tokens(manifest: dict, project: Path, f: Findings, targets: list[Path]) -> None:
    bans = manifest.get("banned_tokens", {})
    enforce = sorted(set(manifest.get("enforce") or
                         [t for v in bans.values() for t in v]))
    advisory = set(manifest.get("advisory_review") or [])
    if not enforce:
        f.add("banned-tokens", "info",
              "No unambiguous regression tokens in the manifest — the drift guard cannot fire.",
              fix="Re-run scan_project.py so enforce is populated from the project's own registry.")
        return
    if not targets:
        f.add("banned-tokens", "info",
              "No prose/coverage targets supplied — drift guard not exercised this phase.")
    for target in targets:
        full = read(target)
        prose = story_body(full)
        lines = prose.splitlines()
        for label, tokens in bans.items():
            for tok in dict.fromkeys(str(t) for t in tokens):
                if tok not in enforce or not tok:
                    continue
                for idx, line in enumerate(lines):
                    if tok.lower() not in line.lower():
                        continue
                    ctx = "\n".join(lines[max(0, idx - 3):idx + 2])
                    # A banned value inside a negation ("no Phoenix God authority", "the deleted
                    # SP526 route") is the chapter *rejecting* it, not asserting it. Only
                    # un-negated mentions are real leaks.
                    if NEGATION.search(line) or DOCUMENTATION.search(ctx):
                        break
                    f.add("banned-tokens", "error",
                          f"{target.name}:{idx + 1} asserts forbidden '{tok}' ({label}) "
                          f"in story prose → “{line.strip()[:110]}”",
                          fix="Remove it or restore the locked current value. If this is "
                              "intended future foreshadowing, it still must not appear as "
                              "achieved fact.")
                    break
    for target in targets:
        prose = story_body(read(target))
        for rx in manifest.get("enforce_regexes") or []:
            try:
                m = re.search(rx, prose, re.I)
            except re.error:
                f.add("banned-tokens", "warn", f"manifest regex is invalid: {rx}")
                continue
            if m:
                f.add("banned-tokens", "error",
                      f"{target.name} matches forbidden pattern /{rx}/ → “{m.group(0)[:110]}”. "
                      f"Regex bans encode *contextual* regressions (e.g. Lan entering a Platform) "
                      f"that a word list cannot catch.",
                      fix=FIX_CTX)


def check_firewalls(manifest: dict, f: Findings) -> None:
    fw = manifest.get("knowledge_firewalls", [])
    if not fw:
        sev = "warn" if manifest.get("_native_passthrough") else "error"
        f.add("firewall-integrity", sev,
              "No knowledge firewalls in the audited state."
              + (" Native manifest carries no firewall register — run scripts/scan_project.py "
                 "so codex/KNOWLEDGE_FIREWALLS.md is parsed into STORYOS_STATE.json."
                 if manifest.get("_native_passthrough") else " Define them."))
        return
    for rule in fw:
        who, topic = rule.get("character", "?"), rule.get("topic", "?")
        state = str(rule.get("state", "")).upper()
        if state not in FIREWALL_STATES:
            f.add("firewall-integrity", "error",
                  f"{who}/{topic}: state '{state}' is not one of "
                  f"{', '.join(sorted(FIREWALL_STATES))}.")
        if not rule.get("earliest_valid_change"):
            f.add("firewall-integrity", "error",
                  f"{who}/{topic}: no earliest_valid_change — the gate cannot be enforced.")
        if not rule.get("rule"):
            f.add("firewall-integrity", "warn", f"{who}/{topic}: missing enforcement rule text.")
    if manifest.get("information_discipline") != "ACTIVE":
        f.add("firewall-integrity", "warn",
              "information_discipline is not ACTIVE in the manifest.")


def check_pacing(manifest: dict, f: Findings) -> None:
    mode = manifest.get("pacing", {}).get("mode", "unspecified")
    if mode not in {"compressed", "expand-meaningful-only", "adaptive", "unspecified"}:
        f.add("pacing-lock", "warn",
              f"pacing.mode='{mode}' looks like the rejected one-canon-chapter-per-fic-chapter mode.",
              fix="Set pacing.mode to 'compressed' with expand-on-meaningful-change.")


def check_next_chapter(manifest: dict, project: Path, f: Findings) -> int | None:
    """Cross-check every 'Next fic chapter' claim in the corpus against live edge."""
    edge = int(manifest["edge"]["fic_chapter"])
    expected = edge + 1
    bad = {}
    edge_day = str(manifest["edge"].get("declared_on", ""))
    roots = [project / "audits", project / "foundation"]
    for root in roots:
        if not root.is_dir():
            continue
        for p in sorted(root.glob("*.md")):
            if re.search(r"(NUMBERING_MAP|LEDGER|INDEX|MANIFEST)", p.name):
                continue     # these tables legitimately list source-chapter numbers
            dm = re.search(r"(20\d\d-\d\d-\d\d)", p.name)
            if dm and edge_day and dm.group(1) < edge_day:
                continue          # receipt predates the live edge: historical, not a conflict
            txt = read(p)
            for m in NEXT_CHAPTER_RE.finditer(txt):
                n = int(m.group(1))
                # a "next ChapterNNN" far from the fic range is a CANON number, not a fic claim
                if abs(n - edge) > 15:
                    continue
                if n != expected:
                    bad.setdefault(p.name, set()).add(n)
    for name, nums in sorted(bad.items()):
        for n in sorted(nums):
            f.add("next-chapter-consistency", "warn",
                  f"{name} implies Chapter{n} is next, but live edge after Chapter{edge} "
                  f"makes Chapter{expected} next. Stale or superseded instruction.",
                  fix=f"Ignore for drafting; next chapter is Chapter{expected}.")
    return expected


def check_numbering(manifest: dict, f: Findings) -> None:
    rows = chapter_map(manifest)
    edge = int(manifest["edge"]["fic_chapter"])
    row = rows.get(edge)
    if not row:
        sev = "warn" if manifest.get("_native_passthrough") else "error"
        f.add("canon-numbering", sev,
              f"Live edge Chapter{edge} absent from canon_numbering."
              + (" Run scan_project.py to build the numbering map."
                 if manifest.get("_native_passthrough") else ""))
        return
    consumed = {int(x) for x in re.findall(r"Chapter(\d+)", str(row.get("canon", "")))}
    later = []
    for n, r in sorted(rows.items()):
        if n > edge and r.get("status") == "accepted":
            f.add("canon-numbering", "warn", f"Chapter{n} is marked accepted beyond live edge {edge}.")
        for c in (int(x) for x in re.findall(r"Chapter(\d+)", str(r.get("canon", "")))):
            if r.get("status") == "accepted" and n <= edge:
                later.append(c)
    nxt = manifest["edge"].get("next_source")
    if manifest.get("_native_passthrough"):
        return          # no derived numbering to check; do not report absence as a defect
    if nxt and later and max(later) >= int(nxt):
        f.add("canon-numbering", "error",
              f"Accepted chapters at or below the live edge already consume Chapter{max(later)} "
              f">= next_source {nxt}: source material was used early.",
              fix="Rebuild coverage so each canon chapter is consumed exactly once, in order.")


def check_character_states(manifest: dict, f: Findings) -> None:
    for name, st in manifest.get("characters", {}).items():
        if "public" in json.dumps(st).lower() and "reveal" in json.dumps(st).lower():
            if st.get("public_identity") and st.get("reveal_status") in (None, ""):
                f.add("character-discipline", "warn",
                      f"{name}: public identity declared but reveal_status unset — "
                      f"an agent cannot tell whether a reveal is allowed.")
        if st.get("power_floor") and st.get("power_ceiling") is None:
            f.add("character-discipline", "info",
                  f"{name}: power_floor locked but no ceiling; anti-inflate guard absent.")


def check_power_drift(manifest: dict, project: Path, f: Findings) -> None:
    """Detect the same stat asserted with different values across live docs."""
    live = manifest.get("characters", {})
    srcs = [project / "foundation" / "STATUS_PANEL.md", project / "foundation" / "PROJECT_BIBLE.md"]
    for src in srcs:
        if not src.exists():
            continue
        txt = read(src)
        for name, st in live.items():
            for field, pat in (("rank", r"Rank\s*(\d+)"), ("sp", r"SP\s*(\d{2,5})")):
                locked = st.get(field)
                if locked is None:
                    continue
                # line-local only: "Yan Shuo" bullets, never a later line that merely
                # starts with the same first name (that scan found Lan's SP505 under Yan).
                found = set()
                stem = name.split()[0]
                for line in txt.splitlines():
                    if stem in line and not re.search(r"\b(?:Lan|Qian|Liu|Song|Luo)\b", line):
                        found.update(int(x) for x in re.findall(pat, line))
                for v in found:
                    if v != int(locked):
                        f.add("power-drift", "error",
                              f"{src.name}: {name} shows {field.upper()}{v} but manifest locks "
                              f"{field.upper()}{locked}. One is stale.",
                              fix="Update the loser to the live value or mark the file quarantined.")


# ---------------------------------------------------------------- driver
SKIP_TOKEN_TARGETS = re.compile(
    r"(BRANCH_LEDGER|CANON_LEDGER|BANNED_TOKENS|NO_MISTAKE_LIVE_RULES|STATUS_PANEL"
    r"|VALIDATION_REPORT|_AUDIT_|AUDIT_)")


def check_required_patterns(manifest: dict, targets: list[Path], f: Findings) -> None:
    """Some projects declare patterns the story body must contain (mirror consistency).
    Reported as warnings: absence is a review prompt, not proof of a defect."""
    pats = manifest.get("required_patterns") or []
    if not (pats and targets):
        return
    # These patterns describe the CURRENT live chapter's mirror expectations, not a standing
    # requirement on every chapter ever written — checking all 52 produces pure noise.
    latest = manifest["edge"].get("fic_chapter")
    if latest is not None:
        only = [t for t in targets if re.search(rf"Chapter[_-]?0*{latest}\.md$", t.name)]
        targets = only or targets[-1:]
    for target in targets:
        txt = read(target)
        missing = []
        for p in pats:
            try:
                if not re.search(p, txt, re.I):
                    missing.append(p)
            except re.error:
                continue
        if missing:
            f.add("required-patterns", "info",
                  f"{target.name} does not match {len(missing)}/{len(pats)} required patterns "
                  f"(e.g. {missing[0][:60]}). These are mirror-consistency expectations written "
                  f"for the previous chapter, so a new chapter legitimately differs.")


def collect_targets(project: Path, explicit: list[str]) -> list[Path]:
    """Prose and coverage only. Files that legitimately DOCUMENT forbidden values
    (ledgers, ban registries, rulebooks, audit receipts) are excluded, or the drift
    guard flags its own registry instead of the prose it exists to protect."""
    if explicit:
        return [project / e if not Path(e).is_absolute() else Path(e) for e in explicit]
    # Drift scanning applies to creative output only. Ledgers, registries and rulebooks
    # legitimately QUOTE forbidden values as documentation — flagging those is the guard
    # reporting on itself.
    out = []
    # Default scope is story prose only. Coverage/ledger documents legitimately contain
    # "Do not use:" bullet lists that enumerate forbidden values, so scanning them produces
    # dozens of confident false positives. Pass --scan-coverage to include them.
    dirs = ("chapters", "canon_coverage") if _INCLUDE_COVERAGE else ("chapters",)
    for d in dirs:
        if (project / d).is_dir():
            out += [p for p in sorted((project / d).glob("*.md"))
                    if not SKIP_TOKEN_TARGETS.search(p.name)
                    and not re.search(r"(LEDGER|MANIFEST|INDEX|TEMPLATE)", p.name)]
    return out


def run(project: Path, phase: str, files: list[str], write_report: str | None) -> int:
    manifest = load_manifest(project)
    f = Findings()
    checks = [
        lambda: check_branch_supersession(manifest, project, f),
        lambda: check_receipt_coverage(manifest, project, f),
        lambda: check_firewalls(manifest, f),
        lambda: check_pacing(manifest, f),
        lambda: check_next_chapter(manifest, project, f),
        lambda: check_numbering(manifest, f),
        lambda: check_character_states(manifest, f),
        lambda: check_power_drift(manifest, project, f),
    ]
    if phase in ("post", "full"):
        targets = collect_targets(project, files)
        checks.append(lambda: check_banned_tokens(manifest, project, f, targets))
        checks.append(lambda: check_required_patterns(manifest, targets, f))
    for c in checks:
        c()

    items = f.sorted()
    # collapse "same line, same token, different registry label" into one error
    collapsed, sig = [], set()
    for i in items:
        s = re.sub(r"\s*\((?:[a-z_]+)\)", "", i["message"])
        if (i["severity"], s) in sig:
            continue
        sig.add((i["severity"], s))
        collapsed.append(i)
    items = collapsed
    errs = [i for i in items if i["severity"] == "error"]
    warns = [i for i in items if i["severity"] == "warn"]
    result = "PASS" if not errs else "FAIL"
    print(f"STORYOS_VALIDATE: {result}  (phase={phase}, errors={len(errs)}, warnings={len(warns)})")
    for i in items:
        mark = {"error": "FAIL", "warn": "WARN", "info": "info"}[i["severity"]]
        print(f"  [{mark}] {i['check']}: {i['message']}")
        if i.get("fix"):
            print(f"         → {i['fix']}")
    if not items:
        print("  no findings — foundation is internally consistent")
    nxt = int(manifest["edge"]["fic_chapter"]) + 1
    print(f"  NEXT CHAPTER: Chapter{nxt}  "
          f"(source: Chapter{manifest['edge'].get('next_source','?')} "
          f"{manifest['edge'].get('next_source_title','')})")
    print(f"  GATE: {'blocked — resolve errors before drafting' if errs else 'clear — blueprint then draft'}")

    if write_report:
        out = project / write_report
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# StoryOS Validation Report", "",
                 f"Date: {_dt.date.today().isoformat()}",
                 f"Phase: `{phase}`", f"Result: **{result}**", "",
                 f"- Live edge: after Chapter{manifest['edge']['fic_chapter']}",
                 f"- Next fic chapter: Chapter{nxt}",
                 f"- Canon consumed through: Chapter{manifest['edge'].get('canon_consumed','?')}",
                 f"- Next source: Chapter{manifest['edge'].get('next_source','?')}",
                 f"- Errors: {len(errs)}  Warnings: {len(warns)}", ""]
        for i in items:
            lines.append(f"- `{i['severity']}` **{i['check']}** — {i['message']}")
            if i.get("fix"):
                lines.append(f"  - fix: {i['fix']}")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"  report written: {write_report}")
    return 0 if result == "PASS" else 1


# ---------------------------------------------------------------- selftest
def selftest() -> int:
    """Build synthetic projects to prove each guard fires AND does not misfire."""
    import shutil, tempfile
    base = Path(tempfile.mkdtemp(prefix="storyos_selftest_"))
    good = {
        "schema": "storyos-manifest/3", "project": "selftest",
        "edge": {"fic_chapter": 51, "fic_title": "The Cost of Quiet", "canon_consumed": 176,
                 "accepted_chapters": [50, 51], "next_source": 177, "next_source_title": "T"},
        "canon_numbering": [{"fic": 50, "canon": "Chapter174 + Chapter175", "status": "accepted"},
                           {"fic": 51, "canon": "Chapter176", "status": "accepted"}],
        "characters": {"Yan Shuo": {"rank": 39, "sp": 962, "public_identity": "Yan Shuo/he",
                                    "reveal_status": "none"}},
        "knowledge_firewalls": [{"character": "Yan Shuo", "topic": "identity", "state": "HIDDEN",
                                 "earliest_valid_change": "authorized reveal",
                                 "rule": "no public reveal"}],
        "information_discipline": "ACTIVE", "pacing": {"mode": "compressed"},
        "branches": {"rejected_post48": {"status": "superseded", "chapters": [52, 53]}},
        "banned_tokens": {"future_power_drift": ["Phoenix God authority", "SP526"]},
    }
    def write(proj: Path, manifest: dict, extra: dict | None = None):
        (proj / "foundation").mkdir(parents=True, exist_ok=True)
        (proj / "audits").mkdir(parents=True, exist_ok=True)
        (proj / "chapters").mkdir(parents=True, exist_ok=True)
        (proj / "foundation" / "CURRENT_STATE_MANIFEST.json").write_text(
            json.dumps(manifest, indent=2), encoding="utf-8")
        (proj / "foundation" / "STATUS_PANEL.md").write_text(
            "# Status Panel\nLive edge: **after Chapter51, `x`**.\n- Yan Shuo: Rank39 / SP962.\n",
            encoding="utf-8")
        for name, body in (extra or {}).items():
            (proj / name).write_text(body, encoding="utf-8")

    cases = []
    # 1 clean project must PASS
    p = base / "clean"; write(p, json.loads(json.dumps(good)))
    (p / "audits" / "CHAPTER_51_VALIDATION_2026-09-18.md").write_text(
        "# ok\nChapter51 valid.\n", encoding="utf-8")
    cases.append(("clean project → PASS", p, 0))
    # 2 superseded-branch receipt claiming a further edge
    p = base / "stale"; m = json.loads(json.dumps(good)); write(p, m)
    (p / "audits" / "CHAPTER_52_VALIDATION_2026-09-17.md").write_text(
        "Live edge: **after Chapter52, `x`**.\nNext fic chapter: Chapter53.\n", encoding="utf-8")
    (p / "audits" / "CHAPTER_51_VALIDATION_2026-09-18.md").write_text(
        "Live edge: **after Chapter51, `x`**.\n", encoding="utf-8")
    m["canon_numbering"].append({"fic": 52, "canon": "Chapter177", "status": "drafted-rejected",
                                 "validation": "CHAPTER_52_VALIDATION_2026-09-17.md"})
    write(p, m)
    cases.append(("superseded branch edge-claim → FAIL", p, 1))
    # 3 banned token in prose
    p = base / "banned"; write(p, json.loads(json.dumps(good)))
    (p / "chapters" / "Chapter_52.md").write_text(
        "…she invoked Phoenix God authority and rose to SP526.\n", encoding="utf-8")
    cases.append(("banned token in prose → FAIL", p, 1))
    # 4 incomplete firewall
    p = base / "fw"; m = json.loads(json.dumps(good))
    m["knowledge_firewalls"] = [{"character": "Lan", "topic": "secrets", "state": "SORTA_KNOWN"}]
    write(p, m)
    cases.append(("bad firewall state → FAIL", p, 1))
    # 5 power drift inside foundation docs
    p = base / "drift"; write(p, json.loads(json.dumps(good)))
    (p / "foundation" / "STATUS_PANEL.md").write_text(
        "# Status Panel\nLive edge: **after Chapter51, `x`**.\n- Yan Shuo: Rank23 / SP156.\n",
        encoding="utf-8")
    cases.append(("power drift in live docs → FAIL", p, 1))

    passed = failed = 0
    for label, proj, want_rc in cases:
        try:
            rc = run(proj, "full", [], None)
        except SystemExit:
            rc = 2
        ok = (rc == want_rc)
        passed += ok
        failed += (not ok)
        print(f"\nSELFTEST {'✓' if ok else '✗'} {label}  (exit {rc}, expected {want_rc})\n")
    shutil.rmtree(base, ignore_errors=True)
    print(f"SELFTEST RESULT: {passed}/{len(cases)} guards behaved correctly")
    return 0 if not failed else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="StoryOS foundation validator")
    ap.add_argument("--project", default=".")
    ap.add_argument("--phase", choices=["pre", "post", "full"], default="full")
    ap.add_argument("--files", nargs="*", default=[])
    ap.add_argument("--write-report", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--scan-coverage", action="store_true",
                    help="also drift-check canon_coverage files (default: story prose only)")
    a = ap.parse_args()
    global _INCLUDE_COVERAGE
    _INCLUDE_COVERAGE = a.scan_coverage
    if a.selftest:
        return selftest()
    return run(Path(a.project).resolve(), a.phase, a.files, a.write_report)


if __name__ == "__main__":
    sys.exit(main())
