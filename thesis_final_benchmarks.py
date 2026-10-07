"""
Final-deposit experiments of the thesis (jury J1, Legrain ii-vii).

One runner for every measurement of the revised Chapter 4. It reuses the helpers of
``run_backend_benchmarks.py`` (problem discovery, parameter assignment, the DPP
predicate of the chain, the kill-safe subprocess runner) and adds:

  * replicates: every measurement is repeated in a FRESH subprocess, up to
    BENCH_REPS (default 20) samples per (problem, target); a target whose first
    sample exceeds BENCH_SLOW_S (default 30 s) stops at BENCH_SLOW_REPS (default 5).
    Each replicate draws its parameter values from its own seed, so the
    parametric samples also vary the instance (jury J1c).
  * instance dimensions of the problem data (n, m, nnz(A), nnz(P), parameters).
  * the engine's phase breakdown (convert / symbolic / numeric / assemble /
    format), read from the instrumented fork (DIFFENGINE_PROFILE=1).
  * the two ablation switches of the fork, as targets:
        DIFFENGINE_NO_DENSE=1  no permuted dense blocks for constant data
        DIFFENGINE_REBUILD=1   conversion + symbolic pass repeated every solve
  * a memory mode (one subprocess per measurement, peak-RSS delta and the
    engine's own allocation counters) and a correctness mode.
  * the environment (machine, versions, BLAS) recorded in every output file.

Two interpreters are needed, because the fork forces parametrized problems onto
DIFFENGINE on the ignore_dpp path (see README, "ignore_dpp fairness"):
    .venv-thesis    the fork (Transurgeon/cvxpy@thesis-ablation) + engine
    .venv-upstream  cvxpy 1.9.2, for the CPP/SCIPY/COO baselines

Usage:
    python thesis_final_benchmarks.py time   --set suite --kind cold --targets ... --out F
    python thesis_final_benchmarks.py time   --set suite --kind warm --targets ... --out F
    python thesis_final_benchmarks.py memory --set suite --kind cold --targets ... --out F
    python thesis_final_benchmarks.py verify --set suite --out F       (fork venv)
--set is "suite", one of thesis_extra_problems.SETS, or a comma list of suite class
names / extra specs. See run_thesis_final.sh for the full sweep.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib
import json
import os
import platform
import subprocess
import sys
import time
import warnings
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_backend_benchmarks as rbb  # noqa: E402
import thesis_extra_problems as extra  # noqa: E402

REPS = int(os.environ.get("BENCH_REPS", "20"))
SLOW_S = float(os.environ.get("BENCH_SLOW_S", "30"))
SLOW_REPS = int(os.environ.get("BENCH_SLOW_REPS", "5"))
ITERS = int(os.environ.get("BENCH_ITERS", "5"))       # re-solves per warm replicate
TIMEOUT = float(os.environ.get("BENCH_TIMEOUT", "1800"))
SOLVER = rbb.COMPARE_SOLVER

# target -> (get_problem_data kwargs, environment of the ablation switches)
DE = {"canon_backend": "DIFFENGINE", "ignore_dpp": True}
DE_CACHED = {"canon_backend": "DIFFENGINE"}
NO_DENSE = {"DIFFENGINE_NO_DENSE": "1"}
REBUILD = {"DIFFENGINE_REBUILD": "1"}
TARGETS = {
    # -- cold: first canonicalization ------------------------------------- #
    "DIFFENGINE": (DE, {}),
    "DE_NODENSE": (DE, NO_DENSE),
    # Parameters evaluated first (EvalParams, inside the timer as in stock
    # ignore_dpp), then the parameter-free problem on DIFFENGINE. Under NO_DENSE
    # this is fully CSR: a parametric matrix has no CSR path in the engine, so
    # DE_NODENSE keeps dense classes on parametric problems.
    "DE_EVAL": (DE_CACHED, {}),
    "DE_NODENSE_EVAL": (DE_CACHED, NO_DENSE),
    "CPP_ND": ({"canon_backend": "CPP", "ignore_dpp": True}, {}),      # upstream
    "SCIPY_ND": ({"canon_backend": "SCIPY", "ignore_dpp": True}, {}),  # upstream
    "COO_ND": ({"canon_backend": "COO", "ignore_dpp": True}, {}),      # upstream
    "CPP": ({"canon_backend": "CPP"}, {}),       # DPP path: builds the tensor
    "SCIPY": ({"canon_backend": "SCIPY"}, {}),
    "COO": ({"canon_backend": "COO"}, {}),
    # -- warm: re-solves after a parameter update ------------------------- #
    # The 2x2 ablation: dense blocks (on/off) x symbolic/numeric split (on/off).
    "de_cached": (DE_CACHED, {}),
    "de_cached_nodense": (DE_CACHED, NO_DENSE),
    "de_cached_rebuild": (DE_CACHED, REBUILD),
    "de_cached_nodense_rebuild": (DE_CACHED, {**NO_DENSE, **REBUILD}),
    # CVXPY: the cached tensor (DPP problems only) or a full recompile.
    "dpp": ({"canon_backend": "CPP"}, {}),
    "dpp_scipy": ({"canon_backend": "SCIPY"}, {}),
    "dpp_coo": ({"canon_backend": "COO"}, {}),
    "nodpp_cpp": ({"canon_backend": "CPP", "ignore_dpp": True}, {}),
    "nodpp_scipy": ({"canon_backend": "SCIPY", "ignore_dpp": True}, {}),
    "nodpp_coo": ({"canon_backend": "COO", "ignore_dpp": True}, {}),
}
SWITCHES = ("DIFFENGINE_NO_DENSE", "DIFFENGINE_REBUILD")
EVAL_TARGETS = {"DE_EVAL", "DE_NODENSE_EVAL"}


def _evaluated(prob):
    """The problem with every parameter replaced by its value (stock ignore_dpp)."""
    from cvxpy.reductions.eval_params import EvalParams
    return EvalParams().apply(prob)[0]
REQUIRES_DPP = {"dpp", "dpp_scipy", "dpp_coo", "CPP", "SCIPY", "COO"}


# --------------------------------------------------------------------------- #
# Problems
# --------------------------------------------------------------------------- #
def problem_list(name):
    """[(module, class_or_spec)] for a --set argument."""
    if name == "suite":
        return [(m, c) for m, c, err in rbb.discover() if c is not None]
    if name in extra.SETS:
        return [("extra", s) for s in extra.SETS[name]]
    suite = {c: m for m, c, err in rbb.discover() if c is not None}
    return [(suite[x], x) if x in suite else ("extra", x)
            for x in name.split(",") if x]


def load_class(module, name):
    if module == "extra":
        return extra.make_class(name)
    sys.path.insert(0, str(rbb.BENCH_DIR))
    return getattr(importlib.import_module(module), name)


def fresh_problem(Cls, seed):
    """A new instance, with every parameter drawn from ``seed``.

    The suite's own setup() may leave parameters unset or fixed; drawing them per
    replicate makes each replicate a different instance of the problem family.
    The extra families keep their defaults on seed 0, so that their three
    variants produce the same data.
    """
    inst = Cls()
    inst.setup()
    prob = rbb._find_problem(inst)
    rng = np.random.default_rng(seed)
    is_extra = Cls.__module__ == extra.__name__
    for p in prob.parameters():
        if p.value is None or (seed != 0 and not is_extra):
            rbb._assign_param(p, rng)
    return prob, rng


def set_switches(env):
    for k in SWITCHES:
        os.environ.pop(k, None)
    os.environ.update(env)


def phases():
    try:
        from cvxpy.reductions.solvers.nlp_solvers.diff_engine import extractor
    except ImportError:
        return None
    return getattr(extractor, "PHASE_TIMES", None)


def dims(prob, data):
    A, P = data.get("A"), data.get("P")
    out = {"n": int(A.shape[1]) if A is not None else None,
           "m": int(A.shape[0]) if A is not None else None,
           "nnz_A": int(A.nnz) if A is not None else None,
           "nnz_P": int(P.nnz) if P is not None else 0,
           "n_vars_user": int(sum(v.size for v in prob.variables())),
           "n_param_objects": len(prob.parameters()),
           "n_param_entries": int(sum(p.size for p in prob.parameters()))}
    if A is not None and A.shape[0] and A.shape[1]:
        out["density_A"] = A.nnz / (A.shape[0] * A.shape[1])
    return out


# --------------------------------------------------------------------------- #
# Workers (one fresh process per replicate)
# --------------------------------------------------------------------------- #
def worker_time(module, name, kind, targets, seed, out_path):
    warnings.filterwarnings("ignore")
    os.environ["DIFFENGINE_PROFILE"] = "1"
    import cvxpy as cp  # noqa: F401

    res = {"module": module, "class": name, "kind": kind, "seed": seed, "targets": {}}

    def flush():
        Path(out_path).write_text(json.dumps(res))

    flush()
    Cls = load_class(module, name)
    ph = phases()
    for t in targets:
        kwargs, env = TARGETS[t]
        rec = res["targets"].setdefault(t, {})
        try:
            set_switches(env)
            prob, rng = fresh_problem(Cls, seed)
            if "is_dpp" not in res:
                res["is_dpp"] = rbb._chain_is_dpp(prob)
            params = prob.parameters()
            if t in REQUIRES_DPP and params and not rbb._chain_is_dpp(prob):
                rec["skip"] = "not DPP"
                continue
            if kind == "warm" and not params:
                rec["skip"] = "no parameters"
                continue
            if t in EVAL_TARGETS and (kind != "cold" or not params):
                rec["skip"] = "no parameters" if not params else "cold only"
                continue
            if ph is not None:
                ph.clear()
            t0 = time.perf_counter()
            if t in EVAL_TARGETS:
                data, _, _ = _evaluated(prob).get_problem_data(solver=SOLVER, **kwargs)
            else:
                data, _, _ = prob.get_problem_data(solver=SOLVER, **kwargs)
            first = time.perf_counter() - t0
            if "dims" not in res:
                res["dims"] = dims(prob, data)
            if kind == "cold":
                rec["time"] = first
                rec["phases"] = dict(ph) if ph else None
            else:
                times, phs = [], []
                for _ in range(ITERS):
                    for p in params:
                        rbb._assign_param(p, rng)
                    if ph is not None:
                        ph.clear()
                    t0 = time.perf_counter()
                    prob.get_problem_data(solver=SOLVER, **kwargs)
                    times.append(time.perf_counter() - t0)
                    phs.append(dict(ph) if ph else None)
                rec["first"] = first
                rec["iters"] = times
                rec["time"] = float(np.median(times))
                rec["phases"] = phs
        except Exception as exc:  # noqa: BLE001
            rec["error"] = f"{type(exc).__name__}: {exc}"[:200]
        finally:
            set_switches({})
        flush()
    res["done"] = True
    flush()


def worker_memory(module, name, kind, target, out_path):
    """One isolated peak-memory measurement (see rbb.run_memory_worker)."""
    warnings.filterwarnings("ignore")
    import cvxpy as cp  # noqa: F401

    kwargs, env = TARGETS[target]
    set_switches(env)
    res = {"module": module, "class": name, "kind": kind, "target": target}
    Cls = load_class(module, name)
    prob, rng = fresh_problem(Cls, 0)
    try:
        if kind == "warm":
            if not prob.parameters():
                res["skip"] = "no parameters"
                raise StopIteration
            prob.get_problem_data(solver=SOLVER, **kwargs)
        if target in EVAL_TARGETS and (kind != "cold" or not prob.parameters()):
            res["skip"] = "no parameters"
            raise StopIteration
        gc.collect()
        pre = rbb._maxrss_mb()
        eng_pre = rbb._engine_counters_mb()
        if target in EVAL_TARGETS:
            _evaluated(prob).get_problem_data(solver=SOLVER, **kwargs)
        elif kind == "cold":
            prob.get_problem_data(solver=SOLVER, **kwargs)
        else:
            for _ in range(ITERS):
                for p in prob.parameters():
                    rbb._assign_param(p, rng)
                prob.get_problem_data(solver=SOLVER, **kwargs)
        res["delta_mb"] = rbb._maxrss_mb() - pre
        res["floor"] = res["delta_mb"] <= 0
        res["engine_peak_mb"] = rbb._engine_counters_mb()[1]
        res["engine_pre_live_mb"] = eng_pre[0]
    except StopIteration:
        pass
    except Exception as exc:  # noqa: BLE001
        res["error"] = f"{type(exc).__name__}: {exc}"[:200]
    res["done"] = True
    Path(out_path).write_text(json.dumps(res))


def _split_nan(M):
    """(M with NaN entries zeroed, set of NaN positions). NaN enters only through
    the problem data (OptimalAdvertising: R_i = lognormal(0/0) when c_i rounds to 0)."""
    import scipy.sparse as sp

    if sp.issparse(M):
        M = sp.coo_matrix(M)
        bad = np.isnan(M.data)
        pos = set(zip(M.row[bad].tolist(), M.col[bad].tolist()))
        data = np.where(bad, 0.0, M.data)
        return sp.csr_matrix((data, (M.row, M.col)), shape=M.shape), pos
    M = np.asarray(M, dtype=float)
    bad = np.isnan(M)
    return np.where(bad, 0.0, M), set(map(tuple, np.argwhere(bad).tolist()))


def _sparse_close(M1, M2, tol=1e-9):
    """Same discipline as _compare._sparse_close (pattern check aside): equal modulo
    explicit zeros. NaN equals NaN at the same position; NaN anywhere else fails."""
    import scipy.sparse as sp

    (M1, n1), (M2, n2) = _split_nan(sp.csr_matrix(M1)), _split_nan(sp.csr_matrix(M2))
    if M1.shape != M2.shape:
        return False, float("inf"), 0
    M1.eliminate_zeros(); M2.eliminate_zeros()
    d = abs(M1 - M2)
    err = float(d.max()) if d.nnz else 0.0
    scale = max(float(abs(M1).max()) if M1.nnz else 0.0, 1.0)
    nan_diff = len(n1 ^ n2)
    return err <= tol * scale and not nan_diff, err, nan_diff


def _dense_close(v1, v2, tol=1e-9):
    (v1, n1), (v2, n2) = _split_nan(v1), _split_nan(v2)
    if v1.shape != v2.shape:
        return False, float("inf"), 0
    err = float(np.max(np.abs(v1 - v2), initial=0.0))
    scale = max(float(np.max(np.abs(v1), initial=0.0)), 1.0)
    nan_diff = len(n1 ^ n2)
    return err <= tol * scale and not nan_diff, err, nan_diff


def worker_verify(module, name, seed, out_path, only=None):
    """Correctness (Legrain vii): (P, c, A, b) of every engine target against the
    stock backends of the same interpreter, at the same parameter values, both on
    the first canonicalization and after a parameter update."""
    warnings.filterwarnings("ignore")
    import cvxpy as cp  # noqa: F401

    Cls = load_class(module, name)
    res = {"module": module, "class": name, "checks": {}}

    def data_for(target, update):
        if target in EVAL_TARGETS:
            kwargs, env = TARGETS[target]
            set_switches(env)
            try:
                prob, rng = fresh_problem(Cls, seed)
                if update:
                    upd = np.random.default_rng(seed + 1000)
                    for p in prob.parameters():
                        rbb._assign_param(p, upd)
                data, _, _ = _evaluated(prob).get_problem_data(solver=SOLVER, **kwargs)
                return data
            finally:
                set_switches({})
        if target.endswith("_EVAL"):
            # Stock reference for a parametric problem: the parameters are replaced
            # by their values (EvalParams, what ignore_dpp does in stock CVXPY) and
            # the parameter-free problem is canonicalized by a cvxcore backend. The
            # DPP tensor is never built: pinned CPP needs > 18 GB for it on
            # ParametrizedQP and SimpleFullyParametrizedLP.
            from cvxpy.reductions.eval_params import EvalParams
            prob, rng = fresh_problem(Cls, seed)
            if update:
                upd = np.random.default_rng(seed + 1000)
                for p in prob.parameters():
                    rbb._assign_param(p, upd)
            fixed = EvalParams().apply(prob)[0]
            data, _, _ = fixed.get_problem_data(
                solver=SOLVER, canon_backend=target[:-len("_EVAL")])
            return data
        kwargs, env = TARGETS[target]
        set_switches(env)
        try:
            prob, rng = fresh_problem(Cls, seed)
            data, _, _ = prob.get_problem_data(solver=SOLVER, **kwargs)
            if update and prob.parameters():
                upd = np.random.default_rng(seed + 1000)
                for p in prob.parameters():
                    rbb._assign_param(p, upd)
                data, _, _ = prob.get_problem_data(solver=SOLVER, **kwargs)
            return data
        finally:
            set_switches({})

    prob0, _ = fresh_problem(Cls, seed)
    parametric = bool(prob0.parameters())
    # Reference: CVXPY's CPP backend; for a parametric problem (DPP or not), CPP on
    # the problem with its parameters evaluated, which is the artefact of the
    # stock ignore_dpp baselines.
    suffix = "_EVAL" if parametric else ""
    ref_target = "CPP" + suffix
    engine = ["DIFFENGINE", "DE_NODENSE"] + (
        ["de_cached", "de_cached_nodense", "de_cached_rebuild",
         "de_cached_nodense_rebuild", "DE_EVAL", "DE_NODENSE_EVAL"] if parametric else [])
    stock = ["SCIPY" + suffix, "COO" + suffix]
    if only:
        engine = [t for t in engine if t in only]
        stock = [t for t in stock if t in only]
    for update in ([False, True] if parametric else [False]):
        tag = "update" if update else "first"
        try:
            ref = data_for(ref_target, update)
        except Exception as exc:  # noqa: BLE001
            res["checks"][f"{tag}:reference"] = f"ERR {type(exc).__name__}: {exc}"[:200]
            continue
        res.setdefault("reference", ref_target)
        for t in engine + stock:
            if t == res["reference"]:
                continue
            try:
                d = data_for(t, update)
                ok, errs, nans = True, {}, {}
                for key in ("P", "A", "c", "b"):
                    if ref.get(key) is None and d.get(key) is None:
                        continue
                    close = _sparse_close if key in ("P", "A") else _dense_close
                    k_ok, err, nan_diff = close(ref[key], d[key])
                    ok &= k_ok
                    errs[key] = err
                    if nan_diff:
                        nans[key] = nan_diff
                rec = {"ok": bool(ok), "max_abs_err": errs}
                if nans:
                    rec["nan_mismatch"] = nans
                res["checks"][f"{tag}:{t}"] = rec
            except Exception as exc:  # noqa: BLE001
                res["checks"][f"{tag}:{t}"] = f"ERR {type(exc).__name__}: {exc}"[:200]
    res["done"] = True
    Path(out_path).write_text(json.dumps(res, default=float))


# --------------------------------------------------------------------------- #
# Parent
# --------------------------------------------------------------------------- #
ENGINE_TARGET_PREFIXES = ("DIFFENGINE", "DE_", "de_")


def _built_engine_commit():
    """The engine commit envs/setup_fork.sh compiled into this venv (None if the
    venv was not built by it, e.g. a PyPI sparsediffpy wheel)."""
    stamp = Path(sys.prefix) / "ENGINE_COMMIT"
    return stamp.read_text().strip() if stamp.exists() else None


def check_engine(mode, targets):
    """Refuse to time or verify engine targets on an engine other than ENGINE_COMMIT.

    The engine build is only knowable from the stamp setup_fork.sh writes; a PyPI
    wheel has none. Set BENCH_ALLOW_ANY_ENGINE=1 to run anyway (the recorded
    environment then still shows engine_built_commit=None)."""
    if os.environ.get("BENCH_ALLOW_ANY_ENGINE") == "1":
        return
    if mode != "verify" and not any(t.startswith(ENGINE_TARGET_PREFIXES) for t in targets):
        return  # stock baselines only (.venv-upstream)
    want, have = os.environ.get("ENGINE_COMMIT"), _built_engine_commit()
    if not want or not have or not (want.startswith(have) or have.startswith(want)):
        sys.exit(f"engine mismatch: ENGINE_COMMIT={want!r} but this venv was built "
                 f"from {have!r} ({Path(sys.prefix) / 'ENGINE_COMMIT'}). "
                 f"Rebuild with envs/setup_fork.sh, or set BENCH_ALLOW_ANY_ENGINE=1.")


def environment():
    import importlib.metadata as md

    env = {"platform": platform.platform(), "machine": platform.machine(),
           "python": platform.python_version(), "executable": sys.executable,
           "threads": {k: os.environ.get(k) for k in (
               "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")}}
    try:
        env["cpu"] = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"],
                                    capture_output=True, text=True).stdout.strip()
    except OSError:
        pass
    for pkg in ("cvxpy", "sparsediffpy", "numpy", "scipy", "clarabel"):
        try:
            env[pkg] = md.version(pkg)
        except md.PackageNotFoundError:
            env[pkg] = None
    try:
        import cvxpy

        root = Path(cvxpy.__file__).resolve().parents[1]
        if (root / ".git").exists():  # an editable checkout, not site-packages
            env["cvxpy_git"] = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "HEAD"],
                capture_output=True, text=True).stdout.strip()
        else:  # installed from a git URL (envs/setup_fork.sh): pip records the commit
            url = json.loads(md.distribution("cvxpy").read_text("direct_url.json") or "{}")
            env["cvxpy_git"] = url.get("vcs_info", {}).get("commit_id")
    except Exception:  # noqa: BLE001
        pass
    try:
        env["numpy_blas_build"] = np.__config__.CONFIG["Build Dependencies"]["blas"]["name"]
    except Exception:  # noqa: BLE001
        pass
    try:
        import sparsediffpy._sparsediffengine as se

        links = subprocess.run(["otool", "-L", se.__file__], capture_output=True,
                               text=True).stdout
        env["engine_blas"] = sorted({ln.split()[0] for ln in links.splitlines()[1:]
                                     if any(k in ln.lower() for k in
                                            ("accelerate", "blas", "lapack", "mkl"))})
        env["engine_built_commit"] = _built_engine_commit()
        env["engine_commit"] = (os.environ.get("ENGINE_COMMIT")
                                if env["engine_built_commit"] else None)
        env["engine_so_sha256"] = hashlib.sha256(Path(se.__file__).read_bytes()).hexdigest()
    except Exception:  # noqa: BLE001
        pass
    try:
        from threadpoolctl import threadpool_info

        env["numpy_blas"] = [{k: i.get(k) for k in ("internal_api", "version",
                                                     "num_threads")}
                             for i in threadpool_info()]
    except Exception:  # noqa: BLE001
        pass
    return env


def _spawn(args, out):
    if out.exists():
        out.unlink()
    status = rbb._run_worker_subprocess([sys.executable, __file__, *args], TIMEOUT,
                                        stderr_path=HERE / "_thesis_worker_stderr.log")
    if status != "ok":
        what = " ".join(a for a in args[2:] if not a.endswith(".json"))
        print(f"  worker {what}: {status}", flush=True)
    try:
        return json.loads(out.read_text()), status
    except Exception:  # noqa: BLE001
        return {}, status


def run_time(problems, kind, targets, out):
    tmp = HERE / "_thesis_worker.json"
    rows = json.loads(out.read_text())["rows"] if out.exists() else []
    done = {(r["module"], r["class"]) for r in rows}
    meta = {"environment": environment(), "kind": kind, "targets": targets,
            "reps": REPS, "slow_s": SLOW_S, "slow_reps": SLOW_REPS, "iters": ITERS}
    for module, name in problems:
        if (module, name) in done:
            continue
        print(f"[{kind}] {name}", flush=True)
        row = {"module": module, "class": name, "samples": {t: [] for t in targets},
               "status": {}}
        want = {t: REPS for t in targets}
        seed = 0
        split = False  # once a shared worker fails, give each target its own
        while any(len(row["samples"][t]) < want[t] and t not in row["status"]
                  for t in targets):
            todo = [t for t in targets
                    if len(row["samples"][t]) < want[t] and t not in row["status"]]
            if split and len(todo) > 1:
                status = "split"
            else:
                res, status = _spawn(["--worker-time", module, name, kind, ",".join(todo),
                                      str(seed), str(tmp)], tmp)
            if status != "ok" and len(todo) > 1:
                split = True
                # One target timed out or crashed and took the worker down; rerun
                # each target alone so a slow ablation variant (e.g. DE_NODENSE on
                # SimpleLP, O(n^2)) cannot cost the others their sample.
                res, per_status = {"targets": {}}, {}
                for t in todo:
                    r1, st1 = _spawn(["--worker-time", module, name, kind, t,
                                      str(seed), str(tmp)], tmp)
                    for k in ("is_dpp", "dims"):
                        if k in r1:
                            res.setdefault(k, r1[k])
                    if t in r1.get("targets", {}):
                        res["targets"][t] = r1["targets"][t]
                    per_status[t] = st1
            else:
                per_status = {t: status for t in todo}
            for k in ("is_dpp", "dims"):
                if k in res and k not in row:
                    row[k] = res[k]
            for t in todo:
                rec = res.get("targets", {}).get(t)
                if rec is None:
                    row["status"][t] = per_status[t] if per_status[t] != "ok" else \
                        "crashed: " + rbb._stderr_tail(HERE / "_thesis_worker_stderr.log")
                elif "skip" in rec or "error" in rec:
                    row["status"][t] = rec.get("skip") or rec.get("error")
                else:
                    row["samples"][t].append({"seed": seed, **rec})
                    if len(row["samples"][t]) == 1 and rec["time"] > SLOW_S:
                        want[t] = min(want[t], SLOW_REPS)
            seed += 1
        rows.append(row)
        out.write_text(json.dumps({"meta": meta, "rows": rows}, indent=1))
    out.write_text(json.dumps({"meta": meta, "rows": rows}, indent=1))
    if tmp.exists():
        tmp.unlink()


def run_memory(problems, kind, targets, out):
    tmp = HERE / "_thesis_worker.json"
    rows = json.loads(out.read_text())["rows"] if out.exists() else []
    done = {(r["module"], r["class"]) for r in rows}
    meta = {"environment": environment(), "kind": kind, "targets": targets,
            "iters": ITERS}
    for module, name in problems:
        if (module, name) in done:
            continue
        print(f"[memory {kind}] {name}", flush=True)
        row = {"module": module, "class": name, "targets": {}}
        for t in targets:
            res, status = _spawn(["--worker-memory", module, name, kind, t, str(tmp)], tmp)
            row["targets"][t] = res if res else {"error": status}
        rows.append(row)
        out.write_text(json.dumps({"meta": meta, "rows": rows}, indent=1))


VERIFY_TARGETS = ("DIFFENGINE", "DE_NODENSE", "de_cached", "de_cached_nodense",
                  "de_cached_rebuild", "de_cached_nodense_rebuild", "SCIPY", "COO",
                  "SCIPY_EVAL", "COO_EVAL", "DE_EVAL", "DE_NODENSE_EVAL")


def run_verify(problems, out):
    tmp = HERE / "_thesis_worker.json"
    # Resumes like the other modes, but only from a file of the same build.
    meta = {"environment": environment()}
    rows = []
    if out.exists():
        prev = json.loads(out.read_text())
        same = all(prev.get("meta", {}).get("environment", {}).get(k) == meta["environment"].get(k)
                   for k in ("cvxpy_git", "engine_commit", "engine_so_sha256"))
        rows = prev.get("rows", []) if same else []
    done = {(r.get("module"), r.get("class")) for r in rows}
    for module, name in problems:
        if (module, name) in done:
            continue
        print(f"[verify] {name}", flush=True)
        res, status = _spawn(["--worker-verify", module, name, "0", str(tmp)], tmp)
        if status != "ok":
            # A target timed out or crashed: check each one in its own worker, so
            # only that target is reported as failed.
            res = {"module": module, "class": name, "checks": {}, "worker": status}
            for t in VERIFY_TARGETS:
                r1, st1 = _spawn(["--worker-verify", module, name, "0", str(tmp), t], tmp)
                res.setdefault("reference", r1.get("reference"))
                res["checks"].update(r1.get("checks", {}))
                if st1 != "ok" and not any(k.endswith(":" + t) for k in r1.get("checks", {})):
                    res["checks"][f"first:{t}"] = f"ERR {st1}"
            res["done"] = True
        rows.append(res if res else {"module": module, "class": name, "error": status})
        out.write_text(json.dumps({"meta": meta, "rows": rows}, indent=1))


def main():
    if len(sys.argv) > 1 and sys.argv[1].startswith("--worker"):
        mode, *a = sys.argv[1:]
        if mode == "--worker-time":
            module, name, kind, targets, seed, out = a
            worker_time(module, name, kind, targets.split(","), int(seed), out)
        elif mode == "--worker-memory":
            worker_memory(*a)
        elif mode == "--worker-verify":
            module, name, seed, out, *only = a
            worker_verify(module, name, int(seed), out,
                          set(only[0].split(",")) if only else None)
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["time", "memory", "verify"])
    ap.add_argument("--set", default="suite")
    ap.add_argument("--kind", choices=["cold", "warm"], default="cold")
    ap.add_argument("--targets", default="")
    ap.add_argument("--skip", default="")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    problems = problem_list(args.set)
    skip = {s for s in args.skip.split(",") if s}
    problems = [(m, c) for m, c in problems if c not in skip]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    targets = [t for t in args.targets.split(",") if t]
    check_engine(args.mode, targets)
    if args.mode == "time":
        run_time(problems, args.kind, targets, out)
    elif args.mode == "memory":
        run_memory(problems, args.kind, targets, out)
    else:
        run_verify(problems, out)


if __name__ == "__main__":
    main()
