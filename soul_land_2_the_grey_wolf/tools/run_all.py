#!/usr/bin/env python3
"""RUN ALL — the serial's whole pipeline in one command.

  1. SCOPE FIXTURE    — proves the gate can still fail. House law: a gate
     that has only ever been seen to pass is a gate nobody has tested; if
     you add an eighth gate, add an eighth fixture. Seven fixtures break
     the tree on purpose, run the gate, and restore it. Skipped if bash
     is not available.
  2. SYNC MANUSCRIPT  — regenerates manuscript/Chapter_*.md (the footer-free
     reader editions) from chapters/ (the author editions).
  3. STYLE GATE       — the style laws, self-enforcing (hard fails stop the
     pipeline; band warnings are the author's call and do not stop it).
  4. BUILD SITE       — regenerates docs/ (the reading site) from manuscript/.
  5. CHECK PANELS     — diffs every 「...」 panel against foundation/PANELS.md:
     a frozen or stale meter fails the build.

Run from anywhere:  python3 tools/run_all.py
After it: commit and push (Pages serves /docs on main).
"""
import glob, os, re, shutil, subprocess, sys

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
    # FULL edition — every chapter in one reader file
    if srcs:
        parts = []
        for s in srcs:
            t = open(s, encoding="utf-8").read()
            b = t.split("\n---\n\n## Footer")[0].split("\n## Footer")[0].rstrip()
            parts.append(b)
        full = "# THE GREY WOLF — the full edition\n\n" + "\n\n---\n\n".join(parts) + "\n"
        open(os.path.join(dst_dir, "FULL.md"), "w", encoding="utf-8").write(full)
        print(f"[2/5] manuscript synced: {n} reader editions + FULL edition")
    else:
        print(f"[2/5] manuscript synced: {n} reader editions")

def scope_fixture():
    """Step 1 — break the tree seven ways and confirm the gate notices."""
    script = os.path.join(HERE, "gate_selftest.sh")
    if not os.path.exists(script) or shutil.which("bash") is None:
        print("[1/5] scope fixture skipped (no bash)")
        return
    r = subprocess.run(["bash", script], cwd=SERIAL, capture_output=True, text=True)
    tail = [l.strip() for l in r.stdout.strip().split("\n") if l.strip()]
    if r.returncode != 0:
        print(r.stdout)
        print("[1/5] SCOPE FIXTURE FAILED — the gate is not trustworthy, nothing built")
        sys.exit(1)
    print(f"[1/5] scope fixture passed — {tail[-1] if tail else ''}")


def run_gate():
    r = subprocess.run([sys.executable, os.path.join(HERE, "style_gate.py")])
    if r.returncode != 0:
        print("[3/5] STYLE GATE FAILED — pipeline stopped (nothing built on a failing gate)")
        sys.exit(1)
    print("[3/5] style gate passed")

def check_panels():
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_panels.py")])
    if r.returncode != 0:
        print("[5/5] PANEL LEDGER OUT OF SYNC — pipeline stopped")
        sys.exit(1)
    print("[5/5] panel ledger in sync")

def build_site():
    r = subprocess.run([sys.executable, os.path.join(HERE, "build_site.py")])
    if r.returncode != 0:
        sys.exit(1)
    print("[4/5] site built")

if __name__ == "__main__":
    scope_fixture()
    sync_manuscript()
    run_gate()
    build_site()
    check_panels()
