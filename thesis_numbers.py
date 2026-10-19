"""Every number of Chapter 4 and its appendices, from the final result files.

Combines results/thesis (first M2 sweep), results/thesis-pr3524 (the rerun on fork + #3524,
whose rows replace the first sweep's) and results/thesis-reassoc (the #3524 rewrite applied
to the stock backends). Writes facts.json, profile_data.json (Figure 4.1) and the LaTeX rows of
the tables to results/thesis-final/; thesis_tex.py writes the remaining rows.

Baseline (THESIS_BASELINE):
  no-rewrite (default, the thesis): no backend uses #3524. On the five problems where it
      fires, the diffengine rows (time, memory, verify) come from the first sweep, which ran
      fork 35e81b1 = 5c07151 minus #3524 on the same engine 4f42e05; CVXPY is 1.9.2 as released.
  best-of-both: each CVXPY backend gets the faster of its times with and without #3524, and
      diffengine always has it (the earlier draft).

Usage: .venv-thesis-pr3524/bin/python thesis_numbers.py
"""
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, ".")
import thesis_stats as ts  # noqa: E402

OUT = Path(__file__).parent / "results" / "thesis-final"
OUT.mkdir(exist_ok=True)
T, P, R = "results/thesis", "results/thesis-pr3524", "results/thesis-reassoc"
G = lambda d, pat: sorted(str(p) for p in Path(d).glob(pat))  # noqa: E731
FILES = (G(T, "verify_*.json") + G(T, "cold_*.json") + G(T, "warm_*.json") +
         G(T, "nondpp_*.json") + G(T, "memory_*.json") +
         G(P, "verify_*.json") + G(P, "cold_*.json") + G(P, "warm_*.json") +
         G(P, "memory_*.json") + G(R, "*.json"))
rows, envs = ts.load(FILES)
memory, verify = ts.load_aux(FILES)
BASELINE = os.environ.get("THESIS_BASELINE", "no-rewrite")
assert BASELINE in ("no-rewrite", "best-of-both"), BASELINE
# The five problems where #3524 rewrites a chain (CHANGES.md, C9).
REWRITTEN = ["UnconstrainedQP", "QuantumHilbertMatrix", "SlowPruningBenchmark",
             "SDPSegfault1132Benchmark", "OptimalAdvertising"]
if BASELINE == "no-rewrite":
    TF = G(T, "verify_*.json") + G(T, "cold_*.json") + G(T, "memory_*.json")
    rowsT, _ = ts.load(TF)
    memT, verT = ts.load_aux(TF)
    for n in REWRITTEN:
        rows[("cold", n)] = rowsT[("cold", n)]
        memory[("cold", n)] = memT[("cold", n)]
        verify[n] = verT[n]

# Thesis order and names (Table 4.1 order is by ratio, decided below).
NAME = {"CVaRBenchmark": "CVaR", "ConeMatrixStuffingBench": "ConeMatrixStuffing",
        "ParametrizedQPBenchmark": "ParametrizedQP", "SDPSegfault1132Benchmark": "SDPSegfault1132",
        "SimpleFullyParametrizedLPBenchmark": "SimpleFullyParametrizedLP",
        "SimpleLPBenchmark": "SimpleLP", "SimpleQPBenchmark": "SimpleQP",
        "SimpleScalarParametrizedLPBenchmark": "SimpleScalarParametrizedLP",
        "SlowPruningBenchmark": "SlowPruning"}
nm = lambda c: NAME.get(c, c)  # noqa: E731
SUITE = sorted(n for (k, n) in rows if k == "cold" and ts.is_suite(n))
assert len(SUITE) == 25, SUITE
STOCK = ["CPP_ND", "SCIPY_ND", "COO_ND"]
RA = {b: b + "_RA" for b in STOCK}
t = lambda kind, name, tgt: ts.times(rows.get((kind, name), {"samples": {}}), tgt)  # noqa: E731
med = lambda a: float(np.median(a))  # noqa: E731
F = {}


def ms(a, scale=1.0):
    return float(np.mean(a)) * scale, (float(np.std(a, ddof=1)) * scale if len(a) > 1 else 0.0)


# ---- Table 4.1: stock backends, or best of stock / with the rewrite per backend ----------
recs = []
for n in SUITE:
    de = t("cold", n, "DIFFENGINE")
    back = {}
    for b in STOCK:
        cands = [b] if BASELINE == "no-rewrite" else [x for x in (b, RA[b]) if len(t("cold", n, x))]
        best = min(cands, key=lambda x: med(t("cold", n, x)))
        back[b] = (best, t("cold", n, best))
    bb = min(back, key=lambda b: med(back[b][1]))
    recs.append(dict(name=n, de=de, back=back, best=bb, ratio=med(de) / med(back[bb][1]),
                     p=ts.mwu(de, back[bb][1]),
                     cpp_ratio=med(de) / med(back["CPP_ND"][1]),
                     nodense=t("cold", n, "DE_NODENSE")))
adj = ts.holm([r["p"] for r in recs])
for r, p in zip(recs, adj):
    r["p_holm"] = float(p)
ratios = [r["ratio"] for r in recs]
g, lo, hi = ts.geomean_ci(ratios)
F["t41"] = dict(geomean=g, lo=lo, hi=hi, wilcoxon=ts.wilcoxon_logratio(ratios),
                fastest=sum(x < 1 for x in ratios),
                sig_faster=sum(x < 1 and r["p_holm"] < .05 for x, r in zip(ratios, recs)),
                sig_slower=sum(x > 1 and r["p_holm"] < .05 for x, r in zip(ratios, recs)),
                twice=sum(x < .5 for x in ratios),
                beats_cpp=sum(r["cpp_ratio"] < 1 for r in recs),
                ra_used=sorted(nm(r["name"]) + ":" + b for r in recs
                               for b, (x, _) in r["back"].items() if x.endswith("_RA")),
                slower=[(nm(r["name"]), round(r["ratio"], 3), r["best"], r["p_holm"])
                        for r in recs if r["ratio"] >= 1])
recs.sort(key=lambda r: r["ratio"])
ORDER = [r["name"] for r in recs]
F["order"] = [nm(n) for n in ORDER]


def cell(m, s, scale=1e3):
    """mean +- std in milliseconds, both to the decimals the mean warrants (none from 100 ms,
    one from 10, two from 1, three below); a std that would round to zero gets one
    significant digit."""
    m, s = m * scale, s * scale
    d = 0 if m >= 100 else 1 if m >= 10 else 2 if m >= 1 else 3
    mf = f"{m:,.{d}f}".replace(",", "\\,")
    sf = f"{s:.{d}f}"
    if float(sf) == 0 and s > 0:
        e = -int(math.floor(math.log10(s)))
        sf = f"{round(s, e):.{e}f}"
    return f"{mf} $\\pm$ {sf}"


lines = []
for r in recs:
    medians = {b: med(v) for b, (_, v) in r["back"].items()}
    medians["DE"] = med(r["de"])
    fastest = min(medians, key=medians.get)
    cells = []
    for b in STOCK:
        x, v = r["back"][b]
        c = cell(*ms(v)) + ("$^{\\dagger}$" if x.endswith("_RA") else "")
        cells.append(f"\\textbf{{{c}}}" if fastest == b else c)
    c = cell(*ms(r["de"]))
    cells.append(f"\\textbf{{{c}}}" if fastest == "DE" else c)
    star = "$^{*}$" if r["p_holm"] < .05 else ""
    lines.append(f"{nm(r['name']):<27} & " + " & ".join(cells) +
                 f" & {r['ratio']:.2f}{star} \\\\")
(OUT / "t41.tex").write_text("\n".join(lines) + "\n")

# Appendix cold table: stock columns (no rewrite), the rewrite noted separately.
lines = []
for r in recs:
    n = r["name"]
    cells = [cell(*ms(t("cold", n, b))) for b in STOCK]
    cells += [cell(*ms(r["de"])), cell(*ms(r["nodense"]))]
    mant, ex = f"{r['p_holm']:.1e}".split("e")
    lines.append(f"{nm(n)} & " + " & ".join(cells) +
                 f" & ${mant} \\times 10^{{{int(ex)}}}$ \\\\")
(OUT / "app_cold.tex").write_text("\n".join(lines) + "\n")
lines = []
for n in ORDER:
    if not len(t("cold", n, "CPP_ND_RA")):
        continue
    lines.append(f"{nm(n)} & " + " & ".join(cell(*ms(t("cold", n, RA[b]))) for b in STOCK) +
                 " \\\\")
(OUT / "app_ra.tex").write_text("\n".join(lines) + "\n")

# Appendix table without the dense blocks: with, without, ratio (Holm over the 25 problems),
# then the ratio to the best CVXPY backend with and without them.
nd_adj = dict(zip(SUITE, ts.holm([ts.mwu(t("cold", n, "DE_NODENSE"), t("cold", n, "DIFFENGINE"))
                                  for n in SUITE])))
by_name = {r["name"]: r for r in recs}
lines = []
for n in ORDER:
    a_, b_ = t("cold", n, "DE_NODENSE"), t("cold", n, "DIFFENGINE")
    r = by_name[n]
    best = med(r["back"][r["best"]][1])
    star = "$^{*}$" if nd_adj[n] < .05 else ""
    lines.append(f"{nm(n)} & {cell(*ms(b_))} & {cell(*ms(a_))} & {med(a_) / med(b_):.2f}{star}"
                 f" & {med(b_) / best:.2f} & {med(a_) / best:.2f} \\\\")
(OUT / "app_nodense.tex").write_text("\n".join(lines) + "\n")

# ---- Phases --------------------------------------------------------------------------------
PH = ["front", "convert", "symbolic", "numeric", "assemble", "format"]
phase = {}
for n in SUITE:
    ss = rows[("cold", n)]["samples"]["DIFFENGINE"]
    shares = []
    for s in ss:
        ph = s["phases"]
        front = s["time"] - sum(ph[k] for k in ts.PHASES)
        shares.append([front / s["time"]] + [ph[k] / s["time"] for k in ts.PHASES])
    phase[nm(n)] = dict(time=float(np.mean([s["time"] for s in ss])),
                        share=list(np.mean(shares, axis=0) * 100))
F["phase"] = phase
F["phase_median"] = list(np.median([v["share"] for v in phase.values()], axis=0))

# ---- Parametric (Table 4.2) ------------------------------------------------------------
DPP7 = [n for n in SUITE if len(t("warm", n, "dpp_coo"))]
assert len(DPP7) == 7, DPP7
TENSOR = ["dpp", "dpp_scipy", "dpp_coo"]
par = []
for n in DPP7:
    row = rows[("warm", n)]
    first = {}
    for b, x in zip(STOCK, TENSOR):
        ss = row["samples"].get(x, [])
        first[b] = float(np.mean([s["first"] for s in ss])) if ss else None
    tens = {x: t("warm", n, x) for x in TENSOR if len(t("warm", n, x))}
    tb = min(tens, key=lambda x: med(tens[x]))
    de = t("warm", n, "de_cached")
    par.append(dict(name=nm(n), first=first, de_first=ms(t("cold", n, "DIFFENGINE"))[0],
                    tensor_by=tb, tensor=ms(tens[tb], 1e3), de=ms(de, 1e3),
                    ratio=med(de) / med(tens[tb]), p=ts.mwu(de, tens[tb]),
                    status={x: row["status"].get(x) for x in TENSOR if x not in tens},
                    nodense=ms(t("warm", n, "de_cached_nodense"), 1e3),
                    rebuild=ms(t("warm", n, "de_cached_rebuild"), 1e3),
                    neither=ms(t("warm", n, "de_cached_nodense_rebuild"), 1e3),
                    recompile=min((ms(t("warm", n, x), 1e3) for x in
                                   ("nodpp_cpp", "nodpp_scipy", "nodpp_coo")
                                   if len(t("warm", n, x))), key=lambda v: v[0])))
padj = ts.holm([p["p"] for p in par])
for p, a in zip(par, padj):
    p["p_holm"] = float(a)
par.sort(key=lambda p: p["ratio"])
F["param"] = par
lines = []
for p in par:
    fs = [p["first"][b] for b in STOCK] + [p["de_first"]]
    fmin = min(x for x in fs if x is not None)
    cells = []
    for x in fs:
        c = "---" if x is None else f"{x:.2f}" if x >= 0.1 else f"{x:.3f}"
        cells.append(f"\\textbf{{{c}}}" if x == fmin else c)
    tm, dm = p["tensor"][0], p["de"][0]
    fr = lambda v: f"{v:.0f}" if v >= 10 else f"{v:.1f}"  # noqa: E731
    tc, dc = fr(tm), fr(dm)
    if dm < tm:
        dc = f"\\textbf{{{dc}}}"
    else:
        tc = f"\\textbf{{{tc}}}"
    star = "$^{*}$" if p["p_holm"] < .05 else ""
    lines.append(f"{p['name']:<27} & " + " & ".join(cells) +
                 f" & {tc} & {dc} & {p['ratio']:.2f}{star} \\\\")
(OUT / "t42.tex").write_text("\n".join(lines) + "\n")
lines = []
for p in par:
    lines.append(f"{p['name']} & " + " & ".join(
        cell(*p[k], scale=1) for k in ("tensor", "recompile", "de", "nodense", "rebuild",
                                       "neither")) +
        " \\\\")
(OUT / "app_warm.tex").write_text("\n".join(lines) + "\n")

# ---- Non-DPP (Table 4.4) -----------------------------------------------------------------
nd = {}
for fam, size in (("lasso", 1000), ("factor_cov", 5000)):
    for v in ("dpp", "nondpp", "free"):
        n = f"{fam}:variant={v}:n={size}:seed=0"
        cold = {b: t("cold", n, b) for b in STOCK}
        bc = min(cold, key=lambda b: med(cold[b]))
        if v == "dpp":
            cv = t("warm", n, "dpp")
            cv_by = "tensor"
        elif v == "nondpp":
            w = {x: t("warm", n, x) for x in ("nodpp_cpp", "nodpp_coo")}
            cv_by = min(w, key=lambda x: med(w[x]))
            cv = w[cv_by]
        else:
            cv, cv_by = cold[bc], bc
        cached = t("warm", n, "de_cached") if v != "free" else None
        rebuild = t("warm", n, "de_cached_rebuild") if v != "free" else t("cold", n, "DIFFENGINE")
        de = cached if cached is not None else rebuild
        nd[f"{fam}:{v}"] = dict(cvxpy=med(cv) * 1e3, cvxpy_mean=float(np.mean(cv)) * 1e3,
                                cvxpy_by=cv_by,
                                cached=None if cached is None else float(np.mean(cached)) * 1e3,
                                cached_med=None if cached is None else med(cached) * 1e3,
                                rebuild=float(np.mean(rebuild)) * 1e3,
                                rebuild_med=med(rebuild) * 1e3,
                                ratio=med(de) / med(cv), p=ts.mwu(de, cv))
F["nondpp"] = nd

# ---- Ablation (Table 4.5) ------------------------------------------------------------------
def suite_contrast(pairs):
    recs = [(n, a, b) for n, a, b in pairs if len(a) and len(b)]
    rr = [med(a) / med(b) for _, a, b in recs]
    pa = ts.holm([ts.mwu(a, b) for _, a, b in recs])
    g, lo, hi = ts.geomean_ci(rr)
    return dict(g=g, lo=lo, hi=hi, p=ts.wilcoxon_logratio(rr), sig=int(sum(pa < .05)),
                n=len(rr), below=sum(x < 1 for x in rr),
                per={nm(n): x for (n, _, _), x in zip(recs, rr)})


def parametric(n):
    return len(t("warm", n, "de_cached")) > 0


abl = {}
abl["nodense_cold"] = suite_contrast([(n, t("cold", n, "DE_NODENSE"),
                                       t("cold", n, "DIFFENGINE")) for n in SUITE])
abl["fullycsr_cold"] = suite_contrast(
    [(n, t("cold", n, "DE_NODENSE_EVAL"), t("cold", n, "DE_EVAL")) if parametric(n)
     else (n, t("cold", n, "DE_NODENSE"), t("cold", n, "DIFFENGINE")) for n in SUITE])
best_back = {r["name"]: r["back"][r["best"]][1] for r in recs}
abl["nodense_vs_best"] = suite_contrast([(n, t("cold", n, "DE_NODENSE"), best_back[n])
                                         for n in SUITE])
for v, k in (("de_cached_nodense", "nodense_warm"), ("de_cached_rebuild", "rebuild_warm"),
             ("de_cached_nodense_rebuild", "neither_warm")):
    abl[k] = suite_contrast([(n, t("warm", n, v), t("warm", n, "de_cached")) for n in DPP7])
F["ablation"] = abl

# ---- Memory --------------------------------------------------------------------------------
mem = {}
for (kind, n), d in memory.items():
    if kind == "cold" and ts.is_suite(n):
        mem[nm(n)] = {k: v.get("delta_mb") for k, v in d.items()}
F["memory"] = mem
memt = [m for m in mem.values() if all(m.get(k) for k in STOCK + ["DIFFENGINE"])]
F["mem_summary"] = dict(
    n=len(memt),
    scipy_lowest=sum(min(STOCK + ["DIFFENGINE"], key=lambda k: m[k]) == "SCIPY_ND" for m in memt),
    lowest={k: sum(min(STOCK + ["DIFFENGINE"], key=lambda q: m[q]) == k for m in memt)
            for k in STOCK + ["DIFFENGINE"]},
    de_over={b: float(np.exp(np.mean([math.log(m["DIFFENGINE"] / m[b]) for m in memt])))
             for b in STOCK},
    nodense_over_de=float(np.exp(np.mean([math.log(m["DE_NODENSE"] / m["DIFFENGINE"])
                                         for m in mem.values()
                                         if m.get("DE_NODENSE") and m.get("DIFFENGINE")]))))

# ---- Correctness ---------------------------------------------------------------------------
ver = {}
for n, r in verify.items():
    d = r.get("checks", {})
    ok = lambda c: isinstance(c, dict) and (c["ok"] or (  # noqa: E731
        c.get("nan_mismatch") and all(e == 0 for e in c["max_abs_err"].values())))
    first = [c for k, c in d.items() if k.startswith("first:")]
    upd = [c for k, c in d.items() if not k.startswith("first:")]
    ver[nm(n)] = dict(first=all(map(ok, first)) if first else None,
                      update=all(map(ok, upd)) if upd else None,
                      n=len(d), passed=sum(map(ok, d.values())), reference=r.get("reference"),
                      nan=any(isinstance(c, dict) and c.get("nan_mismatch") for c in d.values()),
                      maxabs=max((max(c["max_abs_err"].values()) if c.get("max_abs_err") else 0)
                                 for c in d.values() if isinstance(c, dict)))
F["verify"] = ver

F["baseline"] = BASELINE
json.dump(F, open(OUT / "facts.json", "w"), indent=1, default=float)
print(json.dumps({k: F[k] for k in ("t41", "mem_summary")}, indent=1, default=float))

# ---- Profiles (Figure 4.1) and the extra counts ------------------------------------------
prof_t = {}
for r in recs:
    prof_t[nm(r["name"])] = {"diffengine": med(r["de"]),
                             **{b.replace("_ND", ""): med(v) for b, (_, v) in r["back"].items()}}
prof_m = {k: {"diffengine": v["DIFFENGINE"], "CPP": v["CPP_ND"], "SCIPY": v["SCIPY_ND"],
              "COO": v["COO_ND"]} for k, v in mem.items()}
json.dump({"time": prof_t, "memory": prof_m}, open(OUT / "profile_data.json", "w"), indent=1)
ps = {}
for s in ("diffengine", "CPP", "SCIPY", "COO"):
    rt = sorted(v[s] / min(v.values()) for v in prof_t.values())
    rm = sorted(v[s] / min(v.values()) for v in prof_m.values())
    ps[s] = dict(fastest=sum(x == 1 for x in rt), tau100=rt[-1], tau96=rt[-2], tau92=rt[-3],
                 mem_lowest=sum(x == 1 for x in rm), mem_tau100=rm[-1])
F["profile"] = ps
be = {}
for p in par:
    firsts = [x for x in p["first"].values() if x]
    if p["de"][0] > p["tensor"][0]:
        be[p["name"]] = (min(firsts) - p["de_first"]) / ((p["de"][0] - p["tensor"][0]) / 1e3)
F["breakeven"] = be
F["coo_vs_cpp_first"] = sum(1 for p in par if p["first"]["CPP_ND"] is None
                            or p["first"]["COO_ND"] < p["first"]["CPP_ND"])
F["uqp_old_engine"] = ms(ts.times(ts.load([T + "/cold_fork.json"])[0][("cold", "UnconstrainedQP")],
                                  "DIFFENGINE"))
short = {k: v for k, v in rows.items() if any(0 < len(x) < 20 for x in
                                              (s for s in v["samples"].values()))}
F["short_reps"] = sorted({f"{k[0]}:{k[1]}" for k in short})
dims = {}
for n in SUITE:
    d = rows[("cold", n)].get("dims", {})
    dims[nm(n)] = {k: d.get(k) for k in ("m", "n", "nnz_A", "nnz_P", "n_param_objects")}
F["dims"] = dims
F["warm_phase"] = {}
for n in DPP7:
    ss = rows[("warm", n)]["samples"]["de_cached"]
    tot = {k: 0.0 for k in ("numeric", "assemble", "format")}
    cnt = 0
    for s in ss:
        for ph in s["phases"]:
            for k in tot:
                tot[k] += ph[k]
            cnt += 1
    it = float(np.mean([x for s in ss for x in s["iters"]]))
    F["warm_phase"][nm(n)] = {k: v / cnt / it * 100 for k, v in tot.items()} | {"ms": it * 1e3}
json.dump(F, open(OUT / "facts.json", "w"), indent=1, default=float)
print(json.dumps({k: F[k] for k in ("profile", "breakeven", "coo_vs_cpp_first",
                                    "uqp_old_engine", "short_reps", "warm_phase")},
                 indent=1, default=float))
