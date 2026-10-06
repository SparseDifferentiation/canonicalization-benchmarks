"""
Statistics and summary tables for the final-deposit experiments (jury J1a).

Reads the JSON files written by thesis_final_benchmarks.py (any number, from both
interpreters) and writes a Markdown summary plus CSV files next to --out:

  * per problem and target: n, mean, std, median of the replicates
  * cold canonicalization: diffengine against each CVXPY backend and against the
    best of them, two-sided Mann-Whitney U per problem, Holm-corrected across
    problems; suite level, a Wilcoxon signed-rank test on the per-problem log
    ratios of medians and a bootstrap 95% CI of the geometric-mean ratio
  * the ablation contrasts (dense blocks off, split off, both), same tests
  * the phase breakdown of the engine
  * the non-DPP table and the sensitivity / scaling sweeps

Usage:
    python thesis_stats.py results/thesis/*.json --out results/thesis/summary.md
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

import thesis_extra_problems as extra

BASELINES_COLD = ["CPP_ND", "SCIPY_ND", "COO_ND"]
ENGINE_COLD = "DIFFENGINE"
PHASES = ["convert", "symbolic", "numeric", "assemble", "format"]
RNG = np.random.default_rng(12345)
NONDPP = set(extra.SETS["nondpp"])
SWEEP = set(extra.SETS["sensitivity"]) | set(extra.SETS["scaling"])


def is_suite(name):
    """The 25 cvxpy/benchmarks classes; extra specs all contain a colon."""
    return ":" not in name


def load(paths):
    """{(kind, class): {"samples": {target: [sample]}, "dims":..., "is_dpp":...}}"""
    rows, envs = {}, []
    for p in paths:
        d = json.loads(Path(p).read_text())
        if "rows" not in d or "kind" not in d.get("meta", {}):
            continue
        kind = d["meta"]["kind"]
        envs.append((p, d["meta"].get("environment", {})))
        for r in d["rows"]:
            if "samples" not in r:
                continue
            key = (kind, r["class"])
            agg = rows.setdefault(key, {"samples": {}, "status": {}})
            for k in ("dims", "is_dpp"):
                if k in r and k not in agg:
                    agg[k] = r[k]
            for t, v in r["samples"].items():
                if v:
                    agg["samples"][t] = v
            agg["status"].update(r.get("status", {}))
    return rows, envs


def times(row, target):
    return np.array([s["time"] for s in row["samples"].get(target, [])], dtype=float)


def holm(pvals):
    """Holm-Bonferroni adjusted p-values (same order as the input)."""
    p = np.asarray(pvals, dtype=float)
    order = np.argsort(p)
    adj = np.empty_like(p)
    running = 0.0
    m = len(p)
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (m - rank) * p[i]))
        adj[i] = running
    return adj


def mwu(a, b):
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    return float(stats.mannwhitneyu(a, b, alternative="two-sided").pvalue)


def geomean_ci(ratios, n_boot=10000):
    lr = np.log(np.asarray(ratios, dtype=float))
    g = float(np.exp(lr.mean()))
    if len(lr) < 2:
        return g, float("nan"), float("nan")
    boot = RNG.choice(lr, size=(n_boot, len(lr)), replace=True).mean(axis=1)
    lo, hi = np.exp(np.percentile(boot, [2.5, 97.5]))
    return g, float(lo), float(hi)


def wilcoxon_logratio(ratios):
    lr = np.log(np.asarray(ratios, dtype=float))
    if len(lr) < 6 or np.allclose(lr, 0):
        return float("nan")
    return float(stats.wilcoxon(lr).pvalue)


def fmt(x, d=3):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    if isinstance(x, float) and (abs(x) < 10 ** -d and x != 0):
        return f"{x:.1e}"
    return f"{x:.{d}f}"


def contrast(rows, kind, num, den, label, md, csv_rows, keep=is_suite):
    """Per-problem num/den ratio of medians, Mann-Whitney + Holm, suite tests."""
    recs = []
    for (k, name), row in sorted(rows.items()):
        if k != kind or not keep(name):
            continue
        a, b = times(row, num), times(row, den)
        if not len(a) or not len(b):
            continue
        recs.append([name, float(np.median(a)), float(np.median(b)),
                     float(np.median(a) / np.median(b)), mwu(a, b), len(a), len(b)])
    if not recs:
        return
    adj = holm([r[4] if not math.isnan(r[4]) else 1.0 for r in recs])
    md.append(f"\n### {label}: `{num}` / `{den}` ({kind})\n")
    md.append("| problem | median num (s) | median den (s) | ratio | p (Holm) | n |")
    md.append("|---|---:|---:|---:|---:|---|")
    for r, p in zip(recs, adj):
        md.append(f"| {r[0]} | {fmt(r[1], 4)} | {fmt(r[2], 4)} | {fmt(r[3])} | "
                  f"{fmt(float(p))} | {r[5]}/{r[6]} |")
        csv_rows.append([label, kind, num, den, r[0], r[1], r[2], r[3], r[4], float(p)])
    ratios = [r[3] for r in recs]
    g, lo, hi = geomean_ci(ratios)
    md.append(f"\nGeometric-mean ratio **{fmt(g)}** (bootstrap 95% CI {fmt(lo)}–{fmt(hi)}), "
              f"Wilcoxon signed-rank p = {fmt(wilcoxon_logratio(ratios))}, "
              f"{sum(x < 1 for x in ratios)}/{len(ratios)} problems below 1, "
              f"{sum(p < 0.05 for p in adj)}/{len(ratios)} significant at 5% after Holm.")


def best_baseline(rows, md, csv_rows, keep=is_suite,
                  title="Table 4.1: first canonicalization"):
    """diffengine against the best CVXPY backend of each problem (Table 4.1)."""
    recs = []
    for (k, name), row in sorted(rows.items()):
        if k != "cold" or not keep(name):
            continue
        de = times(row, ENGINE_COLD)
        base = {t: times(row, t) for t in BASELINES_COLD if len(times(row, t))}
        if not len(de) or not base:
            continue
        best = min(base, key=lambda t: np.median(base[t]))
        recs.append([name, row.get("dims", {}), float(de.mean()), float(de.std(ddof=1)),
                     {t: (float(v.mean()), float(v.std(ddof=1)) if len(v) > 1 else 0.0)
                      for t, v in base.items()},
                     best, float(np.median(de) / np.median(base[best])),
                     mwu(de, base[best])])
    if not recs:
        return
    adj = holm([r[7] if not math.isnan(r[7]) else 1.0 for r in recs])
    md.append(f"\n## {title}, mean ± std (s)\n")
    md.append("| problem | n | m | nnz(A) | " + " | ".join(BASELINES_COLD) +
              " | diffengine | best | ratio | p (Holm) |")
    md.append("|---|---:|---:|---:|" + "---:|" * len(BASELINES_COLD) + "---:|---|---:|---:|")
    for r, p in zip(recs, adj):
        dm = r[1]
        cells = [f"{fmt(r[4][t][0])} ± {fmt(r[4][t][1])}" if t in r[4] else "–"
                 for t in BASELINES_COLD]
        md.append(f"| {r[0]} | {dm.get('n', '–')} | {dm.get('m', '–')} | "
                  f"{dm.get('nnz_A', '–')} | " + " | ".join(cells) +
                  f" | {fmt(r[2])} ± {fmt(r[3])} | {r[5]} | {fmt(r[6])} | {fmt(float(p))} |")
        csv_rows.append([title, "cold", ENGINE_COLD, r[5], r[0], r[2], None, r[6], r[7],
                         float(p)])
    ratios = [r[6] for r in recs]
    g, lo, hi = geomean_ci(ratios)
    md.append(f"\ndiffengine fastest on {sum(x < 1 for x in ratios)}/{len(ratios)}; "
              f"geometric-mean ratio to the best backend **{fmt(g)}** "
              f"(95% CI {fmt(lo)}–{fmt(hi)}), Wilcoxon p = {fmt(wilcoxon_logratio(ratios))}; "
              f"{sum((x < 1) and (p < 0.05) for x, p in zip(ratios, adj))} problems "
              f"significantly faster, {sum((x > 1) and (p < 0.05) for x, p in zip(ratios, adj))} "
              f"significantly slower (Holm, 5%).")


def phase_table(rows, kind, target, md):
    md.append(f"\n## Phase breakdown of `{target}` ({kind}), mean share of the time\n")
    md.append("| problem | time (s) | front end | " + " | ".join(PHASES) + " |")
    md.append("|---|---:|---:|" + "---:|" * len(PHASES))
    for (k, name), row in sorted(rows.items()):
        if k != kind or not is_suite(name) or not row["samples"].get(target):
            continue
        shares = defaultdict(list)
        tot = []
        for s in row["samples"][target]:
            phs = s.get("phases")
            if kind == "warm":
                phs_list, ts = phs or [], s.get("iters", [])
            else:
                phs_list, ts = [phs], [s["time"]]
            for ph, t in zip(phs_list, ts):
                if not ph:
                    continue
                tot.append(t)
                for p in PHASES:
                    shares[p].append(ph.get(p, 0.0) / t)
                shares["front"].append(1 - sum(ph.get(p, 0.0) for p in PHASES) / t)
        if not tot:
            continue
        md.append(f"| {name} | {fmt(float(np.mean(tot)), 4)} | "
                  f"{100 * np.mean(shares['front']):.0f}% | " +
                  " | ".join(f"{100 * np.mean(shares[p]):.0f}%" for p in PHASES) + " |")


def sweep_csv(rows, prefix, out):
    """One CSV row per extra spec: its parameters and the median of every target."""
    recs = []
    for (k, name), row in sorted(rows.items()):
        if name not in SWEEP or not name.startswith(prefix):
            continue
        fam, *parts = name.split(":")
        kw = dict(p.split("=", 1) for p in parts)
        rec = {"kind": k, "family": fam, **kw, **{f"dim_{a}": b for a, b in
                                                   row.get("dims", {}).items()}}
        for t, v in row["samples"].items():
            if v:
                rec[t] = float(np.median([s["time"] for s in v]))
        recs.append(rec)
    if not recs:
        return
    keys = sorted({k for r in recs for k in r})
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(recs)


def load_aux(paths):
    """The memory rows {(kind, class): {target: result}} and the verify rows."""
    memory, verify = {}, {}
    for p in paths:
        d = json.loads(Path(p).read_text())
        for r in d.get("rows", []):
            if "targets" in r and "kind" in d.get("meta", {}):
                memory.setdefault((d["meta"]["kind"], r["class"]), {}).update(r["targets"])
            elif "checks" in r or "error" in r:
                verify[r["class"]] = r
    return memory, verify


def gate_table(verify, md):
    """Correctness gate (Legrain vii): every check of every problem."""
    if not verify:
        return set()
    failed = set()
    md.append("\n## Correctness gate: (P, c, A, b) vs the reference (rel. 1e-9)\n")
    md.append("| problem | reference | checks passed | failures |")
    md.append("|---|---|---:|---|")
    for name, r in sorted(verify.items()):
        checks = r.get("checks", {})
        bad = [k for k, v in checks.items() if not (isinstance(v, dict) and v.get("ok"))]
        if "error" in r:
            bad.append(f"worker: {r['error']}")
        for k in bad:
            failed.add((name, k.split(":", 1)[-1]))
        ref = r.get("reference") or "–"
        if ref == "DIFFENGINE":
            ref = "DIFFENGINE (no stock reference: non-DPP)"
        md.append(f"| {name} | {ref} | {len(checks) - len(bad)}/{len(checks)} | "
                  f"{', '.join(bad) or '–'} |")
    md.append(f"\n{len(failed)} failed (problem, target) checks.")
    return failed


def memory_table(memory, md):
    """Peak-RSS delta and the engine's own peak, one measurement per cell."""
    for kind in ("cold", "warm"):
        cells = {name: t for (k, name), t in memory.items() if k == kind}
        if not cells:
            continue
        targets = sorted({t for v in cells.values() for t in v})
        md.append(f"\n## Memory ({kind}): peak-RSS delta (MB) [engine peak MB]\n")
        md.append("| problem | " + " | ".join(targets) + " |")
        md.append("|---|" + "---:|" * len(targets))
        for name, v in sorted(cells.items()):
            out = []
            for t in targets:
                r = v.get(t, {})
                if "delta_mb" in r:
                    c = f"{r['delta_mb']:.1f}" + (" (floor)" if r.get("floor") else "")
                    if r.get("engine_peak_mb") is not None:
                        c += f" [{r['engine_peak_mb']:.1f}]"
                else:
                    c = r.get("skip") or r.get("error") or "–"
                out.append(c)
            md.append(f"| {name} | " + " | ".join(out) + " |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows, envs = load(a.files)
    memory, verify = load_aux(a.files)
    out = Path(a.out)
    md = ["# Final-deposit experiments: summary", "", "## Environments", ""]
    for p, e in envs:
        md.append(f"- `{Path(p).name}`: {e.get('cpu')} / {e.get('platform')} / Python "
                  f"{e.get('python')} / cvxpy {e.get('cvxpy')} ({str(e.get('cvxpy_git'))[:9]}) / "
                  f"sparsediffpy {e.get('sparsediffpy')} (engine {e.get('engine_commit')}) / "
                  f"BLAS {e.get('engine_blas')}")
    csv_rows = []
    failed = gate_table(verify, md)
    # A timing counts only if its problem passed the gate: drop failed engine targets.
    for (k, name), row in rows.items():
        for t in list(row["samples"]):
            if (name, t) in failed:
                row["status"][t] = "failed the correctness gate"
                del row["samples"][t]
    best_baseline(rows, md, csv_rows)
    md.append("\n## Ablation (jury J1b, Legrain ii)")
    contrast(rows, "cold", "DE_NODENSE", "DIFFENGINE", "Dense blocks off", md, csv_rows)
    for b in BASELINES_COLD:
        contrast(rows, "cold", "DE_NODENSE", b, f"Engine without dense blocks vs {b}",
                 md, csv_rows)
    contrast(rows, "warm", "de_cached_nodense", "de_cached", "Dense blocks off", md, csv_rows)
    contrast(rows, "warm", "de_cached_rebuild", "de_cached", "Split off", md, csv_rows)
    contrast(rows, "warm", "de_cached_nodense_rebuild", "de_cached", "Both off", md,
             csv_rows)
    md.append("\n## Re-solves")
    for b in ("dpp", "dpp_coo", "dpp_scipy", "nodpp_cpp"):
        contrast(rows, "warm", "de_cached", b, f"Engine re-solve vs {b}", md, csv_rows)
    md.append("\n## Non-DPP re-solves and first compiles (jury J1e, Legrain iii)")
    nd = NONDPP.__contains__
    for b in ("nodpp_cpp", "nodpp_coo", "dpp", "de_cached_rebuild"):
        contrast(rows, "warm", "de_cached", b, f"Engine re-solve vs {b}", md, csv_rows,
                 keep=nd)
    best_baseline(rows, md, csv_rows, keep=nd, title="Non-DPP set: first canonicalization")
    phase_table(rows, "cold", ENGINE_COLD, md)
    phase_table(rows, "warm", "de_cached", md)
    memory_table(memory, md)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(md) + "\n")
    with open(out.with_suffix(".contrasts.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["contrast", "kind", "num", "den", "problem", "median_num", "median_den",
                    "ratio", "p_raw", "p_holm"])
        w.writerows(csv_rows)
    for prefix in ("lasso", "factor_cov", "huber", "advertising"):
        sweep_csv(rows, prefix, out.with_name(f"{out.stem}.{prefix}.csv"))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
