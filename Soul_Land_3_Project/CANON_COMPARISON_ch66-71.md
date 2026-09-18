# CANON COMPARISON — what I wrote vs what canon actually says

**Made 2026-08-30.** User instruction: *"just go and read canon chapter's and comper with what you write."*

Method: I read **canon 288, 289, 291, 295, 302, 303, 304, 305, 306, 307, 240, 260, 168, 596** in full —
not the six lines I had previously extracted from each. Then I compared them against **our chapters 66–71**
(the Shrek working-student arc), which is the range those chapters cover.

---

## 1. WHAT WAS RIGHT

**Every quotation is verbatim and correctly attributed.** I re-ran a word-for-word match of all **30 canon
quotes in the headers of ch66–71** against the 407-chapter corpus plus the frozen quote-source file:

```
ch66-71 header quotes: 30 checked · 30 verified against canon · 0 not found
```

🔴 **A correction to this report's own first draft, because I nearly published the same disease I was hunting.**
I first wrote that all 30 were verbatim and that the single apparent failure was a bug in my audit script.
**It was not a script bug.** ch71's header read *"is able to contain more powerful soul rings and spirit
souls"* — but canon 168's sentence is:

> *"With stronger bodies, **they are** able to contain more powerful soul rings and spirit souls, but this
> isn't done normally."*

The subject and verb had been changed, so a **close paraphrase was sitting inside quotation marks as a
verbatim pull** — substantively correct, correctly attributed, and still not the words. **ch71's header and
Canon Anchors have been corrected to the real sentence**, and the audit re-run afterwards returns:

```
FINAL: ch66-71 header quotes: 30 checked · 30 verbatim · 0 not found
```

The mechanics I built on are also right: the contribution-point economy, the attendance rule (*"anyone who is
absent three times will face expulsion"*, c295), the seven representatives and their stipends
(*"president 1,000 · vice-president 600 · profession council 500"*, c305), the working-student thousand-refining
gap (*"a minimum of two thousand contribution points"* vs the job's 1,000, c302), the Elder Feng precedent
(c302), and what the spirit ascension platform actually is (c240).

---

## 2. 🔴 WHAT I GOT WRONG — four separate facts, all published

### 2.1 The Fallen Angel is NOT Gu Yue. I invented that.

Canon 303–304 gave me a real line — *"How could a Fallen Angel soul master not be an evil soul master?"* —
and I attached it to **Gu Yue**. Canon's target is a different person entirely:

> *"They never expected that this **Fallen Angel girl with two rings** would be a working student like them."*
> *"the image of that **red-haired** Fallen Angel girl popped into his head."*

And Gu Yue's canon power set is not a Fallen Angel at all:

> *"not only could she wield **six different elements**… With **fire, water, wind, earth, light, space, and the
> variant ice attribute**, nothing was impossible for her. She was the first soul master in history to wield so
> many elements."* — c289

Canon **never** says the Fallen Angel is Gu Yue. The enforcer's line I also borrowed —
*"The Academy has already verified my identity and determined that I am not an evil soul master"* — belongs to
the **Fallen Angel girl**, not to Gu Yue.

**Fixed:** ch71's prose now has Xu Xiaoyan say the truth (*"That's not Gu Yue… Gu Yue has six elements and a bad
attitude and no red hair"*), and the AU is labelled where it is actually mine: **Yue Zhengyu has *decided* the
girl he means is Gu Yue.** Corrected in ch70, ch71, `CHARACTER_STATS.md` §2.7, and the codex record. Logged as
**D033**.

### 2.2 Yue Zhengyu is second grade, not a first-year

> *"Honorable enforcer, I am the Angel Clan's Yue Zhengyu, **a student from the second grade's class one**."* — c291

I wrote him as a peer. **Fixed** in `CHARACTER_STATS.md` and ch71.

### 2.3 "Yuanen Yehui" is not his name at c302

In canon 302–304 he is only ever **"Yuanen."** His full name does not appear until **c327**, where it is a
*reveal* — *"So her full name is actually Yuanen Yehui."* I cited *"Yuanen Yehui … canon c302"* in ch70's footer.
The lines I quoted from c302 are all correct; **the name attached to them was 25 chapters premature.**
**Fixed** in `CHARACTER_STATS.md` and the codex record.

*(I also nearly made a worse error here: canon 327's pronouns are female and canon 302–304's are male. I checked
both before writing anything down. The c327 passage is a different narrative thread; in c302–304, which is what
we adapt, he is unambiguously male.)*

### 2.4 Elder Feng and Feng Wuyu are the same person

Canon says so itself:

> *"It's a pun on Elder Feng. Elder Feng is 枫 老 (Feng Lao) while Mad Elder is 疯 老 (also Feng Lao)."*

I had them as two entries. **He is also the man who personally recruited Tang Wulin and gave him the badge**
(*"You're pretty lucky to have Elder Feng personally recruit you"*). **Fixed.**

---

## 3. 🔴 THE BIG ONE — our timeline is ~2 years compressed against canon, and it was never recorded

Canon states Wulin's age at Shrek three times:

> *"Tang Wulin, **at the young age of thirteen**, stood **165 centimeters tall** and was only a head shorter
> than an adult."* — c305
> *"that's right, **I'm only thirteen years old right now!** You can't expect everyone at my age to have three
> soul rings."*
> *"he was coincidently able to harness the power of the Golden Dragon King to spirit refine **at thirteen
> years old**."*

**Our story has him at 10–11 at Shrek, and Lin Hao at 11.**

🔴 **The worst part: we already knew.** `CANON_ACCESS.md` line 774 says, in our own words:

> *"The destination is Shrek Academy, reached around canon ch 291, **at age thirteen**, via a
> once-every-three-year entrance exam."*

That fact was written down and **nothing compared it to 71 chapters of prose.** This is the same defect class
as **D030** (a canon number in one file, contradicted by the story, no check between them) — but a whole
timeline instead of one rank.

**Decision (D032):** the prose wins — 71 chapters cannot be retro-aged. So the divergence is now **recorded and
load-bearing**: our AU runs ~2 years compressed, and **every future canon comparison must convert ages through
the offset instead of reading them across.** Recorded as **K11**.

---

## 4. 🔴 WHAT I MISSED ENTIRELY — the texture of the arc

Reading the chapters instead of the quotes turned up a whole layer of the working-student arc that our ch66–71
does not have at all:

| Canon | What it says | In our story? |
|---|---|---|
| **c288** | The dormitory is **one run-down 30 m² room**, *"It's basically a slum compared to the school building"*, **two metal bunk frames, no walls between the boys and the girls**, one cold-water faucet for the whole building, dust on the floor, two broken windows | ❌ Missing |
| **c288–289** | Their **assigned arrival job is cleaning Spirit Ice Plaza.** Gu Yue does it with a water-and-wind whirlwind — *"it still took her until noon, a total of **four and a half hours**… half were simply spent recovering her soul power"* | ❌ Missing |
| **c289** | *"They had received **one hundred Shrek contribution points each**… but it was then that Tang Wulin discovered that **one hundred points was only enough to feed them for one day**."* | ❌ Missing |
| **c295** | **Elder Cai** — 🔴 **female**, *"Shen Yi replaced **her** at the lectern"* — is the usual lecturer and is **absent as usual**, which is the *reason* Shen Yi runs the class. She also gives the opening speech: outer court only until **thirty-five** | ❌ Missing |
| **c306** | **Elder Feng personally recruited Tang Wulin** and gave him the badge | ❌ Missing |
| **c288–289** | **Student number two** — a frail-looking boy, a **three-ring power-type**, who *"had beaten Xie Xie in the entrance exam with explosive power"* and *"Even Gu Yue's chances of defeating him were slim."* He is a **working student** too | ❌ Missing |
| **c303–304** | **The red-haired Fallen Angel girl with two rings**, also a working student — the actual target of Yue Zhengyu's campaign | ❌ Missing (and misassigned to Gu Yue) |

Recorded as **K10**.

Note what this costs: the working-student arc in canon is **about scarcity** — one room, one faucet, 100 points,
one day of food, a slum hidden in a forest *"to hide the building and save face for the academy."* Our version
has the economics right and the **poverty** missing, which is the part that makes the economics mean anything.

---

## 5. WHY THE CHECKS DID NOT CATCH ANY OF IT

This is the part that matters more than the list.

| Check | What it can prove | What it cannot |
|---|---|---|
| **Layer 7** `verify_canon_quotes` | that a quoted line **exists** in canon | **that it belongs to the character we gave it to** |
| **Layer 3** `audit.py` | that a fact in ch4 is still true in ch71 | that a fact matches **canon** |
| **Layer 4** `verify_ensemble` | that ensemble ranks follow the schedule | that the schedule matches **canon's ages** |

**A verbatim quote attached to the wrong character is worse than a paraphrase**, because the check passes and
the reader is lied to. Layer 7 scored 85/85 while fact 2.1 was false in four documents.

So the fix is not a new check — it is a rule, logged as **D033**:

> 🔴 **READING A QUOTE IS NOT READING A CHAPTER.** A quote is a point; a chapter is a scene. Before any chapter
> that adapts a canon range, read the chapters **in full** and write down the *scene*, not just the *lines*.

---

## 6. WHAT I CHANGED

| File | Change |
|---|---|
| `chapters/chapter_71.md` | Yue Zhengyu scene rewritten to canon: second grade, hunting the **red-haired Fallen Angel girl**; Gu Yue is his mistaken target, labelled AU |
| `chapters/chapter_70.md` | footer corrected |
| `CHARACTER_STATS.md` §2.7 | Fallen Angel girl added as her own entry with the c289 element list; Yue Zhengyu's grade fixed; Yuanen's naming dated; **Elder Feng = Feng Wuyu** merged; **Elder Cai** added (female) |
| `THE_CODEX.md` | ch71 record corrected with the retraction written out in full |
| `CODEX/DECISION_JOURNAL.md` | **D032** (the two-year compression) · **D033** (the canon-comparison rule) |
| `PROBLEM_INVENTORY.md` | **K2 closed** (the arc is written) · **K9, K10, K11** opened |

**Verification after all of it:** `sh checks/run_all.sh` → **exit 0, all thirteen layers.** 85/85 canon quotes.
0 footer contradictions. Timeline 71/71.
