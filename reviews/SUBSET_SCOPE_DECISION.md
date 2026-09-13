# Subset-states and gate entanglement covariance: scope decision

## Recommendation

Reuse the historical **Entangling-successions** repository if its current state and history are preserved, but give the active work the identity of the **gate entanglement covariance paper**. Do not presently describe that paper as an upgraded version of the completed Subset-states manuscript.

This distinction concerns the scientific contribution, not the choice of GitHub container. The user explicitly permits reuse of Entangling-successions and is open to renaming it later. Reusing it can satisfy one active paper per repository without forcing unrelated results into one manuscript.

## Sources actually read

- `repository_review_17/quantum_information/sources/Subset-states/README.md`
- `repository_review_17/quantum_information/sources/Subset-states/PROVENANCE.md`
- `Entanglement-Temporal-Fluctuations-Quantum/theory/THEOREM.md`

This is a comparison of these current-source snapshots and the proposed theorem statement. It is not a new proof audit, literature campaign, or exhaustive assessment of unpublished subset-state results. No repository was modified and no new numerical calculation was run for this review.

## What has already been upgraded

The current Subset-states README explicitly identifies its manuscript as **“Support-size entanglement trajectories of random subset states”** and says that it updates the existing preprint record `arXiv:2501.06292`. Its completed results concern uniformly random supports of fixed cardinality with equal positive amplitudes: exact mean reduced states, exact average purity, a support-size scale hierarchy, entropy trajectories, and constrained arithmetic reference ensembles.

The user's clarification that Entangling-successions is a historical predecessor is consistent with this explicit update statement. Checking preservation of the predecessor's files and commits is a separate repository task.

## Why the current results constitute different papers

| Aspect | Subset-states | Gate entanglement covariance |
|---|---|---|
| Input ensemble | Fixed-cardinality subsets with equal positive amplitudes in a specified basis | Complex-Haar states on a balanced bipartition |
| Variable | Support cardinality and selected reference ensembles | Fixed gates acting on the same sampled input |
| Central object | Mean purity, mean entropy, and support-size trajectories | Joint centered entropy fluctuations and their covariance |
| Mechanism | Sparsity, coherent positive mean, and support correlations | Relative-gate operator Schmidt moments in the Gaussian fluctuation kernel |
| Main analytical conclusion | A near-maximal support window and exact purity scale hierarchy | Full positive-order entropy covariance and a sharp fixed-access correlation floor |

These differences are substantive. Subset-states already has a coherent manuscript and a preprint record. The covariance work supplies a different theorem and a different physical question. Neither project's completed central conclusion is presently a special case of the other's.

## The real mathematical connection

Both studies reshape a bipartite pure state into a coefficient matrix and obtain its reduced-state spectrum from a Gram matrix. This provides a useful shared framework, but it does not establish a common fluctuation law.

For a balanced cut, let `N=d²`, let `B` be the `d × d` zero-one incidence matrix of a uniformly random support of size `M`, and let `J` be the all-ones matrix. The normalized subset-state coefficient matrix obeys the exact decomposition

\[
C=\frac{B}{\sqrt M}
=\frac{\sqrt M}{N}J+
\frac{B-(M/N)J}{\sqrt M}.
\]

The first term is a rank-one coherent mean. Its squared Frobenius norm is `M/N`. The second term contains real entries whose sum is exactly zero and whose dependence is imposed by fixed cardinality. The nonzero eigenvalue of the Gram matrix of the mean term alone is `M/N`; this is not an assertion that the full random reduced state has an eigenvalue exactly equal to that number.

This decomposition gives a concrete route for relating subset-state spectral calculations to random-matrix methods. It also exposes why the complex-Haar theorem cannot simply be imported. Its Gaussian representation has zero mean, complex entries, unitary-invariant marginals, and a specific shared radial normalization. The subset ensemble has different features in each of those places.

Even in a regime with near-maximal average entropy or a similar leading spectral bulk, the covariance theorem concerns fluctuations of order `1/d`. Matching a leading mean or density does not establish those fluctuations, their scaling, or their gate dependence. The fixed computational basis also matters: subset inputs are not invariant under arbitrary local preprocessing, while an operator Schmidt spectrum is insensitive to local dressing of a gate. Extra gate-basis information could therefore survive in a subset-state covariance law.

## What a genuine unification would require

A natural new theorem would choose an explicit support regime `M(d)` and establish a joint fluctuation law for

\[
S_\alpha(U_\ell\psi_S),
\]

where `S` is a uniformly random fixed-cardinality support and the gates have fixed active dimensions. It would need to identify the correct centering and scaling, treat the coherent mean and cardinality constraint, and determine whether the covariance depends only on the relative gate's operator Schmidt probabilities or also on additional basis-dependent invariants. Extending it to noninteger entropies would require control of small singular values, not just polynomial moments.

One possible outcome would be a rigorously delimited Haar-like regime; another would be explicit non-Haar correction terms or a crossover. Either could create a substantive connection. None follows from the completed documents reviewed here, and pursuing it would be new research rather than packaging the existing Quantum candidate.

## Decision for the present handover

The covariance result remains a credible separate paper project under the preceding scientific assessment. The user's newly available historical repository removes a logistical need to create a fresh container. It does not change the assumptions or meaning of the theorem.

Preserve Subset-states as the home of its existing paper. Reuse Entangling-successions for the new active covariance paper with an explicit transition record, preserved history, and an eventual descriptive rename if desired. Retain the subset-ensemble fluctuation question as an optional future connection outside the current manuscript commitment.
