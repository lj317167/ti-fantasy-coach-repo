# Predictions — group buckets and bracket

2026 result: groups **5/16 (720 pts)**, bracket **8/14 (4,320 pts)**. Groups were the weak spot: Claude picked from
pre-tournament form narratives; several favorites (BB, Yandex) missed 4-1 and several "eliminated" picks
qualified. The fix is a procedure, not better hunches.

## Group stage (小组赛) — 16 picks into record buckets

Structure (2026; re-read the client): 4-0 ×1 · 4-1 ×2 · Elim-round winners ×5 · Elim-round losers ×5 · 1-4 ×2 · 0-4 ×1.
Points escalate with total correct; no bonus for upsets → **maximize expected count**, i.e. rank by probability
and fill buckets top-down.

Procedure:
1. **Gather per-team strength** (all 16), tournament-agnostic:
   - Recent T1 results (last 60 days): EWC / Riyadh / DreamLeague / PGL — search `<team> results <month> <year>`
   - Roster changes since last event (stand-ins, loans — 2026 had a carry on loan and multiple rebrands)
   - Any rating board (Liquipedia/GosuGamers Elo, or calculator "title odds") — note rename resets
   - Head-to-head vs the field in the last 3 months
2. **Score each team 1–16.** A 4-0 in Swiss requires beating 4 opponents in a row; even the best team has
   maybe 25–35% — pick the single strongest, accept the variance.
3. **The middle ten**: elimination-round outcome ≈ seed 4–13. The five "qualified" should be ranks 4–8, the five
   "eliminated" ranks 9–13. Avoid the temptation to promote a favorite dark horse over a boring mid-table team.
4. Bottom three: 1-4 ×2 = ranks 14–15, 0-4 = rank 16 (usually the weakest regional qualifier).
5. Sanity check the whole slate against two independent sources (a calculator's title odds, a pundit preview).
   Where they disagree with your ranking, re-check; don't average blindly.
6. Log the slate with a one-line reason per team in `data/<year>/predictions.md` for the retrospective.

Deadline: locks at first-match start (2026: Aug 13, 02:00 UTC). Fantasy roster for Swiss locks at the same time.

## Bracket (国际邀请赛) — 14 series

Opens after groups, before the Main Event lock (2026: open Aug 17 01:00 UTC, lock Aug 20 02:00 UTC).

1. Use **Swiss results** as the primary signal — 4-0/4-1 direct qualifiers vs elimination-round survivors —
   plus map differential and who beat whom.
2. Pick every series independently by probability; then check the implied path is consistent (a team you
   have losing UB R1 must appear in LB R1).
3. Champion pick drives ~5 series. In 2026 the 4-0 team (VSN) was the natural champion pick and lost the
   final — that's variance, not an error. Do not hedge the champion pick against your fantasy roster; they
   should agree (same information).
4. Lock the bracket when the fantasy roster locks; both are one snapshot.

## Coupling with Fantasy

Predictions and fantasy use the same beliefs. Write the bracket first, then choose fantasy teams that play the
most series under that bracket, weighted by per-series projection (see `scoring-model.md §5`).
