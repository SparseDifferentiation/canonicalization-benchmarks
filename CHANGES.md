# Changes these results depend on

The benchmark compares whole backends, so its speedups combine everything listed below.
This file catalogues each modification to SparseDiffEngine, SparseDiffPy and CVXPY that
the `DIFFENGINE` numbers rely on. For each one it gives where it lives and whether the
ablation switches can isolate it. Pinned builds:

| Component | Commit | Source |
|---|---|---|
| SparseDiffEngine | `4f42e05` (branch `fix-block-left-fill-values-quadratic`: main `64f7432` with #125, plus the linear CSR value fill) | github.com/SparseDifferentiation/SparseDiffEngine |
| SparseDiffPy (bindings) | `9e0246e`, submodule moved to the engine commit above | github.com/SparseDifferentiation/SparseDiffPy |
| CVXPY fork | `35e81b1` (`thesis-ablation`) | github.com/Transurgeon/cvxpy |
| CVXPY baseline | 1.9.2 (PyPI) | — |

## Engine (SparseDiffEngine)

| ID | Commit | Change | Ablatable? |
|---|---|---|---|
| E1 | `4172c5e` (#107; 0.6.x backport `3dc7cd8`) | Composite `param_source` refresh. An atom that owns a parameter source marks its subtree dirty before re-evaluating, so `(p*A)@x` and `quad_form(x, g*Sig)` re-solve correctly. | No. It is a correctness fix; without it warm results are wrong. |
| E2 | `c549c64` (0.6.x `424ddde`) | "Swedish" sparsity fill. The symbolic fill of block left-multiply and CSR@CSC gathers from the output side (Gustavson `sorted_pattern_union`) instead of scanning every row. Output is byte-identical. | Only by building an engine without it. PyPI 0.6.0 lacks it: SemidefiniteProgramming 433.8 s vs 2.0 s, QuantumHilbertMatrix 22.2 s vs 2.1 s. |
| E3 | `64f7432` (#125) | The warm refresh walk skips parameter-free subtrees (memoised `has_params`). | Engine-build A/B only. Measured in `results/supplementary/pr125_ab/`: engine share up to 14.9× faster, end-to-end warm geomean 1.302× → 1.172×. |
| E4 | #120, #121, `8321d59`, `4dbb53b` | Matrix-class refactor (`row_gather`, `row_reduce`). | Engine build only. |
| E5 | `9699559` (#96) | Dense-P `quad_form` binding. | Unused when `DIFFENGINE_NO_DENSE=1`. |
| E6 | `ba46030` (branch `fix-block-left-fill-values-quadratic`, head `4f42e05`) | Linear CSR value fill in `block_left_multiply_fill_values` (Gustavson scatter/gather through the CSC mirror). Bit-identical output. See the caveat below. | No. Without it, `DE_NODENSE` is quadratic on long rows. |
| — | `960e02b` (branch `lazy-inv-arrays`) | Lazy inverse arrays: lower memory on the kron path (OptimalAdvertising peaked at 5.9 GB). | **Not merged; not in any measured build.** |

## CVXPY (upstream PRs the fork includes)

| ID | PR / commit | Change | Ablatable? |
|---|---|---|---|
| C1 | #3448 (`67225c5`) | `DIFFENGINE` canon backend for parameter-free problems. | It is the backend choice. |
| C2 | #3523 (`c21435c`) | `make_constant_quad_form`: constant P stored dense or CSR by density; explicit zeros dropped. | `DIFFENGINE_NO_DENSE=1` forces CSR. |
| C3 | #3525 (`773163e`) | Cone restructuring as a chain reduction, applied as a permutation. | No. **Confound:** cvxpy 1.9.2, the baseline, predates it (no `cone_format.py`), so the fork's `format` phase is a permutation while the baselines still do the matrix product. |

## CVXPY fork (Transurgeon/cvxpy, not upstream)

| ID | Commit | Change | Ablatable? |
|---|---|---|---|
| C4 | `538e14f` | `CallbackParamFold` reduction: variable-free, non-parameter-affine subtrees (`power(t,2)`, `log_det(P)`) become a callback parameter re-evaluated on access, so `Dcp2Cone` never epigraph-relaxes them while parameters stay symbolic. | No switch. |
| C5 | `8f36cc4` | Symbolic parameters on the `ignore_dpp`/non-DPP route. Eligible problems skip `EvalParams` and go to `DIFFENGINE`; re-solves re-extract from the cached engine program instead of rebuilding the chain. Parametric `QuadForm` P and parametric `perspective` fall back to `EvalParams`. | `DIFFENGINE_REBUILD=1` removes the caching (the symbolic/numeric split). |
| C6 | `b7bb765` (= cvxpy #3449 head) | `ConeProg` split: `DiffengineConeProg` carries no parameter tensors. | No switch. |
| C7 | `35e81b1` | Benchmark-only switches and phase timers (below). | — |
| C8 | older converter code | Constant matmuls below density 0.05 go to CSR at conversion; `_build_jacobian_csc` drops exact zeros. | **No switch.** The 0.05 routing already sends sparse constants to CSR in both variants. |
| C9 | #3524 (`6207f12`), on branch `thesis-ablation-pr3524` @ `5c07151` | Matmul chains that end in a parameter-free constant are reassociated so the constant moves toward the leaves (`(A @ B) @ c -> A @ (B @ c)`), keeping intermediates narrow (issue #2205). Fires on UnconstrainedQP, QuantumHilbertMatrix, SDPSegfault1132, OptimalAdvertising, SlowPruning. Measured in `results/thesis-pr3524/` (UnconstrainedQP cold 22.9 s -> 0.016 s). | No switch. Rerun only on the affected problems; see `run_pr3524_rerun.sh`. The thesis tables leave it out on every backend (`THESIS_BASELINE`, README). |

## Ablation switches (fork `35e81b1`)

All are read on every call and default to off.

| Variable | Effect |
|---|---|
| `DIFFENGINE_NO_DENSE=1` | Fully CSR only on parameter-free problems: every dense class (PD/SPD) starts in the dense left/right matmul or the dense `quad_form`, and the engine never promotes a CSR product to one. On a parametric problem a parametric `A @ x` / `x @ A` keeps a dense-class Jacobian and a parametric `quad_form` P a dense Hessian (the engine has no CSR path for a parametric matrix). Constant matrices in left/right matmul use the CSR bindings, constant `quad_form` P ignores the density threshold and uses CSR, and constant P in symbolic `quad_form` uses CSR. **Parametric matrices stay dense in both variants.** |
| `DIFFENGINE_REBUILD=1` | `update_parameters` calls `extractor.rebuild()`: conversion and the symbolic pass (`init_jacobian_coo`, Hessian init) are repeated on every update. |
| `DIFFENGINE_PROFILE=1` | Phase times in `extractor.PHASE_TIMES`: convert, symbolic, numeric, assemble (COO→CSC), format (`_restructure`). |

The runner exposes the switches as targets:

| | dense blocks on | dense blocks off |
|---|---|---|
| cold | `DIFFENGINE` | `DE_NODENSE` |
| warm, split on | `de_cached` | `de_cached_nodense` |
| warm, split off | `de_cached_rebuild` | `de_cached_nodense_rebuild` |
| cold, parameters evaluated (fully CSR when off) | `DE_EVAL` | `DE_NODENSE_EVAL` |

`DE_EVAL` / `DE_NODENSE_EVAL` time `EvalParams` plus `get_problem_data` on the parameter-free
result (as stock `ignore_dpp` does), on parametric problems only. Their ratio is the
dense-block contrast with no dense class on the parametric problems.

**What the 2×2 does not separate.** The examiner names three sources of the speedup:
dense representations, the two-pass split, and "a leaner C implementation". The 2×2
isolates the first two. The third (global rather than local layout, no materialised
views, no parameter tensor: E2–E4, C4, C6, C8) has no switch. It is what remains of the
gap to the stock backends after both switches are off.

**Caveats for the write-up:**

- The runner sets `DIFFENGINE_PROFILE=1` in every fork timing, so fork numbers include
  the phase timers' small overhead. The baselines do not.
- `DE_NODENSE` is "no dense blocks for constant data", not "everything in CSR":
  parametric matrices stay dense.
- **The CSR value fill was quadratic on long rows (fixed, engine `ba46030`).**
  `block_left_multiply_fill_values` took a merge-based dot of a whole row of A per
  output entry. On SimpleLPBenchmark (`c @ x`, `c` dense of length n) with
  `DIFFENGINE_NO_DENSE=1` this meant 3.2 s at n=10⁵ and 49 s at 4·10⁵, about 8.5 h
  at the suite's n=10⁷. cvxpy's backends take 6.4–7.4 s there; the dense path takes
  1.36 s. Engine `4dbb53b` already behaved the same, so it is not from #125.
  Without the fix, the ablation would have credited dense blocks with avoiding a
  CSR bug.
  - The fix, on engine branch `fix-block-left-fill-values-quadratic`, is Gustavson
    scatter/gather through the sparse matrix's cached CSC mirror. It is linear
    (`NO_DENSE` at 10⁷: 1.59 s).
  - It is bit-identical: an engine C test compares it against the old kernel, and
    `(P, c, A, b)` hash-match `64f7432` on all 25 suite problems, dense and
    `NO_DENSE`.
  - It also applies to `DIFFENGINE` wherever a constant goes to CSR (density below
    0.05).
  - Pinned for the final runs: engine `4f42e05`, the branch head (`ba46030` plus
    two test commits), in `envs/setup_fork.sh` and `run_thesis_final.sh`. It is not
    yet merged into engine main.
