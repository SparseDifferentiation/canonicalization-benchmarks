"""
Scaled copies of the 25 cvxpy/benchmarks problems, built from the suite's own source.

Each suite class hard-codes its sizes. ``scaled_class(name, s, density)`` takes the
class's source, replaces its size literals with scaled ones (and, for five problems,
masks the data matrix to a given density), and executes it in the module's own
namespace, so the copy is the suite code with different numbers.

The scale ``s`` multiplies the problem data, not one dimension: wherever nnz(A) grows
with the square of a size knob (dense data matrices, all-pairs constructions), that knob
is multiplied by sqrt(s) (SDPSegfault1132, cubic in n: s^(1/3)), so nnz(A) grows by
about s in every family. The exact
dimensions of each instance are recorded by the runner. QuantumHilbertMatrix has only
the number of qubits as a knob: s = 1/2 and 2 map to 2 and 4 qubits.

Data are generated with the suite's fixed seeds; there are no seeds here (the seed of a
random instance moves canonicalization time by < 1%, see results/thesis).

Specs, as accepted by thesis_extra_problems.make_class:
    scaled:cls=HuberRegression:s=2
    scaled:cls=LeastSquares:density=0.05
"""
from __future__ import annotations

import importlib
import inspect
import math
import sys
import textwrap

import numpy as np

import run_backend_benchmarks as rbb

# class -> [(text in the suite source, replacement[, occurrences])]. Each text must occur
# exactly that many times (default once), so a change in the suite source fails loudly.
RULES = {
    "CVaRBenchmark": [("np.random.randn(131072, 192)", "np.random.randn(int(131072 * _S), 192)", 2)],
    "FactorCovarianceModel": [("n = 25000", "n = int(25000 * _S)")],
    "Yitzhaki": [("T = 300", "T = int(round(300 * math.sqrt(_S)))")],
    "Murray": [("T = 700", "T = int(round(700 * math.sqrt(_S)))")],
    "Cajas": [("T = 800", "T = int(round(800 * math.sqrt(_S)))")],
    "ConvexPlasticity": [("deps_dummy = np.full((4000, 4), particular_deps)",
                          "deps_dummy = np.full((max(4000, int(3000 * _S)), 4), particular_deps)"),
                         ("N = 3000", "N = int(3000 * _S)")],
    "HuberRegression": [("n = 3000", "n = int(round(3000 * math.sqrt(_S)))"),
                        ("X = np.random.randn(n, SAMPLES)", "X = _mask(np.random.randn(n, SAMPLES))")],
    "ConeMatrixStuffingBench": [("m = 5000\n        n = 5000",
                                 "m = 2 * int(round(2500 * math.sqrt(_S)))\n        n = m")],
    "ParamConeMatrixStuffing": [("m = 200\n        n = 200",
                                 "m = 2 * int(round(100 * math.sqrt(_S)))\n        n = m")],
    "SmallMatrixStuffing": [("m = 4000\n        n = 4000",
                             "m = 2 * int(round(2000 * math.sqrt(_S)))\n        n = m")],
    "ParamSmallMatrixStuffing": [("m = 300\n        n = 300",
                                  "m = 2 * int(round(150 * math.sqrt(_S)))\n        n = m")],
    "OptimalAdvertising": [("n = 1000", "n = int(1000 * _S)")],
    "QuantumHilbertMatrix": [("N = 3  # number of qubits", "N = {0.5: 2, 1: 3, 2: 4}[_S]")],
    "SDPSegfault1132Benchmark": [("n = 100\n", "n = int(round(100 * _S ** (1 / 3)))\n")],
    "SemidefiniteProgramming": [("n = 200", "n = int(round(200 * math.sqrt(_S)))")],
    "SimpleLPBenchmark": [("n = int(1e7)", "n = int(1e7 * _S)")],
    "SimpleFullyParametrizedLPBenchmark": [("n = int(1e6)", "n = int(1e6 * _S)")],
    "SimpleScalarParametrizedLPBenchmark": [("n = int(2e6)", "n = int(2e6 * _S)")],
    "SimpleQPBenchmark": [("m = 8000\n        n = 1600",
                           "m = int(round(8000 * math.sqrt(_S)))\n        n = int(round(1600 * math.sqrt(_S)))"),
                          ("G = np.random.randn(m, n)", "G = _mask(np.random.randn(m, n))")],
    "ParametrizedQPBenchmark": [("m = 6000\n        n = 2400",
                                 "m = int(round(6000 * math.sqrt(_S)))\n        n = int(round(2400 * math.sqrt(_S)))")],
    "LeastSquares": [("m = 7000\n        n = 2000",
                      "m = int(round(7000 * math.sqrt(_S)))\n        n = int(round(2000 * math.sqrt(_S)))"),
                     ("A = np.random.randn(m, n)", "A = _mask(np.random.randn(m, n))")],
    "UnconstrainedQP": [("N_s = 7", "N_s = max(1, int(round(7 * math.sqrt(_S))))")],
    "SlowPruningBenchmark": [("s = 4000", "s = int(4000 * _S)")],
    "SVMWithL1Regularization": [("m = 25000", "m = int(25000 * _S)"),
                                ("X = np.random.normal(0, 5, size=(m, n))",
                                 "X = _mask(np.random.normal(0, 5, size=(m, n)))")],
    "TvInpainting": [("np.random.randn(512, 512, 3)",
                      "np.random.randn(int(round(512 * math.sqrt(_S))), int(round(512 * math.sqrt(_S))), 3)")],
}
# The density knob: the data matrix is multiplied by a 0/1 mask (kept as a dense numpy
# array, as in the lasso grid), drawn from its own generator so the data are unchanged.
DENSITY_PROBLEMS = ("LeastSquares", "HuberRegression", "SVMWithL1Regularization",
                    "SimpleQPBenchmark")


def _suite():
    return {c: m for m, c, err in rbb.discover() if c is not None}


def scaled_class(name, s=1.0, density=1.0):
    s, density = float(s), float(density)
    module = _suite()[name]
    sys.path.insert(0, str(rbb.BENCH_DIR))
    mod = importlib.import_module(module)
    src = textwrap.dedent(inspect.getsource(getattr(mod, name)))
    for old, new, *count in RULES[name]:
        if "_mask(" in new and density == 1.0:
            continue
        if src.count(old) != (count[0] if count else 1):
            raise ValueError(f"{name}: unexpected count of '{old}' in the suite source")
        src = src.replace(old, new)
    if density != 1.0 and name not in DENSITY_PROBLEMS:
        raise ValueError(f"{name} has no density knob")
    rng = np.random.default_rng(12345)
    ns = dict(vars(mod))
    ns.update(_S=s, math=math,
              _mask=lambda M: M * (rng.random(M.shape) < density))
    exec(compile(src, f"<scaled {name} s={s} density={density}>", "exec"), ns)
    return ns[name]


def build(cls, s=1.0, density=1.0):
    inst = scaled_class(cls, s, density)()
    inst.setup()
    return rbb._find_problem(inst)


# --------------------------------------------------------------------------- #
# Sets
# --------------------------------------------------------------------------- #
ALL25 = sorted(RULES)
SCALED25 = [f"scaled:cls={c}:s={s}" for c in ALL25 for s in (0.5, 2)]
# Ten families at five sizes. s = 1/2, 2 are in SCALED25 and s = 1 is the suite itself;
# lasso (not a suite problem) runs at five n.
FAMILIES10 = ["HuberRegression", "FactorCovarianceModel", "OptimalAdvertising",
              "SVMWithL1Regularization", "LeastSquares", "SimpleQPBenchmark", "Yitzhaki",
              "CVaRBenchmark", "SemidefiniteProgramming"]
FAMILY_EXTRA = ([f"scaled:cls={c}:s={s}" for c in FAMILIES10 for s in (0.25, 4)]
                + [f"lasso:variant=free:n={n}:seed=0" for n in (250, 500, 1000, 2000, 4000)])
DENSITIES = (0.01, 0.05, 0.2, 0.5)
DENSITY = [f"scaled:cls={c}:density={d}" for c in DENSITY_PROBLEMS for d in DENSITIES]
SETS = {"scaled25": SCALED25, "families": FAMILY_EXTRA, "density": DENSITY}
