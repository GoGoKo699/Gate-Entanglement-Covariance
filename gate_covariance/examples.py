"""Fixed gate examples and data for the repository's explanatory figure."""
import numpy as np

from .core import (coefficients, covariance, correlation, marginal_variance,
                   marginal_tail, covariance_tail_bound, correlation_tail_bound,
                   same_state_covariance, operator_schmidt_probabilities)

ORDERS = (0.5, 1.0, 2.0, 3.0, 4.0)
DEFAULT_CUTOFF = 65536


def zz_gate(angle):
    """exp(-i angle Z tensor Z), in |00>,|01>,|10>,|11> order."""
    if not np.isscalar(angle) or np.iscomplexobj(angle) or not np.isfinite(angle):
        raise ValueError("angle must be finite and real.")
    return np.diag(np.exp(-1j*float(angle)*np.array([1, -1, -1, 1])))


def active_swap():
    """SWAP of the two active qubits, with identity on all spectators."""
    return np.eye(4)[[0, 2, 1, 3]]


def _summary(probabilities, cutoff):
    variances = np.array([marginal_variance(alpha) for alpha in ORDERS])
    cov = np.array([[covariance(alpha, beta, probabilities, cutoff=cutoff)
                     for beta in ORDERS] for alpha in ORDERS])
    rho = cov / (np.sqrt(variances[:, None])*np.sqrt(variances[None, :]))
    return {
        "marginal_variance_coefficients": variances.tolist(),
        "same_order_covariance_coefficients": np.diag(cov).tolist(),
        "same_order_correlations": np.diag(rho).tolist(),
        "cross_order_covariance_coefficients": cov.tolist(),
        "cross_order_correlations": rho.tolist(),
        "mean_square_increment_coefficients": (2*(variances-np.diag(cov))).tolist(),
    }


def _tail_report(cutoff):
    tau = np.array([marginal_tail(alpha, cutoff) for alpha in ORDERS])
    return {
        "marginal_variance_omitted_terms": tau.tolist(),
        "covariance_absolute_error_bounds": [
            [covariance_tail_bound(alpha, beta, cutoff) for beta in ORDERS]
            for alpha in ORDERS],
        "correlation_absolute_error_bounds": [
            [correlation_tail_bound(alpha, beta, cutoff) for beta in ORDERS]
            for alpha in ORDERS],
        "mean_square_increment_absolute_error_bounds": (2*tau).tolist(),
        "interpretation": "Floating-point evaluations of analytical omitted-series bounds for exact spectra and coefficients; not outward-rounded numerical certificates. Same-order covariance/correlation sums underestimate the limiting series; increments computed as 2(V_alpha-K_N) overestimate it. Mixed-order bounds are two-sided. Roundoff, spectrum errors, finite-d bias, sampling and ensemble mismatch are excluded.",
    }


def reader_examples(cutoff=DEFAULT_CUTOFF):
    """Generate finite sums, exact marginal normalization and tail reporting."""
    coefficients(1, cutoff)
    if cutoff < 4:
        raise ValueError("The reader examples need cutoff >= 4 to include their integer orders.")
    gates = {"identity": np.eye(4), "ZZ_pi_over_4": zz_gate(np.pi/4),
             "active_SWAP": active_swap()}
    examples = {}
    for name, gate in gates.items():
        probabilities = operator_schmidt_probabilities(gate, 2, 2)
        result = _summary(probabilities, cutoff)
        doubled = _summary(probabilities, 2*cutoff)
        result["operator_schmidt_probabilities"] = probabilities.tolist()
        result["operator_purity"] = float(np.sum(probabilities**2))
        result["cutoff_doubling_max_absolute_change"] = {
            key: float(np.max(np.abs(np.asarray(result[key])-np.asarray(value))))
            for key, value in doubled.items()
        }
        examples[name] = result
    return {
        "schema_version": 2,
        "calculation": "Deterministic mode-2-through-N covariance sums with exact marginal normalization; no random states.",
        "units": "Natural logarithms; covariance and mean-square increment coefficients are multiplied by d^2 in the limit.",
        "setting": "Balanced complex-Haar d by d state; fixed active factors r=s=2; d tends to infinity before any further limit.",
        "orders": list(ORDERS), "cutoff": cutoff, "comparison_cutoff": 2*cutoff,
        "normalization": "V_alpha=alpha/4 exactly for the limiting coefficient. Covariance numerators remain partial sums, including for identity. Increment approximation is 2(V_alpha-K_N); no clipping or forced identity value.",
        "cutoff_diagnostic": "The absolute N-to-2N differences are supplemental convergence diagnostics. The analytical tail bounds below control omitted series terms only.",
        "analytical_tail_bounds": _tail_report(cutoff),
        "same_state_covariance_closed_form": [
            [same_state_covariance(alpha, beta) for beta in ORDERS] for alpha in ORDERS],
        "integer_orders": "Orders 2, 3, and 4 terminate exactly at modes 2, 3, and 4; their series have no omitted terms at this cutoff.",
        "active_SWAP_interpretation": "Only the fixed active qubits are exchanged. This is not SWAP of the entire growing halves.",
        "sources": ["theory/THEOREM.md", "theory/PROOF.md",
                    "checks/inverse/inverse_results.json",
                    "studies/non_diagonal/numerics/entropy_pilot.py"],
        "examples": examples,
    }


def zz_correlation_curve(angles, alpha, cutoff=DEFAULT_CUTOFF):
    """Partial correlation with exact variance for the rank-two ZZ spectra.

    The analytical error bound correlation_tail_bound(alpha,alpha,cutoff)
    holds uniformly over angles for exact spectra and coefficients.
    """
    return np.array([correlation(alpha, alpha,
                                [np.cos(angle)**2, np.sin(angle)**2], cutoff=cutoff)
                     for angle in angles])
