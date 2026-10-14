# Final-deposit experiments: summary

## Environments

- `cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `cold_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `sensitivity_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `sensitivity_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `density_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `density_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `families_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `families_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `scaled25_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4045+g5c071510a (5c071510a) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `scaled25_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']

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
| lasso:variant=free:n=2000:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=250:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=4000:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=500:seed=0 | CPP | 4/4 | – |
| lasso:variant=nondpp:n=1000:seed=0 | CPP_EVAL | 16/16 | – |
| scaled:cls=CVaRBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=CVaRBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=CVaRBenchmark:s=2 | – | 1/4 | first:DIFFENGINE, first:DE_NODENSE, first:COO |
| scaled:cls=CVaRBenchmark:s=4 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=Cajas:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Cajas:s=2 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=0.5 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=2 | CPP | 4/4 | – |
| scaled:cls=ConvexPlasticity:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ConvexPlasticity:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=HuberRegression:density=0.01 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.05 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.2 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.5 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=0.25 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=0.5 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=2 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=4 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.01 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.05 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.2 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.5 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=0.25 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=0.5 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=2 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=4 | CPP | 4/4 | – |
| scaled:cls=Murray:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Murray:s=2 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=0.25 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=0.5 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=2 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=4 | – | 3/4 | first:DIFFENGINE |
| scaled:cls=ParamConeMatrixStuffing:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamConeMatrixStuffing:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=QuantumHilbertMatrix:s=0.5 | CPP | 4/4 | – |
| scaled:cls=QuantumHilbertMatrix:s=2 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=SDPSegfault1132Benchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SDPSegfault1132Benchmark:s=2 | – | 1/4 | first:DIFFENGINE, first:DE_NODENSE, first:COO |
| scaled:cls=SVMWithL1Regularization:density=0.01 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.05 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=4 | CPP_EVAL | 12/16 | first:DE_NODENSE, first:de_cached_nodense, first:de_cached_nodense_rebuild, first:DE_NODENSE_EVAL |
| scaled:cls=SemidefiniteProgramming:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=2 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=4 | CPP | 4/4 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleLPBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleLPBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.01 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.05 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.2 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=4 | CPP | 4/4 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SlowPruningBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SlowPruningBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=2 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=0.5 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=2 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=0.5 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=2 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=0.25 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=2 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=4 | CPP | 4/4 | – |

35 failed (problem, target) checks, of which 35 only ran out of memory (unverified, not wrong).

Passed with a footnote (NaN in the problem data):

- OptimalAdvertising `first:DIFFENGINE`: NaN where the reference has a zero (1 in b); every finite entry identical
- OptimalAdvertising `first:DE_NODENSE`: NaN where the reference has a zero (1 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=0.25 `first:DIFFENGINE`: NaN where the reference has a zero (3 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=0.25 `first:DE_NODENSE`: NaN where the reference has a zero (3 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=0.5 `first:DIFFENGINE`: NaN where the reference has a zero (3 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=0.5 `first:DE_NODENSE`: NaN where the reference has a zero (3 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=2 `first:DIFFENGINE`: NaN where the reference has a zero (1 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=2 `first:DE_NODENSE`: NaN where the reference has a zero (1 in b); every finite entry identical
- scaled:cls=OptimalAdvertising:s=4 `first:DE_NODENSE`: NaN where the reference has a zero (1 in b); every finite entry identical

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

Geometric-mean ratio **1.269** (bootstrap 95% CI 1.010–1.547), Wilcoxon signed-rank p = 0.014, 8/25 problems below 1, 23/25 significant at 5% after Holm.

### Fully CSR, all problems: `fully CSR` / `dense blocks on` (cold)

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

Geometric-mean ratio **1.269** (bootstrap 95% CI 1.009–1.551), Wilcoxon signed-rank p = 0.014, 8/25 problems below 1, 23/25 significant at 5% after Holm.

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

## Re-solves

## Non-DPP re-solves and first compiles (jury J1e, Legrain iii)

## Non-DPP set: first canonicalization, mean ± std (s)

| problem | n | m | nnz(A) | CPP_ND | SCIPY_ND | COO_ND | diffengine | best | ratio | p (Holm) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| lasso:variant=free:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.333 ± 0.001 | 0.365 ± 5.6e-04 | 0.361 ± 4.6e-04 | 0.046 ± 2.4e-04 | CPP_ND | 0.139 | 0.008 |

diffengine fastest on 1/1; geometric-mean ratio to the best backend **0.139** (95% CI –––), Wilcoxon p = –; 1 problems significantly faster, 0 significantly slower (Holm, 5%).

## Scaling: 25 problems at s = 1/2, 1, 2

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | s 0.5 | s 1 | s 2 | nnz(A) range |
|---|---:|---:|---:|---|
| CVaRBenchmark | 0.55 | 0.66 | cap | 12,846,593–51,381,761 |
| Cajas | 0.29 | 0.29 | 0.27 | 990,034–3,894,133 |
| ConeMatrixStuffingBench | 0.31 | 0.30 | 0.29 | 3,536–7,072 |
| ConvexPlasticity | 5.29 | 6.94 | 8.68 | 36,000–144,000 |
| FactorCovarianceModel | 0.15 | 0.14 | 0.18 | 3,225,250–12,900,250 |
| HuberRegression | 0.18 | 0.17 | 0.17 | 6,765,987–27,040,636 |
| LeastSquares | 0.15 | 0.17 | 0.17 | 7,004,250–28,004,271 |
| Murray | 1.14 | 0.95 | 1.01 | 758,935–2,987,920 |
| OptimalAdvertising | 1.09 | 1.67 | 3.06 | 500,500–2,000,500 |
| ParamConeMatrixStuffing | 0.51 | 0.53 | 0.53 | 142–282 |
| ParamSmallMatrixStuffing | 0.52 | 0.52 | 0.51 | 212–424 |
| ParametrizedQPBenchmark | 0.23 | 0.24 | 0.23 | 7,208,008–28,813,363 |
| QuantumHilbertMatrix | 1.17 | 0.63 | cap | 1,560–81,072 |
| SDPSegfault1132Benchmark | 1.29 | 1.27 | cap | 501,736–2,023,126 |
| SVMWithL1Regularization | 0.14 | 0.14 | 0.15 | 6,290,001–25,152,501 |
| SemidefiniteProgramming | 0.61 | 0.63 | 0.63 | 1,211,331–4,862,506 |
| SimpleFullyParametrizedLPBenchmark | 0.22 | 0.21 | 0.20 | 1,000,000–4,000,000 |
| SimpleLPBenchmark | 0.19 | 0.18 | 0.17 | 10,000,000–40,000,000 |
| SimpleQPBenchmark | 0.15 | 0.15 | 0.16 | 6,420,687–25,648,842 |
| SimpleScalarParametrizedLPBenchmark | 0.21 | 0.20 | 0.20 | 2,000,000–8,000,000 |
| SlowPruningBenchmark | 0.21 | 0.22 | 0.21 | 4,200,000–16,800,000 |
| SmallMatrixStuffing | 0.29 | 0.30 | 0.27 | 2,828–5,656 |
| TvInpainting | 0.31 | 0.30 | 0.30 | 1,812,574–7,267,080 |
| UnconstrainedQP | 0.02 | 8.1e-03 | 5.0e-03 | 13,319–26,641 |
| Yitzhaki | 0.15 | 0.14 | 0.14 | 2,281,432–9,147,052 |

## Scaling: 10 families at five sizes

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | s 0.25 | s 0.5 | s 1 | s 2 | s 4 | nnz(A) range |
|---|---:|---:|---:|---:|---:|---|
| HuberRegression | 0.15 | 0.18 | 0.17 | 0.17 | 0.17 | 3,388,500–54,054,000 |
| FactorCovarianceModel | 0.16 | 0.15 | 0.14 | 0.18 | 0.22 | 1,612,750–25,800,250 |
| OptimalAdvertising | 0.78 | 1.09 | 1.67 | 3.06 | cap | 250,500–4,000,500 |
| SVMWithL1Regularization | 0.15 | 0.14 | 0.14 | 0.15 | 0.16 | 3,146,251–50,302,501 |
| LeastSquares | 0.15 | 0.15 | 0.17 | 0.17 | 0.18 | 3,503,500–56,014,000 |
| SimpleQPBenchmark | 0.15 | 0.15 | 0.15 | 0.16 | 0.16 | 3,216,000–51,264,000 |
| Yitzhaki | 0.13 | 0.15 | 0.14 | 0.14 | 0.13 | 1,139,950–18,329,500 |
| CVaRBenchmark | 0.57 | 0.55 | 0.66 | cap | cap | 6,424,065–51,381,761 |
| SemidefiniteProgramming | 0.58 | 0.61 | 0.63 | 0.63 | 0.67 | 611,050–9,704,200 |
| lasso | 0.21 | 0.15 | 0.14 | 0.15 | 0.15 | 126,500–32,024,000 |

## Density: 5 problems at five densities

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | density 0.01 | density 0.05 | density 0.2 | density 0.5 | density 1 | nnz(A) range |
|---|---:|---:|---:|---:|---:|---|
| LeastSquares | 0.81 | 1.13 | 0.58 | 0.33 | 0.17 | 146,860–14,007,000 |
| HuberRegression | 2.56 | 1.70 | 0.65 | 0.34 | 0.17 | 161,911–13,527,000 |
| SVMWithL1Regularization | 0.72 | 1.40 | 0.63 | 0.32 | 0.14 | 202,469–12,577,501 |
| SimpleQPBenchmark | 0.40 | 0.60 | 0.45 | 0.29 | 0.15 | 159,980–12,832,000 |
| lasso (n = 1000) | 0.88 | 0.57 | 0.58 | 0.32 | 0.14 | 25,872–2,006,000 |

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
