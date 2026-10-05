#!/usr/bin/env bash
# .venv-upstream: stock cvxpy 1.9.2 for the CPP/SCIPY/COO baselines (*_ND, dpp*,
# nodpp_*). It cannot share .venv-thesis: the fork forces parametrized problems onto
# DIFFENGINE on the ignore_dpp path, and cvxpy 1.9.2 pins sparsediffpy<0.4.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.venv-upstream
uv venv --python "${PYTHON:-3.13}" "$VENV"
uv pip install --python "$VENV/bin/python" cvxpy==1.9.2 numpy==2.5.3 scipy==1.18.1 clarabel==0.11.1 threadpoolctl==3.7.0
"$VENV/bin/python" -c "import cvxpy; print('cvxpy', cvxpy.__version__)"
