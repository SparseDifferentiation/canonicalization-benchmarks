#!/usr/bin/env bash
# The 25-problem CVXPY benchmark suite (github.com/cvxpy/benchmarks), pinned.
set -euo pipefail
cd "$(dirname "$0")/.."
SUITE_COMMIT=${SUITE_COMMIT:-77c7fa4f59c4fd255aa2a45a9b5a2c5994ebe10a}
[ -d cvxpy_benchmarks/.git ] || git clone https://github.com/cvxpy/benchmarks cvxpy_benchmarks
git -C cvxpy_benchmarks fetch -q origin
git -C cvxpy_benchmarks checkout -q "$SUITE_COMMIT"
echo "cvxpy/benchmarks at $(git -C cvxpy_benchmarks rev-parse --short HEAD)"
