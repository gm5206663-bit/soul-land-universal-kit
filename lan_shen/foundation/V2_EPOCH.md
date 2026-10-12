# V2 EPOCH — 2026-09-23

**Author-ordered full rebuild.** V1 (15 chapters, verify 72,577 / style 72,473) retired to
`_archive/v1_epoch_ch01-15/` — archived, not deleted, per the author's own convention.
V1's banked LAWS carry; its scene FACTS do not bind (REBUILD_PLAN.md: contradictions must
be named in boards). V2: Fire Phoenix register, §0.7 ceilings at draft time, ~2 canon
chapters per serial chapter, Book One ends at the academy-entrance arc close (end beat
locked when canon 095–105 receipts land). Map: foundation/REBUILD_PLAN.md.

| ch | canon | title | banked |
|---|---|---|---|
| 1 | 001–002 | What the Master Said | 3,758w style / 3,793 verify / dual-track canon-parallel / 9 gates green |

## GIT WORKFLOW (repo management law, 2026-09-23)

- **Main is the shipping branch.** One commit per chapter: message = `chN: Title
  (canon XXX–YYY) — gates green` plus any doctrine notes.
- **Tag chapters**: `v2-chNN` after each chapter's battery goes green (`v2-ch01` exists).
- **Docs ride with the chapter** (SERIAL_LOG, CANON_LEDGER, STATUS_PANEL, totals) in the
  same commit — the repo is never left in a state where docs disagree with chapters.
- **House files are permanent**: LICENSE (MIT © Gaurav Meena) + NOTICE.md (Soul Land IP
  disclaimer) — pattern matched to soul-library.
- **No tokens in the tree, ever.** Remote URL carries none; pushes use the token on the
  command line only. Battery layer 5 greps for leaks each chapter.
- **STATUS.md is generated, never edited.** checks/run_all.sh regenerates it at the end
  of every battery run (green or red). A new file with no registry line surfaces itself
  with a ⚠️ marker in STATUS.md — nothing hides; register it in tools/status_gen.py.
| ch2 | The Fifteen | canon 003–004 complete · 4,973 verify words · dual-track: class of fifteen, the knife boy, gold-at-root glance, Lin Ximeng's classifications; OC = the ledger of free years + inattention as an asset | ✅ 9/9 green | tag v2-ch02 |
| ch3 | The Find | canon 005 complete · 5,000 verify / 4,993 style (band ceiling) · dual-track with bystander-slot doctrine payoff; dialogue = hush by amendment | ✅ 9/9 green | tag v2-ch03 |
| ch4 | Bringing Her Home | canon 006 complete · 4,271 style · dialogue true 31.1% (warn-tier, logged) · metric-parity harmonization done this cycle: quotes single-line across chapters; ch3 hush amendment rescinded on data (true 27.1% inside standard); ch2 true 38.5% held at warn pending demotion pass | ✅ 9/9 green (warns logged) | tag v2-ch04 |
| ch1b | What the Master Said | +fathers in the queue (B1 dust) · BUTTERFLY row added to panel · full-join formatting | ✅ 9/9 green | re-tag v2-ch01b |
| ch2b | The Fifteen | +grass-exile desk first-words (B2 dust) · "Lan Yue" name-collision fixed ×9 · chopsticks-doubling and wake-fragment corruption repaired · −150 offsets to 5,001 style | ✅ 9/9 green (dlg 38.8% warn — MTP-1 open) | re-tag v2-ch02b |
| ch4b | Bringing Her Home | +the lane speaks doorstep exchange (B6 dust + M1) · BUTTERFLY row rewritten from "none" to cost-declaration form | ✅ 9/9 green | re-tag v2-ch04b |
| ch5 | Stay Here and Be My Little Sister | canon 007+008 complete · 4,740 style · B7 + M2 + M3 · methodology note: first draft carried a mid-file prose corruption (caught in-scan before any gate run; full tail rewritten) | ✅ 9/9 green (dlg 32.9% warn) | tag v2-ch05 |
| ch6 | Gifted | canon 009 complete · 3,870 style / 3,873 verify · **contact-zero declared at the board** (clause 5b) · class-M M4 · staged inside ch5's montage window (overlap correction logged) · methodology: first battery FAILED style (dlg 12.2% < 13 floor, narr median 14) + banned-token collision ("One Piece" inside "one piece of furniture") — fixed by expansion pass to band (3,239→3,870 style), thresholds untouched | ✅ 9/9 green | tag v2-ch06 |
