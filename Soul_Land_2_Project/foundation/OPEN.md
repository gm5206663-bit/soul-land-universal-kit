# OPEN — questions, checks and rulings
### Soul Land 2 · The Unraveled Tide. Updated 2026-09-20.
### Nothing in this file is decided by accident. When a question stops being
### open, move it (decided, with source) into the bible and update this list
### the same turn.

## OPEN RULINGS (awaiting the author — the gate is honest about these)

**R1 — Name-digits in prose (Sara's proposal, 2026-09-20).** Digits that are
*names* keep their numerals: **Room 108** (this serial), **Dorm333 / Dorm336 /
Rank39 / SP505** (SL4), **ch 17** (SL3/SL4). Measurement digits (ranks spoken
as numbers, times, years, counts) stay forbidden in prose. Implemented in gate
v2.1 and red-tested. *Effect if the author disagrees: the name-digits are
converted to words and the gate exemption removed.*

**R2 — The two CJK dialogue lines (translations proposed, 2026-09-20).**
- ch7: Wang Dong's outburst 话不投机半句多 → proposed: *"Not even half a
  sentence is worth saying!"*
- ch11: Tang Ya's aside 互有胜负 → proposed: *"They've traded wins."*
The chapters now carry the proposed English; the originals are preserved in
`CANON_LEDGER.md` §E. *The author may veto either line; the sweep is one
command.*

**R3 — Emoji/dingbat bookkeeping marks.** This project is now clean (169 marks
removed from chapter tails, 2026-09-20; the test assertions remain as text).
SL3 (826 marks) and SL4 (0 in chapters) carry them elsewhere; a corpus-wide
ruling is owed: are bookkeeping marks allowed in *apparatus only*, or banned
file-wide? The gate currently fails them file-wide. *No action on SL3/SL4
until the author rules.*

**R4 — Filename law admits date hyphens (Sara's change, 2026-09-20).** The
gate's filename law (letters/digits/underscore/dot) failed the corpus's own
dated-file convention — SL4's entire audit tree is
`CHAPTER_52_VALIDATION_2026-09-19.md` and so on. Hyphen is now allowed
alongside the existing set; spaces, CJK and other punctuation still fail.
*Effect if the author disagrees: hyphens are removed from the law and every
dated file in the repos is renamed (a large mechanical sweep).*

## OPEN CANON CHECKS (execute at the listed trigger — never let these lapse)

| # | Check | Trigger | Status |
|---|---|---|---|
| 1 | ~~Rank-20 ring-cap~~ | — | CLOSED (v4.3): Ring 2 fixed to ~740 yr |
| 2 | Town names on the forest road + Tang Ya's exact title | ch 4–6 research fetch | verify against the v15-rebuilt chapters (the rebuild may already hold it) |
| 3 | Star Dou plant-beast roster (validate the Overlord Vine) | first hunt scene | open — the ring hunt is not yet triggered |
| 4 | Fox-type beast canon detail for Xiao Jiu's reveal | her first on-page appearance of the years | open — reserved beat |
| 5 | Tang Ya's recruitment sparkle (both boys) | pre-rebuild note (ch8 OLD NOTES) | verify whether the v15 rebuild kept it |
