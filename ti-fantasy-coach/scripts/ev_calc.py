#!/usr/bin/env python3
"""
ev_calc.py — nine-cell expected-value table for TI Fantasy war-banner buttons.

Usage:
    python ev_calc.py state.json                      # evaluate the 3 options in state["options"] on all banners
    python ev_calc.py state.json --button "reroll stat red all" --banner mid
    python ev_calc.py state.json --samples 50000

The state file follows templates/banner_state.json. Each slot needs color, stat, tier, trait.
Base stat values (two-best-games sums) come from state["bases"][role][stat]; missing stats default to 0
(so add every candidate stat you care about, off-banner ones included).

Button spec grammar (case-insensitive, whitespace separated):
    <action> <target> <color> <scope>
    action : reroll | improve1 | improve2down1 | refresh
    target : stat | trait | quality          (only for reroll)
    color  : red | green | blue | any
    scope  : all | first | last | random     (default all)
Examples:
    "reroll stat blue all"        重新生成蓝色徽标的统计数据
    "reroll trait green first"    重新生成第一枚绿色徽标的特性
    "reroll quality red random"   重新生成随机一枚红色徽标的品质
    "improve1"                    随机提升一项品质
    "improve2down1"               随机提升两项品质，并降低一项品质

Model assumptions (edit PRIORS if new observations say otherwise; see references/mechanics-empirical.md):
    - rerolled attribute always differs from the slot's current value; slots rerolled together are independent
    - stat reroll draws uniformly from the color's stats not currently on the banner (no duplicates)
    - trait reroll draws uniformly from the other 4 traits
    - quality redraw uses PRIORS["quality_redraw"], re-drawn until different from current
    - improve buttons never pick T5 slots; deltas from PRIORS["upgrade_delta"], capped at T5
    - improve2down1: two distinct non-T5 slots up, then one slot (any) down by PRIORS["downgrade_delta"], floored at T1
"""

import argparse
import json
import random
import statistics
import sys
from copy import deepcopy

QUALITY_BONUS = {1: 10, 2: 30, 3: 60, 4: 100, 5: 150}
TRAITS = ["fractal", "benevolent", "vampiric", "unique", "friendly"]
STAT_POOL = {
    "red":   ["kills", "deaths", "cs", "gpm", "madstone", "towers"],
    "blue":  ["wards", "camps", "runes", "watchers", "smokes", "lotus"],
    "green": ["roshan", "teamfight", "stuns", "tormentor", "firstblood", "courier"],
}
PRIORS = {
    "quality_redraw": {1: 0.30, 2: 0.28, 3: 0.22, 4: 0.14, 5: 0.06},
    "upgrade_delta":  {1: 0.50, 2: 0.35, 3: 0.15},
    "downgrade_delta": {1: 0.45, 2: 0.30, 3: 0.15, 4: 0.10},
}


# ----------------------------------------------------------------------------- scoring
def trait_net(slots, i):
    """Net trait % received by slot i (own conditional + neighbour effects). Mirrors the client display."""
    s = slots[i]
    net = 0
    t = s["trait"]
    if t == "vampiric":
        net += 50
    elif t == "unique" and sum(1 for x in slots if x["trait"] == "unique") == 1:
        net += 30
    elif t == "friendly" and sum(1 for x in slots if x["trait"] == "friendly") >= 3:
        net += 50
    elif t == "fractal" and len({x["tier"] for x in slots}) == len(slots):
        net += 60
    for j in (i - 1, i + 1):
        if 0 <= j < len(slots):
            nt = slots[j]["trait"]
            if nt == "benevolent":
                net += 20
            elif nt == "vampiric":
                net -= 10
    return net


def slot_points(slots, i, bases):
    s = slots[i]
    mult = 100 + QUALITY_BONUS[s["tier"]] + trait_net(slots, i)
    return bases.get(s["stat"], 0.0) * mult / 100.0


def banner_points(slots, bases):
    return sum(slot_points(slots, i, bases) for i in range(len(slots)))


# ----------------------------------------------------------------------------- sampling helpers
def draw(dist, rng):
    r, acc = rng.random(), 0.0
    for k, p in dist.items():
        acc += p
        if r <= acc:
            return k
    return list(dist)[-1]


def pick_scope(slots, color, scope, rng):
    idx = [i for i, s in enumerate(slots) if color == "any" or s["color"] == color]
    if not idx:
        return []
    if scope == "all":
        return idx
    if scope == "first":
        return [idx[0]]
    if scope == "last":
        return [idx[-1]]
    if scope == "random":
        return [rng.choice(idx)]
    raise ValueError(scope)


# ----------------------------------------------------------------------------- one sampled press
def apply_button(slots, spec, rng):
    slots = deepcopy(slots)
    parts = spec.lower().split()
    action = parts[0]

    if action == "refresh":
        return slots

    if action == "improve1":
        cands = [i for i, s in enumerate(slots) if s["tier"] < 5]
        if cands:
            i = rng.choice(cands)
            slots[i]["tier"] = min(5, slots[i]["tier"] + draw(PRIORS["upgrade_delta"], rng))
        return slots

    if action == "improve2down1":
        cands = [i for i, s in enumerate(slots) if s["tier"] < 5]
        ups = rng.sample(cands, min(2, len(cands)))
        for i in ups:
            slots[i]["tier"] = min(5, slots[i]["tier"] + draw(PRIORS["upgrade_delta"], rng))
        j = rng.randrange(len(slots))
        slots[j]["tier"] = max(1, slots[j]["tier"] - draw(PRIORS["downgrade_delta"], rng))
        return slots

    if action != "reroll":
        raise ValueError(f"unknown action {action}")

    target, color = parts[1], parts[2]
    scope = parts[3] if len(parts) > 3 else "all"
    targets = pick_scope(slots, color, scope, rng)
    if not targets:
        return slots

    if target == "stat":
        on_banner = {s["stat"] for s in slots}
        for i in targets:
            pool = [x for x in STAT_POOL[slots[i]["color"]] if x not in on_banner]
            if not pool:
                continue
            new = rng.choice(pool)
            on_banner.discard(slots[i]["stat"])
            on_banner.add(new)
            slots[i]["stat"] = new
    elif target == "trait":
        for i in targets:
            slots[i]["trait"] = rng.choice([t for t in TRAITS if t != slots[i]["trait"]])
    elif target == "quality":
        for i in targets:
            while True:
                q = draw(PRIORS["quality_redraw"], rng)
                if q != slots[i]["tier"]:
                    break
            slots[i]["tier"] = q
    else:
        raise ValueError(target)
    return slots


# ----------------------------------------------------------------------------- evaluation
def evaluate(slots, bases, spec, samples, seed=1):
    rng = random.Random(seed)
    before = banner_points(slots, bases)
    deltas = [banner_points(apply_button(slots, spec, rng), bases) - before for _ in range(samples)]
    deltas.sort()
    n = len(deltas)
    return {
        "before": before,
        "mean": statistics.fmean(deltas),
        "p10": deltas[int(0.10 * n)],
        "p50": deltas[n // 2],
        "p90": deltas[int(0.90 * n)],
        "min": deltas[0],
        "max": deltas[-1],
        "p_gain": sum(1 for d in deltas if d > 0) / n,
        "p_loss": sum(1 for d in deltas if d < 0) / n,
    }


def verdict(r):
    if r["mean"] > 500 and r["p_loss"] < 0.5:
        return "✓"
    if r["mean"] >= -100:
        return "△"
    return "✗"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("state")
    ap.add_argument("--button", action="append", help="button spec; repeatable. Defaults to state['options'].")
    ap.add_argument("--banner", choices=["core", "mid", "support"], help="restrict to one banner")
    ap.add_argument("--samples", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    state = json.load(open(args.state))
    buttons = args.button or state.get("options", [])
    if not buttons:
        sys.exit("no buttons: pass --button or fill state['options']")
    roles = [args.banner] if args.banner else ["core", "mid", "support"]

    print(f"{'button':32} {'banner':8} {'V':2} {'mean':>8} {'p10':>8} {'p50':>8} {'p90':>8} {'min':>8} {'max':>8} {'P(+)':>6}")
    for spec in buttons:
        for role in roles:
            b = state["banners"][role]
            bases = state.get("bases", {}).get(role, {})
            r = evaluate(b["slots"], bases, spec, args.samples, args.seed)
            print(f"{spec:32} {role:8} {verdict(r):2} {r['mean']:8.0f} {r['p10']:8.0f} {r['p50']:8.0f} "
                  f"{r['p90']:8.0f} {r['min']:8.0f} {r['max']:8.0f} {r['p_gain']:6.2f}")
    print("\nV: ✓ = clearly positive  △ = ≈0 / variance play  ✗ = negative.  Deltas are banner points (two-game sums).")


if __name__ == "__main__":
    main()
