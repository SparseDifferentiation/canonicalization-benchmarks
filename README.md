# diffengine canonicalization benchmarks

This repo holds the experiments for Chapter 4 of the thesis. They measure the cost of
**canonicalization**: building the solver-ready problem data `(P, c, A, b)` of a convex
program in CVXPY. The CVXPY `DIFFENGINE` backend
([SparseDiffEngine](https://github.com/SparseDifferentiation/SparseDiffEngine) through
[SparseDiffPy](https://github.com/SparseDifferentiation/SparseDiffPy)) is compared with
CVXPY's stock `cvxcore` backends, `CPP`, `SCIPY` and `COO`. The problems are the 25 of
the public [CVXPY benchmark suite](https://github.com/cvxpy/benchmarks), plus seeded
extra families. Nothing is ever solved: only `get_problem_data` is timed.

Two regimes are measured:

- **First canonicalization (cold):** one construction from a freshly built problem
  (Table 4.1, Figure 4.1).
- **Re-solve (warm):** re-extracting the data after the parameter values change
  (Table 4.2).

This repo was split out of
[SparseDifferentiation/Jacobian-accumulation](https://github.com/SparseDifferentiation/Jacobian-accumulation),
which is archived and also holds the CasADi, Julia, JuMP and AMPL/ASL comparisons and
the mechanism probes. Those are not part of the thesis.

`CHANGES.md` lists every modification to the engine and the CVXPY fork that these
numbers depend on, and which of them the ablation switches can turn off.

## Replicating

Requirements: macOS or Linux, [uv](https://docs.astral.sh/uv/), git, cmake and a C/C++
compiler. Run everything from the repo root.

```bash
envs/setup_suite.sh      # clone cvxpy/benchmarks at the pinned commit -> cvxpy_benchmarks/
envs/setup_fork.sh       # .venv-thesis: cvxpy fork @35e81b1 + engine 4f42e05, stamped
envs/setup_upstream.sh   # .venv-upstream: stock cvxpy 1.9.2 (baselines)

./run_thesis_final.sh    # correctness gate, then every timing/memory run -> results/thesis/
```

`run_thesis_final.sh` does the following:

1. It runs the correctness gate first.
2. It times each measurement in a fresh subprocess, 20 replicates (10 when one sample
   takes more than 30 s).
3. It resumes where it stopped, skipping problems already in an output file.
4. It ends by writing `results/thesis/summary.md` with `thesis_stats.py`.

Expect it to take most of a day. Run it on mains power with nothing else running, and
never run two timing jobs at once. The script pins every BLAS to one thread.

Two interpreters are needed. The fork forces parametrized problems onto `DIFFENGINE` on
the `ignore_dpp` path, so stock `CPP`/`SCIPY`/`COO` baselines can only run on upstream
cvxpy.

`thesis_final_benchmarks.py` refuses to time or verify engine targets unless the venv's
engine stamp (`.venv-thesis/ENGINE_COMMIT`, written by `setup_fork.sh`) matches
`ENGINE_COMMIT`. This exists because a PyPI `sparsediffpy` wheel once ended up in the
benchmark venv unnoticed.

Figures:

```bash
uv run --with matplotlib --with numpy --with scipy python plot_thesis_figures.py --thesis
THESIS_DIR=../wzz-thesis uv run --with matplotlib --with numpy python plot_deck_profiles.py
```

## What produces what

| Thesis | Measurement | Targets | Output |
|---|---|---|---|
| correctness statement | `(P, c, A, b)` of every engine variant vs `CPP`/`SCIPY`/`COO`, first build and after a parameter update | `verify` | `results/thesis/verify_{suite,nondpp}.json` |
| Table 4.1, Fig. 4.1(a), dense ablation (cold) | first canonicalization, 25 problems | fork `DIFFENGINE`, `DE_NODENSE`; upstream `CPP_ND`, `SCIPY_ND`, `COO_ND` | `cold_{fork,upstream}.json` |
| Table 4.2, 2×2 ablation (warm) | re-solves of the parametric problems | fork `de_cached{,_nodense,_rebuild,_nodense_rebuild}`; upstream `dpp`, `dpp_coo`, `dpp_scipy`, `nodpp_*` | `warm_{fork,upstream}.json` |
| non-DPP re-solves | `lasso`, `factor_cov` as DPP / non-DPP / parameter-free | see `run_thesis_final.sh` | `nondpp_{warm,cold}_*.json` |
| sensitivity, scaling | n × density grid; scalable suite copies, 5 seeds | cold | `sensitivity_*.json`, `scaling_*.json` |
| Fig. 4.1(b), memory | peak-RSS delta + the engine's counters | cold and warm | `memory_*.json` |
| statistics | mean ± std, Mann–Whitney + Holm, Wilcoxon, bootstrap CIs of the geomean, ablation contrasts, phase shares | `thesis_stats.py` | `summary.md`, CSVs |

Every output file records the machine, CPU, the Python/numpy/scipy/clarabel/cvxpy
versions, the cvxpy commit, the engine commit and `.so` hash, the engine's linked BLAS,
and numpy's BLAS (threadpoolctl).

### Results directories

- `results/thesis/`: the final-deposit runs. The revised thesis numbers come from here.
- `results/v1-submission/`: the single-run data behind the thesis as first submitted
  (2018 Intel MacBook Pro, Aug 2026), kept for provenance. `plot_thesis_figures.py`
  still reads it. Five parametric rows of Table 4.1 were the fastest of three replicate
  runs whose files (`results/repl/`) were never committed, so the submitted tables can
  only be regenerated approximately from here.
- `results/thesis-pr3524/`, `results/thesis-reassoc/`, `results/thesis-scaling-ra/`: the
  fork with CVXPY #3524, and #3524 applied to the stock backends.
- `results/thesis-scaling-norewrite/`: diffengine without #3524 (`.venv-thesis`) on the
  scaled instances of the five problems where #3524 fires (`run_scaling_norewrite.sh`).
- `results/thesis-final/`: every number and table row of Chapter 4 and Appendix A, written
  by `thesis_numbers.py` and `thesis_tex.py`.

The thesis tables use the **no-rewrite** baseline: no backend uses #3524. On the five
problems where it fires, the diffengine rows come from `results/thesis/` (fork 35e81b1, the
same engine 4f42e05), and CVXPY is 1.9.2 as released. `THESIS_BASELINE=best-of-both`
reproduces the earlier draft, in which each CVXPY backend got the faster of its times with
and without #3524 while diffengine always had it.

- `results/supplementary/pr125_ab/`: a warm A/B of SparseDiffEngine #125
  (parameter-free subtree pruning) on cvxpy #3449, Apple M2, 2026-09-19. It is not in
  the thesis. The write-up is in its `results_backends_pr125_summary_20260919.md`; the
  scripts are in `supplementary/pr125_ab/`.

## Files

| File | Role |
|---|---|
| `thesis_final_benchmarks.py` | the runner: `time` / `memory` / `verify` modes, replicates, phase times, environment record, engine guard |
| `thesis_extra_problems.py` | seeded families beyond the suite (non-DPP variants, sensitivity grid, scalable copies) |
| `thesis_stats.py` | statistics and `summary.md` |
| `run_thesis_final.sh` | the full sweep |
| `run_backend_benchmarks.py` | the original single-run backend benchmark; its helpers (problem discovery, parameter assignment, the chain's DPP predicate, the kill-safe subprocess runner) are reused by the runner |
| `verify_de_warm_equivalence.py`, `_compare.py` | standalone warm-artefact gate: DIFFENGINE vs the tensor path after a parameter update |
| `plot_thesis_figures.py`, `plot_sparsity_correlations.py`, `plot_deck_profiles.py` | thesis profiles, structure-metric correlations, defence-deck copies |
| `envs/` | environment setup, all commits pinned |

## Fairness rules

- **What is timed:** only `get_problem_data(solver=CLARABEL)`. Problem construction is
  outside the timer. No solve.
- **`ignore_dpp` baselines:** stock backends run with an explicit `canon_backend`.
  `CPP` is pinned, because otherwise cvxpy silently switches to `COO` above 1000
  parameter entries. The `dpp?` predicate is the chain's
  (`is_dpp('dcp', quad_form_dpp='qp')`), not `problem.is_dpp()`.
- **Same artefact:** a timing is reported only for a problem whose `(P, c, A, b)`
  matches the stock backend's.
- **Engine build:** `sparsediffpy` must be compiled from the pinned engine.
  PyPI 0.6.0 lacked the #107 refresh fix and the gather-based sparsity fill. With it,
  warm results were wrong and the cold SemidefiniteProgramming run took 433.8 s
  instead of 2.0 s.
