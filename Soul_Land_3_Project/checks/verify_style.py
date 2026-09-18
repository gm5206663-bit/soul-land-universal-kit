#!/usr/bin/env python3
"""LAYER 12 — THE VOICE. The prose must sound like chapters 1–3.

WHY THIS EXISTS. Measured 2026-08-29, after the user said: *"the writeing style of your is very bad
you should write like you write Frist three chapters."*

Chapters 1–3 are third-person, scene-and-dialogue driven, funny, concrete, and varied in rhythm.
From ch43 onward the prose slid into a different thing entirely: a first-person journal in which the
protagonist narrates his own record-keeping. The numbers:

    "I would like you to notice"   ch1-3: 0     ch43-62: 84   (ch60: 14, ch61: 12)
    ", and that" chains            ch1-3: 10    ch43-62: 294  (ch59: 27, ch60: 32, ch61: 32)
    record-keeping meta-voice      ch1-3: 0     ch4-62:  41   (ch61: 10)
    dialogue share                 ch1-3: 25-35%            ch55: 13%

Nothing caught any of it, because every existing prose check measures MECHANICS — sentence length,
em-dash density, the rate of the word "because". A chapter can pass all of those and still be
written in a voice that is not the book's. So this layer measures the voice.

THE LAW (THE_CODEX.md §THE VOICE LAW)
  1. Third person, close on Lin Hao. He does not narrate to a reader.
  2. Scene and dialogue carry it. If two people are in a room, they talk.
  3. No journal tics. No "I would like you to notice", no "on the record", no "this is also a fact".
  4. His inner life is SHOWN — a decision, a physical beat, a line of dialogue, a thing he does
     with his hands. Not summarised at the reader.
  5. Sentences vary. Short ones do the heavy lifting.
  6. Bold in prose is for a term, not for emphasis. Journal-style bolded paragraphs are forbidden.

FAILS on any chapter at or after VOICE_LAW_FROM (a new chapter must not regress).
WARNS below it (the back-catalogue debt is real and is tracked in PROBLEM_INVENTORY K9).

Usage:  python3 checks/verify_style.py [--strict]
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
strict = "--strict" in sys.argv

# 🔴 ch62 is the first chapter written under the law. Everything before it is inherited debt.
VOICE_LAW_FROM = 62

# ---- the baseline, measured from chapters 1–3 on 2026-08-29 ----
BASELINE = {
    "dialogue_pct": (25.0, 35.5),   # ch2 35.5 / ch1,ch3 25.0
    "median_sentence": (9, 11),     # ch3 9, ch2 10, ch1 11
    "and_that_per_1k": 2.8,         # 10 chains across 10,516 words
}
# a small tolerance over baseline — the law is "sound like ch1-3", not "be ch1-3"
TOL = {"dialogue_pct": 8.0, "median_sentence": 6, "and_that_per_1k": 6.0}

TIC = re.compile(r"I would like (?:you |him |her |them )?to notice", re.I)
META = re.compile(r"\bon the record\b|\bI have written\b|\bthis is also a fact\b|"
                  r"\bwriting it (?:four|five|six|seven) times\b|\bI have stopped needing\b", re.I)
CHAIN = re.compile(r", and that ")
BOLD = re.compile(r"\*\*[^*\n]{4,}\*\*")
SENT_SPLIT = re.compile(r'(?<=[.!?])\s+')

# 🔴 RECALIBRATED 2026-08-29 (the "calibrate before you obey" rule). The first version of this
# layer counted RAW bold spans and flagged dialogue-share against a baseline drawn from THREE
# atypical intro chapters. Both cried wolf, and a check that cries wolf gets ignored:
#   • raw bold > 30 fired on ch40/44/49, but 160 of 212 long-bold spans are LEGITIMATE —
#     canon dialogue ("My name is Wu Zhangkong…"), recorded data ("Fist: 2,612 kg"), aphorisms
#     ("The greater the pressure…"). Bold is not the disease; bold JOURNAL-NARRATION is.
#   • dialogue < 17% fired on ch25, a strong SOLO forest-survival scene with nobody to talk to.
# So the real signal is measured directly below: a bold span that is (a) long, (b) first-person,
# (c) not a data readout, (d) not dialogue. That is the journal-voice fingerprint, and after the
# 2026-08-29 pass it is at 2 corpus-wide (both Wu Zhangkong dialogue the regex mislabels).
FIRST_PERSON = re.compile(r"\b(?:I|I've|I'd|I'm|my|me)\b")
DATA_READOUT = re.compile(r"(kg|coins?|rank|left|right|years?|rings?|:\s|\d)")
SPEECH_LEAD = re.compile(r'(\bsaid\b|\bsays\b|\basked\b|\btold\b|["“]\s*$|:\s*$)', re.I)


def journal_voice_bold(p):
    """Count bold spans that are first-person journal narration — the actual disease, not bold
    term-emphasis or bold dialogue. Returns (count, samples).

    🔴 CALIBRATED 2026-08-29, second pass. The first version flagged ch9 and ch33, but both are
    bold emphasis INSIDE a Wu Zhangkong dialogue line ("Remember this. **You are my students…**"),
    not journal narration. The discriminator: a journal-narration bold block IS (essentially) the
    whole line — that is how the journal is typeset. Bold dialogue emphasis sits embedded in a
    larger paragraph with surrounding non-bold text. So only count a bold span that occupies the
    whole of its line."""
    hits = []
    for line in p.split("\n"):
        stripped = line.strip()
        # the whole line is one bold span (allowing trailing/leading whitespace) = a journal block
        m = re.fullmatch(r"\*\*([^*].*?)\*\*", stripped)
        if not m:
            continue
        inner = m.group(1).strip()
        if len(inner.split()) < 8:
            continue
        if inner.startswith(('"', "“")):            # a fully-bold quoted line = shouted dialogue
            continue
        if not FIRST_PERSON.search(inner):           # not the protagonist's voice
            continue
        if DATA_READOUT.search(inner):               # a recorded number/fact, legitimately bold
            continue
        hits.append(inner[:55])
    return len(hits), hits


def prose_of(path):
    """The story body only: after the header block, before the footer."""
    t = open(path, encoding="utf-8", errors="replace").read()
    p = t.split("## End of Chapter")[0]
    if "## Part 1" in p:
        p = p.split("## Part 1", 1)[1]
    return p


def measure(p):
    words = len(p.split())
    dlg = sum(len(m.group(0).split()) for m in re.finditer(r'"[^"\n]{2,400}"', p))
    sents = [s for s in SENT_SPLIT.split(p) if len(s.split()) > 1]
    lens = sorted(len(s.split()) for s in sents)
    return {
        "words": words,
        "dialogue_pct": 100.0 * dlg / max(words, 1),
        "median_sentence": lens[len(lens) // 2] if lens else 0,
        "tics": len(TIC.findall(p)),
        "meta": len(META.findall(p)),
        "and_that_per_1k": 1000.0 * len(CHAIN.findall(p)) / max(words, 1),
        "bold": len(BOLD.findall(p)),
    }


fails, warns = [], []
print("verify_style: the prose must sound like chapters 1-3 (THE VOICE LAW)")

for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    p = prose_of(path)
    m = measure(p)
    jbold, jsamples = journal_voice_bold(p)
    bad = []

    # ---- the real disease signals (these FAIL a new chapter) ----
    if m["tics"]:
        bad.append(f"{m['tics']}× \"I would like you to notice\"")
    if m["meta"]:
        bad.append(f"{m['meta']}× record-keeping meta-voice")
    if m["and_that_per_1k"] > BASELINE["and_that_per_1k"] + TOL["and_that_per_1k"]:
        bad.append(f"{m['and_that_per_1k']:.1f}/1k \", and that\" chains (baseline 2.8)")
    if jbold:
        bad.append(f"{jbold}× first-person journal-narration bold (should be italic in-scene text)")

    if not bad:
        continue
    line = f"ch{n}: " + " · ".join(bad)
    if n >= VOICE_LAW_FROM:
        fails.append(line)
    else:
        warns.append(line)

# ---- informational only: dialogue share and median sentence ----
# 🔴 These are NOT debt. Dialogue share cries wolf on solo/introspective chapters (ch25 is a
# strong solo survival scene at 6%), and median sentence length is a weak proxy for rhythm. They
# are printed so a human can eyeball outliers, but they never fail a chapter and never count as
# debt. The disease is the journal-voice, measured above, not these mechanics.
info = []
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"chapter_(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    m = measure(prose_of(path))
    notes = []
    if m["dialogue_pct"] < 12:
        notes.append(f"dialogue {m['dialogue_pct']:.0f}%")
    if m["median_sentence"] > 18:
        notes.append(f"median sentence {m['median_sentence']}w")
    if notes:
        info.append(f"ch{n}: " + " · ".join(notes))

for w in warns:
    print("  DEBT " + w)
for f in fails:
    print("  FAIL " + f)
for i in info:
    print("  note " + i + "  (informational — solo/introspective chapters legitimately run low)")

print(f"  {len(fails)} chapter(s) at or after ch{VOICE_LAW_FROM} violate THE VOICE LAW · "
      f"{len(warns)} older chapter(s) carry inherited journal-voice debt")
if fails and strict:
    sys.exit(1)
sys.exit(0)
