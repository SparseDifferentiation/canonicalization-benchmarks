"""LaTeX rows of the Chapter 4 tables that thesis_numbers.py does not write itself.

Usage: python thesis_tex.py   (after thesis_numbers.py)
"""
import json
import os
import re
import sys
from pathlib import Path

N30 = os.environ.get("THESIS_RESULTS") == "n30"
HERE = Path(__file__).parent / "results" / ("thesis-n30-final" if N30 else "thesis-final")
F = json.load(open(HERE / "facts.json"))
RES = Path(__file__).parent / "results"
NAME = {"CVaRBenchmark": "CVaR", "ConeMatrixStuffingBench": "ConeMatrixStuffing",
        "ParametrizedQPBenchmark": "ParametrizedQP", "SDPSegfault1132Benchmark": "SDPSegfault1132",
        "SimpleFullyParametrizedLPBenchmark": "SimpleFullyParametrizedLP",
        "SimpleLPBenchmark": "SimpleLP", "SimpleQPBenchmark": "SimpleQP",
        "SimpleScalarParametrizedLPBenchmark": "SimpleScalarParametrizedLP",
        "SlowPruningBenchmark": "SlowPruning", "lasso (n = 1000)": "\\texttt{lasso}, $n = 1000$",
        "lasso": "\\texttt{lasso}"}
nm = lambda c: NAME.get(c, c)  # noqa: E731
ORDER = F["order"]


def write(name, lines):
    (HERE / name).write_text("\n".join(lines) + "\n")


# Phases: the five slower problems, then the median.
SLOW = [s[0] for s in sorted(F["t41"]["slower"], key=lambda s: -s[1])]
lines = []
for p in SLOW:
    v = F["phase"][p]
    lines.append(f"{p:<20} & {v['time']:.2f} & " +
                 " & ".join(f"{x:.0f}" for x in v["share"]) + " \\\\")
lines.append("\\midrule")
lines.append("Median, all $25$   & ---  & " +
             " & ".join(f"{x:.0f}" for x in F["phase_median"]) + " \\\\")
write("phases.tex", lines)

# Non-DPP table.
nd = F["nondpp"]
lines = []
for fam, lab in (("lasso", "\\texttt{lasso}, $n = 1000$"),
                 ("factor_cov", "\\texttt{factor\\_cov}, $n = 5000$")):
    for v, vl in (("dpp", "\\ac{DPP}"), ("nondpp", "non-\\ac{DPP}"), ("free", "parameter-free")):
        r = nd[f"{fam}:{v}"]
        f = lambda x: "---" if x is None else (f"{x:.1f}" if x < 100 else f"{x:.0f}")  # noqa
        lines.append(f"{lab if v == 'dpp' else '':<34} & {vl:<15} & {f(r['cvxpy_mean'])} & "
                     f"{f(r['cached'])} & {f(r['rebuild'])} & {r['ratio']:.2f} \\\\")
    if fam == "lasso":
        lines.append("\\addlinespace")
write("nondpp.tex", lines)

# Ablation.
A = F["ablation"]


def arow(lab, ref, k, n):
    a = A[k]
    if a["p"] < 1e-3:
        mant, ex = f"{a['p']:.1e}".split("e")
        p = f"${mant} \\times 10^{{{int(ex)}}}$"
    else:
        p = f"{a['p']:.3f}"
    return (f"{lab:<22} & {ref:<20} & {a['g']:.2f} & {a['lo']:.2f}--{a['hi']:.2f} & "
            f"{p} & {a['sig']}/${n}$ \\\\")


write("ablation.tex", [
    "\\multicolumn{6}{l}{\\textit{First canonicalization, $25$ problems}} \\\\",
    arow("no dense blocks", "\\texttt{diffengine}", "nodense_cold", 25),
    *([] if N30 else [arow("fully sparse", "\\texttt{diffengine}", "fullycsr_cold", 25)]),
    arow("no dense blocks", "best \\texttt{CVXPY}", "nodense_vs_best", 25),
    "\\addlinespace",
    "\\multicolumn{6}{l}{\\textit{Re-solve, $7$ \\ac{DPP} problems}} \\\\",
    arow("no dense blocks", "\\texttt{diffengine}", "nodense_warm", 7),
    arow("no split", "\\texttt{diffengine}", "rebuild_warm", 7),
    arow("neither", "\\texttt{diffengine}", "neither_warm", 7),
])

# Memory appendix table.
lines = []
for p in ORDER:
    m = F["memory"][p]
    f = lambda x: f"{x:,.0f}".replace(",", "\\,") if x >= 100 else f"{x:.1f}"  # noqa: E731
    lines.append(f"{p} & " + " & ".join(f(m[k]) for k in
                                        ("CPP_ND", "SCIPY_ND", "COO_ND", "DIFFENGINE",
                                         "DE_NODENSE")) + " \\\\")
write("app_memory.tex", lines)

# Correctness appendix table.
lines = []
for p in ORDER:
    v = F["verify"][p]
    st = lambda x: "---" if x is None else ("pass" if x else "\\textbf{fail}")  # noqa: E731
    mx = "0" if v["maxabs"] == 0 else f"${v['maxabs']:.1e}".replace("e-", " \\times 10^{-") + "}$"
    mx = re.sub(r"\{-0*(\d+)\}", r"{-\1}", mx)
    lines.append(f"{p} & {st(v['first'])} & {st(v['update'])} & {v['passed']}/{v['n']} & {mx} \\\\")
write("app_verify.tex", lines)
if N30:  # the size and density tables are figures now (thesis_figures_n30.py)
    print("ok")
    sys.exit()


# Scaling tables, parsed from the results repo's own summary.
def md_table(path, title):
    txt = Path(path).read_text().split("\n")
    i = next(k for k, line in enumerate(txt) if line.startswith("## " + title))
    rows = []
    for line in txt[i + 1:]:
        if line.startswith("## "):
            break
        if line.startswith("| ") and not line.startswith("| problem") and "---" not in line:
            rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def cellv(x):
    if x in ("cap", "unverified"):
        return {"cap": "cap", "unverified": "unv."}[x]
    v = float(x)
    return f"{v:.2f}" if v >= 0.01 else f"{v:.3f}"


# Size tables on the baseline of Table 4.1 (facts.json "baseline"); s = 1 is Table 4.1's ratio.
# no-rewrite: on the scaled instances of the five problems where #3524 fires, diffengine comes
#   from thesis-scaling-norewrite (fork 35e81b1, no #3524) against the stock backends.
# best-of-both: each CVXPY backend gets the faster of its times with and without #3524
#   (thesis-scaling-ra).
def medians(path):
    out = {}
    for r in json.load(open(path))["rows"]:
        for t, xs in r["samples"].items():
            ts = sorted(x["time"] for x in xs if x.get("time") is not None)
            if ts:
                out[(r["class"], t)] = ts[len(ts) // 2]
    return out


MED = {}
for f in ("scaled25_fork", "scaled25_upstream", "families_fork", "families_upstream"):
    MED.update(medians(RES / f"thesis-scaling/{f}.json"))
RA = medians(RES / "thesis-scaling-ra/scaled_upstream_ra.json")
NR = medians(RES / "thesis-scaling-norewrite/scaled_fork.json")
# UnconstrainedQP at s = 1/2, rerun alone: its first timing overlapped another job.
NR.update(medians(RES / "thesis-scaling-norewrite/scaled_fork_uqp05_rerun.json"))
T41 = {ln.split("&")[0].strip(): ln.split("&")[-1].split("$")[0].strip()
       for ln in (HERE / "t41.tex").read_text().splitlines() if "&" in ln}


def best_of_both(cls, s, cell):
    if cell in ("cap", "unverified"):
        return cell
    if s == "1":
        return T41.get(nm(cls), cell)
    spec = f"scaled:cls={cls}:s={s}"
    if F.get("baseline", "no-rewrite") == "no-rewrite":
        if (spec, "DIFFENGINE") not in NR:
            return cell
        best = min(MED[(spec, f"{b}_ND")] for b in ("CPP", "SCIPY", "COO"))
        return f"{NR[(spec, 'DIFFENGINE')] / best:.4f}"
    if not any(c == spec for c, _ in RA):
        return cell
    best = min(min(MED[(spec, f"{b}_ND")], RA[(spec, f"{b}_ND_RA")])
               for b in ("CPP", "SCIPY", "COO"))
    return f"{MED[(spec, 'DIFFENGINE')] / best:.4f}"


S = RES / "thesis-scaling/summary.md"
for title, out in (("Scaling: 25 problems", "app_scaled25.tex"),
                   ("Scaling: 10 families", "t_families.tex"),
                   ("Density: 5 problems", "t_density.tex")):
    rows = md_table(S, title)
    if out != "t_density.tex":
        txt = S.read_text()
        head = next(ln for ln in txt[txt.index("## " + title):].splitlines()
                    if ln.startswith("| problem"))
        scales = [h.strip().removeprefix("s ") for h in head.strip("|").split("|")[1:-1]]
        rows = [[r[0]] + [best_of_both(r[0], s, c) for s, c in zip(scales, r[1:-1])] + [r[-1]]
                for r in rows]
    if out == "app_scaled25.tex":
        rows.sort(key=lambda r: ORDER.index(nm(r[0])))
    write(out, [f"{nm(r[0]):<27} & " + " & ".join(cellv(c) for c in r[1:-1]) + " \\\\"
                for r in rows])

# Instance dimensions, to compare with Table B.1.
def k(x):
    if x is None:
        return "?"
    if x >= 1e6:
        return f"{x / 1e6:.3g}\\,M"
    if x >= 1e4:
        return f"{x / 1e3:.3g}\\,k"
    return f"{x:,}".replace(",", "\\,")


write("dims.txt", [f"{p}: m={k(d['m'])} n={k(d['n'])} nnzA={k(d['nnz_A'])} "
                   f"nnzP={k(d['nnz_P'])} params={d['n_param_objects']}"
                   for p, d in F["dims"].items()])
print("ok")
