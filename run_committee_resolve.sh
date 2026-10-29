#!/usr/bin/env bash
# Why the re-solve ratios changed since the version sent to the committee (2026-10-25):
# the committee-version software (fork ca08a26, SparseDiffPy 9db427c with engine 7e7678e,
# Python 3.14, numpy 2.4.6, scipy 1.17.1; CVXPY 1.9.2 for the tensor) re-solved on the M2
# with the Chapter 4 method (30 runs, median of 5 re-solves each). Compare with
# results/thesis-n30/warm_*.json (current software, same machine) and with the committee
# table (same software, 2018 Intel i7).
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=7e7678e
export BENCH_REPS=${BENCH_REPS:-30}
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-n30-committee}
mkdir -p "$OUT"
SET=ParamSmallMatrixStuffing,ParamConeMatrixStuffing,SimpleFullyParametrizedLPBenchmark
SET=$SET,ParametrizedQPBenchmark,SimpleScalarParametrizedLPBenchmark,FactorCovarianceModel
SET=$SET,SVMWithL1Regularization

.venv-committee/bin/python thesis_final_benchmarks.py time --set "$SET" --kind warm \
  --targets de_cached --out "$OUT/warm_fork.json"
.venv-committee-upstream/bin/python thesis_final_benchmarks.py time --set "$SET" --kind warm \
  --targets dpp,dpp_coo,dpp_scipy --out "$OUT/warm_upstream.json"
