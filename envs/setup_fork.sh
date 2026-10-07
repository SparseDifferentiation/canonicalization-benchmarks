#!/usr/bin/env bash
# .venv-thesis: the cvxpy fork with the ablation switches + SparseDiffPy compiled
# against the pinned SparseDiffEngine commit. Everything comes from public GitHub
# commits; the engine commit is stamped into the venv so thesis_final_benchmarks.py
# can refuse to time a different build (the PyPI wheel has no stamp).
#
#   envs/setup_fork.sh            # from the repo root; needs uv, git, cmake, a C compiler
set -euo pipefail
cd "$(dirname "$0")/.."

PYTHON=${PYTHON:-3.13}
CVXPY_COMMIT=${CVXPY_COMMIT:-35e81b1296627ba8ee06caf2d79e055287152d7e}  # Transurgeon/cvxpy@thesis-ablation
SDP_COMMIT=${SDP_COMMIT:-9e0246e}      # SparseDifferentiation/SparseDiffPy (bindings)
ENGINE_COMMIT=${ENGINE_COMMIT:-4f42e05} # SparseDifferentiation/SparseDiffEngine (#125 + linear CSR fill)
VENV=${VENV:-.venv-thesis}
SRC=.build/SparseDiffPy

uv venv --python "$PYTHON" "$VENV"
uv pip install --python "$VENV/bin/python" \
  "cvxpy @ git+https://github.com/Transurgeon/cvxpy.git@${CVXPY_COMMIT}" \
  numpy==2.5.3 scipy==1.18.1 clarabel==0.11.1 threadpoolctl==3.7.0

if [ ! -d "$SRC/.git" ]; then
  git clone https://github.com/SparseDifferentiation/SparseDiffPy.git "$SRC"
fi
git -C "$SRC" fetch -q origin
git -C "$SRC" checkout -q "$SDP_COMMIT"
git -C "$SRC" submodule update --init -q
git -C "$SRC/SparseDiffEngine" fetch -q origin
git -C "$SRC/SparseDiffEngine" checkout -q "$ENGINE_COMMIT"
uv pip install --python "$VENV/bin/python" --reinstall --no-deps "$SRC"

git -C "$SRC/SparseDiffEngine" rev-parse --short=7 HEAD > "$VENV/ENGINE_COMMIT"
"$VENV/bin/python" - <<'PY'
import importlib.metadata as m, cvxpy, sparsediffpy  # noqa: F401
print("cvxpy", m.version("cvxpy"), "| sparsediffpy", m.version("sparsediffpy"))
PY
echo "engine $(cat $VENV/ENGINE_COMMIT) stamped into $VENV/ENGINE_COMMIT"
