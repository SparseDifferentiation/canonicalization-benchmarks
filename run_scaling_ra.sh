#!/usr/bin/env bash
# #3524 rewrite on the stock backends for the scaled instances of the five problems where it
# applies (results/thesis-reassoc covers s = 1). Instances where diffengine is capped or
# unverified have no ratio and are skipped. Same hygiene as run_scaling.sh.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export BENCH_REPS=${BENCH_REPS:-5}
OUT=${OUT:-results/thesis-scaling-ra}
UP=.venv-upstream/bin/python
SET="scaled:cls=UnconstrainedQP:s=0.5,scaled:cls=UnconstrainedQP:s=2,\
scaled:cls=QuantumHilbertMatrix:s=0.5,scaled:cls=SDPSegfault1132Benchmark:s=0.5,\
scaled:cls=OptimalAdvertising:s=0.25,scaled:cls=OptimalAdvertising:s=0.5,\
scaled:cls=SlowPruningBenchmark:s=0.5,scaled:cls=SlowPruningBenchmark:s=2"
mkdir -p "$OUT"
$UP thesis_final_benchmarks.py verify-ra --set "$SET" --out "$OUT/verify_ra.json"
$UP thesis_final_benchmarks.py time --set "$SET" --kind cold \
  --targets CPP_ND_RA,SCIPY_ND_RA,COO_ND_RA --out "$OUT/scaled_upstream_ra.json"
