# Two subsystem assignments and their fluctuation modes

Exchanging the active factors between two balanced halves gives a second entropy observable. Together, the two observables distinguish gates that have identical entropy covariance across the original cut. The result is a corollary of the [fixed-support covariance theorem](THEOREM.md), with an additional exact calibration for purity at finite dimension.

## Setup

Write the first cut as $`A=aR`$, $`B=bT`$, with

```math
\dim a=\dim b=q>1,\qquad
\dim R=\dim T=n,\qquad d=qn.
```

A fixed gate $`U`$ acts only on $`ab`$, and the initial full-system state is complex Haar. Let $`P`$ swap the active factors. The second assignment is $`C=bR`$, with complement $`aT`$. It need not be a contiguous spatial cut. For every state and at every finite dimension,

```math
S_{\alpha,C}(\psi)=S_{\alpha,A}(P\psi).
```

Both entropies have the same Haar mean $`\mu_{\alpha,d}`$. Define $`\delta S_{\alpha,J}=S_{\alpha,J}-\mu_{\alpha,d}`$. Since $`U\psi`$ is again Haar, the after-gate pair has the same marginal joint distribution as the before-gate pair. The temporal covariance compares these pairs obtained from the same input.

## The covariance matrix

Use the theorem's kernel and entropy coefficients:

```math
K_{\alpha\beta}(V)
=\frac14\sum_{k\ge2}k c_{\alpha,k}c_{\beta,k}F_k(V),
\qquad F_k(V)=\sum_h\eta_h(V)^k.
```

The operator probabilities are those of the fixed active gate. The active dimension, gates and each positive entropy order stay fixed as $`n\to\infty`$. Put

```math
\mathbf Z_\alpha(\psi)=
\begin{pmatrix}\delta S_{\alpha,A}(\psi)\\
\delta S_{\alpha,C}(\psi)\end{pmatrix}.
```

With rows indexing the after-gate observable and columns indexing the before-gate observable,

```math
\lim_{n\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits
\left(\mathbf Z_\alpha(U\psi),\mathbf Z_\beta(\psi)\right)
=\begin{pmatrix}
K_{\alpha\beta}(U)&K_{\alpha\beta}(PU)\\
K_{\alpha\beta}(PU)&K_{\alpha\beta}(U)
\end{pmatrix}.
```

The four entries follow directly from the theorem:

1. The first diagonal entry uses $`U`$.
2. The lower-left entry uses $`PU`$ because the output entropy is on $`C`$.
3. In the upper-right entry substitute $`\chi=P\psi`$; the relative gate is $`UP`$.
4. The same substitution in the second diagonal entry gives $`PUP`$.

Exchanging equal active factors leaves the operator Schmidt probabilities unchanged, so $`\eta(PVP)=\eta(V)`$. Consequently $`\eta(UP)=\eta(PU)`$ and $`\eta(PUP)=\eta(U)`$, establishing the displayed matrix. No independent-Schmidt-basis assumption enters.

The before-before matrix is obtained by setting $`U=I`$. Active SWAP has $`q^2`$ equal operator probabilities, giving

```math
K_{\alpha\beta}(P)
=\frac14\sum_{k\ge2}k c_{\alpha,k}c_{\beta,k}q^{2(1-k)}.
```

## Sum and difference modes

Define

```math
X_{\alpha,+}=\delta S_{\alpha,A}+\delta S_{\alpha,C},
\qquad
X_{\alpha,-}=\delta S_{\alpha,A}-\delta S_{\alpha,C}.
```

The limiting covariance matrices are diagonal in this basis, both at one time and between the before/after observations. The mode correlations are

```math
M_{\alpha,\pm}(U)
=\frac{K_{\alpha\alpha}(U)\pm K_{\alpha\alpha}(PU)}
{K_{\alpha\alpha}(I)\pm K_{\alpha\alpha}(P)}.
```

The denominators are strictly positive for fixed $`q>1`$ in the growing-spectator limit. If $`n=1`$, the two subsystems are complementary halves of a pure state. Their entropies then coincide, the difference mode is identically zero and its correlation is undefined.

A bare active SWAP exchanges the two entropy values state by state. It preserves their sum and reverses their difference. Thus its mode correlations are exactly $`+1`$ and $`-1`$ at finite dimension whenever the corresponding variance is nonzero. Conservation of the sum does not imply conservation of the entropy assigned to each cut.

## Rényi-2 and active entangling power

At order two, $`K_{22}(V)=F_2(V)/2`$, so

```math
M_{2,\pm}(U)=\frac{F_2(U)\pm F_2(PU)}{1\pm q^{-2}}.
```

The active product-input linear-entropy entangling power is

```math
e_p^{(q)}(U)=\mathbb E_{a,b}
\left[1-\mathop{\mathrm{Tr}}\nolimits
\rho_a\left(U|ab\rangle\right)^2\right],
```

where the two input vectors are independently Haar-distributed on the active factors. This is the unnormalized average linear entropy. It differs from averaging over product inputs on the full halves, as explained in [Exact finite-dimensional purity covariance](FINITE_PURITY.md).

The established entangling-power identity is

```math
e_p^{(q)}(U)=\left(\frac q{q+1}\right)^2
\left[1+q^{-2}-F_2(U)-F_2(PU)\right].
```

Therefore

```math
M_{2,+}(U)=1-\frac{(q+1)^2}{q^2+1}e_p^{(q)}(U),
```

```math
\lim_{n\to\infty}d^2\mathbb E
\left[(X_{2,+}(U\psi)-X_{2,+}(\psi))^2\right]
=2\left(\frac{q+1}{q}\right)^2e_p^{(q)}(U).
```

The second equation follows from equal before/after variances and the first equation. It connects an entropy fluctuation of globally Haar inputs with entangling power on active product inputs.

For the difference mode, define the established gate typicality in this normalization by

```math
g_t(U)=\frac12\left[1-
\frac{F_2(U)-F_2(PU)}{1-q^{-2}}\right].
```

Then $`M_{2,-}(U)=1-2g_t(U)`$. These modes realize two known gate invariants as fluctuation observables. At other entropy orders the formulas involve both complete operator spectra; no equality with the corresponding average Rényi entangling power is asserted.

## Phase-SWAP example

For active qubits let

```math
U_\phi=P e^{-i\phi Z\otimes Z},\qquad 0\le\phi\le\pi/4.
```

Every member has the same flat operator spectrum $`(1/4,1/4,1/4,1/4)`$. Their complete limiting same-cut covariance families therefore coincide. However,

```math
PU_\phi=e^{-i\phi Z\otimes Z},\qquad
\eta(PU_\phi)=(\cos^2\phi,\sin^2\phi).
```

Normalize same-cut and crossed-cut covariances by the common single-cut variance. At order two,

```math
\begin{aligned}
M_{2,\mathrm{same}}&=1/4,\\
M_{2,\mathrm{cross}}&=1-\tfrac12\sin^2(2\phi),\\
e_p^{(2)}(U_\phi)&=\tfrac29\sin^2(2\phi),\\
M_{2,+}(U_\phi)&=1-\tfrac25\sin^2(2\phi),\\
M_{2,-}(U_\phi)&=-1+\tfrac23\sin^2(2\phi).
\end{aligned}
```

| Gate | Same cut | Crossed cut | Sum mode | Difference mode | Active entangling power |
|---|---:|---:|---:|---:|---:|
| SWAP | $`1/4`$ | $`1`$ | $`1`$ | $`-1`$ | $`0`$ |
| $`P e^{-i\pi ZZ/8}`$ | $`1/4`$ | $`3/4`$ | $`4/5`$ | $`-2/3`$ | $`1/9`$ |
| $`P e^{-i\pi ZZ/4}`$ | $`1/4`$ | $`1/2`$ | $`3/5`$ | $`-1/3`$ | $`2/9`$ |

Entropy correlations in the table are limits, apart from the statewise SWAP mode identities when defined. Each entangling-power value is an exact active-gate property.

## Exact finite-dimensional purity modes

Now use the purities $`P_A=\mathop{\mathrm{Tr}}\nolimits\rho_A^2`$ and $`P_C=\mathop{\mathrm{Tr}}\nolimits\rho_C^2`$, rather than their logarithms. Let

```math
a=F_2(U),\quad b=F_2(PU),\quad D=d^2,\quad
L=\frac{D(D+1)}{(D-1)^2},\quad
B_0=\frac{4D}{(D-1)^2},\quad \lambda=\frac{q^2}{D}.
```

The [global purity identity](FINITE_PURITY.md), together with the spectator factorization of the swapped invariant, gives exact correlations normalized by the common single-cut purity variance:

```math
\rho_{\mathrm{same}}=L(a+\lambda b)-B_0,
\qquad
\rho_{\mathrm{cross}}=L(b+\lambda a)-B_0.
```

The same-time correlation of the two purities is

```math
\rho_0=L(q^{-2}+\lambda)-B_0.
```

The temporal matrix has equal diagonal entries and equal off-diagonal entries. Hence for $`Y_\pm=P_A\pm P_C`$,

```math
\rho_{P,+}=\frac{\rho_{\mathrm{same}}+\rho_{\mathrm{cross}}}{1+\rho_0},
\qquad
\rho_{P,-}=\frac{\rho_{\mathrm{same}}-\rho_{\mathrm{cross}}}{1-\rho_0}.
```

Substituting the entangling-power identity and simplifying yields

```math
\rho_{P,+}=1-\mathcal K(q,d)e_p^{(q)}(U),
```

```math
\mathcal K(q,d)=
\frac{(q+1)^2(D+1)(D+q^2)}
{(q^2+1)D^2+(q^4+1-6q^2)D+q^2+q^4}.
```

For nontrivial spectators, $`n>1`$, the difference simplifies exactly to

```math
\rho_{P,-}=\frac{a-b}{1-q^{-2}}=1-2g_t(U).
```

The factor $`1-\lambda`$ cancels between its numerator and denominator, explaining the spectator-size independence. At $`n=1`$, both are zero because $`Y_-`$ vanishes, so the difference correlation is undefined. The sum formula remains valid there.

For qubits, $`\mathcal K=9(D+1)(D+4)/(5D^2-7D+20)`$. At fixed $`q`$, it tends to $`(q+1)^2/(q^2+1)`$, agreeing with the entropy-mode limit. This agreement does not turn the finite-dimensional purity equations into exact entropy equations.

## Equal second moments can still conceal different entropy covariances

The [two-pair diagonal-gate witness](../docs/WORKED_EXAMPLE.md#same-operator-purity-different-higher-order-covariance) has active dimension four on each side. Its gate spectra are

```math
\eta_A=(1/2,1/2),\qquad
\eta_C=(p^2,p(1-p),p(1-p),(1-p)^2),
\qquad p=\frac{1+\sqrt{\sqrt2-1}}2.
```

Both have $`F_2=1/2`$. Multiplying either diagonal gate by active SWAP gives sixteen uniform operator probabilities, so both crossed purities are $`1/16`$. Thus both gates have $`e_p^{(4)}=8/25`$ and $`g_t=4/15`$, and their standard second-moment transfer operators agree after independent local Haar dressing.

Nevertheless, strict convexity gives $`F_k(U_C)>F_k(U_A)`$ at every integer $`k>2`$. The nonnegative same-order covariance weights, with a nonzero coefficient above mode two at every fixed positive order except two, imply a strictly larger same-cut covariance for $`U_C`$ at each such order. Their crossed spectra remain equal at every order, so their sum- and difference-mode correlations also differ. The worked example supplies the exact gate definitions and proof. [Gate designs](GATE_DESIGNS.md) give a further explicit comparison of two exact unitary 2-designs on active qubits.

These examples concern information absent from ordinary second moments. Higher-replica entanglement features already contain the corresponding higher invariants.

## Attribution, scope and verification

Zanardi's [*Entanglement of Quantum Evolutions*](https://arxiv.org/abs/quant-ph/0010074v3), Eq. 12, supplies the entangling-power relation. Gate typicality and its complementary role are established in Jonnadula et al., [*Entanglement measures of bipartite quantum gates and their thermalization under arbitrary interaction strength*](https://arxiv.org/abs/1909.08139v2), Eq. 18. Their normalized entangling power includes an extra factor $`(q+1)/(q-1)`$ relative to the average linear entropy used here.

Replicated temporal permutation correlations and their invariant families appear in You and Gu, [*Entanglement Features of Random Hamiltonian Dynamics*](https://arxiv.org/abs/1803.10425v2), Eq. 4 and Appendix A.1. The dependence of locally dressed second moments on entangling power and gate typicality is described in Suzuki et al., [*More global randomness from less-random local gates*](https://arxiv.org/abs/2410.24127v3), Section III.2. Static Haar covariances between subsystems are also antecedents, including Bouland, Giurgica-Tiron and Wright, [*The state hidden subgroup problem and an efficient algorithm for locating unentanglement*](https://arxiv.org/abs/2410.12706v1), Appendix A.2. See [References](../docs/REFERENCES.md) for the main theorem's attribution.

The entropy derivation assumes fixed active support and increasing spectators, as specified in [the theorem](THEOREM.md) and [proof](PROOF.md). Operations local to the original halves can cross the exchanged assignment; enlarging allowed support changes the interpretation. These identities provide no generic many-body separation of transport and generation and no experimental sample-complexity improvement.

The [full-system contraction check](../checks/finite_purity/check_two_cut_modes.py) covers fourteen active-gate/spectator cases, including the undefined difference mode without spectators. [Exact symbolic identities](../checks/symbolic/two_cut_symbolic_audit.py) verify centering, variance and mode reductions. A [separate product-input contraction](../checks/numerics/two_cut_check.py) tests both operator invariants and the entangling-power normalization. The [reproduction guide](../REPRODUCE.md) explains how these checks run without state sampling.
