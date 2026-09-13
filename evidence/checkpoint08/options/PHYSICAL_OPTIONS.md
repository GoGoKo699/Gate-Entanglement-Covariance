# Focused scientific options after checkpoint 07

2026-09-12. Independent assessment. No new Haar sampling was performed. The question is what makes the covariance theorem physically useful, not how many further corollaries can be added.

## Recommendation

The strongest bounded next discriminator is **an exact pair of gates with the same standard second-moment transfer operator, but different equilibrium entropy fluctuation memories**. The sum of fluctuations across two exchanged boundary cuts provides a useful calibration: it restores information about active product-input entangling power that a one-cut covariance family can lose. The derivations are short and need no enlarged simulation campaign.

Its novelty case remains conditional. The distinction between SWAP transport and entanglement generation, the operator-entanglement expression for entangling power, and the higher-replica entanglement-feature framework are established. The potential contribution is the closed relation to actual fixed-positive-order entropy covariances and a precise example of what second-moment descriptions miss. It should not be marketed as inventing a transport/production distinction or as an experimentally efficient gate-characterization scheme.

## Option 1: Two cuts recover active entangling power

Take fixed active factors `a,b` of dimension `q`, equally large spectators `A0,B0`, and two balanced subsystems `A=A0a`, `C=A0b`. Let `P` swap `a,b`. The pairwise covariance matrix between before/after cut entropies is

\[
\begin{pmatrix}\kappa(U)&\kappa(PU)\\\kappa(PU)&\kappa(U)\end{pmatrix},
\]

where `κ` is the checkpoint-07 kernel. The eigenvectors are the sum and difference of the two centered cut entropies. For Rényi-2,

\[
\operatorname{Corr}(X_+^{\rm after},X_+^{\rm before})
\longrightarrow
1-\frac{(q+1)^2}{q^2+1}e_{p,a:b}(U).
\]

The active entangling power averages linear entropy generated from product states on `a:b`; it differs from averaging products across the full large halves. The sum observable is exactly invariant under SWAP for every input state. Nevertheless, `SWAP exp(−iφZZ)` decorrelates this sum when its phase interaction is nontrivial, even though all those gates have identical complete same-cut entropy memories.

For qubits, the same-cut correlation stays `1/4`, but the sum-mode correlation is `1−(2/5)sin²(2φ)`. This makes the interpretation more legible: measuring entanglement fluctuations only at one partition loses information that appears when the active factors are assigned to the opposite sides.

**Bounded discriminator:** audit the two-cut formula and the candidate exact purity-sum identity using four-copy contractions on deterministic gates. No new sample survey is needed. A one-panel analytical plot of the phase-SWAP family would explain the physical separation more clearly than another large-dimensional Monte Carlo figure.

**Failure/stop criterion:** if the putative novelty reduces completely to re-labeling already published state-purity covariance formulas, retain this as an explanatory corollary of the all-order theorem and seek a different main contribution. The α=2 result alone may not carry a PRL. The all-order entropy law and an insightful distinction beyond α=2 remain important.

The detailed derivation is in `TWO_CUT_THEORY.md`. Its section 8 records the subsequent novelty stress test: the leading sum and difference modes are exactly the established entangling-power and gate-typicality combinations. It also gives the stronger matched-transfer comparison. Two diagonal `q=4` gates have the same `𝒫_op(U)=1/2`, `𝒫_op(PU)=1/16`, active entangling power `8/25`, and typicality `4/15`, yet their entropy memories differ at every fixed positive order except two. This is the preferable main illustration if the covariance theorem is developed further.

## Option 2: One-step entropy memory does not compose

Let `Uφ=SWAP exp(−iφZZ)`. All `Uφ` have identical normalized operator Schmidt spectra, so their one-step equilibrium entropy covariance families coincide. But

\[
U_\phi^2=e^{-2i\phi ZZ},\qquad
M_2(U_\phi^2)=\cos^4(2\phi)+\sin^4(2\phi).
\]

At `φ=0`, all entropies recur at two steps. At `φ=π/8`, the limiting two-step Rényi-2 correlation is `1/2`. The same one-step entropy-memory data therefore permit distinct later memories.

More generally, Haar invariance reduces the covariance between states `U_iψ` and `U_jψ` to the operator Schmidt spectrum of `U_i U_j†`. Individual gate spectra do not determine relative-gate spectra. A putative Markov closure using only single-time entropies consequently loses coherent information.

**Bounded discriminator:** exhibit the above exact three-time covariance matrices and test any proposed scalar Markov closure algebraically. This requires no new state evolution simulation.

**Assessment:** useful conceptual guardrail and possible secondary figure, but the elementary echo mechanism is unlikely to be a new main result. Statements about a full Gaussian process would require a joint fluctuation theorem; pairwise covariance alone does not establish Gaussianity or conditional independence. Avoid making such claims by extrapolation.

## Option 3: What initial randomness is actually needed?

For purities, the before/after covariance depends only on the fourth projective moment of the initial-state ensemble. Therefore any exact complex projective 4-design reproduces the Haar purity identity, including with a fixed gate inserted. Invariance of the entire finite ensemble is unnecessary because its relevant moments remain design moments under a fixed unitary.

This creates a clean distinction between purity results and the nonpolynomial entropy family. The latter does not automatically follow from a fixed finite design order. A stabilizer ensemble is especially instructive: Clifford orbits reproduce lower Haar moments but are not generically 4-designs, and stabilizer entanglement spectra are flat on their support. Their Rényi entropies at different orders coincide state by state. Calling Page-like mean entanglement sufficient for the full covariance law would therefore be unjustified.

**Bounded discriminator:** contract the known extra Clifford fourth-moment invariant against the two-cut purity observable. Determine whether it survives in the sum mode or cancels. The cancellation question is sharper than another random-circuit survey and could identify a weaker sufficient preparation ensemble.

**Assessment:** a credible reserve direction if a simple cancellation appears, but likely to become a technical design/magic project if it does not. Do not launch a doping or thermalization campaign now. The role of 4-designs in polynomial observables is standard, not itself novel.

## Primary-source check

The focused check used the following primary works. These checks narrow the novelty claims; they do not establish priority exhaustively.

| Primary source | Relevant result | Consequence for this project |
|---|---|---|
| Zanardi, *Entanglement of Quantum Evolutions*, PRA 63, 040304 (2001), arXiv:quant-ph/0010074v3, Eq. 12 | Entangling power combines operator entanglements of `U` and `US` | The two-cut sum formula must credit the established identity |
| Styliaris–Anand–Zanardi, *Information Scrambling over Bipartitions*, PRL 126, 030601 (2021), arXiv:2007.08570v3, Theorems 1–2 | Bipartite OTOC equals operator entanglement and obeys the same entangling-power combination | A second-moment scrambling interpretation alone is insufficient novelty |
| Andreadakis–Dallas–Zanardi, *Operator Space Entangling Power...*, PRA 110, 052416 (2024), arXiv:2406.10206v2, Section III | Explicit treatment of SWAP transport versus generation; pair `E(U),E(US)` | Do not claim the conceptual transport/generation distinction as new |
| Bouland–Giurgica-Tiron–Wright, *The state hidden subgroup problem...*, arXiv:2410.12706v1, Appendix A.2, Fact A.1, Eq. 66 | Exact static Haar covariance of purities across arbitrary cuts | A static entanglement landscape from purity covariance is already covered |
| Zhu–Kueng–Grassl–Gross, *The Clifford group fails gracefully to be a unitary 4-design*, arXiv:1609.08172 | Explicit extra fourth-moment invariant; projective design constructions | Provides the exact object for the reserve ensemble discriminator |

URLs:

- https://arxiv.org/html/quant-ph/0010074v3
- https://arxiv.org/html/2007.08570v3
- https://arxiv.org/html/2406.10206v2
- https://arxiv.org/pdf/2410.12706
- https://arxiv.org/abs/1609.08172

The first four were inspected beyond their abstracts. The fifth abstract was inspected for the reserve direction; no claim here assumes an unverified detailed formula from it.

## Immediate decision

Proceed with the exact two-cut purity audit and the all-order two-cut corollary. Retain the composition example as a small consequence. Leave the initial-ensemble question as a possible next discriminator. This preserves scope flexibility while asking a physically sharper question than adding samples or extending the same theorem mechanically.

Subsequent refinement: verify the matched second-moment gate pair as the more demanding discriminator. You–Gu's all-replica feature formalism (arXiv:1803.10425v2, Eq. 4 and Appendix A.1) and Suzuki et al.'s exact second-moment parametrization (arXiv:2410.24127v2, Section S3.2) mean that the two-cut purity relation alone should not carry the novelty claim. These two primary papers were inspected after the initial five-source check.

## Further parent-workspace refinement: exact 2-design gate ensembles

The parent workspace found an even cleaner second-moment comparison on active qubits. For Cartan gates `U=exp[−i Σ_j c_j σ_j⊗σ_j]`, set `u_j=cos²(2c_j)` with `Σu_j=3/2` and `Σ_{i<j}u_i u_j=3/5`. Then both operator purities `F₂(U)` and `F₂(PU)` equal `2/5`, their active unnormalized entangling power is `1/5`, and gate typicality is `1/2`. The independently locally Haar-dressed gate ensembles therefore match the Haar unitary second moment exactly by the Suzuki et al. criterion.

Two choices given by the parent workspace are

\[
u_A=(\tfrac12+\sqrt{3/20},\tfrac12,\tfrac12-\sqrt{3/20}),
\]
\[
u_B=(\tfrac12+\sqrt{1/20},\tfrac12+\sqrt{1/20},\tfrac12-2\sqrt{1/20}).
\]

Their third operator moments differ by `3√5/800`. Because local dressing preserves operator Schmidt probabilities, ensemble averaging does not remove the entropy-memory distinction. This is a direct boundary of what exact gate 2-design randomness guarantees.

Quantitative caution is important. The α=3 influence function has `c₂=−6/5`, `c₃=−1/5`, hence the normalized Rényi-3 memory is

\[
M_3(U)=\frac{24}{25}F_2(U)+\frac1{25}F_3(U).
\]

The proposed pair consequently differs by only `3√5/20000 ≈ 0.0003354` in this correlation. It is an exact mathematical separation, but a small numerical effect at that order. The incompleteness of a 2-design for higher-order observables is well known. The proposed new physical content remains the quantitative law for actual entropy fluctuations, rather than an unexpected failure of design theory.

This qubit pair is the preferred clean example if its audit passes. No extra simulation is justified merely to resolve this tiny third-order difference.
