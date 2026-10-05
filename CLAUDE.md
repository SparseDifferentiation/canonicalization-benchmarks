# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

Experiments for Chapter 4 of the thesis: CVXPY canonicalization (`get_problem_data`)
with the `DIFFENGINE` backend vs stock `CPP`/`SCIPY`/`COO`, on the 25-problem
cvxpy/benchmarks suite plus `thesis_extra_problems.py`. See README.md for the run
procedure and CHANGES.md for the engine/fork modifications and ablation switches.
Comparisons with CasADi/Julia/JuMP/ASL are out of scope. They live in the archived
SparseDifferentiation/Jacobian-accumulation repo.

## Environment

- Build environments only with `envs/setup_*.sh`. Every commit is pinned there.
- `.venv-thesis` (fork + engine) and `.venv-upstream` (cvxpy 1.9.2) must stay separate.
  The fork forces parametrized `ignore_dpp` problems onto DIFFENGINE, and cvxpy 1.9.2
  pins `sparsediffpy<0.4`.
- Never let a PyPI `sparsediffpy` into `.venv-thesis`. The runner checks
  `.venv-thesis/ENGINE_COMMIT` against `ENGINE_COMMIT` and aborts on a mismatch. Do not
  bypass this with `BENCH_ALLOW_ANY_ENGINE=1` for a reported run.

## Benchmark hygiene

- Pin BLAS to one thread (`run_thesis_final.sh` does this).
- Never run two timing jobs concurrently. `verify` is not timing-sensitive.
- New results go under `results/thesis/` (or a new dated directory). Never overwrite
  `results/v1-submission/` or `results/supplementary/`.
- A timing counts only if the problem passed the correctness gate.
