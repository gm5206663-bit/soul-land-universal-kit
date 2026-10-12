#!/usr/bin/env python3
"""
banned_token_check.py -- layer 9. Regression-token scanner.

Reads foundation/BANNED_TOKENS.json and greps the tree for values that are
known-dead: meta-vocabulary in prose, working markers, identity shapes,
rejected branches, reserved-until-later states, and superseded figures in the
documents a fresh agent reads first.

Why this exists separately from verify.py and style_gate.py: those two judge
whether prose is WELL-FORMED. Neither can know that a particular number used to
be right and now is not, or that a particular word belongs to the author rather
than the character. That knowledge only exists as a list, and this is the
instrument that reads the list.

Each category declares its own scope, because the defect classes live in
different parts of the tree. verify.py gate 3 already forbids every digit in
prose, so scanning chapters for stale figures would be theatre; foundation/
uses "canon" as a technical term hundreds of times, so scanning docs for
fourth-wall vocabulary would drown the real findings.

The exemption logic is imported from the four honesty rules of
storyos-site/scripts/drift.py, which exist because a naive scan gets each of
them wrong in a specific way. A scanner that cries wolf on correction receipts
gets ignored, and an ignored scanner is worse than no scanner.

Exit codes follow this project's three-state convention:
  0  clean
  2  findings that are all exempt receipts -- pass with warnings
  1  at least one unexempted failure
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = os.path.join(ROOT, "foundation", "BANNED_TOKENS.json")

# `:` is deliberately not a splitter -- it introduces a claim, and splitting on
# it severs a directive from the value it points at.
SENTENCE_SPLIT = re.compile(r"(?<=[.;])\s+|\s*\|\s*")


def load():
    with io.open(TOKENS, encoding="utf-8") as fh:
        return json.load(fh)


def strip_fenced(text):
    """Blank out fenced blocks, preserving line numbering.

    A fenced block is apparatus, not prose -- the same boundary verify.py gate 3
    uses to permit digits inside panels. Lines are kept so reported line numbers
    still point at the right place in the file.
    """
    out, fence = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else line)
    return "\n".join(out)


def walk(paths, strip):
    for entry in paths:
        target = os.path.join(ROOT, entry)
        if os.path.isfile(target):
            files = [target]
        elif os.path.isdir(target):
            files = []
            for dirpath, dirnames, filenames in os.walk(target):
                dirnames[:] = [d for d in dirnames
                               if not d.startswith(".") and d != "__pycache__"]
                for fn in sorted(filenames):
                    if fn.endswith((".md", ".txt")):
                        files.append(os.path.join(dirpath, fn))
        else:
            continue
        for path in files:
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            try:
                with io.open(path, encoding="utf-8") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError):
                continue
            yield rel, (strip_fenced(text) if strip else text)


def self_file_exempt(rel, token):
    stem = os.path.basename(rel).rsplit(".", 1)[0].lower().replace("_", " ")
    return bool(stem) and stem in token.lower()


def is_ledger(rel, cfg):
    """Files that are by construction a record of past states: always exempt."""
    ex = cfg["exemptions"]
    led = ex.get("ledger_files", [])
    if any(rel == x or rel.endswith("/" + x.split("/")[-1]) for x in led):
        return True
    base = os.path.basename(rel)
    return any(base.startswith(pre) for pre in ex.get("receipt_files", []))


HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def heading_is_receipt(body, markers):
    """drift.py honesty rule 2: a dated or historically-scoped heading makes
    everything under it a receipt for that moment rather than a claim about now."""
    low = body.lower()
    return any(m in low for m in markers)


def scan_one(path):
    """Single-file mode: scan one file under the chapters ruleset.

    Exists so tools/selftest.py can prove this gate can fail. A scanner that has
    never been seen to fail is a scanner nobody has tested -- the kit's
    negative_test_rule. Fenced blocks are stripped and no exemption applies,
    exactly as for real prose.
    """
    cfg = load()
    with io.open(path, encoding="utf-8") as fh:
        text = strip_fenced(fh.read())
    hits = []
    for cat, body in cfg["banned_tokens"].items():
        if body.get("scope", "both") not in ("chapters", "both"):
            continue
        for rx in body.get("regex", []):
            for m in re.finditer(rx, text):
                hits.append((cat, m.group(0)))
        low = text.lower()
        for lit in body.get("enforce", []) + body.get("literals", []):
            if lit.lower() in low:
                hits.append((cat, lit))
    seen, uniq = set(), []
    for cat, term in sorted(hits, key=lambda x: -len(x[1])):
        if cat in seen:
            continue
        seen.add(cat)
        uniq.append((cat, term))
    print("banned_token_check --file %s" % os.path.basename(path))
    if uniq:
        for cat, term in uniq:
            print("  [%s] %r" % (cat, term))
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


def main(argv):
    if len(argv) >= 2 and argv[0] == "--file":
        if not os.path.exists(argv[1]):
            print("banned_token_check: no such file: %s" % argv[1])
            return 1
        return scan_one(argv[1])
    if not os.path.exists(TOKENS):
        print("banned_token_check: foundation/BANNED_TOKENS.json is missing")
        return 1
    cfg = load()
    sm = cfg["scope_model"]
    never = tuple(x.rstrip("/") for x in sm["never_scanned"])

    def excluded(rel):
        return any(rel == n or rel.startswith(n + "/") for n in never)

    markers = [m.lower() for m in cfg["exemptions"]["historical_markers"]]
    files_ch = [(r, t) for r, t in walk(sm["chapters"], strip=True) if not excluded(r)]
    files_dc = [(r, t) for r, t in walk(sm["docs"], strip=False) if not excluded(r)]

    failures, receipts, per_cat = [], 0, {}

    for cat, body in cfg["banned_tokens"].items():
        scope = body.get("scope", "both")
        exempt_ok = bool(body.get("exempt_with_historical_marker"))
        pats = [(re.compile(r), r) for r in body.get("regex", [])]
        lits = [(l.lower(), l) for l in body.get("enforce", [])] + \
               [(l.lower(), l) for l in body.get("literals", [])]

        targets = []
        if scope in ("chapters", "both"):
            targets += [(r, t, True) for r, t in files_ch]
        if scope in ("docs", "both"):
            targets += [(r, t, False) for r, t in files_dc]

        head_marks = cfg["exemptions"].get("section_context", {}).get("heading_markers", [])
        for rel, text, is_prose in targets:
            ledger = is_ledger(rel, cfg)
            section_receipt = False
            for lineno, line in enumerate(text.splitlines(), 1):
                if not is_prose:
                    h = HEADING.match(line)
                    if h:
                        section_receipt = heading_is_receipt(h.group(2), head_marks)
                        continue
                low = line.lower()
                hits = []
                for rx, raw in pats:
                    m = rx.search(line)
                    if m:
                        hits.append(m.group(0))
                for l, raw in lits:
                    if l in low:
                        hits.append(raw)
                # Dedup: "in canon" and "canon" both match one line and are one
                # finding, not two. Keep the longest term as the label.
                hits = sorted(set(h for h in hits if not self_file_exempt(rel, h)),
                              key=len, reverse=True)[:1]
                for matched in hits:
                    if False:
                        continue
                    # Four cases, in order of authority:
                    #   prose   -- never exempt. Prose does not discuss its own
                    #              history, so a marker word there is coincidence.
                    #   ledger  -- always exempt. An append-only log of past
                    #              states is made of stale figures by design.
                    #   exempt_ok -- judge the sentence carrying the token, not
                    #              the line, so a receipt stays a receipt.
                    #   else    -- not exempt.
                    if is_prose:
                        exempt = False
                    elif ledger or section_receipt:
                        exempt = True
                    elif exempt_ok:
                        exempt = False
                        for sent in SENTENCE_SPLIT.split(line):
                            if matched.lower() in sent.lower():
                                if any(mk in sent.lower() for mk in markers):
                                    exempt = True
                                break
                    else:
                        exempt = False
                    per_cat[cat] = per_cat.get(cat, [0, 0])
                    if exempt:
                        receipts += 1
                        per_cat[cat][1] += 1
                    else:
                        failures.append((rel, lineno, cat, matched,
                                         "prose" if is_prose else "doc"))
                        per_cat[cat][0] += 1

    print("banned_token_check -- %d categories, %d chapters, %d docs scanned"
          % (len(cfg["banned_tokens"]), len(files_ch), len(files_dc)))
    print("  fenced blocks stripped in chapters (apparatus, not prose)")

    if per_cat:
        print("\n  by category:")
        for cat in cfg["banned_tokens"]:
            if cat in per_cat:
                f, r = per_cat[cat]
                print("    %-28s %3d finding(s), %4d exempt receipt(s)" % (cat, f, r))

    if failures:
        print("\nFAILURES (%d) -- a dead value is asserted as current:" % len(failures))
        for rel, lineno, cat, term, where in failures[:60]:
            print("  [%s] %s:%d  %r  (%s)" % (cat, rel, lineno, term, where))
        if len(failures) > 60:
            print("  ... and %d more" % (len(failures) - 60))

    print("\n  failures        : %d" % len(failures))
    print("  receipts exempt : %d  (correction receipts -- correct history, not drift)"
          % receipts)

    if failures:
        print("\nRESULT: FAIL")
        return 1
    if receipts:
        print("\nRESULT: PASS (all findings were exempt receipts)")
        return 0
    print("\nRESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
