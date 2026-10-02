# TIMELINE — live codex for `chapters_rebuilt/`

Built from `SOUL_LAND_UNIVERSAL_KIT/templates/TIMELINE.md`.

**This file is LIVE continuity.** `bluesilver_codex/TIMELINE.md` is SUPERSEDED. Where this
file and `REBUILD_CONTINUITY.md` disagree, **`REBUILD_CONTINUITY.md` wins** — it is the
authoritative ledger and this file is a derived view of it.

---

## Rule 1 — one anchor, everything derived

**Anchor:** his year 0 = **≈1837 DC** `[user ruling]` — never move this.

**Conversion:** `DC ≈ 1837 + age`

Every absolute date in this project is that anchor plus an offset. There is no second
independent absolute date anywhere in the serial. The rebuild compressed the back half
(Ch10–15) rather than moving the anchor, precisely to preserve this.

## Rule 2 — panels are contiguous

Every chapter panel states a span; the next starts where the last ended. No gaps, no
overlaps. Machine-checked by `SOUL_LAND_UNIVERSAL_KIT/tools/verify.py` gate 5.

**Current result: 15 panels, 0 overlaps, 0 gaps.**

---

## Anchor table

| # | Title | Years | DC |
|---|---|---|---|
| 1 | Awake | 0–1 | 1837–1838 |
| 2 | What the Water Teaches | 1–40 | 1838–1877 |
| 3 | The One Who Stayed | 40–105 | 1877–1942 |
| 4 | The Teeth in the Grass | 105–190 | 1942–2027 |
| 5 | The One Who Watched | 190–240 | 2027–2077 |
| 6 | The One Below | 240–300 | 2077–2137 |
| 7 | The One Who Keeps | 300–360 | 2137–2197 |
| 8 | The One Who Crossed | 360–440 | 2197–2277 |
| 9 | The Last Vigil | 440–500 | 2277–2337 |
| 10 | The One Who Answers | 500–580 | 2337–2417 |
| 11 | The Liar at the Door | 580–650 | 2417–2487 |
| 12 | The Ten Thousandth Year | 650–700 | 2487–2537 |
| 13 | The One Who Goes | 700–735 | 2537–2572 |
| 14 | The Ground That Remembers | 735–753 | 2572–2590 |
| 15 | The One Who Is Named | 753–775 | 2590–2612 |

Span: year 0 → 775, i.e. ≈1837 → ≈2612 DC.

---

## Fixed events

Do not drift these. The "derived from" column shows the arithmetic so a later edit cannot
silently break it.

| Year | Event | Derived from |
|---|---|---|
| 1 | first hunting party | Ch1 — fixed |
| ~30 | flood lays the silt | Ch2 — fixed |
| 61 | mantis arrives | Ch3 — fixed |
| **98** | **the killing** | Ch3 — fixed; founds the mercy law |
| 104 | mantis dies | 61 + 43 |
| 163 | shadow cat | Ch4 — fixed |
| ~193 | surveyor marks grid nineteen unresolved | 163 + 30 ("thirty years had gone by") |
| ~243 | serpent night | Ch6 — fixed |
| 301 | night-walker arrives | 243 + 60 |
| 340 | expedition turned | Ch7 — fixed |
| 402 | found one arrives | Ch8 — fixed |
| **468** | **night-walker dies — REFUSAL 1** | Ch9 — fixed |
| 508 | found one answers | 468 + 40 alone |
| 557 | assessor Orrin Vase | Ch10 — fixed |
| 592 | the liar | Ch11 — fixed |
| 630 | found one dies | 402 + 228 |
| **665** | **King gate, Stage 3** | Ch12 — fixed |
| 672 | grid reclassified, refugees hunted out | Ch12 — fixed |
| 706 | last small stock taken | Ch13 — fixed |
| 714 | root-mass lifts | Ch13 — fixed |
| 735 | arrives in the valley | 714 + 21 |
| **746** | **old king dies — REFUSAL 2** | Ch14 — fixed |
| 751 | Hall report names the valley | Ch14 — fixed |
| **753** | **A Yin appears; the naming → ≈2590 DC** | Ch15 — fixed |

## Durations

| From | To | Duration |
|---|---|---|
| King gate (665) | root-mass lifts (714) | 49 |
| King gate (665) | arrives valley (735) | 70 |
| root-mass lifts (714) | arrives valley (735) | 21 |
| grid unresolved (193) | expedition turned (340) | 147 |
| mantis arrives (61) | mantis dies (104) | 43 |
| found one arrives (402) | found one dies (630) | 228 |

---

## Canon reconciliation

| Story event | Story date | Canon constraint | Margin | Verdict |
|---|---|---|---|---|
| The naming | 2590 DC | A Yin's rooted era ends < ≈2621 DC | **+31 yrs** | PASS |
| End of Ch15 | ≈2612 DC | A Yin's rooted era ends < ≈2621 DC | **+9 yrs** | PASS |
| Ch15 coda "in forty-seven years" | 2590 + 47 = **2637 DC** | Tang San emerges 2637 DC (`CANON_NOTES.md:145`) | **0** | PASS — exact |
| Implied death year | ≈2930 DC (yr 1093) | after SL1 events | n/a | acceptable per `CANON_NOTES.md:14` |

**The tightest margin is +9 years.** Any future edit that extends the span past year 784
breaks canon. Compress; never move the 1837 anchor.

---

## Cultivation

| Year | Cultivation | Note |
|---|---|---|
| 500 | ≈7,000 years | |
| 610 | ≈9,000 years | |
| 665 | **10,000 years** | King gate, Stage 3; a black ring becomes possible |

**He takes nothing for 775 years.** Kill count zero, permanent.

---

## Superseded timelines

| Old span | New span | Reason | Date |
|---|---|---|---|
| ~1,175-year span | 775 years | naming fell ≈49 yrs past A Yin's rooted-era end | 2026-09 |
| Ch14 panel `735–765` | `735–753` | overlapped Ch15's `753–775` | 2026-09 |

Do not delete these rows. They are the receipt for why the back half reads as it does.
