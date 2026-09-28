# CANON_ACCESS.md — how canon ore enters this project (L-11)

## THE RULES
**V1 — Ore first, prose second.** No chapter may draft an S1 episode's beats without a
title-verified ore file in `canon_extract/episodes/s1eNN_<slug>.txt`.
**V2 — Title verification (every fetch, no exceptions).** The ore file header MUST
carry: `source_url`, the wiki page's actual `page_title` (from the fetch), the page's
first line (must contain "Season 1, episode NN (Production order)"), and the fetch
date (IST). A fetch whose title doesn't match is a WRONG PAGE (disambiguation trap)
and the ore is rejected.
**V3 — Distill, don't paste.** Ore files are condensed beats/characters/facts in
comment-form. zero_tolerance Z2 kills any 12-gram overlap between prose and ore.
**V4 — Transcript on demand.** Exact dialogue (transform phrases, puns, monologues) is
fetched from `https://miraculousladybug.fandom.com/wiki/<Episode_Title>/Transcript`
only when the chapter needs the exact words, and the transcript facts are marked in
the ore file.
**V5 — The spine is production order.** `canon_extract/SEASON1_INDEX.txt` (26 slots,
N° Overall 101–126, verified against the fandom Season_1 table 2026-09-04, which the
page itself notes "reflects the order in which the episodes were written and
produced… closest to reflecting the show's continuity" per Thomas Astruc). US
Nickelodeon broadcast order (2015-09-01 The Bubbler → 2016-05-24) is a DIFFERENT
ordering — anchors only, never used for chapter planning.
**V6 — Ore status bookkeeping.** SEASON1_INDEX.txt marks each slot `ORE DONE` /
`pending`. workspace_audit + completeness R6 verify every ORE DONE claim has a file.
Marking a slot ORE DONE without a file is a gate failure.

## THE RECIPE (per episode)
1. `fetch https://miraculousladybug.fandom.com/wiki/<Episode_Title>` (chunk 0 first:
   the infobox line "Season 1, episode NN (Production order); Episode NN (Overall)"
   is the verification).
2. Fetch the Plot chunk(s) + Characters section.
3. Distill into `canon_extract/episodes/s1eNN_<slug>.txt`:
   header (URL, page title, first line, date, disambig notes) → SYNOPSIS → PLOT beats
   (numbered) → CHARACTERS (major/minor) → KEY WORLD-STATE FACTS → WARP POINTS
   (suggestions for the D-ledger).
4. Mark the slot `ORE DONE` in SEASON1_INDEX.txt.

## KNOWN TRAPS
- "Stormy Weather" (S1E01) vs "Stormy Weather 2" (S3) vs the character Aurore
  Beauréal (whose akumatized name IS "Stormy Weather").
- The two Origins episodes (slots 22–23) are recaps — ore them like any other slot.
- Character page titles use accents (Césaire, Beauréal, Émilie) — fetch with the
  accented URL form.
