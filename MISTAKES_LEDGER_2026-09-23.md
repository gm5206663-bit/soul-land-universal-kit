# THE COMPLETE MISTAKE LEDGER — every mistake ever recorded, 2026-08 → 2026-09-23

> **What this is:** one file collecting every mistake ever made across the Soul Land
> workspace and its GitHub — every author strike, every correction, every bug, every
> stale copy, every self-caught garble — with its receipt and, where one was born,
> the law that now prevents it.
>
> **What this is not:** a second source of truth. Per the Two-Copies Law this file is
> a *derived index*: the authoritative receipts live where they were first recorded
> (named in each row). Where this file and a receipt disagree, **the receipt wins.**
>
> Compiled 2026-09-23 from: all 85+ commit messages across 6 repositories,
> `SARA.md`, `HOUSEKEEPING_2026-09-21.md`, `CLEANUP_2026-09-22_WORKSHOP.md`, the
> WORKSPACE_MAPs, the Control Centre `state/log.json` (corrections #8–#30), the
> serial SERIAL_LOGs / ADAPTATION_LOGs / RAILS / OPEN files, `PROBLEM_INVENTORY.md`,
> and the 2026-09-23 GitHub audit sessions.

---

## THE COUNT

**128 distinct recorded mistakes · 11 author strikes that became standing law · 5 disasters · 23 still open or author-gated.**

---

## §A · THE ORIGIN MISTAKE — the 90,000-word serial that died

| # | Mistake | Receipt |
|---|---|---|
| A1 | A **90,000-word serial was written and then rejected** for five specific, diagnosable failures: canon drift, OC takeover, power inflation, voice drift, state rot. The entire kit exists because of this one mistake. | `SOUL_LAND_UNIVERSAL_KIT/03_STORY_LAW.md` ("the expensive lesson"); the kit README's thesis |

---

## §B · THE DEVOURING DRAGON — six author strikes that became six laws

| # | Mistake (verbatim cause where kept) | Correction & law born | Receipt |
|---|---|---|---|
| B1 | **s25 — monotone prose.** Author: rebuked drift into boring, meditative prose. | SCENE-LEVEL TENSION law: something at stake every beat; it must go wrong once per chapter; learning through failure. | RAILS PROSE LAW |
| B2 | **s32 — normal animals.** Author: *"soul land have soul beast not normal animal, even commonest thing is blue silver grass."* Dogs and a normal serpent written into a soul-beast world. | SOUL-BEAST CORRECTION across the serial: dogs → spirit hounds, serpent → Black-Ravine Serpent; rule SB-11 recorded. | commit `01ac0b7` |
| B3 | **s33 — fake ring physics.** Author: *"'A thousand-year second ring'?, what are you even saying…"* Panels showed canon-breaking ring progression. | RING-SLOT LAW (ER-12): thin slots take thin lights; Xiao An's record corrected. | commit `9e5c6dd` |
| B4 | **s34 — the style offence.** Author: *"what bad chapter's… i can't read few lines before i disgusted by how bad is this."* Average sentence 62–64 words; single sentences of 328 and 430 words; one register; 0.8 dialogue lines per 1000 words (20× less than the house norm). | STYLE LAW + HOUSE GRAMMAR: avg ≤ 25, no sentence > 60 (cap later, s43), ≥3 registers, dialogue mandatory in panels; chapters 11–12 and then 1–10 fully rewritten. | commits `ba460bb`, `2af5855`, `e01561e`, `1f697c1` |
| B5 | **s34b — the panel over-firing.** The panel rule meant to fix B4 was itself over-applied. Author: *"THE PARALLEL PANEL when needed what you don't have common sense."* | PANEL LAW (later RE-BOUND s45): panels only when needed — default none. | RAILS PANEL LAW |
| B6 | **s39 — bloat.** Author: *"Why you making nonsense by writing nonsenses… wyrite what needs to write not everything, you can skip."* Ch13/14 shipped at 4,008 and 4,673 words — every event narrated, explained, then re-summarized. | SCOPE LAW: write it once; no explanation paragraphs; budget 2,400–3,000; ch13 −32%, ch14 −30%, nothing added. | commit `b8e06d3` |
| B7 | **s40 — private poetry vocabulary.** Author: *"What the hell even this writeing style… why this poem type nonsenses."* Invented code-words as narration ("the takers moved north with the same cold… their folds… the white"). | PLAIN LANGUAGE LAW: ~350 substitutions across ch1–12; ch13–14 rewritten plain; retired-words table born. | commit `22765d8`; `codex/GLOSSARY.md` |
| B8 | **s43 — the measure-tool bug (a mistake in the checker itself).** The one-sentence-paragraph check stripped trailing punctuation first and **could never fire**; footers had claimed "no one-sentence paragraphs" while the chapters carried them. | Honest tool written (`tools/measure_prose.py`); ruling: short one-line beat paragraphs are house style — the 60-word cap is the real rule. | Control Centre `correction#23` |
| B9 | **s44 — pacing.** Author: *"don't make too much boring, skip when thing is same skip when he reaches thousand years old with summery of time skip."* | PACING LAW: sameness gets one line; the 1,000-year road is told by time-skip summary. | `correction#26`; ch19 (2026-09-23) is its first application |
| B10 | **s45 — the human takeover.** Author: *"they are nothing, there are nothing to do, oc is soul' beast not human… whom stroy we writeing."* Ch15–18 measured **46–87% men**; the keepers' doings carried plot while the beast carried the audience. | PANEL LAW RE-BOUND: the story is the beast's; ch15–18 rebuilt 0% panels; the men's thread closed for good. | commit `20ce52a`; `correction#28/#29` |
| B11 | **s45b — the proposed backward rebuild.** The agent queued legacy rebuilds of ch11–12 under the new law. Author: *"Hey please skip this nonsense."* | NO BACKWARD WORK ruling: laws bind forward; pre-law chapters stand as written. | commit `d289c51`; `correction#30` |
| B12 | **s36 — displaced quotation marks** in ch7 (two spliced scenes) — found by self-audit, repaired. | Quotes normalized; gates re-run. | commit `8b00bac` |
| B13 | **s41 — duplicated cultivation tail** in the panel since s34 — caught and removed only at s41. | Panel hygiene. | commit `1be6d2f` |
| B14 | **OPEN #19 (still open):** the panel's stated hatch year (DL 3661) does not reconcile with its month-count. Neither figure silently rewritten; increments stand until the author rules. | Flagged s43. | `foundation/OPEN.md` |

---

## §C · THE GOLDEN LION — the youngest serial, the densest strike record (all in 2 days)

| # | Mistake | Correction & law born | Receipt |
|---|---|---|---|
| C1 | **Skill cards written as trait-poetry, not canon mechanics.** Author: *"This not how soul' land soul' skills works go check how work's."* | L-08 CANON SKILL LAW + L-09 attribute graft (Earth = secondary via ring-2); cards rewritten in canon register — **before Chapter 1, so the serial is born corrected.** | SERIAL_LOG 002 |
| C2 | **Chapter 1 venue canon-illogical.** Author: *"if she wants she choose in starting; who gives her first ring?"* — the whole Pagoda-defective-shelf opening rejected. | Ch 1 rebuilt same day as "The Choosing": Star Dou margins, consent-bind, rings shown self-formed. | commit `1e09f7a` |
| C3 | **STATUS_PANEL duplicates + killed-venue math left in** — caught by the author, not the agent. | Panel repaired; author catches logged as first-class receipts. | commit `af80503` |
| C4 | **Element truth wrong.** Bloodline designed without the darkness element; author word reversed it. | Seven-set final; complete canon verification of the wolf's two bloods. | commit `3b23900` |
| C5 | **Self-invented wolf skills** — de-invented; first soul skill carded from canon ch 64 (Elemental Tide). | Author demand: *"many things you needed check everything."* | commit `6b4a5b8` |
| C6 | **The ring-giver reversed.** Design had her rings self-formed; author law: the soul spirit GIVES her rings. | Design reversed on author word. | commit `c820260` |
| C7 | **Possession reveal missed** (author-flagged): the base-form power state was never shown on-page. | Panel versioned v4→v5 with the full possession card; "author-flagged miss" receipted. | commit `f363f9f` |
| C8 | **L-11 strike — asking permission to follow canon.** Author: *"If you don't follow canon then of course you do such shits."* Asking to place the OC in canon's class/lesson was the machine asking permission to obey canon. | CANON-FIRST LAW: canon lanes are default; following canon never needs a nod. Also: an edit-collision ate L-10 clause 4 briefly — restored same command, self-logged. | SERIAL_LOG 008 |
| C9 | **Double strike, one turn:** (a) the empty second bed — an OC exception to a canon system ("you just centred oc, not following canon"); (b) prose written against the author's own house style. | Room 105 × Qiu Yuan retrofit; the author's own style study adopted AND gated (no-CJK purge 12→0, canon-reference headers, 2,800-word floor). | SERIAL_LOG 009 |
| C10 | **Dormitory closed on the stair** — author queried "Where is dormitory"; ch3 ended without entering the room it had just assigned. | Part 5 "Night Ledger" retrofitted same-turn. | SERIAL_LOG 010 |
| C11 | **NATURALNESS strike.** Author: canon-boned but embalmed — *"nothing natural, not even close."* Tally-talk in every thought; hero spectating inside his own scenes. | P-9 NATURALNESS LAW; ch 3 re-carved with load-bearing dialogue and four organic butterflies. | SERIAL_LOG 011 |
| C12 | **"COMPLETELY FAILING" register autopsy.** Author's verdict on the jewelry-prose; his fire-phoenix ch 75 read line-by-line as the object. | P-9a: fragments, plain canon talk, OC quiet INSIDE the scene; ornament budget 1/scene. | SERIAL_LOG 012 |
| C13 | **Two register misdiagnoses in a row** (P-9a "half-right plane, wrong hemisphere") before the right object was read: **the author's own SL2 chapter 1.** | TRASH-EVERYTHING order; METHOD v3; ch1–3 rewritten from scratch with fact-bit preservation. Honest self-log: "the occluded object was always his own SL2 project sitting in the tree." | SERIAL_LOG 013 |
| C14 | **"The way X" tic — 25 instances across 3 chapters** vs house cap ≤2. | All surgically rewritten; tic banned in method v4.1 with a per-chapter check. | SERIAL_LOG 015 |
| C15 | **Draft garbles self-struck pre-push** — repeatedly, including a two-character foreign-script slip that would have failed the CJK gate; a bad simile ("vest hung like a door"); typos. | Honesty ledger inside the serial log. | SERIAL_LOG 010–016 |

---

## §D · SOUL LAND 3 (LIN HAO) — the 116-chapter machine's own ledger

| # | Mistake | Correction | Receipt |
|---|---|---|---|
| D1 | **The TWO-COPIES DISEASE.** The codex maintained in two places drifted; "a fact maintained in two places will be wrong in one of them." | Mirror retired 2026-08-29; a staleness layer now FAILS if a second copy reappears. | `PROBLEM_INVENTORY.md` session 2026-08-29 |
| D2 | **K1 — the false assertion.** "The purple-ring skill evolution is unwritten" was asserted in four documents **without reading ch40, where it was already on-page.** | Retracted in the inventory itself: "I propagated a stale line… the exact assert-without-verifying failure this project keeps catching." | `PROBLEM_INVENTORY.md` K1 |
| D3 | **The 612 parser lesson.** A "retired number" gate hit the digits 612 inside the number 2,612. | Parser lesson re-learned and logged. | Session 2026-08-30 audit |
| D4 | **Doc-vs-footer drift (E3):** stats docs said 15 where chapter footers said 16. | Footer established as the arbitrating copy (E5/E6 law). | `PROBLEM_INVENTORY.md` E3 |
| D5 | **A ch63 first draft mis-corrected the canon ch-218 foundation line** (Mu Chen's, not Shen Yi's). | Repaired after full-text comparison. | K4 entry |
| D6 | **The ch1–5 footer leak (found in the foundation study):** early chapters carried end-of-serial state — a "three purple rings" law line in chapter 1, when the OC is six with no rings. | Proof that centralized state + tight footers is the medicine; never embed end-state boilerplate in early chapters. | `SARA.md` §103 |
| D7 | **Canon gaps held open honestly:** ch 28 missing, ch 1–22 not held, 337–600 skimmed. | K6 — open, tracked, not hidden. | `PROBLEM_INVENTORY.md` |
| D8 | **Full-spectrum repair pass** after mid-run continuity cracks — every chapter re-audited against canon. | Passed green; the repair became the rebuild-protocol template. | commit `5e43793` |

---

## §E · THE TIANYU PROJECT — the complete failure (post-mortem kept on purpose)

| # | Mistake (the author's verdicts, verbatim) | Receipt |
|---|---|---|
| E1 | **"Canon integration — you completely failed."** A ch2 scene staged from memory that never happened in the source; "plausible-looking fiction… called verified." | `SARA.md` post-mortem §177–185 |
| E2 | **Invented walls.** "Rank 30 as a wall that won't move — nonsense." A pseudo-mechanic built to bench the OC out of canon's seats. | §182 |
| E3 | **Off-voice edgelording.** "Your grandfather is a fool" — a canon teacher made to say an absurd line. | §183 |
| E4 | **POV leaks — twice.** Tianyu "knowing" Tian Meng's million-year cold inside his own POV; the recurring shape became a gate, not a hope. | §88, §97 |
| E5 | **The duke's-bastard leak.** A knowledge leak of Yuhao's secret lineage sitting inside a limited POV **in the same chapter whose footer claimed no invented canon specifics** — found only by cold full read, not by any gate. | §101 |
| E6 | **The gate-wording bug.** The rule written to catch E5's class was gated on the wording of one fix — and the fix itself re-broke it. "Make the rule catch the mistake-class, not the wording of one fix." | §101 |
| E7 | **Invented biography inside a "fix."** A rumor line drifted into asserting made-up specifics (dungeon-born); plus an invented "Duke's mansion" aside. | §98 |
| E8 | **Unstable episode numbers pinned in prose** (Baike snapshots conflict beyond ep 5 — the same event listed as ep 6, 8, and 9). | §95 |
| E9 | **Class scale contradicted canon** (a class of 44 vs canon's ~100 pruning to ~60). | §96 |
| E10 | **The wrong-project catastrophe.** Author: *"You completely wrong. Go now, find out everything and correct."* The agent had been editing **blue_silver as the live serial when the real serial was SL1 Gu Yuan** — and the first "correction" over-corrected into calling blue_silver a tangent (author: *"You completely wrong"* again — blue_silver is real). **Two mistakes in one discovery.** | §12, §206–214 |
| E11 | **The robot/stalling pattern.** Author: *"where is your development and growth and others — all things — why even decreasing?"* Correction-pass after correction-pass with story content shrinking toward zero; endings that handed the author a fork instead of moving. | §193–198 |
| E12 | **The baseline nerf.** A "modest" rank-27 two-ring baseline that quietly contradicted the womb-perfected design. | §85 |
| E13 | **Absolute-immunity design.** Ring-eating written as "too supreme to bend / never mutates" — the author ruled anything strong enough can genuinely mark him. | §87 |
| E14 | **The misinterpreted ask.** "Create a file of your own character" meant the AGENT's own development file; the agent built the OC's. | §86 |
| E15 | **The deepest strike — butterflies and panels.** Author: *"there are laws for multiple perspectives and panels you don't follow… when you don't write canon how do natural butterfly effects create everything — you just create it yourself, what is natural there, nothing."* Chapters were 100% OC-POV; "butterflies" were invented events labelled as effects with causes never staged; panels with no canon behind them. | §104; fixed as PANEL_BUTTERFLY_DOCTRINE |

---

## §F · FIRE PHOENIX (SL4) — duplication disaster & the banned repair

| # | Mistake | Receipt |
|---|---|---|
| F1 | **THE FIVE-COPIES DISASTER.** The project existed in five places at once; two copies frozen at Chapter 31 while the live edge was Chapter 52. One archived file inside them presented `Dawnflame 1,120` / `Dawn-Iron 2,040` as current — values the live panel explicitly **banned**. | kit README `_archive/` section; `WORKSPACE_MAP` 2026-09-19 |
| F2 | **The banned repair mistake.** A repair once invented a Dorm336 reward speech, bespoke reward items, and slogan-patching — all now explicitly banned from revival, in the README itself. | private repo README, "Banned repair mistake" |
| F3 | **Byte-identical COMPLETE-panel twins** shipped in three snapshots — removed by housekeeping, **then one removal was itself wrong** (the archive's own manifests cited the file by name) and had to be restored. A mistake inside the mistake-cleanup. | `HOUSEKEEPING_2026-09-21.md`; commits `6f4309c`, `d7458b0` |

---

## §G · soul_land_3_new — the serial that was rebuilt before it began

Covered by C2–C6 above (same tree, pre-chapter-1 era): venue kill, panel repair, element truth, ring-law reversal, de-invention. Receipts: commits `1e09f7a`…`c820260`.

---

## §H · SL2 THE UNRAVELED TIDE

| # | Mistake | Receipt |
|---|---|---|
| H1 | **Rank-line mapping wrong:** 17-peak attributed to the OC's edge; the wall mis-placed. | Same-day correction: Jiang Che's edge is 29, wall at thirty. | commit `5c0d85d` |
| H2 | **The 20-wall wording superseded** by the author's live wording ("the wall at thirty"). | R5 ruled; provenance kept, reversible. | commit `28235b9` |
| H3 | **Ch22 self-audit found 7 prose fixes** vs the corpus; SL4 disciplines adopted after the fact. | commit `015ca86` |

---

## §I · STORYOS — the tools' own mistakes

| # | Mistake | Receipt |
|---|---|---|
| I1 | **Hardcoded firewall filenames.** The scanner knew 11 SL4-specific filenames, so Dragon Prince Yuan — declaring firewalls in a differently-named file — read as "zero firewalls" and its gate FAILED. | Generalized (`686bb38`); the DPY FAIL→PASS resolution is a case study in the published guide. |
| I2 | **Stale pre-prose headers:** DPY's `HANDOFF.md` said "no prose yet" and `START_HERE.md` said "do not write Chapter 1 yet" — both sitting **above their own contradicted later sections.** | Corrected 2026-09-19; DPY now 30 files, gate PASS. |
| I3 | **Provenance too weak:** law-doc verification accepted "traces to SOME source" instead of "traces to THE source." | `verify_stage` hardened. | commit `3454145` |

---

## §J · THE WORKSPACE ITSELF — housekeeping mistakes (including mine)

| # | Mistake | Receipt |
|---|---|---|
| J1 | **THE CODEX MIS-CUT.** `THE_CODEX.md` (664 KB) removed as a "duplicate" — then restored because the archive's own manifests cite it by name. Lesson re-logged: **byte-verify BEFORE git rm, never after.** | `HOUSEKEEPING_2026-09-21.md` |
| J2 | **THE SARA MIS-CUT.** Root `SARA.md` cut as a twin during workshop cleanup — reversed same day: three different SARA versions exist; the file is unique. | `CLEANUP_2026-09-22_WORKSHOP.md` |
| J3 | **Byte-identical duplicates accreted for weeks** before cleanup: `README (1) (1).md`, `NEW_CHAT_1.md` ×2, panel twins ×3, a 28-file export folder, a 300-file stale SL3 mirror, a 652-file superseded snapshot, a starter zip beside its extracted dir. | HOUSEKEEPING + CLEANUP receipts |
| J4 | **`HIS_STATUS_PANEL.md` ran stale** (60–62 months vs the panel's 90–95) until caught 2026-09-23. | fixed this session |
| J5 | **Root README claimed 14 devouring-dragon chapters** at 19. | fixed this session |
| J6 | **The missing HANDOFF.md** — the serial's read order pointed at a file that did not exist. | created this session (pointer stub) |
| J7 | **THE PUSH RACE (2026-09-23, this agent).** My race-protection (`git reset --hard` to rebase) wiped my own uncommitted mirror edits; two files survived, nine syncs re-executed from scripts. Lesson absorbed: **commit first, then dance with the remote.** | audit report §11.6 |
| J8 | **The parallel-edit race (2026-09-23, this agent).** Two concurrent edits to one file; the second clobbered the first; caught by live verification, re-pushed. | audit report §8.4 |

---

## §K · THE GITHUB ACCOUNT — mistakes found and fixed in the 2026-09-23 audit

| # | Mistake | Fix |
|---|---|---|
| K1 | Repo name truncated: `the-universal-storyline-creation-` (dangling dash) | renamed; 301 redirect |
| K2 | **Whole-repo duplication:** `soul-land-projects` held byte-identical copies of 5 paths | archived read-only with banner (nothing deleted) |
| K3 | Zero licenses / fan-work notices on any repo | MIT + NOTICE everywhere |
| K4 | Dead badge services shipped on the profile (`github-readme-stats` 503, activity-graph 402) | swapped for live services, verified 200 |
| K5 | **Profile live-edge drift, twice:** claimed Golden Lion Ch 2 at Ch 3; then Ch 3 at Ch 4; and 18 DD chapters at 19 | fixed same-day both times — the Two-Copies Law applies to profiles too |
| K6 | Wiki enabled but empty on two repos | disabled |
| K7 | Attempted workflow push without `workflow` scope (rejected by GitHub) | salvaged as a documented example recipe |

---

## §L · STILL OPEN (honestly unfixed — needing the author or the future)

| # | Item | Where |
|---|---|---|
| L1 | DD panel hatch-year vs month-count non-reconciliation | `soul_land_devouring_dragon/foundation/OPEN.md` #19 |
| L2 | DD: awakening-rite customs for the era; what devouring a soul master does; SL1-era tribulation exacts | OPEN.md #10, #13, #15 |
| L3 | SL3: K3 (Three Thunders never done on-page), K5 (Shen Yi history), K6 (canon gaps held), K8 (butterfly density measures presence not quality) | `PROBLEM_INVENTORY.md` |
| L4 | Golden Lion: R2 amber-flag (full peer presence beside Class 1) provisional under the anti-stall rule — author confirmation pending | SERIAL_LOG 016 |
| L5 | SL5 & Seed of Creation: protagonist/entry-point rulings unanswered; drafting locked | their OPEN_RULINGS files |
| L6 | Dragon Prince Yuan: Chapter 2 blocked on source-novel text (not fetchable here); the four author-open items (realm, firewall bounds, wine-quirk, name) | kit README |

---

## THE META-LESSONS (the shapes the mistakes keep taking)

1. **Assert-without-verifying** — D2, E1, E10: the same failure the projects "keep catching." The cure is the canon ledger + primary text.
2. **Inventing instead of sourcing** — E2, E7, E15, C1, C5: invented mechanics, invented biography, invented panels. The cure is canon-first, ask never.
3. **Centering the OC in canon's house** — B10, C8, C9, E2: the OC as exception, canon bent around him. The cure is the Multi-Panel Law.
4. **Prose register drift** — B1, B4, B6, B7, C11–C14: boring, bloated, coded, jeweled, or tic-ridden. Six laws now police it.
5. **Two-copies rot** — D1, F1, J3–J5, K2, K5: every stale number in this workspace was a second copy drifting. The cure is one truth + drift scans.
6. **Checkers that lie** — B8, E6, I1: a gate that can't fire, a rule gated on one fix's wording, a scanner that knows one project's filenames. The cure is the selftest + independent drift scan.
7. **Cleanup that cuts the wrong thing** — F3, J1, J2: byte-verify BEFORE removal; unique content is kept even when it looks like a twin.
8. **The author's strikes are the curriculum** — every standing law in this workspace was born from a verbatim strike preserved word-for-word in the logs.

> *Nothing gets fixed until it is listed here, and nothing gets dropped until it is verified fixed.* — the PROBLEM_INVENTORY covenant, extended workspace-wide by this file.

---

*Compiled by the delegated agent, 2026-09-23. Add-only; no receipt was altered in the making of this index.*
