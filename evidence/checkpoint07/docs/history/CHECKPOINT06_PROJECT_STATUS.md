# Entanglement Temporal Fluctuations: project decision and checkpoint 06

12 September 2026.

**This is the right moment to create a separate research repository and GPT project.** The work now has a self-contained question, a stated analytical result, supporting calculations, and a clear unresolved scientific decision. The suggested name is **Entanglement Temporal Fluctuations**, with repository slug `Entanglement-Temporal-Fluctuations`.

I have prepared the standalone project, but have not created an external repository. Entanglement-Trajectories remains unchanged and frozen. Boundary-Entangling-Susceptibility is also unchanged. Neither is a dependency of this package.

Repository readiness does not settle the PRL question. The result is coherent enough to develop independently. Its originality and broad physical significance still need to earn that ambition.

## The important correction to the earlier assessment

The focused novelty review exposed a weakness in using the quarter-order threshold and the `8α` short-time exponent as the headline. The same leading law, including its leading coefficient for the ZZ comparison, follows from the standard smooth Gaussian interpolation

\[
G(t)=\cos t\,G_0+\sin t\,G_1.
\]

Its spectral-mode memory is `cos(τ)^(2k)`. The physical ZZ gate adds `sin(τ)^(2k)`, but that addition changes the entropy increment only by `O(τ^4)` near zero. It does not alter the leading anomalous law. This comparison is a derivation from established Gaussian fluctuation machinery, not a claim that a prior paper has printed our entropy exponent. Temporal Wishart fluctuation fields and shifted-Chebyshev diagonalization are established foundations [1,2].

Thus the exponent remains a valid consequence within the stated limit, but it is not evidence of a uniquely quantum or local dynamical mechanism. My earlier PRL assessment was too optimistic if read as relying on that exponent alone.

The current scientific center is the **complete finite-time relation between a physical gate and equilibrium entropy covariance**.

## What was added in this checkpoint

The original ZZ calculation now extends to every fixed diagonal boundary Hamiltonian with finite active dimensions `r × s`. The initial state is complex Haar on a balanced `d × d` cut; spectator dimensions grow while `r`, `s`, and the Hamiltonian stay fixed.

For diagonal energies `h_ab`, form

\[
Q_{ab}(\tau)=\frac{e^{-i\tau h_{ab}}}{\sqrt{rs}},
\qquad \eta_\ell(\tau)=\operatorname{eig}_\ell[Q(\tau)Q(\tau)^\dagger].
\]

The `ηℓ` sum to one and are the normalized operator-Schmidt probabilities of the relative gate. The derived relation is

\[
\lim_{d\to\infty}d^2\operatorname{Cov}
 [S_\alpha(t),S_\beta(s)]
=\frac14\sum_{k\ge2}k c_{\alpha k}c_{\beta k}
 \sum_\ell\eta_\ell(t-s)^k.
\]

The entropy coefficients are explicit and the series converges for every fixed positive pair of Rényi orders. The proof evaluates the phase around the surviving annular Wick cycle, then uses stationary marginal approximation and the entropy normalization. Established low-regularity square-LUE results supply the required approximation [3].

The interpretation is simple: **the gate's operator-Schmidt power sums determine how much covariance each entanglement-spectrum fluctuation mode retains**. A common gate acts on both times' same initial random state; two independent Haar draws would erase the object being studied.

For Rényi-2, the normalized entropy covariance reduces to operator purity. Its increment equals linear operator entanglement, a quantity already related to the bipartite OTOC [4]. This familiar order-two connection is acknowledged as prior structure. The full formula retains higher operator moments and applies to von Neumann entropy and pure-state logarithmic negativity as well.

## A consequence beyond matching purity

Consider two diagonal gates supported on at most two qubits on each side. Gate A has operator weights

\[
\eta^A=(1/2,1/2).
\]

For gate C, choose

\[
p=\frac{1+\sqrt{\sqrt2-1}}2,
\qquad
\eta^C=(p^2,p(1-p),p(1-p),(1-p)^2).
\]

The second spectrum comes from two independent commuting ZZ gates with `cos²θ=p`. Both spectra have purity exactly `1/2`. Nevertheless their higher power sums obey

\[
\sum_\ell(\eta^C_\ell)^k>
\sum_\ell(\eta^A_\ell)^k\quad(k>2).
\]

A one-line strict Jensen argument proves the inequality. Positive same-order coefficients in the covariance series then give **strictly greater entropy covariance for C at every positive Rényi order except two**, where it is exactly equal. The two operator spectra themselves are incomparable by majorization; the power-sum proof is the relevant ordering here.

Some analytical covariance values, with natural logarithms, are:

| Entropy order | Gate A: limiting `d² Cov` | Gate C: limiting `d² Cov` |
|---|---:|---:|
| 1/2, pure-state logarithmic negativity | 0.04705283 | 0.04991978 |
| 1, von Neumann entropy | 0.11698406 | 0.11886026 |
| 2 | 0.25000000 | 0.25000000 |

These are analytical series evaluations, not estimates from new random states. The construction matches gate operator purity only; it does not also match Hamiltonian spectrum, duration, or strength. The differences at ordinary orders are modest. The insight is an exact distinction in what the observables resolve, not a claim of a large experimental effect.

A separate general corollary is that operator-spectrum majorization orders every same-order entropy covariance within the proved gate class. Greater concentration gives greater retained covariance. This does not order arbitrary cross-order covariance terms.

## The bounded numerical check

One new numerical protocol was fixed before generating its states. It used 64 independent Haar states at each of `d=64` and `d=128`: **128 independent states and 512 exact diagonal-pulse entropy evaluations**. Each state was reused across two gates and two times; five entropy orders were evaluated from each resulting spectrum.

This check concerns a different analytical pair, A and B, whose diagonal Hamiltonians have the same eight positive and eight negative energies, norm one, and centered interaction strength one. Their gate weights are

\[
\eta^A(t)=(\cos^2t,\sin^2t),\qquad
\eta^B(t)=(\cos^2t,\tfrac12\sin^2t,\tfrac12\sin^2t).
\]

At `t=π/2`, A becomes a product unitary and returns every state's entanglement exactly. B remains entangling. The predicted limiting values of `d² E(ΔS₂)²` are zero and one half respectively. At `d=128`, the measured B value is **0.55194 ± 0.09013**, where the error is one sample standard error. The maximum A recurrence error over both sizes and all orders is **1.78 × 10⁻¹⁵**.

Other comparisons are substantially less favorable and remain in the package:

| B at `d=128`, `t=π/4` | Measured increment statistic | Sample SE | Large-d prediction |
|---|---:|---:|---:|
| Order 1/2 | 0.107929 | 0.016960 | 0.181407 |
| Order 1 | 0.188963 | 0.027740 | 0.326083 |

Several paired B-minus-A estimates at that point are negative, despite positive limiting predictions. The corresponding `d=64` B cohort lies above the predictions. We have not established how much of these discrepancies comes from finite dimension and how much from sampling. Ratios to estimated sample errors of squared increments are not calibrated Gaussian significance scores, and comparisons across orders are correlated.

The pilot therefore supports the exact recurrence contrast more clearly than it establishes quantitative convergence of the full kernel. No extra states were added to make the result look cleaner. The earlier 1,536-state ZZ campaign is retained as inherited evidence, with its existing limitations; it was not repeated or counted as new data for this extension.

## Verification and its limits

Two internal reviews inspected the diagonal extension and the stronger equal-purity example. No material mathematical defect was identified in the stated scope. Independent integer Wick enumeration through trace degree three agrees exactly for both new phase arrays, including mixed-mode covariances. Deterministic operator-spectrum and local-gauge checks have maximum discrepancies below `3.34 × 10⁻¹⁶`. Saved numerical summaries and frozen source/plan hashes were independently checked.

The earlier all-degree argument and low-regularity entropy extension remain included, with their original proof reviews. The standalone package also has a clean-directory portability check recorded in VALIDATION.json. Internal checking is not external peer review or proof that no defect remains.

The theorem does not cover arbitrary non-diagonal gates or physically prepared thermal states. It gives covariance and finite-dimensional Gaussian limits at fixed times, not convergence of whole sample paths or a uniform finite-size shrinking-time law. Means remain stationary and unscaled fluctuations shrink as `1/d`.

## PRL assessment and the next scientific decision

This direction fits the preferred style better now: one organizing relation, short physical corollaries, and a bounded numerical illustration. A full all-order covariance law conveys more than another short-time exponent. The equal-purity example makes that additional content explicit.

It is still possible that a referee will judge this as a technically clean combination of familiar operator entanglement and Wishart fluctuation theory. The focused primary-literature review did not find a direct statement of the full law, but it found important close predecessors and recent neighboring work [1–6]. Absence of a direct match is not sufficient evidence of PRL-level significance.

The next useful discriminator is a small analytical test of the relation outside diagonal gates, with an explicit search for where the proposed operator-spectrum description fails. That can decide whether there is a broader physical organizing principle or only a special exactly solvable family. It should be resolved before launching more simulations. If the broader interpretation fails to add a clear physical insight, retain the result as a focused quantum-information or mathematical-physics project and reassess the journal ambition.

## Repository and GPT-project handover

The standalone folder includes README, scope and claim registry, this assessment, a manuscript feasibility draft, proof notes, numerical source and arrays, figures, literature records, internal reviews, and reproduction instructions. It imports only the directly relevant checkpoint-05 material and records those files' hashes. It contains no Entanglement-Trajectories source or trajectory archive.

Create the new repository and GPT project when ready; this is the point I recommend separating them. Use START_NEW_WORKSPACE.md as the opening context. The package itself is suitable as the initial research tree. No repository, tag, release, or publication has been created by preparing it.

## Primary sources

1. Kusalik, Mingo, and Speicher, *Orthogonal Polynomials and Fluctuations of Random Matrices*, J. Reine Angew. Math. 604 (2007). https://arxiv.org/abs/math/0503169
2. Kuan and Zhou, *Three-dimensional Gaussian fluctuations of spectra of overlapping stochastic Wishart matrices* (2021). https://arxiv.org/abs/2112.13728
3. Hu, *On the regularity conditions in the CLT for the LUE* (2023), Theorem 1.1, Lemma 1.2, and Corollary 1.3. https://arxiv.org/abs/2310.08509
4. Styliaris, Anand, and Zanardi, *Information Scrambling over Bipartitions: Equilibration, Entropy Production, and Typicality*, Phys. Rev. Lett. 126, 030601 (2021). https://arxiv.org/abs/2007.08570
5. Cotler, Hunter-Jones, and Ranard, *Fluctuations of subsystem entropies at late times*, Phys. Rev. A 105, 022416 (2022). https://arxiv.org/abs/2010.11922
6. Lim, Lou, and Tian, *Mesoscopic fluctuations in entanglement dynamics*, Nature Communications 15, 1775 (2024). https://arxiv.org/abs/2305.09962

The fuller source ledger includes inspection depth, additional operator-entanglement foundations, and the September 2026 novelty check. The scalar-interpolation comparison and the physical distinctions drawn here are our analytical inferences from those foundations.
