"""
Old fork build vs new fork build, per (problem, target), for a partial rerun.

Reads the time JSONs of two results directories (e.g. results/thesis and
results/thesis-pr3524), pairs every (kind, problem, target) timed in both, and writes
the medians, the new/old ratio and a two-sided Mann-Whitney p, Holm-corrected within
each (kind, target).

Usage:
    python compare_builds.py --old results/thesis --new results/thesis-pr3524 --out F
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

import thesis_stats as T


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    old, old_env = T.load(sorted(Path(a.old).glob("*.json")))
    new, new_env = T.load(sorted(Path(a.new).glob("*.json")))

    def build(envs):
        e = next((e for p, e in envs if e.get("engine_commit")), {})
        return f"cvxpy {e.get('cvxpy')} ({str(e.get('cvxpy_git'))[:9]}), engine {e.get('engine_commit')}"

    md = ["# Old build vs new build", "",
          f"- old: `{a.old}`: {build(old_env)}",
          f"- new: `{a.new}`: {build(new_env)}", ""]
    groups = {}
    for (kind, name), row in sorted(new.items()):
        for t in row["samples"]:
            b = T.times(old.get((kind, name), {"samples": {}}), t)
            n = T.times(row, t)
            if len(b) and len(n):
                groups.setdefault((kind, t), []).append(
                    [name, float(np.median(b)), float(np.median(n)),
                     float(np.median(n) / np.median(b)), T.mwu(n, b)])
    for (kind, t), recs in sorted(groups.items()):
        adj = T.holm([r[4] if not math.isnan(r[4]) else 1.0 for r in recs])
        md.append(f"\n## `{t}` ({kind})\n")
        md.append("| problem | old median (s) | new median (s) | new/old | p (Holm) |")
        md.append("|---|---:|---:|---:|---:|")
        for r, p in zip(recs, adj):
            md.append(f"| {r[0]} | {T.fmt(r[1], 4)} | {T.fmt(r[2], 4)} | {T.fmt(r[3])} | "
                      f"{T.fmt(float(p))} |")
        g, lo, hi = T.geomean_ci([r[3] for r in recs])
        md.append(f"\nGeometric mean new/old **{T.fmt(g)}** (95% CI {T.fmt(lo)}–{T.fmt(hi)}).")
    Path(a.out).write_text("\n".join(md) + "\n")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
