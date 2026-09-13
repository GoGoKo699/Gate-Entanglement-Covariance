"""Numerical series for the theorem in theory/THEOREM.md.

The gate basis is |a,b>, with a in range(r), b in range(s), and b the
fast index. Realignment uses R[(a,c),(b,e)] = U[(a,b),(c,e)]. The r and s
dimensions are the fixed active factors, not the growing half-dimension d.
"""
from numbers import Integral

import numpy as np


def _positive_integer(value, name, minimum=1):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral):
        raise ValueError(f"{name} must be an integer >= {minimum}.")
    if value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}.")
    return int(value)


def _order(value):
    if isinstance(value, (bool, np.bool_)) or not np.isscalar(value) or np.iscomplexobj(value):
        raise ValueError("Entropy order must be a finite positive real scalar.")
    try:
        alpha = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("Entropy order must be a finite positive real scalar.") from exc
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError("Entropy order must be a finite positive real scalar.")
    return alpha


def _probabilities(values):
    raw = np.asarray(values)
    if np.iscomplexobj(raw):
        raise ValueError("Probabilities must be a real normalized vector.")
    eta = np.asarray(raw, dtype=float)
    if eta.ndim != 1 or eta.size == 0 or not np.all(np.isfinite(eta)):
        raise ValueError("Probabilities must be a nonempty finite vector.")
    if np.any(eta < 0) or np.any(eta > 1):
        raise ValueError("Probabilities must lie in [0, 1].")
    if not np.isclose(eta.sum(), 1, atol=1e-12, rtol=0):
        raise ValueError("Probabilities must sum to one.")
    return eta


def operator_schmidt_probabilities(unitary, r, s, *, atol=1e-12):
    """Return descending normalized operator Schmidt probabilities.

    Validate a unitary on C^r tensor C^s. Return min(r^2,s^2) entries,
    including numerical zero entries; no small channel is discarded.
    A final normalization removes only roundoff in the SVD sum.
    """
    r = _positive_integer(r, "r")
    s = _positive_integer(s, "s")
    if not np.isfinite(atol) or atol <= 0:
        raise ValueError("atol must be finite and positive.")
    gate = np.asarray(unitary, dtype=complex)
    if gate.shape != (r*s, r*s) or not np.all(np.isfinite(gate)):
        raise ValueError(f"Expected a finite {(r*s, r*s)} gate matrix.")
    error = np.max(np.abs(gate.conj().T @ gate - np.eye(r*s)))
    if error > atol:
        raise ValueError(f"Gate is not unitary within atol (error={error:.3g}).")
    realigned = gate.reshape(r, s, r, s).transpose(0, 2, 1, 3).reshape(r*r, s*s)
    eta = np.linalg.svd(realigned, compute_uv=False)**2 / (r*s)
    return eta / eta.sum()


def coefficients(alpha, cutoff):
    """Return modes k=2,...,cutoff and entropy coefficients c_alpha,k.

    The recurrence includes alpha=1 continuously. At an integer alpha>=2
    it terminates exactly after mode alpha. For other positive orders a
    finite cutoff is an approximation to an infinite convergent series.
    """
    alpha = _order(alpha)
    cutoff = _positive_integer(cutoff, "cutoff", minimum=2)
    modes = np.arange(2, cutoff+1, dtype=float)
    coeff = np.empty(cutoff-1)
    coeff[0] = -2*(alpha/(alpha+2))
    coeff[1:] = coeff[0] * np.cumprod((alpha-modes[:-1])/(alpha+modes[:-1]+1))
    return modes, coeff


def covariance(alpha, beta, probabilities, *, cutoff):
    """Truncated coefficient lim d^2 Cov(S_alpha(U_l psi), S_beta(U_m psi)).

    Supply the operator Schmidt probabilities of U_l U_m^dagger. Passing
    a normalized vector alone does not assert that it is a physical gate
    spectrum. Omitted series terms and finite-d bias are distinct errors;
    this function supplies no bound on either.
    """
    eta = _probabilities(probabilities)
    modes, ca = coefficients(alpha, cutoff)
    _, cb = coefficients(beta, cutoff)
    kernel = np.sum(eta[:, None]**modes[None, :], axis=0)
    return float(0.25 * np.sum(modes*ca*cb*kernel))


def same_order_covariance(alpha, probabilities, *, cutoff):
    """Truncated same-order covariance coefficient, using natural logarithms."""
    return covariance(alpha, alpha, probabilities, cutoff=cutoff)


def correlation(alpha, beta, probabilities, *, cutoff):
    """Normalize the truncated cross covariance by its marginal variances.

    For alpha=beta this is the retained entropy correlation. All three
    series use the same cutoff. Doubling it is a numerical diagnostic,
    not a rigorous remainder bound or a bound on finite-dimensional bias.
    """
    value = covariance(alpha, beta, probabilities, cutoff=cutoff)
    va = same_order_covariance(alpha, [1.0], cutoff=cutoff)
    vb = same_order_covariance(beta, [1.0], cutoff=cutoff)
    if not np.isfinite(va) or not np.isfinite(vb) or va <= 0 or vb <= 0:
        raise FloatingPointError("The marginal variance is unresolved in floating-point arithmetic at this order.")
    return float(value / (np.sqrt(va)*np.sqrt(vb)))


def spatial_correlation_bound(alpha, r, s, *, cutoff):
    """Evaluate the fixed-access lower-bound series at rank min(r^2,s^2).

    This returns a truncated ratio. Equal active dimensions admit exact
    saturation of the infinite-series bound by dual-unitary gates.
    """
    r = _positive_integer(r, "r")
    s = _positive_integer(s, "s")
    rank = min(r*r, s*s)
    return correlation(alpha, alpha, np.full(rank, 1/rank), cutoff=cutoff)
