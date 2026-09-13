# Checkpoint 09: primary literature and interpretation limits

Scope: a bounded audit before inspecting the checkpoint's Floquet entropy measurements. The numerical target is a nearest-neighbor, two-layer, periodically repeated circuit with independent generic complex two-qubit gates, and complete eigenbases at eight and ten qubits. This note does not authorize a larger numerical survey.

## Closest precedent for absolute fluctuations

J. F. Rodriguez-Nieva, C. Jonay, and V. Khemani, *Quantifying quantum chaos through microcanonical distributions of entanglement*, Phys. Rev. X **14**, 031014 (2024), [arXiv:2305.11940v1](https://arxiv.org/html/2305.11940v1), is more directly relevant to static entropy variance than the initially suggested Hahn–Luitz–Chalker paper. Its Section III uses periodically repeated odd/even Haar U(4) layers with periodic spatial boundaries. The study compares eigenstate von Neumann entropy distributions with complex Haar states. It reports near agreement of means together with a persistent enhancement of the variance prefactor. Thus ordinary level statistics and Page-like average entropy do not establish Haar fluctuations. Appendix C examines increasing gate range or Floquet period, finding closer variance agreement with Haar. These interventions therefore have direct precedent.

The paper's periodic boundaries give two crossing bonds for a half-chain, whereas an open chain has one. Its fluctuation prefactor should not be imported as a prediction for the present open-chain sample. Its exact finite-dimensional complex-Haar von Neumann variance, Eq. (A4), is a useful independently available reference; the inherited asymptotic benchmark is \(d^2\operatorname{Var}S_1\to1/4\).

## Correlated eigenstates and weak links

D. Hahn, D. J. Luitz, and J. T. Chalker, *Eigenstate correlations, the eigenstate thermalization hypothesis, and quantum information dynamics in chaotic many-body quantum systems*, Phys. Rev. X **14**, 031029 (2024), [arXiv:2309.12982v2](https://arxiv.org/html/2309.12982v2), studies correlations among multiple Floquet eigenstates that encode entanglement dynamics and operator spreading beyond conventional ETH. It does not establish the present same-state entropy response covariance formula for a separate boundary probe.

Section III.1, Section V.1, and Appendices A.2 and C give a concrete warning for this experiment: unrestricted qubit Haar gates can produce weak links and appreciable realization fluctuations. Their main qubit calculations truncate high operator-purity gates; the unrestricted model requires separate treatment. Record the present circuit's gate purities as diagnostics, retain the initially selected realization, and do not silently substitute their truncated ensemble.

The complete eigenbasis is a correlated orthonormal collection. Treat it as a census of one realization. A bootstrap that independently resamples its eigenstates does not provide uncertainty over the circuit ensemble.

## Exact single-crossing constraint

The following is an elementary deduction from circuit structure, independently obtained in the present audit and by the root researcher. It is not attributed as a theorem from either cited paper, and novelty is not claimed.

Let an open-chain Floquet period contain exactly one gate \(G\) crossing the cut. All other gates preserve the Schmidt spectrum across that cut. In a stroboscopic frame immediately before the crossing gate, write

\[
F=L G,
\]

where \(L=L_A\otimes L_B\). For every Floquet eigenstate,

\[
F|\psi_j\rangle=e^{i\theta_j}|\psi_j\rangle
\quad\Longrightarrow\quad
G|\psi_j\rangle=e^{i\theta_j}L^\dagger|\psi_j\rangle.
\]

Consequently the complete Schmidt spectrum, and every spectral entanglement measure, is identical before and after \(G\). At a frame with \(F=G L\), the corresponding identity uses \(G^\dagger\). For the more general representation \(F=L_2 G L_1\), move to the local frame \(|\chi_j\rangle=L_1|\psi_j\rangle\), where the Floquet operator is \(L_1L_2G\).

This supplies an exact counterexample to an unrestricted extension of the Haar memory law to Floquet eigenstates with a probe selected from their generating circuit. It holds at every size and does not rely on a small numerical variance. It does **not** refute a conjecture restricted to probes chosen independently of the circuit. For entropy correlation, a value of one additionally requires nonzero across-eigenstate variance; spectrum preservation remains meaningful even if that variance vanishes.

This identity is not explicitly developed in the inspected portions of either cited paper. That absence is not evidence of originality: it is an immediate consequence of stationarity and locality. The identity also explains why the present open-boundary setup differs from the two-crossing periodic model of Rodriguez-Nieva et al.

## Model and comparison rules

1. **Complex ensemble.** Generic unconstrained complex U(4) gates make the complex-Haar benchmark the intended comparison. Real orthogonal gates, symmetric-unitary constructions, charge-conserving gates, or imposed spatial symmetries change the problem. The absence of an obvious computational-basis symmetry is not a proof that all antiunitary symmetries are absent.
2. **Stroboscopic convention.** Fix the order of the two layers and the exact cut. In the ordinary site indexing, changing from eight to ten sites changes which layer contains the central bond. A local frame change preserves the unperturbed Schmidt spectrum but can change its relation to a fixed boundary probe. Record this convention before interpreting a size trend.
3. **Fixed probes.** The independent SWAP and phase-SWAP probes remain valid bounded tests. An additional actual-gate stationarity control answers a different question and must be labeled as circuit-correlated.
4. **Separate scales.** Record raw covariance, both marginal variances, mean change, and normalized correlation. Agreement after normalization can coexist with failure of the absolute Haar scale. The Floquet eigenstate distribution is not automatically invariant under an independent local probe, so equality of the two marginal means or variances must be checked rather than assumed.
5. **No fictitious replication.** Two complete eigenbases are two deterministic realization-level observations. If the circuits differ as well as size, their difference combines realization and size effects. Neither the number of eigenvectors nor the number of tested entropy orders multiplies the number of independent circuit realizations.
6. **Benchmark scope.** The inherited entropy covariance theorem takes balanced subsystem dimension to infinity with fixed probe support and Haar initial states independent of the probe. Finite eight- and ten-qubit eigenstate calculations can support or fail this extension as a feasibility test; they cannot establish its asymptotic universality.

## Research decision that the literature supports

An enhanced entropy variance would reproduce an established physical phenomenon. Finding the elementary stationarity constraint would explain a clear limit but would not by itself supply a PRL-level contribution. A potentially informative positive outcome is agreement of independently chosen probe correlations despite non-Haar marginal variances; it would still need a mechanism explaining why the normalized structure survives. Conversely, strong probe-dependent deviations should be retained and used to stop claims of immediate eigenstate universality. Enlarging the present sample solely to reconfirm known variance anomalies would fit the user's research preference poorly.

This is a focused primary-source check, not an exhaustive originality review. No eigenstate entropy measurements were inspected while writing it.
