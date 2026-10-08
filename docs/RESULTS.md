# Results and evidence

The [covariance theorem](../theory/THEOREM.md) and [proof](../theory/PROOF.md) give the asymptotic law. This page collects its finite algebraic checks and numerical comparisons, with sources for the data and calculations.

Throughout this page, $`d`$ is the dimension of each half, entropies use natural logarithms, and order $`1/2`$ is pure-state logarithmic negativity. Absolute entropy covariances vanish as $`d^{-2}`$. See the [precise theorem](../theory/THEOREM.md) for the fixed-support, fixed-order, and finite-family assumptions, and the [scope and claims](SCOPE.md) for the distinction between asymptotic theorems, exact identities and numerical evidence.

## Direct entropy illustration

The non-diagonal pilot used **192 independent Haar inputs**: 96 at $`d=32`$ and 96 at $`d=64`$. Each input was reused for boundary SWAP and the Cartan gate $`\exp[-i(0.37\,XX+0.23\,YY+0.11\,ZZ)]`$, with orders $`1/2`$, $`1`$, and $`2`$ evaluated from the same spectra. Thus there were 384 gate applications, not 384 independent inputs. The protocol and predictions were fixed before sampling.

The observable below is the rescaled mean-square entropy increment, $`d^2\mathbb E[(S_\alpha(U\psi)-S_\alpha(\psi))^2]`$. Haar stationarity relates it to the covariance theorem. Each $`\pm`$ gives one sample standard error over the 96 independent inputs at that size.

| Gate | Order | Limiting prediction | Measured, $`d=32`$ | Measured, $`d=64`$ |
|---|---:|---:|---:|---:|
| SWAP | 1/2 | 0.206919 | 0.223061 ± 0.029482 | 0.202017 ± 0.025830 |
| SWAP | 1 | 0.386134 | 0.368730 ± 0.044852 | 0.374868 ± 0.051766 |
| SWAP | 2 | 0.750000 | 0.648855 ± 0.072884 | 0.713391 ± 0.100258 |
| Cartan | 1/2 | 0.102588 | 0.095598 ± 0.011438 | 0.114490 ± 0.014935 |
| Cartan | 1 | 0.169565 | 0.164616 ± 0.021260 | 0.173503 ± 0.024518 |
| Cartan | 2 | 0.319527 | 0.300049 ± 0.042827 | 0.305910 ± 0.048248 |

The pilot is broadly compatible with the predictions at these two sizes and three orders. Gate and order comparisons sharing an input are correlated; the displayed errors describe sampling variation and exclude finite-size bias. Standardized discrepancies are not calibrated significance tests.

Sources: [protocol](../studies/non_diagonal/README.md), [fixed predictions](../studies/non_diagonal/results/pilot_frozen.json), [implementation](../studies/non_diagonal/numerics/entropy_pilot.py), [complete summary](../studies/non_diagonal/results/pilot_summary.json), and saved arrays at [32-dimensional halves](../studies/non_diagonal/results/pilot_d32.npz) and [64-dimensional halves](../studies/non_diagonal/results/pilot_d64.npz). The displayed means and standard errors agree with direct recomputation from these arrays.

The ZZ and diagonal-gate cohorts are separate experiments. They are not pooled into the 192-state pilot. The 128-state diagonal comparison contains substantial adverse deviations: at $`d=128`$, gate B and time $`\pi/4`$, the measured increment statistics were `0.107929 ± 0.016960` against `0.181407` at order $`1/2`$, and `0.188963 ± 0.027740` against `0.326083` at order $`1`$. Some paired gate differences also had the opposite sign to their limiting prediction. Sampling and finite-size contributions to these discrepancies remain unresolved. See the [saved diagonal summary](../studies/haar/numerics/operator_results/summary.json) and [cohort definitions and interpretation](../studies/haar/README.md). The exact recurrence control in that cohort worked to about $`1.78\times10^{-15}`$ in entropy.

## Algebraic and deterministic checks

The leading Gaussian contraction calculation checked 68,786 networks across ten gates, including unequal $`2\times3`$ active factors. Mixed Chebyshev degrees through three agreed within about $`4.57\times10^{-13}`$; degree four for eight gates agreed within about $`3.79\times10^{-10}`$, after cancellation of larger monomial terms. This tests low-degree contraction identities in floating-point arithmetic. The all-degree result rests on the proof above. See [code](../studies/non_diagonal/numerics/general_gate_wick.py), [saved contractions](../studies/non_diagonal/numerics/general_gate_wick.json), and the [non-diagonal study](../studies/non_diagonal/README.md).

The focused reproduction runs these six deterministic programs. The result links contain their reference outputs.

| Calculation | Scope and recorded result | Code and saved output |
|---|---|---|
| Moment inversion | Exact matrix and Newton checks through rank 12, including error amplification and deterministic spectra; passed | [Code](../checks/inverse/inverse_moments.py), [results](../checks/inverse/inverse_results.json) |
| Whole-system purity identity | 14 gates, 336 fourth-Haar-moment permutation traces; largest unnormalized trace difference about $`1.14\times10^{-13}`$ | [Code](../checks/finite_purity/check_exact_global_purity.py), [results](../checks/finite_purity/exact_global_purity_results.json) |
| Two subsystem assignments, full-system contraction | 14 active-gate/spectator cases; largest mode-correlation difference about $`1.66\times10^{-14}`$ | [Code](../checks/finite_purity/check_two_cut_modes.py), [results](../checks/finite_purity/two_cut_modes_results.json) |
| Two-assignment symbolic identities | Eight exact sparse-polynomial identities for centering, variance, and modes; all passed | [Code](../checks/symbolic/two_cut_symbolic_audit.py), [results](../checks/symbolic/two_cut_symbolic_audit.json) |
| Separate purity-sum and product-input contractions | 15 active gates at dimensions 2, 3, 4 and five spectator sizes; 75 correlations agree within $`1.29\times10^{-12}`$; entangling-power formulas within $`1.11\times10^{-16}`$ | [Code](../checks/numerics/two_cut_check.py), [results](../checks/results/two_cut_check.json) |
| Exact gate-design pair | Two full two-copy twirling superoperators agree with Haar within $`3.25\times10^{-16}`$ in Frobenius norm; limiting order-three correlation difference is exactly $`3\sqrt5/20000`$ | [Code](../checks/numerics/design_pair.py), [results](../checks/results/design_pair.json), [analytical derivation](../theory/GATE_DESIGNS.md) |

The two subsystem assignments exchange active factors and need not be contiguous spatial cuts. With no spectator degrees of freedom the difference mode vanishes, so its correlation is undefined. The [two-assignment derivation](../theory/TWO_CUTS.md) states these conditions. Exact rational identities and floating-point checks of exact formulas have different error guarantees. The latter are not certified interval bounds.

The [reproduction guide](../REPRODUCE.md) gives commands and comparison tolerances.

## Floquet eigenstate comparison

The same predictions were tested on complete eigenbases of one nested local Floquet circuit family. The two sizes contain 256 eigenstates at eight spins and 1,024 at ten. Eigenstates of one operator are a dependent cohort, not independent disorder realizations. Both SWAP and phase-SWAP were chosen independently of the circuit and have the same flat operator Schmidt spectrum.

| Comparison | Eight spins | Ten spins |
|---|---:|---:|
| Input von Neumann variance / exact finite-dimensional Haar variance | 8.170846 | 5.686116 |
| SWAP von Neumann correlation; Haar-limit prediction `0.227732` | 0.812486 | 0.736736 |
| Phase-SWAP von Neumann correlation; same prediction | 0.850965 | 0.770672 |
| Nontrivial gate/order comparisons within all declared Haar tolerances | 0 of 6 | 0 of 6 |

All twelve gate/order/size comparisons failed the predeclared descriptive Haar bands. These bands are feasibility tolerances, not statistical critical values. At ten spins the mean von Neumann entropy was within about 1.27% of the Haar mean while its variance was still 5.69 times larger. Agreement of means therefore did not validate the fluctuation law. The two probe correlations were not separated enough to fail their independent equality band, so this experiment does not resolve a failure of operator-spectrum sufficiency between those probes.

These observations concern the two sampled Floquet operators. Sources: [full report](../studies/floquet/README.md), [fixed predictions](../studies/floquet/results/predictions.json), [eight-spin summary](../studies/floquet/results/summary_N8.json), [ten-spin summary](../studies/floquet/results/summary_N10.json), and [independent numerical audit](../studies/floquet/verification/independent_audit.json). The two large eigenvector archives are regenerable but omitted from this repository; [their hashes and generating program](../studies/floquet/omitted_arrays.json) and the [reproduction guide](../REPRODUCE.md) record that distinction.
