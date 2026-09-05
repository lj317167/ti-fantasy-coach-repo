# Token Policy — how many to spend, when, on what

## The 2026 mistake this file prevents

In Swiss, Claude advised stopping with **33 tokens unspent** to "keep reserves for a roster rebuild." That was
wrong twice: team switches are free (emblems persist), and the Main Event brought its own grant. The user
overrode and spent down to 7; the Swiss support banner still went in under-built and scored 10.7k while the
other two banners scored 23k and 19k. Then before the Main Event lock, the user reminded Claude that **tokens die
at lock** — and the remaining 31 were spent to 1, producing the 99.75% result.

Rule: **tokens are worthless after the final lock; hoarding has no upside unless the client explicitly says
tokens survive the lock.** Verify that once per year in the intake protocol.

## Per-stage budget shape

Let G = grant this stage, C = carry-over.

| Phase | Spend target | Purpose |
|---|---|---|
| Stage start (targets known) | ~40% of (G+C) | Stat placement: get the right stats onto the right slots. Deterministic-ish, highest EV/token. |
| Mid-stage | ~30% | Dead-trait lotteries, forced upgrades, breaking trait collisions. |
| Pre-lock clear-out | remaining, to **0–1** | Zero-EV/high-variance moves allowed; refresh freely to hunt a specific button. |

If tokens *do* carry to a later stage: keep ≈ the cost of one full banner re-placement (≈6–8 tokens) as the
floor, not more — the next stage brings its own grant, and stage-2 buttons (new option types, more emblems)
are worth more per token than stage-1 buttons.

## Refresh economics

Refresh costs 1 token and is *cheaper* than pressing a mediocre button "to cycle the pool." Refresh when no cell
in the nine-cell grid is ≥ +0 EV, or when the hunted button has high value (single-slot stat reroll onto a T5
slot was worth ~+11k projected in 2026 — worth several refreshes). Budget refreshes explicitly: "up to N
refreshes for this button, then take the best available cell."

## EV thresholds by phase

- **Early/mid**: press only ≥ +0 EV with acceptable tails. Negative-EV needs explicit user override.
- **Clear-out (last ~6 tokens before lock)**: ≥ −0 EV with fat upside is fine — the alternative is a wasted
  token. Still decline moves whose disaster branch hits a red-line slot.
- Never spend on Fractal completion, madstone, or upgrading a slot to justify a weak stat.

## Variance policy (user's stated preference)

The user maximizes percentile and accepts variance. Present tails; when EV ≈ 0, recommend the higher-variance
option in clear-out and the lower-variance one earlier. When the user asks for a negative-EV gamble, give one
sentence of pushback with the number, then execute and plan the follow-ups for both branches.

## What tokens buy, roughly (2026 measured, for calibration)

| Move | Typical Δ | Tokens |
|---|---|---|
| Stat reroll onto a T5 slot (big stat) | +8k … +11k | 2–4 incl. refreshes |
| Whole-color stat reroll when off-banner pool is exactly what you want | +5k … +15k | 1 |
| Dead-trait lottery on a big-base slot | +1k EV, +3.5k best | 1 |
| Forced "two up one down" on a mostly-T5 banner | +3k EV (observed +0.6k … +5k) | 1 |
| Breaking a dead-Unique collision | +1k … +2k | 1 |
| "Regenerate quality" on a T4 slot | −1k EV | avoid |
| Random quality gamble on a T3 slot | ≈ 0 | clear-out only |
