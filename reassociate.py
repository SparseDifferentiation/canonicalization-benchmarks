"""
The matmul reassociation of CVXPY PR #3524, applied to a whole Problem.

#3524 rewrites matmul chains that end in a parameter-free constant inside the
DIFFENGINE converter only. To credit the rewrite to neither side, the benchmark can
apply the same rewrite to the problem itself before a stock cvxcore backend (CPP, SCIPY,
COO) canonicalizes it. The rules are the PR's (diff_engine/converters.py,
_apply_constant_right / _normalize_matmul):

    constant @ c   -> Constant(value)
    (A @ B) @ c    -> A @ (B @ c)
    (-E) @ c       -> -(E @ c)
    (E1 + E2) @ c  -> E1 @ c + E2 @ c   (vector c only)

applied bottom-up over the objective and every constraint. Only parameter-free
constants fold, and a chain whose left factor is not 2-D is left alone (numpy's 1-D
matmul collapse). The result is mathematically the same problem; the benchmark checks
that its (P, c, A, b) matches the original's.

Works on stock cvxpy 1.9.2 and on the fork.
"""
from __future__ import annotations

import operator
from functools import reduce

import cvxpy as cp
from cvxpy.expressions.constants import Constant
from cvxpy.expressions.leaf import Leaf


def _is_plain_constant(expr):
    return expr.is_constant() and not expr.parameters()


def _is_vector(expr):
    return len(expr.shape) <= 1 or min(expr.shape) == 1


def _apply_constant_right(left, c):
    if _is_plain_constant(left):
        return Constant(left.value @ c.value)
    name = type(left).__name__
    if name == "MulExpression":
        a, b = left.args
        if _is_plain_constant(b):
            return _apply_constant_right(a, Constant(b.value @ c.value))
        if _is_vector(c):
            return a @ _apply_constant_right(b, c)
        if _is_plain_constant(a):
            return a @ (b @ c)
        return left @ c
    if name == "NegExpression":
        return -_apply_constant_right(left.args[0], c)
    if (name == "AddExpression" and _is_vector(c)
            and all(arg.shape == left.shape for arg in left.args)):
        return reduce(operator.add, [_apply_constant_right(arg, c) for arg in left.args])
    return left @ c


def _normalize_matmul(expr):
    left, right = expr.args
    if len(left.shape) != 2:
        return expr
    if _is_plain_constant(right) and not left.is_constant():
        return _apply_constant_right(left, right)
    return expr


class _State:
    def __init__(self):
        self.fired = 0
        self.done = {}   # id(node) -> rewritten node (keeps every visited node alive)


def _rewrite(expr, st):
    if isinstance(expr, Leaf):
        return expr
    hit = st.done.get(id(expr))
    if hit is not None:
        return hit[1]
    args = [_rewrite(a, st) for a in expr.args]
    out = expr.copy(args) if any(n is not o for n, o in zip(args, expr.args)) else expr
    if type(out).__name__ == "MulExpression":
        new = _normalize_matmul(out)
        is_mul = type(new).__name__ == "MulExpression"
        if is_mul and new.args[0] is out.args[0] and new.args[1] is out.args[1]:
            pass  # no rule applied (the fallback rebuilds the same left @ c)
        elif is_mul:
            # As in the PR's converter: the node stays a matmul and only its factors,
            # which the rule may have created, are visited again (memoized nodes are
            # returned as they are).
            st.fired += 1
            args = [_rewrite(a, st) for a in new.args]
            out = new.copy(args) if any(n is not o for n, o in zip(args, new.args)) else new
        else:
            st.fired += 1
            out = _rewrite(new, st)
    st.done[id(expr)] = (expr, out)
    st.done[id(out)] = (out, out)
    return out


def reassociate(problem):
    """(rewritten Problem, number of rewrites). The input is not modified."""
    st = _State()
    obj = problem.objective
    new_obj = type(obj)(_rewrite(obj.args[0], st))
    cons = [c.copy([_rewrite(a, st) for a in c.args]) for c in problem.constraints]
    return cp.Problem(new_obj, cons), st.fired
