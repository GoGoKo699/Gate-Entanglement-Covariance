# Independent numerical and formula audit

Completed 2026-09-12. The audit implementation does not import `run_experiment.py` and does not modify production files. Reproduce with `python audit05.py` after generating the production results. Detailed records are in `audit05.json`.

## Finding

No material implementation or normalization defect was found in the checked calculation. These checks establish numerical consistency of this finite experiment, not an asymptotic scaling theorem or a novelty claim.

| Independent check | Scope | Result |
|---|---:|---:|
| Unordered-pair covariance in long-double arithmetic | All 2,560 cut observations, all 25 matrix entries | Maximum discrepancy 2.09e-15 in covariance RMS-product units |
| Reduced-density commutator rates, with a different SVD driver | 20 states/cuts: saved anchors and each output file's smallest-tail sample | Maximum absolute rate discrepancy 6.66e-14; maximum discrepancy divided by conditional RMS 4.86e-13 |
| Direct 64 by 64 matrix exponentials, reduced-density eigenvalues, and entropy changes | 16 finite pulses at both cuts of a six-qubit state | Maximum entropy-change discrepancy 2.45e-15 |
| Exact spherical two-design for the two-qubit Pauli orientation covariance | 36 deterministic orientation pairs, all five orders | Agreement to numerical roundoff |
| Independent recomputation of saved random-orientation second moments | Two positive fixed spectra, 4,000 orientations each | Maximum discrepancy 1.74 conditional Monte Carlo standard errors |

Every saved spectrum is positive. Across all observations, the smallest singular value is at least 1.11e12 times machine epsilon times the largest singular value. Thus the sampled low-order behavior is comfortably separated from a numerically unresolved Schmidt tail. No cutoff, clipping, or negative-eigenvalue repair is involved.

## Formula checks

For a physical product interaction with traceless Hermitian factors, the response has an unordered-pair expansion with coefficient `2 sqrt(lambda_i lambda_j) (h_i-h_j)`. An off-diagonal product of two independently Haar-rotated operators has imaginary-part variance `v_A v_B/2`. Consequently the exact covariance prefactor is `2 v_A v_B`; for the stated Pauli probe this is `2ab/[(a^2-1)(b^2-1)]`. The unordered-pair formula reproduces the weighted covariance used by production.

The production singular-value derivative contracts `U† dot(M) V`. Its real part multiplied by twice the singular value gives the correct eigenvalue derivative. The independently computed reduced-density derivative is `-i[(H psi) M† - M (H psi)†]`, and agrees in sign and magnitude. Subtracting a constant from each entropy gradient is valid because the spectrum derivative has zero trace.

For a rectangular coefficient matrix, generating `M=U diag(s) V[:, :a]^T` with independent square Haar unitary matrices gives independent Schmidt bases in the two spaces. The production use of ordinary transpose in that state construction and the matching operator matrix elements is consistent; no missing complex conjugation was found.

The physical pulse is exactly `exp(-it ZZ)=cos(t) I - i sin(t) ZZ`, with generator norm one. Shifting the cut changes both the bipartition and the boundary bond on which this probe acts. The comparison therefore tests the declared aspect ratios at equal total dimension. It does not isolate a statewise protection effect caused by moving a fixed physical operation relative to a cut.

## Statistical and physical interpretation

The conditional mean derivative is exactly zero. Empirical second moments, without subtracting an estimated mean, are the appropriate estimators for the orientation validation. At each fixed positive spectrum the derivative is bounded over Schmidt bases, so standard errors of those conditional Monte Carlo products are legitimate.

This does not license the same error bars after randomizing balanced spectra. At low Rényi orders, rare extremely small Schmidt weights can make the fourth derivative moment infinite even while its second moment remains finite. The protocol's use of medians and interquartile ranges of the conditional variance is appropriate. These robust summaries describe a typical conditional scale, and should not be relabeled as estimates of an unconditional mean or deterministic coefficient below order one quarter.

Exact finite pulses verify the stated finite-duration response. Agreement between `Delta S/t` and the initial derivative on tested samples does not give a bound uniform over the Haar ensemble, nor does it prove a proposed shrinking time scale. In particular, entropy differences can remain well behaved where instantaneous derivatives are dominated by rare small Schmidt channels. Any asymptotic or physical interpretation of the finite-pulse results must be stated separately from the numerical implementation checks.

The balanced-cut quarter-order threshold follows from the integrability of the relevant small-eigenvalue moment. The finite-size experiment can check that prediction, but cannot independently establish its limiting exponent or make it a new physical mechanism. It also does not establish spatial dynamics, a Gaussian rate law, or PRL-level originality.
