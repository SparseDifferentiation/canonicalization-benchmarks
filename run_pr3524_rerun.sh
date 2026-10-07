#!/usr/bin/env bash
# Rerun of the problems affected by CVXPY PR #3524 (matmul tail reassociation) and by
# the dense matrix classes, on .venv-thesis-pr3524 (fork 5c07151 = 35e81b1 + #3524,
# engine 4f42e05), plus the fully-CSR cold variant DE_EVAL / DE_NODENSE_EVAL on the
# parametric problems. The upstream baselines in results/thesis/ are reused.
# Same hygiene as run_thesis_final.sh; every step resumes.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
export BENCH_SLOW_REPS=${BENCH_SLOW_REPS:-10}
OUT=${OUT:-results/thesis-pr3524}
FORK=.venv-thesis-pr3524/bin/python
mkdir -p "$OUT"

# The 4 slow problems, every problem where dense blocks move the time by > 10%
# (Holm-significant), the 8 parametric problems, and every problem where #3524 rewrites
# a chain (OptimalAdvertising, QuantumHilbertMatrix, SDPSegfault1132, SlowPruning,
# UnconstrainedQP).
PARAM=ConvexPlasticity,FactorCovarianceModel,ParamConeMatrixStuffing,ParamSmallMatrixStuffing
PARAM=$PARAM,ParametrizedQPBenchmark,SVMWithL1Regularization
PARAM=$PARAM,SimpleFullyParametrizedLPBenchmark,SimpleScalarParametrizedLPBenchmark
COLD=$PARAM,CVaRBenchmark,ConeMatrixStuffingBench,HuberRegression,LeastSquares
COLD=$COLD,OptimalAdvertising,QuantumHilbertMatrix,SDPSegfault1132Benchmark
COLD=$COLD,SimpleLPBenchmark,SimpleQPBenchmark,SlowPruningBenchmark,SmallMatrixStuffing
COLD=$COLD,UnconstrainedQP,Yitzhaki
COLD=${COLD_SET:-$COLD}
PARAM=${PARAM_SET:-$PARAM}

$FORK thesis_final_benchmarks.py verify --set "$COLD" --out "$OUT/verify_suite.json"

if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

$FORK thesis_final_benchmarks.py time --set "$COLD" --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out "$OUT/cold_fork.json"
$FORK thesis_final_benchmarks.py time --set "$PARAM" --kind cold \
  --targets DE_EVAL,DE_NODENSE_EVAL --out "$OUT/cold_eval_fork.json"
$FORK thesis_final_benchmarks.py time --set "$PARAM" --kind warm \
  --targets de_cached,de_cached_nodense,de_cached_rebuild,de_cached_nodense_rebuild \
  --out "$OUT/warm_fork.json"
$FORK thesis_final_benchmarks.py memory --set "$COLD" --kind cold \
  --targets DIFFENGINE,DE_NODENSE --out "$OUT/memory_cold_fork.json"
$FORK thesis_final_benchmarks.py memory --set "$PARAM" --kind cold \
  --targets DE_EVAL,DE_NODENSE_EVAL --out "$OUT/memory_cold_eval_fork.json"

# Old-build rows first, so the rerun rows (later files) replace them.
T=results/thesis
$FORK thesis_stats.py $T/verify_*.json $T/cold_*.json $T/warm_*.json $T/nondpp_*.json \
  $T/sensitivity_*.json $T/scaling_*.json $T/memory_*.json \
  "$OUT"/verify_*.json "$OUT"/cold_*.json "$OUT"/warm_*.json "$OUT"/memory_*.json \
  --out "$OUT/summary.md"
$FORK compare_builds.py --old $T --new "$OUT" --out "$OUT/compare.md"
