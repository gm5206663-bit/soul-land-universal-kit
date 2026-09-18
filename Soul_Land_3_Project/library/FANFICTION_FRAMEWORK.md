# FAN-FICTION FRAMEWORK
### The reusable method, distilled from *Soul Land 3: The Adaptive Prodigy* (37 chapters, ~200k words).
### Recreated 27 Aug 2026. This file is project-agnostic: everything here transfers to the next fic.

---

## 1. THE FOUR-FILE STRUCTURE

Every project gets exactly these, and nothing else. Proliferation is a failure mode — the user's own words:
*"Don't create too many things… delete extra files."*

| File | Holds | Rule |
|---|---|---|
| `THE_CODEX.md` | Story FACTS only — characters, ranks, timeline, canon state, laws, per-chapter records | The bible. Versioned. Mirror it to `CODEX/`. |
| `<MC>_STATUS.md` | The protagonist's current numbers and progression lines | One source of truth for stats. |
| `POWER_MODEL.md` | Every number, its canon anchor, and the curve it sits on | If a number isn't here with a citation, it doesn't exist. |
| `PROBLEM_INVENTORY.md` | Every known defect, with evidence and status | Nothing is fixed until listed; nothing is dropped until verified. |

Supporting, not core: `CANON_ACCESS.md` (what canon you hold and where), `archived: CODEX/98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz` (worklist),
`checks/` (the suite).

---

## 2. THE LAWS

These are the load-bearing rules. Each one exists because it was violated and the violation cost real work.

1. **PRIME LAW** — the OC is the ACTOR, never the SPECTATOR. Verb-count test: if he only *watches*, *files*
   and *notes*, the chapter is broken.
2. **CALIBRATION LAW** — no sandbag fights. Escalating ladder, strain shown. Beating a weaker opponent proves
   nothing; it's a rank gap, not a demonstration.
3. **IDENTITY LAW** — the OC's core is an identity, not a toolkit. Test: strip the auxiliary abilities; can the
   core still win?
4. **PERSONALITY LAW** — give him a *voice*. Teasing, humour and warmth are what make the quiet moments land.
5. **BUTTERFLY-INTEGRATION LAW** — canon characters must react to the OC's presence. Never reproduce a canon
   beat verbatim while pretending the OC isn't in the room.
6. **GROWTH LAW** — every progression line moves every chapter, or the stillness is explicitly justified.
   Time passing without numbers moving is a logic failure, not a style choice.
7. **ENSEMBLE LAW** — the supporting cast is the spine. If a character stops appearing, the story must say why.
8. **NO CHAPTER WITHOUT VERIFIED CANON** — if the canon can't be read, say so and stop. Never invent and label
   it canonical.

---

## 3. PROGRESSION LINES — SIX, AUDITED EVERY CHAPTER

A protagonist has at least six independent lines. Tracking one and freezing the rest is *the* recurring
failure in long fic.

1. **Rank / cultivation** — with a hard gate if the story has one, and an explicit statement of what the gate
   does and does not block.
2. **Spiritual / mental power** — against a canon ladder with named tiers.
3. **Physical** — measured, with the instrument's ceiling stated.
4. **Skill / martial line** — realms and named techniques, not "he swings it well."
5. **Trade / profession** — ranks with canon titles, and the economics of it.
6. **Companion / bond** — a creature, weapon or partner with its own arc.

Plus: **appearance and mutation**, which is the line most often silently dropped. Audit it explicitly.

### 3.1 🔴 THE SAME SIX LINES EXIST FOR EVERY NAMED CANON CHARACTER

**This is the lesson that cost 61 chapters to learn.** The six lines above were audited for the
protagonist and *nowhere else*. The canon characters' numbers were never checked, and every one of
them rotted:

- one character held the same rank for **49 consecutive chapters** while canon moved him three ranks
- another held his for **45**, a third for **41**
- one was never given a number at all in any chapter
- two more were carried as bare labels ("~23", "gone") with no schedule behind them

The protagonist's lines were watched obsessively. The other characters' were not watched at all.
**A progression line that belongs to a secondary character is still a progression line.**

**The permanent fix — three files:**
1. **`CHARACTER_STATS.md`** — every canon number for every named character, each with the verbatim
   canon line that supports it. Not in that file with a citation ⇒ it is AU and must say so.
2. **`checks/ensemble_schedule.py`** — the per-chapter schedule derived from it. Single source of truth.
3. **`checks/verify_ensemble.py`** — checks every chapter's ensemble block against the schedule.

Plus: **one authoritative ensemble block per chapter.** If two places in a footer can state the same
character's rank, they will eventually disagree. 202 stale duplicate lines were deleted to enforce this.

**Three traps, all hit at least once:**
- **A plateau is not automatically a bug.** Canon held its protagonist at rank 11 for ~53 chapters.
  The bug is a plateau that *contradicts* canon. WARN at 12 chapters, FAIL at 25.
- **Two different measurements can share digits.** Canon gives one character **153 kg of strength**
  and another **153 spiritual power**. Reading one as the other produces a confident wrong "fix".
- **Source chapter numbers are not a timeline.** Ingested PDFs are numbered independently; the same
  character's rank went 15 → 16 → 17 → 29 → back to 16 by file number. Order by internal evidence.

### 3.2 🔴 REALM GAP IS A FORCE, NOT A PROHIBITION — and the protagonist may be off the scale

**The wrong version of this law, which I wrote and had to retract:** *"a character may not defeat an
opponent a full realm above them."* **That forbids the entire genre.** Canon is full of lower-realm
winners — that is what a protagonist is. Tang Wulin beats rank-27 opponents at rank 15. A teacher beats
a six-ring Soul Emperor in two strokes. Punching up is the point.

**The correct law:**
> **A realm gap must be PAID FOR on the page.** A lower-realm fighter who wins needs a stated reason —
> a bloodline, a divine-strength body, a purple ring, a mutation, a trump card held back. What is not
> allowed is a lower-realm win *for no reason*, or prose that treats rank as a scoreboard two people
> read off together.

**And separately: the protagonist may simply be off the scale.** Record two numbers for him, never one:

| | |
|---|---|
| **Rank** | what the world measures (e.g. 36 — Soul Elder) |
| **EFFECTIVE COMBAT POWER** | what he actually is in a fight (e.g. **Soul King, 51–60**; ceiling **Soul King peak**) |

Every compounding source belongs in that gap and must be listed: the realm · ring count · ring
**colour** (purple = thousand-year) · spirit-soul age · **the trump-card soul skill** · the talent that
scales with him · the mutations that raise the container's ceiling · measured physique · sword realm ·
the fact that he reads.

**The distinction that makes this writable:**
> *An ordinary* three-ring cultivator is a rank. The protagonist is a Soul King wearing a Soul Elder's
> rank. So a strong peer **can** beat an ordinary third-ring — and **cannot** beat him. Those are
> different statements, and the difference is the character.

**The legal result between him and his strongest peer** is not a win for either: it is **outlasted,
survived, cost him.** That is better writing anyway, and it does not require anyone to break the world.

**Two checks, not one:**
- **FAIL** — a peer written as *defeating* the protagonist. `outlast / survive / evade / did not lose /
  cannot defeat` are legal; `beat / defeat / crush / overwhelm / took him down` are not.
- **WARN** — any *other* lower-realm win in the story with no reason-word within 400 characters. Punching
  up is fine; unexplained punching up is not.

**⚠️ And check the summaries against the prose.** While auditing this I found a codex summary claiming a
character "defeats him without touching him" in a chapter where **no fight occurs** — she declines, he
concedes. The prose was right and the summary was wrong. Summaries drift; the prose is the record.

---

## 4. THE VERIFICATION SUITE

Four layers, run after every chapter, exiting non-zero on failure:

- **`verify.py`** — structural: headers present, part numbering contiguous, canon numbers in prose, the
  physical panel complete.
- **`verify2.py`** — semantic: continuity between chapters, ring-law monotonicity, power bands, ensemble
  presence, prose quality, thread abandonment.
- **`audit.py`** — cross-chapter: density of each named character, appearance-comment gaps, thread silence.
- **`verify_ensemble.py`** — **canon characters**: every rank, spiritual-power figure, ring count,
  departure and roster claim checked against the schedule; freeze detection; no stale duplicate lines.

Plus **`state.py`**, which derives the running state from the chapter footers. The footers exist for the
machine, not the reader — keep them short and never ask the user to read them.

**Rules for writing checks** (each learned from a false positive or a silent pass):
- **Verify every new check against known-good passages.** A check that cries wolf gets ignored; an ignored
  check is worse than none.
- **Test that a check still fires after you loosen it.** Inject the defect, confirm it's caught, remove it.
- **Beware the sentence splitter.** Naive `(?<=[.!?])\s+` merges dialogue exchanges into one 150-word
  "sentence." Split after closing quotes too.
- **Metadata is not prose.** Header blocks must be excluded from prose checks but included in structural ones.
- **Make canon guards case-insensitive.** Prose legitimately capitalises a number mid-sentence.
- **Put word boundaries on colours and short words.** `red` matches "honou**red**", `black` matches
  "**black**smith", `going` matches "was **going** to mention". Four false positives in one pass.
- **Exclude citations from numeric patterns.** `\d{3,}` reads "(canon c113)" as a measurement.
- **Guard against negation.** "Zhang Yangzi is **not going**" must not trip a rule about who is going.

---

## 4.5 🔴 THE DERIVED-DOCUMENTS LAW — nothing that can be derived may be typed

**The failure, measured:** in a 61-chapter project the hand-maintained status file said *"End of
Chapter 18"*, the continuation prompt said chapter 28, the power model described a wall that had
opened 21 chapters earlier, and the state module **hardcoded** a rank ceiling that had expired.
Nothing warned about any of it, because nothing checked.

> **A hand-maintained status file in a long project is not a document. It is a lie with a filename.**

**The fix is not diligence — it is to stop typing the same number twice.**

| Kind of content | Rule |
|---|---|
| Per-chapter numbers (rank, power, ledger, creature age, profession rank) | **DERIVE** from the chapter footers into a state file |
| Per-chapter ensemble state | **GENERATE** the block in every footer from one schedule module |
| Status / continuation documents | **GENERATE** them; keep hand-written *reference* panels in a separate file that the generator appends |
| Canon citations, laws, dossiers | hand-write — these are not derivable |
| Mirrors / copies | sync them in the same command that verifies |

**Then add a STALENESS LAYER** that fails the build if any generated document differs from what the
generator would produce, if a doc names an old chapter, if a mirror differs, if the schedule misses a
chapter, or if any file presents a superseded value as current.

**And run regeneration as stage 0 of the verify command**, so the documents are rebuilt by the same
command that checks them. A stale file then becomes structurally impossible rather than unlikely.

**Three traps, all hit once:**
- **Anchor numeric regexes to their marker.** `r'(\d)(?:st|nd|rd|th) rank'` over a footer matched
  *"a fifth-rank teacher"* and returned 5 when the true rank was 4.
- **A generator that preserves "everything above the marker" duplicates its own title each run** and
  is not idempotent. Preserve only non-heading preamble, and assert idempotency.
- **Before replacing a file, read it.** The status file I overwrote contained panels marked
  *"branch files deleted, this is the only copy."* Recover them, give them a permanent home, and have
  the generator append them.

---

## 4.7 🔴 THE CONSEQUENCE SYSTEM — for logical thinking, not for imagination

**Diagnosis first.** Almost every serious error on this project was the same shape: a fact entered the
story and its mechanical consequence was never followed through. Imagination was never the problem.

| Event that entered | Consequence missed | Found |
|---|---|---|
| both rings turned purple (ch40) | soul skills upgrade with the soul | **21 chapters late** |
| protagonist reached peak rank 15 | canon moves him 15→16→17 | **49 chapters late** |
| he became a Soul Elder with three rings | the ensemble's numbers had to move too | **49 chapters late** |
| the rank-30 wall opened | every doc saying "hard wall" became false | **21 chapters late** |

So build for consequence-tracking, not for creativity. **Three artifacts:**

### 1. `CODEX/CONSEQUENCE_RULES.md` — the rule library
A standing list of *"if X enters the story, Y must follow"*, each rule earned by a real failure.
Ten rules so far: ring colour change · spirit soul threshold · realm boundary · a fact that
invalidates a standing statement · a character absent for an arc · a power used for the first time ·
a number measured in-world · a roster change · a cancelled plan · a user correction arriving.

### 2. `CODEX/consequence.py` — the tool
| Command | Use |
|---|---|
| `brief` | **read before writing.** Derived current state + owed items + open premises + the three questions |
| `impact --event "..."` | which rules fire on an event, so you don't have to remember them |
| `premise --id --event --follows --scan` | register: something happened, here is what must follow |
| `check` | grep the chapters (and/or docs) for each open consequence; report what has not landed |
| `decide --find "..."` | **search the decision journal before deciding anything** |
| `rules` | print the library |

### 3. `CODEX/DECISION_JOURNAL.md` — every AU decision with its reason and its cost
**A decision that is not written down gets re-decided differently later**, and that is how a story
contradicts itself. Most contradictions found here were not bad decisions — they were *unrecorded*
ones. Example: "Zhang Yangzi stays while canon has him transfer out" was decided in ch43, never
recorded, and ch60 cheerfully sent him to Shrek.

**Three traps hit while building it:**
- **A substring matcher missed its own founding example.** "rings change colour" ≠ "rings changes
  colour". Normalise inflection before matching, and test the matcher on the case it was written for.
- **A blanket docs-scope produced all-green false positives.** The rule text lives in the docs, so
  every consequence "landed". Scope must be **per consequence**, and default to *the chapters*,
  because a consequence is normally a thing that must happen in the story.
- **This tool cannot prove absence.** A checker can prove false presence but never false absence.
  A rule of the form "nothing may still say Z" needs its own regex checker, not a scan here — framing
  it as a scan produces a permanently-red line that gets ignored.

**And: make consequence debt a WARNING, not a failure.** A permanently-red build trains you to ignore
the build. `--strict` is there for arc delivery.

---

## 4.8 ⚖️ CALIBRATE A THRESHOLD BEFORE YOU OBEY IT

A check that warns is asking you to change something. Before you change the prose, **check whether the
threshold was ever set against the book's own distribution.** Most defaults are not.

**Worked example.** A prose-quality check flagged "sentences over 95 words" in 14 chapters. Measuring
the actual book — 10,879 sentences — gave median 10, mean 18, p99 = 75, max 116. Only **11 sentences
(0.1%)** exceeded 95. Spot-checking the flagged set showed ch7 and ch21 were *paragraph* artifacts
(em-dash clauses, not single sentences) and the 116-word line was a recursive journal bit whose length
was the joke. The threshold was wrong, not the prose. Recalibrated to 110, with the data written into
the source as a comment so nobody "fixes" it back.

**The discipline:**
1. **Measure the distribution** before believing a style warning.
2. **Spot-check the flagged items.** If most are artifacts, the check is broken, not the writing.
3. **Write the measurement into the check** as a comment. An unexplained threshold gets reverted by the
   next person who thinks it is arbitrary — because it was.
4. **Some warnings are correct and should stay red.** Eight chapters run 1,474–1,950 words against a
   2,000 floor. They are short, dense chapters. Padding them to clear a warning would make them worse.
   Record the decision and leave the warning.

**And one more, found the same day:** a generated metadata block appended to every footer was being
read as *prose* by a scene-continuity check, producing seven phantom "character vanished" warnings.
**Any block you generate must be excluded from every prose check** — and re-checked after you add it.

---

## 4.9 🔴 EXPANDING A CHAPTER CAN SILENTLY SIDELINE A CHARACTER

Found 2026-08-28, twice, while fixing short chapters.

**The mechanism.** A presence check measures *density* — mentions per 1,000 words. Add 570 words of
new material and every existing character's density drops by the same proportion. A character sitting
at 0.51 falls to 0.49 and crosses the threshold. **You fixed a length warning and created a continuity
failure, and nothing tells you the two are connected.**

**The rule:** when you expand a chapter, **strengthen the main cast inside the new material.** Don't
add description, scenery or internal monologue to hit a word count — add a scene where the people who
matter are *doing* something. It fixes the length, fixes the density, and improves the chapter, which
padding never does.

**And check whether the character is genuinely absent.** Both times this fired, the underlying problem
was real: one chapter had a main character at **zero** mentions in prose while everyone else was
present. The dilution only exposed it.

---

## 4.10 ⚖️ PLAN THE CONSEQUENCES, NOT THE ENDING

> User, 2026-08-28: *"i later tell what happens when soul land 3 end but i don't think that plan needed
> if go naturally things started happening naturally i think because i experience this"*

**He is right, and this project is the evidence.** Almost everything good in it arrived as a
consequence of something already true:

- A boy who has invented sword strokes for four years fills in a form, and the sentence *"this is the
  first time I have ever made something that was not a stroke"* wrote itself.
- A character who cannot be classified turned out to be the **founder** of a category, because the
  classification system turned out to be paperwork.
- A girl who never showed anyone anything eventually **taught him something**, and that reversal came
  from forty chapters of her not showing him anything.

None of those were planned. All of them were **earned by what was already established.**

**So:**
- **Plan mechanisms, not outcomes.** Lock *how* things work — a System is whatever is on the form, a
  realm gap must be paid for, a consequence must land. Then let the ending be whatever those mechanisms
  produce.
- **Leave endings OPEN and say so.** Write 🔓 next to them. An undecided fate is not a gap in the work;
  it is the part that is still alive.
- **🔴 NEVER decide a character's death to make a payoff work.** I wrote that a classification
  "outlived him" and thereby killed the protagonist in a codex line, to make a Soul Land 4 connection
  feel poignant. The user caught it. **A payoff that requires a death you were not told about is not a
  payoff, it is a theft.**
- **Sequels get their own protagonist.** Soul Land 4 is a new OC. Connection to the previous story is
  allowed to exist and allowed to be undecided at the same time.

---

## 4.11 🔴 THE EXTRAPOLATION FAILURE — the single most common way I get things wrong

Recorded 2026-08-28 after the user caught **four** of these in one day. This is not four mistakes. It
is one mistake made four times:

> **I take one thing the user says and add two or three things that "belong" to it. The additions are
> always sadder, smaller, or more convenient than what was actually said.**

| What was said | What I added | Cost |
|---|---|---|
| *"Wulin doesn't know he's adopted"* | *"…so Lin Hao must know, and Wulin doesn't know he knows"* | Built a whole law on a fabrication |
| *"全能系 is a Soul Land 4 tier"* | *"…formalised long after he is dead"* | **Killed the protagonist** to make a sequel feel poignant |
| *"He wrote a new category"* | *"…and the word means nothing to anyone, forever"* | Robbed him of the payoff while alive |
| *"Gu Yue is canon romance with Wulin"* | *(imported from canon, never checked against my own 61 chapters)* | Contradicted forty chapters of my own text |

**Every one made the story smaller.** That is the tell. When an addition makes things sadder, neater,
or more thematically convenient than what was actually stated, it is probably mine and not theirs.

**THE DISCIPLINE:**
1. **Write down exactly what was said, in their words, before writing anything derived from it.** The
   codex now quotes the user verbatim above every locked law, for exactly this reason.
2. **Never decide a character's death, fate, or ending to make a payoff land.** If a payoff needs a
   death you weren't told about, the payoff is wrong.
3. **Before importing a canon fact into the AU, grep the AU.** Canon says Gu Yue loves Wulin; my
   sixty-one chapters say otherwise. **The story I have written outranks the story I read.**
4. **Prefer the bigger reading.** If a fact could mean something small or something large, the large one
   is usually the one they meant — and it is almost always the better story.
5. **Mark inferences 🔓.** A decision the user hasn't made is not a gap to fill; it is a space to leave.

---

## 4.12 🔴 TWO AXES — never rank two characters on one axis and call it the answer

> Found 2026-08-28. The user: *"if you only compare Wulin and Lin in physical strength… if they are on
> same level then if compared in physical strength then Wulin win, but even same level if you compare of
> fight them this is very hard fight, winner is hard to decide. Now you can understand the gap… if you go
> this root you found yours one of the mistake you doing."*

**The mistake:** I compared two characters on **one** axis — physical strength — and then wrote the
other axis as though the first one settled it. Two files flatly contradicted each other:

- one said he *"equals or exceeds Wulin's in a clinch"*
- the other said he is *"above Wang Jinxi and **below Wulin**"*

Both cannot be true. The second was right: canon puts Wulin at **1,156/1,348 kg** at age 9–10 and
**2,700 kg** scaled, against the OC's **612 kg**. **About half.**

**What made it worse: the story itself had it right.** The prose has the OC step back from a strength
contest and hand it over — *"this one's yours, and it always was"* — and another chapter has Wulin watch
a measurement pass his own number. **My documentation had drifted from my own writing.** The chapter
prose was the most accurate file in the project.

**THE RULES:**
1. **Two characters can each win a different axis decisively.** State both, separately. Never let one
   axis stand in for the whole comparison.
2. **If they met at equal level, say what the result would be.** Here: a genuinely hard fight with no
   clear winner — which is *more* interesting than a ranking, and it was thrown away.
3. **Check the prose before "fixing" it.** When documentation and prose disagree, the prose is usually
   the one that was written while thinking about the scene.
4. **Grep for the contradiction, not for the claim.** I searched for one phrasing and missed the other.
   Search for the *fact* in every phrasing it could wear.

---

## 4.13 🔴 THE TWO-COPIES LAW — the root cause of nearly every recurring defect

> **A fact maintained in two places will be wrong in one of them, and the check reads the other.**

This is not a writing problem. It is a bookkeeping problem that *presents* as a writing problem, which is
why it survived so long: every symptom looked like "I forgot", so the fix was always "remember next time",
and remembering is not a mechanism.

**Found 2026-08-29, in one session, in a 62-chapter project with ten green verification layers:**

| The two copies | What it produced |
|---|---|
| hand-written footer rank vs generated ensemble block | 46 stale character ranks, up to 49 chapters old |
| a canon superlative in the *generator* vs the chapter prose | the user's own caught defect still shipping 8 chapters later |
| the progression schedule vs the prose | Wulin was rank 11 in one and "rank thirteen since before enrollment" in the other, for 61 chapters |
| `ledger` slot vs `spiritual power` slot on the same line | the ledger *was* the spiritual power in seven chapters |
| GROWTH header rank vs footer rank | five headers said `rank 205`, `238`, `254`, `270`, `290` |
| a table headed *"authoritative, audit EVERY chapter"* vs `state.json` | 32 chapters stale |
| a codex belief vs the check enforcing it | a retired power curve stayed enforced for 40 chapters after the reason for it was gone |

### The four rules

1. **ONE SOURCE, EVERYTHING ELSE DERIVED.** If a number appears twice, one of them is a `print()` of the
   other. Generators beat discipline every time — discipline is a thing I have on the day I remember.
2. **WHEN TWO SOURCES DISAGREE, THE PROSE WINS.** The story is the artefact. A schedule that says a
   character is rank 11 does not get to overrule a sentence that says *"rank thirteen since before
   enrollment"* — it gets updated, and the delta from canon gets recorded **at the source**, where the
   next reader will see it.
3. **WHEN A BELIEF CHANGES, THE CHECK ENFORCING IT MUST CHANGE IN THE SAME EDIT.** This is the one that
   makes mistakes immortal. A wrong number gets fixed in a day; a wrong *rule* encoded in a checker keeps
   re-imposing itself on every future chapter, and it feels like rigour while it does it. There was a
   literal table enforcing *"Gu Yue is canon's crown and must stay highest"* for forty chapters after I
   stopped believing it.
4. **CHECK THE HAND-WRITTEN PART AGAINST THE DERIVED PART.** Generating the authoritative copy is not
   enough. Layer 11 exists purely to diff them, and it found **99 contradictions on its first run** in a
   project that had passed ten layers.

### How to calibrate the new check (do not skip this)

Four of the 99 were the checker's own false positives, and each one had a *name*:

- **narrative history** — "Tang Wulin: Bluesilver Grass, rank 3" is his Awakening-Day reading, not his rank
  at chapter end. Scope to the block that makes current-value claims.
- **multi-character lines** — `- **Xie Xie:** rank 21 · **Wulin:** rank 15` produced three failures for one
  line until the line was split at the bolded name markers.
- **progression vs constant** — the ledger at ch21 is 71 and at ch62 is 109 and both are correct. Compare
  against *that chapter's* value, and flag only a value that goes **backward**.
- **legitimate historical facts** — *"last known rank 25"* about a character who has left is true and must
  not be "fixed".

> **A check that cries wolf gets ignored, and an ignored check is worse than no check.** Name every false
> positive, exempt it by name in the code with a comment saying why, and only then obey the output.

### The parser corollary

Three separate parsers were silently returning the wrong number, and none of them errored:

- a regex character class missing `*`, so `**281 → 289**` captured `281 → ` and recorded the **start** of
  the chain;
- a `re.search` (first match) where a `re.findall(...)[-1]` (last match) was meant;
- a first-match that landed on a *narrative sentence containing the words* rather than on the stat line,
  and recorded **nothing** — so the previous chapter's value was silently reported as current.

**A parser that returns the wrong value quietly is worse than one that crashes.** Always print the derived
value back and look at it. `state.py --show` exists for exactly this and I had stopped running it.

## 4.14 🔴 THE VOICE LAW — a style drift no mechanics-check can catch

> **Every prose check I had measured mechanics — sentence length, em-dash density, the rate of the
> word "because". A chapter can pass all of them and still be written in a voice that is not the
> book's.** The drift from ch1–3 to ch62 was invisible to ten green layers.

**The user's words:** *"the writeing style of your is very bad you should write like you write Frist
three chapters, you learn everything from them and write like that."*

The first three chapters are third-person, scene-and-dialogue driven, concrete, funny, varied in rhythm.
By ch62 the prose had become a **first-person journal in which the protagonist narrates his own
record-keeping** — and it carried three measurable fingerprints, all at **0** in ch1–3:

| Fingerprint | ch1–3 | ch43–62 (before the fix) |
|---|---|---|
| *"I would like you to notice"* | 0 | **84** (ch60: 14, ch61: 12) |
| record-keeping meta-voice (*"on the record"*, *"I have stopped needing to know"*) | 0 | **41** |
| first-person journal-narration in **bold blocks** | 0 | **100+** |
| *", and that"* chains | 10 per 10.5k words | **294** |

### The fix (and the rule it generalises to)

1. **Fix the disease, not a quota.** The tic, the meta-voice, and the bold journal blocks were excised
   or rewritten across all 62 chapters — **all three now measure 0**. The 8 worst chapters (ch55–62)
   were fully rewritten in the ch1–3 voice; the journal device itself was kept but rendered as *italic
   in-scene text* (what he writes) rather than **bold** (the author emphasising at the reader).
2. **Preserve good prose; rewrite only the broken parts.** ch25 is a strong solo survival scene at 6%
   dialogue. It was *not* rewritten. The framework rule holds: don't destroy what works to look busy.
3. **Encode the voice as a check (`verify_style.py`, Layer 12)** that measures the three fingerprints
   directly and FAILS any new chapter that regresses.

### 🔴 The recalibration lesson — a check that cries wolf is worse than no check

The first version of Layer 12 flagged **21 chapters** on two *proxy* signals, and both were wrong:

- **dialogue-share < 17%** fired on ch25 (6%) — a solo scene with nobody to talk to. Low dialogue is
  not the disease; *journal-voice* is. **Downgraded to informational.**
- **raw bold count > 30** fired on ch40/44/49 — but 160 of 212 long-bold spans were legitimate: canon
  dialogue (*"My name is Wu Zhangkong…"*), recorded data (*"Fist: 2,612 kg"*), aphorisms. **Replaced
  with a precise signal: a bold span that is long + first-person + not a data readout + not dialogue
  + occupies its whole line.** That is the journal-block fingerprint, and nothing else.

> **The general rule:** when a check fires, first ask *is this the disease, or a proxy that happens to
> correlate?* A proxy threshold drawn from three atypical chapters (ch1–3 are dialogue-heavy intro
> chapters) will flag good prose. **Measure the actual fingerprint.** A recalibrated check that finds
> the 2 real remaining instances beats a noisy one that finds 21 things a human will learn to ignore.

This is §4.8 (*calibrate a threshold before you obey it*) applied to a *style* check rather than a
number — the failure mode is identical, and so is the discipline.

## 5. CANON INGESTION

Use `canon_extract/ingest.py`. It takes a PDF and reports NEW / CHANGED / UNCHANGED / MISSING chapters.

```bash
pip install pypdf          # does NOT persist between sessions — reinstall each time
python3 canon_extract/ingest.py <pdf> --out canon_extract/chapters
```

**Canon sourcing rules:**
- **NEVER fabricate a URL.** Only text you actually hold is canon. (This project invented proxy URLs ~8 times;
  every one failed.)
- **A wiki is not canon.** If it isn't in the chapter text, it doesn't enter the story.
- **Chapter numbers differ between sites.** The TITLE is the reliable key.
- **Read the report before writing anything.**

---

## 6. ⚠️ THE FIVE MIS-MEASUREMENTS — the most important section in this file

This project logged five things as "missing" that were already present:

| # | Claimed missing | Reality |
|---|---|---|
| 1 | numbers were "footer-only" | they were spelled out in prose |
| 2 | the canon strength table was present | it was in headers only |
| 3 | a whole power system was "unused" | present in 9 chapters |
| 4 | a character's entrance was "missing" | the fight was there; only the arrival was absent |
| 5 | a canon growth mechanic was "never applied" | fully present, and used as a plot engine |

**The single cause: searching for the words you expect instead of looking for the thing.**

**Countermeasures, all mandatory:**
1. **Scan for the CONCEPT across all chapters, not one keyword.** Try three phrasings minimum.
2. **Check prose, headers and footers separately** — they are different things and get counted differently.
3. **Numbers may be spelled out.** Grep for `two hundred and forty-three` as well as `243`.
4. **Before logging a defect, try to disprove it.** Spend one call proving yourself wrong.
5. **A checker can prove false presence. It cannot prove false absence.** Only re-reading can.

---

## 7. THE CORRECTION DISCIPLINE

The user's most repeated complaint: *"you correct mistakes and make centre and too much and ignore past."*

**A correction is a fix to apply, not a new centre of gravity.** When told X is wrong:
1. Fix X.
2. **Re-run the full suite** — the fix usually breaks something adjacent.
3. Update every file that records X (codex, status, plan, inventory, mirror).
4. **Do not drop the other laws while doing it.**

Also: **say what was wrong.** Name the specific claim that failed and why. Defensiveness and silent repair both
cost the user another round trip.

---

## 8. 🔴 PER-CHAPTER WORKFLOW — "UPDATE EVERYTHING, EVERY TIME" (user standing directive, 2026-08-29)

> The user's words: *"update everything New please update everytime."*
> Steps 7 and 8 of the old version said *"update the status file"* and *"mirror the codex"* and **neither
> was enforced**, so the codex's Quick Reference sat **38 chapters stale** directly under a freshly
> updated table, the reference mirrors fell 51 lines behind, and the master index still reported a
> spiritual power that had been retired nine chapters earlier. **An unenforced step in a checklist is not
> a step. It is a hope.** Every step below now has a command that fails if it was skipped.

**BEFORE writing**

1. Read the canon for the era. If you don't have it, **stop and say so.**
2. Read the previous chapter **in full** — not a grep.
3. `python3 CODEX/consequence.py brief` — what is owed, what is open, what must follow.
4. `python3 checks/state.py --show` — **look at the derived numbers.** Do not trust your memory of them.

**WRITING**

5. Identify what the canon beat looks like **because he is standing in it.** If the answer is "the same,"
   the beat has not been adapted (§THE BUTTERFLY LAW).
6. **Preserve good prose.** Rewrite the broken parts; don't destroy what works to look busy.
7. Write.

**AFTER writing — the whole list, every time, in this order**

8. **The footer.** Rank / spiritual power / hawk / ledger / smith rank / rings, in *both* the
   `Character Progression` and `Character States` blocks, and in the `## GROWTH` header.
   → *enforced by Layer 11.*
9. **`checks/ensemble_schedule.py`** — add the chapter. If a canon character's number moves, move it
   **at the source**, never in a chapter. If a canon superlative is quoted, **scope him out of it.**
   → *enforced by Layers 4, 10 and 11.*
10. **`THE_CODEX.md`** — four places, not one:
    - the `CURRENT STATE` marker in the Quick Reference;
    - the **POWER SNAPSHOT table** (it is headed *"audit EVERY chapter"* — it was 32 chapters stale);
    - the **Current Ranks / Current Timeline** block (it was 38 chapters stale);
    - a **per-chapter record** (`**Chapter N: Title (WRITTEN — adapts canon ch X)**`).
    → *enforced by Layer 5.*
11. **`CHARACTER_STATS.md`** — any new canon fact, with its citation.
12. **`RELATIONSHIPS.md`** — the title line (*END OF CHAPTER N*) **and** the relevant relationship table.
13. **`PROBLEM_INVENTORY.md`** — what this chapter closed, what it opened. Nothing gets dropped until
    verified fixed.
14. **`CODEX/DECISION_JOURNAL.md`** — every AU divergence from canon, **with its reason and its cost.**
15. **`CODEX/CONSEQUENCE_REGISTRY.md`** — `consequence.py premise --id P0NN ...` for every new fact that
    has mechanical consequences. **A fact without a registered consequence is how ch40's purple rings
    went 21 chapters without upgrading the soul skills.**
16. **`CODEX/00_MASTER_INDEX.md`** — chapter count, word count, canon count, current state, owed list.
17. **The live-state markers** in `LIN_HAO_PANELS.md`, `POWER_MODEL.md`, `CANON_*_DOSSIER.md`.
    → *enforced by Layer 5's live-marker scan across every working document.*

**THEN**

18. `sh checks/run_all.sh` — **thirteen layers, must exit 0.** It regenerates `state.json`,
    `LIN_HAO_STATUS.md`, `CONTINUATION_PROMPT.md`, the ensemble footer blocks, and **syncs all five
    CODEX mirrors.**
19. If a check reports something you believe is a false positive: **name it, exempt it in the code with a
    comment saying why, and only then obey the output** (§4.8). Never delete the check.
20. If a belief changed this chapter: **change the check that enforces the old belief in the same edit**
    (§4.13 rule 3). Otherwise the mistake is immortal.

---

## 9. WHAT "DONE" MEANS

- **`sh checks/run_all.sh` exits 0 — all thirteen layers.** Layer 11 diffs the hand-written
  footers against the derived state and is the one that catches what the others structurally cannot.
- `state.py --show` prints numbers you have **looked at**, and they match `POWER_MODEL.md`.
- **Every mirror is identical.** Five files, checked by name.
- **No live-state marker anywhere says a chapter number lower than the current one.**
- Every problem closed has the chapter named that closed it.
- Every new canon divergence is in `DECISION_JOURNAL.md` with its reason **and its cost.**
- Every new fact with consequences is a registered premise, and `consequence.py check` is green.
- No character has silently vanished (`audit.py` §9 measures presence density).
- No header claims something false about canon (`verify_canon_quotes.py` — 57/57).
- The tracker's open count is **measured**, not remembered.
