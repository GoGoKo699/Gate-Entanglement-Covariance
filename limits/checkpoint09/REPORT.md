# Floquet eigenstates do not pass the Haar memory test

Entanglement Temporal Fluctuations, checkpoint 09. 12 September 2026.

## Outcome and research decision

The bounded two-size Floquet test fails all twelve nontrivial gate/order comparisons under the criteria fixed before computing eigenstate responses. Both the fluctuation scale and the normalized entropy memory differ substantially from the Haar benchmark. This does not challenge the proven Haar result or establish the thermodynamic behavior of Floquet eigenstates. It means the proposed immediate extension has failed its first declared feasibility test.

The literature already contains enhanced entropy fluctuations in local Floquet eigenstates, so that failure cannot be repackaged as a new PRL mechanism. We retain the proved Haar-limit covariance law as a benchmark and stop this numerical branch at its declared two sizes. A larger survey would not resolve the missing conceptual contribution. The project remains open in scope, without an external repository.

## 1. What was fixed and computed

The model is an open spin chain with a periodically repeated two-layer nearest-neighbor circuit. Every bond carries one generic complex U(4) gate, fixed across periods. The eight- and ten-spin systems share all common bond gates. Coordinates are centered on the same cut so the crossing gate stays in the first layer at both sizes. There are no imposed conservation laws or spatial symmetries. The seed, gate-generation rule, boundary convention, and all probes were frozen before diagonalization.

The state ensemble is the entire Floquet eigenbasis: 256 states at eight spins and 1,024 at ten. There is one nested circuit family. These complete orthonormal cohorts are dependent; their size does not provide independent disorder replication or an independent-state confidence interval.

Three probes act on the central pair of qubits:

1. Identity, as an exact zero-change control.
2. SWAP.
3. Phase-SWAP, `SWAP exp(−iπZZ/4)`.

The two nontrivial probes are fixed independently of the circuit realization. Both have normalized operator Schmidt probabilities `(1/4,1/4,1/4,1/4)`. The inherited Haar law therefore predicts the same limiting entropy correlation for them at every fixed positive order. We selected orders one half, one, and two, corresponding to pure-state logarithmic negativity, von Neumann entropy, and Rényi-2 entropy. All entropies use natural logarithms.

Every state's entropy and purity were retained. No spectral-tail exclusions, selected quasienergy windows, gate rejections, seed replacements, or fitted coefficients were used. The exact finite-dimensional Haar purity statistics and exact von Neumann mean/variance were frozen alongside the limiting entropy predictions.

The protocol calls a nontrivial comparison within its descriptive Haar band only when input/output variance ratios and the mean-square increment ratio are between 0.75 and 1.25, the correlation residual is at most 0.10, and the mean shift is at most 0.25 input standard deviations. These are feasibility tolerances, not calibrated statistical critical values or proven finite-size error bounds. The continuous results matter more than the binary label.

## 2. The absolute fluctuation scale fails an exact finite-size reference

The von Neumann comparison is particularly decisive because its Haar marginal variance is known exactly at these finite dimensions [1]. There is no need to attribute the difference to an uncontrolled large-d approximation.

| Spins | Half dimension | Observed mean `S₁` | Exact Haar mean | Observed variance / exact Haar variance |
|---|---:|---:|---:|---:|
| 8 | 16 | 2.191083 | 2.274866 | 8.170846 |
| 10 | 32 | 2.928578 | 2.966305 | 5.686116 |

At ten spins the mean differs by approximately 0.03773 nats, about 1.27% of the Haar mean, while the variance is still 5.69 times as large. The finite-Haar variance itself is only 0.26% below its leading asymptotic value at this size. Mean entanglement being relatively close does not validate its fluctuation law.

The purity check independently shows a large excess: input purity variances are 15.93 and 8.53 times their exact Haar values at eight and ten spins. These are finite-cohort facts. The downward size trend does not determine an asymptotic limit from two sizes.

## 3. Normalized memory also fails

For either nontrivial probe, the inherited Haar-limit correlations are approximately `0.172322`, `0.227732`, and `0.25` at orders one half, one, and two.

| Order | Haar-limit prediction, both probes | 8 spins, SWAP | 8 spins, phase-SWAP | 10 spins, SWAP | 10 spins, phase-SWAP |
|---|---:|---:|---:|---:|---:|
| 1/2 | 0.172322 | 0.743883 | 0.805898 | 0.660755 | 0.697243 |
| 1 | 0.227732 | 0.812486 | 0.850965 | 0.736736 | 0.770672 |
| 2 | 0.250000 | 0.833044 | 0.847074 | 0.767407 | 0.797838 |

All twelve comparisons miss the declared correlation band by a wide margin. Every corresponding input and output variance also misses its scale band. The identity control is exact.

The purity correlations have exact finite-Haar comparisons. At ten spins, observed SWAP and phase-SWAP purity correlations are `0.771542` and `0.800942`, while their exact Haar references are `0.250737` and `0.248779`. Thus even a polynomial observable with no entropy-series approximation shows the same large mismatch.

The two independent probes differ from one another by less than the declared 0.10 equality band at every order and size. We therefore do **not** claim this test resolves a failure of operator-Schmidt-spectrum sufficiency between independent probes. It resolves a failure of their common Haar prediction in the finite cohorts.

![Exact variance reference and probe correlations](figures/floquet_comparison.png)

Figure: one nested open-chain circuit family. Panel (a) uses the exact finite-dimensional Haar von Neumann variance. Panel (b) compares the ten-spin correlations with the fixed-support entropy limit. There are no error bars because no independent circuit ensemble was sampled. Connecting lines in panel (b) guide the eye across three fixed orders.

## 4. Higher correlation does not mean a smaller response here

The eigenstate ensemble has both higher normalized memory and larger absolute mean-square entropy changes than Haar predicts. At ten spins:

| Order | SWAP mean-square change / Haar-limit prediction | Phase-SWAP ratio |
|---|---:|---:|
| 1/2 | 1.791661 | 1.674149 |
| 1 | 2.116889 | 1.928102 |
| 2 | 2.466718 | 2.216621 |

There is no contradiction. For any finite cohort,

\[
\mathbb E[(S_{\rm out}-S_{\rm in})^2]
=v_{\rm out}+v_{\rm in}-2\operatorname{Cov}(S_{\rm out},S_{\rm in})
+(\mu_{\rm out}-\mu_{\rm in})^2.
\]

The broad input variation survives the probe in part, giving a high correlation, while the absolute response can remain large. Both probes reduce the marginal variance substantially. At ten spins they also increase the mean by about 0.013 nats at order one, so stationarity of the probe-transformed ensemble cannot be assumed. Those mean shifts are approximately 0.345 input standard deviations and fail their declared descriptive band.

This decomposition explains the statistical coexistence of the observations. It does not identify a new microscopic mechanism for the excess variance or the retained memory, and it is not a fitted reduced model.

## 5. An exact limitation known before the numerical outcomes

There is a separate structural statement about a probe correlated with the state-generating circuit. In the chosen starting frame the Floquet period has the form

\[
F=L G_c,\qquad L=L_A\otimes L_B,
\]

because only one gate `G_c` crosses the open-chain cut during a period. For each Floquet eigenstate,

\[
F|\psi_j\rangle=e^{i\theta_j}|\psi_j\rangle
\quad\Longrightarrow\quad
G_c|\psi_j\rangle=e^{i\theta_j}L^\dagger|\psi_j\rangle.
\]

The entire Schmidt spectrum is therefore unchanged by the circuit's own crossing gate. Every entropy and purity increment vanishes, even though that gate is generally entangling on other inputs. In a different starting frame one must transform the state or the probe consistently. With two spatial crossings or multiple crossing gates per period, individual-gate entropy changes need not vanish.

This elementary stationarity argument already prevents an unconditional replacement of Haar states by Floquet eigenstates in the gate-spectrum-only law. The independence between state and gate assumed by the Haar reference is absent. It does not prove that our two independent probes must deviate, or explain the size of their deviations.

As a numerical anchor, the own-crossing-gate identity was checked on the 16 fixed representative indices per size, separately from the three primary probes. The maximum entropy change was approximately `1.78×10⁻¹⁵`. The central gate has operator purity about `0.48649`, so it is not a product gate. The identity was derived and documented before response data were computed; it is not a discovered numerical fit or a novelty claim.

## 6. What the model checks establish

The circuit has circular adjacent-gap ratios approximately 0.632 and 0.604. Computational-basis participation has scaled inverse participation ratios about 2.096 and 2.039. The checked total-Z, Z-parity, spin-flip, and reflection operators have nonzero normalized commutators with the Floquet operator. No eigenphase degeneracy was numerically unresolved. These observations support using this as a generic complex finite Floquet example; they do not prove asymptotic chaos or absence of every hidden symmetry.

All bond operator purities are recorded. The common central bond and its neighbors are preserved when the chain is extended. The maximum bond operator purity is about 0.52063 in both sizes. No weak-link truncation was applied. Prior work warns that unrestricted qubit Haar gates can produce substantial realization effects [3], so the result cannot be generalized to every random circuit on the strength of one realization.

## 7. Validation and reproducibility

The complex Schur decomposition supplies an orthonormal eigenbasis. Largest eigenvector residuals are approximately `2.53×10⁻¹⁴`; orthogonality errors are below `2.49×10⁻¹⁴`. Entropies are evaluated from singular values without truncating small Schmidt probabilities.

The independent numerical audit rebuilds the Floquet operator with Kronecker embeddings, checks its action on all 1,280 saved eigenvectors, evaluates probe entropies through reduced-density-matrix eigenvalues on 96 fixed state/probe representatives, and recomputes the full summaries from saved scalar arrays. The independent entropy calculations agree within `6.22×10⁻¹⁵`; the largest summary discrepancy is `2.59×10⁻¹²`, arising in ratios using an independently evaluated reference variance. All comparison criteria reproduce. These are internal independent checks, not external peer review.

The fresh-directory reproduction passed the predictor, both complete cohort calculations, the independent audit, and figure generation. Every saved numerical array, including the eigenvectors, reproduced byte for byte; summary comparisons exclude elapsed wall time. The records are included under `reviews/` and `VALIDATION.json`.

There are 1,280 eigenstates, 3,840 state/probe spectral records including identity, and three entropy orders per record. The own-crossing-gate anchors are 32 additional selected state/gate checks of an already derived identity. No independent Haar-state sampling or second circuit realization was introduced.

One implementation repair is retained explicitly. The first eight-spin run reached its summary writer, which rejected a NumPy boolean. The fix converts NumPy scalars for JSON serialization. The original frozen source remains in `history/`. All scientific inputs and comparisons stayed fixed, and the deterministic run was restarted without inspecting response output from that failed write.

## 8. Novelty assessment and stopping decision

Rodriguez-Nieva, Jonay, and Khemani already studied entropy distributions of local Floquet eigenstates and their deviations from Haar [2]. Their work finds that the second moment can remain enhanced when familiar level statistics look thermal. Their periodic-boundary model differs from this open chain, so its numerical prefactor is not our prediction, but the general fluctuation phenomenon is established. Their longer-period and longer-range interventions also mean that simply adding such a control would follow an existing line closely.

Hahn, Luitz, and Chalker study spatial eigenstate correlations governing entanglement dynamics and operator spreading beyond ordinary ETH [3]. Our same-state, independent-probe entropy covariance is a different observable. A different observable alone does not establish a new physical mechanism or PRL significance.

The declared positive target was useful agreement with a parameter-free Haar law in a modest physical test. That target was not achieved. The known stationarity constraint clarifies the scope, and the independent probes show substantial discrepancies, but their microscopic explanation remains unestablished.

The appropriate decision is to stop this branch here. Preserve the all-order Haar covariance law and the negative result. Do not expand the calculation merely to tune the model toward Haar or reconfirm known eigenstate fluctuation anomalies. For the user's preferred balance of insight, compact theory, and modest numerics, the next research direction needs a fresh physical question rather than another incremental extension of the present benchmark. No repository is needed yet.

## Primary references

1. Lu Wei, *Proof of Vivo-Pato-Oshanin's conjecture on the fluctuation of von Neumann entropy*, Phys. Rev. E **96**, 022106 (2017). [Primary article](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.96.022106). Exact finite-dimensional Haar von Neumann variance; the formula is explicitly provided in the article abstract. The exact Haar mean is Page's formula, also reviewed in reference 2.
2. J. F. Rodriguez-Nieva, C. Jonay, V. Khemani, *Quantifying Quantum Chaos through Microcanonical Distributions of Entanglement*, Phys. Rev. X **14**, 031014 (2024). [Primary paper](https://arxiv.org/abs/2305.11940), Section III and Appendix C.
3. D. Hahn, D. J. Luitz, J. T. Chalker, *Eigenstate Correlations, the Eigenstate Thermalization Hypothesis, and Quantum Information Dynamics in Chaotic Many-Body Quantum Systems*, Phys. Rev. X **14**, 031029 (2024). [Primary paper](https://arxiv.org/html/2309.12982v2), Sections III.1 and V.1, Appendices A.2 and C.

The inherited covariance theorem and exact finite-purity identity are copied with provenance into `foundation/`. Their literature sources and limitations remain part of those derivations.
