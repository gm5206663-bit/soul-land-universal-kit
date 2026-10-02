#!/usr/bin/env python3
"""Register measurement — house gate shape for the SL3 prequel.
Usage: python3 measure_sl3p.py <chapter.md>
Metrics: body words, ALL avg/median/over-60, NARR (non-quoted) avg/median/over-60,
dialogue paras, CJK chars.
"""
import re, sys, statistics

path = sys.argv[1]
t = open(path).read()

# body: drop header blockquote lines, horizontal rules, and the trailing meta italic
lines = []
for ln in t.split('\n'):
    s = ln.strip()
    if not s: lines.append(ln); continue
    if s.startswith('>'): continue
    if s == '---': continue
    if s.startswith('# '): continue
    lines.append(ln)
body = '\n'.join(lines).strip()

words = re.findall(r"[A-Za-z0-9'’\-]+", body)
body_words = len(words)

def sent_split(x):
    out = []
    for para in x.split('\n'):
        out.extend(s for s in re.split(r'(?<=[.!?])\s+', para.strip()) if s)
    return out

sents = sent_split(body)
all_lens = [len(re.findall(r"[A-Za-z0-9'’\-]+", s)) for s in sents]
all_lens = [n for n in all_lens if n > 0]

def stats(lens):
    if not lens: return (0, 0, 0)
    return (round(sum(lens)/len(lens), 1), round(statistics.median(lens), 1), sum(1 for n in lens if n > 60))

# dialogue paragraphs
dlg = sum(1 for ln in body.split('\n') if ln.strip().startswith('"'))

# NARR = strip quoted spans, then sentence stats on remainder
narr = re.sub(r'"[^"]*"', ' ', body)
narr_lens = [len(re.findall(r"[A-Za-z0-9'’\-]+", s)) for s in sent_split(narr)]
narr_lens = [n for n in narr_lens if n > 0]

cjk = len(re.findall(r'[\u4e00-\u9fff]', t))

print(f"file: {path}")
print(f"body words        : {body_words}")
print(f"ALL  avg/med/o60  : {stats(all_lens)}")
print(f"NARR avg/med/o60  : {stats(narr_lens)}")
print(f"dialogue paras    : {dlg}")
print(f"CJK chars         : {cjk}")
print("--- over-60 ALL sentences ---")
for s in sents:
    if len(re.findall(r"[A-Za-z0-9'’\-]+", s)) > 60:
        print("  *", s[:160])
print("--- over-60 NARR sentences ---")
for s in sent_split(narr):
    if len(re.findall(r"[A-Za-z0-9'’\-]+", s)) > 60:
        print("  *", s[:160])
