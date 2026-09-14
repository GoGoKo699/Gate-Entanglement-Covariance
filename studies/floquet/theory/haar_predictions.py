"""Independent deterministic Haar benchmarks for the checkpoint-09 protocol.

No eigenstates are generated or loaded. Population moments use no Bessel
correction. Exact purity identities are evaluated as rational numbers.
"""
from fractions import Fraction
import json
from pathlib import Path

import numpy as np
from scipy.special import polygamma


def entropy_coefficients(alpha, cutoff=131072):
    k = np.arange(2, cutoff + 1, dtype=float)
    c = np.empty_like(k)
    if alpha == 1:
        c = 4 * (-1.0) ** (k - 1) / (k * (k * k - 1))
    else:
        c[0] = -2 * alpha / (alpha + 2)
        c[1:] = c[0] * np.cumprod((alpha - k[:-1]) / (alpha + k[:-1] + 1))
    return k, c


def entropy_benchmark(alpha):
    k, c = entropy_coefficients(alpha)
    kernel = 4.0 ** (1 - k)
    variance = np.sum(k * c * c) / 4
    covariance = np.sum(k * c * c * kernel) / 4
    return dict(
        alpha=alpha,
        scaled_static_variance=float(variance),
        scaled_swap_covariance=float(covariance),
        swap_correlation=float(covariance / variance),
        scaled_swap_mean_square_increment=float(2 * (variance - covariance)),
        scope="asymptotic complex Haar, fixed boundary, natural logarithms",
        series_cutoff=131072,
    )


def purity_benchmarks(d):
    D = d * d
    mean = Fraction(2 * d, D + 1)
    variance = Fraction(2 * (D - 1) ** 2, (D + 1) ** 2 * (D + 2) * (D + 3))
    correlations = dict(
        identity=Fraction(1),
        swap=Fraction(D * D + D + 16, 4 * (D - 1) ** 2),
        phase_swap=Fraction(D * D - 7 * D + 8, 4 * (D - 1) ** 2),
    )
    rows = {}
    for name, correlation in correlations.items():
        increment = 2 * variance * (1 - correlation)
        rows[name] = dict(
            correlation=float(correlation),
            correlation_rational=str(correlation),
            covariance=float(variance * correlation),
            scaled_covariance=float(d**4 * variance * correlation),
            mean_square_increment=float(increment),
            scaled_mean_square_increment=float(d**4 * increment),
        )
    # Wei, PRE 96, 022106 (2017), with subsystem dimensions m=n=d.
    vn_variance = (
        -polygamma(1, D + 1)
        + Fraction(2 * d, D + 1) * polygamma(1, d)
        - Fraction((d + 1) * (3 * d + 1), 4 * D * (D + 1))
    )
    vn_mean = sum(Fraction(1, j) for j in range(d + 1, D + 1)) - Fraction(d - 1, 2 * d)
    return dict(
        d=d,
        N=2 * int(np.log2(d)),
        mean=float(mean),
        variance=float(variance),
        variance_rational=str(variance),
        scaled_variance=float(d**4 * variance),
        gate_rows=rows,
        exact_Haar_von_Neumann_variance=float(vn_variance),
        exact_Haar_von_Neumann_scaled_variance=float(D * vn_variance),
        exact_Haar_von_Neumann_mean=float(vn_mean),
    )


def main():
    result = dict(
        orders=[entropy_benchmark(a) for a in [.5, 1, 2]],
        sizes=[purity_benchmarks(d) for d in [16, 32]],
        notes=[
            "SWAP and SWAP exp(-i pi ZZ/4) share all limiting entropy benchmarks.",
            "They have different exact finite-d purity correlations.",
            "Identity has correlation one and zero increment for every input ensemble.",
            "Floquet complete-basis statistics are dependent population summaries, not iid estimates.",
            "The entropy series truncation is numerical; purity fractions are exact.",
        ],
    )
    assert abs(result['orders'][2]['scaled_static_variance'] - .5) < 1e-15
    assert abs(result['orders'][2]['swap_correlation'] - .25) < 1e-15
    path = Path(__file__).with_name('haar_predictions.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
