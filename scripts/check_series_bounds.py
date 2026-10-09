#!/usr/bin/env python3
"""Deterministic checks of the closed normalization and omitted-series bounds.

Fraction arithmetic independently checks the mathematical identities. Checks
of floating-point helpers use ordinary numerical tolerances, not certified
intervals. No random-state generation or reference-data writes are involved.
"""
from fractions import Fraction
from math import isfinite, sqrt
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np

from gate_covariance import (
    coefficients, correlation, correlation_tail_bound, covariance,
    covariance_tail_bound, marginal_tail, marginal_variance,
    same_state_covariance, spatial_correlation_bound,
)
from verify_project import safe_output_directory


def _fraction_coefficients(alpha, cutoff):
    """Exact recurrence, used only for these independent rational controls."""
    alpha = Fraction(alpha)
    values = {2: -2*alpha/(alpha+2)}
    for k in range(2, cutoff):
        values[k+1] = values[k]*(alpha-k)/(alpha+k+1)
    return values


def _fraction_covariance(alpha, beta, spectrum, cutoff):
    ca = _fraction_coefficients(alpha, cutoff)
    cb = _fraction_coefficients(beta, cutoff)
    return sum((Fraction(k, 4)*ca[k]*cb[k]*sum(p**k for p in spectrum)
                for k in range(2, cutoff+1)), Fraction(0))


def _fraction_tail(alpha, cutoff):
    alpha = Fraction(alpha)
    c = _fraction_coefficients(alpha, cutoff+1)[cutoff+1]
    return (cutoff+1+alpha)**2*c*c/(16*alpha)


def _close(actual, expected, *, rtol=2e-12, atol=0):
    assert isfinite(actual), actual
    assert abs(actual-float(expected)) <= atol+rtol*abs(float(expected)), (actual, expected)


def _raises(call, exception):
    try:
        call()
    except exception:
        return
    raise AssertionError(f"Expected {exception.__name__}")


def run_checks():
    # The finite identity is exact before any limiting argument. This grid
    # includes nonterminating orders below one, order one, and integers.
    orders = tuple(map(Fraction, ["1/5", "1/2", "2/3", "1", "3/2",
                                  "2", "5/2", "3", "4", "7"]))
    cutoffs = (2, 3, 4, 7, 17, 31)
    exact_identities = 0
    for alpha in orders:
        for beta in orders:
            for cutoff in cutoffs:
                ca = _fraction_coefficients(alpha, cutoff+1)
                cb = _fraction_coefficients(beta, cutoff+1)
                total = sum(k*ca[k]*cb[k] for k in range(2, cutoff+1))
                boundary = ((cutoff+1+alpha)*(cutoff+1+beta)
                            *ca[cutoff+1]*cb[cutoff+1]/(2*(alpha+beta)))
                assert total == 2*alpha*beta/(alpha+beta)-boundary
                for k in range(2, cutoff+1):
                    qk = (k+alpha)*(k+beta)*ca[k]*cb[k]/(2*(alpha+beta))
                    qnext = ((k+1+alpha)*(k+1+beta)*ca[k+1]*cb[k+1]
                             /(2*(alpha+beta)))
                    assert qk-qnext == k*ca[k]*cb[k]
                exact_identities += 1

    # Public floating-point coefficients are checked against rational values,
    # not against another helper in the maintained implementation.
    coefficient_error = 0.
    for alpha in orders:
        k, actual = coefficients(float(alpha), 31)
        expected = _fraction_coefficients(alpha, 31)
        assert np.array_equal(k, np.arange(2, 32))
        for mode, value in zip(range(2, 32), actual):
            _close(value, expected[mode])
            coefficient_error = max(coefficient_error, abs(value-float(expected[mode])))

    # Order one is controlled without evaluating a singular Gamma formula.
    k, actual = coefficients(1, 4096)
    closed = 4*(-1.)**(k-1)/(k*(k*k-1))
    assert np.allclose(actual, closed, rtol=2e-13, atol=0)
    for cutoff in (2, 3, 19, 257, 4096):
        _close(marginal_tail(1, cutoff), Fraction(1, cutoff**2*(cutoff+1)**2))

    # The half-order formula also checks the N versus N+1 indexing directly.
    for cutoff in (2, 3, 7, 16, 64):
        exact = Fraction(9, 8*(2*cutoff+1)**2)
        assert _fraction_tail(Fraction(1, 2), cutoff) == exact
        _close(marginal_tail(.5, cutoff), exact)
        _close(correlation_tail_bound(.5, .5, cutoff), 8*exact)
        # Exact marginal normalization leaves the known positive defect for
        # an identity gate. A truncated-denominator ratio would give one.
        expected_rho = 1-Fraction(9, (2*cutoff+1)**2)
        actual_rho = correlation(.5, .5, [1.], cutoff=cutoff)
        assert actual_rho < 1
        _close(actual_rho, expected_rho)
        _close(1-actual_rho, 1-expected_rho, rtol=2e-11)
    half_default_bound = Fraction(9, (2*65536+1)**2)
    assert half_default_bound < Fraction(524, 10**12)
    _close(correlation_tail_bound(.5, .5, 65536), half_default_bound)

    # Integer termination must be tested on both sides of its exact index.
    integer_controls = 0
    for alpha in (2, 3, 4, 7):
        for cutoff in sorted({2, max(2, alpha-1), alpha, alpha+1, alpha+5}):
            exact_tail = _fraction_tail(alpha, cutoff)
            actual_tail = marginal_tail(alpha, cutoff)
            _close(actual_tail, exact_tail)
            assert (actual_tail == 0) == (cutoff >= alpha)
            c = coefficients(alpha, cutoff+1)[1]
            if cutoff >= alpha:
                assert np.all(c[alpha-1:] == 0)
            else:
                assert c[-1] != 0
            exact_partial = _fraction_covariance(Fraction(alpha), Fraction(alpha),
                                                 (Fraction(1),), cutoff)
            assert exact_partial+exact_tail == Fraction(alpha, 4)
            integer_controls += 1

    # Closed same-state benchmarks are checked independently as rationals.
    benchmark_error = 0.
    for alpha in orders:
        _close(marginal_variance(float(alpha)), alpha/4)
        _close(same_state_covariance(float(alpha), float(alpha)), alpha/4)
        for beta in orders:
            expected = alpha*beta/(2*(alpha+beta))
            actual = same_state_covariance(float(alpha), float(beta))
            _close(actual, expected)
            assert actual == same_state_covariance(float(beta), float(alpha))
            benchmark_error = max(benchmark_error, abs(actual-float(expected)))

    # These exact spectra belong respectively to product gates, ZZ(pi/4),
    # ZZ(pi/6), and active two-qubit SWAP. Bounds are tested on omitted
    # finite blocks using Fraction arithmetic; positivity of each same-order
    # term makes every such block part of the full nonnegative tail.
    spectra = {
        "product": (Fraction(1),),
        "ZZ_pi_over_4": (Fraction(1, 2),)*2,
        "ZZ_pi_over_6": (Fraction(3, 4), Fraction(1, 4)),
        "active_SWAP": (Fraction(1, 4),)*4,
    }
    order_pairs = ((Fraction(1, 5), Fraction(2, 3)),
                   (Fraction(1, 2), Fraction(1, 2)),
                   (Fraction(1), Fraction(1)),
                   (Fraction(1, 2), Fraction(5, 2)),
                   (Fraction(3, 2), Fraction(7)),
                   (Fraction(2), Fraction(3)))
    finite_tail_checks = 0
    for spectrum in spectra.values():
        probabilities = list(map(float, spectrum))
        for alpha, beta in order_pairs:
            for cutoff in (2, 5, 11):
                partial = _fraction_covariance(alpha, beta, spectrum, cutoff)
                omitted_block = _fraction_covariance(alpha, beta, spectrum, 32)-partial
                ta = _fraction_tail(alpha, cutoff)
                tb = _fraction_tail(beta, cutoff)
                assert omitted_block**2 <= ta*tb
                if alpha == beta:
                    assert 0 <= omitted_block <= ta
                numerical = covariance(float(alpha), float(beta), probabilities, cutoff=cutoff)
                _close(numerical, partial, atol=1e-17)
                _close(covariance_tail_bound(float(alpha), float(beta), cutoff),
                       sqrt(float(ta*tb)))
                _close(correlation_tail_bound(float(alpha), float(beta), cutoff),
                       4*sqrt(float(ta*tb/(alpha*beta))))
                _close(correlation(float(alpha), float(beta), probabilities, cutoff=cutoff),
                       4*float(partial)/sqrt(float(alpha*beta)))
                finite_tail_checks += 1

    # A mixed-order remainder can be negative. Here every omitted product
    # past mode two has negative sign, so a one-sided positive bound fails.
    negative_ca = _fraction_coefficients(Fraction(1, 2), 32)
    negative_cb = _fraction_coefficients(Fraction(5, 2), 32)
    assert all(negative_ca[k]*negative_cb[k] < 0 for k in range(3, 33))
    mixed_exact = Fraction(5, 24)
    mixed_partial = _fraction_covariance(Fraction(1, 2), Fraction(5, 2),
                                        (Fraction(1),), 2)
    assert mixed_exact-mixed_partial < 0
    assert (mixed_exact-mixed_partial)**2 <= _fraction_tail(Fraction(1, 2), 2)*_fraction_tail(Fraction(5, 2), 2)

    # Integer controls and the spatial helper must retain their known values.
    for spectrum in spectra.values():
        f2 = sum(p*p for p in spectrum)
        f3 = sum(p**3 for p in spectrum)
        probabilities = list(map(float, spectrum))
        _close(correlation(2, 2, probabilities, cutoff=9), f2)
        _close(covariance(2, 3, probabilities, cutoff=9), Fraction(3, 5)*f2)
        _close(correlation(3, 3, probabilities, cutoff=9), (24*f2+f3)/25)
    # An exactly terminating factor removes all higher mixed terms. The
    # implementation must not evaluate an irrelevant long recurrence for
    # the other order, which would underflow in this example.
    _close(covariance(2, 100.5, [1.], cutoff=65536), Fraction(201, 205))
    assert covariance_tail_bound(2, 100.5, 65536) == 0
    assert correlation_tail_bound(100.5, 2, 65536) == 0
    _close(spatial_correlation_bound(2, 2, 2, cutoff=8), Fraction(1, 4))
    swap_partial = _fraction_covariance(Fraction(1, 2), Fraction(1, 2), spectra["active_SWAP"], 5)
    _close(spatial_correlation_bound(.5, 2, 2, cutoff=5), 8*swap_partial)

    # Historical truncated-marginal normalization is compared analytically
    # with the new exact-marginal normalization. No tolerance is relaxed and
    # no historical record is rewritten by this check.
    normalization_checks = 0
    for alpha, beta in order_pairs:
        cutoff = 5
        numerator = _fraction_covariance(alpha, beta, spectra["active_SWAP"], cutoff)
        va_partial = _fraction_covariance(alpha, alpha, (Fraction(1),), cutoff)
        vb_partial = _fraction_covariance(beta, beta, (Fraction(1),), cutoff)
        ta, tb = _fraction_tail(alpha, cutoff), _fraction_tail(beta, cutoff)
        assert va_partial+ta == alpha/4
        assert vb_partial+tb == beta/4
        old_squared = numerator**2/(va_partial*vb_partial)
        new_squared = 16*numerator**2/(alpha*beta)
        correction_squared = (1-4*ta/alpha)*(1-4*tb/beta)
        assert new_squared == old_squared*correction_squared
        legacy = float(numerator)/sqrt(float(va_partial*vb_partial))
        converted = legacy*sqrt(float(correction_squared))
        _close(correlation(float(alpha), float(beta), list(map(float, spectra["active_SWAP"])),
                           cutoff=cutoff), converted)
        normalization_checks += 1

    # A nearby float is not an exactly terminating integer entropy order.
    for alpha in (np.nextafter(2., 0.), np.nextafter(2., np.inf),
                  np.nextafter(3., 0.), np.nextafter(3., np.inf)):
        _, actual = coefficients(alpha, 9)
        exact = _fraction_coefficients(Fraction.from_float(float(alpha)), 9)
        assert np.all(actual != 0)
        for mode, value in zip(range(2, 10), actual):
            _close(value, exact[mode], rtol=5e-12)
        tail = marginal_tail(alpha, 8)
        assert tail > 0
        _close(tail, _fraction_tail(Fraction.from_float(float(alpha)), 8), rtol=5e-12)

    invalid_count = 0
    for bad in (0, -1, np.nan, np.inf, -np.inf, True, 1+1j, [1], {}, "1", b"1"):
        calls = (lambda bad=bad: coefficients(bad, 4),
                 lambda bad=bad: marginal_variance(bad),
                 lambda bad=bad: same_state_covariance(bad, 1),
                 lambda bad=bad: same_state_covariance(1, bad),
                 lambda bad=bad: marginal_tail(bad, 4),
                 lambda bad=bad: covariance_tail_bound(1, bad, 4),
                 lambda bad=bad: correlation_tail_bound(bad, 1, 4))
        for call in calls:
            _raises(call, ValueError)
            invalid_count += 1
    for bad in (0, 1, -2, 2.5, True, np.inf):
        for call in (lambda bad=bad: coefficients(1, bad),
                     lambda bad=bad: marginal_tail(1, bad),
                     lambda bad=bad: covariance_tail_bound(1, 2, bad),
                     lambda bad=bad: correlation_tail_bound(1, 2, bad)):
            _raises(call, ValueError)
            invalid_count += 1

    # Positive mathematical tails must never become reported exact zeros
    # merely because a recurrence or its squared coefficient underflows.
    unsupported_calls = (
        lambda: coefficients(2.**50, 2),
        lambda: coefficients(1, 1_000_001),
        lambda: coefficients(Fraction(2)+Fraction(1, 10**30), 4),
        lambda: marginal_tail(Fraction(3)-Fraction(1, 10**30), 4),
        lambda: coefficients(100.5, 65536),
        lambda: marginal_tail(100.5, 65536),
        lambda: covariance(1e-200, 1e-200, [1.], cutoff=2),
        lambda: covariance(1e-200, 2e-200, [1.], cutoff=2),
        lambda: marginal_variance(np.nextafter(0., 1.)),
    )
    for call in unsupported_calls:
        _raises(call, FloatingPointError)
    # A stable implementation may resolve this tail; an explicit rejection
    # is also appropriate. Silently returning a numerical zero is not.
    try:
        tiny_tail = marginal_tail(1e-200, 2)
    except FloatingPointError:
        pass
    else:
        assert isfinite(tiny_tail) and tiny_tail > 0

    return {
        "status": "passed",
        "new_random_states": 0,
        "exact_fraction_telescoping_identities": exact_identities,
        "integer_cutoff_controls": integer_controls,
        "exact_fraction_physical_spectrum_tail_checks": finite_tail_checks,
        "historical_normalization_conversion_controls": normalization_checks,
        "floating_coefficient_max_absolute_error": coefficient_error,
        "closed_same_state_max_absolute_error": benchmark_error,
        "half_order_correlation_tail_bound_at_65536": float(half_default_bound),
        "invalid_inputs_rejected": invalid_count,
        "unsupported_numerical_regimes_rejected": len(unsupported_calls),
        "scope": "Exact rational identity controls and ordinary floating-point implementation checks; omitted-series bounds do not enclose numerical, finite-d, or sampling errors.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON report under an allowed output directory.")
    args = parser.parse_args()
    if args.output:
        args.output = args.output.resolve()
        safe_output_directory(args.output.parent)
    report = run_checks()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
