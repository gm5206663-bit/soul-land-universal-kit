# Chapter 6 audit — *Thirty Thousand*

> **Post-ship audit (2026-10-02).** Sources: `chapters/Chapter_06_Thirty_Thousand.md`; `canon_coverage/Canon_Coverage_Chapter_06.md`; canon fetched live the same day (`legend-of-the-dragon-king/ldk-chapter-16…19`, chunk 0 each; ch20–22 fetched and held for ch7); the ledgers as committed with this chapter.

## 1 · Fidelity (canon beat by beat — sampled against the fetched text)

| # | Canon (ch) | On our page | Verdict |
|---|---|---|---|
| 1 | ch16: the beach's answer; *"nearly up to my nose"*; the dimming light; the impatient morning; the family walk; the Pagoda; *"Do you have enough money?"*; **73 whites @70,000 · 11 yellows @1,000,000 · the draw @30,000**; *"Aren't spirit souls thirty thousand coins?"* | §One (beach); §Two (walk, hall, counter, wall, the cliffhanger as the counter's next beat) | PASS |
| 2 | ch17: the draw's terms; the unsuitable risk; the advised ten-year; the father's offer; Wulin's refusal (*"my martial soul is only Bluesilver Grass"*); the fee waived; the record's purpose; **the six realms**; *"A strong spirit soul demands spiritual power equal to it"*; *"Do not fight the machine."* | §Two, complete and in order | PASS |
| 3 | ch18: the machine; the golden world glimpsed (canon-own; unseen); **SP 38**; *"best … of all the Soul Scholars I've had these past few years"*; the bands 1–50 with ≤15/15–30/30–45/45–50; the verdict *advanced*; the record for the academy; the whites' draw → the **pure white ball** | §Two, complete; the bands rendered with 38 in the advanced band (canon's own page slip noted in the coverage) | PASS |
| 4 | ch19: the **Grass Snake** (10 cm, earthen yellow, diamond scales); the deflation; the manufactured defect; **the hundredth slot of a constant hundred**; **24 hours or it dies**; *"Half the boys who draw one of these leave it."*; the walk home; the three years of un-cried tears; the tears on the ball; **Na'er** — *"Big brother," Na'er said, "big brother, don't cry."* | §Two's close, complete | PASS |
| 5 | The private pillars: Tang Ziran's worry; Lang Yue's absence in this block; the parents' arithmetic; the household's meat line | carried as canon carries them (compressed to the father's face and the day's money; no new claim) | PASS |
| 6 | Order preserved; nothing pulled early — **no fusion, no rank 11, no Mang Tian reveal** (ch20–22 held for ch7); the 24-hour clock left running at the chapter's edge | whole chapter | PASS |

## 2 · Register numbers (measure tool, after the final edit)

**11,275 w body · ALL avg 9.5 / med 8 / 0 over 60 · NARR 9.9 / 9 / 0 · dialogue paras 122 · CJK 0 · "the way" 2 (cap).** No meta-narration; no fused name; no percent-speak; no stat-speak (the one printed number in his own line is **ten**, the scene's own measurement; the 38 is canon's own, printed by canon's own scene). Caps met before commit (drill step 3; H8's law).

## 3 · Seals

LSP-10 (no gold on the soul; the golden world is canon's own trace, unseen — WUL-01/04) · R13/DRG-01 (no resonance beat, no bloodline knowledge) · NAE-02 (Na'er exactly as canon shows her at ch19; no name, no theory, no witness beyond canon's own) · R5 (the Talent never named) · **Q-2** (no spiritual-power print in Su Yan's line; the 38 belongs to canon's scene) · no spirit-soul purchase by the OC · **no futures spent** (no ring, no soul, no platform). **All PASS.**

## 4 · Parity (R14.1) at measurement contexts

- **Canon's measurements:** Wulin's SP 38 and his band verdict — carried as canon carries them; the price wall's 70,000 / 1,000,000 / 30,000 — canon's numbers, quoted whole; the defective's slot — canon's hundredth.
- **Our measurement contexts:** the spring tests → **ten** printed by the school's own apparatus in its own scene (second movement of his public record, after ch5's nine); the tin's arithmetic → **three hundred and eighty-two coppers** counted out loud at the table, then **five coins and eighty-one coppers** at the week's close (every figure printed in prose is the family's own money, in the family's own coin-count — *"A hundred coppers makes a coin in this town"*); the fee → **thirty coppers** from the tin, set aside in a twist of paper. **No approximation language anywhere.**

## 5 · Ledger consistency

`GROWTH_LOCKS` §6 (the ch6 line: public record moves nine → **ten**; the door priced; the tin's column moves) · `SU_YAN_STATUS` §2/§3/§4/§12/§15 refreshed from the page the same turn · `HOUSEHOLD_LEDGER` (the fee line; the night-job's two coins; the feed's copper) · spine §K · register rows 43–46 · `BUTTERFLY_LEDGER` ch6 (C-01 · C-02 · C-03 · C-06 landed; B-08/B-09 echoes) · `CANON_CHARACTER_STATE` (Wulin: SP 38; the white ten-year ball; the Grass Snake — the fusion window open, unresolved) · `SERIAL_LOG` LOG 029. **Cross-check: the chapter's tin arithmetic closes exactly (382 + 200 − 1 = 581 coppers; stated as 5 coins 81 coppers).**

## 6 · In-house catches (all fixed before commit)

- **The fragment class — killed at the root.** The first assembly pass (the naive clause-splitter) produced two malformed sentence families (36 bare-verb heads, plus a run of subordinate-clause orphans, on the dead-end build) — e.g. *"Was a thing she did…"*, *"That the man looked like…"*. The draft was **rebuilt on a safe splitter**: splits are allowed only where the right side is a well-formed clause (finite verb present, no subordinator lead), with subject recovery for verb-led continuations; then the longest sentences were rewritten by hand into short complete ones. Final scans: no fragment heads, no orphan clauses, no over-60 sentences.
- **Three quote-balance slips** introduced by the hand-rewrite pass (a cut quote on the master's record speech; a doubled quote in the *"When it rains"* beat; a duplicated tail in the mother's law of the sums page) — caught by an odd-quote-count scan and fixed; a duplicate-sentence scan returns zero.
- **"The way" cap** — 41 occurrences across the source parts cut to the cap of **2** (the mill line and the bowl line survive); verified by count on the final text.
- **Timeline/continuity passes before assembly:** the reckoning re-anchored to *"The reckoning was done the next afternoon. Market-day daylight, and the door open."* (it precedes the Spring test in scene order); the dockman's arrival re-anchored to *"the next morning"*; the pig's hold-read logic made explicit (*walks past the aft rows without reading them — "The pig only read what could still be saved."*); the sums-page close re-totalled to *"Left: five coins, eighty-one coppers."*
- **The supper-line tense slip** (*"He laughed about it, and gone back"*) — caught in the final read and rewritten to *"He had laughed about it. And he had gone back the next morning."*
- **The read-through pass (seven catches):** the office's machine sentence rebuilt (*"It had bought it every year"* → one clean clause); the clerk's *"Next"* line repaired; a dangling *"The spirit soul was actually —"* removed before the reveal; *"Look closely, very closely"* → *"Close up"*; the father's reckoning made arithmetically true (*"At a copper a walk, the wall is thirty thousand weeks"* → *"A coin a week would be thirty thousand weeks of this house"*); the mother's bought-soul figure set to the page's own number (*ninety thousand* → **seventy thousand**); and the office-machine *"quietly"* doubled by the first fix, then merged to one sentence. Word count 11,287 → **11,275**; every gate re-measured after the last edit.

## 7 · Verdict

**PASS.** Canon ch16–19 complete, in order, on the page; the week's OC line carries four costed movements (the fee from the tin · the father's errand at the counter · the reckoning and the new law · the paid night-job) with the first coins in the tin; butterflies paid per the ledger's ch6 priorities; every seal intact; nothing of ch20–22 pulled early. Ready for the author's read.

## 8. The R21 tests (the actor law)

**The actor test, per movement:** the tests day — he queues, signs, takes the machine's number, and his father says it aloud in the yard (his scene, his number). The counter — **Su Heng's** errand, his three questions, his pencil (the OC's side); the boy is present on the page of his own house's arithmetic. The reckoning — the tin is his to count, the law is his to accept, and *Then find it.* is said to him. The night-job — the fee named by him (*"What does the load stand to lose you… if it is wrong?"*), the hold walked with him at the hatch, the honest second coin refused and kept on the dockman's word. **No stretch is passive.**

**The reaction test:** the clerk (*"Su Heng's son. Sign here."*) · the soul master at the tests (*"Ten," … "Take the first breath you want…"*) · Teacher Lin (*"The machine has caught up with my pen… Do not make me look slow."*) · the girl by the window (*"I'm on the list over you now… I looked."*) · the fishwife (*"Ten, is it."*) · the ashen-robed master (the three-line errand; *"The ones who carry a strong soul run hotter… For yours, I would ask."*) · the dockman (the commission; the second coin; *"Bring the beast again."*) · the mother (*"You were counted," she said now. "Come in and eat."*) · the father (*"The harbor's money is not in coppers, boy."*). Behaviours change because he is there.

**The event count:** ≥2 value-changes per movement (the record moves; the tin moves; the trade's standing moves; the family's law changes); ≥1 real cost (the fee from the tin; the father's errand and the price written into his book; the night taken from the house's sleep; the mother's conditions accepted). **The failure-first rule holds from ch5's arc** — the trade's first failure was paid in v2; this chapter is the recovery movement, and its risk is on the page (*"The fifth row is the line"* — a wrong read here would cost the dockman three coins and a season of face).

**Six lines moved:** standing (public ten; on the intermediate list) · knowledge (the price wall; the draw's terms; the six realms' ladder) · resource (the tin: 382 → **581** coppers; the trade's first coin) · relationship (the dockman — a trade now with strangers' money; the fishwife; Teacher Lin; the girl's list) · promise (the reckoning with the door open; the page's *"The price list of the door"*) · position (the door at thirty thousand; *one rank short of nothing now*).

**Seals:** LSP-10 · R13/DRG-01 · NAE-02 · R5 · Q-2 · no futures — all re-checked in the final text. **Verdict: PASS.**
