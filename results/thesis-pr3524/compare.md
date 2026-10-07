# Old build vs new build

- old: `results/thesis`: cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129), engine 4f42e05
- new: `results/thesis-pr3524`: cvxpy 0.1.0.dev4045+g5c071510a (5c071510a), engine 4f42e05


## `DE_NODENSE` (cold)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| CVaRBenchmark | 2.7643 | 2.7562 | 0.997 | 1.000 |
| ConeMatrixStuffingBench | 1.9123 | 1.9095 | 0.999 | 1.000 |
| ConvexPlasticity | 0.0974 | 0.0978 | 1.004 | 0.040 |
| FactorCovarianceModel | 0.3475 | 0.3469 | 0.998 | 1.000 |
| HuberRegression | 0.9902 | 1.0035 | 1.013 | 2.9e-05 |
| LeastSquares | 0.8826 | 0.8968 | 1.016 | 1.4e-06 |
| OptimalAdvertising | 0.8374 | 0.8355 | 0.998 | 1.000 |
| ParamConeMatrixStuffing | 0.0273 | 0.0273 | 1.001 | 1.000 |
| ParamSmallMatrixStuffing | 0.0403 | 0.0403 | 1.001 | 1.000 |
| ParametrizedQPBenchmark | 0.7173 | 0.7166 | 0.999 | 1.000 |
| QuantumHilbertMatrix | 0.6590 | 0.5065 | 0.769 | 1.4e-06 |
| SDPSegfault1132Benchmark | 3.5380 | 3.2929 | 0.931 | 1.4e-06 |
| SVMWithL1Regularization | 0.7358 | 0.7465 | 1.015 | 1.6e-05 |
| SimpleFullyParametrizedLPBenchmark | 0.1094 | 0.1094 | 1.000 | 1.000 |
| SimpleLPBenchmark | 1.4963 | 1.4947 | 0.999 | 1.000 |
| SimpleQPBenchmark | 0.8960 | 0.9117 | 1.018 | 1.8e-05 |
| SimpleScalarParametrizedLPBenchmark | 0.2137 | 0.2136 | 1.000 | 1.000 |
| SlowPruningBenchmark | 0.4051 | 0.4156 | 1.026 | 1.7e-05 |
| SmallMatrixStuffing | 1.3464 | 1.3474 | 1.001 | 1.000 |
| UnconstrainedQP | 0.4897 | 0.0221 | 0.045 | 1.4e-06 |
| Yitzhaki | 0.2536 | 0.2534 | 0.999 | 1.000 |

Geometric mean new/old **0.853** (95% CI 0.627–1.004).

## `DIFFENGINE` (cold)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| CVaRBenchmark | 4.2040 | 4.2724 | 1.016 | 4.7e-04 |
| ConeMatrixStuffingBench | 0.6339 | 0.6335 | 0.999 | 1.000 |
| ConvexPlasticity | 0.4950 | 0.4986 | 1.007 | 0.859 |
| FactorCovarianceModel | 0.1651 | 0.1649 | 0.998 | 0.378 |
| HuberRegression | 0.4768 | 0.4748 | 0.996 | 1.000 |
| LeastSquares | 0.4160 | 0.4159 | 1.000 | 1.000 |
| OptimalAdvertising | 0.8897 | 0.8912 | 1.002 | 1.000 |
| ParamConeMatrixStuffing | 0.0224 | 0.0225 | 1.004 | 0.859 |
| ParamSmallMatrixStuffing | 0.0329 | 0.0329 | 1.000 | 1.000 |
| ParametrizedQPBenchmark | 0.7253 | 0.7248 | 0.999 | 1.000 |
| QuantumHilbertMatrix | 0.6438 | 0.4932 | 0.766 | 1.4e-06 |
| SDPSegfault1132Benchmark | 2.0241 | 1.8987 | 0.938 | 1.4e-06 |
| SVMWithL1Regularization | 0.3584 | 0.3620 | 1.010 | 8.8e-05 |
| SimpleFullyParametrizedLPBenchmark | 0.1113 | 0.1110 | 0.997 | 0.118 |
| SimpleLPBenchmark | 1.0803 | 1.0986 | 1.017 | 1.4e-05 |
| SimpleQPBenchmark | 0.4313 | 0.4325 | 1.003 | 0.378 |
| SimpleScalarParametrizedLPBenchmark | 0.2195 | 0.2197 | 1.001 | 1.000 |
| SlowPruningBenchmark | 0.3918 | 0.3930 | 1.003 | 7.0e-04 |
| SmallMatrixStuffing | 0.4986 | 0.4985 | 1.000 | 1.000 |
| UnconstrainedQP | 22.9297 | 0.0159 | 6.9e-04 | 1.4e-06 |
| Yitzhaki | 0.1337 | 0.1333 | 0.997 | 0.085 |

Geometric mean new/old **0.698** (95% CI 0.345–1.002).

## `de_cached` (warm)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| ConvexPlasticity | 0.2034 | 0.2034 | 1.000 | 1.000 |
| FactorCovarianceModel | 0.0813 | 0.0806 | 0.992 | 0.044 |
| ParamConeMatrixStuffing | 0.0003 | 0.0003 | 1.002 | 1.000 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0005 | 1.005 | 1.000 |
| ParametrizedQPBenchmark | 0.4246 | 0.4232 | 0.997 | 1.000 |
| SVMWithL1Regularization | 0.1525 | 0.1524 | 0.999 | 1.000 |
| SimpleFullyParametrizedLPBenchmark | 0.0526 | 0.0526 | 1.002 | 0.044 |
| SimpleScalarParametrizedLPBenchmark | 0.1040 | 0.1042 | 1.001 | 1.000 |

Geometric mean new/old **1.000** (95% CI 0.997–1.002).

## `de_cached_nodense` (warm)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| ConvexPlasticity | 0.0023 | 0.0023 | 1.010 | 0.001 |
| FactorCovarianceModel | 0.0874 | 0.0871 | 0.996 | 2.0e-04 |
| ParamConeMatrixStuffing | 0.0003 | 0.0003 | 0.996 | 1.000 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0005 | 0.993 | 0.176 |
| ParametrizedQPBenchmark | 0.4250 | 0.4164 | 0.980 | 0.012 |
| SVMWithL1Regularization | 0.1635 | 0.1634 | 1.000 | 1.000 |
| SimpleFullyParametrizedLPBenchmark | 0.0525 | 0.0526 | 1.003 | 1.8e-04 |
| SimpleScalarParametrizedLPBenchmark | 0.1040 | 0.1040 | 1.000 | 1.000 |

Geometric mean new/old **0.997** (95% CI 0.991–1.003).

## `de_cached_nodense_rebuild` (warm)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| ConvexPlasticity | 0.0655 | 0.0655 | 1.000 | 1.000 |
| FactorCovarianceModel | 0.3148 | 0.3150 | 1.000 | 1.000 |
| ParamConeMatrixStuffing | 0.0027 | 0.0027 | 1.005 | 1.000 |
| ParamSmallMatrixStuffing | 0.0042 | 0.0042 | 1.011 | 0.091 |
| ParametrizedQPBenchmark | 0.5611 | 0.5718 | 1.019 | 0.885 |
| SVMWithL1Regularization | 0.6070 | 0.6072 | 1.000 | 1.000 |
| SimpleFullyParametrizedLPBenchmark | 0.0840 | 0.0840 | 1.000 | 1.000 |
| SimpleScalarParametrizedLPBenchmark | 0.1667 | 0.1668 | 1.000 | 1.000 |

Geometric mean new/old **1.004** (95% CI 1.001–1.010).

## `de_cached_rebuild` (warm)

| problem | old median (s) | new median (s) | new/old | p (Holm) |
|---|---:|---:|---:|---:|
| ConvexPlasticity | 0.4117 | 0.4135 | 1.004 | 0.006 |
| FactorCovarianceModel | 0.1292 | 0.1290 | 0.999 | 0.407 |
| ParamConeMatrixStuffing | 0.0027 | 0.0027 | 0.999 | 1.000 |
| ParamSmallMatrixStuffing | 0.0040 | 0.0041 | 1.004 | 0.407 |
| ParametrizedQPBenchmark | 0.5547 | 0.5626 | 1.014 | 0.622 |
| SVMWithL1Regularization | 0.2716 | 0.2717 | 1.000 | 1.000 |
| SimpleFullyParametrizedLPBenchmark | 0.0839 | 0.0842 | 1.004 | 0.054 |
| SimpleScalarParametrizedLPBenchmark | 0.1666 | 0.1667 | 1.001 | 1.000 |

Geometric mean new/old **1.003** (95% CI 1.000–1.007).
