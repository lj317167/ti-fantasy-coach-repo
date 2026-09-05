# Empirical Mechanics — verified by spending tokens (TI 2026)

Tag format: `[empirical n=X]` = observed X times. `[client-confirmed]` = tested directly in UI without a token.
Everything here is *likely to hold* next year but must be re-verified on the first cheap press.
Update the counts as new observations arrive.

## Display semantics — how to read the banner screen

- **Multiplier = 100% + quality bonus + trait line.** `[client-confirmed]`
- **The trait line shows the NET effect received by that slot**, not the trait's own description:
  own conditional bonus (Unique/Friendly/Fractal when active, Vampiric +50) **plus** neighbor effects
  (Benevolent +20 from each adjacent, Vampiric −10 from each adjacent). `[empirical n=30+]`
  - Benevolent shows 0% on itself (it gives, doesn't receive) unless a neighbor feeds it.
  - A dead trait shows only neighbor effects (e.g. "分形 −10%" = dead Fractal next to a Vampiric).
  - Example that pinned this down: Support Stuns "友好 +40%" = dead Friendly between two Benevolents.
- **Adjacency is vertical list order** (slot 1 adjacent to 2; slot 3 adjacent to 2 and 4; ends have one
  neighbor). `[empirical n=30+]`
- Button position words map to this same order: "第一枚红色" = the top-most red emblem, "最后一枚" = bottom-most
  of that color. `[empirical n=6]`

## Three independent tracks

Stat, quality, trait are separate attributes of a slot. Rerolling one never changes the other two.
**Quality and trait are slot assets; stat is interchangeable.** `[empirical n=20+]`
→ Design rule: put the highest-base stat on the highest-quality slot; reroll stats *into* good slots, never
"upgrade" a slot to fit a weak stat.

## Button wording → scope

| Wording | Scope | Notes |
|---|---|---|
| "重新生成红色徽标的统计数据" (no 一枚) | ALL emblems of that color on the selected banner | `[empirical n=5]` — a whole-color stat reroll on Support forced all 3 blues to change |
| "…第一枚/最后一枚…" | exactly that one, by list order | `[n=6]` |
| "…随机一枚…" | one, uniform among that color | `[n=4]` |
| "随机提升一项品质" | one slot's quality +1..+3 tier; **T5 slots are never chosen** | `[n=3]` user-confirmed T5 exclusion |
| "随机提升两项品质，并降低一项品质" | two upgrades then one downgrade; T5 excluded from upgrades; **any** slot incl. T5 can be downgraded | `[n=6]` |
| "重新生成…的品质" | redraw quality from the rarity distribution (biased low) | `[n=6]` |
| "重新生成操作选项" | refresh the 3 options | costs **1 token** `[client-confirmed]` |
| "更改战队" | swap team for that role | **0 tokens**, all emblems kept, options pool unchanged `[client-confirmed]` |

Every roll (any button) costs 1 token and refreshes the option pool. `[official]`

## Reroll "must change" rule and its trap

- A rerolled attribute always differs from its previous value **on that slot**. `[empirical n=20+]`
- Slots rerolled in the same press are independent and **may land on the same value** (two Fractals appeared
  from one "all red traits" press). `[n=2]`
- **Trap:** a whole-color trait reroll necessarily removes any copy of trait X currently on those slots. So it
  can never *complete* a Friendly triple if the existing Friendlys are on the color being rerolled — it destroys
  them. Only single-slot trait rerolls on non-Friendly slots build toward 3-Friendly. Conversely, a whole-color
  reroll on slots that hold *dead* traits is a free lottery. `[n=3]`
- **A 3-Friendly set did complete once by luck**: whole-blue trait reroll on Support with one Friendly on a
  green slot — two of the three blues rolled Friendly (P≈1/16) and one Vampiric was replaced by Friendly at
  zero net loss. Don't plan on it; do recognize it when the cells line up.

## Quality distributions observed

- **Upgrade delta** ("提升" buttons): +1 ×3, +2 ×3, +3 ×2 observed. Working prior: {+1: 0.5, +2: 0.35, +3: 0.15}.
  `[n=8]`
- **Downgrade delta** ("降低一项"): −1 ×3, −2 ×1, −3 ×1, **−4 (T5→T1) ×1**. Working prior:
  {−1: 0.45, −2: 0.30, −3: 0.15, −4: 0.10}. The tail is real; a T5 on a big-base stat can lose 140% in one press.
  `[n=6]`
- **"重新生成品质" redraw**: outcomes seen T1 ×2, T2 ×2, T3 ×1, T4 ×1 from starting tiers 2–4. Consistent with
  "higher tiers rarer". Working prior: {T1 .30, T2 .28, T3 .22, T4 .14, T5 .06}. `[n=6]`
  → For a slot at T1–T2 it's positive EV (only up); at T3 ≈ neutral; at T4–T5 clearly negative.
- **T5 is terminal upward**: never selected by upgrade buttons; only appears on the downgrade die.
  `[user-confirmed]`

### Practical consequence for "two up, one down"

Its EV depends entirely on **how many non-T5 slots exist**:
- Many T5s → upgrade pool is tiny → the two upgrades are *forced* onto exactly the slots you want (Support with
  {5,2,5,5,2} → both T2s upgrade with certainty). Best-EV button of the campaign in that configuration.
- Few T5s and a T5 on your biggest stat → downgrade tail can cost 5,000+. Decline.

## Fractal under 5 emblems

Needs all 5 qualities distinct ⇒ exactly {1,2,3,4,5} ⇒ permanently pins one T1 and one T2 on the banner.
Any second T5 kills it forever (no button lowers a specific slot). Treat as a **bonus if it happens, never a
target**. `[reasoned + n=2 dead-forever cases]`

## Tokens & timeline

- Swiss grant 40, Main Event grant 30 (2026). Unspent Swiss tokens **carried into Main Event**. `[client-confirmed]`
- **Tokens cannot be used after the roster lock** of the final period → spend to zero before lock.
  `[user-confirmed 2026]`
- Coach titles lock **with** the roster snapshot (not freely changeable during the period, despite the tutorial
  wording). `[user-confirmed]`
- Emblem count per banner grew 3 → 5 between Swiss and Main Event; the two new slots arrived pre-populated.
  `[client-confirmed]`
- New option types appeared after the stage change. `[official + confirmed]`

## Scoring quirks (from settlement screens + community parsers)

- Settlement per-slot numbers are **two-game sums**. Derive implied base = points / multiplier.
- Community lotus projections ran ~2× above the measured result (projected 7,832 pair-base, measured 4,066 in a
  single Main-Event series). Lotus counting by Valve loses ~20% vs replays and the meta shifts fast; **haircut
  community lotus numbers heavily**.
- Watchers appear over-counted ~1.5× by the official API vs replays; Madstones under-counted ~3×; Tormentor
  credit goes to last-hitter though the game credits participants. (battlepass.ru parser notes, 2026.)
- Valve shipped a mid-event stun-scoring bugfix in 2025 with 3-token compensation per affected emblem — a
  reason to keep a *small* reserve until the first Main-Event day, unless tokens die at lock (they did in 2026,
  so no reserve).

## Things still unverified (carry these into next year's UNVERIFIED list)

- Exact rarity weights for quality upgrades/redraws (priors above are hand-fit to ~8 observations each).
- Whether "random" selection over slots is uniform or weighted.
- Whether prefix and suffix bonuses stack additively or multiplicatively (difference <1.5%).
- Whether Fractal counts quality distinctness across all 5 or only non-empty slots.
