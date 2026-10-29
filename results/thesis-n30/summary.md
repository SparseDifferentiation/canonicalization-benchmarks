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
- `density8_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `density8_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `grid25_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `grid25_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_cold_upstream.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 1.9.2 (None) / sparsediffpy 0.3.0 (engine None) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']
- `memory_density8_fork.json`: Apple M2 / macOS-26.5.1-arm64-arm-64bit-Mach-O / Python 3.13.5 / cvxpy 0.1.0.dev4044+g35e81b129 (35e81b129) / sparsediffpy 0.7.0 (engine 4f42e05) / BLAS ['/System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate']

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
| factor_cov:variant=dpp:n=5000:seed=0 | CPP_EVAL | 20/20 | – |
| factor_cov:variant=free:n=5000:seed=0 | CPP | 4/4 | – |
| factor_cov:variant=nondpp:n=5000:seed=0 | CPP_EVAL | 20/20 | – |
| lasso:variant=dpp:n=1000:seed=0 | CPP_EVAL | 20/20 | – |
| lasso:variant=free:n=1000:density=0.01:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:density=0.02:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:density=0.05:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:density=0.1:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:density=0.2:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:density=0.5:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1000:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=1414:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=2000:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=500:seed=0 | CPP | 4/4 | – |
| lasso:variant=free:n=707:seed=0 | CPP | 4/4 | – |
| lasso:variant=nondpp:n=1000:seed=0 | CPP_EVAL | 20/20 | – |
| scaled:cls=CVaRBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=CVaRBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=CVaRBenchmark:s=2 | – | 3/4 | first:DIFFENGINE |
| scaled:cls=CVaRBenchmark:s=4 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=Cajas:s=0.25 | CPP | 4/4 | – |
| scaled:cls=Cajas:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Cajas:s=2 | CPP | 4/4 | – |
| scaled:cls=Cajas:s=4 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=0.25 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=0.5 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=2 | CPP | 4/4 | – |
| scaled:cls=ConeMatrixStuffingBench:s=4 | CPP | 4/4 | – |
| scaled:cls=ConvexPlasticity:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=ConvexPlasticity:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ConvexPlasticity:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ConvexPlasticity:s=4 | – | 12/16 | first:DIFFENGINE, first:de_cached, first:de_cached_rebuild, first:DE_EVAL |
| scaled:cls=FactorCovarianceModel:density=0.01 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:density=0.02 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:density=0.05 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:density=0.1 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:density=0.2 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:density=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=FactorCovarianceModel:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=HuberRegression:density=0.01 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.02 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.05 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.1 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.2 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:density=0.5 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=0.25 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=0.5 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=2 | CPP | 4/4 | – |
| scaled:cls=HuberRegression:s=4 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.01 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.02 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.05 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.1 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.2 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:density=0.5 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=0.25 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=0.5 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=2 | CPP | 4/4 | – |
| scaled:cls=LeastSquares:s=4 | CPP | 4/4 | – |
| scaled:cls=Murray:s=0.25 | CPP | 4/4 | – |
| scaled:cls=Murray:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Murray:s=2 | CPP | 4/4 | – |
| scaled:cls=Murray:s=4 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=OptimalAdvertising:s=0.25 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=0.5 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=2 | CPP | 4/4 | – |
| scaled:cls=OptimalAdvertising:s=4 | – | 3/4 | first:DIFFENGINE |
| scaled:cls=ParamConeMatrixStuffing:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamConeMatrixStuffing:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamConeMatrixStuffing:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamConeMatrixStuffing:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParamSmallMatrixStuffing:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=ParametrizedQPBenchmark:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=QuantumHilbertMatrix:s=0.5 | CPP | 4/4 | – |
| scaled:cls=QuantumHilbertMatrix:s=2 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=SDPSegfault1132Benchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SDPSegfault1132Benchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SDPSegfault1132Benchmark:s=2 | – | 1/4 | first:DIFFENGINE, first:DE_NODENSE, first:COO |
| scaled:cls=SDPSegfault1132Benchmark:s=4 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=SVMWithL1Regularization:density=0.01 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.02 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.05 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.1 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:density=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SVMWithL1Regularization:s=4 | CPP_EVAL | 12/16 | first:DE_NODENSE, first:de_cached_nodense, first:de_cached_nodense_rebuild, first:DE_NODENSE_EVAL |
| scaled:cls=SemidefiniteProgramming:density=0.01 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:density=0.02 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:density=0.05 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:density=0.1 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:density=0.2 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:density=0.5 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=2 | CPP | 4/4 | – |
| scaled:cls=SemidefiniteProgramming:s=4 | CPP | 4/4 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleFullyParametrizedLPBenchmark:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleLPBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SimpleLPBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleLPBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SimpleLPBenchmark:s=4 | – | 0/12 | first:DIFFENGINE, first:DE_NODENSE, first:de_cached, first:de_cached_nodense, first:de_cached_rebuild, first:de_cached_nodense_rebuild, first:SCIPY, first:COO, first:SCIPY_EVAL, first:COO_EVAL, first:DE_EVAL, first:DE_NODENSE_EVAL |
| scaled:cls=SimpleQPBenchmark:density=0.01 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.02 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.05 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.1 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.2 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:density=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SimpleQPBenchmark:s=4 | CPP | 4/4 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=0.25 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=0.5 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=2 | CPP_EVAL | 20/20 | – |
| scaled:cls=SimpleScalarParametrizedLPBenchmark:s=4 | CPP_EVAL | 20/20 | – |
| scaled:cls=SlowPruningBenchmark:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SlowPruningBenchmark:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SlowPruningBenchmark:s=2 | CPP | 4/4 | – |
| scaled:cls=SlowPruningBenchmark:s=4 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=0.25 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=0.5 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=2 | CPP | 4/4 | – |
| scaled:cls=SmallMatrixStuffing:s=4 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=0.25 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=0.5 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=2 | CPP | 4/4 | – |
| scaled:cls=TvInpainting:s=4 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=0.25 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=0.5 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=2 | CPP | 4/4 | – |
| scaled:cls=UnconstrainedQP:s=4 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.01 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.02 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.05 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.1 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.2 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:density=0.5 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=0.25 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=0.5 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=2 | CPP | 4/4 | – |
| scaled:cls=Yitzhaki:s=4 | CPP | 4/4 | – |

73 failed (problem, target) checks, of which 73 only ran out of memory (unverified, not wrong).

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
| CVaRBenchmark | 131841 | 263681 | 25691649 | 7.196 ± 0.015 | 6.503 ± 0.020 | 6.512 ± 0.023 | 3.421 ± 0.009 | SCIPY_ND | 0.526 | 7.5e-10 |
| Cajas | 2450 | 640851 | 1960900 | 3.885 ± 0.012 | 0.689 ± 0.005 | 0.693 ± 0.005 | 0.205 ± 0.001 | SCIPY_ND | 0.297 | 7.5e-10 |
| ConeMatrixStuffingBench | 5000 | 5000 | 5000 | 2.517 ± 0.010 | 2.152 ± 0.008 | 3.537 ± 0.008 | 0.642 ± 0.004 | SCIPY_ND | 0.298 | 7.5e-10 |
| ConvexPlasticity | 33000 | 36000 | 72000 | 0.078 ± 6.9e-04 | 0.072 ± 6.8e-04 | 0.070 ± 0.001 | 0.507 ± 0.001 | COO_ND | 7.312 | 7.5e-10 |
| FactorCovarianceModel | 75250 | 75252 | 6450250 | 1.223 ± 0.005 | 1.164 ± 0.003 | 1.150 ± 0.004 | 0.177 ± 0.003 | COO_ND | 0.154 | 7.5e-10 |
| HuberRegression | 16500 | 13500 | 13527000 | 2.770 ± 0.006 | 2.850 ± 0.007 | 2.796 ± 0.007 | 0.495 ± 0.008 | CPP_ND | 0.178 | 7.5e-10 |
| LeastSquares | 9000 | 7000 | 14007000 | 2.410 ± 0.009 | 2.912 ± 0.007 | 2.939 ± 0.005 | 0.435 ± 0.002 | CPP_ND | 0.181 | 7.5e-10 |
| Murray | 245400 | 490051 | 1503700 | 1.276 ± 0.018 | 1.229 ± 0.007 | 1.224 ± 0.007 | 1.181 ± 0.001 | COO_ND | 0.964 | 7.5e-10 |
| OptimalAdvertising | 250250 | 251750 | 1000500 | 2.573 ± 0.003 | 0.598 ± 0.008 | 0.534 ± 0.001 | 0.901 ± 0.004 | COO_ND | 1.685 | 7.5e-10 |
| ParamConeMatrixStuffing | 200 | 200 | 200 | 0.043 ± 1.7e-04 | 0.072 ± 2.6e-04 | 0.089 ± 4.2e-04 | 0.022 ± 4.2e-04 | CPP_ND | 0.524 | 7.5e-10 |
| ParamSmallMatrixStuffing | 300 | 300 | 300 | 0.063 ± 1.9e-04 | 0.127 ± 0.001 | 0.113 ± 8.2e-04 | 0.033 ± 1.5e-04 | CPP_ND | 0.518 | 7.5e-10 |
| ParametrizedQPBenchmark | 8400 | 10800 | 14410800 | 2.974 ± 0.029 | 3.030 ± 0.007 | 2.990 ± 0.010 | 0.755 ± 0.046 | CPP_ND | 0.250 | 7.5e-10 |
| QuantumHilbertMatrix | 6176 | 6176 | 81072 | 1.062 ± 0.002 | 0.805 ± 0.004 | 0.788 ± 0.002 | 0.653 ± 0.003 | COO_ND | 0.828 | 7.5e-10 |
| SDPSegfault1132Benchmark | 4951 | 14951 | 1014157 | 8.000 ± 0.011 | 1.663 ± 0.148 | 7.298 ± 0.110 | 2.147 ± 0.006 | SCIPY_ND | 1.317 | 7.5e-10 |
| SVMWithL1Regularization | 26002 | 51001 | 12577501 | 2.786 ± 0.008 | 2.634 ± 0.008 | 2.742 ± 0.015 | 0.387 ± 0.001 | SCIPY_ND | 0.147 | 7.5e-10 |
| SemidefiniteProgramming | 20100 | 20220 | 2432100 | 1.161 ± 0.003 | 0.632 ± 0.002 | 0.997 ± 0.004 | 0.405 ± 0.003 | SCIPY_ND | 0.641 | 7.5e-10 |
| SimpleFullyParametrizedLPBenchmark | 1000000 | 2000000 | 2000000 | 0.611 ± 0.001 | 0.555 ± 0.001 | 0.523 ± 0.001 | 0.115 ± 4.6e-04 | COO_ND | 0.220 | 7.5e-10 |
| SimpleLPBenchmark | 10000000 | 20000000 | 20000000 | 6.898 ± 0.038 | 6.303 ± 0.017 | 5.962 ± 0.014 | 1.121 ± 0.003 | COO_ND | 0.188 | 7.5e-10 |
| SimpleQPBenchmark | 1600 | 8020 | 12832000 | 2.891 ± 0.005 | 2.944 ± 0.006 | 2.929 ± 0.006 | 0.453 ± 0.001 | CPP_ND | 0.157 | 7.5e-10 |
| SimpleScalarParametrizedLPBenchmark | 2000000 | 4000000 | 4000000 | 1.260 ± 0.003 | 1.151 ± 0.002 | 1.087 ± 0.003 | 0.230 ± 7.2e-04 | COO_ND | 0.212 | 7.5e-10 |
| SlowPruningBenchmark | 402000 | 400000 | 8400000 | 1.792 ± 0.004 | 2.185 ± 0.004 | 2.147 ± 0.004 | 0.408 ± 7.9e-04 | CPP_ND | 0.228 | 7.5e-10 |
| SmallMatrixStuffing | 4000 | 4000 | 4000 | 1.683 ± 0.013 | 1.822 ± 0.008 | 2.508 ± 0.007 | 0.502 ± 0.002 | CPP_ND | 0.298 | 7.5e-10 |
| TvInpainting | 1047553 | 2614279 | 3630958 | 0.919 ± 0.001 | 0.913 ± 0.002 | 0.815 ± 0.002 | 0.257 ± 0.001 | COO_ND | 0.316 | 7.5e-10 |
| UnconstrainedQP | 289 | 1009 | 18649 | 1.955 ± 0.003 | 1.980 ± 0.005 | 2.439 ± 0.002 | 22.937 ± 0.021 | CPP_ND | 11.734 | 7.5e-10 |
| Yitzhaki | 44900 | 89751 | 4574800 | 0.938 ± 0.001 | 0.982 ± 0.002 | 1.006 ± 0.003 | 0.145 ± 7.2e-04 | CPP_ND | 0.154 | 7.5e-10 |

diffengine fastest on 21/25; geometric-mean ratio to the best backend **0.437** (95% CI 0.289–0.704), Wilcoxon p = 0.003; 21 problems significantly faster, 4 significantly slower (Holm, 5%).

## Ablation (jury J1b, Legrain ii)

### Dense blocks off for constant data (parametric matrices stay dense): `DE_NODENSE` / `DIFFENGINE` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 3.4219 | 0.708 | 7.5e-10 | 30/30 |
| Cajas | 0.2090 | 0.2045 | 1.022 | 2.1e-09 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 0.6415 | 3.027 | 7.5e-10 | 30/30 |
| ConvexPlasticity | 0.0965 | 0.5064 | 0.190 | 7.5e-10 | 30/30 |
| FactorCovarianceModel | 0.3651 | 0.1770 | 2.063 | 7.5e-10 | 30/30 |
| HuberRegression | 1.0153 | 0.4930 | 2.059 | 7.5e-10 | 30/30 |
| LeastSquares | 0.9058 | 0.4350 | 2.082 | 7.5e-10 | 30/30 |
| Murray | 1.1783 | 1.1802 | 0.998 | 1.9e-04 | 30/30 |
| OptimalAdvertising | 0.8338 | 0.8997 | 0.927 | 7.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0273 | 0.0224 | 1.218 | 7.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0402 | 0.0327 | 1.229 | 7.5e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.7432 | 0.7420 | 1.002 | 0.684 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 0.6525 | 1.028 | 7.5e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 2.1467 | 1.613 | 7.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.7434 | 0.3873 | 1.920 | 7.5e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 0.4043 | 1.005 | 2.0e-07 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.1147 | 0.1150 | 0.997 | 6.0e-04 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 1.1202 | 1.324 | 7.5e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 0.4528 | 2.015 | 7.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.2250 | 0.2303 | 0.977 | 7.5e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 0.4078 | 1.024 | 7.5e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 0.5017 | 2.727 | 7.5e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.2574 | 0.971 | 7.5e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 22.9320 | 0.022 | 7.5e-10 | 30/30 |
| Yitzhaki | 0.2632 | 0.1446 | 1.820 | 7.5e-10 | 30/30 |

Geometric-mean ratio **1.063** (bootstrap 95% CI 0.706–1.451), Wilcoxon signed-rank p = 0.067, 8/25 problems below 1, 24/25 significant at 5% after Holm.

### Fully CSR, parameter-free problems: `DE_NODENSE` / `DIFFENGINE` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 3.4219 | 0.708 | 5.1e-10 | 30/30 |
| Cajas | 0.2090 | 0.2045 | 1.022 | 1.3e-09 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 0.6415 | 3.027 | 5.1e-10 | 30/30 |
| HuberRegression | 1.0153 | 0.4930 | 2.059 | 5.1e-10 | 30/30 |
| LeastSquares | 0.9058 | 0.4350 | 2.082 | 5.1e-10 | 30/30 |
| Murray | 1.1783 | 1.1802 | 0.998 | 6.4e-05 | 30/30 |
| OptimalAdvertising | 0.8338 | 0.8997 | 0.927 | 5.1e-10 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 0.6525 | 1.028 | 5.1e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 2.1467 | 1.613 | 5.1e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 0.4043 | 1.005 | 1.0e-07 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 1.1202 | 1.324 | 5.1e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 0.4528 | 2.015 | 5.1e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 0.4078 | 1.024 | 5.1e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 0.5017 | 2.727 | 5.1e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.2574 | 0.971 | 5.1e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 22.9320 | 0.022 | 5.1e-10 | 30/30 |
| Yitzhaki | 0.2632 | 0.1446 | 1.820 | 5.1e-10 | 30/30 |

Geometric-mean ratio **1.087** (bootstrap 95% CI 0.608–1.618), Wilcoxon signed-rank p = 0.089, 5/17 problems below 1, 17/17 significant at 5% after Holm.

### Fully CSR, all problems: `fully CSR` / `dense blocks on` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 3.4219 | 0.708 | 5.1e-10 | 30/30 |
| Cajas | 0.2090 | 0.2045 | 1.022 | 1.3e-09 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 0.6415 | 3.027 | 5.1e-10 | 30/30 |
| HuberRegression | 1.0153 | 0.4930 | 2.059 | 5.1e-10 | 30/30 |
| LeastSquares | 0.9058 | 0.4350 | 2.082 | 5.1e-10 | 30/30 |
| Murray | 1.1783 | 1.1802 | 0.998 | 6.4e-05 | 30/30 |
| OptimalAdvertising | 0.8338 | 0.8997 | 0.927 | 5.1e-10 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 0.6525 | 1.028 | 5.1e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 2.1467 | 1.613 | 5.1e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 0.4043 | 1.005 | 1.0e-07 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 1.1202 | 1.324 | 5.1e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 0.4528 | 2.015 | 5.1e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 0.4078 | 1.024 | 5.1e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 0.5017 | 2.727 | 5.1e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.2574 | 0.971 | 5.1e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 22.9320 | 0.022 | 5.1e-10 | 30/30 |
| Yitzhaki | 0.2632 | 0.1446 | 1.820 | 5.1e-10 | 30/30 |

Geometric-mean ratio **1.087** (bootstrap 95% CI 0.604–1.629), Wilcoxon signed-rank p = 0.089, 5/17 problems below 1, 17/17 significant at 5% after Holm.

### Engine without dense blocks vs CPP_ND: `DE_NODENSE` / `CPP_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 7.1947 | 0.337 | 7.5e-10 | 30/30 |
| Cajas | 0.2090 | 3.8841 | 0.054 | 7.5e-10 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 2.5192 | 0.771 | 7.5e-10 | 30/30 |
| ConvexPlasticity | 0.0965 | 0.0780 | 1.237 | 7.5e-10 | 30/30 |
| FactorCovarianceModel | 0.3651 | 1.2230 | 0.299 | 7.5e-10 | 30/30 |
| HuberRegression | 1.0153 | 2.7702 | 0.367 | 7.5e-10 | 30/30 |
| LeastSquares | 0.9058 | 2.4089 | 0.376 | 7.5e-10 | 30/30 |
| Murray | 1.1783 | 1.2750 | 0.924 | 7.5e-10 | 30/30 |
| OptimalAdvertising | 0.8338 | 2.5730 | 0.324 | 7.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0273 | 0.0427 | 0.638 | 7.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0402 | 0.0632 | 0.636 | 7.5e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.7432 | 2.9640 | 0.251 | 7.5e-10 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 1.0625 | 0.631 | 7.5e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 7.9997 | 0.433 | 7.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.7434 | 2.7867 | 0.267 | 7.5e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 1.1600 | 0.350 | 7.5e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.1147 | 0.6108 | 0.188 | 7.5e-10 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 6.8902 | 0.215 | 7.5e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 2.8917 | 0.315 | 7.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.2250 | 1.2600 | 0.179 | 7.5e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 1.7909 | 0.233 | 7.5e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 1.6828 | 0.813 | 7.5e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.9193 | 0.272 | 7.5e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 1.9543 | 0.256 | 7.5e-10 | 30/30 |
| Yitzhaki | 0.2632 | 0.9384 | 0.281 | 7.5e-10 | 30/30 |

Geometric-mean ratio **0.352** (bootstrap 95% CI 0.273–0.448), Wilcoxon signed-rank p = 3.0e-07, 24/25 problems below 1, 25/25 significant at 5% after Holm.

### Engine without dense blocks vs SCIPY_ND: `DE_NODENSE` / `SCIPY_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 6.5108 | 0.372 | 7.5e-10 | 30/30 |
| Cajas | 0.2090 | 0.6884 | 0.304 | 7.5e-10 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 2.1524 | 0.902 | 7.5e-10 | 30/30 |
| ConvexPlasticity | 0.0965 | 0.0717 | 1.346 | 7.5e-10 | 30/30 |
| FactorCovarianceModel | 0.3651 | 1.1643 | 0.314 | 7.5e-10 | 30/30 |
| HuberRegression | 1.0153 | 2.8496 | 0.356 | 7.5e-10 | 30/30 |
| LeastSquares | 0.9058 | 2.9113 | 0.311 | 7.5e-10 | 30/30 |
| Murray | 1.1783 | 1.2292 | 0.959 | 7.5e-10 | 30/30 |
| OptimalAdvertising | 0.8338 | 0.5945 | 1.403 | 7.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0273 | 0.0720 | 0.379 | 7.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0402 | 0.1269 | 0.317 | 7.5e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.7432 | 3.0301 | 0.245 | 7.5e-10 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 0.8040 | 0.834 | 7.5e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 1.6295 | 2.124 | 7.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.7434 | 2.6351 | 0.282 | 7.5e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 0.6312 | 0.644 | 7.5e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.1147 | 0.5547 | 0.207 | 7.5e-10 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 6.3001 | 0.235 | 7.5e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 2.9421 | 0.310 | 7.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.2250 | 1.1511 | 0.195 | 7.5e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 2.1850 | 0.191 | 7.5e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 1.8208 | 0.751 | 7.5e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.9123 | 0.274 | 7.5e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 1.9789 | 0.252 | 7.5e-10 | 30/30 |
| Yitzhaki | 0.2632 | 0.9819 | 0.268 | 7.5e-10 | 30/30 |

Geometric-mean ratio **0.424** (bootstrap 95% CI 0.329–0.558), Wilcoxon signed-rank p = 1.8e-05, 22/25 problems below 1, 25/25 significant at 5% after Holm.

### Engine without dense blocks vs COO_ND: `DE_NODENSE` / `COO_ND` (cold)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| CVaRBenchmark | 2.4225 | 6.5136 | 0.372 | 7.5e-10 | 30/30 |
| Cajas | 0.2090 | 0.6917 | 0.302 | 7.5e-10 | 30/30 |
| ConeMatrixStuffingBench | 1.9416 | 3.5379 | 0.549 | 7.5e-10 | 30/30 |
| ConvexPlasticity | 0.0965 | 0.0693 | 1.393 | 7.5e-10 | 30/30 |
| FactorCovarianceModel | 0.3651 | 1.1497 | 0.318 | 7.5e-10 | 30/30 |
| HuberRegression | 1.0153 | 2.7942 | 0.363 | 7.5e-10 | 30/30 |
| LeastSquares | 0.9058 | 2.9380 | 0.308 | 7.5e-10 | 30/30 |
| Murray | 1.1783 | 1.2237 | 0.963 | 7.5e-10 | 30/30 |
| OptimalAdvertising | 0.8338 | 0.5341 | 1.561 | 7.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0273 | 0.0886 | 0.308 | 7.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0402 | 0.1129 | 0.356 | 7.5e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.7432 | 2.9890 | 0.249 | 7.5e-10 | 30/30 |
| QuantumHilbertMatrix | 0.6709 | 0.7877 | 0.852 | 7.5e-10 | 30/30 |
| SDPSegfault1132Benchmark | 3.4617 | 7.2912 | 0.475 | 7.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.7434 | 2.7404 | 0.271 | 7.5e-10 | 30/30 |
| SemidefiniteProgramming | 0.4062 | 0.9954 | 0.408 | 7.5e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.1147 | 0.5235 | 0.219 | 7.5e-10 | 30/30 |
| SimpleLPBenchmark | 1.4836 | 5.9615 | 0.249 | 7.5e-10 | 30/30 |
| SimpleQPBenchmark | 0.9121 | 2.9272 | 0.312 | 7.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.2250 | 1.0872 | 0.207 | 7.5e-10 | 30/30 |
| SlowPruningBenchmark | 0.4175 | 2.1471 | 0.194 | 7.5e-10 | 30/30 |
| SmallMatrixStuffing | 1.3680 | 2.5064 | 0.546 | 7.5e-10 | 30/30 |
| TvInpainting | 0.2499 | 0.8144 | 0.307 | 7.5e-10 | 30/30 |
| UnconstrainedQP | 0.4993 | 2.4391 | 0.205 | 7.5e-10 | 30/30 |
| Yitzhaki | 0.2632 | 1.0055 | 0.262 | 7.5e-10 | 30/30 |

Geometric-mean ratio **0.381** (bootstrap 95% CI 0.311–0.482), Wilcoxon signed-rank p = 1.1e-06, 23/25 problems below 1, 25/25 significant at 5% after Holm.

### Dense blocks off: `de_cached_nodense` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.0023 | 0.2031 | 0.011 | 2.4e-10 | 30/30 |
| FactorCovarianceModel | 0.0871 | 0.0805 | 1.083 | 2.4e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0003 | 0.0003 | 0.986 | 5.5e-07 | 30/30 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0005 | 0.985 | 1.7e-06 | 30/30 |
| ParametrizedQPBenchmark | 0.4182 | 0.4202 | 0.995 | 0.205 | 30/30 |
| SVMWithL1Regularization | 0.1634 | 0.1522 | 1.073 | 2.4e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.0523 | 0.0525 | 0.997 | 3.9e-06 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1037 | 0.1039 | 0.999 | 0.205 | 30/30 |

Geometric-mean ratio **0.580** (bootstrap 95% CI 0.187–1.036), Wilcoxon signed-rank p = 0.547, 6/8 problems below 1, 6/8 significant at 5% after Holm.

### Split off: `de_cached_rebuild` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.4135 | 0.2031 | 2.036 | 2.4e-10 | 30/30 |
| FactorCovarianceModel | 0.1288 | 0.0805 | 1.600 | 2.4e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0027 | 0.0003 | 8.784 | 2.4e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0040 | 0.0005 | 8.499 | 2.4e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.5664 | 0.4202 | 1.348 | 2.4e-10 | 30/30 |
| SVMWithL1Regularization | 0.2712 | 0.1522 | 1.781 | 2.4e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.0839 | 0.0525 | 1.598 | 2.4e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1663 | 0.1039 | 1.601 | 2.4e-10 | 30/30 |

Geometric-mean ratio **2.493** (bootstrap 95% CI 1.601–4.502), Wilcoxon signed-rank p = 0.008, 0/8 problems below 1, 8/8 significant at 5% after Holm.

### Both off: `de_cached_nodense_rebuild` / `de_cached` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.0654 | 0.2031 | 0.322 | 2.4e-10 | 30/30 |
| FactorCovarianceModel | 0.3151 | 0.0805 | 3.914 | 2.4e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0027 | 0.0003 | 8.802 | 2.4e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0041 | 0.0005 | 8.643 | 2.4e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.5534 | 0.4202 | 1.317 | 2.4e-10 | 30/30 |
| SVMWithL1Regularization | 0.6049 | 0.1522 | 3.974 | 2.4e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.0836 | 0.0525 | 1.593 | 2.4e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1663 | 0.1039 | 1.601 | 2.4e-10 | 30/30 |

Geometric-mean ratio **2.446** (bootstrap 95% CI 1.181–4.759), Wilcoxon signed-rank p = 0.055, 1/8 problems below 1, 8/8 significant at 5% after Holm.

## Re-solves

### Engine re-solve vs dpp: `de_cached` / `dpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0805 | 0.0205 | 3.924 | 1.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.313 | 1.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0019 | 0.254 | 1.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.1522 | 0.0383 | 3.975 | 1.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1039 | 0.0627 | 1.657 | 1.5e-10 | 30/30 |

Geometric-mean ratio **1.155** (bootstrap 95% CI 0.402–3.319), Wilcoxon signed-rank p = –, 2/5 problems below 1, 5/5 significant at 5% after Holm.

### Engine re-solve vs dpp_coo: `de_cached` / `dpp_coo` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0805 | 0.0205 | 3.923 | 2.1e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.316 | 2.1e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0018 | 0.259 | 2.1e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.4202 | 0.2983 | 1.408 | 2.1e-10 | 30/30 |
| SVMWithL1Regularization | 0.1522 | 0.0383 | 3.977 | 2.1e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.0525 | 0.0466 | 1.125 | 2.1e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1039 | 0.0662 | 1.568 | 2.1e-10 | 30/30 |

Geometric-mean ratio **1.179** (bootstrap 95% CI 0.538–2.423), Wilcoxon signed-rank p = 0.469, 2/7 problems below 1, 7/7 significant at 5% after Holm.

### Engine re-solve vs dpp_scipy: `de_cached` / `dpp_scipy` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| FactorCovarianceModel | 0.0805 | 0.0205 | 3.927 | 1.5e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0003 | 0.0010 | 0.317 | 1.5e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0018 | 0.258 | 1.5e-10 | 30/30 |
| SVMWithL1Regularization | 0.1522 | 0.0383 | 3.978 | 1.5e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1039 | 0.0627 | 1.656 | 1.5e-10 | 30/30 |

Geometric-mean ratio **1.162** (bootstrap 95% CI 0.406–3.321), Wilcoxon signed-rank p = –, 2/5 problems below 1, 5/5 significant at 5% after Holm.

### Engine re-solve vs nodpp_cpp: `de_cached` / `nodpp_cpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| ConvexPlasticity | 0.2031 | 0.0432 | 4.697 | 2.4e-10 | 30/30 |
| FactorCovarianceModel | 0.0805 | 1.1483 | 0.070 | 2.4e-10 | 30/30 |
| ParamConeMatrixStuffing | 0.0003 | 0.0377 | 0.008 | 2.4e-10 | 30/30 |
| ParamSmallMatrixStuffing | 0.0005 | 0.0575 | 0.008 | 2.4e-10 | 30/30 |
| ParametrizedQPBenchmark | 0.4202 | 2.8681 | 0.146 | 2.4e-10 | 30/30 |
| SVMWithL1Regularization | 0.1522 | 2.6761 | 0.057 | 2.4e-10 | 30/30 |
| SimpleFullyParametrizedLPBenchmark | 0.0525 | 0.5840 | 0.090 | 2.4e-10 | 30/30 |
| SimpleScalarParametrizedLPBenchmark | 0.1039 | 1.2080 | 0.086 | 2.4e-10 | 30/30 |

Geometric-mean ratio **0.078** (bootstrap 95% CI 0.024–0.309), Wilcoxon signed-rank p = 0.016, 7/8 problems below 1, 8/8 significant at 5% after Holm.

## Non-DPP re-solves and first compiles (jury J1e, Legrain iii)

### Engine re-solve vs nodpp_cpp: `de_cached` / `nodpp_cpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0037 | 0.0489 | 0.075 | 1.2e-10 | 30/30 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0037 | 0.0491 | 0.075 | 1.2e-10 | 30/30 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.3150 | 0.084 | 1.2e-10 | 30/30 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.3149 | 0.084 | 1.2e-10 | 30/30 |

Geometric-mean ratio **0.079** (bootstrap 95% CI 0.075–0.084), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

### Engine re-solve vs nodpp_coo: `de_cached` / `nodpp_coo` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0037 | 0.0458 | 0.080 | 1.2e-10 | 30/30 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0037 | 0.0458 | 0.081 | 1.2e-10 | 30/30 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.3580 | 0.074 | 1.2e-10 | 30/30 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.3578 | 0.074 | 1.2e-10 | 30/30 |

Geometric-mean ratio **0.077** (bootstrap 95% CI 0.074–0.080), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

### Engine re-solve vs dpp: `de_cached` / `dpp` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0037 | 0.0012 | 2.953 | 6.0e-11 | 30/30 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.0064 | 4.119 | 6.0e-11 | 30/30 |

Geometric-mean ratio **3.488** (bootstrap 95% CI 2.953–4.119), Wilcoxon signed-rank p = –, 0/2 problems below 1, 2/2 significant at 5% after Holm.

### Engine re-solve vs de_cached_rebuild: `de_cached` / `de_cached_rebuild` (warm)

| problem | median num (s) | median den (s) | ratio | p (Holm) | n |
|---|---:|---:|---:|---:|---|
| factor_cov:variant=dpp:n=5000:seed=0 | 0.0037 | 0.0069 | 0.530 | 1.2e-10 | 30/30 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 0.0037 | 0.0070 | 0.529 | 1.2e-10 | 30/30 |
| lasso:variant=dpp:n=1000:seed=0 | 0.0264 | 0.0358 | 0.738 | 1.2e-10 | 30/30 |
| lasso:variant=nondpp:n=1000:seed=0 | 0.0264 | 0.0358 | 0.737 | 1.2e-10 | 30/30 |

Geometric-mean ratio **0.625** (bootstrap 95% CI 0.529–0.738), Wilcoxon signed-rank p = –, 4/4 problems below 1, 4/4 significant at 5% after Holm.

## Non-DPP set: first canonicalization, mean ± std (s)

| problem | n | m | nnz(A) | CPP_ND | SCIPY_ND | COO_ND | diffengine | best | ratio | p (Holm) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| factor_cov:variant=dpp:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.054 ± 3.6e-04 | 0.048 ± 2.4e-04 | 0.047 ± 1.8e-04 | 0.011 ± 4.9e-05 | COO_ND | 0.235 | 1.8e-10 |
| factor_cov:variant=free:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.054 ± 3.8e-04 | 0.048 ± 3.6e-04 | 0.047 ± 1.8e-04 | 0.011 ± 5.7e-05 | COO_ND | 0.233 | 1.8e-10 |
| factor_cov:variant=nondpp:n=5000:seed=0 | 15050 | 15052 | 290050 | 0.054 ± 1.5e-04 | 0.048 ± 2.0e-04 | 0.047 ± 1.6e-04 | 0.011 ± 7.7e-05 | COO_ND | 0.238 | 1.8e-10 |
| lasso:variant=dpp:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.339 ± 0.002 | 0.368 ± 8.9e-04 | 0.361 ± 7.7e-04 | 0.049 ± 4.9e-04 | CPP_ND | 0.145 | 1.8e-10 |
| lasso:variant=free:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.333 ± 8.9e-04 | 0.364 ± 8.9e-04 | 0.360 ± 0.002 | 0.049 ± 4.7e-04 | CPP_ND | 0.147 | 1.8e-10 |
| lasso:variant=nondpp:n=1000:seed=0 | 4000 | 4000 | 2006000 | 0.339 ± 0.001 | 0.368 ± 0.003 | 0.361 ± 8.6e-04 | 0.049 ± 4.7e-04 | CPP_ND | 0.145 | 1.8e-10 |

diffengine fastest on 6/6; geometric-mean ratio to the best backend **0.185** (95% CI 0.157–0.219), Wilcoxon p = 0.031; 6 problems significantly faster, 0 significantly slower (Holm, 5%).

## Scaling: 25 problems at s = 1/2, 1, 2

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | s 0.5 | s 1 | s 2 | nnz(A) range |
|---|---:|---:|---:|---|
| CVaRBenchmark | 0.56 | 0.53 | cap | 12,846,593–51,381,761 |
| Cajas | 0.28 | 0.30 | 0.26 | 990,034–3,894,133 |
| ConeMatrixStuffingBench | 0.31 | 0.30 | 0.29 | 3,536–7,072 |
| ConvexPlasticity | 5.40 | 7.31 | 8.82 | 36,000–144,000 |
| FactorCovarianceModel | 0.16 | 0.15 | 0.18 | 3,225,250–12,900,250 |
| HuberRegression | 0.19 | 0.18 | 0.17 | 6,765,987–27,040,636 |
| LeastSquares | 0.16 | 0.18 | 0.17 | 7,004,250–28,004,271 |
| Murray | 1.10 | 0.96 | 1.00 | 758,935–2,987,920 |
| OptimalAdvertising | 1.11 | 1.68 | 3.01 | 500,500–2,000,500 |
| ParamConeMatrixStuffing | 0.52 | 0.52 | 0.52 | 142–282 |
| ParamSmallMatrixStuffing | 0.52 | 0.52 | 0.51 | 212–424 |
| ParametrizedQPBenchmark | 0.23 | 0.25 | 0.23 | 7,208,008–28,813,363 |
| QuantumHilbertMatrix | 1.17 | 0.83 | cap | 1,560–81,072 |
| SDPSegfault1132Benchmark | 1.39 | 1.32 | cap | 501,736–2,023,126 |
| SVMWithL1Regularization | 0.16 | 0.15 | 0.15 | 6,290,001–25,152,501 |
| SemidefiniteProgramming | 0.61 | 0.64 | 0.64 | 1,211,331–4,862,506 |
| SimpleFullyParametrizedLPBenchmark | 0.22 | 0.22 | 0.21 | 1,000,000–4,000,000 |
| SimpleLPBenchmark | 0.20 | 0.19 | 0.18 | 10,000,000–40,000,000 |
| SimpleQPBenchmark | 0.15 | 0.16 | 0.16 | 6,420,687–25,648,842 |
| SimpleScalarParametrizedLPBenchmark | 0.22 | 0.21 | 0.20 | 2,000,000–8,000,000 |
| SlowPruningBenchmark | 0.22 | 0.23 | 0.22 | 4,200,000–16,800,000 |
| SmallMatrixStuffing | 0.30 | 0.30 | 0.27 | 2,828–5,656 |
| TvInpainting | 0.33 | 0.32 | 0.31 | 1,812,574–7,267,080 |
| UnconstrainedQP | 7.59 | 11.73 | 16.78 | 13,319–26,641 |
| Yitzhaki | 0.16 | 0.15 | 0.14 | 2,281,432–9,147,052 |

## Scaling: 10 families at five sizes

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | s 0.25 | s 0.5 | s 1 | s 2 | s 4 | nnz(A) range |
|---|---:|---:|---:|---:|---:|---|
| HuberRegression | 0.16 | 0.19 | 0.18 | 0.17 | 0.17 | 3,388,500–54,054,000 |
| FactorCovarianceModel | 0.17 | 0.16 | 0.15 | 0.18 | 0.22 | 1,612,750–25,800,250 |
| OptimalAdvertising | 0.80 | 1.11 | 1.68 | 3.01 | cap | 250,500–4,000,500 |
| SVMWithL1Regularization | 0.16 | 0.16 | 0.15 | 0.15 | 0.16 | 3,146,251–50,302,501 |
| LeastSquares | 0.16 | 0.16 | 0.18 | 0.17 | 0.18 | 3,503,500–56,014,000 |
| SimpleQPBenchmark | 0.15 | 0.15 | 0.16 | 0.16 | 0.16 | 3,216,000–51,264,000 |
| Yitzhaki | 0.14 | 0.16 | 0.15 | 0.14 | 0.14 | 1,139,950–18,329,500 |
| CVaRBenchmark | 0.59 | 0.56 | 0.53 | cap | cap | 6,424,065–51,381,761 |
| SemidefiniteProgramming | 0.58 | 0.61 | 0.64 | 0.64 | 0.68 | 611,050–9,704,200 |
| lasso | – | 0.16 | 0.15 | 0.15 | – | 503,000–8,012,000 |

## Density: 5 problems at five densities

diffengine / best CVXPY backend, medians of 5 replicates (s = 1 from the suite runs). “cap”: engine over the 20 GB cap. “unverified”: the correctness check did not fit in 20 GB, so the timing is not reported.

| problem | density 0.01 | density 0.05 | density 0.2 | density 0.5 | density 1 | nnz(A) range |
|---|---:|---:|---:|---:|---:|---|
| LeastSquares | 0.81 | 1.20 | 0.61 | 0.34 | 0.18 | 146,860–14,007,000 |
| HuberRegression | 2.54 | 1.78 | 0.67 | 0.34 | 0.18 | 161,911–13,527,000 |
| SVMWithL1Regularization | 0.72 | 1.47 | 0.64 | 0.33 | 0.15 | 202,469–12,577,501 |
| SimpleQPBenchmark | 0.41 | 0.63 | 0.47 | 0.30 | 0.16 | 159,980–12,832,000 |
| FactorCovarianceModel | 0.65 | 1.01 | 0.57 | 0.33 | 0.15 | 262,564–6,450,250 |
| Yitzhaki | 0.73 | 0.99 | 0.53 | 0.29 | 0.15 | 134,588–4,574,800 |
| SemidefiniteProgramming | 1.66 | 1.46 | 1.02 | 0.67 | 0.64 | 67,690–2,432,100 |
| lasso (n = 1000) | 0.86 | 0.58 | 0.59 | 0.33 | 0.15 | 25,872–2,006,000 |

## Phase breakdown of `DIFFENGINE` (cold), mean share of the time

| problem | time (s) | front end | convert | symbolic | numeric | assemble | format |
|---|---:|---:|---:|---:|---:|---:|---:|
| CVaRBenchmark | 3.4207 | 1% | 20% | 16% | 17% | 35% | 10% |
| Cajas | 0.2047 | 46% | 18% | 10% | 6% | 7% | 12% |
| ConeMatrixStuffingBench | 0.6420 | 68% | 24% | 0% | 8% | 0% | 0% |
| ConvexPlasticity | 0.5066 | 6% | 2% | 47% | 6% | 38% | 0% |
| FactorCovarianceModel | 0.1774 | 3% | 10% | 19% | 18% | 29% | 21% |
| HuberRegression | 0.4948 | 1% | 9% | 20% | 10% | 29% | 31% |
| LeastSquares | 0.4349 | 1% | 8% | 11% | 12% | 32% | 36% |
| Murray | 1.1805 | 0% | 94% | 2% | 1% | 1% | 1% |
| OptimalAdvertising | 0.9009 | 4% | 1% | 89% | 4% | 1% | 1% |
| ParamConeMatrixStuffing | 0.0224 | 84% | 14% | 1% | 1% | 1% | 1% |
| ParamSmallMatrixStuffing | 0.0327 | 84% | 14% | 1% | 1% | 0% | 0% |
| ParametrizedQPBenchmark | 0.7553 | 21% | 17% | 6% | 14% | 19% | 22% |
| QuantumHilbertMatrix | 0.6528 | 3% | 9% | 63% | 25% | 0% | 0% |
| SDPSegfault1132Benchmark | 2.1465 | 0% | 0% | 49% | 47% | 3% | 0% |
| SVMWithL1Regularization | 0.3875 | 3% | 7% | 19% | 28% | 23% | 20% |
| SemidefiniteProgramming | 0.4048 | 4% | 14% | 40% | 34% | 4% | 3% |
| SimpleFullyParametrizedLPBenchmark | 0.1151 | 10% | 6% | 22% | 16% | 12% | 35% |
| SimpleLPBenchmark | 1.1206 | 8% | 6% | 23% | 16% | 12% | 34% |
| SimpleQPBenchmark | 0.4528 | 1% | 9% | 15% | 14% | 35% | 26% |
| SimpleScalarParametrizedLPBenchmark | 0.2305 | 8% | 6% | 23% | 17% | 12% | 34% |
| SlowPruningBenchmark | 0.4079 | 2% | 1% | 36% | 11% | 20% | 31% |
| SmallMatrixStuffing | 0.5020 | 71% | 22% | 0% | 7% | 0% | 0% |
| TvInpainting | 0.2574 | 13% | 4% | 24% | 21% | 14% | 23% |
| UnconstrainedQP | 22.9368 | 0% | 0% | 2% | 98% | 0% | 0% |
| Yitzhaki | 0.1446 | 3% | 6% | 10% | 17% | 20% | 43% |

## Phase breakdown of `de_cached` (warm), mean share of the time

| problem | time (s) | front end | convert | symbolic | numeric | assemble | format |
|---|---:|---:|---:|---:|---:|---:|---:|
| ConvexPlasticity | 0.2056 | 0% | 0% | 0% | 12% | 88% | 0% |
| FactorCovarianceModel | 0.0822 | 3% | 0% | 0% | 4% | 50% | 44% |
| ParamConeMatrixStuffing | 0.0003 | 22% | 0% | 0% | 43% | 12% | 23% |
| ParamSmallMatrixStuffing | 0.0005 | 23% | 0% | 0% | 54% | 8% | 16% |
| ParametrizedQPBenchmark | 0.4276 | 15% | 0% | 0% | 20% | 28% | 37% |
| SVMWithL1Regularization | 0.1559 | 3% | 0% | 0% | 3% | 45% | 50% |
| SimpleFullyParametrizedLPBenchmark | 0.0532 | 3% | 0% | 0% | 11% | 19% | 66% |
| SimpleScalarParametrizedLPBenchmark | 0.1058 | 2% | 0% | 0% | 12% | 19% | 67% |

## Memory (cold): peak-RSS delta (MB), one measurement per cell

| problem | COO_ND | CPP_ND | DE_NODENSE | DIFFENGINE | SCIPY_ND |
|---|---:|---:|---:|---:|---:|
| CVaRBenchmark | 3587.0 | 4021.7 | 2115.0 | 10653.9 | 2804.0 |
| Cajas | 320.1 | 1192.7 | 342.2 | 341.0 | 298.3 |
| ConeMatrixStuffingBench | 3729.9 | 2009.8 | 1623.2 | 478.2 | 963.8 |
| ConvexPlasticity | 82.3 | 82.5 | 25.5 | 1329.5 | 82.5 |
| FactorCovarianceModel | 1334.0 | 1129.0 | 999.2 | 759.6 | 1046.7 |
| HuberRegression | 3121.5 | 2223.4 | 1865.5 | 1412.7 | 2245.7 |
| LeastSquares | 3020.7 | 2141.9 | 1893.4 | 1459.2 | 2326.8 |
| Murray | 305.3 | 2849.3 | 307.3 | 306.1 | 219.8 |
| OptimalAdvertising | 196.9 | 172.6 | 944.8 | 6066.2 | 181.7 |
| ParamConeMatrixStuffing | 12.2 | 9.8 | 5.8 | 5.9 | 8.2 |
| ParamSmallMatrixStuffing | 21.9 | 17.4 | 10.5 | 10.6 | 12.4 |
| ParametrizedQPBenchmark | 2997.9 | 2034.8 | 1775.3 | 1775.2 | 2173.9 |
| QuantumHilbertMatrix | 287.9 | 221.7 | 1194.5 | 1194.4 | 217.6 |
| SDPSegfault1132Benchmark | 15628.3 | 7536.4 | 12885.2 | 10413.2 | 3460.1 |
| SVMWithL1Regularization | 2904.4 | 1976.0 | 2416.9 | 2033.7 | 2041.5 |
| SemidefiniteProgramming | 640.0 | 1317.1 | 1137.7 | 1137.7 | 349.8 |
| SimpleFullyParametrizedLPBenchmark | 526.0 | 517.2 | 492.1 | 491.8 | 493.6 |
| SimpleLPBenchmark | 5027.5 | 5352.5 | 5056.7 | 4792.1 | 4960.7 |
| SimpleQPBenchmark | 3236.5 | 2194.1 | 2204.0 | 1654.9 | 2355.1 |
| SimpleScalarParametrizedLPBenchmark | 1067.9 | 1087.8 | 1008.8 | 1008.8 | 1024.1 |
| SlowPruningBenchmark | 1827.8 | 1351.8 | 1120.2 | 1796.9 | 1425.0 |
| SmallMatrixStuffing | 2405.1 | 1189.3 | 1117.0 | 322.1 | 634.0 |
| TvInpainting | 994.0 | 704.9 | 1048.2 | 1048.2 | 857.9 |
| UnconstrainedQP | 2105.0 | 1427.0 | 644.4 | 1754.2 | 1057.8 |
| Yitzhaki | 504.5 | 449.0 | 572.1 | 476.3 | 436.8 |
| lasso:variant=free:n=1000:density=0.01:seed=0 | – | – | 3.0 | 3.0 | – |
| lasso:variant=free:n=1000:density=0.02:seed=0 | – | – | 5.3 | 5.3 | – |
| lasso:variant=free:n=1000:density=0.05:seed=0 | – | – | 14.8 | 14.8 | – |
| lasso:variant=free:n=1000:density=0.1:seed=0 | – | – | 33.3 | 159.8 | – |
| lasso:variant=free:n=1000:density=0.2:seed=0 | – | – | 61.9 | 171.2 | – |
| lasso:variant=free:n=1000:density=0.5:seed=0 | – | – | 129.2 | 182.5 | – |
| scaled:cls=FactorCovarianceModel:density=0.01 | – | – | 73.7 | 72.6 | – |
| scaled:cls=FactorCovarianceModel:density=0.02 | – | – | 82.8 | 82.6 | – |
| scaled:cls=FactorCovarianceModel:density=0.05 | – | – | 108.6 | 597.4 | – |
| scaled:cls=FactorCovarianceModel:density=0.1 | – | – | 155.7 | 612.7 | – |
| scaled:cls=FactorCovarianceModel:density=0.2 | – | – | 256.3 | 631.8 | – |
| scaled:cls=FactorCovarianceModel:density=0.5 | – | – | 503.9 | 676.3 | – |
| scaled:cls=HuberRegression:density=0.01 | – | – | 30.5 | 30.5 | – |
| scaled:cls=HuberRegression:density=0.02 | – | – | 47.3 | 47.2 | – |
| scaled:cls=HuberRegression:density=0.05 | – | – | 102.4 | 1075.6 | – |
| scaled:cls=HuberRegression:density=0.1 | – | – | 190.2 | 1077.9 | – |
| scaled:cls=HuberRegression:density=0.2 | – | – | 393.7 | 1134.9 | – |
| scaled:cls=HuberRegression:density=0.5 | – | – | 877.6 | 1232.5 | – |
| scaled:cls=LeastSquares:density=0.01 | – | – | 26.4 | 26.3 | – |
| scaled:cls=LeastSquares:density=0.02 | – | – | 43.7 | 43.7 | – |
| scaled:cls=LeastSquares:density=0.05 | – | – | 102.1 | 1096.3 | – |
| scaled:cls=LeastSquares:density=0.1 | – | – | 200.6 | 1109.5 | – |
| scaled:cls=LeastSquares:density=0.2 | – | – | 404.8 | 1168.4 | – |
| scaled:cls=LeastSquares:density=0.5 | – | – | 887.4 | 1259.0 | – |
| scaled:cls=SVMWithL1Regularization:density=0.01 | – | – | 43.5 | 43.6 | – |
| scaled:cls=SVMWithL1Regularization:density=0.02 | – | – | 67.7 | 67.7 | – |
| scaled:cls=SVMWithL1Regularization:density=0.05 | – | – | 140.8 | 1722.0 | – |
| scaled:cls=SVMWithL1Regularization:density=0.1 | – | – | 258.1 | 1723.2 | – |
| scaled:cls=SVMWithL1Regularization:density=0.2 | – | – | 508.3 | 1776.6 | – |
| scaled:cls=SVMWithL1Regularization:density=0.5 | – | – | 1169.9 | 1866.8 | – |
| scaled:cls=SemidefiniteProgramming:density=0.01 | – | – | 1073.9 | 1073.9 | – |
| scaled:cls=SemidefiniteProgramming:density=0.02 | – | – | 1078.4 | 1076.6 | – |
| scaled:cls=SemidefiniteProgramming:density=0.05 | – | – | 1083.0 | 1081.6 | – |
| scaled:cls=SemidefiniteProgramming:density=0.1 | – | – | 1089.8 | 1089.8 | – |
| scaled:cls=SemidefiniteProgramming:density=0.2 | – | – | 1102.2 | 1102.1 | – |
| scaled:cls=SemidefiniteProgramming:density=0.5 | – | – | 1120.4 | 1120.5 | – |
| scaled:cls=SimpleQPBenchmark:density=0.01 | – | – | 316.5 | 257.8 | – |
| scaled:cls=SimpleQPBenchmark:density=0.02 | – | – | 336.9 | 276.8 | – |
| scaled:cls=SimpleQPBenchmark:density=0.05 | – | – | 405.0 | 1333.0 | – |
| scaled:cls=SimpleQPBenchmark:density=0.1 | – | – | 508.8 | 1337.7 | – |
| scaled:cls=SimpleQPBenchmark:density=0.2 | – | – | 680.5 | 1372.0 | – |
| scaled:cls=SimpleQPBenchmark:density=0.5 | – | – | 1192.0 | 1469.8 | – |
| scaled:cls=Yitzhaki:density=0.01 | – | – | 0.0 (floor) | 0.0 (floor) | – |
| scaled:cls=Yitzhaki:density=0.02 | – | – | 1.4 | 1.4 | – |
| scaled:cls=Yitzhaki:density=0.05 | – | – | 17.5 | 328.9 | – |
| scaled:cls=Yitzhaki:density=0.1 | – | – | 33.9 | 331.3 | – |
| scaled:cls=Yitzhaki:density=0.2 | – | – | 78.4 | 351.6 | – |
| scaled:cls=Yitzhaki:density=0.5 | – | – | 110.0 | 360.8 | – |
