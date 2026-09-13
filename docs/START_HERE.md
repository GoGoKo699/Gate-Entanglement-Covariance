# What a boundary gate changes about entanglement fluctuations

Take a large bipartite pure state and act on one small factor on each side of its cut. How much does the entanglement after the gate still tell us about the entanglement before it?

The question becomes precise for a Haar-random input. Haar invariance fixes the mean entanglement after any deterministic unitary. It does not fix the relation between the before and after values obtained from the **same input state**. This repository studies that relation through entropy covariance.

## The comparison

For each independently sampled complex-Haar state, record a pair:

```math
X_\alpha=S_\alpha(\psi),\qquad
Y_\alpha=S_\alpha(U\psi).
```

Here the entropy is across the same bipartition before and after the gate. All entropies use natural logarithms. Rényi order one is the von Neumann entropy, order two is negative log purity, and order one half is logarithmic negativity for a pure bipartite state.

Both entries have the same marginal distribution, so

```math
\mathbb E Y_\alpha=\mathbb E X_\alpha,
\qquad
\operatorname{Var}Y_\alpha=\operatorname{Var}X_\alpha.
```

The covariance asks whether an input with slightly above-average entropy tends to remain above average after the gate. A product of local unitaries preserves every pair exactly. A crossing gate can change the entropy of an individual state even though its ensemble mean stays fixed. Using two independently drawn states for the before and after entries would remove the correlation we want to measure.

The word **memory** below means this ensemble correlation. It does not assume a memory device, a stochastic time evolution, or a monotonic decay with time.

## What grows, and what stays fixed

Write the two halves as an active factor and a spectator:

```math
A=aR,\qquad B=bT,\qquad
\dim A=\dim B=d,
\qquad \dim a=r,\quad\dim b=s.
```

The gate acts on $a b$ and is the identity on $R T$. The limit increases $d$ while keeping $r$, $s$, and the gate fixed. The input is globally Haar; the active factors need not start unentangled with their spectators. The entropy orders and the finite collection of gates under comparison also stay fixed.

For each fixed positive order, entropy fluctuations around the ensemble mean have size $1/d$. Their covariance has size $1/d^2$. We therefore study the finite limits of $d^2\operatorname{Cov}(Y_\alpha,X_\beta)$ and of the normalized correlation. A nonzero limiting correlation describes the relation between these small fluctuations. It is not a finite fraction of the total entropy retained by the gate.

## Why the operator Schmidt spectrum appears

The gate itself has an operator Schmidt decomposition. Using Hilbert-Schmidt orthonormal operator bases on the active factors, write

```math
U=\sqrt{rs}\sum_h\sqrt{\eta_h}\,A_h\otimes B_h,
\qquad \eta_h\geq0,\qquad\sum_h\eta_h=1.
```

The probabilities $\eta_h$ describe how the gate is distributed across orthogonal product operators. They are properties of the gate, distinct from the Schmidt probabilities of the input state. Their power sums are

```math
F_k(U)=\sum_h\eta_h^k.
```

The central theorem says that these power sums determine the complete limiting entropy covariance at every pair of fixed positive Rényi orders. The entropy orders provide universal coefficients; the gate enters only through $F_k$.

The proof explains why. Haar input can be represented by a normalized Gaussian coefficient matrix. After averaging the paired spectral observables, the leading connected contractions reduce to a cycle carrying the gate's realigned operator spectrum. Its degree-$k$ weight is $F_k$. The shared state normalization cancels the radial mode. Established Wishart fluctuation and low-regularity approximation results then transfer the calculation to actual entropies. The [proof](../theory/PROOF.md) gives the steps and their dependencies; the [references](REFERENCES.md) distinguish the inherited methods from the proposed gate-to-entropy relation.

## Three consequences

1. **Limited spatial access leaves a positive correlation.** Fixed active dimensions bound the number of operator Schmidt probabilities. Their power sums cannot all approach zero. This imposes a positive floor on the limiting same-order entropy correlation. For equal active dimensions, gates with a flat operator Schmidt spectrum attain it.
2. **Operator purity gives only part of the answer.** Rényi-2 correlation depends only on $F_2$. Other entropy orders also weight higher power sums, so equal operator purity can coexist with unequal entropy covariance.
3. **Ideal covariance data contain spectral information.** A finite integer-order hierarchy determines a finite-rank operator Schmidt spectrum. The inversion is poorly conditioned and does not identify the operator Schmidt bases or provide an efficient tomography method.

The [worked example](WORKED_EXAMPLE.md) makes the gate spectrum and correlation floor concrete for a single boundary qubit pair. The [theorem statement](../theory/THEOREM.md) gives the exact assumptions, coefficients, and consequences.

## What the evidence establishes

The theorem is asymptotic. Existing finite-dimensional Haar samples provide modest illustrations, with sampling error and finite-size deviations reported separately. Exact purity identities and deterministic contraction checks test specific components; they do not replace the all-order entropy proof.

A tested extension to Floquet eigenstates failed its declared Haar comparison. The theorem is therefore retained as a Haar benchmark. It does not currently establish a law for generic prepared states, growing gate support, or a uniform shrinking-time limit. A whole-half SWAP also lies outside the fixed-support limit.

Continue with [the worked example](WORKED_EXAMPLE.md), [results and their limitations](RESULTS.md), or [reproduction instructions](../REPRODUCE.md). The [claim ledger](../CLAIM_LEDGER.md) records the current status of each claim.
