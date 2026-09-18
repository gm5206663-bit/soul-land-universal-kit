"""Ensemble progression schedule — the single source of truth for every canon character's numbers.

Read by checks/verify_ensemble.py. Every value must trace to a canon line quoted in
CHARACTER_STATS.md §1, or be labelled AU.

Format: chapter -> {character_key: (soul_power_rank_or_None, footer_string)}
  rank None = the character has left class zero / is not yet introduced.

WHY THIS EXISTS
  For 49 chapters the ensemble was frozen: Tang Wulin sat at rank 15 from ch13 to ch61 while
  canon moved him 15 -> 16 -> 17; Xie Xie sat at 21 from ch17 to ch61; Wei Xiaofeng at 22 from
  ch21 to ch61; Gu Yue was never given a rank at all. This module makes every number explicit
  and checkable, so a dead progression line cannot be invisible again.

CANON ANCHORS USED
  Wulin   11 (c45) -> 12 (c98) -> peak 15 (c133) -> 16 (c183) -> near 17 (c192)
  Xie Xie 18 (c46) -> 19 (c72) -> 20 + 2nd ring (c101) -> 22 (c134) -> highest in class zero (c184)
  Gu Yue  17 (c72) -> peak 19 (c133) -> 2 rings by the tournament (c224)
  Yangzi  22 (c134), spiritual power 41 (c113)
  Jinxi   23 (c134), spiritual power 18 (c113, lowest in class zero)
  Wei XF  22 (c101)
  Xiaoyan 17 at age 10 on arrival, spiritual power 61, two yellow rings (c183)
"""

SCHEDULE = {}


def _set(ch_from, ch_to, **kw):
    for c in range(ch_from, ch_to + 1):
        SCHEDULE.setdefault(c, {}).update(kw)


# ---------------------------------------------------------------------------
# Footer-string builders (canon citations inline)
# ---------------------------------------------------------------------------
def _wu(r, note="", ring="one white ten-year ring"):
    return f"**Tang Wulin:** rank **{r}**{note} · {ring}"


def _xx(r, rings="one yellow hundred-year ring", note=""):
    return f"**Xie Xie:** rank **{r}**{note} · {rings}"


def _gy(r, rings="one ring", note=""):
    return f"**Gu Yue:** rank **{r}**{note} · {rings} · spiritual power **153** at nine (canon c114)"


def _zy(r, sp=41, note=""):
    return (f"**Zhang Yangzi:** rank **{r}** · spiritual power **{sp}** (canon c113){note}")


def _wj(r, note=""):
    return (f"**Wang Jinxi:** rank **{r}** (canon c134) · spiritual power **18**, lowest in "
            f"class zero (canon c113){note}")


def _wx(r, note=""):
    return f"**Wei Xiaofeng:** rank **{r}** (canon c101){note}"


def _xy(r, note=""):
    return (f"**Xu Xiaoyan:** rank **{r}** · two yellow rings · spiritual power **61** "
            f"(canon c183){note}")


def _none(label, why):
    return f"**{label}:** {why}"


NOT_YET = "not yet introduced"
PURPLE = ("**one purple ring** (canon c184: *\"Despite Tang Wulin only having one ring right now, "
          "it was a purple ring!\"*)")
TWO_RINGS_GY = "**TWO rings** (canon c224)"
# 🔴 BUTTERFLY LAW APPLIED AT THE SOURCE (fixed 2026-08-29).
# Canon c184 says "Xie Xie's soul power is the highest after all" about a class that does NOT
# contain Lin Hao. Copying it verbatim into a footer for a class that DOES contain him is
# transcription, not adaptation — the exact defect the user caught in ch52. The schedule is the
# single source of truth for every footer, so scoping it here fixes all 62 chapters at once
# instead of one at a time. Canon's claim stays (cited), Lin Hao is scoped out (butterfly).
HIGHEST_XX = (" · **highest soul power in class zero except Lin Hao** (canon c184: *\"Xie Xie's "
              "soul power is the highest after all\"* — scoped by the BUTTERFLY LAW)")


# ---------------------------------------------------------------------------
# Departures — STORY FACTS from ch43 ("What Wang Jinxi Understood", adapted from canon
# ch 151-153 "A Problem Appears" / "Wang Jinxi's Pain" / "Leaving"):
#   * Wang Jinxi LEAVES for good (canon ch 153). He transfers to another academy.
#   * Zhang Yangzi STAYS at Eastsea. He embraces Wang Jinxi on the steps. He leaves class zero
#     but not the academy. This is the documented AU divergence from canon, where both go
#     ("Zhang Yangzi and Wang Jinxi are leaving too").
#   * Wei Xiaofeng left class zero before them (canon: "Wei Xiaofeng was the first to leave").
# ch52 confirms the resulting roster: "Class zero had five students and one teacher" —
# Wulin, Xie Xie, Gu Yue, Zhang Yangzi, Lin Hao — then Xu Xiaoyan arrives as the sixth.
# ---------------------------------------------------------------------------
def _zy_out(r):
    return (f"**Zhang Yangzi:** rank **{r}** · spiritual power ~27 after Little Black · "
            "**still at Eastsea Academy**; out of class zero since ch43 · **NOT going to Shrek**")


def _wj_out():
    return ("**Wang Jinxi:** **LEFT in ch43** (canon ch 153 \"Leaving\") · last known rank 25 · "
            "spiritual power 18 (canon c113) · transferred to another academy · "
            "**NOT going to Shrek**")


def _wx_out(r):
    return (f"**Wei Xiaofeng:** rank **{r}** · **left class zero first** "
            "(canon: *\"Wei Xiaofeng was the first to leave\"*) · still at Eastsea Academy · "
            "**NOT going to Shrek**")


# ===========================================================================
# ch 1-3 — before class five. Canon c45: Wulin's intake rank is 11.
# ===========================================================================
_set(1, 3,
     wulin=(11, _wu(11, " (canon c45 intake)", "no rings yet — age 6-9")),
     xiexie=(None, _none("Xie Xie", NOT_YET)),
     guyue=(None, _none("Gu Yue", NOT_YET)),
     yangzi=(None, _none("Zhang Yangzi", NOT_YET)),
     jinxi=(None, _none("Wang Jinxi", NOT_YET)),
     weixf=(None, _none("Wei Xiaofeng", NOT_YET)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 4-9 — class five intake (canon c45/c46).
# 🔴 WULIN IS 13, NOT CANON'S 11 — DOCUMENTED AU DIVERGENCE (fixed 2026-08-29).
# Canon c45 has him at rank 11 at intake. Our ch9 PROSE states on-page: "Wulin, who had been
# rank thirteen since before enrollment." The prose is the story. The schedule exists to stop
# a progression line silently freezing, not to overrule a sentence that is already written and
# internally consistent. It said 11 while 61 footers said 13 and nothing compared them, so the
# disagreement was invisible for the life of the project. Prose wins, the delta is recorded
# here, and Layer 11 now fails if they ever disagree again.
# ===========================================================================
_set(4, 8,
     wulin=(13, _wu(13, " (AU — canon c45 has 11 at intake; ch9 prose: *\"rank thirteen since "
                        "before enrollment\"*)", "one white ten-year ring (Goldlight)")),
     xiexie=(18, _xx(18, note=" (canon c46)")),
     guyue=(None, _none("Gu Yue", "enrolled but sealed — gives no information about herself "
                                 "(canon mystery discipline; AU rank deliberately not stated)")),
     yangzi=(21, _zy(21, note=" · Shadow Phantasm Eagle")),
     jinxi=(21, _wj(21, " · Bone Dragon King")),
     weixf=(21, _wx(21, " · Green Shadow Snake")),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ch 9 — Wulin breaks to 14 on the ninth night of special training (on-page in ch9).
_set(9, 9,
     wulin=(14, _wu(14, " (AU — quiet breakthrough on the ninth night of special training; "
                        "canon c98 has 12)", "one white ten-year ring (Goldlight)")),
     xiexie=(18, _xx(18, note=" (canon c46)")),
     guyue=(None, _none("Gu Yue", "enrolled but sealed — gives no information about herself "
                                 "(canon mystery discipline; AU rank deliberately not stated)")),
     yangzi=(21, _zy(21, note=" · Shadow Phantasm Eagle")),
     jinxi=(21, _wj(21, " · Bone Dragon King")),
     weixf=(21, _wx(21, " · Green Shadow Snake")),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 10-12 — canon c98 has Wulin at 12 here; the AU keeps him a touch ahead.
# ===========================================================================
_set(10, 12,
     wulin=(14, _wu(14, " (AU — canon c98 has 12 at this point; documented delta)")),
     xiexie=(19, _xx(19, note=" (canon c72)")),
     guyue=(17, _gy(17, note=" (canon c72)")),
     yangzi=(22, _zy(22)),
     jinxi=(22, _wj(22)),
     weixf=(22, _wx(22)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 13-16 — Wulin 15 = canon c133 "peak of rank 15".
# ===========================================================================
_set(13, 16,
     wulin=(15, _wu(15, " (canon c133 *peak of rank 15*)")),
     xiexie=(19, _xx(19, note=" (canon c72)")),
     guyue=(17, _gy(17, note=" (canon c72)")),
     yangzi=(22, _zy(22)),
     jinxi=(22, _wj(22)),
     weixf=(22, _wx(22)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 17-20 — Xie Xie breaks to 20 and takes his SECOND ring (canon c101).
# ===========================================================================
_set(17, 20,
     wulin=(15, _wu(15, " (canon c133)")),
     xiexie=(20, _xx(20, rings="**TWO rings**", note=" (canon c101)")),
     guyue=(18, _gy(18, note=" (AU, between canon 17 and peak 19)")),
     yangzi=(23, _zy(23, note=" · climbing out of Spirit Origin (canon c113 predicted within a year)")),
     jinxi=(22, _wj(22)),
     weixf=(23, _wx(23)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 21-29 — Gu Yue peaks at 19 (canon c133). Wang Jinxi advances two ranks (canon c134).
# ===========================================================================
_set(21, 29,
     wulin=(15, _wu(15, " (canon c133)")),
     xiexie=(20, _xx(20, rings="two rings", note=" (canon c101)")),
     guyue=(19, _gy(19, note=", peak (canon c133)")),
     yangzi=(23, _zy(23)),
     jinxi=(23, _wj(23, " — advanced two ranks (canon c134)")),
     weixf=(23, _wx(23)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 30-35 — the run-up to the final exam. Zhang Yangzi breaks out of Spirit Origin, which is
#            exactly what Wu Zhangkong predicted in canon c113 ("within a year").
# ===========================================================================
_set(30, 35,
     wulin=(15, _wu(15, " (canon c133 — held until the deep meditation)")),
     xiexie=(21, _xx(21, rings="two rings",
                     note=" (AU, between canon 20 at c101 and 22 at c134)")),
     guyue=(19, _gy(19, note=", peak (canon c133)")),
     yangzi=(24, _zy(24, note=" · broke out of Spirit Origin within the year Wu Zhangkong "
                              "predicted (canon c113)")),
     jinxi=(24, _wj(24)),
     weixf=(24, _wx(24)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 36-38 — Wulin reaches a stable rank 16 (canon c183, after the deep meditation).
# ===========================================================================
_set(36, 38,
     wulin=(16, _wu(16, " (canon c183: *\"increased to a stable rank 16\"* after the deep "
                        "meditation)")),
     xiexie=(21, _xx(21, rings="two rings")),
     guyue=(19, _gy(19, note=", peak (canon c133)")),
     yangzi=(24, _zy(24)),
     jinxi=(24, _wj(24)),
     weixf=(24, _wx(24)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 39-41 — Little Black dies; Zhang Yangzi loses a third of his spiritual power (AU event).
# ===========================================================================
_set(39, 41,
     wulin=(16, _wu(16, " (canon c183)")),
     xiexie=(21, _xx(21, rings="two rings")),
     guyue=(19, _gy(19, note=", peak (canon c133)")),
     yangzi=(24, "**Zhang Yangzi:** rank **24** · spiritual power **41 → ~27** — Little Black "
                 "dead (AU cost of the forest)"),
     jinxi=(24, _wj(24)),
     weixf=(24, _wx(24)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 42 — Wulin takes the PURPLE ring (canon c184). Gu Yue takes her SECOND ring (canon c224).
# ===========================================================================
_set(42, 42,
     wulin=(16, _wu(16, " (canon c183)", PURPLE)),
     xiexie=(22, _xx(22, rings="two rings", note=" (canon c134)")),
     guyue=(20, _gy(20, rings=TWO_RINGS_GY, note=" (canon c133: one step past peak 19)")),
     yangzi=(24, "**Zhang Yangzi:** rank **24** · spiritual power ~27 (Little Black dead)"),
     jinxi=(25, _wj(25)),
     weixf=(25, _wx(25)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 43-44 — 🔴 Wang Jinxi LEAVES (canon ch 153). Zhang Yangzi stays at Eastsea, out of class zero.
# ===========================================================================
_set(43, 44,
     wulin=(16, _wu(16, " (canon c183)", "one purple ring")),
     xiexie=(22, _xx(22, rings="two rings", note=" (canon c134)")),
     guyue=(20, _gy(20, rings=TWO_RINGS_GY)),
     yangzi=(25, "**Zhang Yangzi:** rank **25** · spiritual power ~27 · **leaves class zero this "
                 "chapter** — he embraces Wang Jinxi on the steps and stays at Eastsea (AU: canon "
                 "has him transfer out too)"),
     jinxi=(None, _wj_out()),
     weixf=(25, _wx_out(25)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 45-51 — class zero is five: Wulin, Xie Xie, Gu Yue, Zhang Yangzi, Lin Hao (ch52 confirms).
#            Wulin reaches 17 (canon c192: "one step away from reaching rank 17").
# ===========================================================================
_set(45, 47,
     wulin=(16, _wu(16, " (canon c183)", "one purple ring")),
     xiexie=(22, _xx(22, rings="two rings", note=" (canon c134)")),
     guyue=(20, _gy(20, rings=TWO_RINGS_GY)),
     yangzi=(25, _zy_out(25)),
     jinxi=(None, _wj_out()),
     weixf=(25, _wx_out(25)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))
_set(48, 51,
     wulin=(17, _wu(17, " (canon c192: *\"one step away from reaching rank 17\"*)",
                    "one purple ring")),
     xiexie=(22, _xx(22, rings="two rings", note=" (canon c134)")),
     guyue=(20, _gy(20, rings=TWO_RINGS_GY)),
     yangzi=(26, _zy_out(26)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(None, _none("Xu Xiaoyan", NOT_YET)))

# ===========================================================================
# ch 52-56 — 🔴 Xu Xiaoyan arrives. Canon c183: age 10, rank 17, spiritual power 61, two yellow
#            rings. Xie Xie now has the highest soul power in class zero (canon c184).
# ===========================================================================
_set(52, 56,
     wulin=(17, _wu(17, " (canon c192)", "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings", note=HIGHEST_XX)),
     # rank 21, not 20: the story has called her a Soul Grandmaster since ch41, and under the
     # bracket law 21-30 is Soul Grandmaster while 20 is still Soul Master. Canon c133 has her at
     # "the peak of rank 19 and... only a step away from reaching rank 20"; this is two steps on.
     guyue=(21, _gy(21, rings=TWO_RINGS_GY, note=" — **Soul Grandmaster**")),
     yangzi=(26, _zy_out(26)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(17, _xy(17, ", age 10 (canon c183)")))

# ===========================================================================
# ch 57-61 — tournament / Shrek invitation. Everyone is 10 (canon c221).
#            Canon c288: four go to Shrek — Wulin, Xie Xie, Gu Yue, Xu Xiaoyan (+ Lin Hao, AU).
# ===========================================================================
_set(57, 59,
     wulin=(17, _wu(17, "", "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings",
                     note=" · highest soul power in class zero except Lin Hao (canon c184, "
                          "scoped by the BUTTERFLY LAW)")),
     guyue=(21, _gy(21, rings=TWO_RINGS_GY + " — **Soul Grandmaster** · spiritual power **153+**")),
     yangzi=(27, _zy_out(27)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(18, _xy(18, "+")))
_set(60, 61,
     wulin=(18, _wu(18, " · **going to Shrek** (canon c288)", "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings", note=" · **going to Shrek** (canon c288)")),
     guyue=(21, _gy(21, rings=TWO_RINGS_GY + " — **Soul Grandmaster** · **going to Shrek** (canon c288)")),
     yangzi=(27, _zy_out(27)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(19, _xy(19, " · **going to Shrek** (canon c288)")))

# ===========================================================================
# ch 62 — 🔴 SKY ICE. Canon ch 227/228: Wu Zhangkong reveals his two-word battle armor in front
#            of the whole Alliance and breaks through to SOUL SAGE midair.
#            AU DIVERGENCE (documented): in canon the provocation is the Zhou sisters nearly
#            killing Tang Wulin and Gu Yue (c223-226). Here nobody is hurt — a Sealand official
#            comes for LIN HAO'S FILE, because a three-ring ten-year-old carrying a seventh
#            System on a stamped form is an asset. THE SKY ICE HAPPENS BECAUSE LIN HAO EXISTS.
#            Canon's numbers are all kept verbatim: four levels, five/six/seven/nine rings,
#            "twenty soul ranks stronger", two words = an eight-ring man.
# ===========================================================================
# ch66 = ARRIVAL at Shrek (canon c288: "This is the dormitory for working students"). "Going to
# Shrek" was already a stale fact for four chapters before this was caught; corrected here.
_set(62, 65,
     wulin=(18, _wu(18, " · **going to Shrek** (canon c288)", "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings", note=" · **going to Shrek** (canon c288)")),
     guyue=(21, _gy(21, rings=TWO_RINGS_GY + " — **Soul Grandmaster** · **going to Shrek** (canon c288)")),
     yangzi=(27, _zy_out(27)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(19, _xy(19, " · **going to Shrek** (canon c288)")))

_set(66, 69,
     wulin=(18, _wu(18, " · **at Shrek, working student** (canon c288)", "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings", note=" · **at Shrek, working student** (canon c288)")),
     guyue=(21, _gy(21, rings=TWO_RINGS_GY + " — **Soul Grandmaster** · **at Shrek, working student** (canon c288)")),
     yangzi=(27, _zy_out(27)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(19, _xy(19, " · **at Shrek, working student** (canon c288)")))

# ---------------------------------------------------------------------------
# ch70 — THE ABSORPTION MONTH, carried by the ensemble. They have ARRIVED at Shrek (ch66+), so
# "going to Shrek" is now a stale fact and is replaced by their standing there. Canon c302/c295/
# c305 supply the working-student economy, the attendance rule and the seven representatives.
# Lin Hao is absent for the whole chapter (day 29 of the one-month absorption), and the AU facts
# created by his absence are marked AU inline.
# ---------------------------------------------------------------------------
_set(70, 71,
     wulin=(18, _wu(18, " · **blacksmith representative at Shrek, unchallenged** (canon c305)",
                    "one purple ring")),
     xiexie=(23, _xx(23, rings="two rings",
                     note=" · **holds the second profession council seat for blacksmithing in "
                          "trust for Lin Hao** (AU, ch70) · **eleven ingots under his bed** (AU, ch71)")),
     guyue=(21, _gy(21, rings=TWO_RINGS_GY + " — **Soul Grandmaster** · **at Shrek** (canon c288)")),
     yangzi=(27, _zy_out(27)),
     jinxi=(None, _wj_out()),
     weixf=(26, _wx_out(26)),
     xiaoyan=(19, _xy(19, " · **at Shrek** (canon c288)")))

# ---------------------------------------------------------------------------
SHREK_GOERS = {"Tang Wulin", "Xie Xie", "Gu Yue", "Xu Xiaoyan", "Lin Hao"}
NOT_SHREK = {"Zhang Yangzi", "Wang Jinxi", "Wei Xiaofeng", "Zhou Zhangxi", "Yun Xiao"}

# Canon's longest legitimate plateau is Tang Wulin at rank 11 from c45 to ~c98 (~53 chapters),
# so a plateau is not automatically a bug. The ch13-ch61 rank-15 freeze was 49 chapters AND
# contradicted canon (c183/c192 move him to 16 then 17). These thresholds are the tripwire.
MAX_STATIC_CHAPTERS = 15    # longer than this -> WARN, confirm a canon anchor covers it
HARD_FREEZE_CHAPTERS = 25   # longer than this -> FAIL
