"""Independent exact four-copy SWAP/phaseSWAP Haar audit.

Standard-library only. No Gaussian contractions, state samples, dense K,
or import of exact_purity.py. The active permutation action is counted
with integer signs; all scalar moments and correlations use Fraction.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def cycles(p):
    seen = set()
    count = 0
    for start in range(len(p)):
        if start not in seen:
            count += 1
            i = start
            while i not in seen:
                seen.add(i)
                i = p[i]
    return count


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def monomial_action(x, phase):
    """Apply A-swap on copies 1,2 and conjugated A-swap on 3,4.

    U=SWAP for phase=False; U=SWAP diag(1,i,i,1) for phase=True.
    The second gate differs from SWAP exp(-i*pi*ZZ/4) by a global phase.
    Its four-copy conjugation phases reduce to integer signs.
    """
    (a, b), (c, e), (f, g), (h, j) = [divmod(t, 2) for t in x]
    exponent = (f ^ g) + (h ^ j) - (f ^ j) - (h ^ g)
    assert exponent in (-2, 0, 2)
    sign = -1 if phase and abs(exponent) == 2 else 1
    return (2*c+b, 2*a+e, 2*f+j, 2*h+g), sign


def integer_terms(phase):
    tau = (1, 0, 3, 2)
    terms = []
    counts = Counter()
    for p in permutations(range(4)):
        inv = tuple(p.index(i) for i in range(4))
        active = 0
        for x in product(range(4), repeat=4):
            output, sign = monomial_action(tuple(x[i] for i in inv), phase)
            if output == x:
                active += sign
        nr = cycles(compose(tau, p))
        nc = cycles(p)
        counts[nr + nc] += active
        terms.append({"permutation": list(p), "nr": nr, "nc": nc,
                      "active_integer": active})
    return terms, counts


def independent_swap_factor_counts():
    """For plain SWAP, also count four physical factors directly."""
    a = (1, 0, 2, 3)
    b = (0, 1, 3, 2)
    tau = compose(a, b)
    counts = Counter()
    for p in permutations(range(4)):
        coefficient = 2 ** (cycles(compose(a, p)) + cycles(compose(b, p)))
        degree = cycles(compose(tau, p)) + cycles(p)
        counts[degree] += coefficient
    return counts


def exact_row(counts, d, phase):
    assert d >= 2 and d % 2 == 0
    D = d*d
    numerator = sum(Fraction(value) * Fraction(d, 2)**degree
                    for degree, value in counts.items())
    moment = numerator / (D*(D+1)*(D+2)*(D+3))
    mean_squared = Fraction(4*D, (D+1)**2)
    variance = Fraction(2*(D-1)**2, (D+1)**2*(D+2)*(D+3))
    covariance = moment - mean_squared
    correlation = covariance / variance
    expected = (Fraction(D*D-7*D+8, 4*(D-1)**2) if phase else
                Fraction(D*D+D+16, 4*(D-1)**2))
    assert correlation == expected
    return {"d": d, "D": D, "numerator_exact": str(numerator),
            "product_moment_exact": str(moment),
            "purity_covariance_exact": str(covariance),
            "purity_correlation_exact": str(correlation),
            "purity_correlation_float": float(correlation)}


def main():
    saved_path = ROOT / "results" / "exact_purity.json"
    saved = json.loads(saved_path.read_text())["results"] if saved_path.exists() else None
    results = {}
    for name, phase in (("SWAP", False), ("phaseSWAP", True)):
        terms, counts = integer_terms(phase)
        expected_counts = {6: 256, 4: 264, 2: 16 if phase else 32}
        assert dict(counts) == expected_counts
        if not phase:
            assert counts == independent_swap_factor_counts()
        rows = [exact_row(counts, d, phase)
                for d in (2, 4, 8, 16, 32, 64, 128, 256, 1024)]
        verification = {"available": bool(saved is not None and name in saved)}
        if verification["available"]:
            errors = []
            moment_errors = []
            covariance_errors = []
            for stored in saved[name]["rows"]:
                audit = exact_row(counts, stored["d"], phase)
                errors.append(abs(audit["purity_correlation_float"] - stored["purity_correlation"]))
                moment_errors.append(abs(float(Fraction(audit["product_moment_exact"])) - stored["purity_product_moment"]))
                covariance_errors.append(abs(float(Fraction(audit["purity_covariance_exact"])) - stored["purity_covariance"]))
            verification.update({"rows_checked": len(errors),
                "max_correlation_error": max(errors),
                "max_product_moment_error": max(moment_errors),
                "max_covariance_error": max(covariance_errors)})
            assert max(errors + moment_errors + covariance_errors) < 1e-12
        results[name] = {
            "active_permutation_terms": terms,
            "numerator_coefficients_in_n_d_over_2": {str(k): v for k, v in sorted(counts.items())},
            "numerator_coefficients_in_d": {str(k): str(Fraction(v, 2**k)) for k, v in sorted(counts.items())},
            "rows": rows, "saved_results_verification": verification}
    for a, b in zip(results["SWAP"]["rows"], results["phaseSWAP"]["rows"]):
        D = a["D"]
        assert Fraction(a["purity_correlation_exact"]) - Fraction(b["purity_correlation_exact"]) == Fraction(2*(D+1), (D-1)**2)
    out = {"method": "Integer monomial four-copy Haar traces and exact rational scalar arithmetic; independent physical-factor count for plain SWAP.",
           "scope": "Finite-d balanced complex-Haar purity moments. No exact finite-d logarithmic-entropy covariance is asserted.",
           "formulas_D_equals_d_squared": {
               "SWAP_correlation": "(D^2+D+16)/(4*(D-1)^2)",
               "phaseSWAP_correlation": "(D^2-7*D+8)/(4*(D-1)^2)",
               "difference": "2*(D+1)/(D-1)^2"},
           "results": results}
    target = ROOT / "results" / "exact_swap_audit.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"status": "passed", "output": str(target),
                      "saved_results_verification": {k: v["saved_results_verification"] for k, v in results.items()}}, indent=2))


if __name__ == "__main__":
    main()
