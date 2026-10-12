# FULL WORKSHOP AUDIT — 2026-10-10

Commission: author — "you check everything completely in your workshop and understand."
Scope: every file class in the tree (121 files): chapters, foundation docs, canon
receipts, codex, tools/gates, kit reference, archive, shipping artifacts.
Method: tree inventory → doctrine re-read → receipt coverage → tool self-test →
chapter-panel vs. reality matrix → V1/V2 cross-consistency → defect classification.

## 1. WHAT THE WORKSHOP ACTUALLY IS

Two serials under one tree:
- **V2 (live)**: canon-parallel rebuild, chapters/ 1–5 shipped + tagged
  (v2-ch01b, v2-ch02b, v2-ch03, v2-ch04b, v2-ch05). 23,531 verify prose words /
  23,513 style. All-alive doctrine: REBUILD_PLAN (clauses 1–5b), SERIAL_LOG,
  BUTTERFLY_BANK_V2, LAN_SHEN_MISSION, V2_EPOCH, PREWRITE boards ch02–05,
  CONTINUITY **V2 section** (added today).
- **V1 (archived)**: the balm/jar-economy serial, 15 chapters (archived in
  _archive/v1_epoch_ch01-15) plus its doctrine baggage: HANDOFF.md, CANON_LEDGER.md
  (rows), STATUS_PANEL.md (edge), CURRENT_STATE_MANIFEST.json (was V1, regenerated
  today), audits/2026-09-20 doc, codex/*, PREWRITE_ch10–15 boards.

## 2. DEFECTS FOUND vs FIXED TODAY

| # | defect | severity | action |
|---|---|---|---|
| 1 | HANDOFF.md billed itself "read this first" while describing V1 ch13-era state | 🔴 trap | bannered V1-epoch |
| 2 | CURRENT_STATE_MANIFEST.json self-declared measured-authority, was V1-dated (14 chapters) | 🔴 trap | **regenerated via tools/scan_project.py** (5 ch / 23 receipts / 23,513) |
| 3 | CONTINUITY.md = V1 anchor table (herb-shop, Yan Song, jar economy); V2 chapters had NO anchor rows | 🔴 drift risk | V2 authoritative section prepended with rows ch1–5; V1 table left intact below |
| 4 | CANON_LEDGER.md = V1 butterfly ledger ("END OF CHAPTER THIRTEEN") coexisting with the active V2 bank | 🟡 confusion | bannered; active rows live in BUTTERFLY_BANK_V2.md |
| 5 | STATUS_PANEL.md edge = V1 ch15 | 🟡 stale | bannered (SERIAL_LOG is the winning source per its own rule) |
| 6 | codex/CHARACTERS, PLACES, KNOWLEDGE_FIREWALLS = V1-era registries | 🟡 collision | bannered (codex/TIMELINE remains alive for V2 — its frame was verified against V2 usage) |
| 7 | audits/2026-09-20 doc, foundation/PREWRITE_ch10–15 = V1 boards | 🟠 clutter | bannered |
| 8 | foundation/PREWRITE_ch04_draft_block.md = superseded staging | 🟠 clutter | **deleted** (content absorbed into tagged ch4) |
| 9 | OPEN_DECISIONS numbering collision at 11/12 (scan_project warning) | 🟡 hygiene | **flagged, NOT renumbered** — renumbering a legal-life doc without the author is disallowed |
| 10 | THE_PLAN.md family-economy rows assume V1 balm/jar household; V2 father = letter-reader (ch1) | 🟡 semantic | noted in LAN_SHEN_MISSION.md; cooking track re-seated at mother's kitchen |
| 11 | PREWRITE boards ch03–05 lacked anchor dates before writing (rule-of-order violated) | 🟡 process | CONTINUITY V2 rows now exist; ch6+ boards must write anchor row FIRST |

Earlier in-session audit finds (today, preceding this doc): ch2 "Lan Yue" name-collision ×9
(canon mother = **Lang Yue**), ch2 duplicated-chopsticks sentence and wake-fragment
corruption — all repaired and retagged as v2-ch02b. Dialogue-metric wrap artifact —
resolved epoch-wide by single-line normalization (SERIAL_LOG revision 4).

## 3. CANON COVERAGE ASSETS

- canon_extract/chapters/: receipts **001–020** (chapter-ahead coverage through canon
  ch20 — roughly V2 serial ch6–10 runway).
- canon_extract/readnovelfull_map.txt: full title map, 1,917 chapters.
- canon_extract/CANON_INDEX_23_600.txt: 577-line index for canon 23–600.
- Manhua corroboration channel (registered, JS-walled in _kit docs): not fetchable;
  novel spine remains the only receipt.

## 4. TOOLS / GATES — all live and self-tested

- checks/run_all.sh = 9 layers: verify · style_gate · canon_copy_check (n-grams 12/7+budget)
  · marker-leak · privacy · build-hygiene · **selftest.py (injected-defect red team: PASS)** ·
  status_gen · banned_token_check (exempt-receipt-aware).
- tools/scan_project.py — measurement service (regenerated the manifest truthfully today).
- Battery state as of this audit: **9/9 ALL GREEN**; warnings logged (ch2 38.8% dialog-true
  warn — MTP-1 demotion still open; ch4 31.5 / ch5 31.2 warn-tier, logged on boards).

## 5. LIVE LEDGER LINE (standing report law)

Butterflies: **7 contact-made (all dust)** · **3 class-M** · consecutive contact-zero
streak **0**. Premise decay: dust-scale, by design. Next canonical event waits canon 009.

## 6. AUTHOR-VISIBLE DECISIONS THIS AUDIT DID NOT MAKE FOR HIM

- OPEN_DECISIONS 11/12 renumbering (his ledger, his numbers).
- Whether V1 codex registries deserve a salvage pass into V2 form (CHARACTERS' OC roster
  has faces — Yan Song, Niu Bao, Zhao — the V2 epoch has not re-adopted; adopting means
  re-prewriting them through Clause 5 gates).
- Whether CANON_LEDGER's V1 decay-rows should be *summarized* into the V2 bank for
  one-ledger cleanliness, or stay as provenance appendix.
