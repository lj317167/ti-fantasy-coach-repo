# Data Sources — where the numbers come from, and how much to trust them

Order of trust: **measured settlement screens** > tournament-only replay parsers > season-average calculators >
pundit picks. Always say which tier a number came from.

## Tier 0 — your own settlement screens `[measured]`

After each period, photograph every banner's settlement (per-slot points + multiplier) and the summary
(total, percentile, top-100 board). Transcribe into `data/<year>/measured_settlements.md` and derive
`implied base = points / multiplier` per slot. These are the only numbers that include Valve's real counting.
2026 archive: `data/2026/measured_settlements.md`.

## Tier 1 — replay-parsed fantasy calculators (verify URLs each year; they are per-TI)

- **battlepass.ru/en/ti<year>/fantasy-calc** — thousands of replays parsed; "TI only" vs "whole season" toggle;
  pair projections with bracket-odds weighting ("41% title odds, 11,013/series"). Documented parser notes:
  official API over-counts watchers ~1.5×, under-counts madstones ~3×, lotus loses ~20%, tormentor credit to
  last-hitter. Removes eliminated teams from the picker.
- **ti<year>calculator.com** — player-level projections from ~1,600 T1 matches; per-emblem expected points.
- **r/Maroomm fantasy data** (Reddit) — the community spreadsheet many guides cite; per-stat top-3 tables by
  role.

Use "TI only" once ≥8–10 maps exist per player; before that, blend with season.

## Tier 2 — guides (good for meta framing, weak for numbers)

- esportsinsider / teamsmurf / dota2protips fantasy guides — recommended pairs, title picks. Updated mid-event.
- GosuGamers / Liquipedia match pages — per-game LH/DN, GPM, KDA, towers for a specific series.
- Dotabuff / DLTV team pages — hero pools (for prefix choice).

## Known biases to apply

| Stat | Adjustment | Why |
|---|---|---|
| Lotus | −20% from parser numbers, and expect meta drift | Valve counting + 2026 measured ≈ half of projection |
| Watchers | −33% from official-API-based numbers | 1.5× over-count |
| Madstone | ignore unless a specific player farms them | +13 each; only spikes in marathon games |
| Tormentor / Roshan / FB / Courier | keep, but treat as spiky | max-selection rewards spikes; coin-flip per game |
| Teamfight | keep | undocumented Valve formula, capped 2,124/game |
| Deaths | keep | 1,950 − 195/death; stable; suits low-death mids |
| Stuns | keep, low base for most supports | 10/sec |

## Search checklist (run at each stage)

Pre-groups:
- `The International <year> compendium fantasy` (Valve blog / patch notes — rule changes)
- `TI <year> fantasy calculator`, `TI <year> fantasy picks reddit`
- `<team> roster <year>` for every team with a recent change
- `<team> results <last event>`; EWC / Riyadh standings

Between stages:
- `TI <year> group stage results`, `TI <year> swiss standings`
- `TI <year> fantasy main event picks` (guides update ~Aug 18)
- `<player> TI <year> stats` for shortlisted pairs (GPM/CS/KDA averages)
- `TI <year> bracket` for schedule and lock times

## Recording standard

Whenever a projection is used in a decision, log: value, source tier, date pulled, and any haircut applied.
The retrospective compares these against Tier 0 to recalibrate next year's haircuts.
