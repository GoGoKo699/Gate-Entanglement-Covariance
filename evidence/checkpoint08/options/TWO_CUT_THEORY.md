# Two balanced cuts reveal what one-cut memory discards

Working derivation, 2026-09-12. This note assumes the checkpoint-07 covariance theorem. Its new statements are corollaries and reinterpretations of that theorem, not a new proof of the underlying fluctuation law. Final checkpoint status: the exact finite-purity formula in section 6 passed independent review, eight exact polynomial identities, and two separately implemented Haar-moment calculations. See `../reviews/TWO_CUT_INDEPENDENT_AUDIT.md` and `../finite_purity/EXACT_GLOBAL_PURITY.md`.

## 1. Setup and the two observables

Write the total space as `A0 ⊗ a ⊗ b ⊗ B0`, with equal active dimensions `dim a = dim b = q`, equal spectator dimensions `dim A0 = dim B0 = s`, and `d = qs`. The state is globally Haar random. A fixed gate `U` acts only on `a ⊗ b`.

Define two balanced subsystems

\[
A=A_0a,\qquad C=A_0b.
\]

They exchange the assignment of the two active factors. In a spatial chain the second subsystem need not be contiguous; this is an exchange of boundary assignments, not a claim about two ordinary contiguous cuts. Let `P = SWAP_ab`. For every state, at every finite dimension,

\[
S_{\alpha,C}(\psi)=S_{\alpha,A}(P\psi).
\]

Both entropies have the same Haar mean `μ_{α,d}`. Define centered fluctuations `δS_{α,J}=S_{α,J}−μ_{α,d}`. Since `Uψ` remains Haar, the joint distribution of the after-gate pair `(S_A,S_C)` is exactly the same as that of the before-gate pair.

## 2. The full two-cut covariance matrix

Use the checkpoint-07 notation

\[
\kappa_{\alpha\beta}(V)
=\frac14\sum_{k\ge2} k c_{\alpha k}c_{\beta k}
\sum_j\eta_j(V)^k,
\]

where `η(V)` are the normalized operator Schmidt probabilities of the fixed active gate, and the coefficients `c_{αk}` are those of the entropy influence function in checkpoint 07. Every positive Rényi order is fixed before `s→∞`.

With row indexing the after-gate cut and column indexing the before-gate cut,

\[
\lim_{s\to\infty}d^2
\operatorname{Cov}
\begin{pmatrix}\delta S_{\alpha,A}(U\psi)\\\delta S_{\alpha,C}(U\psi)\end{pmatrix},
\begin{pmatrix}\delta S_{\beta,A}(\psi)\\\delta S_{\beta,C}(\psi)\end{pmatrix}
=
\begin{pmatrix}
\kappa_{\alpha\beta}(U)&\kappa_{\alpha\beta}(PU)\\
\kappa_{\alpha\beta}(PU)&\kappa_{\alpha\beta}(U)
\end{pmatrix}.
\]

Here and below covariance between column vectors means the matrix of pairwise covariances. A literal derivation avoids assumptions about independent Schmidt bases:

1. The `A,A` entry is the existing theorem for `U`.
2. The `C,A` entry is that theorem for `PU`.
3. In the `A,C` entry substitute the Haar variable `χ=Pψ`; this gives `UP`.
4. In the `C,C` entry the same substitution gives `PUP`.

The operator Schmidt probabilities of `PVP` equal those of `V`, because the two tensor factors have simply exchanged roles. Thus `η(UP)=η(PU)` and `η(PUP)=η(U)`. This proves the matrix.

The before-before covariance matrix is the same expression with `U=I`. Since `P` has `q²` uniform operator Schmidt probabilities,

\[
\kappa_{\alpha\beta}(P)
=\frac14\sum_{k\ge2}k c_{\alpha k}c_{\beta k}q^{2(1-k)}.
\]

## 3. Sum and difference modes

For a fixed order define

\[
X_{\alpha,+}=\delta S_{\alpha,A}+\delta S_{\alpha,C},\qquad
X_{\alpha,-}=\delta S_{\alpha,A}-\delta S_{\alpha,C}.
\]

The sum and difference modes have zero mutual covariance both before the gate and between before/after times. Their own limiting correlations are

\[
M_{\alpha,\pm}(U)
=\frac{\kappa_{\alpha\alpha}(U)\pm\kappa_{\alpha\alpha}(PU)}
{\kappa_{\alpha\alpha}(I)\pm\kappa_{\alpha\alpha}(P)}.
\]

These denominators are strictly positive in the fixed-`q>1`, large-spectator limit. The no-spectator case is different: `A` and `C` are complementary subsystems of a bipartite pure state, so their entropies coincide and the difference mode is identically zero.

For any fixed order, a SWAP gate exchanges the two cut entropies for each individual input state. Consequently `X_+` is unchanged and `X_-` changes sign. The correlations `+1` and `−1` are exact at finite dimensions whenever the mode has nonzero variance. This is a concrete distinction between preserving the sum of two entanglement observables and preserving their spatial assignment.

## 4. Rényi-2 gives active entangling power

Let

\[
\mathcal P_{\rm op}(V)=\sum_j\eta_j(V)^2.
\]

For Rényi-2, `κ_{22}(V)=𝒫_op(V)/2`, so

\[
M_{2,\pm}(U)
=\frac{\mathcal P_{\rm op}(U)\pm\mathcal P_{\rm op}(PU)}{1\pm q^{-2}}.
\]

The active gate's linear-entropy entangling power is the established quantity

\[
e_{p,a:b}(U)=\mathbb E_{|a\rangle,|b\rangle}
\left[1-\operatorname{Tr}\rho_a(U|ab\rangle)^2\right],
\]

with independent Haar pure states on the two `q`-dimensional active factors. It is not the entangling power averaged over product inputs on the two full `d`-dimensional halves.

Zanardi's identity (2001, Eq. 12) gives

\[
e_{p,a:b}(U)
=\left(\frac q{q+1}\right)^2
\left[1+q^{-2}-\mathcal P_{\rm op}(U)-\mathcal P_{\rm op}(PU)\right].
\]

The resulting fluctuation relation is

\[
\boxed{M_{2,+}(U)=1-\frac{(q+1)^2}{q^2+1}e_{p,a:b}(U).}
\]

Equivalently, stationary variance gives

\[
\lim_{s\to\infty}d^2\mathbb E\bigl[(X_{2,+}(U\psi)-X_{2,+}(\psi))^2\bigr]
=2\left(\frac{q+1}{q}\right)^2 e_{p,a:b}(U).
\]

Thus the fluctuation of the sum over these two cuts probes the product-input entangling power of the active gate, even though the initial global states are already highly entangled and their mean cut entropies do not change. The new candidate content is this relation between equilibrium entropy fluctuations and active entangling power. The entangling-power identity, the difference between operator entanglement and entangling power, and the interpretation of SWAP as transport are prior work.

For other Rényi orders the two-cut matrix gives a full pair of operator spectra, not an equality with the average corresponding Rényi entangling power. No such equality is asserted.

The difference mode is also a familiar gate invariant: with the standard gate typicality

\[
g(U)=\frac{E(U)-E(UP)+E(P)}{2E(P)},
\]

one has `M_{2,−}=1−2g(U)`. Thus neither leading mode creates a new invariant. They give fluctuation-observable realizations of two established invariants.

## 5. The phase-SWAP family

For active qubits, set

\[
U_\phi=P e^{-i\phi Z\otimes Z},\qquad 0\le\phi\le\pi/4.
\]

Every `Uφ` is dual unitary, with operator Schmidt probabilities `(1/4,1/4,1/4,1/4)`. Consequently their complete same-cut entropy covariance families are identical. On the crossed cut,

\[
PU_\phi=e^{-i\phi ZZ},\qquad
\eta(PU_\phi)=(\cos^2\phi,\sin^2\phi).
\]

Hence

\[
\begin{aligned}
M_{2,\rm same}&=1/4,\\
M_{2,\rm cross}&=1-\tfrac12\sin^2(2\phi),\\
e_{p,a:b}(U_\phi)&=\tfrac29\sin^2(2\phi),\\
M_{2,+}(U_\phi)&=1-\tfrac25\sin^2(2\phi),\\
M_{2,-}(U_\phi)&=-1+\tfrac23\sin^2(2\phi).
\end{aligned}
\]

| Gate | Same-cut memory | Crossed-cut memory | Sum-mode memory | Difference-mode memory | Active linear entangling power |
|---|---:|---:|---:|---:|---:|
| SWAP | 1/4 | 1 | 1 | −1 | 0 |
| SWAP exp(−iπZZ/8) | 1/4 | 3/4 | 4/5 | −2/3 | 1/9 |
| SWAP exp(−iπZZ/4) | 1/4 | 1/2 | 3/5 | −1/3 | 2/9 |

All tabulated entropy memories are limiting correlations except the SWAP mode values, which hold at finite dimension when defined. In contrast, each entangling power is an exact active-gate property.

## 6. Independently reviewed exact finite-purity extension

The exact formula for the sum of the two *purities*, `Y_+=Tr ρ_A²+Tr ρ_C²`, is as follows. With `D=d²`,

\[
\operatorname{Corr}[Y_+(U\psi),Y_+(\psi)]
=1-K(q,d)e_{p,a:b}(U),
\]

\[
K(q,d)=\frac{(q+1)^2(D+1)(D+q^2)}{(q^2+1)D^2+(q^4+1-6q^2)D+q^2+q^4}.
\]

For active qubits, `K=9(D+1)(D+4)/(5D²−7D+20)→9/5`. This formula is separate from the asymptotic entropy theorem. The factor at `s=1` correctly reduces to the full bipartite-purity relation, but the difference mode then vanishes. Independent validation is recorded in the reviews named at the top of this note. For nontrivial spectators the purity difference has the exact, spectator-size-independent correlation `1−2g(U)`.

## 7. Scope and a decisive bounded check

The derivation assumes fixed active dimensions, gates confined to those factors, a balanced globally Haar state, and growing equal spectators. It is not a universal separation of transport and generation for arbitrary many-body dynamics. Gates acting within a full half can still cross the exchanged cut `C`, so enlarging the allowed support changes the interpretation.

No experimental sample-complexity improvement follows. The unrescaled entropy fluctuations still shrink with size. The significance is an identity linking distinct state preparations and a limitation of one-cut diagnostics.

A sufficient next check is algebraic: verify the exact four-copy purity relation for a handful of deterministic gates, including SWAP, phase-SWAP, a controlled gate, and a generic two-qudit gate. The existing saved state arrays may illustrate the entropy limit, but a larger Haar simulation is unnecessary for deciding whether the identity is correct. The scientific judgment should remain whether this observable makes the full-spectrum theorem physically useful beyond repackaging known operator invariants.

## Primary sources and overlap

- P. Zanardi, *Entanglement of Quantum Evolutions*, Phys. Rev. A 63, 040304 (2001), arXiv:quant-ph/0010074v3, Eq. 12: https://arxiv.org/html/quant-ph/0010074v3 . Source of the entangling-power identity, operator Schmidt normalization, and SWAP caveat.
- G. Styliaris, N. Anand, P. Zanardi, *Information Scrambling over Bipartitions*, Phys. Rev. Lett. 126, 030601 (2021), arXiv:2007.08570v3, Theorems 1–2: https://arxiv.org/html/2007.08570v3 . Operator purity is already tied to a bipartite OTOC, with the same entangling-power combination.
- F. Andreadakis, E. Dallas, P. Zanardi, *Operator Space Entangling Power of Quantum Dynamics and Local Operator Entanglement Growth in Dual-Unitary Circuits*, Phys. Rev. A 110, 052416 (2024), arXiv:2406.10206v2, Section III, especially Eq. 20: https://arxiv.org/html/2406.10206v2 . Explicitly distinguishes transport by SWAP from generation and discusses the pair `E(U),E(US)`.
- A. Bouland, T. Giurgica-Tiron, J. Wright, *The state hidden subgroup problem and an efficient algorithm for locating unentanglement*, arXiv:2410.12706v1, Appendix A.2, Fact A.1, Eq. 66: https://arxiv.org/pdf/2410.12706 . Exact static Haar purity covariance over arbitrary cuts is prior work; a static cut-covariance claim is not a novelty target.

## 8. Further novelty check and a stronger comparison

Two additional primary sources constrain the interpretation substantially:

- Y.-Z. You and Y. Gu, *Entanglement Features of Random Hamiltonian Dynamics*, Phys. Rev. B 98, 014309 (2018), arXiv:1803.10425v2, Eq. 4 and Appendix A.1: https://arxiv.org/html/1803.10425v2 . The integer-replica features `Tr(U^⊗n Xσ U†⊗n Xτ)` are already organized as temporal correlations of replicated permutations. Appendix A.1 explicitly identifies two independent nontrivial cyclic feature families for two-qudit gates. Those are the two operator-spectrum families entering this note.
- R. Suzuki et al., *More global randomness from less random local gates*, arXiv:2410.24127v2, Section S3.2: https://arxiv.org/html/2410.24127v2 . The second-moment operator of locally dressed fixed-gate circuits depends only on entangling power and gate typicality. Their entangling power is normalized by `(q+1)/(q−1)` relative to the unnormalized average linear entropy used here.

Accordingly, the sum/difference purity formulas should be treated as a calibration and physical interpretation, not the main novelty claim. A stronger illustration is an exact pair of gates with identical full ordinary second-moment transfer data but different entropy fluctuation memories.

Let each active factor comprise two qubits (`q=4`), and define

\[
U_A=e^{-i\pi Z_{a_1}Z_{b_1}/4},\qquad
U_B=e^{-i\theta(Z_{a_1}Z_{b_1}+Z_{a_2}Z_{b_2})},
\]

where

\[
x=\cos^2\theta=\frac{1+\sqrt{\sqrt2-1}}2.
\]

Their nonzero operator Schmidt probabilities are respectively

\[
\eta_A=(1/2,1/2),\qquad
\eta_B=(x^2,x(1-x),x(1-x),(1-x)^2).
\]

Both have `𝒫_op=1/2`. Because both gates are diagonal, `PU_A` and `PU_B` have uniform operator Schmidt probabilities on rank 16, so both crossed purities equal `1/16`. Therefore they share

\[
e_{p,a:b}=8/25,\qquad g=4/15,
\]

and have the same standard second-moment transfer operator after independent local Haar dressing. In Suzuki et al.'s convention their entangling power is `e_u=8/15`.

Yet for every integer `k>2`,

\[
\sum_j\eta_{B,j}^k>2^{1-k}=\sum_j\eta_{A,j}^k.
\]

One short proof uses Jensen under the probability measure with weights `η_j`: `Ση_j^k = E_η[η^{k−1}] ≥ (E_ηη)^{k−1} = (Ση_j²)^{k−1}`, with strict inequality for the nonuniform positive spectrum `η_B`. The flat rank-two spectrum saturates the inequality.

The self-covariance kernel weights each moment by the nonnegative coefficient `k c_{αk}²/4`. For every fixed positive order other than two its entropy influence function has at least one nonzero coefficient above degree two. Consequently the one-cut self-memory of `U_B` strictly exceeds that of `U_A` for every such order. Their crossed-cut kernels remain equal at every order, so both their sum- and difference-mode memories also differ. Rényi-2 is the exact exception.

This illustrates a concrete limitation of ordinary second-moment transfer descriptions. It does not reveal a limitation of the full higher-replica entanglement-feature formalism, which already contains the necessary invariants. The candidate contribution is their closed resummation into actual fixed-positive-order entropy covariances in the balanced-Haar, large-spectator regime.
