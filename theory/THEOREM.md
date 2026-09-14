# The scientific core

This is the precise statement used throughout the repository. [The derivation](PROOF.md) fixes the conventions and explains its proof dependencies; [the worked example](../docs/WORKED_EXAMPLE.md) evaluates it for a boundary qubit pair. Natural logarithms are used.

This is the **CHECK** entrance. The result below requires no educational detour.
For translations from the selected Mingo–Speicher passages, use the
[tutorial bridge](../docs/TUTORIAL_BRIDGE.md). The book is background; primary
proof inputs and project-specific steps are distinguished in the proof map below.

## Setting

Fix positive integers r and s. Let d tend to infinity through common multiples of r and s, with

```math
\mathcal H_A=\mathbb C^r\otimes\mathbb C^{d/r},\qquad
\mathcal H_B=\mathbb C^s\otimes\mathbb C^{d/s}.
```

Let ψ be a complex-Haar pure state on the balanced d by d bipartition. A fixed finite list of deterministic unitaries U_l acts on the r by s active factors, with identity action on the spectators. The entropy orders are fixed and positive. Write S_α(U_l ψ) for the Rényi entropy across A|B, with the continuous order-one definition.

For a relative gate V_lm=U_l U_m†, define realignment by

```math
\mathcal R(V)_{(a,c),(b,e)}=V_{ab,ce}.
```

Its normalized operator Schmidt probabilities η_h are the nonzero eigenvalues of

```math
\mathcal R(V)\mathcal R(V)^\dagger/(rs),\qquad
\sum_h\eta_h=1.
```

Let F_k(V)=Σ_h η_h(V)^k. Define coefficients for k≥2 by

```math
c_{\alpha,2}=-\frac{2\alpha}{\alpha+2},\qquad
c_{\alpha,k+1}=c_{\alpha,k}\frac{\alpha-k}{\alpha+k+1}.
```

This recurrence also defines the continuous order-one coefficients, and automatically terminates for positive integer orders at least two.

## Covariance and finite-family limit

The central result is

```math
\lim_{d\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits 
\bigl(S_\alpha(U_l\psi),S_\beta(U_m\psi)\bigr)
=\frac14\sum_{k\ge2}k\,c_{\alpha,k}c_{\beta,k}F_k(V_{lm}).
```

The series is absolutely convergent. Any fixed finite family of exact-mean-centered entropies multiplied by d converges jointly to a mean-zero Gaussian vector with these covariances. Degenerate covariance matrices are allowed.

Each gate preserves the Haar marginal distribution. Thus the same-order mean-square increment satisfies

```math
\lim_{d\to\infty}d^2\mathbb E
\left[(S_\alpha(U\psi)-S_\alpha(\psi))^2\right]
=\frac12\sum_{k\ge2}k c_{\alpha,k}^2[1-F_k(U)].
```

The unscaled fluctuations vanish with d. This theorem describes their covariance, not a large absolute entropy change.

## Spatial-access consequence

Let ρ_α(U) denote the limiting correlation of the same-order entropies before and after U. Then

```math
\rho_\alpha(U)=
\frac{\sum_{k\ge2}k c_{\alpha,k}^2 F_k(U)}
{\sum_{k\ge2}k c_{\alpha,k}^2}.
```

The number of nonzero operator Schmidt probabilities is at most R=min(r²,s²). Convexity gives F_k≥R^{1-k}, hence

```math
\rho_\alpha(U)\ge
\frac{\sum_{k\ge2}k c_{\alpha,k}^2 R^{1-k}}
{\sum_{k\ge2}k c_{\alpha,k}^2}>0.
```

For equal active dimensions q, dual-unitary gates have q² flat probabilities and attain the bound. For a boundary qubit pair the minimum correlations at orders 1/2, 1, and 2 are approximately 0.17232220, 0.22773244, and 0.25. Pure-state logarithmic negativity is order 1/2 in this convention.

Fixed active support is essential. A SWAP of the entire growing halves preserves entanglement exactly and lies outside this limit. A SWAP of only the fixed active factors generally changes the global entanglement and saturates the bound.

## What the hierarchy identifies

At integer order n≥2, the series contains F_2 through F_n with a nonzero coefficient of F_n. For known finite rank R, orders 2 through R therefore determine F_2 through F_R successively; F_1=1 and Newton identities determine the multiset of probabilities. Rank one is trivial. This is exact information content, not a practical inference guarantee.

For a boundary qubit pair the normalized same-order correlations give

```math
F_2=\rho_2,\quad F_3=25\rho_3-24\rho_2,\quad
F_4=441\rho_4-1200\rho_3+760\rho_2.
```

The corresponding worst-case amplification of bounded input errors is 1, 49, and 2401. Root recovery can be still less stable near degeneracy. The hierarchy does not identify the operator Schmidt bases or the full gate.

## Proof map and attribution

1. Represent ψ by a normalized complex Gaussian coefficient matrix. Each transformed matrix is marginally an iid Gaussian matrix; their entry cross-covariance contains V_lm and spectator Kronecker deltas.
2. Connected spectator Wick graphs give the usual orientable Wishart power counting. The leading two-trace graph is planar and unicyclic. Every attached bridge is paired within a single trace, so same-gate unitarity removes all tree decorations.
3. The active contraction on the remaining cycle is Tr[(R(V)R(V)†)^k]/(rs)^k=F_k(V). Ordinary Wishart tree counts diagonalize the covariance in Γ_k(x)=2T_k((x−2)/2), with mode covariance δ_jk k F_k. Higher connected cumulants vanish for a fixed finite family.
4. The low-regularity square-LUE approximation of Henry Hu transfers centered polynomial limits to x^α for every fixed α>0 and to x log x. Marginal L² approximation and Cauchy–Schwarz suffice for cross-covariances; the different gates need not be independent.
5. Normalize the shared Gaussian trace. The exact-mean-centered L² entropy delta method cancels the conserved k=1 radial mode, leaving the displayed k≥2 law. Exceptional events are bounded using the combined normalized entropy, not separate logarithms.

The [consolidated derivation](PROOF.md) gives the indexed Wick convention, cycle contraction, nonpolynomial transfer, shared normalization, and explicit order-one remainder in one route. The detailed inherited [all-degree argument](../evidence/checkpoint08/foundation/GENERAL_GATE_REVIEW.md), [nonpolynomial transfer](../evidence/checkpoint08/foundation/NONSMOOTH_EXTENSION.md), [transfer audit](../evidence/checkpoint08/foundation/NONSMOOTH_EXTENSION_AUDIT.md), and [independent internal proof assessment](../reviews/PROOF_ASSESSMENT.md) remain available as source records.

These arguments build on annular Wishart fluctuations, Chebyshev diagonalization, block-Gaussian methods, and established LUE regularity results. The proposed contribution is the gate-spectrum reduction and the full actual-entropy covariance law with its quantum-information consequences. See [References](../docs/REFERENCES.md) for the external inputs and [publication positioning](../reviews/PUBLICATION_POSITIONING.md) for the closest literature and the limits of the novelty review.

No uniform finite-size error, growing support, growing order, shrinking-time limit, path-space convergence, or generic prepared-state extension is asserted.
