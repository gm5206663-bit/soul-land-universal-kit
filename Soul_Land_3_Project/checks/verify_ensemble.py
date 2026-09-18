#!/usr/bin/env python3
"""LAYER 4 — ENSEMBLE VERIFICATION.

The mistake this exists to prevent, stated plainly:
  * Tang Wulin sat at rank 15 from ch13 to ch61 (49 chapters) while canon moved him 15 -> 16 -> 17.
  * Xie Xie sat at rank 21 from ch17 to ch61; Wei Xiaofeng at 22 from ch21 to ch61.
  * Gu Yue was never given a soul-power rank in any footer.
  * Zhang Yangzi and Wang Jinxi were labelled "gone" / "~27" with no schedule, and ch60 said
    they were "going" to Shrek — canon has them transfer out of class zero, and canon c288 puts
    only four people in the Shrek working-student dorm.

Checks performed
  1. Every chapter footer carries exactly one authoritative ensemble block.
  2. Every rank in that block equals the scheduled rank for that chapter.
  3. No stale per-character ensemble line survives elsewhere in the footer (self-contradiction).
  4. No canon character is frozen across more chapters than the schedule allows.
  5. The Shrek roster is four, not six.
  6. Hard canon numbers are never contradicted in prose.

Expected values live in checks/ensemble_schedule.py and must trace to CHARACTER_STATS.md §1.
"""
import re, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ensemble_schedule as ES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, "chapters")
MARK = "### Ensemble — canon-verified state"

KEYS = {
    "wulin":   ("Tang Wulin",   r"(?<![A-Za-z])Tang Wulin"),
    "xiexie":  ("Xie Xie",      r"(?<![A-Za-z])Xie Xie"),
    "guyue":   ("Gu Yue",       r"(?<![A-Za-z])Gu Yue"),
    "yangzi":  ("Zhang Yangzi", r"(?<![A-Za-z])Zhang Yangzi"),
    "jinxi":   ("Wang Jinxi",   r"(?<![A-Za-z])Wang Jinxi"),
    "weixf":   ("Wei Xiaofeng", r"(?<![A-Za-z])Wei Xiaofeng"),
    "xiaoyan": ("Xu Xiaoyan",   r"(?<![A-Za-z])Xu Xiaoyan"),
}
NAMES = "|".join(v[0] for v in KEYS.values())

errors, warnings, notes = [], [], []

# chapter after which a character no longer appears in the story at all
LEFT_AT = {"jinxi": 43}   # Wang Jinxi leaves in ch43 (canon ch 153 "Leaving")
observed = {}
latest = 0

def rank_in(line):
    m = re.search(r"\brank\s*\**(\d{1,3})", line)
    return int(m.group(1)) if m else None

for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md")),
                   key=lambda p: int(re.search(r"(\d+)", os.path.basename(p)).group(1))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    latest = max(latest, n)
    text = open(path, encoding="utf-8", errors="replace").read()

    # footer starts at the house's state anchor; the fallbacks cover the two
    # era-conventions (ch73-79 'Chapter end state', ch113-116 'Character Progression',
    # which carry no 'Character States' at all). PRIORITY, not min(): chapters 1-72
    # carry BOTH 'Character Progression' (mid-file) and 'Character States', and the
    # authoritative state region is the latter.
    fi = -1
    for _a in ("### Character States:", "### Chapter end state", "### Character Progression:"):
        if text.find(_a) >= 0:
            fi = text.find(_a); break
    footer = text[fi:] if fi >= 0 else ""
    bi = footer.find(MARK)
    block = footer[bi:] if bi >= 0 else ""
    before = footer[:bi] if bi >= 0 else footer

    # ---- 1. the block must exist exactly once ----
    if footer.count(MARK) != 1:
        errors.append(f"ch{n}: expected exactly one '{MARK}' block in the footer, found {footer.count(MARK)}")
        continue

    sched = ES.SCHEDULE.get(n, {})
    for key, (label, rx) in KEYS.items():
        if key not in sched:
            continue
        exp_rank, exp_str = sched[key]
        line = None
        for l in block.split("\n"):
            if re.match(r"\s*-\s+\*\*" + re.escape(label) + r":\*\*", l):
                line = l
                break
        if line is None:
            errors.append(f"ch{n}: the ensemble block has no entry for {label}")
            continue

        # ---- 2. rank agreement ----
        got = rank_in(line)
        if exp_rank is None:
            if got is not None and not re.search(r"last known rank", line):
                errors.append(f"ch{n}: {label} shows rank {got} but the schedule says they are out/absent: {exp_str[:90]}")
        elif got != exp_rank:
            errors.append(f"ch{n}: {label} rank is {got}, schedule says {exp_rank} (CHARACTER_STATS.md §1/§3)")
        if got is not None:
            # A character who has left the story is only counted up to their last in-story
            # chapter, so a "last known rank" line repeating to ch61 is not read as a freeze.
            if exp_rank is None and key in LEFT_AT and n > LEFT_AT[key]:
                pass
            else:
                observed.setdefault(key, {})[n] = got

        # ---- 3. no stale line elsewhere in the footer ----
        for l in before.split("\n"):
            if re.match(r"\s*-\s+\*\*" + re.escape(label) + r":\*\*", l):
                stale = rank_in(l)
                errors.append(
                    f"ch{n}: stale ensemble line for {label} outside the authoritative block"
                    + (f" (rank {stale})" if stale is not None else "")
                    + f": {l.strip()[:110]}")

# ---- 4. freeze detection across the observed series ----
for key, by_ch in observed.items():
    label = KEYS[key][0]
    chs = sorted(by_ch)
    run_start = chs[0]
    for idx in range(1, len(chs) + 1):
        at_end = idx == len(chs)
        if (not at_end) and by_ch[chs[idx]] == by_ch[run_start]:
            continue
        prev = idx - 1
        span = chs[prev] - run_start + 1
        val = by_ch[run_start]
        registered = [p for p in getattr(ES, "REGISTERED_PLATEAUS", [])
                      if p[0] == key and p[1] == val and run_start >= p[2] and chs[prev] <= p[3]]
        if registered:
            notes.append(f"{label}: rank {val} held {span} chapters (ch{run_start}-ch{chs[prev]}) — "
                         f"REGISTERED PLATEAU: {registered[0][4]}")
        elif span > ES.HARD_FREEZE_CHAPTERS:
            errors.append(
                f"{label}: rank frozen at {val} for {span} chapters (ch{run_start}-ch{chs[prev]}). "
                f"Hard limit {ES.HARD_FREEZE_CHAPTERS}. Canon's longest legitimate plateau is "
                f"Tang Wulin at rank 11 from c45 to ~c98; if this hold is that long it needs an "
                f"explicit canon anchor in CHARACTER_STATS.md.")
        elif span > ES.MAX_STATIC_CHAPTERS:
            warnings.append(
                f"{label}: rank held at {val} for {span} chapters (ch{run_start}-ch{chs[prev]}) — "
                f"confirm a canon anchor covers the plateau.")
        if not at_end:
            run_start = chs[idx]

# ---- 5. the Shrek roster ----
# Canon c288 puts four in the Shrek working-student dorm: Wulin, Xie Xie, Gu Yue, Xu Xiaoyan
# (+ Lin Hao, AU). Only flag an AFFIRMATIVE claim that a non-goer is going, so that
# "nobody was going to mention" and "Zhang Yangzi is NOT going" do not trip it.
GOING = re.compile(r"(?<!not )(?<!not\s)(?<!isn't )\bgoing\b", re.I)
NEGATED = re.compile(r"(not|isn't|aren't|never|won't|nobody|no one)[^.\n]{0,25}\bgoing\b", re.I)
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    text = open(path, encoding="utf-8", errors="replace").read()
    for bad in ES.NOT_SHREK:
        for m in re.finditer(r"(?<![A-Za-z])" + re.escape(bad) + r"[^\n]{0,110}", text):
            seg = m.group(0)
            if not GOING.search(seg):
                continue
            if NEGATED.search(seg) or re.search(r"NOT going", seg):
                continue
            # must actually be about travelling, not "going to mention"
            if not re.search(r"going (to Shrek|with|too|as well|anyway)|\bgoing\b[^\n]{0,20}Shrek", seg, re.I):
                continue
            errors.append(
                f"ch{n}: {bad} described as going — canon c288 puts only Tang Wulin, Xie Xie, "
                f"Gu Yue and Xu Xiaoyan (+ Lin Hao, AU) in the Shrek group.\n      line: {seg.strip()[:150]}")

# ---- 6. hard canon numbers never contradicted ----
CANON_CONTRADICTIONS = [
    (r"Xu Xiaoyan(?:(?!Xie Xie|Tang Wulin|Gu Yue|Lin Hao|Wu Zhangkong)[^\n]){0,80}three (?:soul )?rings",
     "Xu Xiaoyan has TWO rings until rank 30 (canon: 'Xu Xiaoyan only had two soul rings, no doubt about it')."),
    (r"Mu Xi[^\n]{0,80}(one|two) (soul )?rings",
     "Mu Xi is a three-ringed Soul Elder, yellow/yellow/purple (canon)."),
    (r"\b(black|black-coloured|black colored)\b(?:(?!red|scarlet|crimson)[^\n]){0,40}(?:hundred[- ]thousand|100[,.]?000)",
     "Black = ten thousand years (canon: 'Black represented ten thousand years')."),
    (r"\b(red|scarlet|crimson)\b[^\n]{0,30}(soul )?ring[^\n]{0,40}ten[- ]thousand",
     "Ten-thousand-year rings are BLACK, not red (canon: 'Black represented ten thousand years')."),
    (r"Wang Jinxi[^\n]{0,90}spiritual power[^\n]{0,10}?\**\b(4[2-9]|[5-9]\d|\d{3,})\b",
     "Wang Jinxi's spiritual power is canon's lowest in class zero: 18 (canon c113)."),
    (r"(Zhang Yangzi|Xie Xie|Gu Yue|Tang Wulin|Xu Xiaoyan)[^\n]{0,60}spiritual power[^\n]{0,10}?\**\b(\d{4,})\b",
     "No class-zero student has four-digit spiritual power before the Spirit Abyss realm (5,000+, canon c134)."),
]
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    for i, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        for rx, why in CANON_CONTRADICTIONS:
            if re.search(rx, line, re.I):
                errors.append(f"ch{n}:{i}: canon contradiction — {why}\n      line: {line.strip()[:150]}")

# ---- 7. EFFECTIVE POWER — LIN HAO CANNOT BE BEATEN BY HIS AGE GROUP (v2.91) ----
# v2.90 encoded "no character may defeat someone a full realm above them" as a universal law.
# THAT WAS WRONG: canon is full of lower-realm winners (Wulin beats rank 27 at rank 15; Wu Zhangkong
# beats a six-ring Soul Emperor in two strokes). Punching up is the genre. So this check is NOT a
# universal realm rule -- it is specific to Lin Hao, whose effective combat power is far above his rank.
#
# LOCKED (user directive 2026-08-28): rank 36 Soul Elder, three purple rings, but EFFECTIVE COMBAT
# POWER = SOUL KING (51-60), ceiling SOUL KING PEAK (60) with everything spent -- the ceiling that
# "normal guys who don't have a black ring" reach. Biggest single reason: his SECOND SOUL SKILL,
# HAWK-SOUL UNION, a trump card only a 100%-integrated soul spirit can give.
# => "a lower realm person defeat him is nonsense."
# NOTE: Gu Yue CAN defeat an ordinary three-ring Soul Elder. She cannot defeat Lin Hao. The check
# therefore guards HIM, not the realm system.
# 🔴 READ FROM state.json, NOT HARDCODED (changed 2026-08-30, ch71 — §4.13). This was
# `LINHAO_EFFECTIVE_REALM = "Soul King"` / `FLOOR = 51`, and "Soul King" was separately hardcoded
# in state.py, build_status.py and build_continuation.py: four copies of one belief. The fourth
# ring moves it, so the check now reads the derived value like everything else.
import json as _json
_STATE_F = os.path.join(ROOT, "checks", "state.json")
_ST = _json.load(open(_STATE_F, encoding="utf-8")) if os.path.exists(_STATE_F) else {}
LINHAO_EFFECTIVE_REALM = _ST.get("effective_realm", "Soul King")
LINHAO_EFFECTIVE_FLOOR = (_ST.get("effective_rank_band") or [51, 60])[0]
LINHAO_EFFECTIVE_CEIL = (_ST.get("effective_rank_band") or [51, 60])[1]
LINHAO_EFFECTIVE_DELTA = _ST.get("effective_rank_delta") or [11, 20]

BRACKETS = [(1, 10, "Soul Scholar"), (11, 20, "Soul Master"), (21, 30, "Soul Grandmaster"),
            (31, 40, "Soul Elder"), (41, 50, "Soul Ancestor"), (51, 60, "Soul King"),
            (61, 70, "Soul Emperor"), (71, 80, "Soul Sage")]
ENSEMBLE_KEYS = ("wulin", "xiexie", "guyue", "xiaoyan", "yangzi", "jinxi", "weixf")

# Lin Hao's rank per chapter, from the footer's authoritative state line
LINHAO_RANK = {}
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    text = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"Lin Hao:\*\*\s*\*\*rank\s*(\d{1,3})", text)
    if not m:
        m = re.search(r"\brank\s*\**\s*(\d{1,3})\s*\**\s*\(Soul (?:Scholar|Master|Grandmaster|Elder|Ancestor|King)", text)
    if m:
        LINHAO_RANK[n] = int(m.group(1))

# verbs that mean WIN. "outlast / survive / evade / did not lose" are legal and better writing.
WINS = re.compile(r"\b(beats?|beat|beaten|defeats?|defeated|defeating|wins? against|won against|"
                  r"outclass\w*|crush\w*|overwhelms?|overwhelmed|took him down|put him down)\b", re.I)
SURVIVES = re.compile(r"\b(outlast\w*|lasted?|surviv\w*|evad\w*|held (him|her|off)|"
                      r"did not lose|doesn't lose|doesn't win|did not win|not a win|"
                      r"cannot defeat|can't defeat|could not defeat)\b", re.I)

for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    lh = LINHAO_RANK.get(n)
    if not lh:
        continue
    sched = ES.SCHEDULE.get(n, {})
    text = open(path, encoding="utf-8", errors="replace").read()
    for key in ENSEMBLE_KEYS:
        if key not in sched:
            continue
        erank = sched[key][0]
        if erank is None or erank >= LINHAO_EFFECTIVE_FLOOR:
            continue          # at or above Soul King -- outside this rule
        label = KEYS[key][0]
        for m in re.finditer(r"(?<![A-Za-z])" + re.escape(label) + r"[^\n.]{0,70}", text):
            seg = m.group(0)
            if not re.search(r"\b(him|Lin Hao)\b", seg, re.I):
                continue
            if not WINS.search(seg):
                continue
            if SURVIVES.search(seg):
                continue      # "outlasted him" / "cannot defeat him" -- the legal version
            errors.append(
                f"ch{n}: EFFECTIVE POWER LAW - {label} (rank {erank}) is written as defeating "
                f"Lin Hao (rank {lh}). His effective combat power is {LINHAO_EFFECTIVE_REALM} "
                f"({LINHAO_EFFECTIVE_FLOOR}-{LINHAO_EFFECTIVE_CEIL}, "
                f"+{LINHAO_EFFECTIVE_DELTA[0]}-{LINHAO_EFFECTIVE_DELTA[1]} ranks above his paper) -- "
                f"derived in state.py from his rank and ring count. A lower-realm character "
                f"defeating him is nonsense. They may outlast, survive or cost him; they may not "
                f"WIN.\n      line: {seg.strip()[:150]}")

# ---- 7b. REALM GAP IS A FORCE, NOT A PROHIBITION (warning only, for everyone else) ----
# Punching up is legal and canonical. What is NOT legal is a lower-realm win with no stated reason.
# We cannot read "reason" mechanically, so this warns rather than fails, and only across a FULL realm.
REASON_WORDS = re.compile(
    r"bloodline|divine strength|innate god|purple ring|thousand[- ]year|mutat|golden (dragon|scale)|"
    r"trump card|held back|secret|unreadable|cannot read|can't read|fusion|battle armor|"
    r"heavenly treasure|spirit soul|soul skill|teacher|intent|adaptation|talent", re.I)
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    text = open(path, encoding="utf-8", errors="replace").read()
    sched = ES.SCHEDULE.get(n, {})
    ranks = {KEYS[k][0]: sched[k][0] for k in ENSEMBLE_KEYS if k in sched and sched[k][0]}
    names = list(ranks)
    for a in names:
        for b in names:
            if a == b:
                continue
            ta = next((i for i, (lo, hi, t) in enumerate(BRACKETS) if lo <= ranks[a] <= hi), None)
            tb = next((i for i, (lo, hi, t) in enumerate(BRACKETS) if lo <= ranks[b] <= hi), None)
            if ta is None or tb is None or ta <= tb:
                continue          # a is not above b
            for m in re.finditer(r"(?<![A-Za-z])" + re.escape(b) + r"[^\n.]{0,60}?"
                                 r"\b(beats?|beat|defeats?|defeated)\b[^\n.]{0,40}?"
                                 + re.escape(a), text):
                seg = m.group(0)
                if REASON_WORDS.search(text[max(0, m.start()-400):m.end()+400]):
                    continue
                warnings.append(
                    f"ch{n}: {b} (rank {ranks[b]}, {BRACKETS[tb][2]}) defeats {a} "
                    f"(rank {ranks[a]}, {BRACKETS[ta][2]}) -- a full realm up. Punching up is "
                    f"legal and canonical, but the reason must be on the page.\n"
                    f"      line: {seg.strip()[:140]}")

# ---- 7c. PURPLE-RING SKILL EVOLUTION (v2.92) ----
# Canon: "if his spirit soul was upgraded, then the soul skills it provided would be upgraded too."
# In ch40 both of Lin Hao's rings re-formed purple (hawk 964 + 200/ring = 1,164) and a third was
# bestowed. So Gale Talon and Hawk-Soul Union BOTH upgraded to thousand-year tier at ch40.
# THE OMISSION: the rings changed colour and the skills kept being written exactly as before.
#   FAIL  -- a skill described at yellow/hundred-year tier from ch40 onward
#   WARN  -- the skill used at all from ch40 onward while the evolution scene is still unwritten
SKILL_EVOLUTION_CHAPTER = 40
SKILLS = ("Gale Talon", "Hawk-Soul Union")
YELLOW_TIER = re.compile(r"\b(hundred[- ]year|yellow[- ]tier|yellow (soul )?skill|"
                         r"(still|same|unchanged|no different)[^\n.]{0,30}(yellow|as before))\b", re.I)
EVOLUTION_STAGED = None   # set to the chapter number once the evolution scene is written

for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    text = open(path, encoding="utf-8", errors="replace").read()
    if re.search(r"(Gale Talon|Hawk-Soul Union)[^\n.]{0,200}(thousand[- ]year|purple)[^\n.]{0,120}"
                 r"(evolv|upgrad|re-?formed|changed|became|new)", text, re.I):
        if EVOLUTION_STAGED is None or n < EVOLUTION_STAGED:
            EVOLUTION_STAGED = n
    if n < SKILL_EVOLUTION_CHAPTER:
        continue
    for sk in SKILLS:
        for m in re.finditer(re.escape(sk) + r"[^\n.]{0,120}", text):
            seg = m.group(0)
            if YELLOW_TIER.search(seg):
                errors.append(
                    f"ch{n}: {sk} described at hundred-year/yellow tier, but both rings re-formed "
                    f"PURPLE in ch40 and canon says \"if his spirit soul was upgraded, then the soul "
                    f"skills it provided would be upgraded too\". From ch40 both skills are "
                    f"THOUSAND-YEAR tier.\n      line: {seg.strip()[:150]}")
# The evolution is detected by evidence in the prose, not by a hardcoded flag. F1 was closed
# in ch40 on 2026-08-28; before that this warning was the only thing keeping the debt visible,
# and after that it would have been a lie -- so it must actually look.
EVOLUTION_EVIDENCE = re.compile(
    r"(thousand[- ]year soul skill|skill[^\n.]{0,50}got \*{0,2}older|"
    r"permission[^\n.]{0,60}(hundred|thousand)|soul skills? (it )?provided would be upgraded)", re.I)
ev_ch = None
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    if n < SKILL_EVOLUTION_CHAPTER:
        continue
    body = open(path, encoding="utf-8", errors="replace").read()
    if EVOLUTION_EVIDENCE.search(body):
        ev_ch = n
        break
if ev_ch is None:
    warnings.append(
        f"PURPLE-RING SKILL EVOLUTION UNWRITTEN: both rings re-formed purple in ch{SKILL_EVOLUTION_CHAPTER}, "
        f"so Gale Talon and Hawk-Soul Union both upgraded to thousand-year tier (canon: upgraded spirit soul "
        f"=> upgraded soul skills). No chapter shows that evolution. Until it is written, neither skill may "
        f"be used as though ch{SKILL_EVOLUTION_CHAPTER} changed nothing.")
else:
    print(f"  ok   purple-ring skill evolution shown on-page in ch{ev_ch} "
          f"(canon: upgraded spirit soul => upgraded soul skills)")

# ---- 7d. LIN HAO MUST NOT BE KILLED OR IMPLIED DEAD (LOCKED D017) ----
# I wrote in the codex that a classification was "formalised long after he is dead" — I killed the
# protagonist to make a sequel connection feel poignant. The user caught it. A payoff that requires a
# death you were not told about is not a payoff, it is a theft.
# 🔴 CALIBRATED after six false positives. The first version matched ANY death within 120 characters
# of his name, so it fired on "the grave, solemn face of a man delivering a eulogy" (a joke about Wulin
# being pinched), "a dead man's record" (Long Bing's grave), "a dead thing the size of a house" (a soul
# beast), and "canon's Xie Xie is nearly killed". **Other people and things are allowed to die.**
# What is forbidden is a claim about HIS death, HIS grave, or the world continuing after HIM.
DEATH = re.compile(
    r"\bLin Hao\b[^\n.]{0,40}?\b(?:dies|died|death|is dead|was dead|killed)\b"
    r"|\b(?:death|killing|murder)\s+of\s+Lin Hao\b"
    r"|\bLin Hao\'s\s+(?:death|grave|tomb|funeral|memorial)\b"
    r"|\b(?:after|since|following)\s+Lin Hao\b[^\n.]{0,30}?\b(?:died|death|gone)\b"
    r"|\b(?:outlived|outlive)\s+Lin Hao\b"
    r"|\bLin Hao\b[^\n.]{0,60}?\b(?:posthumous|after he is dead|long after he is gone)\b",
    re.I)
DEATH_OK = re.compile(r"not dead|is not dead|NEVER|do not ever|must not|🔓|OPEN|undecided|"
                      r"did not die|didn't die|would have died|nearly died|almost died|"
                      r"nearly killed|almost killed|not nearly|if he died|were he to die|"
                      r"does not die|hurt but not", re.I)
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    for i, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        if DEATH.search(line) and not DEATH_OK.search(line):
            errors.append(
                f"ch{n}:{i}: implies Lin Hao's death. LOCKED (D017): he lives through all of Soul "
                f"Land 3 and beyond; his fate is OPEN. Nothing may write or imply it.\n"
                f"      line: {line.strip()[:150]}")
# the tracking documents too
for doc in ("THE_CODEX.md", "RELATIONSHIPS.md", "CHARACTER_STATS.md", "LIN_HAO_PANELS.md",
            "LIN_HAO_STATUS.md", "POWER_MODEL.md"):
    fp = os.path.join(ROOT, doc)
    if not os.path.exists(fp):
        continue
    for i, line in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
        if DEATH.search(line) and not DEATH_OK.search(line):
            errors.append(
                f"{doc}:{i}: implies Lin Hao's death (LOCKED, D017).\n      line: {line.strip()[:150]}")

# ---- 8. the cancelled "Divine Stormbringer" plan must not resurface ----
for path in sorted(glob.glob(os.path.join(CH, "chapter_*.md"))):
    n = int(re.search(r"chapter_(\d+)", os.path.basename(path)).group(1))
    for i, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
        if re.search(r"Divine\s+Stormbringer|Stormbringer\s+Divine", line, re.I):
            errors.append(
                f"ch{n}:{i}: the \"Divine Stormbringer\" evolution plan was CANCELLED (v2.90, user "
                f"directive). The sword evolves into a TOP-LEVEL martial soul at the fourth ring — "
                f"never divine tier.\n      line: {line.strip()[:150]}")

print(f"verify_ensemble: scanned {latest} chapters, {len(observed)} tracked characters")
for w in warnings:
    print("  WARN " + w)
for nn in notes:
    print("  NOTE " + nn)
for e in errors:
    print("  FAIL " + e)
if errors:
    print(f"\nverify_ensemble: {len(errors)} failure(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"verify_ensemble: PASS ({len(warnings)} warning(s))")
sys.exit(0)
