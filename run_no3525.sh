#!/usr/bin/env bash
# Re-solve times without CVXPY #3525 (2026-10-26). #3525 made the cone row layout a
# permutation; on the DIFFENGINE route it is re-applied on every re-solve as a CSR row
# gather, where the earlier code did one product with a cached restructuring matrix.
# .venv-thesis-no3525 is .venv-thesis (fork 35e81b1, engine 4f42e05) with only
# diff_engine/cone_program.py's _restructure put back to that cached product.
# Also times the tensor backends on the fork (which has #3525), to check that #3525
# does not change their re-solves (Ch. 4 times them on CVXPY 1.9.2, without it).
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=4f42e05
export BENCH_REPS=${BENCH_REPS:-30}
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-n30-no3525}
NO=.venv-thesis-no3525/bin/python
mkdir -p "$OUT"
SET=ParamSmallMatrixStuffing,ParamConeMatrixStuffing,SimpleFullyParametrizedLPBenchmark
SET=$SET,ParametrizedQPBenchmark,SimpleScalarParametrizedLPBenchmark,FactorCovarianceModel
SET=$SET,SVMWithL1Regularization

for set in suite nondpp; do
  $NO thesis_final_benchmarks.py verify --set "$set" --out "$OUT/verify_$set.json"
done
$NO thesis_final_benchmarks.py time --set suite --kind warm \
  --targets de_cached,de_cached_nodense,de_cached_rebuild,de_cached_nodense_rebuild \
  --out "$OUT/warm_fork.json"
$NO thesis_final_benchmarks.py time --set nondpp --kind warm \
  --targets de_cached,de_cached_rebuild --out "$OUT/nondpp_warm_fork.json"
.venv-thesis/bin/python thesis_final_benchmarks.py time --set "$SET" --kind warm \
  --targets dpp,dpp_coo,dpp_scipy --out "$OUT/warm_tensor_with3525.json"
$NO thesis_final_benchmarks.py time --set suite --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out "$OUT/cold_fork.json"
