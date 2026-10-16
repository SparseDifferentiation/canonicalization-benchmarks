#!/usr/bin/env bash
# diffengine without CVXPY #3524 on the scaled instances of the five problems where #3524
# rewrites a chain, for the no-rewrite baseline of thesis_tex.py. Fork: .venv-thesis
# (fork 35e81b1 = 5c07151 minus #3524, engine 4f42e05); the stock baselines of
# results/thesis-scaling are reused. Instances where diffengine is capped with #3524 are
# skipped. Same hygiene as run_scaling.sh.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
export BENCH_REPS=${BENCH_REPS:-5}
OUT=${OUT:-results/thesis-scaling-norewrite}
FORK=.venv-thesis/bin/python
SET="scaled:cls=UnconstrainedQP:s=0.5,scaled:cls=UnconstrainedQP:s=2,\
scaled:cls=QuantumHilbertMatrix:s=0.5,scaled:cls=SDPSegfault1132Benchmark:s=0.5,\
scaled:cls=OptimalAdvertising:s=0.25,scaled:cls=OptimalAdvertising:s=0.5,\
scaled:cls=OptimalAdvertising:s=2,\
scaled:cls=SlowPruningBenchmark:s=0.5,scaled:cls=SlowPruningBenchmark:s=2"
mkdir -p "$OUT"
$FORK thesis_final_benchmarks.py verify --set "$SET" --out "$OUT/verify_scaled.json"

if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

$FORK thesis_final_benchmarks.py time --set "$SET" --kind cold --targets DIFFENGINE \
  --out "$OUT/scaled_fork.json"
# The first UnconstrainedQP s = 1/2 timing overlapped another job on 2026-10-16; it was
# rerun alone (medians 3.04 s and 3.08 s), and thesis_tex.py uses the rerun.
$FORK thesis_final_benchmarks.py time --set "scaled:cls=UnconstrainedQP:s=0.5" --kind cold \
  --targets DIFFENGINE --out "$OUT/scaled_fork_uqp05_rerun.json"
