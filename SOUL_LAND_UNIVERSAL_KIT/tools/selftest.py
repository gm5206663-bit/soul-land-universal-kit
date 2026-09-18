#!/usr/bin/env python3
"""
SOUL LAND UNIVERSAL KIT — gate self-test.

Usage:
    python3 tools/selftest.py

Builds throwaway chapters that each contain exactly one known defect, runs
verify.py over them, and confirms every defect is caught. Then builds a clean
chapter and confirms it passes.

Why this file exists
    A gate that passes everything verifies nothing. verify.py was once run on a
    proven 33,000-word serial and reported 15 failures, all of them false
    positives from an over-broad rule. Nothing caught that except a hand-built
    negative test. This script is that test, permanently.

    Run it after ANY edit to verify.py. If a gate is tightened, loosened, or
    rewritten, this is what tells you whether it still does its job.

Exits 0 only when every defect is caught AND the clean chapter passes.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.join(HERE, "verify.py")

MARKER = "\u25c6"
ENDASH = "\u2013"
EMDASH = "\u2014"
NL = chr(10)

# A minimal chapter that satisfies all seven gates. Every defect fixture is this
# text with exactly one corruption applied, so a failure can only mean the gate
# missed that corruption.
CLEAN = (
    "# Chapter 1 " + EMDASH + " The Clean One" + NL + NL
    + "```" + NL
    + MARKER + " STATUS " + EMDASH + " Chapter 1: years 0" + ENDASH + "1" + NL
    + "KIND      : a test subject" + NL
    + "AGE       : six" + NL
    + "CLASS     : none" + NL
    + "THREAT    : a recruiter" + NL
    + "```" + NL + NL
    + "---" + NL + NL
    + "The man came to the door." + NL + NL
    + '"Your name," he said.' + NL + NL
    + '"Lin," the boy said.' + NL + NL
    + '"Lin what."' + NL + NL
    + '"Just Lin."' + NL + NL
    + "The man wrote it down. "
    '"Innate soul power four," he said. "That is enough to matter."' + NL + NL
    + '"It is not nothing," the boy said.' + NL + NL
    + '"No," said the man. "It is not nothing."' + NL + NL
    + "---" + NL
)


def _set_panel(text, lo, hi):
    """Rewrite the panel's year range."""
    return re.sub(
        r"years \d+" + ENDASH + r"\d+",
        "years " + str(lo) + ENDASH + str(hi),
        text,
        count=1,
    )


def d_digits(t):
    return t.replace("The man came to the door.",
                     "The man came to the door in year 163 with 3 others.")


def d_cjk(t):
    return t.replace("The man came to the door.",
                     "The man came to the door " + "\u84dd\u94f6\u8349")


def d_nodialogue(t):
    return t.replace('"', "")


def d_placeholder(t):
    return t.replace("The man came to the door.",
                     "TODO: <fill this in> the man came to the door.")


def d_backslash_n(t):
    return t.replace("The man came to the door.",
                     "The man came to the door." + chr(92) + "nHere.")


def d_marker_in_prose(t):
    return t.replace("The man came to the door.",
                     MARKER + " The man came to the door.")


def d_two_cards(t):
    return (t
            + "```" + NL + MARKER + " END OF BOOK TWO" + NL + "```" + NL + NL
            + "```" + NL + MARKER + " END OF BOOK THREE" + NL + "```" + NL)


# name -> (mutator, substring that must appear in verify.py's complaint)
DEFECTS = [
    ("digits in prose",      d_digits,          "digits in prose"),
    ("unreadable script",    d_cjk,             "unreadable script"),
    ("no dialogue",          d_nodialogue,      "spoken dialogue lines"),
    ("placeholder text",     d_placeholder,     "placeholder text"),
    ("literal backslash-n",  d_backslash_n,     "backslash-n"),
    ("marker leaked to prose", d_marker_in_prose, "panel marker in prose"),
    ("two book-end cards",   d_two_cards,       "marker cards"),
]


def run_verify(path):
    r = subprocess.run(
        [sys.executable, VERIFY, path],
        capture_output=True, text=True,
    )
    return r.returncode, r.stdout + r.stderr


def main():
    if not os.path.exists(VERIFY):
        print("selftest: cannot find verify.py next to this file")
        return 1

    tmp = tempfile.mkdtemp(prefix="sl_selftest_")
    failures = []
    try:
        # ---- 1. the clean chapter must PASS --------------------------------
        d = os.path.join(tmp, "clean")
        os.makedirs(d)
        with open(os.path.join(d, "Chapter_01_Clean.md"), "w", encoding="utf-8") as fh:
            fh.write(CLEAN)
        rc, out = run_verify(d)
        if rc != 0:
            failures.append(
                "clean chapter FAILED the gate (false positive)" + NL
                + "".join("    " + l + NL for l in out.splitlines() if "FAIL" in l)
            )
        else:
            print("  ok    clean chapter passes")

        # ---- 2. each defect must be caught, alone --------------------------
        for i, (name, mutate, needle) in enumerate(DEFECTS):
            d = os.path.join(tmp, "d%d" % i)
            os.makedirs(d)
            bad = mutate(_set_panel(CLEAN, 100 + i, 199 + i))
            with open(os.path.join(d, "Chapter_01_Defect.md"), "w",
                      encoding="utf-8") as fh:
                fh.write(bad)
            rc, out = run_verify(d)
            if rc == 0:
                failures.append("NOT CAUGHT: " + name + " (gate returned PASS)")
            elif needle not in out:
                failures.append(
                    "caught for the wrong reason: " + name
                    + NL + "    expected a complaint containing " + repr(needle)
                )
            else:
                print("  ok    caught: " + name)

        # ---- 3. contiguity: overlap and gap --------------------------------
        d = os.path.join(tmp, "contig")
        os.makedirs(d)
        for n, (lo, hi) in enumerate([(0, 10), (10, 20), (18, 30)]):
            with open(os.path.join(d, "Chapter_%02d_X.md" % (n + 1)), "w",
                      encoding="utf-8") as fh:
                fh.write(_set_panel(CLEAN, lo, hi))
        rc, out = run_verify(d)
        if "OVERLAP" not in out:
            failures.append("panel OVERLAP not detected")
        else:
            print("  ok    caught: panel overlap")

        d = os.path.join(tmp, "gap")
        os.makedirs(d)
        for n, (lo, hi) in enumerate([(0, 10), (25, 30)]):
            with open(os.path.join(d, "Chapter_%02d_X.md" % (n + 1)), "w",
                      encoding="utf-8") as fh:
                fh.write(_set_panel(CLEAN, lo, hi))
        rc, out = run_verify(d)
        if "GAP" not in out:
            failures.append("panel GAP not detected")
        else:
            print("  ok    caught: panel gap")

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("-" * 64)
    if failures:
        print("SELFTEST FAILED " + EMDASH + " verify.py is not trustworthy:")
        for f in failures:
            print("  " + f)
        return 1
    print("SELFTEST PASSED " + EMDASH + " all defects caught, clean chapter passes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
