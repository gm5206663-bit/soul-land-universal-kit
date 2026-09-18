# ⚠️ PROBLEM INVENTORY — everything known to be wrong
### Created 27 Aug 2026 after the user's correction: *"there is too many things remaining you needed to correct them"*
### **This file is the single place where every known problem lives. Nothing gets fixed until it is listed here, and nothing gets dropped from here until it is verified fixed.**

**How to use:** work top-down. Do not fix one thing and move on — check whether the fix broke
something else on this list. Update the STATUS column every time.

---

## ⚠️ SESSION 2026-08-29 (ch62) — THE TWO-COPIES DISEASE, FOUND AND CLOSED AT THE ROOT

The user's standing correction is *"solve problems permanently, not after every chapter."* Writing ch62
exposed a whole family of the same bug, and it is one bug, not nine:

> **A fact maintained in two places will be wrong in one of them, and the check reads the other.**

Layer 0 already derives `LIN_HAO_STATUS.md`, `CONTINUATION_PROMPT.md` and the `### Ensemble` footer block.
Nothing ever compared **the hand-written part of a footer** against the generated block sitting underneath
it. Ten layers ran green over all of the following:

| # | What was wrong | How long | Fix |
|---|---|---|---|
| **D1** | 🔴 **`"Xie Xie's soul power is the highest"`** copied verbatim from canon c184 into the footers of **ch52–59** — the exact line the user caught in ch52, still shipping eight chapters later because it lived in the *generator*, not the chapter. | 8 chapters | **Fixed at the source:** `ensemble_schedule.py::HIGHEST_XX` now reads *"highest soul power in class zero **except Lin Hao**"*. One edit, all 62 footers. |
| **D2** | 🔴 **38 stale ensemble ranks** in the hand-written footers (Wulin said 15 while the block below said 18; Xie Xie said 21 while it said 23; Wei Xiaofeng said 22 while it said 26; Wang Jinxi given a rank after he left). | up to 49 chapters | Fixed, and the **schedule re-baselined to the prose** where the prose was right — see D3. |
| **D3** | 🔴 **THE SCHEDULE AND THE PROSE DISAGREED ABOUT WULIN.** Schedule said canon's **11**; ch9 prose says on-page *"Wulin, who had been rank thirteen since before enrollment."* Both were "right" and nothing compared them. **The prose is the story.** | 61 chapters | Schedule now reads **13 (ch4–8) → 14 (ch9)**, labelled AU with the canon delta recorded at the source. |
| **D4** | 🔴 **THE LEDGER WAS THE SPIRITUAL POWER.** ch60 said `ledger 264` (its spiritual power, two words earlier on the same line). The same paste was in **ch32–35, ch37** (`ledger 205`). | up to 30 chapters | Chain rebuilt monotonic: 71 → 78 → 79 → 83 → **95** (ch29 wolf pack) → 96 → 97 → 98 → 100 → 101 → 104 → 107 → **109**. Prose counts in **ch37** ("ninety-one lines") and **ch50** ("eighty-four lines") corrected to match. |
| **D5** | 🔴 **FIVE GROWTH HEADERS HAD THE SPIRITUAL POWER IN THE RANK SLOT** — ch40 `rank 205`, ch45 `238`, ch49 `254`, ch54 `270`, ch59 `290`, ch60 `294`. Soul ranks run 1–100. | 5 chapters | Corrected to 31/32/33/34/35/36. |
| **D6** | 🔴 **THE AUTHORITATIVE POWER SNAPSHOT TABLE WAS 32 CHAPTERS STALE** — still describing the rank-30 hard wall, two yellow rings, hawk 926, ledger 84, 3rd-rank Grandmaster. It is headed *"audit this EVERY chapter."* | 32 chapters | Rebuilt to match `checks/state.json`, with a comment saying why it must never be hand-maintained again. |
| **D7** | 🔴 **THE CODEX STILL ENFORCED THE RETIRED SPIRITUAL-POWER BELIEF** — *"the old curve put him ABOVE Gu Yue's canon 153/186, which canon forbids. He is second at every point."* `POWER_MODEL.md` said *"Gu Yue keeps her crown at every point"* and *"canon states she is the highest."* | since v2.63 | Both retracted on the page, kept as evidence, and the standing rule written down: **when a belief changes, the check enforcing it must change in the same edit, or the mistake is immortal.** |
| **D8** | 🔴 **THREE PARSERS WERE SILENTLY WRONG.** (a) `state.py::RE_SP` could not see through `**`, so a `281 → 289` chain recorded **281**. (b) The ledger parse took the chain's **start**, not its end. (c) `RE_SP.search` matched the narrative phrase *"eight points from spiritual power from WATCHING"* and recorded **no value at all** for ch62. (d) `verify.py::CURVE` was a hardcoded list, so a brand-new value (289) was invisible to the check. | — | All four derive from one source now. `CURVE = sorted(set(SP.values()))`. |

### 🔒 THE NEW LAYER

**`checks/verify_footer_facts.py` — LAYER 11.** Compares every hand-written footer against
`ensemble_schedule.py` and `checks/state.json`: seven tracked characters' ranks, Lin Hao's
rank / spiritual power / hawk / ledger, the GROWTH header vs the footer, ranks > 100, a ledger that goes
backward, and a ledger equal to the spiritual power on the same line. **It found 99 contradictions on its
first run; four were its own false positives and were calibrated out by name; it now stands at 0.**
Added to `run_all.sh` (which also had a duplicated 4-line header block, removed). **Eleven layers.**

<!-- OPEN-PROBLEMS — MACHINE-READABLE. ONE PER LINE: id | problem | status
     🔴 This block is the SINGLE SOURCE for the owed list. `CODEX/consequence.py brief` and
     `checks/build_continuation.py` both read it. Three earlier attempts to scrape the free-text
     tables above produced three different wrong answers, because those tables mix open and closed
     rows across ten id series and their cells contain literal pipe characters. A generated
     document must have one unambiguous source. Layer 5 checks this block against the table.
     Keep it in sync: when you close a line here, close the row in the table too. -->
<!-- OPEN-PROBLEMS-BEGIN
K3 | Three Thunders in One Voice — the synchronisation of all three soul skills — has never been done on-page. Largest multiplier in his kit. | Open
K4 | The battle-armor-smithing thread is OPENED and unfulfilled. Xie Xie decided out loud in ch62: you are going to make the metal. Mu Chen's canon line — the foundation of a battle armor master stems from being a first-rank blacksmith — was never connected to Lin Hao until ch62. | Must not be dropped
K5 | Shen Yi is Wu Zhangkong's TEACHER, now on the page, but their history is unexplored and Shrek is still not named as his origin (canon ch204 reveal). | Open, scheduled
K6 | Canon gaps — ch 28 missing, ch 1-22 not held, nothing past ch 600 (and 600 is not the ending), canon 337-600 skimmed not read. | Open
K7 | HAWK-SOUL UNION has never been used on-page, 62 chapters in. Deliberate (D006), but it upgraded to thousand-year tier at ch40 and that half has never been shown. The debt is not the upgrade; it is that the trump card has no shape in the reader's mind. | Open by decision, 22 chapters old
K8 | Butterfly density measures presence, not quality. A chapter can score 1.3 per thousand words and still be thin. | Method
K9 | 🔴 HAWK-SOUL UNION must be RE-THOUGHT, not just used. The hawk now shares him with a ten-thousand-year jiao. What that does to a perfectly-bonded soul spirit has never been examined. DOMINEER (the fourth ring's stroke) has also never been used on-page. | Opened by ch71
K10 | 🔴 THE SHREK WORKING-STUDENT ARC IS HALF-ADAPTED. Found by reading canon 288-306 in full. Missing entirely: the dormitory is ONE run-down 30 sq m room with two bunk frames and no walls between boys and girls (c288); their assigned arrival job is CLEANING SPIRIT ICE PLAZA, which Gu Yue does with a water-and-wind whirlwind in four and a half hours, half of it spent recovering (c288-289); they start with 100 contribution points each, which is ONE DAY of food (c289); Feng Wuyu personally recruited Tang Wulin (c306); Elder Cai is the usual lecturer and is absent, which is why Shen Yi runs it (c295, c305). Missing CHARACTERS: the frail three-ring power-type working student (student number two) who beat Xie Xie in the entrance exam and whom none of the four dare claim to beat (c288-289); the RED-HAIRED FALLEN ANGEL GIRL with two rings who is also a working student (c303-304). | 🔴 Open — found 2026-08-30
K11 | 🔴 OUR TIMELINE IS ~2 YEARS COMPRESSED AGAINST CANON AND WAS NEVER RECORDED until D032. Canon has Tang Wulin at thirteen at Shrek (c305: "at the young age of thirteen, stood 165 centimeters tall"); our story has him at 10-11. Our own CANON_ACCESS.md already recorded "at age thirteen" and nothing compared it to the prose. Every future canon comparison must convert ages through the offset. | 🔴 Recorded (D032) — must be applied
OPEN-PROBLEMS-END -->

### 🔴 STILL OPEN (not found this session — carried forward)

| # | Problem | Status |
|---|---|---|
| ~~**K1**~~ | ~~The purple-ring skill evolution is unwritten.~~ 🔴 **I ASSERTED THIS FALSELY ON 2026-08-29 AND IT IS RETRACTED.** **F1 WAS CLOSED IN ch40.** The evolution is on-page: *"Gale Talon is now a **thousand-year soul skill** — he lays the same strike he has laid four hundred times, changes nothing, and a thirty-metre deadfall comes apart instead of opening."* Gu Yue: *"Your skill didn't improve. It got **older**… A soul ring isn't a container. It's a **permission.**"* `verify_ensemble.py` already detects the evidence in prose and reports it landed. **I propagated a stale line from `CONTINUATION_PROMPT.md` into four documents without reading ch40 — the exact "assert without verifying" failure this project keeps catching.** **What is genuinely still owed is the OTHER half: Hawk-Soul Union's upgrade was never shown on-page, because its first use is still reserved (D006). See K7.** | ✅ **CLOSED (ch40) — retracted, not fixed** |
| ~~**K2**~~ | ~~The fourth-ring arc is not written.~~ **WRITTEN — ch69 (the jiao found, the month begins) and ch71 (the emergence).** Every locked element is on-page: rank 40 → 45, the BLACK fourth ring, spiritual power 517 (Spirit Sea), Stormbringer Sword → **Frost Abyss Sword** (top-level), the **Frost Abyss Domain** appearing and nobody naming it, the body changing so far that Wulin does not recognise him, and the personality change shown through other people. **What is still owed out of the arc is in K9/K10, not here.** | ✅ **CLOSED (ch69 + ch71)** |
| **K3** | **「三雷合鸣」 Three Thunders in One Voice** — the synchronisation of all three skills — has never been done on-page. Largest multiplier in his kit. | Open |
| **K4** | **NEW AT ch62: the battle-armor-smithing thread is OPENED and unfulfilled.** Xie Xie decided out loud: *"you're going to make the metal."* Mu Chen's canon line — *"the foundation of a battle armor master stems from being a first-rank blacksmith"* — was never connected to Lin Hao until now. | **Must not be dropped** |
| **K5** | **NEW AT ch62: Shen Yi is Wu Zhangkong's TEACHER** and it is now on the page (*"Congratulations, Zhangkong"*), but their history is still unexplored and **Shrek is still not named as his origin** (canon ch204 reveal). | Open, scheduled |
| **K6** | Canon **ch 28** missing; ch 1–22 not held; nothing past **ch 600** (and 600 is not the ending). Canon 337–600 is skimmed, not read. | Open |
| **K7** | **HAWK-SOUL UNION has never been used on-page — 62 chapters in.** Deliberate (D006: *"It's not a demonstration. It's a decision."*), but it upgraded to **thousand-year tier at ch40** and that half of the upgrade has never been shown, because showing it means spending it. **The debt is not the upgrade, it is that the trump card has no shape in the reader's mind after 62 chapters.** | Open by decision — and now 22 chapters old |
| **K8** | **Butterfly density measures presence, not quality.** A chapter can score 1.3/1k and still be thin. The measure cannot tell the difference and I should stop trusting it as a quality signal. | Method |
| **K9** | 🔴 **NEW AT ch71: HAWK-SOUL UNION must be RE-THOUGHT, not merely used.** The hawk now shares him with a ten-thousand-year jiao. What that does to a perfectly-bonded soul spirit has never been examined — and the trump card has still never been spent (D006, K7). 🔴 **DOMINEER (「镇」), the fourth ring's stroke, has also never been used on-page**, and **nobody has named the Frost Abyss Domain.** | 🔴 Opened by ch71 |
| **K10** | 🔴 **THE SHREK WORKING-STUDENT ARC IS HALF-ADAPTED — found 2026-08-30 by reading canon 288–306 in full instead of quoting the extracted lines.** **Missing worldbuilding:** the dormitory is **one run-down 30 m² room with two bunk frames and no walls between the boys and the girls** (c288) · their assigned arrival job is **cleaning Spirit Ice Plaza**, which Gu Yue does with a water-and-wind whirlwind in **four and a half hours, half of it spent recovering** (c288–289) · they start with **100 contribution points each, which is one day of food** (c289) · **Feng Wuyu personally recruited Tang Wulin** (c306) · **Elder Cai is the usual lecturer and is absent, which is why Shen Yi runs the class** (c295, c305). **Missing characters:** the **frail three-ring power-type working student (student number two)** who beat Xie Xie in the entrance exam and whom none of the four dare claim to beat (c288–289) · the **red-haired Fallen Angel girl with two rings**, also a working student (c303–304). | 🔴 Open |
| **K11** | 🔴 **OUR TIMELINE IS ~2 YEARS COMPRESSED AGAINST CANON** — recorded as **D032** on 2026-08-30. Canon has Tang Wulin **thirteen** at Shrek (*"at the young age of thirteen, stood 165 centimeters tall"*, c305); our story has him at **10–11**. **Our own `CANON_ACCESS.md` already recorded *"at age thirteen"* and nothing compared it to 71 chapters of prose.** The prose wins (D030's rule), so the divergence stands — but **every future canon comparison must convert ages through the offset instead of reading them across.** | 🔴 Recorded — must be applied |
| ~~**K9**~~ | ✅ **CLOSED 2026-08-29 — THE VOICE.** The user's correction: *"the writeing style of your is very bad you should write like you write Frist three chapters."* Measured disease: **84** uses of *"I would like you to notice"* (0 in ch1–3), **294** *", and that"* chains, **41** record-keeping meta-voice instances, **100+** first-person journal-narration bold blocks. **All now 0 across all 62 chapters** (verified). **ch55–62 fully rewritten** in the ch1–3 voice — third person, scene-and-dialogue driven, journal rendered as *italic in-scene text*. **ch4–54**: tics/meta excised surgically, journal-narration bold converted to italic. `verify_style.py` (Layer 12) now enforces it: FAILS any chapter at/after ch62 that regresses, and measures the real signal (journal-voice bold) not raw proxies. See `THE_CODEX.md §THE VOICE LAW`. | ✅ **CLOSED — 0 tics, 0 meta-voice, 0 journal-bold across all 62. Two checks were recalibrated after proving they cried wolf: dialogue-ratio (fires on solo chapters) downgraded to informational; raw-bold replaced with journal-voice-bold.** |

---

## A. BLOCKING — the story cannot continue until these are resolved

| # | Problem | Evidence | Status |
|---|---|---|---|
| **A1** | ✅ **FIXED** — ensemble restored in ch33–35 (Wulin 2.26/2.04/3.01, Gu Yue 0.68/1.39) from seven characters to three.** Wang Jinxi, Zhang Yangzi and Wei Xiaofeng have **0 mentions for 10 consecutive chapters** (ch26–35). Gu Yue has 0 in ch33–35. Wulin has 0 in ch34–35. | `audit.py` §9 presence table | **OPEN — blocks writing** |
| **A2** | ~~Chapters 33–35 are not canon-backed.~~ **Canon ch 99–135 supplied by the user, 27 Aug.** ch 33 and ch 34 verified correct against source. **ch 35, 36 and 37 still carry headers asserting canon 133+ was unreadable and that they adapt no canon event — those statements are now false and the headers must be rewritten.** | canon_132–135.txt | **PARTIALLY CLOSED — ch 33/34 verified; ch 35–37 headers must be corrected** |
| **A3** | ✅ **FIXED** — ch33 Part 2 and ch35 Part 2; the ch14 "he told me everything" thread (C1) picked up and named Densities: ch32 6.66 → ch33 0.36 → ch34 0.00 → ch35 0.00. This is the spine of the story. | `audit.py` §9 | **OPEN** |
| **A4** | **No new chapter may be written until canon for that era is verified.** New standing rule. | THE_CODEX.md | **RULE LOCKED** |

## B. CANON FACTS I GOT WRONG OR NEVER APPLIED

| # | Problem | Evidence | Status |
|---|---|---|---|
| **B1** | ~~I flip-flopped on ring colour twice without a source.~~ **CLOSED and independently confirmed by canon ch 184:** Wulin's ring turns **purple at the thousand-year level** (*"Despite Tang Wulin only having one ring right now, it was a purple ring!"*). The v2.50 rule — colour reflects the soul's **current** age tier — is correct, and is on the page in ch 15 and ch 32. The lesson stands: I twice changed a rule without checking either time. | ch15, ch32; canon_184 | ✅ **CLOSED** |
| **B2** | ✅ **CLOSED — my log was wrong (5th such error).** ~~I never applied the canon growth mechanic to the RINGS.~~ **Ch 31 contains the entire canon ch 130 mechanic, in Wu Zhangkong's mouth, verbatim in substance:** one-tenth of the beast's years, spread evenly among the rings, five percent each on two rings, evolving at a thousand. Lin Hao then does the arithmetic on himself — **862 → 885 = 23 years, where the rule predicts 5** — and concludes the platform is *not* what is ageing the hawk. The mechanic is not only present, it is the engine of a mystery. Hawk chain verified monotonic: 700 → 862 → 906 → 912 → 918 → 926 → 934 → 942 → 950. | ch31 prose; canon_130 | ✅ **CLOSED** |
| **B3** | ✅ **CLOSED as a non-issue.** ~~Lightning has its own ring colour (Purple Gold).~~ **Verified 27 Aug: the phrase "purple gold" appears NOWHERE in canon ch 23–135.** The claim came from a wiki, not from the text — exactly the sourcing error this project keeps making. And our fic never claimed a lightning ring colour in the first place: ch 30/34 treat the lightning as living in the sword and then in him. There is nothing to fix and nothing was ever wrong. **Rule: a wiki is not canon. If it is not in the chapter text, it does not enter the story.** | grep of all 108 canon chapters: 0 hits | ✅ **CLOSED** |
| **B4** | **ch30 quoted canon's "nine-years-old" verbatim** while the AU has them at ten. | Fixed | **FIXED (adapted + recorded)** |
| **B5** | The **Shrek lock was mis-scoped** — it banned naming Shrek at all, but canon has the boys discussing Shrek Academy as a goal (our ch1 legitimately does). The real lock is Wu Zhangkong's origin. | Fixed | **FIXED (re-scoped)** |
| **B6** | ~~Canon ch 133+ has never been read.~~ **CLOSED 27 Aug.** Three user-supplied PDFs now give canon ch **23–135**. Total held: **ch 1–135**, missing only 28, 47, 102, 108, 115 (absent from the PDFs themselves). | `canon_extract/chapters/` | **CLOSED** |
| **B7** | ~~Our "Cen Yue" is a woman and an enrollment clerk (ch 4).~~ **CLOSED 27 Aug.** Ch 4 rebuilt: the enrollment scene now belongs to **Liu Yuxin** (canon ch 33–34) — first grader, class one of the advanced academy, black hair, red phoenix eyes. **Cen Yue appears 0 times in the prose.** The correction is documented in the chapter header. | ch04 rebuilt; `Cen Yue in prose: 0` | ✅ **CLOSED** |
| **B8** | ~~Mu Xi's defining trait is inverted.~~ **CLOSED 27 Aug — ch 5 and ch 6 both rebuilt.** Ch 5 rebuilt against verbatim canon ch 42 and 57: golden ponytail (not "silver-bright eyes"), *"not suitable for girls"*, began at **five**, two years of persistence, **first-rank at eleven**, second rank after thirteen, went **stocky**, **resents the word prodigy**, aiming at ninth-rank **Divine Craftsman** (only three on the continent). **Ch 6 still needs the same treatment.** | ch05 + ch06 rebuilt | ✅ **CLOSED** |
| **B9** | ✅ **CLOSED 27 Aug.** ~~The 243 kg fist is provably too low.~~ Canon ch 26 puts nine-year-old Wulin at **483 kg (left) / 543 kg (right)**. Our ch 32 measures the older, rank-30 Lin Hao at 243 kg. | canon_026.txt; audit.py | **OPEN — was already flagged, now settled by canon** |

## C. DROPPED THREADS — promises made in the text and never paid

| # | Thread | Where promised | Last touched | Status |
|---|---|---|---|---|
| **C1** | Wulin and Lin Hao share "the file" about the scales/gold | ✅ **TRACKER WAS WRONG (measured 27 Aug): 12 chapters, last mention ch 35 — not dropped.** | ch 7, 14, …35 | ✅ **ALIVE — no action** |
| **C2** | Gu Yue's "blank page" thread | ✅ **PAID — ch35 Part 7** ("she is not the blank page. I was") | ch23 → ch35 | ✅ **CLOSED** |
| **C3** | **Gu Yue × Lin Hao development** | Measured: **29 chapters, last ch 37** — the most consistently present relationship in the book. Tracker said "STALLED"; that is not what the data shows. | ch23 → ch37 | ✅ **ALIVE — no action** |
| **C4** | ✅ **ADVANCED AND CANON-GROUNDED 27 Aug.** The Spirit Pagoda's card is no longer static: **canon ch 168** establishes that *"it would be troublesome to draw more attention to yourself when you evolve your spirit soul to the thousand-year level"* — so the card (**C4**) and the locked crossing (**E6**) are the same problem arriving from two directions. Ch 37 now has Wu Zhangkong name the man with the card outright and explain the strategy: **concealment by crowd** — Heaven Dou City, more geniuses, no dominant clan, *"a talent shines for a moment and then it is somebody else's turn."* The card's contents stay unrevealed, deliberately. | ch24, 29, 31, 37; canon_168 | ✅ **ADVANCED — thread live and deadline-set** |
| **C5** | Na'er / the search for her | ✅ **REVIVED — ch33** (the hand, "Mine does it when I sleep") and **ch35 Part 6** ("I want to be the one who finds you") | ch29, 31, 33, 35 | ✅ **CLOSED (revived)** |
| **C6** | Lin Hao asking to be told things | ✅ **REVIVED — ch35 Part 6** ("I'd like to be told things too" / "I want an hour") | ch31 → ch35 | ✅ **CLOSED (revived)** |
| **C7** | The variants / what the adaptation is doing to him | ✅ **REVIVED — ch35 Part 6**, plus Gu Yue's verdict ("the second variant before breakfast") | ch28, 31, 35 | ✅ **CLOSED (revived)** |
| **C8** | **Xie Xie's Glorybound decision** — six Saturdays at the bench, the letter | ✅ **CLOSED 27 Aug in ch 37** (tracker still said UNRESOLVED): withdrawn, pilot track chosen, the hinge, his father's pride, Wu Zhangkong writing to the track himself. Measured: 11 chapters, last ch 37. | ch28 → ch37 | ✅ **CLOSED** |
| **C9** | **Xie Xie's secret list** ("you are on it eleven times") | Measured: 11 chapters, **last ch 37** — alive and current, not static as the tracker implied. | ch32 → ch37 | ✅ **ALIVE — no action** |
| **C10** | **The Unnamed Stroke / the hawk's stopped waiting** | ch35 | ch35 | alive |

## E. POWER, BODY AND APPEARANCE (user corrections, 27 Aug 2026)

| # | Problem | Evidence | Status |
|---|---|---|---|
| **E1** | ~~The "rank 30 wall" framing.~~ **CLOSED** — codex WALL CORRECTION plus stated on-page in ch 3, 18 and 35: *"You are not stuck at thirty. You are **coiled**."* A bottleneck gates only the rank and the next ring; soul power, spiritual power, body and the hawk all keep rising. | ch3, 18, 35 | ✅ **CLOSED** |
| **E2** | ~~I never applied the canon ring-age benefits.~~ **CLOSED — measured 27 Aug:** the ring-age benefit set (strength, speed, soul power, reaction speed, bodily tenacity) is on the page in **ch 5, 12, 15, 18 and 25**. Logged as missing without checking. | ch5, 12, 15, 18, 25; canon_131 | ✅ **CLOSED** |
| **E3** | ~~His body carries ~1,800 years of soul ring and I wrote him as an ordinary strong ten-year-old.~~ **CLOSED** — the measurement was recalibrated to canon: **fist 470 → 612 kg** (ch 21/32), clearing Wang Jinxi's canon 468 and sitting correctly below Wulin's 1,348 and his 3,998 Golden Dragon Claw (ch 115). | ch21, ch32; canon_114/115 | ✅ **CLOSED** |
| **E4** | ✅ **FIXED** — appearance/mutation line written back into ch8–35; longest gap now 2 chapters. `audit.py` §11 enforces it Mutations are unwritten for **16 consecutive chapters** (nothing since ch7). The codex plans permanent feather-marks, eyes perceiving spiritual-energy tracks and bone densification — **none of it was ever written.** This is forgetting, not nerfing. | `audit.py` §11 | **OPEN — `audit.py` now fails on it** |
| **E5** | ✅ **FIXED** — longest comment gap now 1 chapter ch1–4 had 7,7,8 mentions; ch22–35 have essentially none. | `audit.py` §11 | **OPEN — `audit.py` now fails on it** |
| **E6** | **I treated the third ring as a mechanical note.** At the 1,000-year crossing the rings turn purple, a third is bestowed, a 1,000-year soul spirit bestows up to three rings, the rank unlocks and the mutations escalate. **That is one of the largest events of his life and must be a full chapter**, not a line in a footer. | canon tier table | **RULE LOCKED** |

## F. CANON ACCESS — and my repeated failure

| # | Problem | Status |
|---|---|---|
| **F1** | **I fabricated `routify-file-proxy...` URLs and fetched them, ~8 times.** Every one failed with `SignatureDoesNotMatch`. Those URLs were invented by me. This is the "assert without verifying" failure the user has corrected repeatedly, and I repeated it in a single session. | **RULE LOCKED — see `CANON_ACCESS.md`: never construct a proxy URL. Only use a URL that came back from `web_search` or from a page already fetched. If I have no real link, say so.** |
| **F2** | ~~Canon ch 133+ has never been read in full.~~ **CLOSED 27 Aug — the user supplied the full text as a PDF.** Ch 133, 134 and 135 are now verified verbatim. | **CLOSED** |
| **F5** | ✅ **RESOLVED 27 Aug — the user supplied `uploads/soul land 3 novel .pdf`.** Canon ch **23–51** extracted (27 chapters, 37,049 words) to `/home/user/canon_extract/chapters/`. Canon **28 and 47 are missing from the PDF itself.** Remaining unread: **52–122 and 133+**. | **CLOSED for 23–51** |
| **F3** | **Numbering differs between sites.** Wuxiaworld 132 = "Summary", 133 = "Before the Final Exam"; Webnovel 133 = "Summary", 134 = "Before the Final Exam". | **RECORDED — always check the title, never the number** |
| **F4** | ✅ **CLOSED 27 Aug.** ~~Canon divergence:~~ canon ch 133 has Wu Zhangkong rebuke **Wulin** — *"Their sacrifices, were all because of you."* **In our AU Lin Hao was present for the wolf pack**, so that rebuke cannot land the same way. **The canon sentence is now verified verbatim, so this is a precise edit against known text rather than a guess.** | ✅ **CLOSED — the rebuke is now written into ch 33, re-derived: Lin Hao was the fourth in the wolf pack, so Wu Zhangkong turns the same question on him, and the chapter's lesson becomes "a reading is not a warning."** |

**Verified working sources and the full list of what I actually have are in `CANON_ACCESS.md`.**

## G. CANON ch 8–22 AUDIT (user-pasted canon, 27 Aug 2026)

| # | Problem | Status |
|---|---|---|
| **G1** | **Our ch2 described Mang Tian with "blue hair and blue eyes… a beast-type martial soul."** Canon ch 22: his martial soul is the **Earth Hammer — a TOOL soul** — and he is a **Soul Ancestor with four rings**. | ✅ **FIXED** — ch2 rewritten to canon |
| **G2** | ~~Mang Tian's rank never established.~~ **CLOSED 27 Aug in ch 2** — Wulin sees the four rings rise (one white, two yellow, one purple: ten-year rabbit, hundred-year hammers, thousand-year brown bear), hears **Tenacity** named, and learns the man shouting at him is a **40th-rank Soul Ancestor**. | ✅ **CLOSED** |
| **G3** | ~~Spirit-soul price ladder never used.~~ **CLOSED 27 Aug in ch 2** — a full scene at the three-layer Glorybound branch: **70,000** for a ten-year white, **1,000,000** for a hundred-year yellow, **30,000** for the draw, against a **1,000-coin monthly stipend**. Wulin does the arithmetic aloud: *"a white one is seventy months."* | ✅ **CLOSED** |
| **G4** | ✅ **CLOSED 27 Aug — canon ch 190 supplies the whole geography.** ~~Sun-Moon Federation mentioned once; Shrek City never mentioned.~~ Now verified: **eighteen first-class cities in five regions**; the **centre region has only Heaven Dou City and Shrek City**; the **east has five coastal first-class cities forming the Skysea Alliance, with Eastsea City ranked second**; a **Skysea Alliance Tournament every three years** and a **federation-wide tournament every five years in Shrek City**. Also: **Wulin's Golden Dragon Claw = 3,998 kg** (ch 115, machine destroyed), which confirms our 612 kg sits correctly below his 1,348. | canon_190, canon_115 | ✅ **CLOSED — worldbuilding facts recorded in `CANON_ACCESS.md`; **woven into ch 4 (the pamphlet on the train) and ch 37 (the three-year horizon)** |
| **G5** | Na'er's canon facts verified correct — no martial soul at all, the seven-coloured ring at night fusing between her eyes. | canon ch 12 | ✅ **CLOSED — no action** |

## H. CANON ch 23–51 AUDIT (user-supplied PDF, 27 Aug 2026) — six new problems

| # | Problem | Evidence | Status |
|---|---|---|---|
| **H2** | ~~Cen Yue gender-swapped and re-cast~~ (see B7). | ch04 rebuilt | ✅ **CLOSED** |
| **H3** | ✅ **CLOSED 27 Aug.** ~~Liu Yuxin is nearly unused.~~ **PARTIALLY CLOSED 27 Aug** — she now carries the whole enrollment scene in ch 4 (6 prose mentions) and the soul-camera thread is explicitly opened in the footer. Still owed: the **soul camera** itself (canon ch 46/57) and her report that Wu Zhangkong has at least six rings. | ch04 enrollment + **ch07 soul camera** | ✅ **CLOSED — she now carries the enrollment, the recommendation, the metal placard, AND canon ch 46/57's soul camera, which is how the class learns Wu Zhangkong has **six rings / a Soul Emperor**. |
| **H4** | ✅ **CLOSED 27 Aug.** ~~Li Chushui never appears.~~ **OPENED, then completed** — she is now in class five in ch 7, positioned two desks up, with the detail that she reminds Wulin uncomfortably of somebody. Her cat martial soul (half her hair turns white, one eye green) is still owed. | ch07 rebuilt | ✅ **CLOSED — the full canon ch 51 transformation is on the page: half her light-blue hair turns white, one blue eye goes green, a white ring, a white cat on her shoulder, white fur on her palms, claws from her fingertips, eleven metres in the time Chen Long lifts a ladle.** |
| **H5** | ~~Mu Xi inverted~~ (see B8). | ch05 + ch06 rebuilt | ✅ **CLOSED** |
| **H6** | ~~243 kg fist contradicted by canon~~ (see B9). | canon_026 + ch32 rebuilt | ✅ **CLOSED** |

### ✅ Confirmed CORRECT by this canon (do not "fix" these)
- **The blacksmith rank ladder we use matches canon exactly** — rank 1–2 Master, **3–4 Grandmaster** (so
  Lin Hao as a "3rd-rank Grandmaster" is right), 5–6 Master Craftsman, 7–8 Saint Craftsman, 9 Divine.
- **Mu Chen as an eight-star Saint Craftsman and Association President** — matches.
- **The Shrek lock is correctly scoped** — canon ch 46 has Liu Yuxin say only that Wu Zhangkong "was a
  teacher at the advanced academy previously, but for some reason he was sent to the intermediate academy."
  Canon does not name Shrek here either.
- **Heavy Silver, Thousand Refinement / Hundred Refinement, Harmonizing** — all used consistently with canon.
- **The Mang Tian contradiction is genuinely fixed** — `grep "blue hair and blue eyes"` returns 0 across all
  37 chapters, and ch 2 now reads "his martial soul was a hammer."

## I. CANON ch 52–99 AUDIT (user-supplied PDF, 27 Aug 2026) — what this stretch of canon demands

| # | Problem | Evidence | Status |
|---|---|---|---|
| **I1** | ~~"One Sword Cleaves All Techniques" is canon's named sword realm and our fic has never used it.~~ **CLOSED 27 Aug in ch 9.** Wu Zhangkong takes down a plain ash wooden sword, suppresses Xie Xie in eleven seconds **without releasing his martial soul or using a soul skill**, and names the realm: *"whatever comes at me — whatever it is, whoever is holding it — I answer with the same thing. One sword."* Lin Hao's existing sword-intent coaching is now anchored to canon instead of only to my invention. | ch09 rebuilt; grep = 1 | ✅ **CLOSED** |
| **I2** | ✅ **CLOSED — and my claim was wrong.** ~~Spirit Connection as the ring-count gate is unused.~~ **Measured 27 Aug: the full ladder is in ch 3's prose** (Spirit Origin → Connection → Sea → Abyss → Domain → Divine Origin, with each realm's spirit-soul capacity), and the capacity rule recurs in ch 2, 11, 12, 15, 16, 21, 24, 32. I had logged it as unused without checking. Canon: above 100 spiritual power = Spirit Connection, and only then can a body *"bear the load of two yellow spirit souls or one purple spirit soul."* Our ring law and the locked third-ring event should be expressed in these terms. | canon_069; grep = 0 | **OPEN** |
| **I3** | ✅ **CLOSED 27 Aug.** ~~The comparison has never been made on the page.~~ Canon ch 69: Xie Xie 29, Wulin 44, Gu Yue 119. Lin Hao is at 120 — level with Gu Yue, triple the boys. That is a story-relevant fact and nobody in the story has ever said it. | ch32 prose now carries canon ch 114's full punch table | ✅ **CLOSED — all ten canon values (61/69 · 115/143 · 153/164 · 423/468 · ceiling 5,000) are in the prose, and Lin Hao's 612 sits correctly between Wang Jinxi and Wulin.** |
| **I4** | ✅ **CLOSED 27 Aug.** ~~Gu Yue's Elementalist is canonically a *spiritual-type* martial soul~~, one of the rarest and most sought-after kinds because it pairs with mechas. Our fic uses "Elementalist" but never this classification, which is what makes her valuable beyond raw power. | canon_069; grep = 0 | **OPEN** |
| **I5** | ~~"Stacked Hammers" is unused.~~ **CLOSED 27 Aug in ch 10.** Wulin finds his effect by hitting flat on purpose (three shocks instead of one); **Lin Hao identifies it and names it for him** — and then finds his own, quieter one, which he does *not* name but writes in the ledger's column for things the metal has done that he cannot yet explain. | ch10 rebuilt; grep = 2 | ✅ **CLOSED** |
| **I6** | ~~The canon teacher-vs-blacksmith conflict is unused.~~ **CLOSED 27 Aug in ch 9.** "The clumsy bird flies early into the forest" and "what a farce" are delivered to **both** boys. Wulin stays silent (in character). **Lin Hao argues back** — *"You can't tell a boy to make his own weapon and then be surprised when he wants to know how it's made. That isn't a distraction, Teacher. That's the same instruction."* — and Wu Zhangkong concedes the point, which sets up the swordsman/blacksmith tension as a live argument rather than a fact. | ch09 rebuilt | ✅ **CLOSED** |
| **I7** | ~~Mu Xi's backstory is not applied~~ (see B8/H5). **CLOSED 27 Aug in ch 5** — the whole backstory is now a scene, told from her own point of view. Ch 6 still to come. | ch05 + ch06 rebuilt | ✅ **CLOSED** |
| **I8** | ✅ **CLOSED 27 Aug.** ~~Gu Yue's canon entrance is unused.~~ Ch 8 already had the six-element fight (Part 4, "Six Things at Once") but **not the arrival** — I checked keywords and wrongly concluded the whole entrance was missing, then wrote a duplicate fight and had to cut it. Final state: canon's arrival is ch 8 Part 1 (white clothes, no uniform, registration closed, the recommendation letter, *"I can take a test"*), and the existing fight follows. | ch08 rebuilt; parts 1–6 in order | ✅ **CLOSED** |
| **I9** | ~~The trio dynamic is never stated.~~ **CLOSED 27 Aug.** Ch 10 already had Xie Xie losing four of four to Gu Yue (canon's "never beaten her one-on-one"). Now the *shape* is stated too: fire and water, no incident, and **Wulin as the hinge** — *"You're not keeping the peace. You're making the fight impossible. Different thing. Much better."* | ch10 rebuilt | ✅ **CLOSED** |

### ✅ Confirmed CORRECT by ch 52–99 (do not "fix" these)
- **The Skyfrost Sword and its exact rings** (Y, Y, P, P, **black, black** — two ten-thousand-year rings) — our fic reproduces canon verbatim.
- **Guang Biao's six rings and three spirit souls**, Long Hengxu's *"step over my dead body"*, and the
  *"You're from that place" / "I was expelled from there because of my temper"* exchange — all correct.
- **Gu Yue's martial soul is the Elementalist and her first skill is Elemental Tide** — correct.
- **Lin Hao at Spirit Connection 120** is canonically well-placed against Gu Yue's 119.
- **The Shrek lock is correctly scoped a third time** — canon ch 57 names Shrek Academy as the origin of Wu
  Zhangkong's meditation method, while ch 85 still leaves his own origin unnamed ("that place").

## J. CANON ch 99–135 AUDIT (user-supplied PDF, 27 Aug 2026)

| # | Problem | Evidence | Status |
|---|---|---|---|
| **J1** | ✅ **CLOSED 27 Aug.** ~~Lin Hao's spiritual power of 318 is more than double canon's benchmark.~~ Canon ch 114 measures **Gu Yue at 153** and states *"I don't think there is a single Soul Master on the entire continent that is this young yet has such high level spiritual power!"* Gu Yue is canon's spiritual prodigy and the one predicted to reach Spirit Sea. Our own codex says his speciality is **not** spiritual power. **318 outranks the character canon names the best on the continent for her age.** | `state.py` → **145**, monotonic 118→145, always below Gu Yue's 153→186 | ✅ **CLOSED — the whole 37-chapter curve was rebuilt, ch 21's reveal inverted so Gu Yue keeps the top step, and the SPIRIT/PANEL guards retargeted to the new values.** |
| **J2** | ✅ **CLOSED 27 Aug.** ~~The 243 kg fist is now disproven by a full table.~~ Canon ch 114: Zhang Yangzi 61/69 · Gu Yue 115/143 · Xie Xie 153/164 · **Wang Jinxi 423/468** · Wulin 1,156/1,348 · scaled 2,700. Lin Hao at rank 30 carrying ~1,800 years of soul ring measures **below Wang Jinxi at rank 23**. | canon_114; ch32; PANEL guard | ✅ **CLOSED — 186→243 became 470→612 kg, clearing Wang Jinxi's canon 468 and sitting below Wulin's 1,348.** |
| **J3** | ✅ **CLOSED 27 Aug.** ~~The ch 35/36/37 headers are factually false.~~ Each states canon ch 133+ was unreadable and that the chapter adapts no canon event. Canon 133–135 is in hand and covers exactly that era: the rebuke, Mu Chen's perfect-foundation teaching, the rebellion platform, the secondary-occupation choice. | ch 33/35/36/37 headers rewritten; canon 132–135 now adapted in ch 33 and hooked in ch 37 | ✅ **CLOSED** |
| **J4** | ✅ **CLOSED 27 Aug.** ~~"Wulin is the youngest in Association records" is imprecise.~~ The **prose was already correct** ("youngest second-rank") — the imprecision was in ch 5/34 footers and THE_CODEX. All now read *"youngest **second-rank** in the Eastsea Branch (canon ch 58: the president was youngest first-rank at eight)"*. | 3 files fixed | ✅ **CLOSED** |

### ✅ Confirmed CORRECT by ch 99–135 (do not "fix" these)
- **Zhang Yangzi's martial soul is the Shadow Phantasm Eagle** and his fusion skill with Wang Jinxi is the
  **Shadow Eagle Dragon** — our fic has both exactly right.
- **Class zero's membership and Wu Zhangkong as teacher-in-charge** — matches our ch 19.
- **The Skyfrost Sword, six rings, one ten-thousand-year** — consistent with our ch 15/33.
- **The Shrek lock is correctly scoped a fourth time** — President Yu Zhen names Shrek Academy openly in ch 109
  while Wu Zhangkong's own origin stays unnamed.
- **Gu Yue's haughty distance from the group and Wulin as mediator** — our ensemble framing matches canon ch 135.

### 🎁 NEW CANON TOOLS now available (not problems — unused assets)
- **The complete spiritual-power ladder** with each realm's spirit-soul capacity — this is how every ring
  decision in the story should be justified from now on.
- **The rebellion spirit ascension platform** and its **100-second stealing rule** — a ready-made high-stakes
  arena where other Soul Masters are as dangerous as the beasts.
- **The secondary-occupation deadline ("within three years")** and Wu Zhangkong's **"god altar"** goal — a
  ticking clock that belongs to Lin Hao's blacksmith line by canon's own words.
- **The perfect-foundation doctrine** — *"the less strikes it received, the greater the effects of the Thousand
  Refinements"* — which is the same idea as Lin Hao's READING THE GRAIN, and canon says it makes third-rank
  work **10% faster**.
- **Wu Zhangkong's rebuke**, verbatim, ready to be re-derived for our AU.

## D. STRUCTURAL / METHOD

| # | Problem | Status |
|---|---|---|
| **D1** | **The recurring cause: when a correction arrives I make it the centre of every following chapter and drop everything else.** Named by the user three times. Growth correction → story about numbers. Swordsmanship → story about Wu Zhangkong. Lightning → story about the hawk. | **RULE LOCKED in THE_CODEX.md (ENSEMBLE LAW) + `audit.py` §9 enforces it** |
| **D2** | Chapter Summary footers are for my state derivation, not for the user. Keep them short. | **NOTED** |
| **D3** | My checks keep producing false positives (35 in the audit alone; 11 before that). Every new check must be verified against known-good passages. | **RULE LOCKED** |
| **D4** | ~~The audit's canon-citation check warns on ch1–20 because those headers say "Novel Chapter N" not "canon ch N".~~ **CLOSED 27 Aug** — all 37 headers normalised to `Canon Reference: canon ch N` (37 files touched across two passes); `grep -l "Canon Reference: Novel"` returns nothing. | verified by grep | ✅ **CLOSED** |

---

## WHAT I AM NOT GOING TO DO

**I am not going to write chapter 36.** A4 and B6 block it: I have no verified canon for the current
era, and the ensemble has collapsed. Writing now would add to the problem.

## THE ORDER OF WORK

1. **J1** — resolve the spiritual-power calibration. 318 against Gu Yue's canon 153 is the largest single
   inconsistency in the project, and it contradicts our own codex about what his speciality is.
2. **J2** — re-derive his measured strength against canon's full class-zero table.
3. **J3** — rewrite the ch 35/36/37 headers. They currently assert something false about canon.
4. **I1** — anchor the SWORDSMAN LAW to canon's **"One Sword Cleaves All Techniques."**
5. **H1** — decide what happened to Zhou Zhangxi and Yun Xiao.
6. **B7 / H2** — fix Cen Yue.
7. **I2 / I3** — express the ring gate in canon's ladder terms and put the spiritual-power comparison on the page.
8. **F4** — re-derive Wu Zhangkong's rebuke for our AU, now against the verified sentence.
9. **J4 / I5–I9 / H3–H6** — the remaining smaller items.

**Note on ordering:** E1–E3 come before the rewrite, because rewriting chapters around a power level
that is itself wrong would just have to be done twice.

## STATUS

**`run_all.sh` now returns exit 0 — all four layers pass** (state · verify · verify2 · audit ·
verify_ensemble).

**🔴 NEW — F1: THE PURPLE-RING SKILL EVOLUTION IS UNWRITTEN (found 2026-08-28, user correction)**

Canon, verbatim: *"if his spirit soul was upgraded, then the soul skills it provided would be upgraded
too."* In **ch40** both of Lin Hao's rings re-formed **purple** (hawk 964 + 200/ring = 1,164) and a third
ring was bestowed. Therefore **Gale Talon and Hawk-Soul Union both upgraded to thousand-year tier at
ch40** — and I wrote the rings changing colour, then kept writing both skills exactly as they were.
**Twenty-one chapters (ch40–ch61) have used yellow-tier skills on purple-tier rings.**

Owed scene, requirements in `THE_CODEX.md` §THE ADVANTAGE LEDGER §2: shown not reported · perfect
compatibility is the reason · witnessed (someone says aloud what a thousand-year soul skill is, as canon's
witnesses do) · costed · Union likewise, trump card and cost both bigger.

`checks/verify_ensemble.py` §7c **WARNs every run until this is written**, and **FAILs** if either skill is
ever described at hundred-year/yellow tier from ch40 onward.

**🔴 NEW — F2: THE ADVANTAGE LEDGER WAS NEVER ASSEMBLED (found 2026-08-28, user correction)**

Fifteen separate advantages were each recorded somewhere and none of them were ever put in one place, so
he kept getting written at baseline. Now consolidated in `THE_CODEX.md` §THE ADVANTAGE LEDGER §5,
including two corrections: his **three purple rings are perfectly compatible and so exceed normal purple**,
and his **martial soul, classified peak high-level, performs as a TOP-LEVEL martial soul in his hands**.
Standing instruction recorded there: *when writing Lin Hao, imagine what he is — nothing about him is
written at baseline.*

**STILL OPEN (do not close these until verified):**
- ✅ **F1 CLOSED (ch40, 2026-08-28)** — the soul-skill evolution is now on-page in the chapter where the
  rings actually turn purple. Gale Talon is shown becoming a thousand-year soul skill (same strike, thirty-
  metre deadfall, triple cost, not chosen), Gu Yue frames it (*"your skill didn't improve, it got older"*),
  the Spirit Pagoda witness dates it against Wu Zhangkong's own, and Hawk-Soul Union is felt larger but
  stays reserved per decision **D006**.
- **F2 — the advantage ledger** must be applied on-page, not just recorded.
- **A2 / B6 — canon ch 133+ has never been read.** Chapters 33–35 are still QUARANTINED against canon.
  They were rebuilt for ensemble, appearance and power framing, but **not** verified against source.
- **B2 — ring-age benefits** stated on-page (ch35) and **applied in ch36** (the strength is the ring age showing; Mu Chen states the reason). **Considered closed pending canon verification.**
- ✅ **E3 CLOSED (ch36)** — the child plate's ceiling is confirmed on-page and the true figure is
  established as **past the marks on the dial**, deliberately given no number so canon cannot contradict it.
- ✅ **E6 CLOSED (ch40)** — the third ring was bestowed on-page: *"Both rings re-form purple. A third ring
  is bestowed."* Hawk 1,164 at the crossing.
- **C8 — Xie Xie's Glorybound decision** is still unresolved (six Saturdays, the letter).
- **Canon ch 28** is absent from the source PDFs.

