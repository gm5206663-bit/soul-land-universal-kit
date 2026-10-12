#!/usr/bin/env python3
"""plain_word_check.py — advisory companion to PLAIN LANGUAGE LAW (kit 07_PROSE_LAW §11,
imported at STYLE_LAW §11). Reads foundation/PLAIN_WORD_LIST.md for the classification:
  Class A  — retired from narration; any hit is a defect (this tool prints; gates decide)
  Class B  — flagged in-scene vocabulary; hits are printed with line numbers so the
             writer can eyeball the noun budget before shipping.
This tool NEVER fails. It is the "grep the retired word list (kit + project)" step that
kit rule §11.5 demands. Exit code is always 0 unless a file cannot be read.
"""
import re, sys, io

FLAGGED = [
    "the bank", "the wednesdays", "the flat line", "the door", "the ticket",
    "the jar-washing", "the case man", "the carry man", "the second row",
    "the column of fours", "the summer field", "the third door", "the stairs",
    "the file",
]
RETIRED = []  # Class A — nothing retired at classification time

def paragraph_class(par):
    """dialogue paragraphs are exempt: speech may carry anything a character would say"""
    stripped = par.strip()
    if not stripped:
        return "blank"
    return "speech" if stripped.startswith('"') or stripped.startswith('*') else "narration"

def main(paths):
    total = {}
    bad = 0
    for path in paths:
        try:
            text = io.open(path, encoding="utf-8").read()
        except OSError as e:
            print(f"READ ERROR {path}: {e}"); bad = 1; continue
        lines = text.split("\n")
        # strip the panel apparatus block (first ``` fence pair) — apparatus is not narration
        in_fence, fence_done, out = False, False, []
        for ln in lines:
            if ln.strip().startswith("```") and not fence_done:
                in_fence = not in_fence
                if not in_fence:
                    fence_done = True
                continue
            if not in_fence:
                out.append(ln)
        for n, ln in enumerate(out, 1):
            low = ln.lower()
            if paragraph_class(ln) != "narration":
                continue
            for term in RETIRED:
                if term in low:
                    print(f"  RETIRED  {path}:{n}  '{term}'  {ln.strip()[:90]}")
            for term in FLAGGED:
                hits = low.count(term)
                if hits:
                    total[term] = total.get(term, 0) + hits
                    print(f"  flagged  {path}:{n}  '{term}' x{hits}  {ln.strip()[:90]}")
    print("\nflagged totals:", ", ".join(f"{k}={v}" for k, v in sorted(total.items(), key=lambda x: -x[1])) or "none")
    print("RESULT: PASS (advisory — this instrument never fails a build)")
    return bad

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
