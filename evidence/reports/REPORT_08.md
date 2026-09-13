# What equilibrium entanglement memory distinguishes

Entanglement Temporal Fluctuations, checkpoint 08. 12 September 2026.

## Research decision

This checkpoint improves the physical interpretation of the covariance law, but it also sharpens its novelty problem. There is a compact relation between entanglement fluctuations across two exchanged subsystem assignments and a gate's established entangling power. There is also an explicit pair of exact gate 2-designs that have identical second moments yet different entropy memories. Both are useful consequences. Neither alone establishes the kind of new physical principle sought for a PRL.

The strongest current candidate remains the closed covariance formula for actual entropies at every fixed positive Rényi order, under balanced-Haar and fixed-boundary assumptions. The replica invariants entering it, the distinction between SWAP and entanglement generation, and second-moment gate classifications are established antecedents. The research should now test physical reach rather than accumulate further algebraic examples. No repository is needed at this stage.

## 1. Setting and the inherited law

Start from a complex Haar random pure state on two equal halves of dimension `d`. A deterministic unitary `U` acts only on one active factor of dimension `q≥2` in each half. Each half also has a spectator of dimension `n≥1`, with `d=qn`. The limit holds `q` and `U` fixed while `n` grows. Use natural-log entropies

\[
S_\alpha(\rho)=\frac{\log\operatorname{Tr}\rho^\alpha}{1-\alpha},
\]

with the continuous von Neumann limit at order one. Order one half is pure-state logarithmic negativity. Haar invariance makes the before- and after-gate entropy means identical. Memory here means their ensemble correlation, not a nonzero mean entropy change.

Let `η_j(U)` be the normalized operator Schmidt probabilities of the active gate and write `F_k(U)=Σ_j η_j(U)^k`. The checkpoint-07 derivation, copied into `foundation/`, gives

\[
\kappa_{\alpha\beta}(U)
=\lim_{n\to\infty}d^2\operatorname{Cov}[S_\alpha(U\psi),S_\beta(\psi)]
=\frac14\sum_{k\ge2}k c_{\alpha k}c_{\beta k}F_k(U).
\tag{1}
\]

For `α≠1`, the coefficients are fixed by

\[
c_{\alpha,2}=-\frac{2\alpha}{\alpha+2},\qquad
c_{\alpha,k+1}=c_{\alpha,k}\frac{\alpha-k}{\alpha+k+1}.
\]

At order one, `c_{1,k}=4(−1)^{k−1}/[k(k²−1)]`. Every order is fixed before the dimension limit. The theorem concerns a fixed finite collection of gates or times; it supplies no uniform finite-size bias, growing-support theorem, or state-preparation universality result. Absolute covariances vanish as `d⁻²`.

## 2. What the whole hierarchy identifies

If the operator Schmidt rank is at most `R`, the same-order integer entropy covariances at orders `2,…,R` determine the operator Schmidt spectrum. The proof in `inverse/` is triangular moment inversion followed by Newton identities. Conversely, that spectrum determines the complete covariance family (1). Thus the hierarchy is complete for this spectrum, while it does not identify the gate's operator Schmidt bases or every gate property.

This is an information statement, not an efficient reconstruction protocol. For active qubits, let `ρ_m` be the limiting order-`m` entropy correlation. Then

\[
F_2=\rho_2,\qquad
F_3=25\rho_3-24\rho_2,\qquad
F_4=441\rho_4-1200\rho_3+760\rho_2.
\tag{2}
\]

Arbitrary signed input errors bounded by `δ` can give moment errors as large as `δ`, `49δ`, and `2401δ`, respectively, before imposing consistency constraints. These are sharp linear amplification factors, not statistical lower bounds for an optimal constrained estimator. Recovering roots adds instability near degeneracies. The covariance theorem also gives no uniform finite-size bias rate. Exact arithmetic checks through rank twelve support the derivation; no tomography claim follows.

## 3. An exact relation at finite dimension

An independently derived identity clarifies the role of the input ensemble. For **any** global unitary `V` on a balanced `d×d` system, put `P(ψ)=Tr ρ_A²` and define

\[
e_p^{(d)}(V)=\mathbb E_{a,b}[1-P(V|a\rangle|b\rangle)],
\]

where the product inputs are independently Haar over the **whole** `d`-dimensional halves. Then

\[
\boxed{\operatorname{Corr}_{\psi\sim\mathrm{Haar}}[P(V\psi),P(\psi)]
=1-\frac{d^2+1}{(d-1)^2}e_p^{(d)}(V).}
\tag{3}
\]

This is exact for purity at finite `d`. It is not an exact formula for logarithmic purity or other entropies. Its proof explicitly classifies all 24 fourth-Haar-moment contractions and uses the established entangling-power identity of Zanardi, Zalka, and Faoro [1]. The denominator `(d−1)²/(d²+1)` is the mean entangling power of a Haar-distributed global gate. Greater-than-average entangling power therefore gives negative purity covariance. For example, CNOT on two qubits gives `−1/9`; an established two-qutrit perfect permutation gives `−1/4`.

This qualifies our earlier interpretation. One-cut memory can fail to distinguish the **active gate's** product-input entangling power. It is nevertheless exactly related, for purity, to product-input entangling power defined on the **whole halves**. A whole-half product state can contain active-spectator entanglement inside each half. These are different input ensembles.

For an active gate embedded with identity spectators, the two global operator purities are `F_2(U)` and `F_2(UP)/n²`, where `P` swaps the active factors. The second term disappears in the fixed-boundary limit. This explains both the one-cut limitation and why it cannot be extended to a whole-half SWAP.

## 4. Two exchanged subsystem assignments recover the missing distinction

Write the original halves as `A=aR` and `B=bT`. Compare `A` with the equal-size subsystem `C=bR`, whose complement is `aT`. This exchanges the two active factors. In a chain, `C` need not be contiguous; the result is not about two ordinary adjacent contiguous cuts.

For every state, `S_{α,C}(ψ)=S_{α,A}(Pψ)`. Therefore the limiting before/after covariance matrix, rescaled by `d²`, is

\[
\begin{pmatrix}
\kappa_{\alpha\beta}(U)&\kappa_{\alpha\beta}(PU)\\
\kappa_{\alpha\beta}(PU)&\kappa_{\alpha\beta}(U)
\end{pmatrix}.
\tag{4}
\]

The centered entropy sum and difference, `X_{α,±}=δS_{α,A}±δS_{α,C}`, diagonalize this matrix. Their limiting correlations are

\[
M_{\alpha,\pm}
=\frac{\kappa_{\alpha\alpha}(U)\pm\kappa_{\alpha\alpha}(PU)}
{\kappa_{\alpha\alpha}(I)\pm\kappa_{\alpha\alpha}(P)}.
\tag{5}
\]

Let `e_p` now denote the **active** `q×q` gate's mean unnormalized linear entropy on independent pure product inputs. Let `g_t` be its standard gate typicality. With `f=F_2(U)` and `h=F_2(PU)`, their conventions here are

\[
e_p=\frac{q^2}{(q+1)^2}(1+q^{-2}-f-h),\qquad
g_t=\frac12\left[1-\frac{f-h}{1-q^{-2}}\right].
\]

At Rényi order two, equation (5) reduces to

\[
\boxed{M_{2,+}=1-\frac{(q+1)^2}{q^2+1}e_p,\qquad
M_{2,-}=1-2g_t.}
\tag{6}
\]

The symmetric fluctuation now recovers the active entangling power. The antisymmetric fluctuation records the established difference between the two gate invariants. A bare active SWAP gives the clearest interpretation: it exchanges the two entropies state by state, preserving their sum and reversing their difference. This is an exact finite-dimensional statement at every entropy order whenever the relevant variance is nonzero.

For active qubits, `U_φ=P exp(−iφZZ)` has the same one-cut memory at every `φ`, yet the two-cut modes distinguish it:

| Active gate | Limiting one-cut order-2 correlation | Sum correlation | Difference correlation | Active `e_p` |
|---|---:|---:|---:|---:|
| SWAP | 1/4 | 1 | −1 | 0 |
| SWAP exp(−iπZZ/8) | 1/4 | 4/5 | −2/3 | 1/9 |
| SWAP exp(−iπZZ/4) | 1/4 | 3/5 | −1/3 | 2/9 |

All entropy correlations in this table use the spectator limit, except the SWAP sum/difference identities. There is no changing Haar mean and no universal separation into transport and production currents for arbitrary many-body dynamics. The result assumes the gate acts only on the two active factors.

There is also an exact finite-dimensional purity version. Set `Y_±=P_A±P_C`, `D=d²`, and

\[
H=(q^2+1)D^2+(q^4+1-6q^2)D+q^2+q^4.
\]

Then

\[
\operatorname{Corr}[Y_+(U\psi),Y_+(\psi)]
=1-\frac{(q+1)^2(D+1)(D+q^2)}{H}e_p,
\tag{7}
\]

while the purity difference correlation is exactly `1−2g_t`, independent of spectator size for `n>1`. At `n=1`, the two cuts are complementary, so their purities and entropies coincide. The difference mode vanishes and its correlation is undefined. A sum of Rényi-2 entropies is not a sum of purities; equations (6) and (7) must remain distinct.

## 5. Two exact gate 2-designs with different entropy memory

The two-cut relation depends on known second-moment invariants. To exhibit content beyond those invariants, we constructed two fixed two-qubit gates and dressed each with independent local Haar input/output rotations. Each resulting ensemble is an exact unitary 2-design on the two active qubits. In particular, their entire two-copy moment operators agree with one another and with Haar on `U(4)`.

Nevertheless their entropy memories differ under the same globally Haar initial-state ensemble:

| Limiting one-cut correlation | Ensemble A | Ensemble B |
|---|---:|---:|
| Logarithmic negativity, order 1/2 | 0.300458 | 0.297653 |
| Von Neumann, order 1 | 0.373885 | 0.372930 |
| Rényi-2 | 0.400000 | 0.400000 |
| Rényi-3 | 0.391750 | 0.391415 |

The Rényi-3 separation is exact:

\[
\rho_3(A)-\rho_3(B)=\frac{3\sqrt5}{20000}\simeq0.0003354102.
\tag{8}
\]

The noninteger rows are deterministic evaluations of the convergent covariance series, not fitted estimates or independent entropy simulations. The exact order-three result suffices for the distinction.

For reproducibility, take `U=exp[−i(c_1XX+c_2YY+c_3ZZ)]`, `u_i=cos²(2c_i)`, with

\[
u_A=(1/2+\sqrt{3/20},1/2,1/2-\sqrt{3/20}),
\]
\[
u_B=(1/2+\sqrt{1/20},1/2+\sqrt{1/20},1/2-2\sqrt{1/20}).
\]

Both give `F_2(U)=F_2(PU)=2/5`, `e_p=1/5`, and `g_t=1/2`, which supply the known local-dressing 2-design criterion [4]. The independent review also proves the criterion by the rank-two Haar moment projector. Their third moments differ by `3√5/800`, giving (8). Local input/output rotations preserve the full Haar-input before/after entropy distribution even at finite dimension. The entropy-correlation formula used to compute (8) is still asymptotic.

These are **gate** 2-designs on the active qubits. They are not global gate designs after spectators are added, and they do not replace the initial Haar state ensemble by a state 2-design. The general fact that a 2-design need not match higher-order observables is elementary. The contribution of this example is a quantified entropy-memory difference within the current formula. Its small magnitude does not justify a new Monte Carlo campaign.

## 6. Verification and reproducibility

No new global Haar-state simulations were performed. The new calculations evaluate exact moment expressions directly, with no fitted coefficients.

| Check | Scope | Result |
|---|---|---|
| Global fourth-Haar-moment classification | 14 gates, 336 permutation traces | Largest unnormalized trace difference about `1.14×10⁻¹³` |
| Independent full-system two-cut contractions | 14 active-gate/spectator cases | Largest mode-correlation difference about `1.66×10⁻¹⁴` |
| Direct contraction of the purity sum, separate implementation | 15 gates, active dimensions 2, 3, 4; five spectator sizes | 75 correlations; largest difference `1.29×10⁻¹²` |
| Separate product-input entangling-power contraction | Same 15 active gates | Largest invariant-formula difference `1.11×10⁻¹⁶` |
| Exact sparse-polynomial audit | Eight centering, variance, and mode identities | All pass |
| Exact moment inversion | Through rank 12, plus deterministic spectra | All pass |
| Full two-copy twirling superoperator | Two constructed ensembles | Frobenius differences below `3.25×10⁻¹⁶` |
| Analytical design-pair audit | Exact spectra, design criterion, order-three separation | Passed |

These are internal independent formulations and reviews, not external peer review. Floating-point evaluations of exact Haar identities do not constitute certified floating-point interval bounds. The rational checks are exact. The inherited nonpolynomial covariance theorem is supported by the earlier proofs copied into `foundation/`; checking purity identities alone does not establish it.

The fresh-directory reproduction passed all six declared programs. Five output JSON files reproduced byte for byte. Two floating-point values in the sixth differed by at most `5.73×10⁻¹⁵`; all assertions and comparisons passed. The package preserves this record. No earlier sampling campaign needs to be rerun.

## 7. Novelty and the next scientific discriminator

The literature comparison restricts the claim substantially:

- Entangling power, its two operator invariants, and its Haar mean are established [1]. Gate typicality and their joint dynamical use are also established [2].
- Entanglement features already organize integer-replica gate information and temporal correlations of replicated permutations [3]. Showing that purity omits higher-order information does not exceed that framework.
- The full second-moment operator of locally dressed fixed gates is already characterized by entangling power and gate typicality [4]. Our exact designs use that established structure.
- Static covariances of purity across different cuts have prior exact Haar-moment treatments [5]. The temporal identities must be assessed against that background.

We did not locate the exact normalized identity (3) stated in the same form during the focused review. That absence is not an originality certificate. The two-cut result is a useful physical calibration, and the design pair is a useful illustration, but neither should become an inflated headline.

The potential contribution that remains is a closed resummation from gate spectra to **actual entropy covariance at every fixed positive order**, with explicit support restrictions and a clear physical interpretation. Its PRL significance remains unresolved. Further theoretical corollaries would not resolve that uncertainty.

A better next question is whether the gate-dependent memory becomes predictive for an ordinary many-body equilibrium ensemble. The proposed bounded test uses eigenstates of one nonconserving Floquet spin chain at two tractable sizes, three fixed boundary gates, and entropy orders one half, one, and two. Compare the absolute fluctuation scale and normalized memory with the existing Haar predictions, without fitting their coefficients. Resolve any exact symmetries, retain changes in the ensemble mean under the probe gate, and treat eigenstates of one operator as a dependent cohort. Agreement of the mean entropy alone is insufficient to validate the covariance law. That experiment has not been performed in this checkpoint.

Stop this extension if useful agreement requires a broad model/size campaign or the deviations have no compact physical explanation. A modest discrepancy by itself would not establish a new equilibration scale. In that event, retain the exact law as a benchmark and reconsider the PRL direction.

The project remains open in scope. The existing mathematics and negative novelty findings are retained. No external repository is needed to continue this bounded exploration.

## Primary references

1. P. Zanardi, C. Zalka, L. Faoro, *Entangling power of quantum evolutions*, Phys. Rev. A **62**, 030301 (2000). [Primary paper](https://arxiv.org/html/quant-ph/0005031v1). Propositions 1 and 2 give the two-invariant relation and Haar mean. The project's `e_p` is unnormalized linear entropy.
2. B. Jonnadula, P. Mandayam, K. Życzkowski, A. Lakshminarayan, *Entanglement measures of bipartite quantum gates and their thermalization under arbitrary interaction strength*, Phys. Rev. Research **2**, 043126 (2020). [Primary paper](https://arxiv.org/html/1909.08139v2). Their normalized entangling power differs from ours by `(q+1)/(q−1)`; gate typicality agrees.
3. Y.-Z. You, Y. Gu, *Entanglement Features of Random Hamiltonian Dynamics*, Phys. Rev. B **98**, 014309 (2018). [Primary paper](https://arxiv.org/abs/1803.10425). Integer-replica temporal entanglement features are a close antecedent.
4. R. Suzuki et al., *More global randomness from less random local gates*, arXiv:2410.24127. [Version 2, Section S3.2](https://arxiv.org/html/2410.24127v2). Independent audit also consulted version 3, Section III.2, equation (25). This source uses normalized entangling power, equal to `3e_p` for active qubits.
5. A. Bouland, T. Giurgica-Tiron, J. Wright, *The state hidden subgroup problem and an efficient algorithm for locating unentanglement*, arXiv:2410.12706. [Primary paper](https://arxiv.org/abs/2410.12706), Appendix A.2. Static Haar purity covariances across cuts.

Additional antecedents and precise limits appear in `finite_purity/EXACT_GLOBAL_PURITY.md`, `options/PHYSICAL_OPTIONS.md`, and `options/TWO_CUT_THEORY.md`. The prior fluctuation-theorem sources, including the low-regularity LUE extension, are identified in `foundation/`.
