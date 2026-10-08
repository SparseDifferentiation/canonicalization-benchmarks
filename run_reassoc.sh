#!/usr/bin/env bash
# CVXPY #3524's matmul reassociation applied to the stock backends as well
# (reassociate.py, inside the timer), on the suite problems where it fires, so the
# rewrite is credited to neither diffengine nor cvxcore. Baselines on cvxpy 1.9.2;
# the engine side is results/thesis-pr3524/. Same hygiene as run_thesis_final.sh.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-reassoc}
UP=.venv-upstream/bin/python
SET=${SET:-UnconstrainedQP,QuantumHilbertMatrix,SDPSegfault1132Benchmark,OptimalAdvertising,SlowPruningBenchmark}
mkdir -p "$OUT"

$UP thesis_final_benchmarks.py verify-ra --set "$SET" --out "$OUT/verify_ra.json"

if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

$UP thesis_final_benchmarks.py time --set "$SET" --kind cold \
  --targets CPP_ND_RA,SCIPY_ND_RA,COO_ND_RA --out "$OUT/cold_upstream_ra.json"

T=results/thesis
P=results/thesis-pr3524
.venv-thesis-pr3524/bin/python thesis_stats.py $T/verify_*.json $T/cold_*.json \
  $P/verify_*.json $P/cold_fork.json "$OUT"/*.json --out "$OUT/summary.md"
