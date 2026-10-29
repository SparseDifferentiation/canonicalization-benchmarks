#!/usr/bin/env bash
# The final sweep at 30 runs (advisor review, 2026-10-24): every timed comparison of
# Chapter 4 at the same n, every problem at s = 1/4, 1/2, 1, 2, 4 (grid25), and the
# density sweep with and without dense blocks (density8). No backend uses CVXPY #3524.
# Order: the suite at s = 1 first, then re-solves, density, and the size grid last.
# Same hygiene as run_thesis_final.sh; every step resumes.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
export BENCH_REPS=${BENCH_REPS:-30}
# Slow targets (first sample > 30 s) keep 10 replicates.
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-n30}
FORK=.venv-thesis/bin/python
UP=.venv-upstream/bin/python
mkdir -p "$OUT"

for set in suite nondpp density8 grid25; do
  $FORK thesis_final_benchmarks.py verify --set "$set" --out "$OUT/verify_$set.json"
done

if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

cold() {  # cold <set> <prefix>
  $FORK thesis_final_benchmarks.py time --set "$1" --kind cold \
    --targets DIFFENGINE,DE_NODENSE --out "$OUT/${2}_fork.json"
  $UP thesis_final_benchmarks.py time --set "$1" --kind cold \
    --targets CPP_ND,SCIPY_ND,COO_ND --out "$OUT/${2}_upstream.json"
}

# Table 4.1, the profiles and the dense-block ablation.
cold suite cold
$FORK thesis_final_benchmarks.py memory --set suite --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out "$OUT/memory_cold_fork.json"
$UP thesis_final_benchmarks.py memory --set suite --kind cold \
  --targets CPP_ND,SCIPY_ND,COO_ND --out "$OUT/memory_cold_upstream.json"

# Table 4.2 and the 2x2 ablation: re-solves of the parametric problems.
$FORK thesis_final_benchmarks.py time --set suite --kind warm \
  --targets de_cached,de_cached_nodense,de_cached_rebuild,de_cached_nodense_rebuild \
  --out "$OUT/warm_fork.json"
$UP thesis_final_benchmarks.py time --set suite --kind warm \
  --targets dpp,dpp_coo,dpp_scipy,nodpp_cpp,nodpp_coo,nodpp_scipy --out "$OUT/warm_upstream.json"

# Non-DPP: DPP / non-DPP / parameter-free variants.
$FORK thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets de_cached,de_cached_rebuild --out "$OUT/nondpp_warm_fork.json"
$UP thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets dpp,nodpp_cpp,nodpp_coo --out "$OUT/nondpp_warm_upstream.json"
$FORK thesis_final_benchmarks.py time --set nondpp --kind cold \
  --targets DIFFENGINE --out "$OUT/nondpp_cold_fork.json"
$UP thesis_final_benchmarks.py time --set nondpp --kind cold \
  --targets CPP_ND,SCIPY_ND,COO_ND --out "$OUT/nondpp_cold_upstream.json"

# Density, with its memory (the dense blocks store the zeros of the mask).
cold density8 density8
$FORK thesis_final_benchmarks.py memory --set density8 --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out "$OUT/memory_density8_fork.json"

# The size grid; s = 1 is the suite above.
cold grid25 grid25

$FORK thesis_stats.py "$OUT"/verify_*.json "$OUT"/cold_*.json "$OUT"/warm_*.json \
  "$OUT"/nondpp_*.json "$OUT"/density8_*.json "$OUT"/grid25_*.json "$OUT"/memory_*.json \
  --out "$OUT/summary.md"
