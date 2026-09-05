# Scoring Model — how to turn a banner screen into numbers

## 1. Per-slot score

```
multiplier(slot) = 100% + quality_bonus[tier] + trait_net(slot, banner)
points(slot)     = base(stat, players) × multiplier / 100
banner_points    = Σ slots
```

`base(stat, players)` = the two-best-games sum the players actually produce for that stat (see
`data/<year>/measured_settlements.md` for measured examples; `references/data-sources.md` for projections).

Quality bonus: T1 10, T2 30, T3 60, T4 100, T5 150. **Tier deltas are not uniform**: 1→2 = +20, 2→3 = +30,
3→4 = +40, 4→5 = +50. So an upgrade is worth most on a high tier *and* a high base.

trait_net = own conditional (Unique +30 if sole / Friendly +50 if ≥3 / Fractal +60 if all tiers distinct /
Vampiric +50) + Σ neighbors (Benevolent neighbor +20 each; Vampiric neighbor −10 each). Adjacency = list order.

## 2. Slot-quality matching (the single most valuable idea)

Because quality/trait stay on the slot when the stat is rerolled:

1. Rank the position's available stats by expected base (color-constrained per slot).
2. Sort the slots by multiplier.
3. Target = biggest base on biggest multiplier, and so on down.
4. Reroll *stats* to reach the target. Only then spend on quality/trait.

2026 example (Support): Lotus (7.8k projected) was off-banner while Runes (1.3k) sat on the T5 slot. Moving Lotus
to the T5 slot was worth ~+11k projected — more than every quality gamble of the night combined. Getting Lotus onto
the T4 slot instead of T5 would have cost ~4k. The slot matters as much as the stat.

## 3. Whole-color stat reroll = deterministic when the off-banner pool is small

Blue pool has 6 stats; a support banner holds 3 → exactly 3 off-banner. "Reroll all blue stats" forces the three
slots to take **the three off-banner stats** (each slot must change, no duplicates). If the off-banner three are
the ones you want, the button is a guaranteed swap — only the *assignment to slots* is random (1/3 per slot).
Same logic for red on a 2-red mid banner: 4 off-banner, 2 slots → P(specific stat lands) = 50%.

## 4. EV templates per button type

Report every action as: **mean Δ, best realistic branch, worst realistic branch, P(Δ>0)**. Use
`scripts/ev_calc.py` for the full distribution; the shapes below are for quick hand checks.

**Single-slot stat reroll.** Candidates = color pool − on-banner stats, uniform. Δ = mult × (base_new − base_old).
Cycle until target; each miss is a re-draw (old stat returns to pool).

**Single-slot trait reroll (current trait dead).** Free lottery: 1/4 each of the other four traits.
Value the four outcomes with the *actual* neighbors (e.g. Vampiric on a 7.8k base next to a 3.3k base:
+3,916 − 336). Unique is +30 only if no other Unique exists. Friendly is +50 × three stats only if it completes a
triple — otherwise 0.

**Single-slot trait reroll (current trait alive).** Same lottery minus the value being destroyed *including what
it feeds neighbors* (a Benevolent feeding two big neighbors can be worth more than any replacement).

**Whole-color trait reroll.** Sum the single-slot templates, then add cross-slot terms: P(two Friendly) = C(k,2)/16
etc., P(two Unique collide) = 1/16 per pair. Remember it *deletes* existing Friendly/Unique on those slots.

**"Regenerate quality" (redraw).** Prior {T1 .30, T2 .28, T3 .22, T4 .14, T5 .06}. EV is positive from T1–T2,
≈0 at T3, negative at T4+. Never on a T4/T5 slot with a big base.

**"Improve one quality."** Uniform over non-T5 slots; delta prior {+1 .5, +2 .35, +3 .15}. Always ≥0. Value
∝ base × tier-delta. Best when the non-T5 pool is exactly the slots you want raised.

**"Improve two, lower one."** Upgrades: two distinct draws from non-T5 slots (if only two exist, both are forced).
Downgrade: one draw over *all* slots incl. T5; delta prior {−1 .45, −2 .30, −3 .15, −4 .10}. Compute the
upgrade EV and the downgrade EV separately and show the disaster branch (biggest-base T5 hit for −3/−4)
explicitly. It was the best button of 2026 on a {5,2,5,5,2} banner and a coin-flip elsewhere.

## 5. Roster / team choice

- Score the *pair*, not the star: core = pos1+pos3 averaged, support = pos4+pos5 averaged.
- Prefer **tournament-only** data once ≥8 maps exist; season averages wash out patch/meta.
- Fit matters as much as talent: a CS/GPM-heavy banner wants a farming core duo; a Lotus/Sentry banner wants a
  support duo with that habit. Compare candidate teams *slot by slot* against the actual banner.
- Best-series selection rewards depth: a team predicted to play 5 series gives more draws than one playing 3,
  but a 4-series favorite with +1,100/series projected still wins. Weigh both.
- Correlation: 3 slots over 2 teams is fine (2-1). All three on one team is a legitimate high-variance play in
  a percentile game, not a mistake — but say so out loud.
- Switching team is free and keeps emblems: **re-evaluate the roster after the Swiss data lands** and before
  lock. 2026: swapping core from FLCN to VSN the night before lock was the highest-EV zero-token action.

## 6. Coach titles

Expected value = bonus × P(condition fires per game). Estimate P from the *chosen teams'* style:

| Suffix | P estimate (pro games) | Note |
|---|---|---|
| the Tormented +23% | 0.45–0.55 | rises with game length; correlates with Tormentor emblems |
| the Patient +23% | 0.15–0.20 | |
| the Decisive +24% | 0.10–0.15 | |
| the Lucky +21% | 0.10 | pure noise |
| the Clutch +16% | P(series goes the distance) | **≈0 for teams that sweep** — bad with a dominant favorite |
| the Cruel +13% | low, unobservable | |

Prefix: pick from the drafted players' actual hero pools (client hero tags). 2026 calculators rated
Otherworldly best raw EV and Heroic best "fires often". Titles lock with the roster — decide before lock.

## 7. Percentile mindset

The payout has a cliff (80th → 90th = +2,600). Variance is a resource: take it from **roster correlation and
schedule** (positive-EV variance) and from zero-EV emblem lotteries in the clear-out phase — not from
negative-EV quality gambles early. Present the tails so the user can choose; don't decide for them.
