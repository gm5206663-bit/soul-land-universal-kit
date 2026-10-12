#!/usr/bin/env python3
"""measure_chapter.py — the measuring tool for Qian Xun Ji Reborn.

Aligned to the house (Grey Wolf) style gate so numbers are comparable:
body = text before the line "## Footer"; sentences split per LINE on
[.!?] + whitespace; words counted over all non-empty body lines except
lines starting with "# "; dialogue = body lines containing a double quote.

Stdlib only.
Run:      python3 tools/measure_chapter.py chapters/*.md
Receipt:  python3 tools/measure_chapter.py chapters/*.md --receipt

Hard failures (exit 1): any sentence over 60 words; a banned "the way"
simile; jargon in prose; a bare panel line (「) in prose.
Warnings: body outside the 2400–3400 band.
"""
import argparse
import re
import statistics
import sys

BAND = (2400, 3400)
MAX_SENT = 60

WAY_ALLOW = [
    "all the way", "on the way", "by the way", "the way of", "opens the way",
    "out of the way", "make way", "give way", "paved the way",
]

JARGON = [
    "adaptation talent", "mortal divine", "true divine", "master foundation",
    "master \u00a7", "system window", "status screen", "readout",
    "second mind", "reward engine", "system voice", "the system",
    "level up", "quest", "interface", "per instruction", "per user",
    "per canon",
]


def split_body(text):
    if "\n## Footer" in text:
        return text.split("\n## Footer")[0]
    m = re.search(r"(?m)^\s*#{1,6}\s*Footer\b", text, re.I)
    return text[:m.start()] if m else text


def measure(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    body = split_body(text)
    lines = [l for l in body.split("\n") if l.strip() and not l.startswith("# ")]
    prose = [l for l in lines if not l.startswith(">")]
    words = len("\n".join(lines).split())
    sents = []
    for l in prose:
        sents += [s for s in re.split(r"(?<=[.!?])\s+", l.strip()) if s]
    lens = [len(s.split()) for s in sents]
    avg = statistics.mean(lens) if lens else 0.0
    med = statistics.median(lens) if lens else 0
    over = [(n, s) for n, s in zip(lens, sents) if n > MAX_SENT]
    dlg = len([l for l in lines if '"' in l])
    per1k = (dlg / words * 1000) if words else 0.0
    bare = [l for l in body.split("\n") if l.strip().startswith("\u300c")]
    low = body.lower()
    way = []
    for m in re.finditer(r"\bthe way\b", low):
        ctx = low[max(0, m.start() - 20):m.end() + 20]
        if not any(a in ctx for a in WAY_ALLOW):
            way.append(ctx.strip())
    jar = [(j, len(re.findall(r"\b" + re.escape(j) + r"\b", low))) for j in JARGON]
    jar = [(j, n) for j, n in jar if n]
    band = "IN" if BAND[0] <= words <= BAND[1] else ("OVER" if words > BAND[1] else "UNDER")
    return dict(file=path, words=words, avg=avg, med=med, mx=max(lens) if lens else 0,
                over=over, dlg=dlg, per1k=per1k, bare=bare, way=way, jar=jar, band=band)


def receipt(r):
    name = r["file"].split("/")[-1].replace(".md", "")
    return (f"{name:28s} {r['words']:5d}w band:{r['band']:5s} avg:{r['avg']:5.1f} "
            f"med:{r['med']:3.0f} max:{r['mx']:3d} dlg:{r['dlg']:3d} ({r['per1k']:4.1f}/1k) "
            f"over60:{len(r['over'])} the-way:{len(r['way'])} "
            f"jargon:{sum(n for _, n in r['jar'])} bare:{len(r['bare'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--receipt", action="store_true")
    args = ap.parse_args()
    hard = False
    for f in args.files:
        r = measure(f)
        if args.receipt:
            print(receipt(r))
        else:
            print("=" * 74)
            print(receipt(r))
        for n, s in r["over"]:
            hard = True
            if not args.receipt:
                print(f"  OVER60 [{n}w]: {s[:120]}{'...' if len(s) > 120 else ''}")
        for w in r["way"]:
            hard = True
            if not args.receipt:
                print(f"  THE-WAY: ...{w}...")
        for j, n in r["jar"]:
            hard = True
            if not args.receipt:
                print(f"  JARGON: '{j}' x{n}")
        for b in r["bare"]:
            hard = True
            if not args.receipt:
                print(f"  BARE PANEL: {b[:80]}")
        if not args.receipt and r["band"] != "IN":
            print(f"  BAND: {r['words']}w outside {BAND[0]}-{BAND[1]} (warning)")
    print("VERDICT:", "FAIL" if hard else "PASS")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
