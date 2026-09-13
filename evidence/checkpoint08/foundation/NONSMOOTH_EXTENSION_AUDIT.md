# Independent review of the nonsmooth extension

Completed 2026-09-12 as a post-protocol analytical followup. I independently read Henry Hu's primary manuscript, *On the regularity conditions in the CLT for the LUE*, arXiv:2310.08509v1, including Theorem 1.1, Lemma 1.2, Corollary 1.3, and its notation convention, and checked their use in `NONSMOOTH_EXTENSION.md`.

Primary source: https://arxiv.org/html/2310.08509v1

## Finding

The proposed extension is sound, conditional on the all-degree polynomial covariance and joint Gaussian limit. Hu's results supply the needed marginal variance approximation. The positive-order nonsmooth endpoint is therefore not an additional unresolved obstruction once the polynomial result is established. The exact low-degree enumeration alone remains insufficient to establish that all-degree result.

## Specific checks

**The square ensemble is included.** Hu's fixed parameter is the nonnegative integer difference between the two matrix dimensions. The manuscript explicitly defines it as nonnegative, so the square case is covered. This parameter is unrelated to Rényi order.

**The regularity requirement is met.** A bounded smooth upper cutoff of `x^alpha`, equal to the power on a neighborhood of [0,4], satisfies Hu's stronger weighted integral for every fixed alpha>0. In the corner `0<y<x<delta`, substitution `y=ux` separates an integrable factor `integral x^(2alpha-1) dx` from an integrable u factor. The test function is smooth near the soft edge at 4. The `x log x` function has the required regularity as well. The upper cutoff can be removed in L2 using the exponentially small largest-eigenvalue tail and fixed polynomial moments of the Gaussian matrix norm.

**A marginal theorem suffices for the finite-time vector.** Every fixed-time marginal of the phase-block process is precisely the same LUE. Polynomial approximation of a centered statistic in the limiting variance seminorm, followed by Hu's variance convergence, gives a marginal L2 remainder tending to zero in the successive limits. Cut off each approximating polynomial outside a fixed interval when applying the bounded-function theorem, and remove that cutoff using the same Gaussian tail argument. Any finite linear combination over times is bounded in L2 by the sum of the marginal errors. Cauchy–Schwarz transfers the covariance, while the fixed-polynomial joint CLT and approximation transfer the finite-dimensional Gaussian limit. No independence between the time marginals is needed.

**Uniform integrability is available.** Convergence in distribution of a centered LSS to its Gaussian limit, together with convergence of its second moment to the Gaussian second moment, implies uniform integrability of its square. Thus the argument does not require a fourth-moment bound for the LSS or for an entropy derivative.

**The entropy delta method works in L2.** Let `mu_d=E Tr W^alpha`, `X=Tr W^alpha-mu_d`, and `Z=Tr W-d`. On the stated good event, both `Tr W^alpha` and `mu_d` are bounded above and below by positive constants times d. The scaled logarithmic Taylor remainder is bounded by `C|X|` and divided by `|X|` tends to zero in probability. Uniform integrability of `X^2` makes its L2 norm vanish. The trace term works in the same way.

For clarity, the bad-event estimate must be applied to the *combined normalized entropy*, not separately to `log Tr W^alpha` and `log Tr W`. Put

    s_0,d = [log mu_d-alpha log d]/(1-alpha).

Then `s_0,d=log d+O(1)`, and on the exceptional event the bound `0<=S_alpha<=log d` gives a deterministic `O(d log d)` bound for `d(S_alpha-s_0,d)`. Squaring it and multiplying by the exponentially small exceptional probability tends to zero. The linear centered statistics on that event are controlled by their uniform integrability. This proves the centered expansion first relative to `s_0,d`; its vanishing L2 remainder then allows replacement by the exact entropy mean. The existing extension note uses this combined-entropy argument, so no change in its conclusion is needed.

For increments at two times, trace normalization is even simpler: `log Tr W` cancels exactly because the Frobenius norm is conserved. This simplification is optional; the stronger full centered-entropy argument above is valid.

## Remaining qualification

These steps close the nonsmooth-observable and normalization gaps for finite sets of fixed times, provided the stated all-degree phase-weighted polynomial kernel is correct. They do not prove a functional process limit, tightness, almost-sure path regularity, or a uniform finite-size/time-step approximation. The small-time mean-square laws are consequences of the resulting limiting covariance series with dimension taken to infinity first.
