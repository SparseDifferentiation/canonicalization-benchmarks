#!/usr/bin/env bash
# The three slower-problem fixes at 30 runs (advisor review, 2026-10-25), each against
# the fork it is applied to, in the same session so before and after share conditions:
#   .venv-thesis        fork 35e81b1 (the Chapter 4 baseline)
#   .venv-thesis-pr3524 + #3524, matmul chains evaluated from the constant (UnconstrainedQP)
#   .venv-thesis-ones   + #3570, products with a vector of ones as sums (OptimalAdvertising)
#   .venv-thesis-quad   + #3571, constant P of a quadratic objective by density (ConvexPlasticity)
# Engine 4f42e05 everywhere. Same hygiene as run_n30.sh; every step resumes.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
export BENCH_REPS=${BENCH_REPS:-30}
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-n30-prfixes}
mkdir -p "$OUT"
SET=UnconstrainedQP,ConvexPlasticity,OptimalAdvertising

run() {  # run <venv> <set> <tag>
  .venv-$1/bin/python thesis_final_benchmarks.py verify --set "$2" --out "$OUT/verify_$3.json"
  .venv-$1/bin/python thesis_final_benchmarks.py time --set "$2" --kind cold \
    --targets DIFFENGINE --out "$OUT/cold_$3.json"
  .venv-$1/bin/python thesis_final_benchmarks.py memory --set "$2" --kind cold \
    --targets DIFFENGINE --out "$OUT/memory_$3.json"
}

run thesis "$SET" base
run thesis-pr3524 UnconstrainedQP pr3524
run thesis-ones OptimalAdvertising pr3570
run thesis-quad ConvexPlasticity pr3571
