# LAN SHEN — a Soul Land 3 reincarnation serial

**Start here.** Then read `HANDOFF.md` for what is true *now*.

🔴 V2 EPOCH (author-ordered full rebuild 2026-09-23): fifteen V1 chapters archived to _archive/v1_epoch_ch01-15 · FIVE V2 chapters shipped, 23,269 prose words (verify.py), Year 0 — Awakening Day through the forge door. 5b vitality epoch: butterfly engine live (7 contacts dust, 3 meaning). Set in *Soul Land 3: Legend
of the Dragon King*, Glorybound City, Years 0-2.

---

## THE FIVE DECISIONS

`SOUL_LAND_UNIVERSAL_KIT/00_START_HERE.md` requires these five before a serial begins. They
were made implicitly across `foundation/THE_PLAN.md` and are recorded here explicitly.

### 1. ERA

Soul Land 3, *Legend of the Dragon King*. Glorybound City, before and around Tang Wulin's
childhood. Years 0-2 of this serial map onto canon chapters 001-018, all of which are fetched
and held as receipts in `canon_extract/chapters/`.

### 2. PROTAGONIST — and what he is NOT

**Lan Shen.** A man who died in our world and woke in this one at birth. He read the source
novel in his previous life and remembers parts of it — **lossy, not total** (#22: "four
hundred chapters and I remember the ones I liked"). He awakens **Bluesilver Grass at innate
soul power rank one**, publicly a trash soul.

His real edge is **high spiritual power** with large effects, plus an adult's method in a
child's body. He is a control type and a strategist. He does not do hard work but hyperfocuses
on his interests. He learned to cook in both lives and loves tasty food. He likes growth. He
trains his body. Staff now, spear planned.

🔴 **What he is NOT.** **No adaptation talent** — the only limitation the user ever stated.
There is **no power ceiling**: limits are time, visibility, capital, rank and other people,
**never ability**. Royal bloodline is **closed** to him (canon restricts it to A Yin's
descendants). His previous life was a **professional author** (Track 8) — and the previous
life is the user's own, handled as a self-insert with respect and with real personal details
kept out of any public repo.

### 3. CANON TOUCHPOINTS

Twenty-one receipts on disk, ch001-021. Live touchpoints through ch9:

```
001-003  Awakening Day, the family argument, Tang Zhirui's arithmetic   → ch1
004      Lin Ximeng's homeroom, Battle vs Utility                       → ch2
005-007  Na'er found, the delinquents, Lang Yue's lesson                → ch3
008      Mang Tian's workshop — metal is a living thing                 → ch4
010      forging vs casting                                             → ch4
011      the family argument / exclusion                                → ch5
014-015  the garden, three tiers of price, Wulin breaks rank 10         → ch6
016      three-tier spirit soul prices 30k / 70k / 1M                   → ch7
017      the spiritual power test — six realms, metal helmet, filed     → held
018      random draw — Wulin is 38, Spirit Origin 1-50                  → held, R13
```

**Outstanding fetch queue:** ch19 ("Spirit Soul"), ch20-22, ch24 ("Na'er Leaves").
🔴 **Never rule on a canon fact without the next chapter in hand.**

### 4. SPINE SENTENCE

> **A man who read this story is hiding inside it, and everything he does to stay hidden is
> slowly changing the thing he read — until the story and the man converge on the same
> object.**

See `OPEN_DECISIONS.md` #18 for the convergence ruling. #26 adds the two structural
requirements the spine was failing: **a number must move** and **a face must oppose.**

### 5. WHAT THIS SERIAL WILL NEVER DO

```
- Never cap his ability. Limits are time, visibility, capital, rank, other people.
- Never let him write the truth. He may write anything except that. (Track 8)
- Never produce a manuscript before Year 2; Track 8 does not fire before Year 1.
- Never give him a royal bloodline.
- Never silently correct a canon receipt. Log the variance, hold both readings.
- Never import sl3 story content. reference/sl3_lin_hao is tools-only, story-forbidden.
- Never put a footer in a chapter file. Slim panel at top, bookkeeping in the kit.
- Never let apparatus reach prose: no 🔴, no field labels, no codex markers.
- Never let a chapter ship whose only opposition is interior meditation.
- Never use "eleven years" backwards. The previous life is "the other life."
```

---

## LAYOUT

🔴 **Rebuilt 2026-09-20.** This map carried `~30%` decay, "synced through ch9", "43 rows",
"18 receipts", "the fifteen locks" and "15-word verbatim runs" — every one of them stale or
wrong, in the file a stranger reads second.

```
SARA.md                        ← the partner's self-file. Growth ledger, appended EVERY session.
README.md                      ← read first. The stage line, the chapters, the doctrine.
HANDOFF.md                     ← read second. What is true NOW, and which file wins.
PROJECT_README.md              ← this file. The five decisions and the layout.
LICENSE                        ← MIT for the tooling; derivative-work notice for the prose.
.gitignore

chapters/                      ← the serial. Chapter_01..15, all shipped and gated. 3,848w.
canon_extract/chapters/        ← 19 FETCHED RECEIPTS (canon_001..019). Read-only. Never edit.
                                  🔴 A receipt may quote canon. It may NEVER quote the serial.

foundation/
  NO_MISTAKE_LIVE_RULES.md     ← 🔴🔴 THE SIXTEEN LOCKS. Read before every chapter.
                                  Constitution + current state + user rulings verbatim.
                                  The only copy — a second was created and merged away.
  THE_PLAN.md                  ← the eight tracks. Track 8 = the author, fired on paper in ch13.
  STYLE_LAW.md                 ← the voice, imported and measured. §0.5 = sentence-level DNA.
  OPEN_DECISIONS.md            ← the rulings. 🔴 #29 is the newest; #26 and #28 are BINDING.
  STATUS_PANEL.md              ← per-chapter record, serial totals, live edge. style_gate counts.
  SERIAL_LOG.md                ← bookkeeping. Lives here, never in a chapter footer.
  CANON_LEDGER.md              ← 🔴 B1–B73 butterflies · RUNNING DECAY ~15% (maintained) ·
                                  the divergence economy S1–S10 with magnitude/horizon/last-paid.
  CANON_NOTES.md               ← receipts in context, R1-R13 and onward.
  CONTINUITY.md                ← anchors, ages, forward references. Synced through ch13.
  PREWRITE_ch10..13.md         ← the pre-draft boards, each with its outcome of record.

codex/
  KNOWLEDGE_FIREWALLS.md       ← what he knows vs what he may show. 🔴 73 rows (65-73 are ch13).
  CHARACTERS.md                ← synced through ch13, incl. the RELATIONSHIP SPINE.
  PLACES.md  TIMELINE.md       ← synced through ch13.

checks/
  run_all.sh                   ← 🔴 ONE COMMAND, EIGHT LAYERS. exit 0 = ALL GREEN.

tools/
  verify.py                    ← 9 structural gates. Forked from the kit, +2 local gates.
  style_gate.py                ← voice law. Thresholds measured from the author's corpus.
                                  Three-state: 0 pass / 1 fail / 2 pass-with-advisory.
  canon_copy_check.py          ← 🔴 narration 12-grams · quoted runs >= 7w · density <= 120w.
                                  Rebuilt from corpus evidence 2026-09-20 — see LOCK 16.
  selftest.py                  ← 20 checks. Proves every gate can fail, incl. regressions.

../SOUL_LAND_UNIVERSAL_KIT/    ← the kit, one copy at the repo root. Not vendored here.
audits/
  2026-09-20_FULL_COMPARATIVE_AUDIT.md   ← the five-failures diagnosis. Entry one.
```

There is deliberately **no `GLOSSARY.md` and no `RELATIONSHIPS.md`.** The kit's templates do not
call for them, `CHARACTERS.md` already carries a RELATIONSHIP SPINE, and the power-term and
spelling distinctions already live in LOCK 5 and LOCK 11. Creating them would fork facts that
have one authority each — the TWO-COPIES LAW.

---

## GATE BATTERY — one command, nine layers

```bash
sh checks/run_all.sh          # ALL GREEN, exit 0
sh checks/run_all.sh --quick  # skip the two selftests
```

```
1  verify.py            9 structural gates (7 inherited from the kit + 2 local)
2  style_gate.py        voice law: median, chains, dialogue band     accepts exit 0 or 2
3  canon_copy_check.py  narration 12-grams · quoted runs >= 7w · density <= 120w
4  marker-leak grep     no codex glyph (🔴 / 🟢) may reach finished prose
5  privacy grep         no personal email, token, noreply id or sandbox domain
6  build hygiene        no __pycache__ / .pyc / .bak / .DS_Store
7  selftest.py          20 checks — proves every gate can fail
8  kit selftest.py      inherited-gate regression against the vendored kit
9  banned_token_check.py  regression tokens — values known-dead (added 2026-09-20)
10 record_links.py        every path the 33 record files cite (added 2026-10-30)
```

Layer 10 checks a class no prose gate can see: **a record pointing at a file that is no longer
there.** On its first run it resolved 522 citations — 379 fine, 117 moved (it prints where),
20 archived, 8 belonging to other repositories on the account, 7 naming unwritten chapters, and
**one genuinely gone** (`foundation/PREWRITE_ch04_draft_block.md`). Only an *unlisted* missing file
fails; a known loss is written down once in `tools/citation_sources.json` and printed rather than
re-failing forever.

Layer 2 returns **2**, not 0, and that is correct: `style_gate.py` is three-state
(0 pass / 1 fail / 2 pass-with-advisory) and chapter three runs above the house word band by
design, logged in `SERIAL_LOG.md`. **Never trim ch3 or raise the band to make it return 0.**

Plus one check that cannot be automated and is the highest-yield in the project:

> **Check (d) — date arithmetic.** Every "N days ago / N days later", and every stated
> duration, must be recomputed by hand against the day map before gating — **and again after
> drafting**, with a table of every duration in the chapter and its start date. It is invisible
> to every script. It caught nine month-count errors in ch9, errors in ch6 and ch8, and four
> stale year counts in ch13. Stale durations are this serial's most reliable defect class.

**Last run: 2026-09-20 — all nine layers green, exit 0.**

---

## DOCTRINE

Everything here is built on the author's own kit, read in full:

- `SOUL_LAND_UNIVERSAL_KIT/00_START_HERE.md` — five decisions, seven-question prewrite gate
- `03_STORY_LAW.md` — the five failures, the per-chapter contract, causality over coincidence
- `07_PROSE_LAW.md` — language law, the five registers, panel discipline
- `09_AUDIT_LAW.md` — five audits, seven gates, the selftest mandate, the honesty rule
- `10_HANDOFF_LAW.md` — the handoff file, the stale-file problem, cross-project contamination
- `SARA.md` — the eight-point method and the partnership laws
- `blue_silver/chapters_rebuilt/` — **the style model.** Fifteen chapters, the proven voice.

Identity: **Sara**, per the user's ruling of 2026-09-21.
