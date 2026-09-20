# 07 — PROSE LAW

Language, registers, panel discipline, filenames. The craft-level rules that make a serial
readable in sequence rather than one chapter at a time.

---

## 1. LANGUAGE LAW

**English only. Zero non-ASCII characters in any file — prose, panels, ledgers, notes.**

Names are written in pinyin: A Yin, Tang San, Lan Xuanyu, Spirit Hall. Never in characters.

This is not stylistic. It is a portability law: files that contain mixed scripts break on
transfer, render incorrectly in viewers, and fail automated checks. It also forces the
discipline of naming things once, consistently, in the glossary.

Two related artifacts to never emit:

- **Literal backslash-n sequences.** Never write that two-character escape sequence
  anywhere — including in rules *about* it, which is how it keeps coming back. Express it in
  a verification script as `chr(92) + 'n'`.
- **Placeholder or template text** left in a shipped file.

---

## 2. THE FIVE REGISTERS

Fifteen chapters in one register is unreadable however good each chapter is. Every chapter
uses **at least three** of these:

| Register | What it is | Example use |
|---|---|---|
| **Close sense** | Immediate physical experience, inside a body or a place | The pressure of a beast's cultivation through the ground |
| **Hard scene** | Real-time action with consequence | A fight, a hunt, an escape, a measurement |
| **Dialogue** | Spoken exchange between named characters | An antagonist explaining what they want |
| **Other POV** | A scene from someone else's eyes, usually in italics | The hunter's report; the clerk reading a file |
| **Lyrical** | Elevated, reflective, time-compressed | The long view; what the years did |

The **dialogue** register is the one that goes missing, because interior protagonists don't
talk and introspective prose is easier to write. Its absence is detectable and fatal: a
serial with no spoken exchange has no faces, and a serial with no faces has no opposition.

**Hard gate: every chapter carries at least three spoken dialogue lines.** If your
protagonist cannot speak, give the chapter to someone who can. An antagonist with lines is
worth more than a protagonist with thoughts.

---

## 3. PANEL DISCIPLINE

**Slim panel at the top. No footer.**

The panel carries only what a reader needs to orient:

```
◆ STATUS — Chapter N: <year range>
KIND      : <what the protagonist is, right now>
AGE       : <age>
CLASS     : <rank / tier, and what just opened>
THREAT    : <this chapter's opposition>
BOND      : <only if the chapter turns on a relationship>
LOSS      : <only if something ends>
LAW       : <only if a rule is established or tested>
```

That is it. Not eleven fields. The bookkeeping — position, canon touched, world changes,
wires left open, doctrine exercised — lives in the kit, in `SERIAL_LOG.md`, where a reader
never sees it.

**A footer in the chapter file is apparatus outgrowing story.** It is failure mode five and
it is revoked.

---

## 4. THE NUMBER LAW

```
PANELS and LEDGERS  → exact figures permitted
PROSE               → round felt counts, in words, spoken or thought by characters
```

A character thinks *he had lived a long time*. The ledger says 743.

Prose carries **no digits at all**. Not years, not ranks, not distances. This is a hard gate
and it is machine-checked. It forces the prose to express magnitude as experience rather
than as bookkeeping, which is the difference between a story and a spreadsheet.

The single exception: a number a character literally reads off a document or a device, in
dialogue or quoted text, may appear — but it must be in words, and it must be justified as
something being read.

---

## 5. VOICE LAW

Lock these in setup and never drift:

- **POV** — whose head are we in? Can it change? How is a change marked?
- **Tense** — past or present, and never both.
- **Person** — first or third.
- **Register floor** — see §2.

A POV change that isn't marked is a continuity error the reader feels before they can name
it. Mark it with a break, a heading, or a clear shift in the first sentence.

---

## 6. THE FULL-PLAY LAW

Every element justifies the narrative space it consumes.

**Never:**
- thin hinge chapters that only move the cast somewhere
- copy-machine rooms — the same scene type repeated with different nouns
- kit-recap presented as story
- audits presented as story
- a chapter whose only content is interior meditation

**Always:**
- play full — use the kit, the cast, the consequences
- a named job finishes in the turn it is given
- if a character is introduced, they want something in the scene they arrive in

---

## 7. FILENAME LAW

```
ASCII letters, digits, underscores, dots. Nothing else.
No spaces. No special characters. No non-ASCII.
```

`Chapter_07_The_Teeth_in_the_Grass.md` — yes.
`Chapter 7 — The Teeth in the Grass.md` — no.

Upload-safe names survive transfer between agents, platforms and archives. Pretty names get
mangled, and a mangled filename in a handoff is a lost file.

---

## 8. THE PROSE AUDIT

Before shipping:

```
- Zero non-ASCII characters
- Zero literal backslash-n sequences
- Zero digits in prose
- At least three spoken dialogue lines
- At least three of the five registers present
- No template or placeholder text
- The chapter has a turn: something is true at the end that was not true at the start
```

All of these except the last are machine-checked by `tools/verify.py`. The last one is yours
to answer honestly.

---

## 9. HOUSE GRAMMAR (measured standard, 2026-09-20)

Drawn from published Soul Land fanfiction read directly and from the corpus of
this workspace (every project measured: average sentence 19-30 words, dialogue
10-20 spoken lines per thousand words). A chapter that sits outside this band
does not read like the fandom and will be rejected by the author regardless of
its facts.

- **Sentence average <= 25 words; no sentence over 60; the median near 15.**
- **Dialogue >= 8-10 spoken lines per thousand words** in any chapter that has
  people in it. Exposition is delivered in speech, by named characters with
  wants, the way canon and the fandom both do it.
- **Open inside a scene** (a body doing something, or a voice speaking).
- **Several small finished scenes** per chapter, at least one in real time.
- **Plain concrete nouns.** Motif words are texture, never the sentence engine.
- **End on a hook**: a decision, an arrival, a threat, a name.
