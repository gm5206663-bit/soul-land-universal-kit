# SOUL LAND 2 — THE UNRAVELED TIDE (Jiang Che)
### Branch 06 · Fan fiction of Douluo Dalu 2: Unrivaled Tang Sect (绝世唐门)
**Live edge: after Chapter 21, "Round One."** · Re-railed 2026-09-20 (governance layer rebuilt; prose untouched).

---

## THE ONE FILE THAT MATTERS

**`foundation/STATUS_PANEL.md` is the single source of truth for where this
story is.** Every other document — codex, status file, continuation prompt —
mirrors it. If two files disagree, the STATUS_PANEL wins and the other file is
a defect to be repaired the same turn. This is the rule that was broken on
2026-09-20 (four files, four different live edges) and never broken again.

## Read order (every session, no exceptions)

1. `foundation/STATUS_PANEL.md` — the live edge, current scene, character states.
2. `foundation/NO_MISTAKE_LIVE_RULES.md` — the twelve locks.
3. `THE_CODEX.md` — the full bible (read completely; the laws live here in detail).
4. `JIANG_CHE_STATUS.md` — the OC dossier (v4.2; design-era numbers are
   superseded where flagged — the per-chapter "Ranks:" lines in the codex
   chapter records are the source of truth for rank).
5. The last two chapters.
6. `foundation/CURRENT_STATE_MANIFEST.json` — the machine-readable edge.

## Gate

```
python3 ../SOUL_LAND_UNIVERSAL_KIT/tools/verify.py --project .     # whole project
python3 ../SOUL_LAND_UNIVERSAL_KIT/tools/verify.py chapters/       # chapter gate
python3 ../SOUL_LAND_UNIVERSAL_KIT/tools/selftest.py               # the gate's own test
```

"Done" means the gate exits 0 — zero failures, not "mostly passing." A gate that
has never passed a chapter in this project is a gate nobody reads, and this one
now passes all 22 chapters (re-rail receipt: `audits/2026-09-20_RE_RAIL_RECEIPT.md`).

## Mirror

`THE_CODEX.md` is mirrored at `../CODEX/06_PROJECT_SOUL_LAND_2.md` (the mirror
rule for this project, per the workspace map). Sync in the same turn as any
codex change:

```
cp Soul_Land_2_Project/THE_CODEX.md Soul_Land_2_Project/../CODEX/06_PROJECT_SOUL_LAND_2.md
```

## What this project is (short version)

Jiang Che (江澈), age 11, year of Huo Yuhao's birth — a Blue Silver Tide Grass
holder (life-core, water-carried, light-fed) built from conception by an
Adaptation Talent that is never visible, never voiced, never a system. The
serial is a **full retelling**: canon happens whole and on-page; the OC is
added, woven beside the canon cast (Tang Ya, Bei Bei, Huo Yuhao, Wang Dong,
Xiao Xiao, Ma Xiaotao), and the story bends only where his compounded presence
earns it, and every bend is logged.

**What he is not:** not a canon character reborn; not granted any canon
character's private mechanics; no romance pre-decided; no prodigy rings for a
design character (the ring-config law); the AT is never named in prose.

## File map

| Path | What it is |
|---|---|
| `foundation/STATUS_PANEL.md` | **single live-edge source** |
| `foundation/CURRENT_STATE_MANIFEST.json` | machine-readable edge + required patterns |
| `foundation/NO_MISTAKE_LIVE_RULES.md` | the twelve locks |
| `foundation/KNOWLEDGE_FIREWALLS.md` | who knows what (L1–L4) |
| `foundation/CANON_LEDGER.md` | canon receipts + the CJK glossary (chapter titles now live here) |
| `foundation/CONTINUITY.md` | anchor table + forward debts |
| `foundation/SERIAL_LOG.md` | dated log |
| `foundation/OPEN.md` | open canon checks + open rulings |
| `THE_CODEX.md` | the bible (v15.2) |
| `JIANG_CHE_STATUS.md` | the OC dossier (v4.2) |
| `CONTINUATION_PROMPT.md` | the paste-first file for a new chat (points at the panel) |
| `THE_LETTER_HOME.md` | Chapter 5's letter artifact (prose artifact, kept for the record) |
| `chapters/chapter_01..21.md` | the serial (chapter_08a is a side panel of ch8) |
| `audits/` | receipts |
