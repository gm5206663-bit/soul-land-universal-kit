#!/usr/bin/env python3
"""BUILD SITE — generates the reading site from manuscript/ into /docs.

Run from anywhere:  python3 soul_land_system_cheat/tools/build_site.py
Reads manuscript/Chapter_*.md (footer-free reader editions), writes
docs/index.html + docs/chapter_NN.html. Self-contained pages: inline CSS
only, no external fonts, scripts, or images. Regenerate after every chapter
change, then commit and push (GitHub Pages serves /docs on main).
"""
import glob, os, re, sys, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SERIAL = os.path.dirname(HERE)
DOCS = os.path.join(SERIAL, "docs")

TEASERS = {}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#faf7f0;color:#24211c;font-family:Georgia,'Times New Roman',serif;
     line-height:1.75;font-size:19px;-webkit-font-smoothing:antialiased}
.wrap{max-width:37em;margin:0 auto;padding:4.5em 1.4em 6em}
.kicker{font-family:'Courier New',monospace;font-size:12px;letter-spacing:.22em;
        text-transform:uppercase;color:#8a7f6a;margin-bottom:1.1em}
h1{font-weight:normal;font-size:1.9em;line-height:1.25;margin-bottom:.5em}
h1 .num{color:#9a8f78}
.byline{color:#6f6552;font-style:italic;margin-bottom:2.2em}
.teaser{color:#4d463a;margin-bottom:.6em}
nav.toc{margin-top:2.6em;border-top:1px solid #e2dac9;padding-top:1.6em}
nav.toc a{display:block;color:#24211c;text-decoration:none;padding:.75em 0;
          border-bottom:1px solid #eee6d6}
nav.toc a:hover{background:#f3eee2}
nav.toc .ct{font-size:1.06em}
nav.toc .ct .n{color:#9a8f78;font-family:'Courier New',monospace;font-size:.85em;margin-right:.6em}
nav.toc .tz{display:block;color:#6f6552;font-size:.9em;font-style:italic;margin-top:.15em}
.foot{margin-top:3.4em;border-top:1px solid #e2dac9;padding-top:1.3em;
      font-family:'Courier New',monospace;font-size:12.5px;color:#8a7f6a;letter-spacing:.06em}
.foot a{color:#6f6552}
.panel{font-family:'Courier New',monospace;font-size:.86em;color:#3d4a5c;
       background:#eef0f3;border-left:3px solid #9fb0c4;padding:.9em 1.1em;
       margin:1.7em 0;line-height:1.9;letter-spacing:.02em}
.panel p{display:block}
.scene{margin:2.6em 0;text-align:center;color:#b3a98f;letter-spacing:.6em}
p{margin:0 0 1.15em}
em{font-style:italic}
.navbar{display:flex;justify-content:space-between;margin-bottom:3em;
        font-family:'Courier New',monospace;font-size:13px}
.navbar a{color:#6f6552;text-decoration:none}
.navbar a:hover{color:#24211c}
.status{font-family:'Courier New',monospace;font-size:12.5px;color:#8a7f6a;
        margin-top:2.4em;letter-spacing:.05em}
"""

def esc(s): return html.escape(s, quote=False)

def md_inline(s):
    s = esc(s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s

def page(title, body, kicker="THE GREY WOLF — a Soul Land 2 fan fiction"):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}</style></head>
<body><div class="wrap">
<div class="kicker">{esc(kicker)}</div>
{body}
<div class="foot">THE GREY WOLF · fanfiction · Soul Land (Douluo Dalu) belongs to Tang Jia San Shao.<br>
The story is fiction about fictional people. Source &amp; bibles: github.com/gm5206663-bit/soul-land-2-the-grey-wolf</div>
</div></body></html>"""

def chapter_html(src, prev, nxt, idx, total):
    t = open(src, encoding="utf-8").read().strip()
    lines = t.split("\n")
    title = lines[0].lstrip("# ").strip()
    num = idx
    out, panel = [], []
    def flush():
        if panel:
            out.append('<div class="panel">' + "".join(f"<p>{md_inline(p)}</p>" for p in panel) + "</div>")
            panel.clear()
    for raw in lines[1:]:
        l = raw.strip()
        if not l:
            flush(); continue
        if l.startswith(">"):
            panel.append(l.lstrip("> ").strip()); continue
        if l == "---":
            flush(); out.append('<div class="scene">◆ ◆ ◆</div>'); continue
        if l.startswith("#"):
            flush(); out.append(f"<h2>{md_inline(l.lstrip('# '))}</h2>"); continue
        flush(); out.append(f"<p>{md_inline(l)}</p>")
    flush()
    nav = ['<div class="navbar">']
    nav.append(f'<span>{f"&larr; {esc(prev[1])}" if prev else "&nbsp;"}</span>' if prev else "<span>&nbsp;</span>")
    nav.append('<a href="index.html">Index</a>')
    nav.append(f'<span><a href="chapter_{nxt[0]:02d}.html">{esc(nxt[1])} &rarr;</a></span>' if nxt else "<span>&nbsp;</span>")
    nav.append("</div>")
    head = f'<h1><span class="num">{num}.</span> {esc(title.split(":",1)[-1].strip() if ":" in title else title)}</h1>'
    body = "\n".join(nav) + head + "\n" + "\n".join(out) + \
        f'\n<div class="status">{"THE STORY CONTINUES." if nxt else "END OF THE WRITTEN ARC — the serial continues."}</div>'
    return page(f"{title} — The Grey Wolf", body)

def build():
    os.makedirs(DOCS, exist_ok=True)
    srcs = sorted(glob.glob(os.path.join(SERIAL, "manuscript", "Chapter_*.md")))
    total = len(srcs)
    titles = []
    for i, s in enumerate(srcs):
        first = open(s, encoding="utf-8").readline().lstrip("# ").strip()
        titles.append(first)
    for i, s in enumerate(srcs):
        prev = (i, titles[i-1]) if i > 0 else None
        nxt = (i+2, titles[i+1]) if i < total-1 else None
        out = chapter_html(s, prev, nxt, i+1, total)
        open(os.path.join(DOCS, f"chapter_{i+1:02d}.html"), "w", encoding="utf-8").write(out)
    toc = []
    for i, ti in enumerate(titles):
        tz = TEASERS.get(i+1, "")
        nm = ti.split(":", 1)[-1].strip() if ":" in ti else ti
        toc.append(f'<a href="chapter_{i+1:02d}.html"><span class="ct"><span class="n">{i+1:02d}</span>{esc(nm)}</span>'
                   f'<span class="tz">{esc(tz)}</span></a>')
    today = datetime.date.today().isoformat()
    body = f"""<h1>The Grey Wolf</h1>
<div class="byline">a Soul Land 2 fan fiction — a rank-one wolf, a silent Ledger, and the road beside Huo Yuhao</div>
<p class="teaser">A tallykeeper dies on Earth and is born again on the Douluo Continent, six
years before the story he has already read begins. A wolf, a single rank of
innate soul power, and a thing behind his eyes that counts everything —
slots, meters, and a full status panel. He knows this world's book. He
intends to live past his page in it.</p>
<nav class="toc">
{''.join(toc)}
</nav>
<div class="status">Updated {today} · {"foundations locked — no chapters yet; the serial begins at the author's word" if total == 0 else f"chapters 1–{total} · the serial continues"}</div>"""
    open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(
        page("The Grey Wolf — a Soul Land 2 fan fiction", body))
    print(f"site built: {total} chapters + index -> {DOCS}")
    # SCOPE LAW — publish only what was gated, and say how much that was.
    n_src = len(glob.glob(os.path.join(SERIAL, "manuscript", "Chapter_*.md")))
    full = os.path.join(SERIAL, "manuscript", "FULL.md")
    full_ch = len(re.findall(r"(?m)^# Chapter \d+", open(full, encoding="utf-8").read())) if os.path.exists(full) else 0
    print(f"COVERAGE: manuscript/ {n_src} of {n_src} reader editions -> docs/ {total} chapter pages "
          f"+ index · FULL.md {full_ch} of {n_src} chapters")
    if total != n_src or (n_src and full_ch != n_src):
        print("SCOPE — the site, the reader editions and the FULL edition disagree")
        sys.exit(1)

if __name__ == "__main__":
    build()
