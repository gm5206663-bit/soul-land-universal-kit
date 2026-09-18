#!/usr/bin/env python3
"""BUILD_STATUS — regenerate LIN_HAO_STATUS.md from the derived state.

WHY THIS EXISTS
  LIN_HAO_STATUS.md said "End of Chapter 18" while the story was at chapter 61. CONTINUATION_PROMPT.md
  said chapter 28. POWER_MODEL.md still described a rank-30 wall that opened in ch40. Every one of them
  was hand-maintained, and every one of them rotted. A hand-maintained status file in a 61-chapter
  project is not a document, it is a lie with a filename.

  So the status file is now GENERATED. Run it after every chapter. `verify_stale.py` fails the suite
  if the generated file is out of date, so it cannot rot silently again.

Usage:
    python3 checks/build_status.py            # regenerate LIN_HAO_STATUS.md
    python3 checks/build_status.py --check    # exit 1 if the file on disk is out of date
"""
import os, re, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import state as STATE
import ensemble_schedule as ES

OUT = os.path.join(ROOT, "LIN_HAO_STATUS.md")
MARK_BEGIN = "<!-- GENERATED-BY checks/build_status.py — DO NOT HAND-EDIT -->"
MARK_END = "<!-- END GENERATED -->"


def build():
    st = STATE.derive()
    n = st["latest_chapter"]
    r = st["current_rank"]
    sched = ES.SCHEDULE.get(n, {})

    # ensemble at the current chapter
    ens = []
    for key in ("wulin", "xiexie", "guyue", "xiaoyan", "yangzi", "jinxi", "weixf"):
        if key in sched:
            ens.append(sched[key][1])

    ceiling = st["rank_ceiling"]
    head = st["rings"]["count"]
    colour = st["rings"]["colour"]
    hawk = st["current_hawk_years"]
    eff_lo, eff_hi = st["effective_rank_band"]
    d_lo, d_hi = st["effective_rank_delta"]

    L = []
    A = L.append
    A(f"# LIN HAO — CURRENT STATUS")
    A("")
    A(MARK_BEGIN)
    A("")
    A(f"**Regenerated from the chapter footers by `checks/build_status.py`. Do not hand-edit this block;**")
    A(f"**edit the footers or `checks/ensemble_schedule.py` and re-run the generator.**")
    A("")
    A(f"## Position: end of Chapter {n}")
    A("")
    A(f"Current soul rank {r}. Current spiritual power {st['current_spiritual_power']}. "
      f"(This line exists so the SYNC check can find both values.)")
    A("")
    A("| Line | Value |")
    A("|---|---|")
    # verify.py's SYNC check looks for the literal "rank <N>", so the rank line must contain it.
    A(f"| **Rank** | rank **{r}** — **{st['current_realm']}** |")
    A(f"| **Effective combat power** | 🔴 **{st['effective_realm']} ({eff_lo}–{eff_hi})**, ceiling {st['effective_realm']} peak — **{d_lo}–{d_hi} ranks above his own number** |")
    A(f"| **Rings** | **{head} {colour}** — perfectly compatible, so they exceed normal {colour} |")
    A(f"| **Spiritual power** | **{st['current_spiritual_power']}** |")
    A(f"| **Spirit soul (Gale Hawk)** | **{hawk:,} years** |")
    A(f"| **Ledger (opponents adapted)** | **{st['current_ledger']}** |")
    A(f"| **Smithing** | **{st['current_smith_rank']}th rank — {st['current_smith_title']}** (canon c40: 1–2 Master · 3–4 Grandmaster · 5–6 Master Craftsman · 7–8 Saint Craftsman · 9 Divine Craftsman) |")
    A(f"| **Swordsmanship** | **⚔️ Sword Intent** — absurd at ten; adults spend lifetimes below Intent |")
    A(f"| **Rank ceiling** | **{ceiling}** — {st['rank_ceiling_reason']} |")
    A("")
    A("## 🔴 THE BENCHMARK — normal 3rd / 4th / 5th-ring masters, from canon")
    A("")
    A("| | normal 3-ring | normal 4-ring | normal 5-ring | **LIN HAO** |")
    A("|---|---|---|---|---|")
    A("| Age | 14–18 | 15–23 | adult | **10** |")
    A("| Rings | 2 yellow + 1 purple, or 3 yellow | mixed | mostly purple | **3 PURPLE, perfectly compatible** |")
    A("| Soul skills | hundred-year + one thousand-year | mixed | mostly thousand-year | **all thousand-year tier** |")
    A("| Trump card | — | — | — | **🃏 Hawk-Soul Union** |")
    A("| Sword realm | — | — | — | **Sword Intent** |")
    A("| Own techniques | — | — | — | **five self-created strokes** |")
    A(f"| **Effective power** | Soul Elder | Soul Ancestor | **Soul King** | **{st['effective_realm']}** |")
    A("")
    A("Canon, verbatim: *\"Normally, soul masters don't get a ten-thousand-year soul ring until rank 50.\"*")
    A(f"His fourth ring is planned at ten-thousand-year+. **He will do at ~40 what canon says waits for 50.**")
    A("")
    A("## Ensemble at this chapter (from `checks/ensemble_schedule.py`)")
    A("")
    for e in ens:
        A(f"- {e}")
    A("")
    A("## 🔴 LOCKED — current as of the last regeneration")
    A("")
    A("> ⚠️ This block is hardcoded prose. It has gone stale twice (F1 was still listed as unwritten")
    A("> after it was written; and it carried the retracted claim that Gu Yue \"cannot beat him\" when he")
    A("> says at ch58 that she has beaten him five times). **When a law changes, change it here too.**")
    A("")
    A("- ✅ **F1 CLOSED (ch40).** The purple-ring skill evolution is on-page: Gale Talon and Hawk-Soul")
    A("  Union both upgraded to thousand-year tier when the rings re-formed. Canon: *\"if his spirit soul")
    A("  was upgraded, then the soul skills it provided would be upgraded too.\"*")
    A("- **THE FOURTH RING — LOCKED (v2.98).** Second spirit soul is a **DRAGON, ice + water dual")
    A("  element, ten-thousand-year+**. Absorption takes **ONE MONTH** and changes everything — martial")
    A("  soul, body, **appearance (he ends up looking ~16)**, a little of his personality, the rings.")
    A("  **Rank 40 → 45 directly.** Martial soul gains water + ice, evolves to **TOP-LEVEL**, and")
    A("  **changes name** (proposed: Frost Abyss Sword). Gains a **DOMAIN** (martial-soul innate, not a")
    A("  ring skill) and **DOMINEER** as the fourth ring's skill. 🔴 **\"Divine Stormbringer\" is")
    A("  CANCELLED** — never name or foreshadow it. 🔴 **The month gets no invented story time:** canon")
    A("  events happen without him; the ensemble carries it.")
    A(f"- **THE EFFECTIVE POWER LAW — DERIVED, not hardcoded.** Effective **{st['effective_realm']}** "
      f"({st['effective_rank_band'][0]}–{st['effective_rank_band'][1]}), from his rank and ring count.")
    A("  A lower-realm character defeating him is nonsense **from ch40**. 🔴 The band moved at ch71")
    A("  (the fourth ring, the top-level martial soul and the Domain); state.py computes it.")
    A("  🔴 **But Gu Yue HAS beaten him five times** — he says so at ch53 and ch58. Those happened")
    A("  before, at two rings. **Do not erase them to satisfy the law.**")
    A("- **HE IS NOT DEAD (D017).** He lives through all of Soul Land 3 and beyond. His fate is 🔓")
    A("  OPEN. **Soul Land 4 is a NEW OC**, not him.")
    A("- **CLASSIFICATION: 「全能系」 COMPREHENSIVE SYSTEM — he FOUNDED it at ch59** by writing the word")
    A("  in the blank line under the six squares. The word becomes real **because of him**, as he grows")
    A("  strong and famous, and **he is alive to see it.**")
    A("- **Standing instruction:** when writing Lin Hao, **imagine what he is.** Nothing about him is")
    A("  written at baseline. See `THE_CODEX.md` §THE ADVANTAGE LEDGER and §HOW LIN HAO IS WITH PEOPLE.")
    A("")
    A("## Progression traces (derived, not typed)")
    A("")
    A(f"- rank: {st['rank_by_chapter'].get(str(min(int(k) for k in st['rank_by_chapter'])), '?')} → **{r}** across {len(st['rank_by_chapter'])} recorded chapters")
    spk = sorted(int(k) for k in st["spiritual_power_by_chapter"])
    if spk:
        A(f"- spiritual power: {st['spiritual_power_by_chapter'][str(spk[0])]} → **{st['current_spiritual_power']}** across {len(spk)} recorded chapters")
    hk = sorted(int(k) for k in st["hawk_by_chapter"])
    if hk:
        A(f"- hawk: {st['hawk_by_chapter'][str(hk[0])]:,} → **{hawk:,}** years across {len(hk)} recorded chapters")
    smk = sorted(int(k) for k in st["smith_by_chapter"])
    if smk:
        A(f"- smithing: {st['smith_by_chapter'][str(smk[0])]} → **{st['current_smith_rank']}** ({st['current_smith_title']}) across {len(smk)} recorded chapters")
    A("")
    A("Full canon citations for every ensemble number: **`CHARACTER_STATS.md`**.")
    A("Full laws: **`THE_CODEX.md`** — §THE ADVANTAGE LEDGER, §THE REALM GAP LAW, §THE FOURTH RING LAW.")
    A("")
    A(MARK_END)
    out = "\n".join(L) + "\n"

    # Append the PERMANENT REFERENCE PANELS (physical panel, techniques panel, cultivation
    # speed, the specialty). These are hand-maintained reference material, not per-chapter
    # state, so they live in LIN_HAO_PANELS.md and are appended on every regeneration.
    # THEY ARE THE ONLY COPY — the branch files they were merged from were deleted.
    panels = os.path.join(ROOT, "LIN_HAO_PANELS.md")
    if os.path.exists(panels):
        out += "\n---\n\n" + open(panels, encoding="utf-8").read()
    else:
        out += ("\n---\n\n> ⚠️ **LIN_HAO_PANELS.md IS MISSING.** The physical panel, techniques panel,\n"
                "> cultivation speed and specialty panels live there and are the only copy.\n")
    return out


def main():
    text = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        m = re.search(re.escape(MARK_BEGIN) + r".*?" + re.escape(MARK_END), cur, re.S)
        cur_block = m.group(0) if m else ""
        new_block = text[text.find(MARK_BEGIN):text.find(MARK_END) + len(MARK_END)]
        if cur_block != new_block:
            print("build_status: LIN_HAO_STATUS.md is STALE — run `python3 checks/build_status.py`")
            sys.exit(1)
        print("build_status: LIN_HAO_STATUS.md is current")
        sys.exit(0)

    # preserve any hand-written material ABOVE the generated block
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
    pre = ""
    if MARK_BEGIN in old:
        # Keep only the non-heading preamble (e.g. the archive pointer comment). Headings are
        # regenerated, so preserving them duplicates the title on every run — that bug made the
        # file non-idempotent and would have grown the file by two lines forever.
        head = old[:old.find(MARK_BEGIN)]
        # 🔴 Drop BOTH headings and any previously-emitted banner comment. The banner is
        # re-emitted fresh below on every run. Preserving it is what made it say
        # "the story was at chapter 61" forever — a second copy of a number, exactly the
        # defect §THE TWO-COPIES LAW exists to prevent.
        kept = [l for l in head.split("\n")
                if not l.startswith("#") and not l.startswith("<!--")]
        pre = ("\n".join(kept).strip() + "\n\n") if "\n".join(kept).strip() else ""
    elif old:
        # first conversion: archive the hand-written file rather than destroy it
        arc = os.path.join(ROOT, "LIN_HAO_STATUS_ARCHIVE_ch18.md")
        if not os.path.exists(arc):
            open(arc, "w", encoding="utf-8").write(old)
            print(f"build_status: old hand-written file archived to {os.path.basename(arc)}")
        import paths as _P
        arc = os.path.join(_P.CODEX, "98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz")
        pre = ("<!-- This file is GENERATED by checks/build_status.py. The previous hand-written "
               "version was 43 chapters behind the story the day it was retired; it is archived "
               "in CODEX/98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz. -->\n\n")
    # the banner is DERIVED, never hardcoded, and is emitted on every run
    _banner = ("<!-- This file is GENERATED by checks/build_status.py from checks/state.json, which is "
               "derived from the chapter footers. DO NOT HAND-EDIT. The previous hand-written version "
               "of this file was 43 chapters behind the story on the day it was retired, and is "
               "archived in CODEX/98_SUPERSEDED_DOCS_ARCHIVE_2026-08-28.tar.gz. -->\n\n")
    open(OUT, "w", encoding="utf-8").write(_banner + pre + text)
    st = STATE.derive()
    print(f"build_status: LIN_HAO_STATUS.md regenerated — ch{st['latest_chapter']}, "
          f"rank {st['current_rank']} ({st['current_realm']}), effective {st['effective_realm']}")


if __name__ == "__main__":
    main()
