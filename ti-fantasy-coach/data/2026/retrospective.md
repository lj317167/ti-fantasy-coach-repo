# TI 2026 Retrospective

Result: Swiss 52.9k / 83% → Main Event 108.0k / **99.75%** → overall 23,526 / 97%. Rewards: map + cosmetics.
Three chat sessions, ~31 Main-Event tokens spent over one evening, ~50 screenshots.

## What worked

1. **Slot-quality matching.** Realizing quality/trait stay on the slot changed the whole approach: reroll stats
   *into* the best slots. Lotus onto the T5 support slot, CS onto the T5 core slot, Runes onto a T5 mid slot —
   those three slots alone produced 42k of the 108k.
2. **Whole-color stat reroll as a deterministic swap.** With exactly three blue stats off-banner, "reroll all
   blue stats" was a guaranteed Lotus/Wards/Smokes placement — only the slot assignment was random.
3. **Roster switch on data, the night before lock.** Swapping core from Falcons to Team Vision (Satanic +
   Noticed, the calculators' #1 pair at 11,013/series) cost zero tokens and produced the 36k core banner.
4. **Dead-trait lotteries.** Any slot whose trait was dead (colliding Unique, lone Friendly, impossible Fractal)
   was a free 1/4 shot at Vampiric/Benevolent. Core CS 270% → 320% came from exactly this.
5. **Forced "two up one down."** On a banner with three T5s and two T2s, the two upgrades *had* to land on the
   two T2s; Lotus went T4→T5 for +3.9k. Recognizing when the upgrade pool is forced was the best single insight.
6. **Zero-out before lock.** Once we knew tokens die at lock, spending 31 → 1 with zero-EV lotteries in the
   last few presses landed a 1/16 three-Friendly completion on Support (+4k).
7. **Numbers over gut, twice.** The user noted two decisions where the EV table contradicted instinct and the
   table was right (the whole-blue stat reroll, and the improve2down1 on the T5-heavy support banner).

## What failed / cost points

1. **Rules inferred, not verified (Swiss).** Claude assumed buttons applied only to the selected banner,
   wasn't sure refresh/team-switch costs, and didn't know lock semantics. Cost: several suboptimal Swiss
   presses and one under-built banner. Fix → SKILL.md intake protocol + UNVERIFIED list.
2. **Under-spent in Swiss.** Held 33 tokens for an imagined "roster rebuild." Support went in with 3 slots and
   two trap stats (Tormentor 470, Runes 1,349) → 10.7k vs 23k/19k for the other banners. Fix →
   workflow/token-policy.md.
3. **Didn't re-rank stats proactively.** Only "obviously wrong" stats (Madstone on mid) were flagged for
   replacement; the systematic per-position ranking came only after the user supplied a streamer's tier list.
   Fix → scoring-model.md §2 + data-sources.md as a stage-start step.
4. **Early negative-EV quality gambles.** ~4 presses of "regenerate quality" on T3/T4 slots netted about −4k
   before the discipline "redraw only from T1–T2, improve-only buttons otherwise" was adopted. Fix → priors in
   mechanics-empirical.md and EV thresholds in token-policy.md.
5. **Too conservative at times.** Claude defaulted to "refresh" and to declining improve2down1 based on a
   mis-remembered "−2 minimum" note; the user pushed, the button paid. Fix → present tails and P(gain) rather
   than a verdict; treat zero-EV variance as acceptable in clear-out.
6. **Support stuns slot (598 measured) and mid Tormentor (1,758)** were the weakest real slots — green
   candidates for this roster were all weak; acceptable, but next time look at whether Roshan/Courier fit the
   drafted supports' style before defaulting to Stuns.
7. **Group predictions 5/16.** Picks followed pre-tournament narratives (BB/Yandex as 4-1) and mis-sorted the
   middle ten. Fix → references/predictions.md procedure (rank all 16, fill buckets top-down, two-source check).
8. **Title choice.** the Clutch (+16% only in a deciding game) was carried through Swiss with two banners on a
   team that sweeps; switched to **the Tormented (+23%, ~50% trigger)** before the Main Event lock, keeping
   Otherworldly as prefix. Confirmed by the user; the 108k Main Event result was scored under Otherworldly + the
   Tormented. Lesson stands: choose the suffix from the drafted teams' *style*, not from the raw bonus.

## Mechanics learned this year (moved to references/mechanics-empirical.md)

Trait line = net effect · adjacency = list order · three independent tracks · button scope by wording ·
must-change per slot but duplicates across slots · upgrade +1..+3, downgrade −1..−4 · T5 never upgraded ·
Fractal needs {1,2,3,4,5} · tokens carry between periods but die at final lock · titles lock with roster ·
team switch free.

## Process notes for next year

- Run the whole campaign in one Claude Code / Cowork session pointed at this repo; keep the state JSON as a file.
- Photograph settlement screens *and* the option list before every press; the audit trail is what made the
  empirical file possible.
- Budget real time: the interstage rebuild took one evening (~3 h) for ~30 tokens. Start the night before the
  night before lock.
