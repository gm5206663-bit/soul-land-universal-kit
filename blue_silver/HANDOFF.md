# HANDOFF — Blue Silver

**Read this first. It is the only file in this project that says what is true *now*.**

Built to `SOUL_LAND_UNIVERSAL_KIT/templates/HANDOFF.md`. Rewrite it at the end of every work
session.

---

## 1. One-paragraph state

Blue Silver is a Soul Land pre-canon serial about a Blue Silver Emperor grass named **Home**.
The first draft (`chapters/`, 15 chapters, ~80,700 words) was **rejected by the user as
"nonsense"** and has been fully rebuilt. The live serial is `chapters_rebuilt/` — 15
chapters, 33,100 prose words, spanning year 0 to 775 (≈1837–2612 DC), passing every gate.
Kill count is zero and permanent. Book One is complete and ends with A Yin naming him.

## 2. Authority order

1. The user's words
2. `bluesilver_foundation/REBUILD_CONTINUITY.md` — **the authoritative ledger**
3. `rebuild_codex/` — derived views of that ledger
4. `chapters_rebuilt/` — the text itself
5. `SOUL_LAND_UNIVERSAL_KIT/` — method and law

Where any two disagree, the higher one wins.

## 3. Edge

**Book One is complete.** Chapter 15, year 775, ≈2612 DC. Home is named.

| | |
|---|---|
| Rank | King gate, Stage 3 (10,000 years at yr 665) |
| Rings | none taken, ever |
| Age at end of Ch15 | 775 years |
| Named | year 753, ≈2590 DC |
| Kill count | **zero, permanent** |

Book Two is not started and not authorised.

## 4. Locked decisions

| Lock | Value |
|---|---|
| ERA | deep pre-canon, Star Dou Forest; birth ≈**1837 DC** — `[user ruling]`, never move |
| PROTAGONIST | Blue Silver Emperor grass. NOT: no royal/dragon/devour blood, nothing fused in |
| CANON ENTRY | Blue Silver Valley is canon; A Yin canon; Tang San emerges 2637 DC |
| SPINE | **Spirit Hall wants rings, and sends hunters into the forest to take them** |
| POWER CEILING | 10,000 years / King gate Stage 3 by yr 665; takes nothing |
| IDENTITY | unnamed until yr 753; A Yin names him **Home** |
| ABSOLUTES | **never kills** — no exception, no accident; dormant ritual powers |
| CANON IMMUNITY | A Yin's canon fate is never staged on page |
| MEASUREMENT | exact figures in panels/ledgers only; prose gets round felt counts |
| VOICE | third person, past tense; English only, zero CJK |
| CADENCE | one chapter per pass |

## 5. Live files vs stale files

**This is the section that matters.** Two superseded directories sit beside their live
replacements and the names are similar.

| Path | Status |
|---|---|
| `chapters_rebuilt/` | **LIVE** — the serial, sole continuity source for text |
| `rebuild_codex/` | **LIVE** — codex; start at `CODEX.md` |
| `bluesilver_foundation/REBUILD_CONTINUITY.md` | **LIVE** — authoritative ledger |
| `bluesilver_foundation/REBUILD_PLAN.md` | **LIVE** — seven-point chapter contract |
| `bluesilver_foundation/NO_MISTAKE_LIVE_RULES.md` | **LIVE** |
| `bluesilver_foundation/FOUNDATION.md` | **LIVE** — footer rule REVOKED, slim panel |
| `bluesilver_bible/BEAST_LAW.md` | **LIVE** — ring tiers, Titled Douluo |
| `bluesilver_foundation/CANON_NOTES.md` | **LIVE** — canon receipts |
| `chapters/` | **SUPERSEDED** — the rejected draft. Fails 29 gates. History only |
| `bluesilver_codex/*.md` (7 files) | **SUPERSEDED** — banners say so; do not read as continuity |
| `README.md` | **SUPERSEDED** — bannered; its premise prose is still fine, its state is not |
| `ADAPTATION_TALENT.md` | PARTIALLY SUPERSEDED — see its banner |

**If `chapters/` and `chapters_rebuilt/` disagree, `chapters_rebuilt/` wins.**
**If `bluesilver_codex/` and `rebuild_codex/` disagree, `rebuild_codex/` wins.**
**If anything and `REBUILD_CONTINUITY.md` disagree, `REBUILD_CONTINUITY.md` wins.**

## 6. Open questions

- Book Two is unwritten and unauthorised. Do not start it without the user saying so.
- The nine human dossiers exist in `rebuild_codex/CHARACTERS.md`. They are not mirrored into
  the superseded `bluesilver_codex/CHARACTERS.md` and should not be — that file is history.

## 7. Known gaps

- `rebuild_codex/CREATURES.md` does not exist. Beast detail lives in
  `CHARACTERS.md` §THE BEASTS and `bluesilver_bible/BEAST_LAW.md`. Create a separate file
  only if beast detail outgrows the characters file.
- The tightest canon margin is **+9 years** (end of Ch15 at ≈2612 DC vs A Yin's rooted era
  ending <≈2621 DC). Any edit extending the span past year 784 breaks canon. Compress; never
  move the 1837 anchor.

## 8. Do-not list

- Never kill. Kill count stays zero. No exception, no accident, no self-defence.
- Never move the 1837 DC birth anchor.
- Never soften or retcon either refusal (yr 468, yr 746), and never give a fourth option.
- Never stage A Yin's canon fate.
- Never call Blue Silver Valley a `[design]` name. `[user ruling 2026-09]` — it is canon.
- Never re-add the revoked footer rule, or the revoked "canon nowhere names it" wording.
- Never write digits in prose. Exact figures belong in panels and ledgers.
- Never re-stamp the already-stamped superseded files.

## 9. Last verification

Run from `/home/user`:

```
python3 SOUL_LAND_UNIVERSAL_KIT/tools/verify.py blue_silver/chapters_rebuilt/
```

| Suite | Result |
|---|---|
| Rebuilt serial | **PASS** — 15 files, 33,100 prose words, 0 failures, 0 warnings |
| Live codex (6 files) | **PASS** — 0 unreadable script, 0 backslash-n, 0 placeholders |
| Rejected draft `chapters/` | **FAIL** — 29 failures (expected; it is the negative control) |

Gate note: `tools/verify.py` has seven hard gates. Gates 3–5 and 7 are chapter gates; gates
1–2 apply to every file; gate 6 applies to shipped prose but **never to templates or law
files**. See `SOUL_LAND_UNIVERSAL_KIT/09_AUDIT_LAW.md`.
