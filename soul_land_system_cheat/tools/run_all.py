#!/usr/bin/env python3
"""RUN ALL — the serial's whole pipeline in one command.

  1. SYNC MANUSCRIPT  — regenerates manuscript/Chapter_*.md (the footer-free
     reader editions) from chapters/ (the author editions).
  2. STYLE GATE       — the style laws, self-enforcing (hard fails stop the
     pipeline; band warnings are the author's call and do not stop it).
  3. BUILD SITE       — regenerates docs/ (the reading site) from manuscript/.
  4. CHECK PANELS     — diffs every 「...」 panel against foundation/PANELS.md:
     a frozen or stale meter fails the build.

Run from anywhere:  python3 soul_land_system_cheat/tools/run_all.py
After it: commit and push (Pages serves /docs on main).
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERIAL = os.path.dirname(HERE)

def sync_manuscript():
    srcs = sorted(glob.glob(os.path.join(SERIAL, "chapters", "Chapter_*.md")))
    dst_dir = os.path.join(SERIAL, "manuscript")
    os.makedirs(dst_dir, exist_ok=True)
    n = 0
    for s in srcs:
        t = open(s, encoding="utf-8").read()
        body = t.split("\n---\n\n## Footer")[0].split("\n## Footer")[0].rstrip() + "\n"
        out = os.path.join(dst_dir, os.path.basename(s))
        open(out, "w", encoding="utf-8").write(body)
        n += 1
    print(f"[1/4] manuscript synced: {n} reader editions")

def run_gate():
    r = subprocess.run([sys.executable, os.path.join(HERE, "style_gate.py")])
    if r.returncode != 0:
        print("[2/3] STYLE GATE FAILED — pipeline stopped (nothing built on a failing gate)")
        sys.exit(1)
    print("[2/4] style gate passed")

def check_panels():
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_panels.py")])
    if r.returncode != 0:
        print("[4/4] PANEL LEDGER OUT OF SYNC — pipeline stopped")
        sys.exit(1)
    print("[4/4] panel ledger in sync")

def build_site():
    r = subprocess.run([sys.executable, os.path.join(HERE, "build_site.py")])
    if r.returncode != 0:
        sys.exit(1)
    print("[3/4] site built")

if __name__ == "__main__":
    sync_manuscript()
    run_gate()
    build_site()
    check_panels()
