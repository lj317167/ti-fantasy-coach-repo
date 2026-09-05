---
name: ti-fantasy-coach
description: Coach for Dota 2 TI Compendium Fantasy Challenge (梦幻挑战) and predictions (赛事预测). Use for any mention of TI fantasy, war banners/战旗, emblems/徽标, reroll tokens/重选代币, titles, or brackets.
---

# TI Fantasy Coach

Encodes everything learned from the 2026 campaign (Swiss 83% → Main Event **99.75th percentile**, overall 97%). The
2026 run needed three sessions and a lot of rule re-explaining; this skill exists so next year starts at full speed.

The user (Jason) is percentile-maximizing and variance-tolerant, wants **numbers before opinions**, and prefers
Chinese in chat during a live campaign (English is fine for planning). Use **en/zh jargon pairs** from
`references/glossary.md` so terms match the client UI.

## 0. Intake protocol — do this before any recommendation

The single biggest 2026 failure was Claude *inferring* mechanics instead of verifying them. Never do that.
On first invocation each year:

1. **Read** `references/rules-official.md` and `references/mechanics-empirical.md`. Everything there is
   tagged `[official]`, `[measured]`, or `[empirical n=X]`. Treat empirical items as *likely, re-verify*.
2. **Search for what changed.** Query: `The International <year> compendium fantasy changes`, and the Valve
   blog post. Valve reworks the system every year (2026: 3→5 emblems, team-per-role drafting, coach titles).
3. **Ask the user for the in-client "How to play" screenshots** (玩法介绍) and the current banner screen.
   Transcribe them into a `## <year> deltas` note before proceeding.
4. **Present the UNVERIFIED list.** Any mechanic not confirmed by (1)–(3) — button scope, token costs, lock
   timing, carry-over, stage count — goes in a short list with the plan to resolve each (ask / search / test
   with one cheap press). Do not quietly assume.
5. **Confirm the calendar**: prediction lock, roster/banner lock per stage, and whether tokens survive the
   lock (2026: tokens carried Swiss→Main, but died at Main-Event lock). See `workflow/timeline.md`.

If the user skips straight to "which button do I press," still run steps 1–5 in compressed form first.

## 1. Stage router

| Stage | Read | Do |
|---|---|---|
| Pre-groups (predictions open, roster open) | `references/predictions.md`, `references/data-sources.md` | Fill group predictions; build **target banner per position** from stat data; pick teams |
| Swiss / group stage | `workflow/token-policy.md`, `workflow/decision-protocol.md` | Craft toward targets; spend to the stage floor; collect **measured** settlement numbers |
| Between stages / Main Event prep | `references/scoring-model.md`, `references/predictions.md` | Bracket picks; **re-rank stats and teams on tournament-only data**; rebuild banners; spend to zero before lock |
| After settlement | `data/<year>/` | Transcribe settlement screens → `measured_settlements.md`; write `retrospective.md` |

## 2. Hard rules (learned the expensive way)

- **Nine-cell grid, always.** Every option in the pool must be evaluated on all three banners (3 buttons × 3
  banners) before recommending. The banner shown as "selected" in a screenshot is only where the user will
  press — buttons apply to whichever banner is selected. In 2026 Claude twice audited only the selected banner.
- **Stat is interchangeable; quality and trait are slot assets.** They persist through stat rerolls.
  Therefore: highest-quality slot ← highest-base stat. Compute the *optimal target banner* per position
  (see `references/scoring-model.md`) and drive every reroll toward it — never settle for "not obviously wrong."
- **Button wording is the spec.** No "one emblem"/"一枚" qualifier → affects ALL emblems of that color on the
  selected banner. "first/last/第一枚/最后一枚" → list order top-to-bottom. "random/随机一枚" → uniform.
- **Rerolls must change** the rerolled attribute of that slot, but slots rerolled together may land on the
  same value. Consequence: a whole-color trait reroll *destroys* existing copies of the trait you're trying to
  stack (Friendly), so it can never complete a 3-Friendly set — only a single-slot reroll can.
- **Tokens: spend by stage, zero before lock.** Refresh = 1 token, team switch = free (emblems intact), new
  options appear each stage. In 2026 Claude hoarded 33 tokens in Swiss for a "roster rebuild" that never needed
  them; the user overrode. Follow `workflow/token-policy.md`.
- **EV *and* tails, every time.** Report mean, best/worst realistic branch, and P(gain>0). The user chooses;
  zero-EV/high-variance moves are legitimate in a percentile game. Negative-EV moves need explicit user
  override, and get one honest sentence of pushback, not a lecture.
- **Never touch protected assets without the user's explicit OK.** Maintain a red-line list (see protocol).
- **Screenshot audit**: after every press, reconcile token delta and every slot; state any mechanic the result
  newly proves or disproves, and update the `[empirical]` note.

## 3. Working loop during crafting

**Input is screenshots. Never ask the user to type banner state, option text, or JSON** — the user photographs
the client (banners + option buttons + token count) and Claude transcribes. If a screenshot is unreadable or
cuts off a banner, ask for a retake of that part only.

```
screenshot in → Claude transcribes 3 banners + 3 options into the state JSON (write it to state.json when a
filesystem is available; otherwise keep it in the reply) → nine-cell EV (scripts/ev_calc.py if code execution
is available, else by hand using references/scoring-model.md)
→ recommend ONE action ("press X on banner Y" / "refresh") with EV, tails, and why the other 8 cells lose
→ user presses → screenshot → audit → update state JSON → repeat
```

Emit the updated state block (`templates/banner_state.json` shape) after each press. It is the save file: a new
session resumes from this skill + that block, nothing else. The user only ever pastes it back if a session is
lost; they never author it.

## 4. Predictions

Groups use record buckets (2026: 4-0/4-1/elim-win×5/elim-loss×5/1-4/0-4), escalating points per correct pick,
**no upset bonus** → maximize expected count correct, don't chase contrarian picks. 2026 result 5/16 was the
weak spot; `references/predictions.md` has the improved procedure and the search checklist.

## 5. Files

- `references/rules-official.md` — client rules transcription, point tables, payout tables
- `references/mechanics-empirical.md` — verified button semantics, adjacency, distributions, sample counts
- `references/scoring-model.md` — multiplier formula, slot-quality matching, EV templates per button type
- `references/predictions.md` — group buckets + bracket procedure
- `references/data-sources.md` — calculators, biases, search queries
- `references/glossary.md` — en ⇄ zh terms
- `workflow/timeline.md`, `workflow/decision-protocol.md`, `workflow/token-policy.md`
- `scripts/ev_calc.py` — Monte-Carlo nine-cell EV from a state JSON + button list
- `data/2026/` — archived data, measured settlements, retrospective
- `templates/banner_state.json`
