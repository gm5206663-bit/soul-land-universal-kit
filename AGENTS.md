# AGENTS.md — the contract for any AI agent arriving in this workspace

You are not the first agent here, and you will not be the last. This file is the
front door. It is law-shaped on purpose: everything below has a receipt somewhere
in the tree, and most of it was paid for by a real mistake (see
`MISTAKES_LEDGER_2026-09-23.md`).

## What this workspace is

Soul Land (斗罗大陆 / Douluo Dalu) fanfiction, written like software: every serial
carries laws (rails), a single-status panel, a canon ledger, and a verification
gate that must pass before a chapter ships. The author is **Gaurav Meena**
(gm5206663-bit). His word outranks every file, including this one.

## Authority order (obey, never re-derive)

author word > the serial's own RAILS / FOUNDATION > its STATUS_PANEL > its codex
> the kit (`SOUL_LAND_UNIVERSAL_KIT/`) > README tables > everything else.
Where two files disagree, the more specific file wins — and you fix the stale
one the same turn, with a dated receipt. **A fact maintained in two places will
be wrong in one of them, and the check reads the other.**

## The non-negotiables

1. **No chapter ships without its gate passing.** Run the serial's verify before
   and after your work. A gate that has never caught anything is decoration.
2. **Panels only when the serial's law allows** (Devouring Dragon: default NONE —
   the story is the beast's).
3. **Never weaken a gate to pass it.** Fix the work or fix the panel — never the check.
4. **Author rulings outrank your design.** Record them verbatim; never paraphrase
   a ruling into something "better".
5. **The separation walls hold.** Nothing crosses between era-serials or between
   fandoms. See `calendar.html` in soul-library for the view — a view, not a bridge.
6. **Add-only housekeeping.** Superseded material is archived with dated receipts,
   never silently deleted. Byte-verify BEFORE removing anything that looks like a
   duplicate — two "duplicates" here have been unique files with different fates.
7. **Sync every mirror the same turn** you change state: panels, logs, ledgers,
   READMEs, the Control Centre registry. "Later" is how state rots.
8. **Commit before you dance with the remote.** Live agents push to this repo
   concurrently: fetch, rebase, push — and never `reset --hard` with uncommitted
   work in the tree.

## Style, measured

Plain language (s40-family laws), sentence average ≤ 25 words, no sentence over
60, no count-numbers in prose, no retired house-words (each serial's glossary
carries the list), "the way X" capped at two per chapter. Measure, don't argue:
each serial ships its own measure tool. Your draft will be caught by the gate —
that is the gate working, not the gate being rude.

## Boundaries

- **Golden Lion (`soul_land_2_new/`)** has a live writing agent. Do not touch it
  without the author's explicit word.
- The private repo `soul_land_4_fire_phoenix` is the live Fire Phoenix; copies in
  this workspace are archived snapshots — never read them as current.
- Dragon Prince Yuan's chapter 2 is blocked on source text the author must paste.
  Do not fetch copyrighted novel text from unofficial sites.
- Fan-work law: non-commercial, reading copies only, the disclaimer travels with
  everything (see NOTICE.md).

## Token hygiene

Tokens are arguments, never files, never logs. Revoke and re-mint any token that
has traveled. Never widen a scope to dodge a design — if GitHub refuses your
push, that refusal is information.

## Where to start

The root `README.md` (workspace map) → the serial's own README/HANDOFF → its
`foundation/STATUS_PANEL.md` (the live edge) → its RAILS → the last two chapters.
Read **everything** you will touch before you touch it: the Use Everything
Protocol is law, and the coldest catches are the ones greps can't see.

*Added 2026-09-23 (add-only). If this file and the author disagree, the author wins.*

---

## AMENDMENT — 2026-09-30 (add-only): the park and the prequel

- **Qing Ling (SL3) is PARKED** (ch 1–7 shipped, gates green). Its folder lives at `_archive/2026-09-30_park/soul_land_3_fanfiction/` and is the **one resumable exception** to the archive law — start at its `foundation/PARKED_2026-09-30.md`. Its ch 7 commit is local-only; on any push, restore the remote first.
- **Workshop park:** `Soul_Land_3_Project/`, `blue_silver/`, and five dated root docs moved (git mv, zero content changes) into `_archive/2026-09-30_park/` — see that folder's README for the map.
- **New serial founded:** `soul_land_3_prequel/` — Soul Land 3 era, **thirty years before canon** (author-locked). Foundation phase; premise candidates P1–P4 await the author's pick. Read its `README.md` first.
- On-disk view now: root docs + `soul_land_2_new/` (live; its own agent owns it) + `_archive/2026-09-30_park/` + `soul_land_3_prequel/`.

## AMENDMENT — 2026-10-02 (add-only): the prequel was struck; the live serial is *One in a Thousand*

- The author deleted the prequel serial (*The Sixth Kilometer*, `soul_land_3_prequel/`), verbatim: *"Delete it we create another because you completely can't create fen fiction without following canon."* It is gone from the live tree; its commits stay in history; **do not revive it.**
- Its replacement, founded the same day on the author's full spec: **`soul_land_3_oc/` — *One in a Thousand*** (SL3 era; same town as Tang Wulin; dual track — canon on the page, complete and in order, with the OC parallel). Start at its `README.md`.
- Where the 2026-09-30 note above says `soul_land_3_prequel/`, read `soul_land_3_oc/`.

