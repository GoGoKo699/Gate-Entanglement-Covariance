# One boundary qubit pair

This example compares three fixed two-qubit gates inside two growing halves. It evaluates the covariance theorem directly; it adds no random-state simulation.

Write

```math
A=aR,\qquad B=bT,\qquad
\dim a=\dim b=2,\qquad
\dim R=\dim T=n,\qquad d=2n.
```

For every complex-Haar input $\psi$, compare the entropy across $aR\mid bT$ before and after a gate on $ab$. Keep that gate fixed while $n$ grows. The three choices are the identity, a $ZZ$ phase gate, and SWAP of the active qubits.

## The three gate spectra

**Identity.** The gate is one product operator. Its normalized operator Schmidt spectrum is $(1)$, hence $F_k=1$. Every state's entropy is unchanged.

**The phase gate.** Since $(Z\otimes Z)^2=I$,

```math
U_{ZZ}=e^{-i\pi Z\otimes Z/4}
=\frac{I\otimes I-iZ\otimes Z}{\sqrt2}.
```

The Pauli operators are orthogonal in the Hilbert-Schmidt inner product. After normalizing the operator Schmidt coefficients, the probabilities are $(1/2,1/2)$, so $F_k=2^{1-k}$.

**The active SWAP.** Its Pauli expansion is

```math
P_{ab}=\frac12\left(I\otimes I+X\otimes X
+Y\otimes Y+Z\otimes Z\right).
```

The four normalized probabilities are $(1/4,1/4,1/4,1/4)$, so $F_k=4^{1-k}$. This is the flattest possible operator Schmidt spectrum for a two-qubit gate.

| Gate on $ab$ | Nonzero operator Schmidt probabilities | $F_k$ |
|---|---|---:|
| Identity | $(1)$ | $1$ |
| $e^{-i\pi ZZ/4}$ | $(1/2,1/2)$ | $2^{1-k}$ |
| Active SWAP | $(1/4,1/4,1/4,1/4)$ | $4^{1-k}$ |

## The simplest entropy calculation

At Rényi order two, the coefficient sequence in the [theorem](../theory/THEOREM.md) has only one nonzero term: $c_{2,2}=-1$. Consequently,

```math
\lim_{d\to\infty}d^2\operatorname{Var}[S_2(\psi)]=\frac12,
\qquad
\lim_{d\to\infty}d^2\operatorname{Cov}[S_2(U\psi),S_2(\psi)]
=\frac12F_2(U).
```

The two entropies have identical variances by Haar invariance. Their limiting correlation is therefore $F_2(U)$. Their mean-square difference is twice the variance minus twice the covariance:

```math
\lim_{d\to\infty}d^2\mathbb E
\left[(S_2(U\psi)-S_2(\psi))^2\right]=1-F_2(U).
```

| Gate | Limiting $S_2$ correlation | Limiting $d^2\mathbb E[(\Delta S_2)^2]$ |
|---|---:|---:|
| Identity | $1$ | $0$ |
| $e^{-i\pi ZZ/4}$ | $1/2$ | $1/2$ |
| Active SWAP | $1/4$ | $3/4$ |

The mean entropy change is zero for all three gates. The table describes how much the paired fluctuations change. For example, an active SWAP gives an asymptotic root-mean-square $S_2$ change of $\sqrt{3}/(2d)$, which vanishes as the half-dimension grows.

The identity row is exact at every dimension. The other displayed entropy values are limits. An exact finite-dimensional purity correlation must not be substituted for a Rényi-2 entropy correlation: taking logarithms changes the observable.

## Changing the entropy order

For a general fixed order $\alpha>0$, define the limiting same-order correlation by

```math
\rho_\alpha(U)=
\frac{\sum_{k\geq2}k c_{\alpha,k}^2F_k(U)}
{\sum_{k\geq2}k c_{\alpha,k}^2}.
```

Here are deterministic evaluations of that convergent series, rounded to six decimal places:

| Gate | Logarithmic negativity, $\alpha=1/2$ | Von Neumann, $\alpha=1$ | Rényi-2, $\alpha=2$ |
|---|---:|---:|---:|
| Identity | 1 | 1 | 1 |
| $e^{-i\pi ZZ/4}$ | 0.376423 | 0.467936 | 0.5 |
| Active SWAP | 0.172322 | 0.227732 | 0.25 |

Unlike order two, the first two columns include higher $F_k$. They therefore weight the same gate spectrum differently. These decimals are theorem evaluations, not fitted correlations or uncertainty estimates.

The active SWAP attains the lower bound in each column. Any gate on the same two active qubits has at most four nonzero operator Schmidt probabilities, and convexity gives $F_k\geq4^{1-k}$. Every coefficient weight $k c_{\alpha,k}^2$ in the same-order correlation is nonnegative.

## Why SWAP can change this entanglement

SWAP exchanges $a$ and $b$ but leaves $R$ and $T$ in place. State by state,

```math
S_{\alpha,aR}(P_{ab}\psi)=S_{\alpha,bR}(\psi).
```

The operation changes which active qubit belongs with spectator $R$. Existing correlations between the active factors and the spectators can therefore change the entanglement across $aR\mid bT$. No claim that SWAP entangles a product of two bare qubits is needed.

A concrete state makes this distinction visible. At $n=2$, start with one Bell pair between $a$ and $R$, and another between $b$ and $T$. The state is a product across $aR\mid bT$. After swapping $a$ and $b$, both Bell pairs cross that cut, giving entropy $2\log2$ at every positive order. This state is an illustration of the subsystem assignment, not an input to the Haar covariance theorem or a sample in the numerical cohort.

Swapping the **entire halves** $aR$ and $bT$ instead preserves every Schmidt probability, so every entropy remains exactly unchanged. Its active support grows with $d$ and the fixed-support theorem does not apply. In particular, the active-SWAP limiting row cannot be used at $n=1$, where the active qubits are already the complete halves.

## Sources and reproduction

The maintained [theorem](../theory/THEOREM.md) and [proof](../theory/PROOF.md) supply the formulas. The underlying operator spectra and SWAP distinction are recorded in the [general-gate derivation](../evidence/checkpoint08/foundation/GENERAL_GATE_REVIEW.md). The phase-gate values agree with the inherited [frozen phase-gate predictions](../evidence/checkpoint07/numerics/operator_results/frozen_prediction.json); the SWAP values agree with the [frozen non-diagonal predictions](../evidence/checkpoint07/checkpoints/07/results/pilot_frozen.json). Those prediction files record scaled increments and variances rather than all the normalized correlations printed here.

See [reproduction](../REPRODUCE.md) for the maintained calculation entry point, [results](RESULTS.md) for the existing finite-size samples, and [references](REFERENCES.md) for prior work. The illustrative table makes no claim of a finite-size error bound, general prepared-state universality, or practical estimation precision.
