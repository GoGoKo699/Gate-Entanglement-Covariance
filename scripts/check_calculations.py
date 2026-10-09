#!/usr/bin/env python3
"""Check maintained calculations against independent analytical references.

No sampling and no changes to reference data. These checks exercise the
implementation; they do not replace the theorem's proof or its review.
"""
from fractions import Fraction
from copy import deepcopy
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
from gate_covariance import (coefficients, covariance, correlation, marginal_tail,
                             operator_schmidt_probabilities)
from gate_covariance.examples import active_swap, reader_examples, zz_gate, _summary
from check_series_bounds import run_checks as check_series_bounds
from verify_project import safe_output_directory


def _historical_summary(summary, orders, cutoff):
    """Schema-1 view: V_N=V-tau, rho_old=rho_new*sqrt(VaVb/Va_NVb_N).

    D_old=D_new-2*tau. Only this comparison adapter uses the old
    normalization; the kernel and all generated output use the current API.
    """
    result = deepcopy(summary)
    variances = np.asarray(summary["marginal_variance_coefficients"])
    tails = np.array([marginal_tail(alpha, cutoff) for alpha in orders])
    old_variances = variances-tails
    assert np.all(old_variances > 0)
    scale = np.sqrt(variances/old_variances)
    result["marginal_variance_coefficients"] = old_variances.tolist()
    result["same_order_correlations"] = (
        np.asarray(summary["same_order_correlations"])*scale**2).tolist()
    result["cross_order_correlations"] = (
        np.asarray(summary["cross_order_correlations"])*scale[:, None]*scale[None, :]).tolist()
    result["mean_square_increment_coefficients"] = (
        np.asarray(summary["mean_square_increment_coefficients"])-2*tails).tolist()
    return result


def _historical_reader_view(actual):
    """Explicit conversion to the protected schema-1 semantics and metadata.

    No reference bytes are modified. The unchanged recursive comparison
    below retains its original rtol=2e-12 and atol=2e-14 for every field.
    """
    old = deepcopy(actual)
    for key in ("normalization", "analytical_tail_bounds", "same_state_covariance_closed_form"):
        del old[key]
    old["schema_version"] = 1
    old["calculation"] = "Deterministic truncated evaluation of the fixed-support Haar limit; no random states."
    old["cutoff_diagnostic"] = "The absolute K-to-2K differences report series convergence only. They are not certified remainder bounds and do not estimate finite-d bias."
    # Literal schema-1 source labels are historical provenance, not links
    # for the current reading route.
    old["sources"] = ["theory/THEOREM.md", "evidence/checkpoint08/inverse/inverse_results.json",
                      "evidence/checkpoint07/checkpoints/07/numerics/entropy_pilot.py"]
    for name, summary in actual["examples"].items():
        converted = _historical_summary(summary, actual["orders"], actual["cutoff"])
        double = _historical_summary(
            _summary(summary["operator_schmidt_probabilities"], actual["comparison_cutoff"]),
            actual["orders"], actual["comparison_cutoff"])
        converted["cutoff_doubling_max_absolute_change"] = {
            key: float(np.max(np.abs(np.asarray(converted[key])-np.asarray(value))))
            for key, value in double.items()
        }
        old["examples"][name] = converted
    return old


def run_checks(reference=None):
    errors = {}
    # Frozen values were produced by exact binomial and Fraction arithmetic,
    # independent of the maintained floating-point recurrence.
    saved = json.loads((ROOT/"checks/inverse/inverse_results.json").read_text())
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
              "series_identity_and_tail_checks": check_series_bounds(),
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
        historical_view = _historical_reader_view(actual)
        compare(expected, historical_view)
        report["reader_reference_comparison"] = "Exact-normalized schema 2 converted analytically to preserved schema 1; original field tolerances unchanged."
        report["normalization_correlation_max_absolute_change"] = max(
            float(np.max(np.abs(np.asarray(actual["examples"][name]["cross_order_correlations"])-
                                np.asarray(old["cross_order_correlations"]))))
            for name, old in historical_view["examples"].items())
        report["reader_reference_max_absolute_change"] = max(differences)
        assert max(d["cutoff_doubling_max_absolute_change"]["same_order_correlations"]
                   for d in actual["examples"].values()) < 1e-9
        report["series_cutoff_doubling_correlation_change_below"] = 1e-9
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report path.")
    args = parser.parse_args()
    if args.output:
        args.output = args.output.resolve()
        safe_output_directory(args.output.parent)
    report = run_checks(ROOT/"results/reader_examples.json")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
