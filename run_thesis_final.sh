#!/usr/bin/env bash
# The full sweep of the final-deposit experiments (see thesis_final_benchmarks.py).
# Run from the repo root, on mains power, with other applications closed.
# Every step resumes: a problem already in its output file is skipped.
#   .venv-thesis    the fork (Transurgeon/cvxpy@thesis-ablation) + SparseDiffPy built
#                   against SparseDiffEngine@$ENGINE_COMMIT
#   .venv-upstream  cvxpy 1.9.2
set -euo pipefail
cd "$(dirname "$0")"
# Keep the machine awake: a sleep pauses the monotonic clock behind BENCH_TIMEOUT and
# makes any sample that spans it meaningless (a lid-close stalled a smoke run 40 min).
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
# Slow targets (first sample > 30 s) keep 10 replicates, not 5: at 5 vs 5 the smallest
# two-sided Mann-Whitney p is 2/252 = 0.008, which Holm can push above 0.05.
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=results/thesis
FORK=.venv-thesis/bin/python
UP=.venv-upstream/bin/python
mkdir -p $OUT

# Correctness first: no timing is reported for a problem that does not match.
$FORK thesis_final_benchmarks.py verify --set suite --out $OUT/verify_suite.json
$FORK thesis_final_benchmarks.py verify --set nondpp --out $OUT/verify_nondpp.json

# Timings on battery are not comparable: wait for mains power before timing.
if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

# Table 4.1 and the dense-block ablation: first canonicalization.
$FORK thesis_final_benchmarks.py time --set suite --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out $OUT/cold_fork.json
$UP thesis_final_benchmarks.py time --set suite --kind cold \
  --targets CPP_ND,SCIPY_ND,COO_ND --out $OUT/cold_upstream.json

# Table 4.2 and the 2x2 ablation: re-solves of the parametric problems.
$FORK thesis_final_benchmarks.py time --set suite --kind warm \
  --targets de_cached,de_cached_nodense,de_cached_rebuild,de_cached_nodense_rebuild \
  --out $OUT/warm_fork.json
$UP thesis_final_benchmarks.py time --set suite --kind warm \
  --targets dpp,dpp_coo,dpp_scipy,nodpp_cpp,nodpp_coo,nodpp_scipy --out $OUT/warm_upstream.json

# Non-DPP: DPP / non-DPP / parameter-free variants (re-solves and first compiles).
$FORK thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets de_cached,de_cached_rebuild --out $OUT/nondpp_warm_fork.json
$UP thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets dpp,nodpp_cpp,nodpp_coo --out $OUT/nondpp_warm_upstream.json
$FORK thesis_final_benchmarks.py time --set nondpp --kind cold \
  --targets DIFFENGINE --out $OUT/nondpp_cold_fork.json
$UP thesis_final_benchmarks.py time --set nondpp --kind cold \
  --targets CPP_ND,SCIPY_ND,COO_ND --out $OUT/nondpp_cold_upstream.json

# Sensitivity (n x density) and scaling: fewer replicates, five seeds per point.
export BENCH_REPS=${SWEEP_REPS:-5}
for set in sensitivity scaling; do
  $FORK thesis_final_benchmarks.py time --set $set --kind cold \
    --targets DIFFENGINE,DE_NODENSE --out $OUT/${set}_fork.json
  $UP thesis_final_benchmarks.py time --set $set --kind cold \
    --targets CPP_ND,SCIPY_ND,COO_ND --out $OUT/${set}_upstream.json
done
unset BENCH_REPS

# Memory of the ablation (one subprocess per measurement).
$FORK thesis_final_benchmarks.py memory --set suite --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out $OUT/memory_cold_fork.json
$UP thesis_final_benchmarks.py memory --set suite --kind cold \
  --targets CPP_ND,SCIPY_ND,COO_ND --out $OUT/memory_cold_upstream.json
$FORK thesis_final_benchmarks.py memory --set suite --kind warm \
  --targets de_cached,de_cached_nodense,de_cached_rebuild,de_cached_nodense_rebuild \
  --out $OUT/memory_warm_fork.json

$FORK thesis_stats.py $OUT/verify_*.json $OUT/cold_*.json $OUT/warm_*.json \
  $OUT/nondpp_*.json $OUT/sensitivity_*.json $OUT/scaling_*.json $OUT/memory_*.json \
  --out $OUT/summary.md
