# TIMELINE — the dual clock

Set the endpoints **before** writing. Most timeline contradictions come from choosing a duration
in prose and discovering later that it does not fit the panel.

**This project has two clocks and they must never be mixed in a sentence.** Full derivation and
its margin live in `foundation/CONTINUITY.md` §1, which is the single continuity ledger and wins
over this file. This file is the working view.

---

## Rule 1 — One anchor per clock, everything derived

```
DOULUO CLOCK   anchor: year 0 = ~12,650 DC = Huo Yuhao's ascension and the turbulence
               conversion: DC ≈ 12,650 + Douluo years since the fall
               margin: ±25 years. No source dates SL2 in DC. Never derive a plot point that
               needs better precision than that.

DIVINE CLOCK   anchor: the protagonist has lived 20 years at year 0
               conversion: divine years lived = 20 + (Douluo years since the fall ÷ 365)
               basis: one divine day = one Douluo year, stated by Tang San in novel text
```

Never state two independent absolute dates. The second one is a bug waiting to happen.

## Rule 2 — Panels are contiguous

Each chapter's panel states a span in **Douluo years since the fall**. The next chapter starts
where the last one ended. No gaps, no overlaps — `verify.py` gate 5 checks this mechanically.

**Record the divine-clock equivalent in the ledger, never in the panel.** A panel carrying both
clocks invites a reader to do the arithmetic, and firewall Layer 5 says nobody on the plane is
allowed to do that arithmetic yet.

---

## THE RATIO, AND WHY IT IS THE SHAPE OF THIS SERIAL

| Divine time | Douluo time | What it means here |
|---|---|---|
| 1 day | 1 year | canon, stated in novel text |
| ~1 year (the whole of DD2.5) | ~365 years | the war, the fusion, the disappearance — a single divine year |
| 20 years (his life so far) | 7,300 years | how long he was hidden, measured on the plane he was hidden from |
| ~27.4 years | 10,000 years | his entire span on Douluo, if the serial runs to SL3's opening |

**The consequence that should drive the whole book:** he lives about twenty-seven more years
while the plane lives ten thousand. Everyone he meets dies. Every institution he knows is
replaced three times over. He is a being whose natural clock runs 365 times faster than the
world's, standing still in a world that will not stop.

That is not decoration. It is a source of pressure that ages whether or not he attends to it,
which is what `STATUS_PANEL.md` OPEN PRESSURES is for, and it makes the ten-thousand-year
countdown of the Seeds personally tolerable — ten thousand years is twenty-seven years to him,
which is exactly how long a person has to become someone.

---

## ANCHOR TABLE

| # | Chapter | Span (Douluo years since the fall) | Absolute | Key events |
|---|---|---|---|---|
| 1 | *not drafted* | must start at 0 | ~12,650 DC | the fall |
| 2 | *not drafted* | must start where 1 ends | derived | — |

## FIXED EVENTS

Events that must happen at a specific point. Everything else is derived around these.

| When | Event | Why fixed | Derived from |
|---|---|---|---|
| year 0, before the fall | Huo Yuhao ascends; Tang Wutong takes the Butterfly seat | canon, end of SL2 | `[canon]` #24 |
| year 0 | the Committee meeting; expansion refused; the one-year bet | canon, DD2.5 opening | `[canon]` #2, #14 |
| year 0 | the war: Xiao Wu taken, Tang San sealed, Yuhao and Wutong flee | canon | `[canon]` #14 |
| year 0 | Tang Wulin born in the Divine Realm; Sheng Ming's gift of vitality | canon | `[canon]`/`[fan]` #14, #15 |
| year 0 | the Time-Space Turbulence | canon, DD2.5 climax | `[canon]` #2 |
| year 0 | Hui Mie and Sheng Ming fuse; the two Seeds; cores to Tang San | canon; immune | `[canon]` #9–#11 |
| year 0 | the Golden Dragon King breaks seal; its nucleus enters Wulin | canon; immune | `[canon]` #15 |
| year 0 | Huo Yuhao sends Wulin down to Douluo | canon; immune | `[canon]` #15 |
| **year 0** | **the protagonist falls to Douluo** | `[design]` on the canon mechanism above — same event-window, unnoticed | Lock 2, Lock 3 C6 |
| year 0 | the Divine Realm swept away with every god | canon; hard boundary | `[canon]` #15 |
| year 0 onward | Tang Hao as Plane Master, A Yin as Life Core, already or imminently installed | canon | `[canon]` #33 |
| ~year 0 + 365 | the divine one-year bet expires, unanswered, because the realm is gone | derived | 1 divine year = 365 Douluo years |
| ~year 1,000 (≈ 2 divine years for him) | ~1,000 years after the Pagoda's founding: beasts still going extinct despite the truce; the Silver Dragon wakes in the Star Dou Great Forest | `[fan]` — **one source; atmosphere only until a second receipt exists** | `[fan]` #32 |
| ~year 10,000 (≈ 27.4 divine years) | SL3's era opens; Tang Wulin's story begins | canon gap | `[canon]` #41 |
| ~year 10,000 | the Seeds' ten-thousand-year return horizon; the successor is named — Tang Wulin | canon; immune; paid off in SL4 | `[canon]` #10, #12, #13 |
| `[disputed]` — inside SL3 | Shrek Academy and Shrek City destroyed by Holy Spirit Cult shells; the Ancient Golden Tree dies; 12 million+ dead; the Life Seed is planted in the crater lake | canon event, **disputed date — see CANON_NOTES.md §0 finding three. Far horizon, not on page until re-verified** | `[canon]`/`[disputed]` #35, #36 |
| SL3's end | the Abyss Plane's decisive battle; Tang Hao kills the Abyss Saint Emperor; Tang Hao and A Yin sleep | canon; immune | `[canon]` #34, #35 |

---

## DURATIONS

| From | To | Duration | Check |
|---|---|---|---|
| his arrival | SL3's opening | 10,000 Douluo years | = 27.4 divine years: 10,000 ÷ 365 = 27.397 |
| his arrival | the Seeds' return horizon | 10,000 Douluo years | canon states ten thousand years to return; matches the SL2→SL3 gap exactly |
| his hidden life | his arrival | 20 divine years | = 7,300 Douluo years of outside time, which is why it cannot have elapsed on Douluo before the ascension |
| the divine one-year bet | its expiry | 1 divine year | = 365 Douluo years |

**Show the arithmetic in this column, always.** A duration fixed by arithmetic should display the
sum, so a later edit cannot silently break it.

---

## CANON RECONCILIATION

Where this timeline meets canon dates. This is the section that catches the expensive errors.

| Story event | Story date | Canon constraint | Margin | Verdict |
|---|---|---|---|---|
| the protagonist's arrival | year 0 | must be at or after the ascension, inside the turbulence window | 0 | fits — the same event-window as Wulin's descent |
| his twenty years of prior life | before year 0 | cannot have elapsed on Douluo before the ascension | n/a | fits only because the hidden place ran on the divine ratio. This is Reading A, reversible |
| act one completes | within ~1 divine year of the fall | the fusion, the escape and the disappearance all fall inside DD2.5's ~1 divine year | ~365 Douluo years of slack | fits |
| no god reachable | year 0 to year 10,000 | canon: the Divine Realm is swept away; no ascension occurs in the gap | 10,000 y | fits — and it is a hard boundary. A god on the plane fails the chapter |
| the plane has a Plane Master and a Life Core | year 0 onward | canon #33 — installed around the disappearance | 0 | fits, and it constrains every concealment claim. See firewall Layer 1 |
| Tang Wulin met | ~year 10,000 | SL3 opens then; Wulin is a child on Douluo with no memory of the Divine Realm until then | 10,000 y | reserved. Never early |
| the successor named | ~year 10,000, paid off in SL4 | canon; immune | 10,000 y | reserved. Never rerouted |
| Shrek Academy's destruction | far horizon | `[disputed]` between two readings, both landing in SL3's era | ~10,000 y | **do not put on page until re-verified against SL3 text** |

**A negative margin is a hard fail.** Fix the story span; never move a user-locked anchor.

---

## THE SL2 DC ANCHOR, AND WHY IT IS A DERIVED NUMBER

```
SL1 begins                    2637 DC   [canon — kit 01_CANON_SPINE §1]
+ the canon 10,000-year gap   10,000    [canon]
= SL2 era opens              ~12,637 DC [derived]
+ Huo Yuhao's age at ascension 13–26    [disputed — sources say 23, 25, 26]
= YEAR ZERO                  ~12,650 DC [derived, margin ±25 y]
+ the canon 10,000-year gap   10,000    [canon]
= SL3 era opens              ~22,650 DC [derived]
```

No source checked gives a DC date for anything in SL2. The number above is arithmetic on the
kit's one hard SL1 anchor plus canon's stated gaps. **Use it as a spine, never as a fact.** It is
listed in `STATUS_PANEL.md` FORBIDDEN FIGURES as a thing not to be treated with false precision.

---

## SUPERSEDED TIMELINES

When a span is compressed or extended, record the old value. Do not delete it.

| Old span | New span | Reason | Date |
|---|---|---|---|
| *none yet* | | | |

The first likely entry: if the user revokes Reading A and rules that "twenty years old" means
twenty **Douluo** years, this entire file's divine-clock section changes and `CONTINUITY.md` §1
must be rewritten with it.
