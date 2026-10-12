# AUDIT — Chapters 1–3, read cold, front to back (foundations re-check)
### Done 2026-09-07 · at the user's request: "check the first chapters of the foundation fiction, understand all your mistakes and problems and missing things."
### Method applied: the project's own (METHOD.md full-play law, source-of-truth layers, knowledge firewall, canon audit, smallest-area repair). Each chapter read start-to-finish as continuous narrative, then repaired, then gates re-run (all green).

---

## SCOPE NOTE

Only **3 prose chapters exist** (chapters/chapter_01–03: 门 · 一班 · 铁衣). The "foundation opening" of this story is those three + the locked bible set. Chapters 4–5 are **design-ready but unwritten** (the seam lives in bible/CURRENT_STATE_PRE11.md). Everything below covers what exists; the most important *missing* finding targets chapter 4.

---

## A. ERRORS FOUND & FIXED (source-level, smallest area)

| # | Error class | Where | What was wrong | Fix |
|---|---|---|---|---|
| A1 | **Knowledge / identity leak (worst find)** | ch1, handshake beat | Narration called 霍雨浩 "a duke's bastard" from inside 言天宇's limited POV — asserting Yuhao's secret 白虎公爵 lineage the POV cannot know. The ch1 footer even claims "no invented canon specifics asserted." | Removed the lineage claim ("not a road-boy... not a charity case") + added a verify.sh gate so the token class can't return. |
| A2 | **POV breach (free indirect into Yuhao)** | ch1, same beat | "In eleven years, no one had offered *him* a hand quite like that" narrated Yuhao's private history/feeling. | Rewrote as 言天宇's own read: "言天宇 did not know the boy's eleven years. He did not need to..." — emotion kept, POV held. |
| A3 | **Continuity — form of address** | ch3 Part Five vs ch1 | 言天宇 calls 穆恩 "Teacher" in ch3 but "Grandteacher" throughout ch1 (canon: 言少哲 is 穆恩's 大弟子 → the boy is 徒孙; "Grandteacher" is right). | Unified ch3's four direct addresses to "Grandteacher." |
| A4 | **Setting continuity — dormitory drift** | ch3 Part Five | 言天宇 "did not go to his dormitory... a corridor of sleeping boys," but ch1/ch2 had him sleeping in the dean's house (his corner room since childhood). Silent setting change. | Established the move deliberately in ch2 Part One (言少哲's condition: "a student of 史莱克 sleeps where students sleep"; 蔡媚儿's three-times promise to eat). Recorded in CURRENT_STATE POST-ch2. ch1's final night at home remains the last night before the term. |
| A5 | **Missing canon classmate** | ch1–3 | 萧萧 is canonically in 一班 (twin braids, observant, keeps her second soul hidden at this era) yet never appears while 言天宇 "learns the room." | Light presence added: ch3 Part One (the fellow watcher who catches him watching), and the 铁衣 rally (she steps back onto the track with the others). No second-soul/王冬-crush secrets touched. |
| A6 | **Canon-order hazard (latent)** | ch1 market fish vs canon ep-6 fish venture | ch1 has Yuhao selling a fish for copper on his first night in the city; canon ep 6 is when his 烤鱼 *business* starts. If later chapters treat ep 6 as "his first fish," it contradicts ch1. | Guard note added in CANON_CLOCK seam + CURRENT_STATE seam: ch1 = one informal fish; ep 6 = the venture properly starting. |
| A7 | **Gate hygiene** | checks/verify.sh | The prose-hygiene gate didn't catch the leak class that actually occurred. | Added "duke's bastard/Duke's" tokens to the gate. (First attempt over-matched my own replacement text; corrected.) |

---

## B. PROBLEMS (not errors — real risks to manage, not all fixed now)

1. **Protagonist passivity is becoming structural.** Across three chapters 言天宇's strongest dramatic moments are *reactions* (he declines to run, he watches, he brings water). 周漪 and 穆恩 are the engines; he is the excellent pupil. That is the intended arc ("the watcher") — but three straight chapters of an extraordinary boy nobly holding back will stale. **Chapter 4 must give him an active thread with a real choice and stakes.**
2. **The complete-holder kit is all reputation, zero demonstration.** In 3 chapters the reader has never seen one of his named skills (燎羽 / 贯日), his 御光/御火, 敛焰步, or even his cooking on-page — 唐雅 keeps *saying* he cooks better than chefs; we never see it. This violates the user's standing criterion: *advantage effects visible in performance.* The one shown power — the light-wash that steadies 马小桃's 邪火 (ch1) — is the strongest proof the reader has that he is what the files say. **Chapter 4's market/food lane is the natural place to finally show 御火 + 厨艺 + a controlled first skill beat.**
3. **Repetition tics across a binge read** (watch, don't necessarily excise): "the cold at his spine stirred — a ripple/breathed it down with the habit of a decade"; "the warm, open smile that made people trust him"; the authorial "He did not know, yet, that..."; "It was not a question" (used for both 穆恩 and 周漪). Some are deliberate motif — keep the best, vary the rest.
4. **Telling his goodness through other characters' confirmation.** 周漪/唐雅/马小桃 repeatedly voice that he is special/real. At foundation length this works; going forward it must convert into *shown choices* (see #1).
5. **Overlapping "gate" metaphor** — the academy gate, 周漪's culling gate, and the third-ring wall all get called "the gate." Largely handled (周漪's is "the gate behind you"; the ring's is "the wall"), but keep them distinct in prose.
6. **Canon-worship risk.** The 100-lap day and the 铁衣 day both resolve with 言天宇 watching Yuhao's canon triumph. That is fine as the term's theme; it must not become the book's default posture once Yuhao's arcs accelerate (海神湖, 考核, etc.).

---

## C. MISSING THINGS (foundation-level gaps)

1. **A positive want.** 言天宇's driving wish so far is negative — *not* to be a trophy, *not* to be excluded. The 3rd-ring hunt is distant. He needs a positive, present-tense want the reader can root for through the term (chapter 4 can seed it: belonging to a *room* — not 唐门's pitch, but a room of his own making).
2. **The cost of moving out, on-page.** 蔡媚儿's three-times promise is lovely — but we never see the empty corner room, the grandmother's face when he leaves, the grandfather who ordered it. One emotional beat owed (small, does not need a full scene).
3. **His world is food-centric and thin elsewhere.** Rooms, the dormitory corridor, non-plot classmates beyond 徐磊/温宁/萧萧 barely have texture. Full-play law wants small weight in the shared spaces.
4. **Zero on-page cooking/roast** despite "the boy who cooks" being load-bearing identity (see B2).
5. **马小桃 thread** has been correctly rested since ch1; fine, but the story should not let her fade so far the ch1 bond cools before it can matter.

---

## D. STRENGTHS CONFIRMED (keep — do not "fix" these)

- **The secret firewall holds.** No dragon leak, no 双生武魂 reveal, no 天梦/million-year leak, no knowing-circle break anywhere in prose (verified by read + gates).
- **Canon spine respected.** ep 3/4/5 backdrops are title-verified and the OC rides them without rerouting a single canon outcome; the OC is explicitly not on the 考核 trio; class scale matches canon (~100 → culls).
- **Doctrine language holds.** The ring-eating threshold is written as a living threshold (fight/contender, never immunity) in every prose mention.
- **The friendship engine is genuinely warm.** The ch1 fish → ch2 dining hall → ch3 fire-side chain earns its payoffs without stealing Yuhao/王冬/萧萧's canon dynamics.
- **Footers are honest.** Position / butterflies / wires / state-check each match the page (verified during this read).
- **Voice.** The OC's warmth is real, his restraint is shown in behavior (the kept-light, the middle-pack running), and his grief sits underneath without owning scenes. This is the hardest thing to get right and it is working.

---

## E. DIRECTIVES FOR CHAPTER 4 (the night-market era)

1. Give 言天宇 an **active** lane with a choice and a consequence (the food/market lane is his natural vehicle — but no touching the 徐三石/玄水丹/贝贝-duel chain).
2. **Show the kit for the first time on-page:** 御火 to grill, 厨艺 as craft, and ideally one small controlled 燎羽/light beat whose cost is real.
3. Seed a **positive want** (a room that is his).
4. Pay the **moving-out cost** in a half-scene (grandmother / empty house / grandfather's pride hiding worry).
5. Respect the order-guards added in A6; keep OC peripheral to canon's ep-6 chain; no ep number cited in prose (indexes unstable past ep 5).

---

## F. ADDENDUM — 2026-09-06 spine correction (supersedes part of the above)

**Correction received from the partner:** the invented rationale that protected 霍雨浩's canon 班长 seat — "the over-level auditor can't be fielded; selections exclude him" — is **rejected as false logic and a mischaracterization of 言天宇**. No-favours means the OC is given nothing; it never means he is set aside knowingly. The OC is not a pampered prince: he is humble, playful, a top student trained by 穆恩, warm — the natural center of his room.

**What this changes in this audit:**
- The "protagonist passivity / nobly holding back / he declines to run" finding (§B.1 and §A row notes) was written while ch3's non-run was framed as **周漪's exclusion**. That framing is gone. Under the corrected spine the OC is **wall-capped and not on this year's ladder** (he cannot gain a level until 穆恩's hunt — his grandfather's own ch1 framing; the room's selections belong to the room's climb), and he *chooses* the room's back for the 班长-run and says so plainly to 周漪. He runs every training day with the room; the hundred-lap cull (ch2) he ran with them and finished holding back.
- **Acting vs spectating is now caused and bounded:** ch3's single rail-morning is a choice spent in service (he steadies, reports, feeds, brings water). His driven want moves events from ch4 on (the wall-fire for the ones who eat last; the stall partnership with 霍雨浩 in ch6). Watching-while-waiting is a posture for one year, never a habit.
- The audit's hard canons survive unchanged: not on the 考核 trio (locked), 霍雨浩 becomes 班长 on the iron-run day (canon), no canon outcome altered. The *reason* the OC isn't on the trio / isn't the room's banner now flows from the wall + his nature, never from a bench rule.

Retrofit executed across ch2–ch6 prose, footers, and the bible/doctrine copies (T02 row, POST-CH3 standing rule, CANON_CLOCK lane). Verify gates re-run green.
