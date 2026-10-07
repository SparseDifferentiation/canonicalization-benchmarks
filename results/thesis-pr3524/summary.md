# Final-deposit experiments: summary

## Environments

- `cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `cold_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `warm_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `warm_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `nondpp_cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `nondpp_cold_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `nondpp_warm_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `nondpp_warm_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `sensitivity_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `sensitivity_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `scaling_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `scaling_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_warm_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `cold_eval_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `warm_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_eval_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']

## Correctness gate: (P, c, A, b) vs the reference (rel. 1e-9)

| problem | reference | checks passed | failures |
|---|---|---:|---|
| CVaRBenchmark | CPP | 4/4 | – |
| Cajas | CPP | 4/4 | – |
| ConeMatrixStuffingBench | CPP | 4/4 | – |
| ConvexPlasticity | CPP_EVAL | 20/20 | – |
| FactorCovarianceModel | CPP_EVAL | 20/20 | – |
| HuberRegression | CPP | 4/4 | – |
| LeastSquares | CPP | 4/4 | – |
| Murray | CPP | 4/4 | – |
| OptimalAdvertising | CPP | 4/4 | – |
| ParamConeMatrixStuffing | CPP_EVAL | 20/20 | – |
| ParamSmallMatrixStuffing | CPP_EVAL | 20/20 | – |
| ParametrizedQPBenchmark | CPP_EVAL | 20/20 | – |
| QuantumHilbertMatrix | CPP | 4/4 | – |
| SDPSegfault1132Benchmark | CPP | 4/4 | – |
| SVMWithL1Regularization | CPP_EVAL | 20/20 | – |
| SemidefiniteProgramming | CPP | 4/4 | – |
| SimpleFullyParametrizedLPBenchmark | CPP_EVAL | 20/20 | – |
| SimpleLPBenchmark | CPP | 4/4 | – |
| SimpleQPBenchmark | CPP | 4/4 | – |
| SimpleScalarParametrizedLPBenchmark | CPP_EVAL | 20/20 | – |
| SlowPruningBenchmark | CPP | 4/4 | – |
| SmallMatrixStuffing | CPP | 4/4 | – |
| TvInpainting | CPP | 4/4 | – |
| UnconstrainedQP | CPP | 4/4 | – |
| Yitzhaki | CPP | 4/4 | – |
| factor_cov:variant=dpp:n=5000:seed=0 | CPP_EVAL | 16/16 | – |
| factor_cov:variant=free:n=5000:seed=0 | CPP | 4/4 | – |
| factor_cov:variant=nondpp:n=5000:seed=0 | CPP_EVAL | 16/16 | – |
| lasso:variant=dpp:n=1000:seed=0 | CPP_EVAL | 16/16 | – |
| lasso:variant=free:n=1000:seed=0 | CPP | 4/4 | – |
| lasso:variant=nondpp:n=1000:seed=0 | CPP_EVAL | 16/16 | – |

0 failed (problem, target) checks.

Passed with a footnote (NaN in the problem data):

- OptimalAdvertising `first:DIFFENGINE`: NaN where the reference has a zero (1 in b); every finite entry identical
- OptimalAdvertising `first:DE_NODENSE`: NaN where the reference has a zero (1 in b); every finite entry identical

## Table 4.1: first canonicalization, mean ± std (s)

| problem | n | m | nnz(A) | CPP_ND | SCIPY_ND | COO_ND | diffengine | best | ratio | p (Holm) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| CVaRBenchmark | 131841 | 263681 | 25691649 | 7.205 ± 0.017 | 6.505 ± 0.020 | 6.499 ± 0.033 | 4.273 ± 0.055 | COO_ND | 0.658 | 1.7e-06 |
| Cajas | 2450 | 640851 | 1960900 | 3.554 ± 0.030 | 0.683 ± 0.003 | 0.691 ± 0.003 | 0.201 ± 0.002 | SCIPY_ND | 0.292 | 1.7e-06 |
| ConeMatrixStuffingBench | 5000 | 5000 | 5000 | 2.484 ± 0.020 | 2.145 ± 0.015 | 3.499 ± 0.012 | 0.634 ± 0.004 | SCIPY_ND | 0.295 | 1.7e-06 |
| ConvexPlasticity | 33000 | 36000 | 72000 | 0.079 ± 0.001 | 0.075 ± 7.7e-04 | 0.072 ± 0.001 | 0.499 ± 0.007 | COO_ND | 6.943 | 1.7e-06 |
| FactorCovarianceModel | 75250 | 75252 | 6450250 | 1.205 ± 0.004 | 1.161 ± 0.007 | 1.151 ± 0.004 | 0.165 ± 6.3e-04 | COO_ND | 0.143 | 1.7e-06 |
| HuberRegression | 16500 | 13500 | 13527000 | 2.746 ± 0.017 | 2.858 ± 0.018 | 2.804 ± 0.015 | 0.475 ± 0.002 | CPP_ND | 0.173 | 1.7e-06 |
| LeastSquares | 9000 | 7000 | 14007000 | 2.402 ± 0.015 | 2.903 ± 0.016 | 2.939 ± 0.015 | 0.416 ± 0.002 | CPP_ND | 0.173 | 1.7e-06 |
| Murray | 245400 | 490051 | 1503700 | 1.235 ± 0.010 | 1.225 ± 0.007 | 1.221 ± 0.007 | 1.164 ± 0.002 | COO_ND | 0.955 | 1.7e-06 |
| OptimalAdvertising | 250250 | 251750 | 1000500 | 2.577 ± 0.010 | 0.596 ± 0.007 | 0.535 ± 0.002 | 0.889 ± 0.007 | COO_ND | 1.667 | 1.7e-06 |
| ParamConeMatrixStuffing | 200 | 200 | 200 | 0.043 ± 2.6e-04 | 0.072 ± 3.5e-04 | 0.089 ± 4.8e-04 | 0.022 ± 1.3e-04 | CPP_ND | 0.526 | 1.7e-06 |
| ParamSmallMatrixStuffing | 300 | 300 | 300 | 0.063 ± 5.4e-04 | 0.128 ± 4.8e-04 | 0.113 ± 6.9e-04 | 0.033 ± 1.8e-04 | CPP_ND | 0.518 | 1.7e-06 |
| ParametrizedQPBenchmark | 8400 | 10800 | 14410800 | 2.971 ± 0.031 | 3.011 ± 0.006 | 2.991 ± 0.005 | 0.730 ± 0.048 | CPP_ND | 0.245 | 1.7e-06 |
| QuantumHilbertMatrix | 6176 | 6176 | 81072 | 1.060 ± 0.002 | 0.804 ± 0.006 | 0.789 ± 0.009 | 0.492 ± 0.003 | COO_ND | 0.627 | 1.7e-06 |
| SDPSegfault1132Benchmark | 4951 | 14951 | 1014157 | 7.979 ± 0.023 | 1.510 ± 0.038 | 8.929 ± 0.084 | 1.903 ± 0.014 | SCIPY_ND | 1.267 | 1.7e-06 |
| SVMWithL1Regularization | 26002 | 51001 | 12577501 | 2.782 ± 0.012 | 2.625 ± 0.006 | 2.740 ± 0.009 | 0.363 ± 0.004 | SCIPY_ND | 0.138 | 1.7e-06 |
| SemidefiniteProgramming | 20100 | 20220 | 2432100 | 1.169 ± 0.006 | 0.633 ± 0.002 | 0.996 ± 0.008 | 0.396 ± 0.003 | SCIPY_ND | 0.629 | 1.7e-06 |
| SimpleFullyParametrizedLPBenchmark | 1000000 | 2000000 | 2000000 | 0.613 ± 0.002 | 0.556 ± 0.001 | 0.525 ± 0.001 | 0.111 ± 2.3e-04 | COO_ND | 0.211 | 1.7e-06 |
| SimpleLPBenchmark | 10000000 | 20000000 | 20000000 | 6.844 ± 0.011 | 6.329 ± 0.027 | 5.984 ± 0.016 | 1.098 ± 0.007 | COO_ND | 0.184 | 1.7e-06 |
| SimpleQPBenchmark | 1600 | 8020 | 12832000 | 2.876 ± 0.010 | 2.933 ± 0.006 | 2.930 ± 0.006 | 0.433 ± 0.003 | CPP_ND | 0.150 | 1.7e-06 |
| SimpleScalarParametrizedLPBenchmark | 2000000 | 4000000 | 4000000 | 1.266 ± 0.005 | 1.149 ± 0.005 | 1.087 ± 0.003 | 0.220 ± 7.4e-04 | COO_ND | 0.202 | 1.7e-06 |
| SlowPruningBenchmark | 402000 | 400000 | 8400000 | 1.795 ± 0.013 | 2.179 ± 0.004 | 2.147 ± 0.007 | 0.393 ± 7.8e-04 | CPP_ND | 0.220 | 1.7e-06 |
| SmallMatrixStuffing | 4000 | 4000 | 4000 | 1.664 ± 0.014 | 1.818 ± 0.008 | 2.490 ± 0.012 | 0.500 ± 0.006 | CPP_ND | 0.299 | 1.7e-06 |
| TvInpainting | 1047553 | 2614279 | 3630958 | 0.920 ± 0.003 | 0.908 ± 0.008 | 0.814 ± 0.002 | 0.244 ± 6.6e-04 | COO_ND | 0.299 | 1.7e-06 |
| UnconstrainedQP | 289 | 1009 | 18649 | 1.951 ± 0.005 | 1.983 ± 0.008 | 2.434 ± 0.011 | 0.016 ± 9.4e-05 | CPP_ND | 0.008 | 1.7e-06 |
| Yitzhaki | 44900 | 89751 | 4574800 | 0.925 ± 0.010 | 0.979 ± 0.011 | 1.000 ± 0.019 | 0.133 ± 4.5e-04 | CPP_ND | 0.145 | 1.7e-06 |

diffengine fastest on 22/25; geometric-mean ratio to the best backend **0.317** (95% CI 0.198–0.501), Wilcoxon p = 1.2e-04; 22 problems significantly faster, 3 significantly slower (Holm, 5%).

## Ablation (jury J1b, Legrain ii)

### Dense blocks off for constant data (parametric matrices stay dense): `DE_NODENSE` / `DIFFENGINE` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 4.2724 | 0.645 | 1.7e-06 | 20/20 |
| Cajas | 0.2039 | 0.2000 | 1.020 | 4.1e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 0.6335 | 3.014 | 1.7e-06 | 20/20 |
| ConvexPlasticity | 0.0978 | 0.4986 | 0.196 | 1.7e-06 | 20/20 |
| FactorCovarianceModel | 0.3469 | 0.1649 | 2.104 | 1.7e-06 | 20/20 |
| HuberRegression | 1.0035 | 0.4748 | 2.114 | 1.7e-06 | 20/20 |
| LeastSquares | 0.8968 | 0.4159 | 2.156 | 1.7e-06 | 20/20 |
| Murray | 1.1744 | 1.1633 | 1.010 | 1.7e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 0.8912 | 0.938 | 1.7e-06 | 20/20 |
| ParamConeMatrixStuffing | 0.0273 | 0.0225 | 1.215 | 1.7e-06 | 20/20 |
| ParamSmallMatrixStuffing | 0.0403 | 0.0329 | 1.226 | 1.7e-06 | 20/20 |
| ParametrizedQPBenchmark | 0.7166 | 0.7248 | 0.989 | 0.925 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 0.4932 | 1.027 | 1.7e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 1.8987 | 1.734 | 1.7e-06 | 20/20 |
| SVMWithL1Regularization | 0.7465 | 0.3620 | 2.062 | 1.7e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 0.3979 | 0.997 | 0.327 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1094 | 0.1110 | 0.986 | 1.7e-06 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 1.0986 | 1.361 | 1.7e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 0.4325 | 2.108 | 1.7e-06 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2136 | 0.2197 | 0.973 | 1.7e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 0.3930 | 1.057 | 1.7e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 0.4985 | 2.703 | 1.7e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.2437 | 0.979 | 1.7e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 0.0159 | 1.397 | 1.7e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.1333 | 1.901 | 1.7e-06 | 20/20 |

Geometric-mean ratio **1.269** (bootstrap 95% CI 1.014–1.551), Wilcoxon signed-rank p = 0.014, 8/25 problems below 1, 23/25 significant at 5% after Holm.

### Fully CSR, parameter-free problems: `DE_NODENSE` / `DIFFENGINE` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 4.2724 | 0.645 | 1.2e-06 | 20/20 |
| Cajas | 0.2039 | 0.2000 | 1.020 | 2.8e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 0.6335 | 3.014 | 1.2e-06 | 20/20 |
| HuberRegression | 1.0035 | 0.4748 | 2.114 | 1.2e-06 | 20/20 |
| LeastSquares | 0.8968 | 0.4159 | 2.156 | 1.2e-06 | 20/20 |
| Murray | 1.1744 | 1.1633 | 1.010 | 1.2e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 0.8912 | 0.938 | 1.2e-06 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 0.4932 | 1.027 | 1.2e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 1.8987 | 1.734 | 1.2e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 0.3979 | 0.997 | 0.164 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 1.0986 | 1.361 | 1.2e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 0.4325 | 2.108 | 1.2e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 0.3930 | 1.057 | 1.2e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 0.4985 | 2.703 | 1.2e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.2437 | 0.979 | 1.2e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 0.0159 | 1.397 | 1.2e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.1333 | 1.901 | 1.2e-06 | 20/20 |

Geometric-mean ratio **1.405** (bootstrap 95% CI 1.151–1.725), Wilcoxon signed-rank p = 0.008, 4/17 problems below 1, 16/17 significant at 5% after Holm.

### Fully CSR, parametric problems (parameters evaluated): `DE_NODENSE_EVAL` / `DE_EVAL` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.0967 | 0.4482 | 0.216 | 5.4e-07 | 20/20 |
| FactorCovarianceModel | 0.3464 | 0.1648 | 2.102 | 5.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0331 | 0.0316 | 1.048 | 5.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0510 | 0.0472 | 1.081 | 5.4e-07 | 20/20 |
| ParametrizedQPBenchmark | 0.9462 | 0.4338 | 2.181 | 5.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.7479 | 0.3648 | 2.050 | 5.4e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1450 | 0.1074 | 1.350 | 5.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2887 | 0.2157 | 1.338 | 5.4e-07 | 20/20 |

Geometric-mean ratio **1.195** (bootstrap 95% CI 0.695–1.766), Wilcoxon signed-rank p = 0.195, 1/8 problems below 1, 8/8 significant at 5% after Holm.

### Fully CSR, all problems: `fully CSR` / `dense blocks on` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 4.2724 | 0.645 | 1.7e-06 | 20/20 |
| Cajas | 0.2039 | 0.2000 | 1.020 | 2.8e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 0.6335 | 3.014 | 1.7e-06 | 20/20 |
| ConvexPlasticity | 0.0967 | 0.4482 | 0.216 | 1.7e-06 | 20/20 |
| FactorCovarianceModel | 0.3464 | 0.1648 | 2.102 | 1.7e-06 | 20/20 |
| HuberRegression | 1.0035 | 0.4748 | 2.114 | 1.7e-06 | 20/20 |
| LeastSquares | 0.8968 | 0.4159 | 2.156 | 1.7e-06 | 20/20 |
| Murray | 1.1744 | 1.1633 | 1.010 | 1.7e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 0.8912 | 0.938 | 1.7e-06 | 20/20 |
| ParamConeMatrixStuffing | 0.0331 | 0.0316 | 1.048 | 1.7e-06 | 20/20 |
| ParamSmallMatrixStuffing | 0.0510 | 0.0472 | 1.081 | 1.7e-06 | 20/20 |
| ParametrizedQPBenchmark | 0.9462 | 0.4338 | 2.181 | 1.7e-06 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 0.4932 | 1.027 | 1.7e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 1.8987 | 1.734 | 1.7e-06 | 20/20 |
| SVMWithL1Regularization | 0.7479 | 0.3648 | 2.050 | 1.7e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 0.3979 | 0.997 | 0.164 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1450 | 0.1074 | 1.350 | 1.7e-06 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 1.0986 | 1.361 | 1.7e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 0.4325 | 2.108 | 1.7e-06 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2887 | 0.2157 | 1.338 | 1.7e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 0.3930 | 1.057 | 1.7e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 0.4985 | 2.703 | 1.7e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.2437 | 0.979 | 1.7e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 0.0159 | 1.397 | 1.7e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.1333 | 1.901 | 1.7e-06 | 20/20 |

Geometric-mean ratio **1.334** (bootstrap 95% CI 1.065–1.625), Wilcoxon signed-rank p = 0.002, 5/25 problems below 1, 24/25 significant at 5% after Holm.

### Engine without dense blocks vs CPP_ND: `DE_NODENSE` / `CPP_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 7.2017 | 0.383 | 1.7e-06 | 20/20 |
| Cajas | 0.2039 | 3.5651 | 0.057 | 1.7e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 2.4888 | 0.767 | 1.7e-06 | 20/20 |
| ConvexPlasticity | 0.0978 | 0.0787 | 1.243 | 1.7e-06 | 20/20 |
| FactorCovarianceModel | 0.3469 | 1.2040 | 0.288 | 1.7e-06 | 20/20 |
| HuberRegression | 1.0035 | 2.7422 | 0.366 | 1.7e-06 | 20/20 |
| LeastSquares | 0.8968 | 2.3998 | 0.374 | 1.7e-06 | 20/20 |
| Murray | 1.1744 | 1.2352 | 0.951 | 1.7e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 2.5760 | 0.324 | 1.7e-06 | 20/20 |
| ParamConeMatrixStuffing | 0.0273 | 0.0428 | 0.639 | 1.7e-06 | 20/20 |
| ParamSmallMatrixStuffing | 0.0403 | 0.0634 | 0.635 | 1.7e-06 | 20/20 |
| ParametrizedQPBenchmark | 0.7166 | 2.9594 | 0.242 | 1.7e-06 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 1.0600 | 0.478 | 1.7e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 7.9676 | 0.413 | 1.7e-06 | 20/20 |
| SVMWithL1Regularization | 0.7465 | 2.7809 | 0.268 | 1.7e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 1.1699 | 0.339 | 1.7e-06 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1094 | 0.6128 | 0.179 | 1.7e-06 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 6.8449 | 0.218 | 1.7e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 2.8752 | 0.317 | 1.7e-06 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2136 | 1.2653 | 0.169 | 1.7e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 1.7892 | 0.232 | 1.7e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 1.6656 | 0.809 | 1.7e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.9206 | 0.259 | 1.7e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 1.9500 | 0.011 | 1.7e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.9217 | 0.275 | 1.7e-06 | 20/20 |

Geometric-mean ratio **0.306** (bootstrap 95% CI 0.208–0.426), Wilcoxon signed-rank p = 3.0e-07, 24/25 problems below 1, 25/25 significant at 5% after Holm.

### Engine without dense blocks vs SCIPY_ND: `DE_NODENSE` / `SCIPY_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 6.5052 | 0.424 | 1.7e-06 | 20/20 |
| Cajas | 0.2039 | 0.6840 | 0.298 | 1.7e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 2.1462 | 0.890 | 1.7e-06 | 20/20 |
| ConvexPlasticity | 0.0978 | 0.0745 | 1.313 | 1.7e-06 | 20/20 |
| FactorCovarianceModel | 0.3469 | 1.1601 | 0.299 | 1.7e-06 | 20/20 |
| HuberRegression | 1.0035 | 2.8521 | 0.352 | 1.7e-06 | 20/20 |
| LeastSquares | 0.8968 | 2.8993 | 0.309 | 1.7e-06 | 20/20 |
| Murray | 1.1744 | 1.2234 | 0.960 | 1.7e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 0.5937 | 1.407 | 1.7e-06 | 20/20 |
| ParamConeMatrixStuffing | 0.0273 | 0.0721 | 0.379 | 1.7e-06 | 20/20 |
| ParamSmallMatrixStuffing | 0.0403 | 0.1275 | 0.316 | 1.7e-06 | 20/20 |
| ParametrizedQPBenchmark | 0.7166 | 3.0100 | 0.238 | 1.7e-06 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 0.8033 | 0.631 | 1.7e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 1.4985 | 2.197 | 1.7e-06 | 20/20 |
| SVMWithL1Regularization | 0.7465 | 2.6253 | 0.284 | 1.7e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 0.6327 | 0.627 | 1.7e-06 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1094 | 0.5561 | 0.197 | 1.7e-06 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 6.3232 | 0.236 | 1.7e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 2.9336 | 0.311 | 1.7e-06 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2136 | 1.1478 | 0.186 | 1.7e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 2.1793 | 0.191 | 1.7e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 1.8160 | 0.742 | 1.7e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.9065 | 0.263 | 1.7e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 1.9816 | 0.011 | 1.7e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.9742 | 0.260 | 1.7e-06 | 20/20 |

Geometric-mean ratio **0.367** (bootstrap 95% CI 0.246–0.530), Wilcoxon signed-rank p = 1.0e-05, 22/25 problems below 1, 25/25 significant at 5% after Holm.

### Engine without dense blocks vs COO_ND: `DE_NODENSE` / `COO_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.7562 | 6.4972 | 0.424 | 1.7e-06 | 20/20 |
| Cajas | 0.2039 | 0.6905 | 0.295 | 1.7e-06 | 20/20 |
| ConeMatrixStuffingBench | 1.9095 | 3.4972 | 0.546 | 1.7e-06 | 20/20 |
| ConvexPlasticity | 0.0978 | 0.0718 | 1.362 | 1.7e-06 | 20/20 |
| FactorCovarianceModel | 0.3469 | 1.1499 | 0.302 | 1.7e-06 | 20/20 |
| HuberRegression | 1.0035 | 2.8000 | 0.358 | 1.7e-06 | 20/20 |
| LeastSquares | 0.8968 | 2.9389 | 0.305 | 1.7e-06 | 20/20 |
| Murray | 1.1744 | 1.2183 | 0.964 | 1.7e-06 | 20/20 |
| OptimalAdvertising | 0.8355 | 0.5345 | 1.563 | 1.7e-06 | 20/20 |
| ParamConeMatrixStuffing | 0.0273 | 0.0890 | 0.307 | 1.7e-06 | 20/20 |
| ParamSmallMatrixStuffing | 0.0403 | 0.1131 | 0.356 | 1.7e-06 | 20/20 |
| ParametrizedQPBenchmark | 0.7166 | 2.9920 | 0.240 | 1.7e-06 | 20/20 |
| QuantumHilbertMatrix | 0.5065 | 0.7865 | 0.644 | 1.7e-06 | 20/20 |
| SDPSegfault1132Benchmark | 3.2929 | 8.9248 | 0.369 | 1.7e-06 | 20/20 |
| SVMWithL1Regularization | 0.7465 | 2.7398 | 0.272 | 1.7e-06 | 20/20 |
| SemidefiniteProgramming | 0.3966 | 0.9938 | 0.399 | 1.7e-06 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.1094 | 0.5253 | 0.208 | 1.7e-06 | 20/20 |
| SimpleLPBenchmark | 1.4947 | 5.9805 | 0.250 | 1.7e-06 | 20/20 |
| SimpleQPBenchmark | 0.9117 | 2.9300 | 0.311 | 1.7e-06 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.2136 | 1.0874 | 0.196 | 1.7e-06 | 20/20 |
| SlowPruningBenchmark | 0.4156 | 2.1466 | 0.194 | 1.7e-06 | 20/20 |
| SmallMatrixStuffing | 1.3474 | 2.4900 | 0.541 | 1.7e-06 | 20/20 |
| TvInpainting | 0.2385 | 0.8140 | 0.293 | 1.7e-06 | 20/20 |
| UnconstrainedQP | 0.0221 | 2.4308 | 0.009 | 1.7e-06 | 20/20 |
| Yitzhaki | 0.2534 | 0.9922 | 0.255 | 1.7e-06 | 20/20 |

Geometric-mean ratio **0.327** (bootstrap 95% CI 0.222–0.450), Wilcoxon signed-rank p = 8.3e-07, 23/25 problems below 1, 25/25 significant at 5% after Holm.

### Dense blocks off: `de_cached_nodense` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.0023 | 0.2034 | 0.011 | 5.4e-07 | 20/20 |
| FactorCovarianceModel | 0.0871 | 0.0806 | 1.080 | 5.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0003 | 0.0003 | 0.982 | 1.7e-05 | 20/20 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0005 | 0.977 | 1.7e-05 | 20/20 |
| ParametrizedQPBenchmark | 0.4164 | 0.4232 | 0.984 | 0.013 | 20/20 |
| SVMWithL1Regularization | 0.1634 | 0.1524 | 1.072 | 5.4e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.0526 | 0.0526 | 1.000 | 0.598 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1040 | 0.1042 | 0.999 | 0.547 | 20/20 |

Geometric-mean ratio **0.578** (bootstrap 95% CI 0.187–1.034), Wilcoxon signed-rank p = 0.547, 6/8 problems below 1, 6/8 significant at 5% after Holm.

### Split off: `de_cached_rebuild` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.4135 | 0.2034 | 2.032 | 5.4e-07 | 20/20 |
| FactorCovarianceModel | 0.1290 | 0.0806 | 1.600 | 5.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0027 | 0.0003 | 8.788 | 5.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0041 | 0.0005 | 8.482 | 5.4e-07 | 20/20 |
| ParametrizedQPBenchmark | 0.5626 | 0.4232 | 1.329 | 5.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.2717 | 0.1524 | 1.783 | 5.4e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.0842 | 0.0526 | 1.600 | 5.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1667 | 0.1042 | 1.600 | 5.4e-07 | 20/20 |

Geometric-mean ratio **2.489** (bootstrap 95% CI 1.595–4.494), Wilcoxon signed-rank p = 0.008, 0/8 problems below 1, 8/8 significant at 5% after Holm.

### Both off: `de_cached_nodense_rebuild` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.0655 | 0.2034 | 0.322 | 5.4e-07 | 20/20 |
| FactorCovarianceModel | 0.3150 | 0.0806 | 3.906 | 5.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0027 | 0.0003 | 8.801 | 5.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0042 | 0.0005 | 8.791 | 5.4e-07 | 20/20 |
| ParametrizedQPBenchmark | 0.5718 | 0.4232 | 1.351 | 5.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.6072 | 0.1524 | 3.984 | 5.4e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.0840 | 0.0526 | 1.596 | 5.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1668 | 0.1042 | 1.601 | 5.4e-07 | 20/20 |

Geometric-mean ratio **2.459** (bootstrap 95% CI 1.187–4.759), Wilcoxon signed-rank p = 0.055, 1/8 problems below 1, 8/8 significant at 5% after Holm.

## Re-solves

### Engine re-solve vs dpp: `de_cached` / `dpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0806 | 0.0206 | 3.911 | 3.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.314 | 3.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0019 | 0.256 | 3.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.1524 | 0.0383 | 3.982 | 3.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1042 | 0.0633 | 1.645 | 3.4e-07 | 20/20 |

Geometric-mean ratio **1.156** (bootstrap 95% CI 0.403–3.313), Wilcoxon signed-rank p = –, 2/5 problems below 1, 5/5 significant at 5% after Holm.

### Engine re-solve vs dpp_coo: `de_cached` / `dpp_coo` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0806 | 0.0205 | 3.933 | 4.8e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.316 | 4.8e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0018 | 0.260 | 4.8e-07 | 20/20 |
| ParametrizedQPBenchmark | 0.4232 | 0.3045 | 1.390 | 4.8e-07 | 20/20 |
| SVMWithL1Regularization | 0.1524 | 0.0386 | 3.953 | 4.8e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.0526 | 0.0468 | 1.125 | 4.8e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1042 | 0.0659 | 1.581 | 4.8e-07 | 20/20 |

Geometric-mean ratio **1.179** (bootstrap 95% CI 0.545–2.420), Wilcoxon signed-rank p = 0.469, 2/7 problems below 1, 7/7 significant at 5% after Holm.

### Engine re-solve vs dpp_scipy: `de_cached` / `dpp_scipy` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0806 | 0.0205 | 3.924 | 3.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.317 | 3.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0018 | 0.260 | 3.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.1524 | 0.0383 | 3.984 | 3.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1042 | 0.0627 | 1.660 | 3.4e-07 | 20/20 |

Geometric-mean ratio **1.164** (bootstrap 95% CI 0.408–3.324), Wilcoxon signed-rank p = –, 2/5 problems below 1, 5/5 significant at 5% after Holm.

### Engine re-solve vs nodpp_cpp: `de_cached` / `nodpp_cpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.2034 | 0.0432 | 4.708 | 5.4e-07 | 20/20 |
| FactorCovarianceModel | 0.0806 | 1.1496 | 0.070 | 5.4e-07 | 20/20 |
| ParamConeMatrixStuffing | 0.0003 | 0.0379 | 0.008 | 5.4e-07 | 20/20 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0577 | 0.008 | 5.4e-07 | 20/20 |
| ParametrizedQPBenchmark | 0.4232 | 2.8589 | 0.148 | 5.4e-07 | 20/20 |
| SVMWithL1Regularization | 0.1524 | 2.6798 | 0.057 | 5.4e-07 | 20/20 |
| SimpleFullyParametrizedLPBenchmark | 0.0526 | 0.5847 | 0.090 | 5.4e-07 | 20/20 |
| SimpleScalarParametrizedLPBenchmark | 0.1042 | 1.2087 | 0.086 | 5.4e-07 | 20/20 |

Geometric-mean ratio **0.078** (bootstrap 95% CI 0.024–0.309), Wilcoxon signed-rank p = 0.016, 7/8 problems below 1, 8/8 significant at 5% after Holm.

## Non-DPP re-solves and first compiles (jury J1e, Legrain iii)

### Engine re-solve vs nodpp_cpp: `de_cached` / `nodpp_cpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0036 | 0.0489 | 0.073 | 2.7e-07 | 20/20 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0036 | 0.0490 | 0.073 | 2.7e-07 | 20/20 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.3164 | 0.083 | 2.7e-07 | 20/20 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.3151 | 0.084 | 2.7e-07 | 20/20 |

Geometric-mean ratio **0.078** (bootstrap 95% CI 0.073–0.084), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

### Engine re-solve vs nodpp_coo: `de_cached` / `nodpp_coo` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0036 | 0.0458 | 0.078 | 2.7e-07 | 20/20 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0036 | 0.0458 | 0.078 | 2.7e-07 | 20/20 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.3584 | 0.074 | 2.7e-07 | 20/20 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.3585 | 0.074 | 2.7e-07 | 20/20 |

Geometric-mean ratio **0.076** (bootstrap 95% CI 0.074–0.078), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

### Engine re-solve vs dpp: `de_cached` / `dpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0036 | 0.0012 | 2.877 | 1.4e-07 | 20/20 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.0064 | 4.113 | 1.4e-07 | 20/20 |

Geometric-mean ratio **3.440** (bootstrap 95% CI 2.877–4.113), Wilcoxon signed-rank p = –, 0/2 problems below 1, 2/2 significant at 5% after Holm.

### Engine re-solve vs de_cached_rebuild: `de_cached` / `de_cached_rebuild` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0036 | 0.0069 | 0.516 | 2.7e-07 | 20/20 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0036 | 0.0070 | 0.515 | 2.7e-07 | 20/20 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.0356 | 0.741 | 2.7e-07 | 20/20 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.0357 | 0.739 | 2.7e-07 | 20/20 |

Geometric-mean ratio **0.618** (bootstrap 95% CI 0.515–0.740), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

## Non-DPP set: first canonicalization, mean ± std (s)

| problem | n | m | nnz(A) | CPP_ND | SCIPY_ND | COO_ND | diffengine | best | ratio | p (Holm) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| factor_cov:variant=dpp:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.053 ± 7.1e-05 | 0.047 ± 2.7e-04 | 0.047 ± 1.8e-04 | 0.011 ± 5.9e-05 | COO_ND | 0.231 | 0.008 |
| factor_cov:variant=free:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.053 ± 1.9e-04 | 0.047 ± 1.6e-04 | 0.047 ± 1.6e-04 | 0.011 ± 6.7e-05 | COO_ND | 0.229 | 4.1e-07 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.053 ± 3.1e-04 | 0.048 ± 1.4e-04 | 0.047 ± 2.0e-04 | 0.011 ± 2.1e-04 | COO_ND | 0.233 | 4.1e-07 |
| lasso:variant=dpp:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.334 ± 0.001 | 0.365 ± 0.001 | 0.360 ± 6.4e-04 | 0.046 ± 1.5e-04 | CPP_ND | 0.139 | 4.1e-07 |
| lasso:variant=free:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.334 ± 7.7e-04 | 0.365 ± 0.003 | 0.360 ± 5.9e-04 | 0.046 ± 1.8e-04 | CPP_ND | 0.138 | 4.1e-07 |
| lasso:variant=nondpp:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.333 ± 0.002 | 0.365 ± 0.001 | 0.360 ± 7.6e-04 | 0.047 ± 1.4e-04 | CPP_ND | 0.140 | 4.1e-07 |

diffengine fastest on 6/6; geometric-mean ratio to the best backend **0.179** (95% CI 0.151–0.213), Wilcoxon p = 0.031; 6 problems significantly faster, 0 significantly slower (Holm, 5%).

## Phase breakdown of `DIFFENGINE` (cold), mean share of the time

| problem | time (s) | front end | convert | symbolic | numeric | assemble | format |
|---|---:|---:|---:|---:|---:|---:|---:|
| CVaRBenchmark | 4.2735 | 1% | 16% | 13% | 25% | 35% | 9% |
| Cajas | 0.2005 | 47% | 19% | 10% | 6% | 7% | 12% |
| ConeMatrixStuffingBench | 0.6342 | 68% | 23% | 0% | 8% | 0% | 0% |
| ConvexPlasticity | 0.4993 | 6% | 3% | 47% | 6% | 38% | 0% |
| FactorCovarianceModel | 0.1646 | 3% | 10% | 20% | 17% | 29% | 22% |
| HuberRegression | 0.4754 | 1% | 8% | 20% | 10% | 28% | 33% |
| LeastSquares | 0.4161 | 1% | 7% | 11% | 12% | 31% | 38% |
| Murray | 1.1637 | 0% | 94% | 2% | 1% | 1% | 1% |
| OptimalAdvertising | 0.8894 | 4% | 1% | 90% | 3% | 1% | 1% |
| ParamConeMatrixStuffing | 0.0225 | 84% | 14% | 1% | 1% | 1% | 1% |
| ParamSmallMatrixStuffing | 0.0329 | 84% | 14% | 1% | 1% | 0% | 0% |
| ParametrizedQPBenchmark | 0.7305 | 22% | 17% | 6% | 14% | 19% | 23% |
| QuantumHilbertMatrix | 0.4923 | 4% | 13% | 63% | 20% | 0% | 0% |
| SDPSegfault1132Benchmark | 1.9034 | 0% | 0% | 46% | 49% | 4% | 0% |
| SVMWithL1Regularization | 0.3627 | 3% | 8% | 18% | 27% | 24% | 22% |
| SemidefiniteProgramming | 0.3964 | 5% | 14% | 40% | 34% | 4% | 4% |
| SimpleFullyParametrizedLPBenchmark | 0.1110 | 10% | 6% | 22% | 16% | 11% | 35% |
| SimpleLPBenchmark | 1.0978 | 8% | 6% | 23% | 16% | 12% | 35% |
| SimpleQPBenchmark | 0.4327 | 1% | 8% | 15% | 14% | 34% | 27% |
| SimpleScalarParametrizedLPBenchmark | 0.2198 | 8% | 7% | 23% | 17% | 11% | 34% |
| SlowPruningBenchmark | 0.3930 | 2% | 1% | 35% | 10% | 19% | 32% |
| SmallMatrixStuffing | 0.4995 | 71% | 21% | 0% | 7% | 0% | 0% |
| TvInpainting | 0.2438 | 13% | 4% | 25% | 21% | 14% | 24% |
| UnconstrainedQP | 0.0159 | 14% | 13% | 43% | 27% | 2% | 2% |
| Yitzhaki | 0.1333 | 3% | 6% | 10% | 17% | 20% | 44% |

## Phase breakdown of `de_cached` (warm), mean share of the time

| problem | time (s) | front end | convert | symbolic | numeric | assemble | format |
|---|---:|---:|---:|---:|---:|---:|---:|
| ConvexPlasticity | 0.2060 | 0% | 0% | 0% | 12% | 88% | 0% |
| FactorCovarianceModel | 0.0819 | 3% | 0% | 0% | 4% | 50% | 44% |
| ParamConeMatrixStuffing | 0.0003 | 22% | 0% | 0% | 43% | 12% | 23% |
| ParamSmallMatrixStuffing | 0.0005 | 23% | 0% | 0% | 54% | 8% | 16% |
| ParametrizedQPBenchmark | 0.4265 | 14% | 0% | 0% | 20% | 29% | 37% |
| SVMWithL1Regularization | 0.1566 | 3% | 0% | 0% | 3% | 45% | 50% |
| SimpleFullyParametrizedLPBenchmark | 0.0535 | 3% | 0% | 0% | 11% | 19% | 66% |
| SimpleScalarParametrizedLPBenchmark | 0.1062 | 2% | 0% | 0% | 12% | 19% | 67% |

## Memory (cold): peak-RSS delta (MB), one measurement per cell

| problem | COO_ND | CPP_ND | DE_EVAL | DE_NODENSE | DE_NODENSE_EVAL | DIFFENGINE | SCIPY_ND |
|---|---:|---:|---:|---:|---:|---:|---:|
| CVaRBenchmark | 3587.0 | 4021.7 | – | 2211.0 | – | 6282.6 | 2803.9 |
| Cajas | 320.0 | 1192.8 | – | 342.5 | – | 341.1 | 298.4 |
| ConeMatrixStuffingBench | 3730.0 | 2009.9 | – | 1623.2 | – | 478.7 | 963.5 |
| ConvexPlasticity | 82.5 | 82.5 | 1327.6 | 25.6 | 24.1 | 1329.5 | 82.4 |
| FactorCovarianceModel | 1334.1 | 1129.1 | 759.7 | 999.2 | 999.2 | 759.8 | 1046.8 |
| HuberRegression | 3121.2 | 2223.2 | – | 1834.4 | – | 1412.9 | 2245.7 |
| LeastSquares | 3020.7 | 2140.0 | – | 1893.6 | – | 1459.3 | 2326.7 |
| Murray | 305.3 | 2849.5 | – | 305.8 | – | 307.9 | 219.8 |
| OptimalAdvertising | 196.9 | 172.6 | – | 944.8 | – | 6066.2 | 181.4 |
| ParamConeMatrixStuffing | 12.3 | 9.7 | 7.0 | 6.2 | 8.5 | 5.9 | 8.3 |
| ParamSmallMatrixStuffing | 21.9 | 17.2 | 11.5 | 10.6 | 14.9 | 10.6 | 13.0 |
| ParametrizedQPBenchmark | 2997.8 | 2035.2 | 1501.5 | 1775.5 | 2001.4 | 1775.4 | 2173.9 |
| QuantumHilbertMatrix | 288.0 | 221.7 | – | 909.7 | – | 909.6 | 217.7 |
| SDPSegfault1132Benchmark | 12983.2 | 7536.5 | – | 11186.0 | – | 9253.8 | 3460.1 |
| SVMWithL1Regularization | 2904.4 | 1976.3 | 2033.6 | 2416.9 | 2416.8 | 2033.7 | 2041.8 |
| SemidefiniteProgramming | 640.1 | 1317.1 | – | 1137.7 | – | 1137.9 | 350.0 |
| SimpleFullyParametrizedLPBenchmark | 526.0 | 517.2 | 480.6 | 492.1 | 513.7 | 492.2 | 493.6 |
| SimpleLPBenchmark | 5027.4 | 5352.5 | – | 5056.8 | – | 4792.2 | 4960.7 |
| SimpleQPBenchmark | 3236.5 | 2194.1 | – | 2204.2 | – | 1655.1 | 2355.2 |
| SimpleScalarParametrizedLPBenchmark | 1067.9 | 1087.8 | 963.0 | 1008.9 | 1021.1 | 1008.9 | 1024.1 |
| SlowPruningBenchmark | 1827.8 | 1351.8 | – | 1120.3 | – | 1796.9 | 1425.0 |
| SmallMatrixStuffing | 2405.1 | 1189.7 | – | 1117.3 | – | 322.3 | 634.0 |
| TvInpainting | 993.9 | 705.0 | – | 1048.3 | – | 1048.4 | 857.8 |
| UnconstrainedQP | 2105.0 | 1427.1 | – | 41.4 | – | 52.9 | 1057.8 |
| Yitzhaki | 504.5 | 449.0 | – | 572.2 | – | 476.5 | 437.1 |

## Memory (warm): peak-RSS delta (MB), one measurement per cell

| problem | de_cached | de_cached_nodense | de_cached_nodense_rebuild | de_cached_rebuild |
|---|---:|---:|---:|---:|
| ConvexPlasticity | 105.7 | 2.9 | 7.3 | 506.7 |
| FactorCovarianceModel | 76.5 | 77.9 | 544.1 | 326.5 |
| ParamConeMatrixStuffing | 0.4 | 0.4 | 0.4 | 0.4 |
| ParamSmallMatrixStuffing | 0.8 | 0.7 | 0.8 | 0.8 |
| ParametrizedQPBenchmark | 220.2 | 220.2 | 990.5 | 990.5 |
| SVMWithL1Regularization | 145.0 | 145.1 | 727.8 | 625.0 |
| SimpleFullyParametrizedLPBenchmark | 45.9 | 45.9 | 141.5 | 141.5 |
| SimpleScalarParametrizedLPBenchmark | 45.9 | 45.9 | 198.7 | 198.7 |
