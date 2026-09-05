# Decision Protocol — how each press gets decided

The user sends a screenshot; Claude returns one recommended action with numbers. Discipline here is what turned
83% into 99.75%. The failures it prevents (all happened in 2026): auditing only the selected banner, pressing
whole-color buttons that destroyed live traits, assuming button scope, forgetting that quality/trait persist.

## 1. Transcribe

From the user's screenshot, Claude writes (or updates) the state block for all three banners: per slot — color, stat, tier,
trait, displayed multiplier and trait-line value; token count; the three option texts verbatim. If a banner is
cut off, ask for it — don't guess.

Reconcile the displayed multiplier: `100 + tier bonus + trait line` must equal the number shown. If it doesn't,
your adjacency/trait model is wrong for that slot — resolve before recommending.

## 2. Nine-cell grid (mandatory)

For each of the 3 options × 3 banners, one line: `✓ / △ / ✗ — EV, key branch`. Skip nothing; "not applicable"
(e.g. red button on a banner with no red) is an explicit cell. The user often has a different banner in mind
than the one selected — the grid catches value elsewhere.

Use `scripts/ev_calc.py` when the cell is close or involves multi-slot effects; hand-estimate the obvious cells.

## 3. Red lines

Keep a running list of protected assets: high-tier slots holding big-base stats, live Vampiric/Unique traits,
Benevolent slots feeding big neighbors, Friendly slots in a 2-of-3 set. A button that *could* hit a red-line
asset ("all green traits", "random red quality", "two up one down" with a T5 on the biggest stat) is ✗ by
default. The user may override with an explicit sentence ("I want to take the risk") — then run it, log it, and
never re-argue it after the roll.

## 4. Recommend

One action. Format:

```
按 <option N> @ <banner>  |  EV +X · best +Y · worst −Z · P(gain) p%
Why the other cells lose: <one clause each for the 2–3 closest alternatives>
Refresh instead if: <condition>
```

Prefer, in order: positive-EV deterministic moves (stat placement, dead-trait lotteries, forced upgrades) →
positive-EV gambles → refresh (1 token) → zero-EV variance plays (only in clear-out phase) → decline.

State the variance honestly: "this is a +900 EV coin with a 5% branch of −5,000" is a recommendation the user
can act on; "don't" is not.

## 5. Audit after the press

- Token delta = 1 per roll/refresh, 0 per team switch. Any other delta → ask what happened.
- Re-derive every changed slot's multiplier. Record what the result *proves* (e.g. "downgrade −3 observed") and
  bump the `n=` count in mechanics-empirical.md at the end of the session.
- If the result contradicts a mechanic you relied on, say so immediately and re-run the grid before the next press.

## 6. State block (the save file)

After each audited press, emit:

```json
{
  "stage": "main-event-prep", "tokens": 12, "lock_utc": "2026-08-20T02:00Z",
  "titles": {"prefix": "Otherworldly", "suffix": "the Tormented"},
  "banners": {
    "core":    {"team": "VSN", "players": ["Satanic","Noticed"], "slots": [
      {"color":"red","stat":"towers","tier":4,"trait":"fractal"}, ...]},
    "mid":     {...}, "support": {...}
  },
  "red_lines": ["support.slot1 Lotus T5", "core.slot3 CS T5 Vampiric"],
  "queue": ["support: reroll stat on slot2 → Lotus", "mid: single red trait on slot1 → Friendly/Vampiric"]
}
```

Full schema in `templates/banner_state.json`. A new session needs only this block + the skill to continue.

## 7. Tone

Numbers first, then one line of judgment. When the user overrides, comply and make the roll as informed as
possible ("if it lands X we then do Y"). After a bad roll, no post-mortem lecturing — state the new position and
the next best move. After a good roll, say what it unlocks.
