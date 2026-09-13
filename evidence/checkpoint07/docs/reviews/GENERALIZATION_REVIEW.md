# Independent review of the diagonal-gate extension

2026-09-12. This is a bounded internal review of `theory/DIAGONAL_GATE_THEORY.md`, including its added full-spectrum comparisons, the standalone project's `numerics/operator_memory.py`, and the saved operator-memory outputs. No new random-state simulation was run. I performed a small exact Gaussian-contraction check and recalculated statistics from the already saved arrays.

## Finding

I found no material mathematical defect in the generalized fixed-time diagonal-gate covariance, the gauge normalization, the short-lag interaction coefficient, or the matched controls. The result remains restricted to a fixed diagonal interaction on fixed active boundary dimensions, with balanced Haar spectator dimensions tending to infinity. The document states those restrictions accurately.

The new equal-operator-purity comparison gives a compact analytical reason to retain the complete mode kernel: equal purity fixes the Rényi-2 memory but can leave every other positive-order Rényi memory different. This is useful content beyond merely evaluating another purity correlation. It does not, by itself, establish originality or PRL significance.

## Theory checks

1. **Operator-Schmidt normalization.** With equal label-sector multiplicities, compressing the phase matrix divided by d gives P/sqrt(rs). The operator U/d has Hilbert-Schmidt norm one and the same coefficient matrix in normalized projector bases. Thus the eta values sum to one and are the claimed normalized operator-Schmidt probabilities. No spectator-dimension factor is missing.

2. **Generalized covariance.** The same bridge cancellation and unicyclic leading Wick graph argument applies to arbitrary real fixed h_ab. Only the cycle retains phase weights, which sum to Tr[(Q Q†)^k]. The tree counts, trace-mode removal, and marginal L2 extension therefore carry over. The result for two times uses the operator spectrum of the relative gate U(t−s), not an independent spectrum assignment at each time.

3. **Gauge and interaction strength.** Additive row and column functions are commuting local terms and multiply Q by diagonal unitaries. In the centered gauge K=h^c/sqrt(rs) annihilates the uniform row and column vectors. The first perturbation of QQ† vanishes, and the largest eigenvalue's second-order coefficient is −chi. Its evenness gives eta_1=1−chi t²+O(t⁴). The remaining eigenvalues are O(t²). The stated asymptotic coefficients and powers then follow from the dominant eigenvalue and convergent coefficient bounds. The infinite series is treated before differentiation where required.

4. **Matched 4 by 4 Hamiltonians.** Both arrays have eight +1 and eight −1 energies, zero row/column means, norm one, and chi=1. Their nonzero singular values are respectively 4 and (sqrt(8),sqrt(8)). Their gate spectra, product-gate recurrence for A, and stated Rényi-2 increments follow exactly. The larger boundary support of B is correctly declared.

5. **Full-spectrum comparisons.** Majorization gives the stated ordering of every same-order entropy autocovariance, with strictness supplied by c_(alpha,2)≠0. The separate rank-two versus product-Bernoulli construction matches F_2 exactly. Its strict Jensen argument correctly gives F_k(C)>F_k(A) for every integer k>2. The formulas c_(alpha,2)=−2alpha/(alpha+2), c_(alpha,3)=−2alpha(alpha−2)/[(alpha+2)(alpha+3)], and the Rényi-3 covariance difference 9(3−2sqrt(2))/800 are correct. This comparison matches gate operator purity only; the text appropriately does not claim equal Hamiltonian strength, spectrum, or duration.

6. **Scope control.** The whole-half SWAP example correctly excludes an unrestricted all-gates interpretation but does not disprove a possible theorem for fixed active non-diagonal dimensions. That distinction is retained. No new sample-path or finite-size/time-scale theorem is supplied or needed for the current covariance claim.

## Independent algebra and saved-output checks

`generalized_wick_check.py` enumerates all leading connected complex-Gaussian pairings through trace degree three, sums every four-valued boundary-label assignment directly, and compares the complete Chebyshev covariance Fourier polynomials for both A and B. All mixed degrees agree exactly, with maximum integer discrepancy zero at common denominator 4096. The full record is `generalized_wick_check.json`. This resolves a concrete low-degree phase-label or normalization risk; it is not a substitute for the all-degree argument or the nonsmooth theorem.

The numerical implementation applies the correct diagonal phases to the same Haar matrix for both interactions. Its chosen row and column label maps each have four equally sized sectors and correspond to fixed boundary factors. Each saved result has 64 states, two interactions, two pulse times, and five orders. Source and plan hashes match the frozen records. Means and sample standard errors recomputed from the saved arrays match the summary exactly. The largest spectrum-normalization residual is 2.67e−15; no numerical tail exclusion is present.

Doubling the covariance-series cutoff from 32768 to 65536 changes the selected predictions by at most 3.84e−15. This is a numerical stability check of the existing asymptotic-tail evaluation, not a certified truncation bound. It rules out a relevant coefficient-truncation explanation for the much larger Monte Carlo deviations.

## Numerical interpretation that must remain visible

The data do not uniformly follow the limiting curves. The sharpest downward cohort occurs for B at d=128 and t=pi/4:

| Order | Saved estimate | Sample standard error | Limiting prediction |
|---|---:|---:|---:|
| 1/2 | 0.107929 | 0.016960 | 0.181407 |
| 1 | 0.188963 | 0.027740 | 0.326083 |

Those residuals are respectively 4.33 and 4.94 times the estimated sample standard error. They are **not calibrated Gaussian z-scores or p-values**: the statistic is a squared increment, the standard error is estimated from only 64 states, and these comparisons are strongly correlated. A downward cohort can also underestimate its squared-increment variance. The d=64 B cohort at the same time lies above both predictions. No implementation error identified in this review explains the difference, but that does not justify assigning it solely to sampling or solely to finite size.

At d=128 and t=pi/4 several paired B-minus-A estimates are negative even though the limiting comparison is positive. They should remain in the report. The cohort supports the exact A recurrence and the finite B response much more clearly than it establishes quantitative convergence of the full covariance. The maximum observed A recurrence entropy error is 1.78e−15.

No additional physical simulation is required merely to make this bounded check look cleaner. The theorem can lead the presentation, with this finite-sample limitation stated explicitly.

## Project and significance decision

The extension strengthens the project's independent scientific identity: equilibrium entanglement memory resolves a gate's full operator-Schmidt power sums within the proved diagonal family. The equal-purity example explains why the complete relation is more informative than its familiar order-two consequence. The short-lag anomalous exponent remains a generic smooth hard-edge effect, as shown by the earlier scalar-correlated comparison.

A separate research repository is appropriate now. Its claims should center on the fixed-time diagonal-gate relation and distinguish established foundations, proved consequences, numerical diagnostics, and unresolved originality. PRL significance remains an open judgment. The next argument to settle is whether this full-spectrum relation supplies a sufficiently new physical use or interpretation beyond established operator-entanglement and random-matrix fluctuation results, not whether a larger simulation campaign can produce tighter error bars.
