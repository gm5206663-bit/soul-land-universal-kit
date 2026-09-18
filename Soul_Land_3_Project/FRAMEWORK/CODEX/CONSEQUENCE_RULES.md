# THE CONSEQUENCE RULE LIBRARY

**What this is.** A standing list of *"if X enters the story, Y must follow."* Each rule was earned
by a real failure. When an event happens in a chapter, this library is what stops the consequence from
being discovered twenty chapters later by the reader.

**Why it exists.** Every serious error in this project was the same shape: a fact entered the story and
its mechanical consequence was never followed through.

| The event that entered | The consequence that was missed | Found |
|---|---|---|
| Both rings re-formed **purple** (ch40) | canon: *"if his spirit soul was upgraded, then the soul skills it provided would be upgraded too"* — both soul skills became thousand-year tier | **21 chapters later** |
| Wulin reached **peak rank 15** | canon moves him 15 → 16 → 17 across the same span | **49 chapters later** |
| Lin Hao became a **Soul Elder with three rings** | the ensemble's numbers had to keep moving too | **49 chapters later** |
| The **rank-30 wall opened** (ch40) | every document saying "hard wall" / "88 years to the crossing" became false | **21 chapters later** |

**How to use it.** Before writing a chapter, run `python3 CODEX/consequence.py brief`. It prints every
open premise and the rules that fire on it. After writing, run `check` — it greps the chapters for each
consequence and tells you which ones are still unlanded.

---

## THE RULES

Each rule is: **TRIGGER → CONSEQUENCE**. The `scan` line is a regex the checker uses to look for
evidence that the consequence landed.

### R01 — A RING CHANGES COLOUR
**TRIGGER:** a character's soul ring changes colour (white→yellow→purple→black).
**CONSEQUENCES:**
- **Their soul skills upgrade with it.** Canon: *"if his spirit soul was upgraded, then the soul skills
  it provided would be upgraded too."* A purple ring's skill is a **thousand-year soul skill**, and canon
  treats witnesses seeing one as an event.
- **The new tier must be shown**, not assumed — someone reacts, or the user of it gets a different
  result than they expected.
- **The cost changes too.** A stronger skill is not a free one.
- `scan: (thousand[- ]year (soul )?skill|soul skill.{0,40}(upgrad|evolv|changed|different))`

### R02 — A SPIRIT SOUL CROSSES A THRESHOLD
**TRIGGER:** a spirit soul's age crosses a band boundary (10 / 100 / 1,000 / 10,000 / 100,000).
**CONSEQUENCES:**
- The **rings it produced re-form** in the new colour.
- **R01 fires** for every one of those rings.
- **A new ring may be bestowed.** Canon: a thousand-year spirit soul bestows **up to three** rings.
- Canon: *"A thousand-year spirit soul provides THREE soul skills."* Count them. If the count changes,
  say so.
- **The rank ceiling moves.** `N rings ⇒ ranks N·10+1 … (N+1)·10`. Every document stating the old
  ceiling is now wrong.
- `scan: (rings? re-?form|re-?formed (purple|yellow|black)|bestow|third ring|ceiling (moved|now))`

### R03 — A CHARACTER CROSSES A REALM BOUNDARY
**TRIGGER:** anyone's rank passes 10 / 20 / 30 / 40 / 50 …
**CONSEQUENCES:**
- Their **title changes** (Soul Scholar → Soul Master → Soul Grandmaster → Soul Elder → Soul Ancestor →
  Soul King …). Check every place the old title is used.
- **They may now reach things they could not.** Canon: *"It wasn't until the Soul Elder ranks that this
  type of strength could…"* — a number the lower realm cannot produce.
- **Everyone comparing themselves to them must re-compare.** A rival's whole self-image can be built on
  the gap.
- `scan: (Soul (Scholar|Master|Grandmaster|Elder|Ancestor|King|Emperor|Sage)|realm)`

### R04 — A NEW FACT ENTERS THAT INVALIDATES A STANDING STATEMENT
**TRIGGER:** any event that makes a previously-true sentence false.
**CONSEQUENCES:**
- **Grep every tracking document for the old claim.** Codex, status file, continuation prompt, power
  model, problem inventory. A hand-maintained file that says the old thing is now a lie.
- **Grep the chapters.** Prose that states the old thing in the present tense is a continuity error.
- `scan:` *(set per premise)*

### R05 — A CHARACTER IS ABSENT FOR AN ARC
**TRIGGER:** a named character stops appearing.
**CONSEQUENCES:**
- **Their progression lines must still be decided**, even off-page — or they freeze and the freeze
  becomes visible the moment they return.
- **Someone must notice the absence.** Canon does this constantly.
- **Their return must cost something.** Nobody comes back unchanged.
- `scan:` *(the character's name)*

### R06 — A POWER IS USED FOR THE FIRST TIME ON-PAGE
**TRIGGER:** a locked ability, trump card or technique is finally used.
**CONSEQUENCES:**
- **It must cost something countable** — soul power, body, time, a debt.
- **Witnesses must recalibrate.** The people who ranked him yesterday are wrong today.
- **It cannot be un-used.** Every later chapter knows it exists now.
- `scan:` *(the ability's name)*

### R07 — A NUMBER IS MEASURED IN-WORLD
**TRIGGER:** an instrument produces a number on-page.
**CONSEQUENCES:**
- **It becomes a hard floor.** It may never be under-performed under equal conditions.
- **Every earlier estimate of the same quantity must be reconciled with it.**
- **Comparison targets update.** If canon gives other characters' numbers, state the gap.
- `scan:` *(the number)*

### R08 — A CHARACTER LEAVES OR JOINS A GROUP
**TRIGGER:** roster change.
**CONSEQUENCES:**
- **Recount the group.** Every later line saying "the six of us" / "all five" must be right.
- **The reason must be stated**, and it must be consistent with who they are.
- **Canon may disagree** — if so, record the AU divergence explicitly, in writing, where it can be found.
- `scan: (\b(six|five|four|three|seven) of (us|them)|all (six|five|four))`

### R09 — A PLAN IS CANCELLED
**TRIGGER:** a previously-locked future event is called off.
**CONSEQUENCES:**
- **Nothing may foreshadow it again.** Not in prose, not in a character's speculation, not in a codex
  "future evolution" line.
- **Add a checker** that fails if the cancelled thing's name reappears.
- `scan:` *(the cancelled thing's name — as a FAIL, not a search)*

### R10 — A USER CORRECTION ARRIVES
**TRIGGER:** the user says something is wrong.
**CONSEQUENCES:**
- **Fix the thing. Do not re-centre on it.** The correction is a fix to apply, not a new centre of
  gravity. Everything else still has to be true.
- **Find the root, not the symptom.** Ask *"what class of mistake is this?"* and check whether the same
  class exists elsewhere. It usually does, several times.
- **Write a check** that would have caught it. If a mistake was found by reading, the next one will be
  too — and reading does not scale to 61 chapters.
- **Say what was wrong, in a sentence, without defending it.**
- `scan:` n/a — this one is a process rule

---

## THE THREE QUESTIONS (run these before and after every chapter)

**Before writing:**
1. **What changed since the last chapter?** List it. Not what I *plan* to change — what already did.
2. **Which rules in this library fire on those changes?** Run the tool; don't rely on remembering.
3. **What does the reader now know that the characters don't — and vice versa?** Both directions matter.

**After writing:**
1. **Did every fired consequence land on-page, or get an explicit decision not to?** Silence is not a
   decision.
2. **Does any tracking document now say something false?** Grep, don't recall.
3. **What did I decide that isn't written down anywhere?** Write it in the decision journal, or it will
   be re-decided differently later.
