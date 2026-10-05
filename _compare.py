"""Sparse-matrix equality used by the correctness gates.

Copied verbatim from the CasADi harness of SparseDifferentiation/Jacobian-accumulation
(canonicalization/casadi_compare.py), which this repo no longer carries.
"""
import numpy as np


def _sparse_close(M1, M2, tol=1e-9):
    if M1.shape != M2.shape:
        return False, f"shape {M1.shape} vs {M2.shape}"
    # Explicit stored zeros are a storage artifact (e.g. cvxpy keeps a dense
    # user-supplied D = H*eye block dense in P; DM constants may carry
    # structural zeros): compare modulo them, but report the count.
    A1, A2 = M1.tocsr(), M2.tocsr()
    nnz1, nnz2 = A1.nnz, A2.nnz
    A1.eliminate_zeros(); A2.eliminate_zeros()
    A1.sort_indices(); A2.sort_indices()
    n_explicit = (nnz1 - A1.nnz) + (nnz2 - A2.nnz)
    zeros_note = f" (modulo {n_explicit} explicit zeros)" if n_explicit else ""
    if not ((A1.indptr == A2.indptr).all() and (A1.indices == A2.indices).all()):
        d = abs(M1 - M2)
        err = d.max() if d.nnz else 0.0
        return False, f"pattern differs, max|diff|={err:.3g}"
    # identical NaNs (e.g. NaN already present in the problem data) count as equal
    close = np.isclose(A1.data, A2.data, rtol=tol, atol=tol, equal_nan=True)
    if close.all():
        diff = np.abs(A1.data - A2.data)
        err = np.nanmax(diff) if diff.size else 0.0
        return True, f"max|diff|={err:.3g}{zeros_note}"
    return False, f"{(~close).sum()}/{close.size} entries differ"

