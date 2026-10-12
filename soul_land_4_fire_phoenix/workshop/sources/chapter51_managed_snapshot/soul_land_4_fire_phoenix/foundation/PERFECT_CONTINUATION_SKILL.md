# Perfect Continuation Skill — Live Project Protocol

Updated: 2026-09-18  
Live edge: **after Chapter51, `The Cost of Quiet`**  
Machine manifest: `foundation/CURRENT_STATE_MANIFEST.json`  
Checker: `tools/perfect_continuation_skill_check.py`

This file is the standing continuation skill for the Soul Land 4 Fire Phoenix fic. It exists to stop drift, fake payoff, accidental nerfing, stale support state, and future-currentization.

---

## 1. Current baseline after Chapter51

- Latest prose: `chapters/Chapter_51.md` — **The Cost of Quiet**.
- Latest coverage: `canon_coverage/Canon_Coverage_Chapter_51.md`.
- Latest validation: `audits/CHAPTER_51_VALIDATION_2026-09-18.md`.
- Latest support sync target: `audits/CHAPTER_51_SUPPORT_SYNC_2026-09-18.md`.
- Canon consumed through verified Chapter176 `Be harder on yourself`.
- Next source boundary: Chapter177 `1,000-year Purple Zoysia`.
- Next fic chapter: Chapter52.

Current scene:

- Dorm333 is inside simulated Star Dou Forest in the seven-day Shrek Heaven Luo qualifier round.
- Team transfer is random; teams are separately scored; final-kill points matter; team-killing transfers half the victim team's accumulated points.
- Dorm333 has finished its first day, reached about twenty kilometers inward, avoided one beast horde by tree-climbing, met no other teams, recovered overnight, and begins the second morning with a faster risk-taking advance.
- Liu Feng leads/opens path; Qian Lei stays in the middle and ready to summon at any time; Lan Xuanyu covers/commands.

---

## 2. Required workflow for every next chapter

1. Read `foundation/STATUS_PANEL.md`, `foundation/CURRENT_STATE_MANIFEST.json`, this skill file, and relevant locks before drafting.
2. Fetch/read all chunks of the next verified source chapter.
3. Write canon coverage **before** prose:
   - For Chapter52, create `canon_coverage/Canon_Coverage_Chapter_52.md` from verified Chapter177.
4. Draft prose using repaired pacing:
   - compress routine canon;
   - expand character/system/butterfly/tactical/relationship consequences only when meaningful;
   - never stretch one source chapter just because it exists.
5. Validate the story body separately from the footer.
6. Write validation audit.
7. Update support files and status mirrors.
8. Run:
   - `python3 tools/perfect_continuation_skill_check.py --phase post --write-report audits/PERFECT_CONTINUATION_SKILL_CHECK_REPORT_YYYY-MM-DD.md`
9. Present only after the checker passes or after clearly explaining any blocker.

---

## 3. Repaired pacing rule

The user rejected the old post-Chapter48 path because it was too canon-copy/paste and too slow, then rejected the overcorrection because it invented unnatural Dorm336 reward handling.

Therefore:

- Do **not** default to one canon chapter per fic chapter.
- Do **not** copy canon beat-for-beat when the events are routine movement/travel/explanation.
- Do compress consecutive routine beats into one fic chapter when that gives better pacing.
- Do expand meaningful butterflies: Yan/Dorm336 pressure, Lan/Yan relationship weight, team tactics, Shrek observation logic, power-system implications, and emotional consequences.
- Do not invent formal Shrek items, ceremonies, or reward mechanisms unless verified source or explicit user approval provides them.
- Dorm336 second place must remain real through natural consequences: ranking, teacher attention, school support/debriefs, student perception, Shrek records, pressure, and future tests.
- Keep `no fake reward package` as the active rule.

---

## 4. Anti-nerf power-system rule

Never evaluate power by formal Soul Power rank alone.

Always reason through:

- formal rank and ring count;
- martial soul grade and bloodline/species hierarchy;
- attribute quality, especially Ultimate Fire;
- soul-spirit age/load/compatibility/absorption;
- Spiritual Power realm/control;
- body/frame/wings/metamorphosis;
- adaptation talent;
- terrain, rules, team, tactics, restrictions, cost, and observation context.

Yan Shuo current effective baseline must not be flattened:

- public Yan Shuo/he, private Yan Shuo'er unrevealed;
- Rank39 / SP962 / Spirit Sea;
- true awakened Fire Phoenix;
- Ultimate Fire;
- three purple soul spirits/rings: Dawnflame Phoenix Kite 3,100, Dawn-Iron Phoenix Roc 3,950, Purple Flame Eidolon Bird 6,400;
- cocoon-rebuilt body/frame/wings and adaptation talent;
- low Soul King-class effective threat floor in serious no-full-fusion release against ordinary/no-special-counter opponents.

This is not formal Rank50 and not automatic victory over every Soul King. It is a foundation-weighted threat floor.

---

## 5. Current Dorm333 locks

Lan Xuanyu:

- Rank20 / SP505 / Spirit Sea.
- Elementary Spirit Ascension Platform access card/opportunity is delivered and unspent.
- No Platform growth has occurred.
- Public command role is real; do not turn command authority into raw-power superiority over Yan.

Qian Lei:

- +500-year all-current-Soul-Rings reward has been processed through the Spirit Pagoda.
- Chapter175 source-confirms darker yellow rings and the 500-year realm.
- Do not invent exact post-reward ages or a breakthrough beyond source.
- Chapter51 adds a one-year target: five hundred Spiritual Power and Rank30 Soul Power.
- Spiritual Power overdraft is painful and risky for a summoner; repeated Gate training is useful but costly.

Liu Feng:

- Rank29 after fusing Silver Moon Wolf Right Arm Bone.
- Silver Edge exists as a Soul Bone skill/trump-card/familiarization path.
- Do not show extended Silver Edge mastery or unsupported combat feats before source/continuity earns them.
- Chapter51 deepens Liu's motivation: stronger people gain resources that let them become stronger again.

---

## 6. Lan/Yan relationship lock

Lan × Yan is not ordinary friendship and not an empty someday slow-burn.

Current accepted foundation:

- first friend / childhood friend;
- best friends;
- rivals;
- growth partners;
- among each other's most important special people;
- age-appropriate care before confession;
- long familiarity that lets them read weight in public-safe silences.

Secrets are adult-imposed/circumstance-imposed safety firewalls, not proof of distrust. Trust is shown by saying what can be said, not demanding unsafe answers, noticing what is hidden, and waiting for promised “after.”

Do not force a reveal to prove trust. Do not let Dong Qianqiu/Bai Xiuxiu canon romance erase the already-special Lan/Yan foundation.

---

## 7. Future/current bans

Not current unless verified later:

- SP526;
- early/current Platform growth;
- Yan fourth ring;
- Yan Emerald Demon Bird route;
- Yan external soul bone;
- Rainbow Dragon martial soul/rings/skills;
- Dragon Queen necklace possession before later Shrek auction;
- Phoenix God authority;
- Phoenix Domain;
- Nirvana / true resurrection skill;
- Martial Soul True Body;
- completed battle armor;
- public Yan Shuo'er reveal;
- Glacial Halcyon King, Black Phoenix, Three-Eyed Colorful Feather Clan, Silver/Golden Blue Demon Bird, Ultimate Spiritual attribute, later-colour Phoenix states.

---

## 8. Chapter52 guard

Chapter52 must begin from the Chapter51 endpoint:

- second morning in simulated Star Dou Forest;
- about twenty kilometers inward;
- Dorm333 has judged the first day too quiet/too careful;
- Liu Feng leads and opens the path;
- Qian Lei stays ready to summon at any time;
- Lan frames the test as courage, meticulousness, strength, adaptability, and luck.

Required next action before prose:

- Fetch/read all chunks of verified NovelFull Chapter177 `1,000-year Purple Zoysia`.
- Write `canon_coverage/Canon_Coverage_Chapter_52.md` before `chapters/Chapter_52.md`.
- Do not use Chapter178 material until Chapter52 is complete, validated, support-synced, checked, and presented.

---

## 9. Final self-check before presenting

Before presenting a chapter, confirm:

- latest prose/coverage/audits exist;
- coverage says PASS;
- story body has no next-source spillover;
- Yan is not nerfed by formal rank-only reasoning;
- Dorm336 is not erased and is not given invented rewards;
- Lan/Yan bond is special without forced reveal;
- Qian/Liu/Lan reward states are current and not stale;
- status mirrors exactly match `foundation/STATUS_PANEL.md`;
- checker exits PASS.
