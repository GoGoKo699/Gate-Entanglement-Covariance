#!/usr/bin/env python3
"""Check maintained calculations against independent analytical references.

No sampling and no changes to imported evidence. These checks exercise the
implementation; they do not replace the theorem's proof or its review.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
from gate_covariance import coefficients, covariance, correlation, operator_schmidt_probabilities
from gate_covariance.examples import active_swap, reader_examples, zz_gate


def run_checks(reference=None):
    errors = {}
    # Frozen values were produced by exact binomial and Fraction arithmetic,
    # independent of the maintained floating-point recurrence.
    saved = json.loads((ROOT/"evidence/checkpoint08/inverse/inverse_results.json").read_text())
    rational_errors = []
    for witness in saved["exact_witnesses"].values():
        eta = [float(Fraction(x)) for x in witness["spectrum"]]
        for alpha, exact in zip([2, 3, 4], witness["covariances_2_3_4"]):
            rational_errors.append(abs(covariance(alpha, alpha, eta, cutoff=12)-float(Fraction(exact))))
        # The overlap of order-two and order-three Fourier polynomials has
        # only mode two: C_23=3 F_2/5, an independent mixed-order anchor.
        f2 = float(Fraction(witness["moments_through_4"][1]))
        rational_errors.append(abs(covariance(2, 3, eta, cutoff=12)-3*f2/5))
    errors["saved_rational_covariance_max_error"] = max(rational_errors)
    assert max(rational_errors) < 5e-14

    # Independently known spectra, including unequal active dimensions.
    gate_cases = [(np.eye(4), 2, 2, [1, 0, 0, 0]),
                  (zz_gate(np.pi/4), 2, 2, [.5, .5, 0, 0]),
                  (active_swap(), 2, 2, [.25]*4)]
    f3 = np.exp(2j*np.pi*np.outer(np.arange(3), np.arange(3))/3)/np.sqrt(3)
    gate_cases.append((np.kron(np.array([[0, 1], [1, 0]]), f3), 2, 3, [1, 0, 0, 0]))
    controlled_qutrit_phase = np.diag(np.r_[np.ones(3), np.exp(2j*np.pi*np.arange(3)/3)])
    gate_cases.append((controlled_qutrit_phase, 2, 3, [.5, .5, 0, 0]))
    gate_errors = [float(np.max(abs(operator_schmidt_probabilities(u, r, s)-eta)))
                   for u, r, s, eta in gate_cases]
    errors["analytical_gate_spectrum_max_error"] = max(gate_errors)
    assert max(gate_errors) < 2e-14

    # A closed expression independently anchors the continuous alpha=1 case.
    k, c = coefficients(1, 4096)
    explicit = 4*(-1.)**(k-1)/(k*(k*k-1))
    errors["order_one_closed_coefficient_max_error"] = float(np.max(abs(c-explicit)))
    assert np.allclose(c, explicit, rtol=2e-13, atol=1e-16)
    assert all(np.all(coefficients(a, 12)[1][a-1:] == 0) for a in [2, 3, 4])

    # Gate spectrum moments are recovered through the published rational
    # inverse, testing the normalization of all three integer correlations.
    eta = [float(Fraction(x)) for x in saved["exact_witnesses"]["interior_cartan"]["spectrum"]]
    rho2, rho3, rho4 = [correlation(a, a, eta, cutoff=12) for a in [2, 3, 4]]
    recovered = [rho2, 25*rho3-24*rho2, 441*rho4-1200*rho3+760*rho2]
    expected = [sum(x**m for x in eta) for m in [2, 3, 4]]
    errors["integer_hierarchy_moment_max_error"] = float(np.max(abs(np.array(recovered)-expected)))
    assert errors["integer_hierarchy_moment_max_error"] < 2e-12

    rejected = 0
    bad_calls = [lambda: coefficients(0, 12), lambda: coefficients(np.inf, 12),
                 lambda: coefficients(np.complex128(1+1j), 12),
                 lambda: coefficients(1, 1), lambda: coefficients(1, 2.5),
                 lambda: covariance(1, 1, [.4, .4], cutoff=12),
                 lambda: covariance(1, 1, [-.2, 1.2], cutoff=12),
                 lambda: covariance(1, 1, [np.nan], cutoff=12),
                 lambda: operator_schmidt_probabilities(2*np.eye(4), 2, 2),
                 lambda: operator_schmidt_probabilities(np.eye(4), 2, 3)]
    for call in bad_calls:
        try:
            call()
        except ValueError:
            rejected += 1
    assert rejected == len(bad_calls)

    report = {"status": "passed", "new_random_states": 0,
              "independent_anchors": errors, "invalid_inputs_rejected": rejected,
              "scope": "Maintained code checks against saved rational witnesses and analytical gates; no proof audit or finite-size simulation."}
    if reference is not None:
        expected = json.loads(Path(reference).read_text())
        actual = reader_examples(expected["cutoff"])
        differences = []
        def compare(x, y):
            if isinstance(x, dict):
                assert x.keys() == y.keys()
                for key in x:
                    compare(x[key], y[key])
            elif isinstance(x, list):
                assert len(x) == len(y)
                for u, v in zip(x, y):
                    compare(u, v)
            elif isinstance(x, float):
                differences.append(abs(x-y))
                assert np.isclose(x, y, rtol=2e-12, atol=2e-14)
            else:
                assert x == y
        compare(expected, actual)
        report["reader_reference_max_absolute_change"] = max(differences)
        assert max(d["cutoff_doubling_max_absolute_change"]["same_order_correlations"]
                   for d in actual["examples"].values()) < 1e-9
        report["series_cutoff_doubling_correlation_change_below"] = 1e-9
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path.")
    args = parser.parse_args()
    report = run_checks(ROOT/"results/reader_examples.json")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
