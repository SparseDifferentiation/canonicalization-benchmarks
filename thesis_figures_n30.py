"""Figures and facts of Chapter 4 from the 30-run sweep (run_n30.sh).

Reads results/thesis-n30 (cold suite at s = 1, the size grid grid25, the density sweep
density8 and the memory of the ablation) and writes, at the thesis text width:

  forest_thesis.pdf      ratio of diffengine to the best CVXPY backend per problem, median
                         and bootstrap 95% CI of the ratio of medians, with and without the
                         dense blocks; filled = significant (Mann-Whitney, Holm)
  ablation_thesis.pdf    (a) histogram of the per-problem effect of the dense blocks on
                         time, (b) the same for peak memory
  size_thesis.pdf        heatmap of the ratio over 25 problems + lasso x five sizes
  density_thesis.pdf     ratio against the density, with and without the dense blocks

and grid_facts.json with every number the text quotes. With --legacy, the same figures are
drawn from the 20-run / 5-run results (results/thesis, results/thesis-scaling) to test the
script before the sweep finishes.

Usage: uv run --with matplotlib --with numpy --with scipy python thesis_figures_n30.py [--legacy]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import thesis_stats as ts  # noqa: E402

PLOTS = HERE / "results" / "plots"
STOCK = ["CPP_ND", "SCIPY_ND", "COO_ND"]
ENGINES = {"DIFFENGINE": "with dense blocks", "DE_NODENSE": "without dense blocks"}
TEXTWIDTH_IN = 6.53
# Reference-palette roles (dataviz skill), as in plot_thesis_figures.py. Diverging pair:
# blue (diffengine faster) <-> red (slower), gray midpoint.
BLUE, RED, MID = "#2a78d6", "#e34948", "#f0efec"
INK, INK2, MUTED, GRID, AXIS = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
NAME = {"CVaRBenchmark": "CVaR", "ConeMatrixStuffingBench": "ConeMatrixStuffing",
        "ParametrizedQPBenchmark": "ParametrizedQP", "SDPSegfault1132Benchmark": "SDPSegfault1132",
        "SimpleFullyParametrizedLPBenchmark": "SimpleFullyParametrizedLP",
        "SimpleLPBenchmark": "SimpleLP", "SimpleQPBenchmark": "SimpleQP",
        "SimpleScalarParametrizedLPBenchmark": "SimpleScalarParametrizedLP",
        "SlowPruningBenchmark": "SlowPruning"}
SIZES = (0.25, 0.5, 1, 2, 4)
DENS = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1)
BOOT = 2000
RNG = np.random.default_rng(12345)
LASSO = "lasso"


def nm(c):
    return NAME.get(c, c)


def parse(spec):
    """Problem name -> (family, s, density)."""
    if ":" not in spec:
        return spec, 1.0, 1.0
    kv = dict(x.split("=") for x in spec.split(":")[1:])
    if spec.startswith("scaled:"):
        return kv["cls"], float(kv.get("s", 1)), float(kv.get("density", 1))
    if spec.startswith("lasso:") and kv.get("variant") == "free":
        n = int(kv["n"])
        return LASSO, round((n / 1000) ** 2, 2), float(kv.get("density", 1))
    return None, None, None


def cell(row, engine):
    """Ratio of medians engine / best stock backend, its bootstrap CI and the MWU p."""
    if row is None:
        return None
    de = ts.times(row, engine)
    base = {t: ts.times(row, t) for t in STOCK if len(ts.times(row, t))}
    status = row.get("status", {})
    if not len(de):
        st = str(status.get(engine, ""))
        return {"cap": "CAP" in st.upper() or "TIME" in st.upper(), "status": st,
                "all_cap": not base}
    if not base:
        return {"cap": False, "status": "no stock"}
    best = min(base, key=lambda t: np.median(base[t]))
    b = base[best]
    r = float(np.median(de) / np.median(b))
    bd = RNG.choice(de, size=(BOOT, len(de))).copy()
    bb = RNG.choice(b, size=(BOOT, len(b))).copy()
    lo, hi = np.percentile(np.median(bd, 1) / np.median(bb, 1), [2.5, 97.5])
    return {"ratio": r, "lo": float(lo), "hi": float(hi), "p": ts.mwu(de, b), "best": best,
            "n": [len(de), len(b)], "cap": False}


def adjust(cells):
    """Holm over the cells of one comparison (one column), in place."""
    live = [c for c in cells if c and "ratio" in c]
    for c, p in zip(live, ts.holm([c["p"] if not math.isnan(c["p"]) else 1 for c in live])):
        c["p_holm"] = float(p)
        c["sig"] = bool(p < 0.05)


def collect(rows):
    """{(family, s, density): row} over the cold rows."""
    out = {}
    for (kind, name), row in rows.items():
        if kind != "cold":
            continue
        fam, s, d = parse(name)
        if fam:
            out[(fam, s, d)] = row
    return out


def build(rows, memory):
    grid = collect(rows)
    fams = sorted({f for (f, s, d) in grid if f != LASSO and s == 1 and d == 1})
    F = {"suite": {}, "size": {}, "density": {}, "memory": {}}
    # s = 1, both engines; Holm over the 25 problems per engine.
    for e in ENGINES:
        cs = {f: cell(grid.get((f, 1.0, 1.0)), e) for f in fams}
        adjust(list(cs.values()))
        F["suite"][e] = cs
    for e in ENGINES:
        rs = [F["suite"][e][f]["ratio"] for f in fams if "ratio" in (F["suite"][e][f] or {})]
        g, lo, hi = ts.geomean_ci(rs)
        F["suite"][e + "_geomean"] = {"g": g, "lo": lo, "hi": hi,
                                      "wilcoxon": ts.wilcoxon_logratio(rs),
                                      "faster": sum(r < 1 for r in rs), "n": len(rs)}
    # The effect of the dense blocks: nodense / dense, per problem.
    eff = {}
    for f in fams:
        row = grid.get((f, 1.0, 1.0))
        a, b = ts.times(row, "DE_NODENSE"), ts.times(row, "DIFFENGINE")
        if len(a) and len(b):
            eff[f] = {"ratio": float(np.median(a) / np.median(b)), "p": ts.mwu(a, b)}
    adjust(list(eff.values()))
    rs = [v["ratio"] for v in eff.values()]
    g, lo, hi = ts.geomean_ci(rs)
    F["dense_effect"] = {"per": eff, "g": g, "lo": lo, "hi": hi,
                         "wilcoxon": ts.wilcoxon_logratio(rs)}
    for f in fams:
        m = memory.get(("cold", f), {})
        mm = {t: m[t]["delta_mb"] for t in m if m[t].get("delta_mb") is not None}
        if mm:
            F["memory"][f] = mm
    # Size grid: Holm within each s, over the problems measured at that s.
    for s in SIZES:
        cs = {f: cell(grid.get((f, s, 1.0)), "DIFFENGINE") for f in fams + [LASSO]}
        adjust(list(cs.values()))
        F["size"][s] = cs
    # Density: Holm within each density and engine.
    dfams = sorted({f for (f, s, d) in grid if d < 1})
    for d in DENS:
        for e in ENGINES:
            cs = {f: cell(grid.get((f, 1.0, d)), e) for f in dfams}
            adjust(list(cs.values()))
            F["density"].setdefault(e, {})[d] = cs
    F["families"], F["density_families"] = fams, dfams
    return F


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #
def _style(ax, grid_axis="x"):
    ax.set_facecolor("white")
    for side in ax.spines:
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=INK2, labelsize=7.5)
    ax.grid(True, axis=grid_axis, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def _ratio_axis(ax, lo, hi, axis="x", step=1):
    ticks = [2.0 ** k for k in range(-6, 7, step) if lo <= 2.0 ** k <= hi]
    lab = [f"1/{round(1 / t)}" if t < 1 else f"{t:g}" for t in ticks]
    if axis == "x":
        ax.set_xscale("log", base=2)
        ax.set_xlim(lo, hi)
        ax.set_xticks(ticks, lab)
        ax.xaxis.set_minor_locator(__import__("matplotlib").ticker.NullLocator())
        ax.axvline(1, color=INK2, linewidth=0.9, zorder=1)
    else:
        ax.set_yscale("log", base=2)
        ax.set_ylim(lo, hi)
        ax.set_yticks(ticks, lab)
        ax.yaxis.set_minor_locator(__import__("matplotlib").ticker.NullLocator())
        ax.axhline(1, color=INK2, linewidth=0.9, zorder=1)


def fig_forest(plt, F):
    """Figure A: per-problem ratio with CI, with and without the dense blocks."""
    fams = F["families"]
    de = F["suite"]["DIFFENGINE"]
    order = sorted(fams, key=lambda f: de[f]["ratio"] if "ratio" in (de[f] or {}) else 1e9)
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN, 6.2))
    _style(ax)
    y = np.arange(len(order))[::-1]
    for e, color, marker, dy in (("DIFFENGINE", BLUE, "o", 0.17), ("DE_NODENSE", INK2, "D", -0.17)):
        for yi, f in zip(y, order):
            c = F["suite"][e][f]
            if not c or "ratio" not in c:
                continue
            ax.plot([c["lo"], c["hi"]], [yi + dy] * 2, color=color, linewidth=1.2, zorder=2)
            ax.plot(c["ratio"], yi + dy, marker=marker, markersize=5 if marker == "o" else 4.2,
                    color=color, markerfacecolor=color if c.get("sig") else "white",
                    markeredgewidth=1.1, zorder=3, linestyle="none")
    ax.set_yticks(y, [nm(f) for f in order], fontsize=7.5, color=INK)
    ax.set_ylim(-0.7, len(order) - 0.3)
    _ratio_axis(ax, 1 / 16, 32)
    ax.set_xlabel(r"time of $\mathtt{diffengine}$ / time of the best CVXPY backend"
                  "\n(< 1: diffengine faster)", fontsize=8.5, color=INK2)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=BLUE, marker="o", markersize=5, label="with dense blocks"),
         Line2D([], [], color=INK2, marker="D", markersize=4.2, label="without dense blocks"),
         Line2D([], [], color=MUTED, marker="o", markersize=5, markerfacecolor="white",
                linestyle="none", label="not significant")]
    ax.legend(handles=h, loc="upper right", fontsize=7.5, frameon=True, framealpha=1,
              edgecolor=GRID, fancybox=False)
    return fig


def fig_ablation(plt, F):
    """Figure B: distribution over the problems of the effect of the dense blocks."""
    eff = F["dense_effect"]["per"]
    mem = F["memory"]
    fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH_IN, 2.9))
    bins = 2.0 ** np.arange(-6, 6.5, 0.5)
    panels = [
        (axes[0], [v["ratio"] for v in eff.values()], [v.get("sig") for v in eff.values()],
         "(a) time without / with dense blocks", F["dense_effect"]["g"]),
        (axes[1], [m["DE_NODENSE"] / m["DIFFENGINE"] for m in mem.values()
                   if m.get("DIFFENGINE") and m.get("DE_NODENSE")], None,
         "(b) peak memory without / with dense blocks", None),
    ]
    for ax, vals, sig, tag, g in panels:
        _style(ax, "y")
        vals = np.clip(vals, bins[0], bins[-1])
        if sig is None:
            ax.hist(vals, bins=bins, color=BLUE, edgecolor="white", linewidth=1)
        else:
            s = np.array(sig, dtype=bool)
            ax.hist([vals[s], vals[~s]], bins=bins, stacked=True, color=[BLUE, "#a9c8ef"],
                    edgecolor="white", linewidth=1,
                    label=["significant", "not significant"])
            ax.legend(fontsize=7, frameon=False, loc="upper left")
        ax.set_ylim(0, ax.get_ylim()[1] * 1.15)
        if g is None:
            g = float(np.exp(np.mean(np.log(vals))))
        ax.axvline(g, color=INK, linestyle=(0, (3, 2)), linewidth=1)
        ax.text(0.98, 0.97, f"geometric mean {g:.2f}", transform=ax.transAxes, fontsize=7,
                color=INK, va="top", ha="right")
        _ratio_axis(ax, 1 / 64, 64, step=2)
        ax.yaxis.set_major_locator(__import__("matplotlib").ticker.MaxNLocator(integer=True))
        ax.set_xlabel(f"> 1: the dense blocks help\n{tag}", fontsize=8, color=INK2,
                      linespacing=1.6)
        ax.set_ylabel("problems", fontsize=8, color=INK2)
    return fig


def _diverging():
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list("bd", [BLUE, MID, RED])


SLOWER = ("UnconstrainedQP", "ConvexPlasticity", "OptimalAdvertising", "SDPSegfault1132")
SLOWER_COLORS = ("#2a78d6", "#eb6834", "#1baf7a", "#eda100")  # categorical slots 1-4
DENSITY_SHOWN = ("LeastSquares", "SVMWithL1Regularization", "HuberRegression",
                 "SemidefiniteProgramming")


def fig_size(plt, F):
    """Figure C: ratio against the size; the four slower problems highlighted."""
    fams = F["families"] + [LASSO]
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN, 3.4))
    _style(ax, "both")

    def series(f):
        return [(s, F["size"][s][f]["ratio"]) for s in SIZES
                if "ratio" in (F["size"][s].get(f) or {})]

    for f in fams:
        if nm(f) in SLOWER:
            continue
        pts = series(f)
        ax.plot(*zip(*pts), color=MUTED, linewidth=0.9, alpha=0.6, zorder=2)
    for f, color in zip(SLOWER, SLOWER_COLORS):
        pts = series(next(g for g in fams if nm(g) == f))
        ax.plot(*zip(*pts), color=color, linewidth=2, marker="o", markersize=4, zorder=3)
        x, y = pts[-1]
        ax.annotate(f, (x, y), xytext=(6, 0), textcoords="offset points", fontsize=7.5,
                    color=INK, va="center")
    ax.set_xscale("log", base=2)
    ax.set_xticks(SIZES, ["1/4", "1/2", "1", "2", "4"])
    ax.xaxis.set_minor_locator(__import__("matplotlib").ticker.NullLocator())
    ax.set_xlim(0.22, 9)
    _ratio_axis(ax, 1 / 8, 32, axis="y")
    ax.set_xlabel("size factor $s$", fontsize=8.5, color=INK2)
    ax.set_ylabel("diffengine / best CVXPY backend", fontsize=8.5, color=INK2)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([], [], color=MUTED, linewidth=0.9,
                              label="the other 22 problems")],
              loc="upper left", fontsize=7.5, frameon=False)
    return fig


def fig_size_heatmap(plt, F):
    """Former Figure C: ratio over problems x sizes."""
    fams = F["families"] + [LASSO]
    base = F["size"][1]
    order = sorted(fams, key=lambda f: base[f]["ratio"] if "ratio" in (base[f] or {}) else 1e9)
    M = np.full((len(order), len(SIZES)), np.nan)
    fig, ax = plt.subplots(figsize=(TEXTWIDTH_IN, 6.6))
    cmap = _diverging()
    for i, f in enumerate(order):
        for j, s in enumerate(SIZES):
            c = F["size"][s].get(f)
            if c and "ratio" in c:
                M[i, j] = math.log2(c["ratio"])
    im = ax.imshow(M, cmap=cmap, vmin=-4, vmax=4, aspect="auto")
    for i, f in enumerate(order):
        for j, s in enumerate(SIZES):
            c = F["size"][s].get(f)
            if c and "ratio" in c:
                txt = f"{c['ratio']:.2f}" + ("" if c.get("sig") else "°")
                ax.text(j, i, txt, ha="center", va="center", fontsize=7,
                        color="white" if abs(M[i, j]) > 2.6 else INK)
            else:
                lab = ("all cap" if c.get("all_cap") else "cap") if c and c.get("cap") else "n/a"
                ax.add_patch(__import__("matplotlib").patches.Rectangle(
                    (j - 0.5, i - 0.5), 1, 1, facecolor="white", edgecolor=GRID, hatch="////",
                    linewidth=0))
                ax.text(j, i, lab, ha="center", va="center", fontsize=7, color=MUTED)
    ax.set_xticks(range(len(SIZES)), [rf"$s = {'1/4' if s == 0.25 else '1/2' if s == 0.5 else f'{s:g}'}$"
                                       for s in SIZES], fontsize=8)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(order)), [nm(f) for f in order], fontsize=7.5)
    ax.tick_params(length=0)
    for side in ax.spines:
        ax.spines[side].set_visible(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02, ticks=[-4, -2, 0, 2, 4])
    cb.ax.set_yticklabels(["1/16", "1/4", "1", "4", "16"], fontsize=7)
    cb.set_label("diffengine / best CVXPY backend", fontsize=8, color=INK2)
    cb.outline.set_visible(False)
    return fig


def fig_density(plt, F):
    """Figure D: ratio against density, small multiples per problem."""
    fams = [f for f in DENSITY_SHOWN if f in F["density_families"]]
    ncol = 4
    nrow = math.ceil(len(fams) / ncol)
    fig, axes = plt.subplots(nrow, ncol, figsize=(TEXTWIDTH_IN, 1.75 * nrow + 0.6),
                             sharex=True, sharey=True, squeeze=False)
    for k, f in enumerate(fams):
        ax = axes[k // ncol][k % ncol]
        _style(ax, "both")
        ax.axvline(0.05, color=MUTED, linestyle=(0, (1, 1.5)), linewidth=0.8)
        for e, color, marker in (("DIFFENGINE", BLUE, "o"), ("DE_NODENSE", INK2, "D")):
            pts = [(d, F["density"][e][d].get(f)) for d in DENS]
            pts = [(d, c) for d, c in pts if c and "ratio" in c]
            if not pts:
                continue
            xs, cs = zip(*pts)
            ax.plot(xs, [c["ratio"] for c in cs], color=color, linewidth=1.3, zorder=2)
            for x, c in pts:
                ax.plot(x, c["ratio"], marker=marker, markersize=4 if marker == "o" else 3.4,
                        color=color, markerfacecolor=color if c.get("sig") else "white",
                        markeredgewidth=1, zorder=3)
        ax.set_xscale("log")
        ax.set_xticks([0.01, 0.1, 1], ["1%", "10%", "100%"])
        _ratio_axis(ax, 1 / 8, 4, axis="y")
        ax.set_title(nm(f), fontsize=7, color=INK, pad=3)
    for k in range(len(fams), nrow * ncol):
        axes[k // ncol][k % ncol].axis("off")
    fig.supxlabel(r"density $\rho$ of the data matrix (dotted: the 5% sparse threshold)",
                  fontsize=8, color=INK2)
    fig.supylabel("diffengine / best CVXPY backend", fontsize=8, color=INK2)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=BLUE, marker="o", markersize=4, label="with dense blocks"),
         Line2D([], [], color=INK2, marker="D", markersize=3.4, label="without dense blocks")]
    fig.legend(handles=h, loc="upper center", ncol=2, fontsize=7.5, frameon=False,
               bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0.02, 0.0, 1, 0.93))
    return fig


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", default="results/thesis-n30")
    ap.add_argument("--legacy", action="store_true")
    args = ap.parse_args()
    if args.legacy:
        files = ([str(p) for p in Path("results/thesis").glob("cold_*.json")]
                 + [str(p) for p in Path("results/thesis-scaling").glob("*_f*.json")]
                 + [str(p) for p in Path("results/thesis-scaling").glob("*_upstream.json")]
                 + [str(p) for p in Path("results/thesis").glob("memory_cold_*.json")])
        suffix = "_legacy"
    else:
        files = [str(p) for p in Path(args.dir).glob("*.json")]
        suffix = ""
    rows, _ = ts.load(files)
    memory, _ = ts.load_aux(files)
    F = build(rows, memory)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "text.color": INK,
                         "axes.labelcolor": INK2, "figure.facecolor": "white",
                         "savefig.facecolor": "white"})
    PLOTS.mkdir(parents=True, exist_ok=True)
    for stem, fn in (("size", fig_size), ("density", fig_density)):
        fig = fn(plt, F)
        if stem != "density":
            fig.tight_layout()
        fig.savefig(PLOTS / f"{stem}{suffix}_thesis.pdf")
        fig.savefig(PLOTS / f"{stem}{suffix}_thesis.png", dpi=200)
        plt.close(fig)
    out = Path(args.dir if not args.legacy else "results/thesis-final") / f"grid_facts{suffix}.json"
    out.write_text(json.dumps(F, indent=1, default=str))
    print(f"figures -> {PLOTS}, facts -> {out}")


if __name__ == "__main__":
    main()
