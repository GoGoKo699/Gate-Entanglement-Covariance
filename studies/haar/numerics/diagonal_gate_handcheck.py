"""Deterministic finite-matrix checks, no random-state survey or asymptotic fit."""
from pathlib import Path
import json
import numpy as np


def eta(h, t):
    return np.linalg.svd(np.exp(-1j * t * h) / np.sqrt(h.size), compute_uv=False) ** 2


def centered(h):
    return h - h.mean(axis=0, keepdims=True) - h.mean(axis=1, keepdims=True) + h.mean()


def main():
    h_a = np.outer([1, -1, 1, -1], [1, 1, -1, -1]).astype(float)
    h_b = np.array([[1, 1, -1, -1], [1, -1, -1, 1],
                    [-1, -1, 1, 1], [-1, 1, 1, -1]], dtype=float)
    result = {"kind": "deterministic algebra check", "controls": {}, "max_probability_error": 0.0}
    for name, h in [("A", h_a), ("B", h_b)]:
        assert np.array_equal(np.sort(h.ravel()), np.array([-1.] * 8 + [1.] * 8))
        assert np.array_equal(centered(h), h)
        rec = {"chi": float(np.mean(h * h)), "singular_values": np.linalg.svd(h, compute_uv=False).tolist(), "times": []}
        for t in [0., 0.173, np.pi / 4, np.pi / 2, np.pi]:
            expected = ([np.cos(t)**2, np.sin(t)**2, 0., 0.] if name == "A" else
                        [np.cos(t)**2, np.sin(t)**2 / 2, np.sin(t)**2 / 2, 0.])
            observed = eta(h, t)
            error = float(np.max(np.abs(np.sort(observed) - np.sort(expected))))
            result["max_probability_error"] = max(result["max_probability_error"], error)
            rec["times"].append({"time": float(t), "eta": observed.tolist(),
                                  "F2": float(np.sum(observed**2)),
                                  "V2_prediction": float(1 - np.sum(observed**2)), "max_eta_error": error})
        result["controls"][name] = rec
    h3 = np.outer(np.arange(3), np.arange(3)).astype(float)
    e3 = eta(h3, 2 * np.pi / 3)
    result["fourier_three_level"] = {"chi": float(np.mean(centered(h3)**2)), "eta": e3.tolist(),
                                      "F2": float(np.sum(e3**2))}
    result["max_probability_error"] = max(result["max_probability_error"], float(np.max(np.abs(e3 - 1/3))))
    # Additive local energies act only as left/right diagonal phases on Q.
    gauge_h = h_b + np.array([.17, -.41, 1.23, .09])[:, None] + np.array([-.31, .25, .72, -.64])[None, :]
    result["gauge_probability_error"] = float(np.max(np.abs(eta(h_b, .371) - eta(gauge_h, .371))))
    # Exact equal-purity gate construction, checked only as finite matrix algebra.
    p = (1 + np.sqrt(np.sqrt(2) - 1)) / 2
    q = 1 - p
    theta = np.arccos(np.sqrt(p))
    z1, z2 = np.array([1, 1, -1, -1]), np.array([1, -1, 1, -1])
    phase_a = (np.pi / 4) * np.outer(z1, z1)
    phase_c = theta * (np.outer(z1, z1) + np.outer(z2, z2))
    e_a, e_c = eta(phase_a, 1.), eta(phase_c, 1.)
    probability_error = max(float(np.max(np.abs(e_a - np.array([.5, .5, 0., 0.])))),
                            float(np.max(np.abs(e_c - np.array([p*p, p*q, p*q, q*q])))))
    result["equal_operator_purity"] = {
        "p": float(p), "theta": float(theta), "eta_A": e_a.tolist(), "eta_C": e_c.tolist(),
        "F2_A": float(np.sum(e_a**2)), "F2_C": float(np.sum(e_c**2)),
        "F3_A": float(np.sum(e_a**3)), "F3_C": float(np.sum(e_c**3)),
        "F3_C_exact": float((11 - 6*np.sqrt(2))/8),
        "renyi3_covariance_difference_exact": float(9*(3-2*np.sqrt(2))/800),
        "max_probability_error": probability_error,
        "proof_scope": "All integer k>2 follow from strict Jensen, not from sampled k checks."
    }
    result["max_probability_error"] = max(result["max_probability_error"], probability_error)
    assert result["max_probability_error"] < 2e-14
    assert result["gauge_probability_error"] < 2e-14
    target = Path(__file__).with_name("diagonal_gate_handcheck.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(target), "max_probability_error": result["max_probability_error"],
                      "gauge_probability_error": result["gauge_probability_error"]}))


if __name__ == "__main__":
    main()
