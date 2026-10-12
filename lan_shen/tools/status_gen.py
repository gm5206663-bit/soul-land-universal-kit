#!/usr/bin/env python3
"""STATUS.md generator — the live file inventory for the lan_shen project.

Regenerates STATUS.md at repo root from the actual tree, so the status file can
never disagree with the workspace. Called automatically at the end of
checks/run_all.sh (battery run) with the battery result; may be run by hand.

Usage:  python3 tools/status_gen.py ["battery line" ["date"]]

Every file is listed. Any file with no registry description is auto-listed under
its group with a ⚠️ marker — nothing hides. Register new files below in REGISTRY
or in the group walker patterns.
"""
import os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = (sys.argv[2] if len(sys.argv) > 2 else str(datetime.date.today()))
BATTERY = sys.argv[1] if len(sys.argv) > 1 else "not run this session — run checks/run_all.sh"

SKIP_DIRS = {".git", "__pycache__", ".venv"}

# ---------------------------------------------------------------- registry ---
REGISTRY = {
    # root
    "README.md":              ("🏠", "Public front door — pitch, doctrine, live stage line, project map."),
    "PROJECT_README.md":      ("🏠", "Agent-facing quickstart — how to work this repo end-to-end."),
    "HANDOFF.md":             ("🏠", "Session handoff — state of play for the next operator."),
    "SARA.md":                ("🏠", "Ceremony memo at the kit lineage level (author reflections)."),
    "LICENSE":                ("🏠", "MIT License © 2026 Gaurav Meena — house standard."),
    "NOTICE.md":              ("🏠", "Soul Land / Tang Jia San Shao IP disclaimer — fan-work terms."),
    "STATUS.md":              ("🏠", "This file — live inventory, auto-generated, never hand-edited."),
    ".gitignore":             ("🏠", "Git hygiene (pycache, venv, bak files)."),
    # chapters
    "chapters/Chapter_01_What_the_Master_Said.md":
        ("🟢", "V2 ch1 — 'What the Master Said' — dual-track canon-parallel (canon 001–002 + OC Awakening Day). Gated 9/9."),
    "chapters/Chapter_02_The_Fifteen.md":
        ("🟢", "V2 ch2 — 'The Fifteen' — first school day with the fifteen and the knife boy (canon 003–004). Gated 9/9."),
    "chapters/Chapter_03_The_Find.md":
        ("🟢", "V2 ch3 — 'The Find' — the silver girl by the roadside, the record as shield (canon 005). Gated 9/9."),
    "chapters/Chapter_04_Bringing_Her_Home.md":
        ("🟢", "V2 ch4 — 'Bringing Her Home' — mother's fear, the wash, five and a half, first meditation (canon 006). Gated 9/9."),
    "chapters/Chapter_05_Stay_Here.md":
        ("🟢", "V2 ch5 — 'Stay Here and Be My Little Sister' — consent ruling, Mang Tian's door (canon 007–008). Gated 9/9."),
    "chapters/Chapter_06_Gifted.md":
        ("🟢", "V2 ch6 — 'Gifted' — the thousand blows, the spine-shudder, the lane's count from the well (canon 009). Gated 9/9."),
    # foundation
    "foundation/REBUILD_PLAN.md":       ("📜", "THE law of the V2 epoch: canon-parallel doctrine, arc spine, word sizes, ends-at-academy gate."),
    "foundation/V2_EPOCH.md":           ("📜", "Epoch registry — V1 retired, V2 chapter rows, git workflow law."),
    "foundation/STYLE_LAW.md":          ("📜", "Six-vertex style bans + SCOPE/ART/PLAIN/CNDR/FP readability ceilings."),
    "foundation/NO_MISTAKE_LIVE_RULES.md": ("🟢", "Single live table of current project numbers (drift guard)."),
    "foundation/CANON_LEDGER.md":       ("📜", "Canon-receipt master: what's used, pending, forbidden."),
    "foundation/CANON_NOTES.md":        ("🟢", "Canon quotes/bible — ingested from the control centre."),
    "foundation/CONTINUITY.md":         ("🟢", "Scene-level continuity record."),
    "foundation/STATUS_PANEL.md":       ("🟢", "In-world state: vocabulary, fog, registers, inventory."),
    "foundation/SERIAL_LOG.md":         ("🟢", "Chapter rows + revision rows — every number the project ever froze on."),
    "foundation/BANNED_TOKENS.json":    ("🟢", "Drift-guard snapshot: current values + banned values of every stat."),
    "foundation/CURRENT_STATE_MANIFEST.json": ("🟢", "Manifest of occupied workspace (scan_project default target)."),
    "foundation/THE_PLAN.md":           ("🟢", "Arc outline surface THE PLAN (infra meta)."),
    "foundation/LAN_SHEN_MISSION.md":   ("🟢", "The mission thread's on-page visibility schedule — four columns, years 0–3 (REVISION 6)."),
    "foundation/OPEN_DECISIONS.md":     ("🟢", "Open author decisions (empty = nothing pending)."),
    "foundation/LAN_SHEN_MISSION.md":   ("🟢", "The mission thread's on-page visibility schedule — four columns, years 0–3 (REVISION 6)."),
    "foundation/BUTTERFLY_BANK_V2.md":  ("🟢", "Butterfly bank V2 (5b epoch) — contact-made and class-M rows, streak watch, premise-decay count."),
    "foundation/CANON_MASTER.md":       ("🟢", "Canon master: inventory, per-receipt digests, variance + gold ledgers, fetch queue (through 027)."),
    "foundation/REBUILD_5b_DELTA.md":   ("🟢", "5b audit + delta map — the starvation repair behind REVISION 5."),
    "foundation/PLAIN_WORD_LIST.md":    ("📜", "Vocabulary bank for the plain register (FP hinges allowed)."),
    # prewrites
    "foundation/PREWRITE_ch04.md":      ("🟢", "V2 ch4 prewrite board — clause-5 gate form; open item MTP-1 lives here."),
    "foundation/PREWRITE_ch05.md":      ("🟢", "V2 ch5 prewrite board — short-form; post-draft record carries the corruption incident, logged openly."),
    "foundation/PREWRITE_ch06.md":      ("🟢", "V2 ch6 prewrite board — 27-beat canon-009 enumeration; contact-zero declared; both first-run FAILs logged."),
    "foundation/PREWRITE_ch10.md":      ("🗄", "V1-era prewrite board (retired with V1, kept for mined material)."),
    # codex
    "codex/CHARACTERS.md":              ("🟢", "Character registry."),
    "codex/PLACES.md":                  ("🟢", "Places registry."),
    "codex/TIMELINE.md":                ("🟢", "Timeline skeleton (codex-sealed)."),
    "codex/KNOWLEDGE_FIREWALLS.md":     ("📜", "Knowledge firewall system — what Lan knows and when."),
    # tools
    "tools/verify.py":                  ("🧰", "Scene skeleton verifier — canonical structure gate."),
    "tools/style_gate.py":              ("🧰", "Style gates + Fire Phoenix readability ceilings."),
    "tools/canon_copy_check.py":        ("🧰", "Verbatim-plagiarism sweep vs canon receipts (n-gram runs)."),
    "tools/banned_token_check.py":      ("🧰", "Banned-token / drift-guard sweep across docs."),
    "tools/plain_word_check.py":        ("🧰", "Plain-register wordlist audit of chapters."),
    "tools/scan_project.py":            ("🧰", "Deterministic scope-line tracker for workspace files."),
    "tools/selftest.py":                ("🧰", "Test suite for every tool above (regression harness)."),
    "audits/2026-09-20_FULL_COMPARATIVE_AUDIT.md": ("🔍", "Full comparative audit ch1–15 vs style laws — the V2 rebuild trigger document."),
    "audits/AUDIT_2026-10-10_FULL.md":  ("🔍", "Full workshop audit 2026-10-10 — tree quantified; V1 baggage quarantined (commit c7ca486)."),
    "audits/AUDIT_2026-10-10_DEEP.md":  ("🔍", "Deep audit 2026-10-10 — the 'seriously' pass: doctrine docs read in full, chapter beats verified against receipts."),
    "tools/status_gen.py":              ("🧰", "This generator — rebuilds STATUS.md from the tree."),
    "checks/run_all.sh":                ("🧰", "The battery: 9 layers, all must pass before presenting."),
    # canon extract
    "canon_extract/readnovelfull_map.txt": ("🧰", "Original mirror map the extraction used (URLs)."),
    "canon_extract/CANON_INDEX_23_600.txt": ("🧰", "Index of canon chapters held ahead (023–600 line list — future receipt source)."),
    # audits
    
}

def prog_desc(path):
    """Generated descriptions for patterned groups (archives, receipts, prewrites)."""
    name = os.path.basename(path)
    m = re.match(r"canon_(\d+)_excerpt", name)
    if m:
        return ("📄", f"Novel chapter {int(m.group(1))} quotation receipt — the canon spine for that beat.")
    m = re.match(r"Chapter_(\d+)_", name)
    if m and path.startswith("_archive"):
        return ("🗄", f"V1 epoch ch{int(m.group(1))} (archived — style laws carried, story retired).")
    if name in ("CANON_LEDGER.md", "SERIAL_LOG.md", "STATUS_PANEL.md") and path.startswith("_archive"):
        return ("🗄", "V1 epoch " + name.replace(".md", "") + " (archived).")
    m = re.match(r"PREWRITE_ch(\d+)", name)
    if m:
        return ("🗄", f"V1-era prewrite board ch{int(m.group(1))} (retired with V1; mined material kept).")
    if path.startswith("_kit_reference/templates/"):
        return ("🛩", f"Kit template: {name[:-3].replace('_', ' ').title()} — the original blank our foundation filled.")
    if path.startswith("_kit_reference/"):
        return ("🛩", f"Kit document: {name[:-3].replace('_', ' ').title()} — source manual (vendored reference).")
    return None

ORDER = [
    ("📖 chapters — the serial (live)", "chapters/"),
    ("🏛 foundation — laws, logs, boards", "foundation/"),
    ("🃏 codex — canon-faced registries", "codex/"),
    ("📄 canon_extract — novel receipts", "canon_extract/"),
    ("🧰 tools + checks — the gates", ("tools/", "checks/")),
    ("🔍 audits — battery artifacts", "audits/"),
    ("🗄 _archive — V1 epoch (retired)", "_archive/"),
    ("🛩 _kit_reference — source kit (vendored manual)", "_kit_reference/"),
]

def human(size):
    if size < 1024:
        return f"{size}B"
    if size < 1048576:
        return f"{size/1024:.1f}K"
    return f"{size/1048576:.1f}M"

def prose_words(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    return len(re.findall(r"[A-Za-z'’'\-]+", t))

# ------------------------------------------------------------------ collect --
all_files = []
for base, dirs, names in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for n in names:
        p = os.path.relpath(os.path.join(base, n), ROOT)
        all_files.append(p.replace(os.sep, "/"))
all_files.sort()

lines = []
lines.append("# LAN SHEN — LIVE STATUS")
lines.append("")
lines.append("> Auto-generated by `tools/status_gen.py` — **never hand-edit**.")
lines.append("> Regenerated automatically at the end of every `checks/run_all.sh` battery run,")
lines.append("> or by hand: `python3 tools/status_gen.py`. If a file appears below with a")
lines.append("> ⚠️ marker it is real but unregistered — add its line to the generator.")
lines.append("")
live_chapters = sorted(p for p in all_files if p.startswith("chapters/") and p.endswith(".md"))
total_prose = sum(prose_words(os.path.join(ROOT, p)) for p in live_chapters)
lines.append("## AT A GLANCE")
lines.append("")
lines.append("| state | value |")
lines.append("|---|---|")
lines.append("| 🔴 epoch | **V2 — canon-parallel rebuild** (V1 archived) |")
lines.append(f"| 📖 chapters live | **{len(live_chapters)}** — {', '.join(os.path.basename(p) for p in live_chapters) or '—'} |")
lines.append(f"| ✍️ prose on page | **{total_prose:,} words** |")
lines.append(f"| 🔋 battery (last run) | **{BATTERY}** |")
lines.append('| ▶️ next | ch7 — acceptance night (canon 010–011; pairing decided at its board) |')
lines.append(f"| 🗓 status dated | {NOW} |")
lines.append("")

covered = set()
for section, pref in ORDER:
    prefs = pref if isinstance(pref, tuple) else (pref,)
    members = [p for p in all_files if any(p.startswith(pp) for pp in prefs)]
    if not members:
        continue
    covered.update(members)
    sub_bytes = sum(os.path.getsize(os.path.join(ROOT, p)) for p in members)
    lines.append(f"## {section}  ·  {len(members)} files · {human(sub_bytes)}")
    lines.append("")
    lines.append("| file | size | status | role |")
    lines.append("|---|---|---|---|")
    for p in members:
        icon_desc = REGISTRY.get(p) or prog_desc(p)
        if os.path.basename(p) == "run_all.sh" and p == "checks/run_all.sh":
            icon_desc = REGISTRY[p]
        if icon_desc is None:
            icon_desc = ("⚠️", "UNREGISTERED — add a line for this file in tools/status_gen.py")
        icon, desc = icon_desc
        extra = ""
        if p in live_chapters:
            extra = f" ({prose_words(os.path.join(ROOT, p)):,} w)"
        lines.append(f"| `{p}` | {human(os.path.getsize(os.path.join(ROOT, p)))}{extra} | {icon} | {desc} |")
    lines.append("")

root_files = [p for p in all_files if "/" not in p]
covered.update(root_files)
lines.append(f"## 🏠 root — front door + house papers  ·  {len(root_files)} files")
lines.append("")
lines.append("| file | size | status | role |")
lines.append("|---|---|---|---|")
for p in root_files:
    icon, desc = REGISTRY.get(p, ("⚠️", "UNREGISTERED — add a line for this file in tools/status_gen.py"))
    lines.append(f"| `{p}` | {human(os.path.getsize(os.path.join(ROOT, p)))} | {icon} | {desc} |")
lines.append("")

left = [p for p in all_files if p not in covered]
if left:
    lines.append("## ⚠️ Everything else (auto-listed)")
    lines.append("")
    for p in left:
        lines.append(f"- `{p}` — {human(os.path.getsize(os.path.join(ROOT, p)))} — ⚠️ UNREGISTERED")
    lines.append("")

lines.append("---")
lines.append("")
lines.append(f"*{len(all_files)} files · generated {NOW} · last battery: {BATTERY}*")
lines.append("")

out = os.path.join(ROOT, "STATUS.md")
open(out, "w", encoding="utf-8").write("\n".join(lines))
print(f"STATUS.md rebuilt: {len(all_files)} files, {total_prose:,} prose words")
