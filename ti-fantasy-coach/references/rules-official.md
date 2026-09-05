# Official Rules — TI 2026 client transcription

Source: in-client "How to play" (玩法介绍) screens, photographed and transcribed 2026-08-18. Tag: `[official]`.
Valve changes these yearly. **Re-transcribe from the current client before trusting any number here.**

## Two point systems

Predictions (赛事预测) and Fantasy (梦幻挑战) are separate, both feed the overall Compendium score.
2026 maxima: Predictions 12,000 + 12,000; Fantasy 12,000 per settlement period (2 periods).

## Predictions

**Group stage (小组赛)** — place all 16 teams into record buckets. Points escalate with count correct:

| Correct | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pts | 30 | 60 | 120 | 360 | 720 | 1200 | 1800 | 2520 | 3360 | 4320 | 5400 | 6600 | 7920 | 9360 | 10920 | 12000 |

2026 buckets: **4-0 (1) · 4-1 (2) · Qualified via Elimination Round (5) · Eliminated via Elimination Round (5) · 1-4 (2) · 0-4 (1)**.
The middle ten are judged by elimination-round *results*, not Swiss seeding.

**Bracket (国际邀请赛)** — pick the winner of all 14 main-event series (8-team double elimination, Bo3, GF Bo5).

| Correct | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pts | 120 | 360 | 720 | 1200 | 1800 | 2520 | 3360 | 4320 | 5400 | 6600 | 7920 | 9360 | 10920 | 12000 |

No bonus for bold picks in either table → maximize expected number correct.

## Fantasy — roster (打造基础知识)

- Draft by **team per role slot**: both supports (4+5) from one team, safelane+offlane (1+3) from one team,
  one midlaner. The same team may fill multiple slots (client-confirmed 2026).
- One War Banner (战旗) per role slot; a duo shares the banner and is **averaged**.
- Team can be changed freely ("更改战队") until the period's roster snapshot. Emblems stay.
- New crafting options appear after each period — "在每个阶段结束后记得回来确认".

## Fantasy — rolling (重新生成)

- Always **3 unique roll options**, identical for all banners.
- Each roll costs **1 token**, affects **only the currently selected banner**, and **replaces all three options**.
- (Empirical, see mechanics file: the "regenerate options" button costs 1 token; team switch costs 0.)

## Fantasy — coach titles (指导员称号)

One prefix + one suffix, applying to all your players; each gives a % bonus to a game's final score when its
condition is met. Changeable without tokens **until the roster snapshot locks** (empirical: locked after).

Prefixes (hero attribute of the hero played that game):

| Prefix | zh | Bonus | Condition |
|---|---|---|---|
| Crimson | 赤红的 | +6% | red hero |
| Cerulean | 蔚蓝的 | +11% | blue hero |
| Emerald | 翠绿的 | +6% | green hero |
| Royal | 尊贵的 | +10% | purple hero |
| Golden | 金色的 | +8% | yellow or brown hero |
| Elemental | 元素的 | +8% | Aquatic / Fiery / Icy |
| Otherworldly | 异界的 | +7% | Undead / Demon / Spirit |
| Heroic | 英雄的 | +9% | Caped / Masked |

Suffixes (game event):

| Suffix | zh (approx.) | Bonus | Condition |
|---|---|---|---|
| the Tormented | 受折磨者 | +23% | any player dies to a Tormentor |
| the Flayed Twins Acolyte | 剥皮双子信徒 | +9% | first blood before the horn |
| the Patient | 耐心者 | +23% | no first blood before 10:00 |
| the Underdog | 弱者 | +6% | games the player loses |
| the Decisive | 果断者 | +24% | game shorter than 25:00 |
| the Clutch | 关键之人 | +16% | last *possible* game of a series (G3 of Bo3 / G5 of Bo5) |
| the Lucky | 幸运者 | +21% | match clock ends with an 8 |
| the Cruel | 残忍者 | +13% | a player is killed in their own fountain |

Hero color/attribute tags ship in the client (`npc_heroes.txt` "Adjectives"); no public API. Verify zh names
against the client — the ones above are working translations.

## Fantasy — scoring pipeline (积分规则)

1. When a period's matches begin, the roster is snapshotted.
2. Each player scores **individually per game**, only for stats present on the banner, × title bonus if met.
3. Duo scores are **averaged** per game → role score for that game.
4. Role's series score = **top two games** within the series.
5. If a role plays several series in a period, **the best series** counts. (Not a sum.)

Implication: more series = more draws for the max; spiky stats (Roshan, Tormentor, FB) are partially re-rated
upward by max-selection; a single monster series carries the period.

## Base stat values (每项数据的基础得分)

| Stat | zh | Points | Color |
|---|---|---|---|
| Kills | 击杀 | +107 per kill | Red |
| Deaths | 死亡 | 1,950 start, −195 per death | Red |
| Creep Score | 正反补 | +3 per last hit or deny | Red |
| GPM | GPM | GPM × 2 | Red |
| Madstone | 狂石收集数量 | +13 per stone | Red |
| Tower Kills | 摧毁防御塔 | +352 per tower | Red |
| Wards Placed | 放置守卫 (侦察守卫) | +117 per observer | Blue |
| Camps Stacked | 堆叠野怪 | +234 per stack | Blue |
| Runes | 拾取/激活神符 | +141 per rune | Blue |
| Watchers | 占领观察者 | +147 per watcher | Blue |
| Smokes Used | 开雾次数 | +293 per smoke | Blue |
| Lotuses | 采集莲花 | +176 per lotus | Blue |
| Roshan | 击杀肉山 | +1,172 per kill | Green |
| Teamfight | 参与团战 | max 2,124 | Green |
| Stuns | 眩晕时间 | +10 per second | Green |
| Tormentor | 消灭痛苦魔方 | +879 per kill | Green |
| First Blood | 第一滴血 | 1,934 | Green |
| Courier Kills | 杀害信使 | +703 per kill | Green |

Because a slot's points are the sum of the best two games, "base" numbers in settlement screens are
**two-game sums** (e.g. GPM base 3,226 ≈ two games at ~806 GPM).

## Emblems (徽标)

Each emblem = Color · Stat · Quality · Trait. Color distribution per banner is fixed by role; the stat is
determined by color; rerolling a stat always yields a new stat; **no duplicate stats on one banner**.

2026 layouts (5 emblems from the Main Event; 3 during Swiss): Core 3R+2G, Mid 2R+1B+2G, Support 3B+2G.
Verify each year.

Quality (品质): T1 +10% · T2 +30% · T3 +60% · T4 +100% · T5 +150%. Higher tiers rarer when crafting.

Traits (特性):

| Trait | zh | Effect |
|---|---|---|
| Fractal | 分形 | +60% to this stat if **all** emblem qualities on the banner differ (5 emblems ⇒ exactly {1,2,3,4,5}) |
| Benevolent | 仁爱 | +20% to the stat of each **adjacent** emblem |
| Vampiric | 吸血鬼 | +50% this stat, −10% each adjacent emblem |
| Unique | 唯一 | +30% if this is the only Unique on the banner |
| Friendly | 友好 | +50% if ≥3 Friendly emblems on the banner |

## Rewards (奖励) — per settlement period, percentile vs everyone who submitted

| Percentile | 100 | 99 | 95 | 90 | 80 | 60 | 40 | 20 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| Points | 12,000 | 11,400 | 10,000 | 8,400 | 5,800 | 3,300 | 1,700 | 400 | 200 |

Relative scoring: beat other rosters, not an absolute target. Note the cliff between 80th (5,800) and 90th
(8,400) — that gap is the whole point of optimizing.
