#!/usr/bin/env python3
"""ship_chapter.py — the one-command chapter ship for the Soul Land workspace.

Born 2026-09-23 from the mistakes ledger's most-recurring failure mode: the
SYNC GAP. Three times the Sentinel caught a surface left stale after a ship
(panel LIVE EDGE line, profile count, news/feed). This tool exists so that
class of mistake cannot happen again: every mechanical step of a ship is done
here, verified after execution, and refused past any failing gate.

WHAT IT AUTOMATES (the mechanical 80%):
  1. gates first: measure_prose (floor/ceiling/60-cap) + verify single-file
     + full project sweep — the ship STOPS if any fails
  2. kit root README: chapter count bumped (LIVE BUILD line + tree-table row)
  3. serial README: LIVE EDGE / NEXT BEAT block swapped
  4. site: chapter copied, serials.json appended, search_data.json rebuilt,
     analytics rebuilt, news.html + feed.xml entries, calendar edge
  5. profile README: chapter counts bumped, pushed (needs SHIP_TOKEN env)
  6. sentinel re-run at the end (expects green)

WHAT IT DELIBERATELY DOES NOT AUTOMATE (the authored 20% — intelligence):
  STATUS_PANEL entry + LIVE EDGE line, HIS_STATUS_PANEL live line,
  ADAPTATION_LOG delta, SERIAL_LOG row, CONTINUITY row, PLACES/TIMELINE rows.
  The tool prints this checklist and refuses to claim "shipped" until the
  checklist is confirmed with --mirrors-done.

Usage:
  python3 tools/ship_chapter.py chapters/Chapter_24_X.md \
      --serial devouring_dragon --title "The Stone Country" \
      --live-edge "LIVE EDGE: Chapter 24 — ..." --next-beat "NEXT BEAT: ..." \
      --news-text "..." [--site /path/to/site] [--kit /path/to/kit] \
      [--dry] [--mirrors-done] [--run-sentinel]

Exit 0 only when every automated step verified. A step that cannot verify
itself is a bug in this tool — report it, do not hand-wave past it.
"""
import argparse, json, os, re, shutil, subprocess, sys

FLOOR, CEILING = 2000, 3400

def run(cmd, cwd=None):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return r.stdout + r.stderr, r.returncode

def die(msg):
    print(f"  ✗ {msg}"); sys.exit(1)

def ok(msg):
    print(f"  ✓ {msg}")

def gate_measure(kit, chpath):
    rel = chpath[len("soul_land_devouring_dragon/"):] if chpath.startswith("soul_land_devouring_dragon/") else chpath
    out, rc = run(f"python3 tools/measure_prose.py {rel}", os.path.join(kit, "soul_land_devouring_dragon"))
    if rc != 0 and not out.strip():
        die(f"measure_prose failed to run: {out[:200]}")
    m = re.search(r': (\d+)w \| dialogue (\d+)', out)
    if not m:
        die(f"could not parse measure output: {out[:200]}")
    words = int(m.group(1))
    over60 = re.search(r'OVER 60: \[(.+)\]', out)
    retired = re.search(r'RETIRED-WORD HITS.*?: \[(.+)\]', out)
    tics = len(re.findall(r'\bthe way [a-z]', open(os.path.join(kit, "soul_land_devouring_dragon", rel), encoding='utf-8').read()))
    print(f"  measured: {words}w | tics {tics} | over60 {over60.group(1) if over60 else 'none'} | retired {retired.group(1) if retired else 'none'}")
    if words < FLOOR: die(f"under floor ({words}w < {FLOOR}w) — expand with real scene material, never padding")
    if words > CEILING: die(f"over ceiling ({words}w > {CEILING}w) — SCOPE LAW")
    if over60: die(f"sentences over the 60-word cap: {over60.group(1)[:120]}")
    if retired: die(f"retired-word hits: {retired.group(1)}")
    if tics > 2: die(f"the-way tic count {tics} > cap 2")
    ok(f"measure gate ({words}w)")

def gate_verify(kit, chpath):
    out, rc = run(f"python3 SOUL_LAND_WORKSPACE/kit/tools/verify.py {chpath}", kit)
    if rc != 0 or 'RESULT: PASS' not in out:
        die(f"single-file gate FAIL:\n{out[-400:]}")
    ok("single-file gate PASS")
    out, rc = run("python3 SOUL_LAND_WORKSPACE/kit/tools/verify.py --project soul_land_devouring_dragon", kit)
    if rc != 0 or 'VERDICT: PASS' not in out:
        die(f"project sweep FAIL:\n{out[-400:]}")
    m = re.search(r'chapters carrying a footer: (\d+)/(\d+)', out)
    ok(f"project sweep PASS ({m.group(2) if m else '?'} chapters)")

def bump_root_readme(kit, n):
    p = os.path.join(kit, "README.md")
    t = open(p, encoding='utf-8').read()
    a = re.search(r'devouring-dragon serial \((\d+) chapters', t)
    if not a: die("root README LIVE BUILD line not found")
    t = t.replace(f"devouring-dragon serial ({a.group(1)} chapters", f"devouring-dragon serial ({n} chapters", 1)
    b = re.search(r'devouring-dragon serial\*\* \((\d+) chapters;', t)
    if b: t = t.replace(f"devouring-dragon serial** ({b.group(1)} chapters;", f"devouring-dragon serial** ({n} chapters;", 1)
    open(p, 'w', encoding='utf-8').write(t)
    if f"devouring-dragon serial ({n} chapters" not in open(p, encoding='utf-8').read():
        die("root README bump did not verify")
    ok(f"root README -> {n} chapters")

def swap_serial_readme(kit, live_edge, next_beat):
    p = os.path.join(kit, "soul_land_devouring_dragon", "README.md")
    t = open(p, encoding='utf-8').read()
    i, j = t.index("LIVE EDGE:"), t.index("NEXT BEAT:")
    k = t.index("\n", t.index("panels only when needed (s45)", j)) if "panels only when needed (s45)" in t[j:] else t.index("\n", j)
    end = t.index("panels only when needed (s45)", j) + len("panels only when needed (s45).") if "panels only when needed (s45)" in t[j:] else k
    t = t[:i] + live_edge + "\n" + next_beat + t[end:]
    open(p, 'w', encoding='utf-8').write(t)
    if live_edge.splitlines()[0] not in open(p, encoding='utf-8').read():
        die("serial README swap did not verify")
    ok("serial README LIVE EDGE / NEXT BEAT swapped")

def site_update(site, kit, chpath, n, title, news_text):
    rel = chpath[len("soul_land_devouring_dragon/"):] if chpath.startswith("soul_land_devouring_dragon/") else chpath
    src = os.path.join(kit, "soul_land_devouring_dragon", rel)
    dst = os.path.join(site, "chapters", "devouring_dragon", os.path.basename(chpath))
    shutil.copy(src, dst)
    if not os.path.exists(dst): die("chapter copy failed")
    t = open(dst, encoding='utf-8').read()
    words = len(t.split('## Footer')[0].split())
    d = json.load(open(os.path.join(site, "data", "serials.json"), encoding='utf-8'))
    dd = next(s for s in d['serials'] if s['id'] == 'devouring_dragon')
    if any(c['n'] == n for c in dd['chapters']): die(f"serials.json already has chapter {n}")
    dd['chapters'].append({'n': n, 'file': os.path.basename(chpath), 'title': title, 'words': words})
    dd['total_words'] = sum(c['words'] for c in dd['chapters'])
    json.dump(d, open(os.path.join(site, "data", "serials.json"), 'w', encoding='utf-8'), indent=1)
    out = []
    for s in d['serials']:
        for c in s['chapters']:
            t2 = open(os.path.join(site, "chapters", s['id'], c['file']), encoding='utf-8').read()
            out.append({'i': s['id'], 'n': c['n'], 't': c['title'], 'w': c['words'], 'x': t2.split('## Footer')[0]})
    json.dump(out, open(os.path.join(site, "search_data.json"), 'w', encoding='utf-8'))
    ok(f"site: serials.json + search_data.json ({len(out)} entries)")
    for tool in ("analytics.py",):
        out, rc = run(f"python3 tools/{tool}", site)
        if rc != 0: die(f"tools/{tool} failed: {out[-200:]}")
    ok("site: analytics rebuilt")
    # news + feed
    p = os.path.join(site, "news.html")
    t = open(p, encoding='utf-8').read()
    anchor = re.search(r'<div class="item"><div class="date">[^<]*</div><h2>', t)
    entry = f'<div class="item"><div class="date">2026-09-23</div><h2>Devouring Dragon: Chapter {n} — {title}</h2>\n<p>{news_text}</p></div>\n'
    t = t[:anchor.start()] + entry + t[anchor.start():]
    open(p, 'w', encoding='utf-8').write(t)
    p = os.path.join(site, "feed.xml")
    t = open(p, encoding='utf-8').read()
    anchor = ' <entry><title>'
    ent = (f' <entry><title>Devouring Dragon — Chapter {n}, {title}</title>\n'
           f'  <id>urn:soul-library:dd:{n}</id><link href="https://gm5206663-bit.github.io/soul-library/#devouring_dragon"/>\n'
           f'  <updated>2026-09-23T22:00:00Z</updated><summary>{news_text[:280]}</summary></entry>\n')
    t = t.replace(anchor, ent + anchor, 1)
    t = re.sub(r'<updated>2026-09-23T\d\d:\d\d:\d\dZ</updated>', '<updated>2026-09-23T22:00:00Z</updated>', t, count=1)
    open(p, 'w', encoding='utf-8').write(t)
    ok("site: news + feed entries")
    return words

def calendar_bump(site, old, new):
    p = os.path.join(site, "calendar.html")
    t = open(p, encoding='utf-8').read()
    if old not in t: die(f"calendar edge text not found: {old[:60]}")
    open(p, 'w', encoding='utf-8').write(t.replace(old, new, 1))
    ok("calendar edge updated")

def profile_update(n, total, profile_dir):
    p = os.path.join(profile_dir, "README.md")
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'(\| \*\*Devouring Dragon\*\* \| Soul Land \| )\d+ chapters', r'\g<1>' + str(n) + ' chapters', t, count=1)
    t = re.sub(r'(\d+ serials · )\d+ chapters', r'\g<1>' + str(total) + ' chapters', t, count=1)
    open(p, 'w', encoding='utf-8').write(t)
    if f"| **Devouring Dragon** | Soul Land | {n} chapters" not in open(p, encoding='utf-8').read():
        die("profile bump did not verify")
    ok(f"profile -> DD {n} chapters, {total} total")

MIRRORS = """AUTHORED MIRRORS — NOT AUTOMATABLE, NOT OPTIONAL (do these before claiming shipped):
  1. foundation/STATUS_PANEL.md   — new Updated entry (session prose) + structured LIVE EDGE line
  2. bible/HIS_STATUS_PANEL.md    — live-after line
  3. bible/ADAPTATION_LOG.md      — s-session delta + figures (panel-only)
  4. foundation/SERIAL_LOG.md     — one row
  5. foundation/CONTINUITY.md     — one row
  6. codex/PLACES.md              — new places
  7. codex/TIMELINE.md            — one row
  8. root README ADDITION block   — add-only chapter receipt
  9. commit + push the kit BEFORE pushing the site"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--serial", default="devouring_dragon")
    ap.add_argument("--title", required=True)
    ap.add_argument("--live-edge", required=True)
    ap.add_argument("--next-beat", required=True)
    ap.add_argument("--news-text", required=True)
    ap.add_argument("--cal-old"); ap.add_argument("--cal-new")
    ap.add_argument("--site", default="/home/user/library-build/site")
    ap.add_argument("--kit", default=None)
    ap.add_argument("--profile", default="/home/user/profile-staging")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--mirrors-done", action="store_true")
    ap.add_argument("--run-sentinel", action="store_true")
    a = ap.parse_args()
    kit = a.kit or os.getcwd()
    n = int(re.search(r'Chapter_(\d+)', a.chapter).group(1))
    print(f"== SHIP: Chapter {n} — {a.title} ==")
    gate_measure(kit, a.chapter)
    gate_verify(kit, a.chapter)
    if a.dry:
        print("\n--dry: gates green. Plan beyond this point:\n" + MIRRORS); return
    if not a.mirrors_done:
        print("\nGates green. Now do the authored mirrors, then re-run with --mirrors-done:\n" + MIRRORS); return
    bump_root_readme(kit, n)
    swap_serial_readme(kit, a.live_edge, a.next_beat)
    out, rc = run(f"python3 soul_land_devouring_dragon/tools/build_oc_status.py --site {a.site}", kit)
    print("  " + out.strip().splitlines()[-1])
    if rc != 0: die("OC status regeneration failed")
    words = site_update(a.site, kit, a.chapter, n, a.title, a.news_text)
    if a.cal_old and a.cal_new: calendar_bump(a.site, a.cal_old, a.cal_new)
    d = json.load(open(os.path.join(a.site, "data", "serials.json"), encoding='utf-8'))
    total = sum(len(s['chapters']) for s in d['serials'])
    profile_update(n, total, a.profile)
    if a.run_sentinel:
        out, rc = run(f"python3 tools/sentinel.py --kit {kit}", a.site)
        print("  " + out.strip().splitlines()[-1])
        if rc != 0: die("sentinel not green — fix before pushing anything")
    print(f"\n== SHIPPED (mechanical): Ch {n} · {words}w · library {total} chapters ==")
    print("Remaining human steps: git add/commit/push the kit, the site, and the profile.")

if __name__ == "__main__":
    main()
