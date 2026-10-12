#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SELFTEST — proves the gates can fail.

Doctrine: SOUL_LAND_UNIVERSAL_KIT/09_AUDIT_LAW.md.
  "A gate that has only ever been seen to pass is a gate nobody has tested."

This script builds a known-good sample chapter in memory, writes it to a temp file,
then injects one defect at a time and asserts that each gate complains. If any defect
passes silently, the gate is blind and this script exits non-zero.

Covers:
  verify.py     — the kit's seven hard gates (CJK, backslash-n, digits-in-prose,
                  dialogue minimum, panel contiguity, placeholders, marker discipline)
  style_gate.py — this serial's voice gates (narration median, ', and' chain rate,
                  word floor, dialogue band, Spectator Test)
  both          — the prose-extraction contract (panels are not prose)

Run:  python3 tools/selftest.py
"""

import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.join(HERE, "verify.py")
STYLE = os.path.join(HERE, "style_gate.py")
COPY = os.path.join(HERE, "canon_copy_check.py")
NL = chr(10)
BSLASH_N = chr(92) + "n"  # never written literally — 07_PROSE_LAW.md

# ---------------------------------------------------------------- clean sample
# Deliberately passes every gate: slim panel, no footer, plenty of dialogue,
# short narration sentences, low chain rate, protagonist-attributed turns.

_PANEL = (
    "```" + NL
    + "◆ STATUS — Chapter 99: years 4–5" + NL
    + "KIND      : a man who counts." + NL
    + "AGE       : nine." + NL
    + "CLASS     : rank ten, and the ring is not his yet." + NL
    + "THREAT    : a named man with a reason." + NL
    + "BOND      : the woman who walks him to the garden." + NL
    + "LAW       : an offset can be subtracted." + NL
    + "DIALOGUE  : standard 13-30% - a yard and a bench." + NL
    + "TURN      : what was true is no longer true." + NL
    + "```" + NL
)

_DIALOGUE = [
    'He said, "Take it off the bench and put it on the table."',
    'Su Wan said, "The table is not mine to move."',
    '"Then ask," he said. "Ask whether the table is yours."',
    'She asked. The answer came back in the negative.',
    '"Write it down," he said. "If it is not written it did not happen."',
    'She wrote it down. The ink was thin and the paper was thinner.',
    '"How many?" she said.',
    '"Three," he said. "Three batches, and the third is the one I believe."',
    '"You do not believe the others?" she said.',
    '"I believe they are right," he said. "Right is not enough."',
    '"Come back in the spring," she said.',
    '"There is nothing to come back to," he said. "Not in the spring."',
    '"There is the garden," she said.',
    'He did not answer, which was an answer, and she took it as one.',
    '"Your mother came by," she said. "She wanted the balm."',
    '"Which one?" he said.',
    '"The one that is right," she said. "Not the one you believe."',
    'He laughed once. It was not a happy sound and neither of them pretended.',
    '"Tell her the shelf is empty," he said.',
    '"It is not empty," she said. "I counted."',
    '"Then tell her I counted wrong," he said.',
    '"I will tell her the truth," she said, "and she will not like it."',
    '"There is one thing I am not going to do yet," he said, "and I will not say what it is."',
    '"You always say that," she said, "and it always turns out to be the same thing."',
    '"Then you already know what it is," he said, "and neither of us has to say it aloud."',
    '"That is not knowing," she said. "That is guessing with extra steps."',
    '"Guessing with extra steps is most of what counting is," he said.',
    '"Your father says you have not slept properly in a week," she said.',
    '"My father says a great many things," he said, "and most of them are about me."',
    '"He is worried about the money," she said. "The shop does not carry the month."',
    '"The shop carries the month," he said. "It does not carry the next one."',
    '"Then fix the next one," she said.',
    '"I intend to," he said. "Not today, and not by telling you how."',
    '"You are impossible when you are like this," she said.',
]

# short, flat narration: low chain rate, low sentence median
_PAD_UNIT = [
    "The wall was cold to the back of the hand.",
    "He counted the slats. There were nine.",
    "A bird went over the roof. It did not come back.",
    "The bench held three things and nothing else.",
    "Dust lay on the ledger in a thin even coat.",
    "He wiped it with his cuff and read the top line.",
    "The number had not changed since autumn.",
    "Outside, the street was empty and stayed empty.",
    "Grass under the wall had gone the colour of straw.",
    "He put the pen down. The ink dried on the nib.",
    "A cart went past. The wheels were unshod.",
    "The light left the yard before the cold did.",
]


def _sample(pad_reps=8):
    """Deterministic clean sample: >900 prose words, dialogue inside 13-30%,
    short narration sentences, low ', and' chain rate, protagonist-attributed turns."""
    body = list(_DIALOGUE)
    pad = _PAD_UNIT * pad_reps
    return (
        "# Chapter 99: The Sample" + NL + NL
        + _PANEL + NL
        + NL.join(body) + NL + NL
        + NL.join(pad) + NL
    )


def _set_panel(text, lo, hi):
    return re.sub(r"Chapter 99: years \d+-\d+", f"Chapter 99: years {lo}-{hi}", text, count=1)


# ------------------------------------------------------------------- defects
# (name, mutator, needle-that-must-appear-in-the-complaint, which-gate)
#  which-gate: 'v' = verify.py, 's' = style_gate.py, 'b' = both

DEFECTS = [
    # --- verify.py: the kit's seven hard gates -------------------------------
    ("cjk-in-prose",
     lambda t: t.replace("The bench held three things", "The bench held 草 three things"),
     "unreadable", "v"),
    ("backslash-n-literal",
     lambda t: t.replace("The bench held", "The bench held " + BSLASH_N + " a"),
     "slash", "v"),
    ("digit-in-prose",
     lambda t: t.replace("There were nine.", "There were 9."),
     "digit", "v"),
    ("no-dialogue",
     lambda t: t.replace('"', "'"),
     "dialogue", "v"),
    ("panel-prose-intrusion",
     lambda t: t.replace("AGE       : nine.", "AGE       : nine." + NL + NL + "stray prose line." + NL),
     "panel", "v"),
    ("placeholder-left-in",
     lambda t: t.replace("The number had not changed", "TODO: the number had not changed"),
     "laceholder", "v"),
    ("marker-in-prose",
     lambda t: t.replace("Dust lay on the ledger", "◆ Dust lay on the ledger"),
     "marker", "v"),
    # --- style_gate.py: this serial's voice gates ----------------------------
    ("chain-flood",
     lambda t: t.replace(
        "The wall was cold to the back of the hand.",
        "The wall was cold, and the hand was cold, and the stone was cold, and the air "
        "was cold, and he was cold, and the day was cold, and the yard was cold, and "
        "the roof was cold, and the bird was cold, and the bench was cold, and the "
        "ledger was cold, and the ink was cold."),
     "chain", "s"),
    ("narration-drift",
     # A median is robust: to move it you must change more than half the sentences.
     # Rewrite every short narration line as one long drifting sentence.
     lambda t: (lambda long_s: NL.join(
         (long_s if ln in _PAD_UNIT else ln) for ln in t.split(NL)))(
         "The thing in question had been sitting exactly where it was since long "
         "before anyone thought to notice it, and it would remain there for some "
         "considerable while after they had stopped, which is the sort of fact that "
         "only becomes interesting when a person is standing in front of it at the "
         "wrong time of the year with nothing better to do than look at it properly."),
     "narration", "s"),
    ("word-floor",
     lambda t: _PANEL + NL + NL.join(_DIALOGUE[:4]) + NL + NL.join(_PAD_UNIT[:2]) + NL,
     "word", "s"),
    ("dialogue-flood",
     lambda t: _PANEL + NL + NL.join(
        ['"Say the thing again," he said.'] * 60) + NL + "The yard was cold. He counted." + NL,
     "dialogue", "s"),
]

# The extraction contract: a file that is ONLY a panel has no prose at all.
EXTRACTION = [
    ("panel-is-not-prose",
     lambda t: _PANEL,
     "word", "s"),
]


def run(script, path):
    p = subprocess.run([sys.executable, script, path],
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def write_tmp(text):
    fd, path = tempfile.mkstemp(suffix=".md", prefix="selftest_")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    print("=" * 72)
    print("SELFTEST — proving the gates can fail")
    print("=" * 72)

    for s in (VERIFY, STYLE):
        if not os.path.exists(s):
            print("FATAL  missing gate:", s)
            return 2

    failures = []

    # ---- 0. the clean sample must pass both gates ---------------------------
    base = _sample()
    p = write_tmp(base)
    rv, out_v = run(VERIFY, p)
    rs, out_s = run(STYLE, p)
    os.unlink(p)

    clean_ok_v = "RESULT: PASS" in out_v
    clean_ok_s = ("RESULT: PASS" in out_s) or ("RESULT: PASS (warnings)" in out_s)

    print()
    print("[0] clean sample")
    print("    verify.py      :", "PASS" if clean_ok_v else "FAIL")
    print("    style_gate.py  :", "PASS" if clean_ok_s else "FAIL")
    if not clean_ok_v:
        failures.append(("clean sample", "verify.py", out_v.strip().splitlines()[-6:]))
    if not clean_ok_s:
        failures.append(("clean sample", "style_gate.py", out_s.strip().splitlines()[-6:]))

    # ---- 1. year-range in the panel is read by verify.py -------------------
    p = write_tmp(_set_panel(base, 4, 5))
    _, out = run(VERIFY, p)
    os.unlink(p)
    yrs_ok = "yrs 4-5" in out
    hyphen_probe = _set_panel(base, 4, 5).replace("years 4\u20135", "years 4-5")
    print()
    print("[1] panel year-range parsed  :", "PASS" if yrs_ok else "FAIL")
    if not yrs_ok:
        failures.append(("year-range parse", "verify.py", [l for l in out.splitlines() if "PASS" in l or "FAIL" in l]))

    # ---- 2. injected defects must be caught --------------------------------
    print()
    print("[2] injected defects")
    all_defects = DEFECTS + EXTRACTION
    for name, mutate, needle, which in all_defects:
        try:
            bad = mutate(base)
        except Exception as e:  # a broken mutator is itself a selftest failure
            failures.append((name, "mutator", [repr(e)]))
            print(f"    {name:<26} MUTATOR ERROR {e}")
            continue

        path = write_tmp(bad)
        rc, out = run(VERIFY if which == "v" else STYLE, path)
        os.unlink(path)

        caught = (rc != 0) or ("FAIL" in out)
        named = needle.lower() in out.lower()
        ok = caught and named

        tag = "caught" if ok else ("SILENT" if not caught else "caught-but-unlabelled")
        print(f"    {name:<26} {tag}")
        if not ok:
            failures.append((name, "verify.py" if which == "v" else "style_gate.py",
                             [l.strip() for l in out.splitlines() if l.strip()][-8:]))

    # ---- 3. canon_copy_check — the transcription blind spot -----------------
    # Regression suite for the defect that shipped: chapters one to four staged
    # canon scenes by transcribing them, and the gate reported PASS because its
    # quoted-speech threshold was 15 words while every borrowed run sat between
    # 8 and 14. A gate whose limit is chosen before the evidence measures nothing.
    print()
    print("[3] canon_copy_check — transcription")

    canon_fixture = (
        "CANON FIXTURE\n"
        "\'Little girl, where are your parents?\' Right at that moment several young\n"
        "delinquents surrounded her after being attracted by her silver hair.\n"
        "\'Are you hungry? Big brother will bring you to eat some good things, how\n"
        "about it?\' The man smiled.\n"
        "\'You guys are villains!\' He had rolled on the ground but immediately got up.\n"
        "\'Villains won\'t have a good end! I\'m a Soul Master!\'\n"
    )
    cdir = tempfile.mkdtemp(prefix="selftest_canon_")
    cpath = os.path.join(cdir, "canon_001_excerpt.txt")
    with open(cpath, "w", encoding="utf-8") as f:
        f.write(canon_fixture)

    def run_copy(text):
        cp = write_tmp(text)
        r = subprocess.run([sys.executable, COPY, "--chapters", cp, "--canon", cpath],
                           capture_output=True, text=True)
        os.unlink(cp)
        return r.returncode, r.stdout + r.stderr

    # (a) the clean sample borrows nothing
    rc, out = run_copy(base)
    clean_copy = rc == 0 and "RESULT: PASS" in out
    print("    clean-sample-no-borrow       ", "PASS" if clean_copy else "FAIL")
    if not clean_copy:
        failures.append(("copy: clean sample", "canon_copy_check.py",
                         [l.strip() for l in out.splitlines() if l.strip()][-6:]))

    # (b) one 13-word verbatim run inside a quote  -> check B
    # NB: _PAD_UNIT lines are NARRATION, so the needle is unquoted in the sample.
    one = base.replace("The bench held three things and nothing else.",
                       chr(34)+"Are you hungry big brother will bring you to eat some good things"+chr(34))
    rc, out = run_copy(one)
    b_ok = rc != 0 and "[B]" in out
    print("    single-long-quoted-run       ", "caught" if b_ok else "SILENT")
    if not b_ok:
        failures.append(("copy: 13-word quoted run", "canon_copy_check.py",
                         [l.strip() for l in out.splitlines() if l.strip()][-6:]))

    # (c) THE REGRESSION — many runs of 8-14 words, none reaching 15.
    #     This is exactly what chapter three did. The old threshold passed it.
    regression = base.replace(
        "The bench held three things and nothing else.",
        chr(34) + "Big brother will bring you to eat some good things Villains "
                  "won't have a good end" + chr(34))
    rc, out = run_copy(regression)
    c_ok = rc != 0 and ("[B]" in out or "[C]" in out)
    print("    sub-threshold-run-cluster    ", "caught" if c_ok else "SILENT")
    if not c_ok:
        failures.append(("copy: 8-14 word run cluster (the shipped blind spot)",
                         "canon_copy_check.py",
                         ["the gate passed a chapter built out of canon dialogue,",
                          "because every borrowed run was shorter than the old 15-word limit"]))

    # (d) density — a transcript of many short quotes, no single long run
    # every quote carries a 6-word canon run: too short for check B, numerous
    # enough to blow a lowered check-C ceiling. Tests density in isolation.
    dense = base.replace("The bench held three things and nothing else.",
                         chr(34)+"little girl where are your parents today"+chr(34))
    cp = write_tmp(dense)
    r = subprocess.run([sys.executable, COPY, "--chapters", cp, "--canon", cpath,
                        "--budget-fail", "20", "--budget-warn", "10"],
                       capture_output=True, text=True)
    os.unlink(cp)
    out = r.stdout + r.stderr
    d_ok = r.returncode != 0 and "[C]" in out
    print("    density-ceiling-fires        ", "caught" if d_ok else "SILENT")
    if not d_ok:
        failures.append(("copy: density ceiling", "canon_copy_check.py",
                         [l.strip() for l in out.splitlines() if l.strip()][-6:]))

    import shutil
    shutil.rmtree(cdir, ignore_errors=True)

    # ---- [4] banned_token_check.py: layer 9 can fail, and stays silent when clean
    # The kit's negative_test_rule: every rejection rule fires on its bad case
    # and stays silent on its good case. Layer 9 was added 2026-09-20 and found
    # eight real fourth-wall breaks in shipped prose on its first run, so the
    # bad case is not hypothetical.
    BANNED = os.path.join(os.path.dirname(os.path.abspath(VERIFY)),
                          "banned_token_check.py")
    print()
    print("[4] banned_token_check.py (layer 9)")
    if os.path.exists(BANNED):
        bad = base.replace("The bench held three things and nothing else.",
                           "The bench held three things, and in canon it held four.")
        bp = write_tmp(bad)
        rb = subprocess.run([sys.executable, BANNED, "--file", bp],
                            capture_output=True, text=True)
        os.unlink(bp)
        ob = rb.stdout + rb.stderr
        fw_ok = rb.returncode != 0 and "fourth_wall" in ob
        print("    fourth-wall-word-fires       ", "caught" if fw_ok else "SILENT")
        if not fw_ok:
            failures.append(("banned: fourth_wall", "banned_token_check.py",
                             [l.strip() for l in ob.splitlines() if l.strip()][-6:]))

        gp = write_tmp(base)
        rg = subprocess.run([sys.executable, BANNED, "--file", gp],
                            capture_output=True, text=True)
        os.unlink(gp)
        og = rg.stdout + rg.stderr
        cl_ok = rg.returncode == 0 and "RESULT: PASS" in og
        print("    clean-sample-silent          ", "quiet" if cl_ok else "FALSE POSITIVE")
        if not cl_ok:
            failures.append(("banned: clean sample", "banned_token_check.py",
                             [l.strip() for l in og.splitlines() if l.strip()][-6:]))
    else:
        print("    MISSING tools/banned_token_check.py")
        failures.append(("banned: gate absent", "banned_token_check.py", []))

    # ---- verdict -----------------------------------------------------------
    print()
    print("-" * 72)
    total = 8 + len(all_defects)   # [0] clean + [1] panel + [2] defects + [3] four copy checks + [4] two banned-token checks
    bad_n = len(failures)
    print(f"{total} checks  |  {total - bad_n} held  |  {bad_n} blind")
    print("-" * 72)

    if failures:
        print()
        for name, gate, tail in failures:
            print(f"  BLIND  {name}  ({gate})")
            for l in tail:
                print("         " + l)
        print()
        print("RESULT: FAIL — a gate let a known defect through. Fix the gate, not the test.")
        return 1

    print()
    print("RESULT: PASS — every injected defect was caught and named.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
