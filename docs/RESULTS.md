# Results and evidence

The central result is a derived asymptotic theorem: for a balanced complex-Haar state, a deterministic gate on fixed boundary factors determines the limiting entropy covariance through its operator Schmidt probabilities. The numerical work checks finite algebraic consequences and illustrates the entropy prediction at modest sizes. It does not replace the all-degree proof or supply a finite-size error theorem.

Throughout this page, $d$ is the dimension of each half, entropies use natural logarithms, and order $1/2$ is pure-state logarithmic negativity. Absolute entropy covariances vanish as $d^{-2}$. See the [precise theorem](../theory/THEOREM.md) for the fixed-support, fixed-order, and finite-family assumptions, and the [claim ledger](../CLAIM_LEDGER.md) for current exclusions.

On **LEARN**, this page follows the [tutorial bridge](TUTORIAL_BRIDGE.md) and
[worked calculation](WORKED_EXAMPLE.md): they explain what the kernel predicts;
the sections below separate its derivation from deterministic evaluations,
finite-size observations and the failed extension. On **CHECK**, start from the
[maintained proof](../theory/PROOF.md), then use the linked records to inspect a
specific dependency or comparison. No checkpoint chronology is needed to read
the current result. The [sole tutorial and primary citations](REFERENCES.md)
have separate educational and attribution roles.

## What has been derived

| Result | Proof and evidence | What the result permits |
|---|---|---|
| The relative gate's operator Schmidt probabilities determine every fixed positive-order entropy cross-covariance and the fixed finite-family Gaussian limit | [Maintained derivation](../theory/PROOF.md), with inherited [general-gate argument](../evidence/checkpoint08/foundation/GENERAL_GATE_REVIEW.md), [low-regularity entropy transfer](../evidence/checkpoint08/foundation/NONSMOOTH_EXTENSION.md), [transfer audit](../evidence/checkpoint08/foundation/NONSMOOTH_EXTENSION_AUDIT.md), and [current proof assessment](../reviews/PROOF_ASSESSMENT.md) | The theorem includes non-diagonal gates. It gives no growing-support, shrinking-time, or sample-path convergence statement. |
| Fixed spatial access leaves positive limiting same-order entropy correlation; dual-unitary gates attain the bound for equal active dimensions | [Theorem and convexity argument](../theory/THEOREM.md), [general-gate report](../evidence/checkpoint07/checkpoints/07/REPORT.md), and [algebraic review](../evidence/checkpoint07/checkpoints/07/reviews/ADDITIONAL_COROLLARY_AUDIT.md) | The minimum correlations for one active qubit on each side are approximately `0.17232220`, `0.22773244`, and `0.25` at orders $1/2$, $1$, and $2$. These are limiting correlations, not bounds at every finite dimension. |
| Equal operator purity can coexist with different entropy covariance at other orders | [Explicit diagonal-gate pair and proof](../evidence/checkpoint08/foundation/DIAGONAL_GATE_THEORY.md), [saved series evaluations](../evidence/checkpoint07/numerics/operator_results/equal_purity_analytic.json); a stronger second-moment comparison is given by the [exact gate-design audit](../evidence/checkpoint08/reviews/DESIGN_PAIR_INDEPENDENT_AUDIT.md) and [design-pair results](../evidence/checkpoint08/results/design_pair.json) | The distinction is analytical. The design example concerns gate 2-designs on the active qubits; it does not replace the initial Haar ensemble by a state 2-design. |
| Ideal integer-order covariances identify a finite-rank operator Schmidt spectrum | [Moment-inversion proof](../evidence/checkpoint08/inverse/INVERSE_MEMORY_NOTE.md), [code](../evidence/checkpoint08/inverse/inverse_moments.py), and [exact results](../evidence/checkpoint08/inverse/inverse_results.json) | Known finite rank gives triangular moment inversion and Newton reconstruction. The qubit correlation-to-moment error amplification factors are $1$, `49`, and `2401` before root recovery. There is no efficient tomography claim or recovery of Schmidt bases. |
| Finite-dimensional Haar purity correlation is exactly related to whole-half product-input entangling power | [Exact identity](../evidence/checkpoint08/finite_purity/EXACT_GLOBAL_PURITY.md), [independent contraction code](../evidence/checkpoint08/finite_purity/check_exact_global_purity.py), and [saved results](../evidence/checkpoint08/finite_purity/exact_global_purity_results.json) | Purity is not Rényi-2 entropy at finite dimension. Whole-half product inputs can contain active-spectator entanglement within each half, so they differ from product inputs on the active factors alone. |

The independent reviews are internal checks, not external peer review. Annular Wishart fluctuations, LUE regularity, operator entanglement, entangling power, and moment inversion have established antecedents. The [literature assessment](../reviews/PUBLICATION_POSITIONING.md) identifies the closest comparisons and limits of the novelty review.

## Direct entropy illustration

The non-diagonal pilot used **192 independent Haar inputs**: 96 at $d=32$ and 96 at $d=64$. Each input was reused for boundary SWAP and the Cartan gate $\exp[-i(0.37\,XX+0.23\,YY+0.11\,ZZ)]$, with orders $1/2$, $1$, and $2$ evaluated from the same spectra. Thus there were 384 gate applications, not 384 independent inputs. The protocol and predictions were fixed before sampling.

The observable below is the rescaled mean-square entropy increment, $d^2\mathbb E[(S_\alpha(U\psi)-S_\alpha(\psi))^2]$. Haar stationarity relates it to the covariance theorem. Each $\pm$ gives one sample standard error over the 96 independent inputs at that size.

| Gate | Order | Limiting prediction | Measured, $d=32$ | Measured, $d=64$ |
|---|---:|---:|---:|---:|
| SWAP | 1/2 | 0.206919 | 0.223061 ± 0.029482 | 0.202017 ± 0.025830 |
| SWAP | 1 | 0.386134 | 0.368730 ± 0.044852 | 0.374868 ± 0.051766 |
| SWAP | 2 | 0.750000 | 0.648855 ± 0.072884 | 0.713391 ± 0.100258 |
| Cartan | 1/2 | 0.102588 | 0.095598 ± 0.011438 | 0.114490 ± 0.014935 |
| Cartan | 1 | 0.169565 | 0.164616 ± 0.021260 | 0.173503 ± 0.024518 |
| Cartan | 2 | 0.319527 | 0.300049 ± 0.042827 | 0.305910 ± 0.048248 |

The pilot is broadly compatible with the predictions at this resolution. It does not establish convergence with dimension, cover every entropy order, or isolate finite-size bias. Gate and order comparisons sharing an input are correlated; the displayed errors include sampling variation only. Standardized discrepancies are not calibrated significance tests.

Sources: [protocol](../evidence/checkpoint07/checkpoints/07/PROTOCOL.md), [frozen predictions](../evidence/checkpoint07/checkpoints/07/results/pilot_frozen.json), [implementation](../evidence/checkpoint07/checkpoints/07/numerics/entropy_pilot.py), [complete summary](../evidence/checkpoint07/checkpoints/07/results/pilot_summary.json), and saved arrays at [32-dimensional halves](../evidence/checkpoint07/checkpoints/07/results/pilot_d32.npz) and [64-dimensional halves](../evidence/checkpoint07/checkpoints/07/results/pilot_d64.npz). The displayed means and standard errors agree with direct recomputation from these arrays. The [original validation record](../evidence/checkpoint07/VALIDATION.json) documents the historical fresh-directory reproduction.

Earlier ZZ and diagonal-gate cohorts remain separate inherited evidence. They are not pooled into the 192-state pilot. The earlier 128-state diagonal comparison contains substantial adverse deviations: at $d=128$, gate B and time $\pi/4$, the measured increment statistics were `0.107929 ± 0.016960` against `0.181407` at order $1/2$, and `0.188963 ± 0.027740` against `0.326083` at order $1$. Some paired gate differences also had the opposite sign to their limiting prediction. Sampling and finite-size contributions to these discrepancies remain unresolved. See the [saved diagonal summary](../evidence/checkpoint07/numerics/operator_results/summary.json) and [interpretation](../evidence/checkpoint07/docs/history/CHECKPOINT06_PROJECT_STATUS.md). The exact recurrence control in that cohort worked to about $1.78\times10^{-15}$ in entropy.

## Algebraic and deterministic checks

The leading Gaussian contraction calculation checked 68,786 networks across ten gates, including unequal $2\times3$ active factors. Mixed Chebyshev degrees through three agreed within about $4.57\times10^{-13}$; degree four for eight gates agreed within about $3.79\times10^{-10}$, after cancellation of larger monomial terms. This tests low-degree contraction identities in floating-point arithmetic. The all-degree result rests on the proof above. See [code](../evidence/checkpoint07/checkpoints/07/numerics/general_gate_wick.py), [saved contractions](../evidence/checkpoint07/checkpoints/07/numerics/general_gate_wick.json), and the [bounded-validation report](../evidence/checkpoint07/checkpoints/07/REPORT.md).

The focused reproduction reruns the following six existing deterministic programs. The result links contain the reference outputs; no global Haar-state sampling is involved.

| Calculation | Scope and recorded result | Code and saved output |
|---|---|---|
| Moment inversion | Exact matrix and Newton checks through rank 12, including error amplification and deterministic spectra; passed | [Code](../evidence/checkpoint08/inverse/inverse_moments.py), [results](../evidence/checkpoint08/inverse/inverse_results.json) |
| Whole-system purity identity | 14 gates, 336 fourth-Haar-moment permutation traces; largest unnormalized trace difference about $1.14\times10^{-13}$ | [Code](../evidence/checkpoint08/finite_purity/check_exact_global_purity.py), [results](../evidence/checkpoint08/finite_purity/exact_global_purity_results.json) |
| Two subsystem assignments, full-system contraction | 14 active-gate/spectator cases; largest mode-correlation difference about $1.66\times10^{-14}$ | [Code](../evidence/checkpoint08/finite_purity/check_two_cut_modes.py), [results](../evidence/checkpoint08/finite_purity/two_cut_modes_results.json) |
| Two-assignment symbolic identities | Eight exact sparse-polynomial identities for centering, variance, and modes; all passed | [Code](../evidence/checkpoint08/reviews/two_cut_symbolic_audit.py), [results](../evidence/checkpoint08/reviews/two_cut_symbolic_audit.json) |
| Separate purity-sum and product-input contractions | 15 active gates at dimensions 2, 3, 4 and five spectator sizes; 75 correlations agree within $1.29\times10^{-12}$; entangling-power formulas within $1.11\times10^{-16}$ | [Code](../evidence/checkpoint08/numerics/two_cut_check.py), [results](../evidence/checkpoint08/results/two_cut_check.json) |
| Exact gate-design pair | Two full two-copy twirling superoperators agree with Haar within $3.25\times10^{-16}$ in Frobenius norm; limiting order-three correlation difference is exactly $3\sqrt5/20000$ | [Code](../evidence/checkpoint08/numerics/design_pair.py), [results](../evidence/checkpoint08/results/design_pair.json), [analytical audit](../evidence/checkpoint08/reviews/DESIGN_PAIR_INDEPENDENT_AUDIT.md) |

The two subsystem assignments exchange active factors and need not be contiguous spatial cuts. With no spectator degrees of freedom the difference mode vanishes, so its correlation is undefined. The [two-assignment derivation](../evidence/checkpoint08/options/TWO_CUT_THEORY.md) states these conditions. Exact rational identities and floating-point checks of exact formulas have different error guarantees. The latter are not certified interval bounds.

The [recorded clean reproduction](../evidence/checkpoint08/VALIDATION.json) passed all six programs. Five JSON outputs reproduced byte for byte; two numbers in the sixth differed by at most $5.73\times10^{-15}$ and passed the stated tolerance. The maintained [reproduction guide](../REPRODUCE.md) explains the current entry point. Its analytic reader figure evaluates the formula and adds no random states. Neither that figure nor these six checks independently establishes the all-order entropy theorem.

## A failed extension sets a useful boundary

The same predictions were tested on complete eigenbases of one nested local Floquet circuit family. The two sizes contain 256 eigenstates at eight spins and 1,024 at ten. Eigenstates of one operator are a dependent cohort, not independent disorder realizations. Both SWAP and phase-SWAP were chosen independently of the circuit and have the same flat operator Schmidt spectrum.

| Comparison | Eight spins | Ten spins |
|---|---:|---:|
| Input von Neumann variance / exact finite-dimensional Haar variance | 8.170846 | 5.686116 |
| SWAP von Neumann correlation; Haar-limit prediction `0.227732` | 0.812486 | 0.736736 |
| Phase-SWAP von Neumann correlation; same prediction | 0.850965 | 0.770672 |
| Nontrivial gate/order comparisons within all declared Haar tolerances | 0 of 6 | 0 of 6 |

All twelve gate/order/size comparisons failed the predeclared descriptive Haar bands. These bands are feasibility tolerances, not statistical critical values. At ten spins the mean von Neumann entropy was within about 1.27% of the Haar mean while its variance was still 5.69 times larger. Agreement of means therefore did not validate the fluctuation law. The two probe correlations were not separated enough to fail their independent equality band, so this experiment does not resolve a failure of operator-spectrum sufficiency between those probes.

This result limits the proposed extension to prepared eigenstates. It neither contradicts the Haar theorem nor determines a thermodynamic limit from two sizes. The branch stopped under its protocol. Sources: [full report](../limits/checkpoint09/REPORT.md), [frozen predictions](../limits/checkpoint09/results/predictions.json), [eight-spin summary](../limits/checkpoint09/results/summary_N8.json), [ten-spin summary](../limits/checkpoint09/results/summary_N10.json), and [independent numerical audit](../limits/checkpoint09/reviews/independent_audit.json). The two large eigenvector archives are regenerable but omitted from this repository; [their hashes and generating program](../provenance/OMITTED_GENERATED_FILES.json) and the [reproduction guide](../REPRODUCE.md) record that distinction.

## What remains open

A uniform finite-size error, support growing with system size, orders growing with dimension, shrinking-time limits, and generic prepared-state or subset-state extensions are unproved here. The evidence also supplies no practical gate-spectrum reconstruction guarantee. These are scope limits, not instructions to launch new numerical campaigns. Repository refurnishing uses the existing results and their qualifications; manuscript preparation comes after the repository is complete and checked.
