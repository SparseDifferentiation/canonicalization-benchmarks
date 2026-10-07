#!/usr/bin/env bash
# Scaling and density study (thesis_scaled_problems.py): the 25 suite problems at
# s = 1/2 and 2, ten families at s = 1/4 and 4 (s = 1/2, 1, 2 come from the other
# runs) plus lasso at five n, and five problems at four densities (density 1 is the
# suite). 89 instances, cold only, 5 replicates each, no seeds.
# Fork: .venv-thesis-pr3524 (fork + CVXPY #3524, engine 4f42e05); baselines: cvxpy 1.9.2.
# Same hygiene as run_thesis_final.sh; every step resumes.
set -euo pipefail
cd "$(dirname "$0")"
if [ "$(uname)" = Darwin ] && [ -z "${CAFFEINATED:-}" ]; then
  exec env CAFFEINATED=1 caffeinate -dimsu "$0" "$@"
fi
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05}
export BENCH_REPS=${BENCH_REPS:-5}
OUT=${OUT:-results/thesis-scaling}
FORK=.venv-thesis-pr3524/bin/python
UP=.venv-upstream/bin/python
SETS=${SETS:-scaled25 families density}
mkdir -p "$OUT"

for set in $SETS; do
  $FORK thesis_final_benchmarks.py verify --set "$set" --out "$OUT/verify_$set.json"
done

if [ "$(uname)" = Darwin ]; then
  until pmset -g batt | grep -q "AC Power"; do
    echo "waiting for AC power before timing ($(date +%H:%M))"; sleep 60
  done
fi

for set in $SETS; do
  $FORK thesis_final_benchmarks.py time --set "$set" --kind cold \
    --targets DIFFENGINE,DE_NODENSE --out "$OUT/${set}_fork.json"
  $UP thesis_final_benchmarks.py time --set "$set" --kind cold \
    --targets CPP_ND,SCIPY_ND,COO_ND --out "$OUT/${set}_upstream.json"
done

# Suite rows (s = 1, density 1) and the lasso grid come from the earlier runs.
T=results/thesis
P=results/thesis-pr3524
$FORK thesis_stats.py $T/verify_*.json $T/cold_*.json $T/sensitivity_*.json \
  $P/verify_*.json $P/cold_fork.json "$OUT"/*.json --out "$OUT/summary.md"
