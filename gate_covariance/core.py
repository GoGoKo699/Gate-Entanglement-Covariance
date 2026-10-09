"""Numerical series for the theorem in theory/THEOREM.md.

The gate basis is |a,b>, with a in range(r), b in range(s), and b the
fast index. Realignment uses R[(a,c),(b,e)] = U[(a,b),(c,e)]. The r and s
dimensions are the fixed active factors, not the growing half-dimension d.
"""
from numbers import Integral

import numpy as np

# These are implementation limits, not restrictions on the fixed-order theorem.
_MAX_ORDER = 2**50
_MAX_CUTOFF = 1_000_000
_MAX_KERNEL_WORK = 50_000_000


def _positive_integer(value, name, minimum=1):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral):
        raise ValueError(f"{name} must be an integer >= {minimum}.")
    if value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}.")
    return int(value)


def _order(value):
    if (isinstance(value, (bool, np.bool_, str, bytes))
            or not np.isscalar(value) or np.iscomplexobj(value)):
        raise ValueError("Entropy order must be a finite positive real scalar.")
    try:
        alpha = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("Entropy order must be a finite positive real scalar.") from exc
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError("Entropy order must be a finite positive real scalar.")
    if alpha >= _MAX_ORDER:
        raise FloatingPointError("Orders >= 2**50 are unsupported by the binary64 recurrence.")
    # Converting a higher-precision scalar must not create false termination.
    if alpha.is_integer() and value != alpha:
        raise FloatingPointError("Conversion to binary64 would round this order to an integer.")
    return alpha


def _cutoff(value):
    cutoff = _positive_integer(value, "cutoff", minimum=2)
    if cutoff > _MAX_CUTOFF:
        raise FloatingPointError("Cutoffs above 1,000,000 exceed the supported array budget.")
    return cutoff


def _positive_result(value, quantity):
    if not np.isfinite(value) or value <= 0:
        raise FloatingPointError(
            f"The positive {quantity} is unresolved in binary64 arithmetic; "
            "a numerical zero is not mathematical termination.")
    return float(value)


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


def _coefficient_sequence(alpha, cutoff):
    """Shared recurrence after scalar validation, also used at the tail boundary."""
    modes = np.arange(2, cutoff+1, dtype=float)
    coeff = np.zeros(cutoff-1)
    # Only an exactly represented integer >= 2 terminates mathematically.
    final_mode = min(cutoff, int(alpha)) if alpha >= 2 and alpha.is_integer() else cutoff
    coeff[0] = -2*alpha/(alpha+2)
    if final_mode > 2:
        k = modes[:final_mode-2]
        try:
            with np.errstate(under="raise", over="raise", invalid="raise"):
                coeff[1:final_mode-1] = coeff[0] * np.cumprod((alpha-k)/(alpha+k+1))
        except FloatingPointError as exc:
            raise FloatingPointError(
                "The entropy coefficient recurrence underflowed or overflowed; "
                "this is not mathematical termination.") from exc
    active = coeff[:final_mode-1]
    if not np.all(np.isfinite(active)) or np.any(abs(active) < np.finfo(float).tiny):
        raise FloatingPointError(
            "A nonzero entropy coefficient underflowed or overflowed in binary64; "
            "this is not mathematical termination.")
    return modes, coeff


def coefficients(alpha, cutoff):
    """Return modes k=2,...,cutoff and entropy coefficients c_alpha,k.

    The recurrence includes alpha=1 continuously. Only an exactly represented
    integer alpha>=2 terminates after mode alpha; nearby orders do not. The
    implementation supports 0<alpha<2**50 and 2<=cutoff<=1,000,000. It raises
    FloatingPointError on recurrence underflow or subnormal coefficients.
    These numerical/resource restrictions are not mathematical order limits.
    """
    return _coefficient_sequence(_order(alpha), _cutoff(cutoff))


def marginal_variance(alpha):
    """Closed limiting coefficient V_alpha=alpha/4 (natural logarithms).

    This is not a finite-d variance and uses no series cutoff.
    """
    return _positive_result(_order(alpha)/4, "marginal variance")


def same_state_covariance(alpha, beta):
    """Closed limiting covariance alpha*beta/[2*(alpha+beta)] on one Haar state.

    Both entropy orders are evaluated on the SAME state. This is neither an
    independent-state covariance nor a nontrivial-gate formula. The stable
    evaluation below avoids forming alpha*beta or alpha+beta.
    """
    low, high = sorted((_order(alpha), _order(beta)))
    return _positive_result(low/(2*(1+low/high)), "same-state covariance")


def marginal_tail(alpha, cutoff):
    """Evaluate the exact omitted marginal variance after mode cutoff.

    Mathematically tau=(cutoff+1+alpha)^2*c[cutoff+1]^2/(16*alpha).
    A returned float evaluates this proved identity; it is NOT an outward-
    rounded certificate. Zero is returned only for exact integer termination.
    Positive coefficients or remainders that underflow raise FloatingPointError.
    Roundoff, spectrum errors, finite-d bias and sample errors are not enclosed.
    """
    alpha, cutoff = _order(alpha), _cutoff(cutoff)
    if alpha >= 2 and alpha.is_integer() and cutoff >= alpha:
        return 0.0
    _, coeff = _coefficient_sequence(alpha, cutoff+1)
    # Scale before squaring so small orders need not underflow at c^2.
    scaled = abs(coeff[-1])*((cutoff+1+alpha)/(4*np.sqrt(alpha)))
    with np.errstate(under="ignore"):
        tail = scaled*scaled
    return _positive_result(tail, "marginal series tail")


def covariance_tail_bound(alpha, beta, cutoff):
    """Gate-uniform absolute omitted covariance bound sqrt(tau_a*tau_b).

    For equal orders the omitted covariance is nonnegative. For mixed orders
    this is an absolute bound, with no asserted sign. The float is a numerical
    evaluation of an analytical bound, not an outward-rounded certificate.
    """
    alpha, beta, cutoff = _order(alpha), _order(beta), _cutoff(cutoff)
    if any(a >= 2 and a.is_integer() and cutoff >= a for a in (alpha, beta)):
        return 0.0
    ta, tb = marginal_tail(alpha, cutoff), marginal_tail(beta, cutoff)
    return _positive_result(np.sqrt(ta)*np.sqrt(tb), "covariance tail bound")


def correlation_tail_bound(alpha, beta, cutoff):
    """Absolute omitted correlation bound with exact marginal normalization.

    Evaluate 4*sqrt(tau_a*tau_b)/sqrt(alpha*beta). The same-order error is
    one-sided and nonnegative. This bounds omitted mathematical series terms
    only; the returned binary64 value is not a numerical certificate.
    """
    alpha, beta, cutoff = _order(alpha), _order(beta), _cutoff(cutoff)
    if any(a >= 2 and a.is_integer() and cutoff >= a for a in (alpha, beta)):
        return 0.0
    ta, tb = marginal_tail(alpha, cutoff), marginal_tail(beta, cutoff)
    with np.errstate(under="ignore"):
        bound = 4*(np.sqrt(ta)/np.sqrt(alpha))*(np.sqrt(tb)/np.sqrt(beta))
    return _positive_result(bound, "correlation tail bound")


def covariance(alpha, beta, probabilities, *, cutoff):
    """Truncated coefficient lim d^2 Cov(S_alpha(U_l psi), S_beta(U_m psi)).

    Supply the operator Schmidt probabilities of U_l U_m^dagger. Passing
    a normalized vector alone does not assert that it is a physical gate
    spectrum. The partial sum includes mode cutoff and remains truncated
    unless an order terminates within it. covariance_tail_bound evaluates an
    analytical omitted-series bound; numerical errors and finite-d bias are
    separate and are not bounded by these calculations. Spectrum length times
    the number of evaluated modes may not exceed 50,000,000 operations.
    """
    eta = _probabilities(probabilities)
    alpha, beta, cutoff = _order(alpha), _order(beta), _cutoff(cutoff)
    # Terms above either exact termination order vanish even at larger cutoffs.
    final_mode = min([cutoff] + [int(a) for a in (alpha, beta)
                               if a >= 2 and a.is_integer()])
    modes, ca = _coefficient_sequence(alpha, final_mode)
    _, cb = _coefficient_sequence(beta, final_mode)
    if eta.size*modes.size > _MAX_KERNEL_WORK:
        raise FloatingPointError("Spectrum size times cutoff exceeds the supported work budget.")
    # Accumulate one channel at a time to keep memory linear in the cutoff.
    kernel = np.zeros_like(modes)
    with np.errstate(under="ignore"):
        for probability in eta:
            kernel += probability**modes
        terms = modes*ca*cb*kernel
        # Mode two has strictly positive weight for every valid order pair
        # and spectrum. Do not silently lose the entire covariance scale.
        if terms[0] == 0:
            raise FloatingPointError("The positive mode-two covariance term underflowed.")
        total = float(np.sum(terms))
        value = 0.25*total
        if total != 0 and value == 0:
            raise FloatingPointError("The nonzero covariance underflowed after its factor of one quarter.")
    if not np.isfinite(value):
        raise FloatingPointError("The covariance is unresolved in binary64 arithmetic.")
    if alpha == beta:
        return _positive_result(value, "same-order covariance")
    return value


def same_order_covariance(alpha, probabilities, *, cutoff):
    """Truncated same-order covariance coefficient, using natural logarithms."""
    return covariance(alpha, alpha, probabilities, cutoff=cutoff)


def correlation(alpha, beta, probabilities, *, cutoff):
    """Partial covariance divided by the EXACT limiting marginal variances.

    Return 4*K^(cutoff)/sqrt(alpha*beta), without clipping. In particular an
    identity gate and a nonterminating equal order have a series-tail defect
    below one, subject to floating-point error. correlation_tail_bound reports
    the analytical omitted-series bound. It does not enclose numerical errors,
    spectrum errors, finite-d bias or sampling uncertainty.
    """
    alpha, beta = _order(alpha), _order(beta)
    value = covariance(alpha, beta, probabilities, cutoff=cutoff)
    denominator = (marginal_variance(alpha) if alpha == beta else
                   np.sqrt(marginal_variance(alpha))*np.sqrt(marginal_variance(beta)))
    result = value/denominator
    if not np.isfinite(result) or (value != 0 and result == 0):
        raise FloatingPointError("The normalized covariance is unresolved in binary64 arithmetic.")
    return float(result)


def spatial_correlation_bound(alpha, r, s, *, cutoff):
    """Evaluate the fixed-access lower-bound series at rank min(r^2,s^2).

    The numerator is truncated and its marginal denominator is exact. The
    returned value underestimates the infinite-series lower bound by at most
    correlation_tail_bound(alpha,alpha,cutoff), apart from numerical error.
    Equal active dimensions admit exact saturation of the infinite-series
    bound by dual-unitary gates. Ranks above 1,000,000 are unsupported.
    """
    r = _positive_integer(r, "r")
    s = _positive_integer(s, "s")
    rank = min(r*r, s*s)
    if rank > _MAX_CUTOFF:
        raise FloatingPointError("The rank exceeds the supported array budget.")
    return correlation(alpha, alpha, np.full(rank, 1/rank), cutoff=cutoff)
