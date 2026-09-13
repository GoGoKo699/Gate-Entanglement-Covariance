"""Fixed gate examples and data for the repository's explanatory figure."""
import numpy as np

from .core import coefficients, operator_schmidt_probabilities

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
    modes = np.arange(2, cutoff+1, dtype=float)
    kernel = np.sum(np.asarray(probabilities)[:, None]**modes[None, :], axis=0)
    co = np.array([coefficients(alpha, cutoff)[1] for alpha in ORDERS])
    variances = 0.25*np.sum(modes*co*co, axis=1)
    cov = np.array([[0.25*np.sum(modes*ca*cb*kernel) for cb in co] for ca in co])
    rho = cov / np.sqrt(variances[:, None]*variances[None, :])
    return {
        "marginal_variance_coefficients": variances.tolist(),
        "same_order_covariance_coefficients": np.diag(cov).tolist(),
        "same_order_correlations": np.diag(rho).tolist(),
        "cross_order_covariance_coefficients": cov.tolist(),
        "cross_order_correlations": rho.tolist(),
        "mean_square_increment_coefficients": (0.5*np.sum(modes*co*co*(1-kernel), axis=1)).tolist(),
    }


def reader_examples(cutoff=DEFAULT_CUTOFF):
    """Generate deterministic asymptotic examples and a cutoff comparison."""
    # Validate the cutoff through the public entry point before allocating.
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
        "schema_version": 1,
        "calculation": "Deterministic truncated evaluation of the fixed-support Haar limit; no random states.",
        "units": "Natural logarithms; covariance and mean-square increment coefficients are multiplied by d^2 in the limit.",
        "setting": "Balanced complex-Haar d by d state; fixed active factors r=s=2; d tends to infinity before any further limit.",
        "orders": list(ORDERS), "cutoff": cutoff, "comparison_cutoff": 2*cutoff,
        "cutoff_diagnostic": "The absolute K-to-2K differences report series convergence only. They are not certified remainder bounds and do not estimate finite-d bias.",
        "integer_orders": "Orders 2, 3, and 4 terminate exactly at modes 2, 3, and 4; their series have no omitted terms at this cutoff.",
        "active_SWAP_interpretation": "Only the fixed active qubits are exchanged. This is not SWAP of the entire growing halves.",
        "sources": ["theory/THEOREM.md", "evidence/checkpoint08/inverse/inverse_results.json",
                    "evidence/checkpoint07/checkpoints/07/numerics/entropy_pilot.py"],
        "examples": examples,
    }


def zz_correlation_curve(angles, alpha, cutoff=DEFAULT_CUTOFF):
    """Evaluate the exact rank-two ZZ gate spectrum at the requested angles."""
    modes, coeff = coefficients(alpha, cutoff)
    weights = modes*coeff**2
    denominator = weights.sum()
    values = []
    for angle in angles:
        probabilities = np.array([np.cos(angle)**2, np.sin(angle)**2])
        kernel = np.sum(probabilities[:, None]**modes[None, :], axis=0)
        values.append(float(np.dot(weights, kernel)/denominator))
    return np.array(values)
