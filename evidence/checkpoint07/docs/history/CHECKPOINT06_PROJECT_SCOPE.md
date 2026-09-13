# Project scope and claim registry

Checkpoint 06, 12 September 2026.

## Independent identity

Working repository and GPT project name: **Entanglement Temporal Fluctuations**. Suggested repository slug: `Entanglement-Temporal-Fluctuations`.

The organizing object is the same-input, two-time covariance of equilibrium entanglement under a fixed boundary gate. This is a self-contained question with its own ensemble, theorem, data, and manuscript.

| Project | Central object | Boundary for this package |
|---|---|---|
| Entanglement-Trajectories | A frozen atlas of metric agreement, disagreement, majorization, and chronological controls | No source, data, release, tag, or scientific claims from the atlas are changed or required here. |
| Boundary-Entangling-Susceptibility | Average response to a fresh finite gate and dependence on neighboring-cut information | Central-spectrum insufficiency is not the contribution pursued here. |
| Entanglement Temporal Fluctuations | A prescribed gate's operator-Schmidt spectrum and equilibrium entropy covariance | Own derivation, small simulations, literature positioning, and unresolved significance question. |

The older weak-link disagreement and local response-angle pilots are historical motivation. They are not current hypotheses, required data, or promised work for this project. No chronology-enhancement, angle-law novelty, or broad metric-equivalence claim is inherited.

## Definitions and limits

The initial state is complex Haar on `C^d ⊗ C^d`. The gate is `exp(-itH)` with a real diagonal energy array on fixed `r × s` boundary factors and identities on spectators. The dimension `d` grows through multiples of `r` and `s`. All entropies use natural logarithms; the Rényi order is fixed and strictly positive. Means are stationary because the full state remains Haar in distribution. Actual entropy fluctuations have size `1/d`.

The statements concern covariance limits and joint Gaussian convergence at a fixed finite collection of times. For short-time asymptotics, first take `d → ∞`, then the time lag to zero.

## Claim registry

| ID | Claim | Current status and evidence |
|---|---|---|
| C01 | For fixed diagonal boundary gates, spectral Chebyshev mode `k` has normalized memory `Σηℓ^k`. | Derived by the phase-weighted annular Wick argument. Internal review and finite-degree independent checks accompany the proof. |
| C02 | The resulting series gives all fixed positive-order entropy covariances and their finite-dimensional Gaussian limit. | Derived using C01, established square-LUE regularity results, marginal L2 approximation, and entropy normalization. |
| C03 | Gate operator-spectrum majorization orders every same-order entropy covariance in this class. | Direct corollary of positive same-order coefficients and convex power sums. It does not order cross-order covariances. |
| C04 | Two explicit gates with equal operator purity have different entropy covariance at every positive order except two. | Analytical construction and strict inequality from Jensen's inequality. No separate physical Monte Carlo claim is made for this example. |
| C05 | The dimension-first increment has powers `8α`, a quadratic logarithm, or a quadratic law across `α=1/4`. | Derived consequence. The same leading law occurs in standard smooth Gaussian interpolation, so it is not presented as unique to local unitary physics. |
| C06 | Matched energy spectra and initial interaction strength need not fix finite-time memory. | Exact four-level boundary construction. The new finite-size pilot supports its exact recurrence contrast; some other estimates differ considerably from the large-d prediction. |
| C07 | The same law applies to every fixed non-diagonal local gate. | Open; not claimed. |
| C08 | The same law describes physically prepared chaotic equilibrium states or autonomous many-body evolution. | Open; not claimed. Haar stationarity is not a thermalization theorem. |
| C09 | The result meets the novelty and significance standard of PRL. | Unresolved. No direct match was located in the focused review; broad significance is not established by that search. |

Other exclusions: no path-space convergence, almost-sure roughness, fractional Brownian motion, uniform shrinking-time bound, finite-size error rate, or finite-dimensional singularity is established. Whole-half SWAP is outside the fixed-support diagonal theorem and forbids unrestricted gate wording.

## Research preferences

Favor one explanatory physical relation with a short derivation and bounded simulations. Add computation only to answer a concrete scientific question. Do not enlarge an ensemble merely to obtain a favorable comparison. Keep adverse results and distinguish exploratory choices from frozen predictions. PRL is an ambition to assess candidly, not an assumed destination.

The next decision is whether the full entropy-memory relation has sufficient physical reach beyond the established operator-purity/OTOC identity. A bounded analytical test of a non-diagonal gate, with an explicit counterexample search before a universal claim, would answer more than another Haar-size survey. Its result should determine further scope.
