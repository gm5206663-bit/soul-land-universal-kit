# ⚡ POWER MODEL v2 — CANON-LOCKED (rebuilt 27 Aug 2026)
### Supersedes v1 entirely. v1 was built before canon ch 99–135 was read, and canon disproved two of its
### central numbers. **Every figure below is either a canon number with a chapter citation, or explicitly
### marked DERIVED/CHOSEN with the reason it was chosen.**

---

## 0. WHY v1 HAD TO BE TORN DOWN

Two numbers in v1 were wrong, and both were load-bearing:

| v1 claimed | Canon says | Verdict |
|---|---|---|
| Lin Hao's spiritual power = **318** | **Gu Yue = 153** at canon ch 114, and canon calls her *"the single Soul Master on the entire continent… this young yet has such high level spiritual power."* At canon ch 134 she still has *"the greatest spiritual power"* of class zero. | 🔴 **v1 put our OC at more than double canon's crowned prodigy — in a story whose own codex says his speciality is NOT spiritual power.** |
| ~~Lin Hao's fist = 243 kg~~ **RETIRED — see §4; he measures 2,612 kg** | Canon ch 114 punch table, age 9–10: Zhang Yangzi **69**, Gu Yue **143**, Xie Xie **164**, Wang Jinxi **468**, Wulin **1,348** (scaled **2,700**). | 🔴 **v1 put a rank-30 boy carrying ~1,800 years of soul ring BELOW Wang Jinxi at rank 23.** |

**Root cause: I invented both numbers before I had canon's table to check them against.** Neither was a
stylistic choice. Both were unverified assertions that then propagated into 17 chapters.

---

## 1. THE GOVERNING PRINCIPLE (from THE_CODEX.md, unchanged)

> **His speciality is NOT spiritual power. It is that NOTHING IS LOW.**

Every line is solid. No single line is the continent's best. **That principle now has a hard consequence:
wherever canon crowns another character as the best at something, Lin Hao is second — visibly, and on the
page.** Canon's crowns are not ours to take. Taking Gu Yue's spiritual crown would violate the
BUTTERFLY-INTEGRATION LAW as surely as nerfing Lin Hao would violate the GROWTH LAW.

---

## 2. THE CANON SPIRITUAL-POWER LADDER (canon ch 134, verbatim — this is the ruler everything is measured with)

| Realm | Spiritual power | Spirit souls it can bear |
|---|---|---|
| **Spirit Origin** | 1–100 (innate from birth) | **one**; up to a single **yellow** |
| **Spirit Connection** | **100+** | **two yellow**, or **one purple** |
| **Spirit Sea** | **500+** | **five yellow / three purple / one black** |
| **Spirit Abyss** | **5,000+** | **any level, even orange and red** |
| **Spirit Domain** | **20,000+** | any; theoretical limit nine legendary |
| **Divine Origin** | **50,000+** | primordial spirit — a demigod |

Canon: *"the first four spiritual power realms were the most important."* *"A huge gap existed between Spirit
Connection and Spirit Sea, preventing the majority from ever reaching the latter."* **Spirit Sea is what
permits six or seven rings, and nine rings requires it.**

**Growth window (canon ch 114):** spiritual power grows with the body until **forty**; Soul Masters keep
growing it until **sixty**. So a ten-year-old is at the very bottom of his natural curve — **large numbers at
ten are canonically abnormal, and canon reserves them for Gu Yue.**

---

## 3. CORRECTED SPIRITUAL-POWER CURVES (the J1 fix)

**Canon anchors I must not contradict:**
- ch 17 (≈ our ch 3, **Glorybound, age 9**): Wulin **38** · the testing Spirit Master a 28th-rank Soul
  Grandmaster at **87**
- ch 69 (≈ our ch 11, **Eastsea, start of term**): Xie Xie **29** · Wulin **44** · Gu Yue **119**
- ch 114 (≈ our ch 20–21): Gu Yue **153**
- ch 134 (≈ our ch 33): Gu Yue highest of the five · Wulin **Spirit Connection** · the other three **at the
  boundary of Spirit Connection** (≈100)

⚠️ **CORRECTION (found while rebuilding ch 3):** v2's first table used canon ch 69's Eastsea figures
(Wulin 44 / Xie Xie 29) for the **Glorybound** chapters 1–3. That was wrong — those boys are not in Glorybound,
and canon ch 17 puts Wulin at **38** at age 9. Lin Hao's ch 1–3 figures were therefore set far too high
(74 at ch 3). Corrected below.

| Our chapter | Era | **Gu Yue** (canon) | **LIN HAO** 🔴 **v3.06: ABOVE her from ch21 on — the "second" column header was the codified disease, corrected 2026-08-29** | Wulin | Xie Xie |
| ⚠️ | *the rows 01–37 below are the **pre-ch21 baseline** and are kept for provenance. The live curve from ch21 is in the v3.06 note further down and in `checks/state.json`.* | | | | |
|---|---|---|---|---|---|
| 01–03 | Glorybound, age 6→9 | *not present* | **20 → 30 → 45** | **38** *(canon ch 17)* | *not present* |
| 04–10 | Eastsea arrival, age 9 | **119** *(canon ch 69)* | **45 → 62** | 38 → **44** *(canon ch 69)* | **29** *(canon ch 69)* |
| 11–16 | first term | 119 → 131 | **62 → 84** | 44 → 61 | 29 → 38 |
| 17–22 | tournament | 131 → **153** *(canon ch 114)* | **84 → 118 → 124** *(crosses 100 at ch 20)* | 61 → 84 | 38 → 52 |
| 23–28 | class zero | 153 → 168 | **131 → 136** | 84 → 100 | 52 → 66 |
| 29–33 | platform trials | 168 → 181 | **136 → 145** | 100 → 112 | 66 → 74 |
| 34–37 | pre-final-exam | 776 → **812** | **145 → 152** | 112 → 118 | 74 → 79 |

**Why this shape:**
- ~~**Gu Yue keeps her crown at every point.**~~ 🔴 **RETRACTED 2026-08-29.** Her **153 is a canon number and stays 153** — but "keeps her crown" was the belief that built the wrong curve. Canon's own line is *"eighty percent of Soul Masters are just barely able to reach the Spirit Sea realm"* (500): **153 is barely into Spirit Connection, not a crown.** The real wall is **SPIRIT SEA at 500.** He passes her at ch21 and `verify_power_scale.py` now enforces it.
- **At ch 3, Lin Hao is 45 against Wulin's canon 38** — clearly ahead, but not monstrously. He is not the
  spiritual specialist and the story should not pretend otherwise.
- 🔴 **v3.06 RE-BASELINE (2026-08-28) — supersedes both v2 and v3.** The v3 curve capped him **below**
  Gu Yue's canon 153 → 186 on the reasoning that *"canon forbids him above her"* and *"his crown was never
  his to take."* **That was the same disease as the strength error — ranking him inside a range built for
  somebody else.** Per **THE MONSTER LAW** he is above everyone except Tang San. Canon's line *"there is not
  a single Soul Master on the entire continent that is this young yet has such high level spiritual power"*
  is now **false because of him** — a divergence to be **stated**, not a ceiling to be accommodated.
  **Curve: 178 (ch21) → 184 → 191 → 196 → 205 → 212 → 218 → 226 → 233 → 241 → 249 → 256 → 264 (ch60) → 281 (ch61) → 289 (ch62). Above Gu Yue at every point.** 🔴 **ch62 note: the +8 into 289 came from WATCHING the Sky Ice, not from a fight — the "the fighting is the cultivation" rule is incomplete, and the chapter says so on-page.**
- 🔴 **The gap is the point — and it runs the other way now.** He is not second to anyone. Gu Yue's 153 was the continent's highest at her age **until him**, and she does not yet know that.
- **He is still far above Wulin, Xie Xie, Zhang Yangzi and Wang Jinxi** — no nerf against the class.

~~**🔴 CHANGE FROM v1: 318 → 152. This is a 52% cut and it touches 17 chapters. It is not negotiable, because
canon states Gu Yue's number and canon states she is the highest.**~~

🔴 **THE PARAGRAPH ABOVE IS THE FOSSIL OF THE DISEASE, KEPT ONLY AS EVIDENCE.** Canon states Gu Yue's
*number.* Canon does **not** state that she is the highest in a class that contains Lin Hao — that was my
inference, and for forty chapters a `LIN_BAND` table in `verify2.py` **enforced** it. That is how a wrong
belief survives: **the check kept the mistake alive after the reason for it was gone.** Standing rule:
**when a belief changes, the check enforcing it must change in the same edit, or the mistake is immortal.**

---

## 4. CORRECTED PHYSICAL STATS (the J2 fix)

**Canon ch 114 punch table (machine ceiling 5,000 kg, measures punch power only):**

| Student | Left | Right |
|---|---|---|
| Zhang Yangzi | 61 | **69** |
| Gu Yue | 115 | **143** |
| Xie Xie | 153 | **164** |
| Wang Jinxi | 423 | **468** |
| Tang Wulin | 1,156 | **1,348** |
| Tang Wulin, arm scaled | — | **2,700** |

**LIN HAO — CHOSEN, with the reasoning stated:**

| Stat | Value | Why |
|---|---|---|
| **Fist, right** | **2,612 kg** | **Above Wang Jinxi's 468**, which v1 wrongly put him below. Justified on three canon grounds: he swings **Thousand Refined** hammers daily (canon ch 42: rank-2 smiths cannot lift one 40 kg hammer), he carries **~900-year rings** which canon ch 131 says raise *"strength, speed, soul power, reaction speed, or the tenacity of one's body; all of them"*, and blacksmithing is a strength trade. |
| **Fist, left** | **2,478 kg** | Slight asymmetry — he is right-handed at the anvil. Canon gives Wulin the same left/right split. |
| **Blacksmith's pillar** (50 kg hammer, weight deducted) | **~3,172 kg** | A separate machine (canon ch 25–26). Wulin hit 483/543 there at **age nine**. Lin Hao is older and stronger, so he must clear it comfortably — but the pillar is not the punch machine and the two must never be conflated again. |
| **Ceiling honesty** | never stated as a final number | Canon ch 36 already established the true figure is *"past the marks on the dial."* Keep that. Give the measured number, then say the measurement is the limit of the instrument, not of him. |

**🔴 STRENGTH RE-BASELINED TWICE, 2026-08-28: 243 → 612 → 1,612 → 2,612 kg.** The first three values were all wrong for the same reason: they placed him inside canon's ch114 punch table, which is a list of OTHER children. **THE SCALE (user-locked): Wulin at rank 15 ≈ a normal 3-ring master (1,156/1,348 kg, his single greatest asset). Lin Hao at rank 36 ≈ a 4-ring SOUL ANCESTOR in physical strength alone — a ring tier above Wulin in Wulin's own best attribute. And physical is NOT his best: his overall combat is Soul King.** See THE_CODEX.md §THE TWO AXES.
non-bloodline prodigy belongs.**

---

## 5. WHAT IS GATED AND WHAT IS NOT (unchanged from v1 — this part was correct)

| Gated at rank 30 | NOT gated — still rising |
|---|---|
| The rank number | **Soul power** (rises within the band) |
| The third ring | **Spiritual power** (152 → 499 available before Spirit Sea) |
| | **The hawk's age** (950 → 1,000) |
| | **The rings' age** (~900 → 1,000) |
| | **Body, mutations, soul power capacity** |

**He is coiled, not blocked.**

---

## 6. THE RINGS

> 🔴 **CORRECTED 2026-08-28 — this section described a future event that has already happened.**
> The crossing **occurred in ch40**: hawk 964 + 200 per ring = **1,164**, both rings re-formed
> **purple**, and a **third ring was bestowed**. The hawk is now **1,399 years**. Everything below
> is written in the past tense. The rank ceiling is **derived from the ring count** in
> `checks/state.py` (`N rings ⇒ ranks N·10+1 … (N+1)·10`), so it moved to **40** automatically and
> can never go stale again. Hardcoding it was the original bug.

- **Three PURPLE rings**, all perfectly compatible — so they express *more* than a normal purple ring
  of the same age. A normal three-ring master has **2 yellow + 1 purple** (canon: Guang Long, rank 27)
  or **three yellow** (canon: the Skysea Academy captain).
- **The third ring was gated by the 1,000-year crossing**, and by canon ch 46's absorption ceiling:
  *"White spirit souls could only offer up one soul ring and currently, Soul Masters could only absorb
  up to three spirit souls."* Both conditions are now satisfied.
- **Colour follows current age tier** (RING-COLOR LAW v2.50): the rings were **yellow** at ~900 years
  and re-formed **purple** at the crossing (ch40, on-page).
- **Canon ch 134 confirms a thousand-year spirit soul bestows THREE soul skills.**
- 🔴 **THE CONSEQUENCE THAT WAS MISSED:** canon says *"if his spirit soul was upgraded, then the soul
  skills it provided would be upgraded too."* So **Gale Talon and Hawk-Soul Union both upgraded to
  thousand-year tier at ch40** — and no chapter shows it. Tracked as **F1** in
  `PROBLEM_INVENTORY.md`; `verify_ensemble.py` §7c warns on every run until it is written.
- **Effective combat power is 🔴 SOUL KING (51–60), ceiling Soul King peak** — 15 to 24 ranks above his
  own number. See `THE_CODEX.md` §THE ADVANTAGE LEDGER for the benchmark against normal 3rd/4th/5th-ring
  masters, and §THE REALM GAP LAW for why a lower-realm character cannot defeat him.
- **Next: the fourth ring.** Ten-thousand-year+ second spirit soul ⇒ **BLACK ring**, and the martial
  soul evolves to **TOP-LEVEL**. Canon: *"Normally, soul masters don't get a ten-thousand-year soul
  ring until rank 50"* — he will do it at ~40. 🔴 **"Divine Stormbringer" is CANCELLED.**


---

## 7. HOW THIS BINDS THE REBUILD

Every rebuilt chapter must satisfy:
1. **Lin Hao's spiritual power at chapter N = the table in §3.** Not higher, not lower.
2. **Gu Yue's number at chapter N = the table in §3, and it is always higher than his.**
3. **Any strength figure = §4.** The **243, 612 and 1,612 kg readings are all retired** and must not reappear. The measured value is **2,612 kg (ch32)** and the ch21 figure is **812 kg**.
4. **Any ring claim = §6.** Yellow until the 1,000-year crossing.
5. **Where canon crowns someone else, Lin Hao is second and the text acknowledges it.**

`checks/verify2.py` enforces 1–4 mechanically. See `archived: CODEX/98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz` for the per-chapter ledger.
