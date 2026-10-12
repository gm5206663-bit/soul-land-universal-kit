#!/usr/bin/env python3
"""tools/style_gate.py — THE VOICE LAW, MACHINE-ENFORCED.

`verify.py` is the kit's portability gate. It checks that a chapter is uploadable: no CJK, no
digits in prose, three dialogue lines, one marker, a book-end card if there is one. It PASSES
a chapter that is a 3,000-word interior monologue with 5% dialogue and a fifty-line footer.

That is not a bug in verify.py. It is a floor. This file is the wall above it.

Everything here is derived by measurement from the author's own live serials, not from taste:

  SOURCE                                   words   dlg lines   dlg%   median sent
  SL3 Lin Hao ch1   (the named voice bar)  5,389       122    20.6%      11
  SL3 Lin Hao ch2                          4,032       111    26.8%       9
  SL3 Lin Hao ch3                          4,752        85    21.0%       9
  SL3 Lin Hao ch75  (author's quality bar) 4,891       138    31.0%       7
  SL3 Lin Hao ch101 (newest)               2,683        72    32.1%      12
  SL4 Fire Phoenix ch31                    8,194       212    21.0%       8
  Blue Silver rebuilt ch1 (plant POV)      2,723        18     2.7%      10
  Blue Silver REJECTED ch1 (do not write)  4,627         0     0.0%       —

Doctrines enforced:
  THE VOICE LAW  (SL3 CODEX, LOCKED v3.10, from the author's own correction:
                  "the writeing style of your is very bad you should write like you write
                  Frist three chapters")
  STYLE_GOLD     (SL3, 102 lines — the dialogue dial, the cliff rotation, the motif law)
  PROSE LAW      (kit 07 — slim panel, no footer, the marker law, the number law)
  STORY LAW      (kit 03 — failure 2 "nothing contested", failure 4 "one register",
                  failure 5 "apparatus outgrew the story")
  THE SPECTATOR TEST (SL3: the protagonist is never a watcher across a whole chapter)

SCOPE: this gate is written for THIS serial — a named human protagonist, no chapter footers,
pinyin-only text. Running it over the author's other projects produces deliberate false
positives, and each one is informative:
  · blue_silver/chapters_rebuilt/  — a plant POV with no name and no dialogue for most of
    each chapter. Scores 2.7% dialogue and 0 spoken turns. Legal there, illegal here.
  · reference/sl3_lin_hao/          — chapters carry a "## End of Chapter" footer block, which
    inflates the sentence counts. The gate has no footer to strip because this project has none.
  · sl4_fire_phoenix/               — other-POV chapters. Handled: declare `POV : Other` in the
    panel and the Spectator Test steps aside.
Red-tested 2026-09-19 against that corpus. It caught SL3 ch60 on the banned tic "I would like
you to notice" — the exact drift the SL3 CODEX documents as firing 14 times in that chapter.

A chapter must DECLARE its dialogue load in the panel, because the load is a dial chosen per
chapter, not a default: `DIALOGUE  : lesson 44-66%` / `standard 13-30%` / `hush 8-15%`.
Undeclared chapters are measured against `standard` and warned.

Run:  python3 tools/style_gate.py chapters/*.md
Exit: 0 clean · 1 failures · 2 warnings only
"""
import re
import sys
import pathlib
import statistics

MARKER = "\u25c6"

# ── THE VOICE LAW §3 — journal tics, forbidden outright ────────────────────────
TICS = [
    "i would like you to notice", "on the record", "this is also a fact",
    "i have stopped needing to know", "i have written that sentence",
]
# ── SL3 L10 — the author's meta-teaching pasted into a character's mouth ───────
DOCTRINE_IN_A_MOUTH = ["no law anywhere", "whole existence", "the main engine"]
# ── SL3 zero_tolerance.py §2 — the banned abstract-cliff register ──────────────
ABSTRACT_CLIFF = [
    "everything was about to change", "nothing would ever be the same",
    "little did they know", "everything would never be the same",
]
# ── Lock 11 — the house spelling. Canon_002 §5 is one word. ────────────────────
SPELLING = re.compile(r"[Bb]lue\s+[Ss]ilver")

CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")

DIALS = {"lesson": (44.0, 66.0), "standard": (13.0, 30.0), "hush": (8.0, 15.0)}

# Watch-verbs vs act-verbs. The Spectator Test, coarse but honest.
WATCH = re.compile(
    r"\b(watch(?:ed|es|ing)?|observ(?:ed|es|ing)|notic(?:ed|es|ing)|"
    r"look(?:ed|s|ing)?\s+(?:at|on|toward|towards)|saw|sees|gaze[ds]?|stared|studied)\b", re.I)
ACT = re.compile(
    r"\b(said|asked|told|answered|replied|took|gave|put|walked|ran|stepped|picked|"
    r"wrote|made|built|pulled|pushed|turned|held|carried|reached|offered|chose|decided|"
    r"negotiat\w+|argued|laughed|cooked|fed|threw|caught|paid|bought|sold)\b", re.I)


def split_prose(text):
    """Return (prose, panel_block, extra_blocks). Fences are apparatus; prose is outside them."""
    blocks, spans = [], []
    for m in re.finditer(r"```.*?```", text, flags=re.S):
        blocks.append(m.group(0))
        spans.append(m.span())
    prose = text
    for a, b in reversed(spans):
        prose = prose[:a] + prose[b:]
    prose = re.sub(r"^#{1,6}.*$", "", prose, flags=re.M)
    prose = prose.replace("---", " ")
    return prose.strip(), (blocks[0] if blocks else ""), (blocks[1:] if len(blocks) > 1 else [])


def sentences(prose):
    flat = re.sub(r"\*", "", prose)
    out = [s for s in re.split(r"(?<=[.!?])\s+", flat) if len(s.split()) > 1]
    return out


STOP = {"Chapter", "Status", "Kind", "Age", "Class", "Threat", "Bond", "Law", "Loss",
        "Dialogue", "Turn", "The", "And", "But", "Then", "That", "This", "He", "She", "It",
        "There", "Not", "What", "When", "Where", "Which", "Who", "Because", "After", "Before",
        "Yes", "No", "Well", "So", "If", "Of", "In", "On", "At", "To", "A", "I", "My", "Your",
        "His", "Her", "Its", "Their", "Our", "You", "Me", "Him", "Them", "Us", "We"}


def protagonist(text):
    """The POV name. Two-word proper nouns first (Lan Shen), then one-word (Wulin).

    Scores on the whole chapter, not the opening, because the opening is often another
    character's beat. Ties break toward the two-word form, which is the house convention
    for a full name on first and formal use.
    """
    from collections import Counter
    body = re.sub(r"```.*?```", "", text, flags=re.S)
    two = Counter(a + " " + b for a, b in re.findall(
        r"\b([A-Z][a-z]{1,})(?:\s+|—\s*)([A-Z][a-z]{1,})\b", body)
        if a not in STOP and b not in STOP)
    one = Counter(n for n in re.findall(r"\b([A-Z][a-z]{2,})\b", body) if n not in STOP)
    if two:
        top2, n2 = two.most_common(1)[0]
        head = top2.split()[0]
        # a two-word name outranks a one-word name only when it is genuinely frequent
        if n2 >= 5 or n2 >= one.get(head, 0):
            return top2
    return one.most_common(1)[0][0] if one else None


def gate(path):
    p = pathlib.Path(path)
    text = p.read_text(encoding="utf-8")
    prose, panel, extra = split_prose(text)
    flat = re.sub(r"\*", "", prose).lower()
    fails, warns = [], []

    words = prose.split()
    n_words = len(words)

    # 1. dialogue dial ─────────────────────────────────────────────────────────
    dlgs = re.findall(r'"([^"\n]+)"', prose)
    n_dlg = len(dlgs)
    dlg_words = sum(len(d.split()) for d in dlgs)
    pct = 100.0 * dlg_words / n_words if n_words else 0.0

    dial = None
    m = re.search(r"DIALOGUE\s*:\s*(lesson|standard|hush)", panel, re.I)
    if m:
        dial = m.group(1).lower()
    else:
        warns.append("panel does not declare DIALOGUE load (lesson|standard|hush) — measured as 'standard'")
        dial = "standard"
    lo, hi = DIALS[dial]
    if pct < lo:
        fails.append(f"dialogue share {pct:.1f}% is below the {dial} floor {lo:.0f}% "
                     f"(the rejected Blue Silver draft ran 0.0%; the voice bar runs 20.6-32.1%)")
    elif pct > hi:
        warns.append(f"dialogue share {pct:.1f}% is above the {dial} ceiling {hi:.0f}% — re-dial, don't apologise")

    # 2. sentence rhythm — measured on NARRATION and on the whole chapter.
    #
    # Why two numbers. The 9-11 bar in the SL3 CODEX is aimed at narration turning into
    # journal-ese. Dialogue sentences are structurally longer, so an all-sentence median
    # rises with dialogue share and stops measuring the thing the law is about. Measured
    # 2026-09-19 across the author's corpus:
    #
    #                       ALL   NARRATION
    #   SL3 ch1 voice bar    11       11
    #   SL3 ch2 / ch3         9        7-8
    #   SL3 ch101 (newest)   12       11
    #   SL4 ch31              8        7
    #   BS rebuilt ch1       10       12
    #   BS REJECTED ch1      16       16   ← the only corpus member that scores high on both
    #
    # Narration separates the rejected draft from every good chapter. Both are checked; the
    # thresholds are set from the table, not from taste.
    sents = sentences(prose)
    lens = [len(s.split()) for s in sents]
    med = statistics.median(lens) if lens else 0

    narr = re.sub(r'"[^"]*"', ' ', prose)
    narr = re.sub(r"\*[^*]*\*", " ", narr)
    nlens = [len(s.split()) for s in sentences(narr)]
    nmed = statistics.median(nlens) if nlens else 0

    if nmed > 13:
        fails.append(f"narration median sentence {nmed:.0f} words — drift (the rejected Blue "
                     f"Silver draft measured 16; the voice bar measures 7-11)")
    elif nmed > 11.5:
        warns.append(f"narration median sentence {nmed:.1f} words — above the 7-11 bar")
    if med > 15:
        fails.append(f"all-sentence median {med:.0f} words — the rejected draft measured 16; "
                     f"good chapters measure 8-12")
    elif med > 13:
        warns.append(f"all-sentence median {med:.1f} words — good chapters measure 8-12")

    # 2b. the ", and" chain — the drift fingerprint the SL3 CODEX actually caught.
    #     voice bar 16.9/1k · the drift chapter 26.7/1k
    chains = len(re.findall(r",\s+and\s", prose))
    rate = 1000.0 * chains / n_words if n_words else 0
    if rate > 26:
        fails.append(f"', and' chains {rate:.1f}/1k — the drift rate (SL3 ch60 measured 26.7; "
                     f"the voice bar 16.9)")
    elif rate > 20:
        warns.append(f"', and' chains {rate:.1f}/1k — above the voice bar (16.9). Split run-ons.")

    # 3. the Spectator Test ────────────────────────────────────────────────────
    # An "Other POV" chapter is one of the kit's five registers and is legal. It must
    # DECLARE itself, because an undeclared POV change is a continuity error the reader
    # feels before they can name it (07_PROSE_LAW.md §5). Declared POV chapters are
    # measured against their own viewpoint character, not the serial protagonist.
    m = re.search(r"POV\s*:\s*([A-Z][A-Za-z'\- ]{1,40})", panel)
    pov = m.group(1).strip() if m else None
    who = pov or protagonist(text)
    if pov and pov.lower().startswith("other"):
        who = None
    turns = 0
    if who:
        for d in dlgs:
            pass
        # attribute: a quote followed/preceded within 90 chars by the POV name + a speech verb
        for m in re.finditer(r'"[^"\n]{2,}"', prose):
            ctx = prose[max(0, m.start() - 90): m.end() + 90]
            if re.search(rf"\b{who}\b", ctx) and re.search(r"\b(said|asked|told|replied|answered)\b", ctx, re.I):
                turns += 1
    if who is None:
        warns.append("declared OTHER POV chapter — Spectator Test skipped. The kit permits it; "
                     "03_STORY_LAW.md still forbids a chapter whose only content is meditation.")
    elif turns < 4:
        fails.append(f"SPECTATOR TEST: viewpoint character '{who}' has {turns} attributed spoken "
                     f"turns (law: >= 4). A watcher chapter does not ship.")
    w, a = len(WATCH.findall(prose)), len(ACT.findall(prose))
    if w and w > a * 0.6:
        warns.append(f"watch-verbs {w} vs act-verbs {a} — the chapter is leaning observational")

    # 4. apparatus discipline (failure mode five, revoked) ─────────────────────
    n_marker = text.count(MARKER)
    if n_marker > 1:
        fails.append(f"{n_marker} marker blocks — a chapter carries the panel and nothing else. "
                     f"A book-end card belongs to a BOOK's last chapter only.")
    if extra:
        fails.append(f"{len(extra)} extra fenced block(s) after the panel — that is a footer. "
                     f"Bookkeeping lives in SERIAL_LOG.md, where a reader never sees it.")
    fields = re.findall(r"^[A-Z][A-Z0-9 ]{1,14}\s*:", panel, flags=re.M)
    if len(fields) > 8:
        fails.append(f"panel has {len(fields)} fields — the slim panel is 8 or fewer "
                     f"(KIND/AGE/CLASS/THREAT/BOND/LOSS/LAW/DIALOGUE)")

    # 5. banned registers ──────────────────────────────────────────────────────
    for t in TICS:
        if t in flat:
            fails.append(f"banned voice tic: {t!r}")
    for t in DOCTRINE_IN_A_MOUTH:
        if t in flat:
            fails.append(f"doctrine-in-a-mouth fingerprint: {t!r}")
    for t in ABSTRACT_CLIFF:
        if t in flat:
            fails.append(f"banned abstract-cliff register: {t!r}")

    # 6. portability ───────────────────────────────────────────────────────────
    hit = CJK.search(text)
    if hit:
        fails.append(f"CJK character {hit.group(0)!r} — the Language Law is absolute, any file")
    if SPELLING.search(text):
        fails.append(f"two-word spelling {SPELLING.search(text).group(0)!r} — canon writes "
                     f"'Bluesilver Grass' as one word (Lock 11)")
    if re.search(r"\*\*[^*\n]+\*\*", prose):
        warns.append("bold in prose — bold is for a term, never for emphasis (Voice Law §6)")

    # 7. length band ───────────────────────────────────────────────────────────
    if n_words < 900:
        fails.append(f"prose only {n_words} words — summary-as-chapter (<900)")
    elif n_words > 6000:
        warns.append(f"{n_words} words — above the measured band (1,400-5,000; ch1 of a serial "
                     f"may run long, but say so in SERIAL_LOG)")

    # 8. the turn ──────────────────────────────────────────────────────────────
    if not re.search(r"TURN\s*:", panel, re.I) and "turn" not in flat:
        warns.append("no TURN declared — what is true at the end that was not true at the start?")

    return dict(name=p.name, words=n_words, dlg=n_dlg, pct=pct, med=med, nmed=nmed,
                chain=rate, turns=turns, who=who, dial=dial, fails=fails, warns=warns)


def main(argv):
    files = argv[1:] or sorted(str(x) for x in pathlib.Path("chapters").glob("*.md"))
    if not files:
        print("style_gate: no chapters found"); return 0
    print("=" * 76)
    print("VOICE LAW / STYLE_GOLD GATE  —  the wall above verify.py")
    print("=" * 76)
    nf = nw = 0
    for f in files:
        f = pathlib.Path(f)
        if f.is_dir():
            files.extend(sorted(str(x) for x in f.glob("*.md")))
            continue
        r = gate(f)
        tag = "FAIL" if r["fails"] else ("WARN" if r["warns"] else "PASS")
        print(f"{tag:5s} {r['name']}")
        print(f"      {r['words']}w · dialogue {r['pct']:.1f}% ({r['dlg']} lines, dial={r['dial']}) "
              f"· sentence median {r['med']:.0f} all / {r['nmed']:.0f} narr "
              f"· ', and' {r['chain']:.1f}/1k · {r['who']} speaks {r['turns']}x")
        for x in r["fails"]:
            print(f"      FAIL  {x}")
        for x in r["warns"]:
            print(f"      warn  {x}")
        nf += len(r["fails"]); nw += len(r["warns"])
    print("-" * 76)
    print(f"{len(files)} file(s)  |  {nf} failures  |  {nw} warnings")
    print("RESULT:", "FAIL" if nf else ("PASS (warnings)" if nw else "PASS"))
    return 1 if nf else (2 if nw else 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
