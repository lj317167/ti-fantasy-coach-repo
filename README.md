# ti-fantasy-coach

A Claude skill for the Dota 2 **The International Compendium Fantasy Challenge** (梦幻挑战) and **Tournament
Predictions** (赛事预测). Built from the TI 2026 campaign: Swiss 83rd percentile → Main Event **99.75th**,
overall 97th.

It encodes the rules (with the year they were verified), the button mechanics that were confirmed by spending
tokens, a scoring model, a per-stage checklist, a decision protocol, an EV calculator, and the 2026 data as a
calibration baseline. Read `ti-fantasy-coach/SKILL.md` first.

> 不负责声明 / Disclaimer: this is a hobby project shared as-is. Valve changes the fantasy system every year;
> the skill's first instruction is to re-verify everything. No guarantee of percentile, prizes, or sanity.

## Layout

```
ti-fantasy-coach/          ← the skill (this is what gets zipped for claude.ai)
  SKILL.md                 ← intake protocol, stage router, hard rules
  references/              ← official rules, empirical mechanics, scoring model, predictions, data sources, glossary
  workflow/                ← timeline, decision protocol, token policy
  scripts/ev_calc.py       ← Monte-Carlo nine-cell EV table from a state JSON
  data/2026/               ← archived data, measured settlements, retrospective
  templates/banner_state.json
archive/                   ← screenshots etc. (repo only, not part of the skill)
```

## Install — Claude Code

```bash
git clone <this repo> ~/skills/ti-fantasy-coach-repo
ln -s ~/skills/ti-fantasy-coach-repo/ti-fantasy-coach ~/.claude/skills/ti-fantasy-coach
```

Or copy the `ti-fantasy-coach/` folder into `.claude/skills/` of a project. Claude Code picks it up by the
frontmatter description. Recommended: run the whole campaign in one Claude Code (or Cowork) session pointed at
this repo, and keep `state.json` as a real file that Claude edits after every press.

## Install — claude.ai (web / desktop)

Custom skills are uploaded as a zip through Settings → Capabilities/Customize → Skills (Pro/Max/Team/Enterprise
with code execution enabled). The zip must contain **the skill folder itself**, not the whole repo:

```bash
zip -r ti-fantasy-coach.zip ti-fantasy-coach -x "*.DS_Store"
```

Don't upload GitHub's "Download ZIP" (it wraps everything in `<repo>-main/`, which the uploader rejects).
The `description` in SKILL.md is kept under 200 characters on purpose — claude.ai caps it there.

## Using the EV calculator

```bash
python3 ti-fantasy-coach/scripts/ev_calc.py state.json                       # evaluates state["options"] on all banners
python3 ti-fantasy-coach/scripts/ev_calc.py state.json --button improve2down1 --banner support
python3 ti-fantasy-coach/scripts/ev_calc.py --help                            # button grammar
```

`templates/banner_state.json` is a complete example (the real 2026 pre-lock state).

## Yearly maintenance

1. Re-transcribe the in-client rules → `references/rules-official.md` (bump the year).
2. Update `[empirical n=X]` counts and the priors in `references/mechanics-empirical.md`.
3. Add `data/<year>/measured_settlements.md` and `retrospective.md`.
4. Refresh calculator URLs in `references/data-sources.md`.

## Updating

The `ti-fantasy-coach/` folder is the single source of truth; zips are build artifacts.

- **Claude Code**: symlinked → `git pull` is the update.
- **claude.ai**: run `./scripts/build.sh` and re-upload `dist/ti-fantasy-coach.zip` (replaces the old version).
  Or push a tag (`git tag v2027.1 && git push --tags`) and the GitHub Action attaches the zip to a Release.
- Re-upload to claude.ai only at milestones (e.g. after the yearly intake update), not every commit.
