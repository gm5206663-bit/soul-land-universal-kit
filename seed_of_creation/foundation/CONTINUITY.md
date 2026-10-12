# CONTINUITY — the single ledger

**This is the only continuity source.** Where this file and any codex file disagree, this file wins.

---

## 1. ABSOLUTE DATING — AND THE TWO CLOCKS

This project has **two clocks** and every arithmetic error in it will come from confusing them.

### Clock one: Douluo years (DC, the Douluo Calendar)

Protagonist arrives: **year 0 = ~12,650 DC** — the moment of Huo Yuhao's ascension and the
Time-Space Turbulence.

Derivation, shown so it can be checked rather than trusted:

```
SL1 begins (Tang San age six)          = 2637 DC      [canon — kit 01_CANON_SPINE §1]
SL2 is set ten thousand years later    = +10,000 y    [canon — SL2's own premise text]
⇒ SL2 era opens                        ≈ 12,637 DC    [derived]
SL2 spans Huo Yuhao's life to ascension≈ +13 to 26 y  [disputed — sources say 23, 25, 26]
⇒ ascension                            ≈ 12,650 DC    [derived, margin ≈ ±25 y]
SL3 begins ten thousand years after SL2≈ +10,000 y    [canon — stated repeatedly in SL3]
⇒ SL3 era opens                        ≈ 22,650 DC    [derived]
```

**The margin is real and is recorded rather than hidden.** No source checked dates SL2's start
in DC. The figure above is arithmetic on the kit's SL1 anchor plus canon's stated
ten-thousand-year gaps. Treat 12,650 as ±25 years and never derive a plot point that requires
precision better than that.

Formula for this clock: **DC ≈ 12,650 + Douluo years elapsed since the fall.**

### Clock two: divine years

Canon, in Tang San's own words in the source text: **a single day in the God Realm is equivalent
to a year in the mortal world, and this is true for every plane.** Receipt in `CANON_NOTES.md`.

```
1 divine day   = 1 Douluo year
1 divine year  = 365 Douluo years (using 360 or 365 changes nothing plot-bearing; record 365)
```

The user's ruling was that the protagonist is **twenty years old when Huo Yuhao ascends**. Read
on the divine clock:

```
20 divine years × 365 Douluo years = 7,300 Douluo years of mortal-plane time
```

But the ascension is a single moment, and the whole of DD2.5 occupies roughly **one divine
year** — which is the ten-thousand-year gap between SL2 and SL3. So twenty divine years of his
life cannot have elapsed *on Douluo's timeline* before the ascension. They elapsed somewhere
else, at a different rate, which is exactly what the seal-and-hidden-place design supplies.

**The resolution this project uses:**

```
He lived twenty subjective years in a hidden place outside Douluo's counting.
He arrives on Douluo at the turbulence.
By Douluo's reckoning he has existed for twenty DAYS at the ascension —
    because the hidden place ran on the divine ratio, not the mortal one.
By his own reckoning he is twenty.
Both statements are true and neither is a mistake.
```

This is a `[design]` structure on a `[canon]` ratio, and it is recorded as Reading A in
`NO_MISTAKE_LIVE_RULES.md`. **Reversible by the user.** If the ruling means twenty Douluo years
instead, this whole section must be rewritten and the hiding place re-derived — twenty Douluo
years before the ascension lands inside SL2, where the Divine Realm is not yet at war.

**Formula for this clock: divine years lived = 20 + (Douluo years elapsed since the fall ÷ 365).**

### Canon bounds on this story

```
- Act one must complete within roughly one divine year of the ascension, because that is how
  long DD2.5 occupies and the fusion, the escape and the disappearance all fall inside it.
- No god may be reachable on Douluo after the disappearance, for the whole remaining span.
- Tang Wulin's story begins ≈ 22,650 DC. Our serial may run up to that boundary but must not
  pre-empt it: Wulin is a child on Douluo with a sealed nucleus and no memory of the Divine
  Realm, and that stays true until SL3 opens.
- The Seeds' return and the successor choice are a ten-thousand-year horizon. Reserved.
```

**Check every chapter's end year against these BEFORE drafting.**

---

## 2. CHAPTER LEDGER

Panels must be contiguous — no overlap, no gap. Machine-checked by `verify.py` gate 5.

| # | Title | Years (Douluo) | DC | What happens |
|---|---|---|---|---|
| — | *none drafted* | — | — | — |

Row one is written the moment chapter one is drafted. Set its panel endpoints **before** writing
any date in the prose.

---

## 3. ANCHOR TABLE

One row per dated event, with the derivation visible in the note. New dates get checked against
this table *before* they are written, never after.

| Anchor | Year | Chapter | Note |
|---|---|---|---|
| SL1 begins | 2637 DC | — | `[canon]` kit 01_CANON_SPINE §1. The only hard DC date this project inherits |
| SL2 era opens | ~12,637 DC | — | 2637 + 10,000. `[canon]` gap, `[derived]` figure |
| **Huo Yuhao ascends — YEAR ZERO** | ~12,650 DC | — | 12,637 + ~13–26 (his age at ascension, `[disputed]`). Margin ±25 y |
| God of Destruction demands the core | year 0 | — | DD2.5 opens with the Committee meeting and the refused expansion `[canon]` |
| Tang San's one-year bet | year 0 | — | canon: if the premonition does not come true in one year, expand. One divine year = 365 Douluo years `[canon]` |
| The war; Xiao Wu taken; Tang San sealed | year 0 | — | `[canon]` DD2.5 |
| Tang Wulin born in the Divine Realm | year 0 | — | `[canon]` DD2.5. The Goddess of Life gifts him vitality |
| The Time-Space Turbulence | year 0 | — | `[canon]` DD2.5 climax |
| Hui Mie and Sheng Ming fuse; the two Seeds | year 0 | — | `[canon]` DD2.5. Cores left in Tang San's hands, consciousness surviving |
| Golden Dragon King breaks seal; nucleus enters Wulin | year 0 | — | `[canon]` DD2.5 |
| **The protagonist falls to Douluo** | year 0 | — | `[design]` on the canon mechanism that sends Wulin down. Same event-window, unnoticed |
| The Divine Realm swept away | year 0 | — | `[canon]` DD2.5. Hard boundary: no god reachable after this |
| SL3 era opens | ~22,650 DC | — | 12,650 + 10,000. `[canon]` gap, `[derived]` figure |
| The Seeds' return horizon | ~22,650 DC | — | canon: ten thousand years to return `[canon]`. Paid off in SL4 |

---

## 4. FORWARD REFERENCES

Every promise of the "X years later" kind, computed. Nothing is written into a chapter until the
target year is in this table.

| Promise | Made in | Lands on | Target | Status |
|---|---|---|---|---|
| The Seeds return after ten thousand years | *not yet made on page* | ~22,650 DC | canon horizon | reserved — do not spend early |
| A successor will be named for Destruction | *not yet made on page* | SL4 era | Tang Wulin `[canon]` | reserved — immune, never rerouted |
| The seal wears as he grows | *not yet made on page* | per stage | each unsealing | reserved — needs a ruling per stage |
| The hidden twenty years | *not yet made on page* | flashback or disclosure | before year 0 | open — how much he remembers is firewall L2 |

---

## 5. CHARACTER REGISTER

Everyone named, with first and last appearance. A name that appears once and is never tracked is
how a dead character walks back in.

| Name | Role | First | Last | Status |
|---|---|---|---|---|
| *the protagonist* | POV | — | — | unnamed — awaiting ruling |
| Hui Mie | father; God of Destruction | — | — | canon; becomes the Seed of Destruction in act one |
| Sheng Ming | mother; Goddess of Life | — | — | canon; becomes the Seed of Life in act one |
| Tang San | Sea God / Asura God; holds both Seeds | — | — | canon; immune |
| Xiao Wu | Tang San's wife | — | — | canon; immune |
| Huo Yuhao | God of Emotions; ascends at year zero | — | — | canon; immune |
| Tang Wutong | Butterfly Goddess | — | — | canon; immune |
| Tang Wulin | infant at year zero; canon's chosen successor | — | — | canon; immune |
| Golden Dragon King | breaks seal at the turbulence | — | — | canon; immune |
| Rong Nianbing | God of Ice; enters the Committee after the sacrifice | — | — | canon; immune |
| Zhou Weiqing | Destruction's subordinate who sides with Tang San | — | — | canon; immune |
| The Seven Original Sin Gods | Destruction's enforcement | — | — | canon; Pride, Greed, Sloth, Envy are named in source |
| God of Damage | captured Xiao Wu | — | — | canon |
| Ditian (Beast God) | 820,000-year Golden-eyed Black Dragon King | — | — | canon; on Douluo during the gap era |

No invented character is registered until they appear on a page. That is deliberate: a codex
full of people who never appear is a lie maintained at your own expense.

---

## 6. SUPERSEDED FILES

Stamped, retained for history, never used as continuity.

| File | Why stale | Replaced by |
|---|---|---|
| *none yet* | — | — |

This table gets a row the first time a file is superseded. An unstamped stale file is a trap
with a five-minute fuse.

---

## 7. WHAT THIS FILE DOES NOT CONTAIN, AND WHERE IT LIVES

```
Canon receipts and confidence tags     → foundation/CANON_NOTES.md
One-row-per-fact canon ledger          → foundation/CANON_LEDGER.md
Current rank / rings / age / position  → foundation/STATUS_PANEL.md  (the only place)
Decision receipts, append-only         → foundation/SERIAL_LOG.md
Undecided things and what they cost    → foundation/OPEN_DECISIONS.md
Who knows what                         → codex/KNOWLEDGE_FIREWALLS.md
Distances and extents                  → codex/PLACES.md
```

If a number appears in two of those places and they disagree, **this file and STATUS_PANEL.md
win** — STATUS_PANEL for current state, this file for dating.
