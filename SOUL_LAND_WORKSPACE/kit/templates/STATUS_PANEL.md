# STATUS PANEL — the single status source

**This is the only file that states current state.** Every other file derives from it.
If another file disagrees with this one, that file is wrong — fix it here, at the source.

---

## LIVE EDGE

**Chapter N — "<title>"**

---

## TIMELINE POSITION

Date drift is the most expensive class of bug in a long serial: one bad number propagates
into every later chapter and is invisible until a reader finds it. **These four fields are
the single source of truth for it.** Derive every in-chapter number from them; never state
an independent absolute date anywhere else in the project.

| Field | Value |
|---|---|
| Anchor (year 0 = absolute date) | |
| Span covered so far | year __ – __ |
| Current absolute date | |
| Next chapter must start at | year __ |

**The last row is a gate.** If the next chapter's panel does not start where this one ends,
gate 5 fails. Set it here before drafting, not after.

**Canon margin:** if your serial runs toward a canon date, record the remaining slack here.
A negative margin is a hard fail — compress the span; never move the anchor.

| Canon event | Canon date | Story reaches it at | Margin |
|---|---|---|---|
| | | | |

---

## PROTAGONIST

| Field | Value |
|---|---|
| Public name | |
| True name | <if different; mark who knows it> |
| Age | |
| Rank | |
| Soul power | |
| Rings held | <colour — source beast — chapter acquired> |
| Position | |
| Condition | <injuries, debts, exhaustion — anything that persists> |

---

## KNOWN BY WHOM

| Who | Knows | Does NOT know |
|---|---|---|
| | | |

---

## FORBIDDEN NOW

What has **not** happened yet, and where it is reserved for. This field is what stops a
chapter from spending a later chapter's payoff because the scene wanted it.

```
- <power / ring / reveal / event>   — reserved for chapter N
- <power / ring / reveal / event>   — reserved for chapter N
```

---

## OPEN PRESSURES

Things that age whether or not the protagonist attends to them.

```
- <pressure>   — raised chapter N, unresolved
```

---

## LAST UPDATED

After chapter N. <date>
