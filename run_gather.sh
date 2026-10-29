#!/usr/bin/env bash
# Prototype (2026-10-26, not in the thesis): apply the cone row layout on the DIFFENGINE
# re-solve path as a gather of A.data planned once per sparsity pattern (CSC indptr is
# unchanged by a row permutation). .venv-thesis-gather is .venv-thesis (fork 35e81b1,
# engine 4f42e05) with only diff_engine/cone_program.py changed. Compare with
# results/thesis-n30/warm_fork.json (#3525 gather) and results/thesis-n30-no3525/.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=4f42e05
export BENCH_REPS=${BENCH_REPS:-30}
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-n30-gather}
PY=.venv-thesis-gather/bin/python
mkdir -p "$OUT"
for set in suite nondpp; do
  $PY thesis_final_benchmarks.py verify --set "$set" --out "$OUT/verify_$set.json"
done
$PY thesis_final_benchmarks.py time --set suite --kind warm \
  --targets de_cached,de_cached_nodense --out "$OUT/warm_fork.json"
$PY thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets de_cached --out "$OUT/nondpp_warm_fork.json"
