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

## Choose a route

**LEARN:** use the selected reading below as needed, then follow the
[tutorial bridge](TUTORIAL_BRIDGE.md), the [worked gate example](WORKED_EXAMPLE.md),
and [results and evidence](RESULTS.md). The progression is the physical
same-state comparison, correlated Gaussian/Wishart matrices, fluctuation modes,
gate power sums, normalized entropy covariance, and spatial-access consequences.

**CHECK:** go straight to the [canonical theorem](../theory/THEOREM.md) and
[proof](../theory/PROOF.md). They state the assumptions, indexed contraction,
analytic input and normalization. The [claim ledger](../CLAIM_LEDGER.md),
[references](REFERENCES.md), and [results](RESULTS.md) provide status, attribution
and evidence. You need not complete LEARN first.

**REPRODUCE:** the [focused reproduction](../REPRODUCE.md) evaluates the maintained
example, verifies frozen inputs, and runs six inherited deterministic checks.
Historical files are supporting records, not prerequisite reading. Neither a
manuscript nor an earlier conversation is needed.

## Selected reading

The sole external background tutorial is James A. Mingo and Roland Speicher,
*Free Probability and Random Matrices*, Fields Institute Monographs 35,
Springer, 2017. Use the [author page and errata](https://rolandspeicher.com/literature/mingo-speicher/)
and its [author PDF](https://rolandspeicher.com/wp-content/uploads/2019/02/mingo-speicher.pdf).
The [publisher edition](https://doi.org/10.1007/978-1-4939-6942-5) has different
pagination. No published-page equivalence is assumed here.

The table separately names physical PDF pages (counted from one) and printed
author-PDF folios. They coincide at these verified locations. The source was
retrieved on 13 September 2026; its hash, errata review and source cautions are
in the [implementation record](../reviews/mingo-speicher-reader-route/IMPLEMENTATION.md).
These are short selections, not whole-chapter assignments. Skip any selection
whose concept you already know.

| Exact selection | Physical PDF pages / printed folios | Concept to learn | Question it prepares you to answer | Local destination |
|---|---|---|---|---|
| §1.4, definition and moments of a standard complex Gaussian, before Exercise 6 | 17 / 17 | Variance-one complex entries and vanishing unconjugated covariance | Which Gaussian convention represents a Haar coefficient matrix? | [Bridge §2](TUTORIAL_BRIDGE.md#2-a-quantum-state-becomes-a-normalized-wishart-matrix) |
| §4.5.1, Wishart model and Marchenko–Pastur identification including Eq. (4.18); omit Exercises 12–13 | 122–123 / 122–123 | The scaling of `XX*/N` and aspect ratio `M/N` | What is the spectrum before trace normalization, at square aspect ratio? | [Bridge §2](TUTORIAL_BRIDGE.md#2-a-quantum-state-becomes-a-normalized-wishart-matrix) |
| §5.1, scaling discussion on 128 before Theorem 1; first-kind Chebyshev definition/table and Definition 2 on 129 | 128–129 / 128–129 | Fluctuations of unnormalized traces, covariance, and the book's polynomial convention | Why do order-one trace fluctuations coexist with a deterministic empirical law? | [Bridge §3](TUTORIAL_BRIDGE.md#3-fluctuation-modes-separate-the-spectral-contributions) |
| §5.6 opening, from its heading through the introductory explanation, stopping before §5.6.1 | 156–157 / 156–157 | Exact mean centering and covariance diagonalization | What benefit does a basis of uncorrelated fluctuation modes provide? | [Bridge §3](TUTORIAL_BRIDGE.md#3-fluctuation-modes-separate-the-spectral-contributions) |
| §5.6.1, Example 42 only, stopping before Remark 43 | 160–161 / 160–161 | Shifted and scaled first-kind Chebyshev polynomials for Wishart fluctuations | Which polynomial basis belongs to the square-Wishart interval `[0,4]`? | [Bridge §3](TUTORIAL_BRIDGE.md#3-fluctuation-modes-separate-the-spectral-contributions), then [worked example](WORKED_EXAMPLE.md) |

The local bridge explains the square Marchenko–Pastur density, trace conventions,
and the quantum dictionary directly. Reading the free-cumulant identification in
§4.5.1 does not require mastering the R-transform here: `NC(k)` there means
noncrossing partitions of `k` cyclically ordered positions, used to count the
limiting moments. Our square law and its use are stated locally. The assigned
Example 42 supplies a basis convention, not the gate-dependent covariance law.

### Deeper reading for the derivation

These optional selections use the same book. The [proof](../theory/PROOF.md)
provides the project-specific calculation, so they are not a second required
course. Read them when you want to follow the pairing language behind the bridge.

| Exact selection | Physical PDF pages / printed folios | Concept to learn | Question it prepares you to answer | Local destination |
|---|---|---|---|---|
| §1.1, cumulants from the logarithm of the characteristic function on 14, including the Gaussian paragraph through the first sentence on 15 | 14–15 / 14–15 | Classical cumulants and the Gaussian truncation | Why do connected contractions control the Gaussian fluctuation limit? | [Proof §2](../theory/PROOF.md#2-connected-contractions-and-the-surviving-cycle) and [§3](../theory/PROOF.md#3-chebyshev-modes-and-polynomial-gaussian-limits) |
| §1.3 Gaussian-vector definitions; §1.4 complex moments; §1.5 Theorem 1, Corollary 2, Eqs. (1.7)–(1.8), and Exercise 7 statement | 16–19 / 16–19 | Wick expansion and conjugated complex pairings | Which indices can be paired in the gate-transformed Gaussian array? | [Proof §1](../theory/PROOF.md#1-assumptions-and-gaussian-representation) and [§2](../theory/PROOF.md#2-connected-contractions-and-the-surviving-cycle) |
| §5.1 opening annular-pairing paragraph on 130, before the diagrams; Theorem 9, Eq. (5.5), its Euler explanation and Remark 10 on 135 | 130 and 135 / 130 and 135 | Connected trace diagrams and dimension power counting | Why does covariance select a planar annulus, while higher connected cumulants vanish? | [Proof §2](../theory/PROOF.md#2-connected-contractions-and-the-surviving-cycle) |
| §5.6.1, Remark 43 on 161 through the paragraph describing `k` planar gluings, stopping before Figure 5.5 | 161 / 161 | Through-pair intuition for diagonal modes | Why separate a surviving cycle from ordinary tree decorations? | [Bridge §4](TUTORIAL_BRIDGE.md#4-the-surviving-cycle-carries-the-gate-spectrum) and [Proof §3](../theory/PROOF.md#3-chebyshev-modes-and-polynomial-gaussian-limits) |

Apply the author's correction to Exercise 7: its reference is to Exercise 6(ii),
not 6(iii). The GUE through-pairs in Remark 43 are an intuition for diagram
organization; our Wishart mode `k` is the half-length of an alternating row/column
cycle. The local proof gives that adaptation. Exercises 11–12 and Figure 5.6
are not assigned; see the [source cautions](../reviews/mingo-speicher-reader-route/IMPLEMENTATION.md#source-caveats)
before using nearby formulas with different normalization or centering.

Three roles remain distinct throughout: the book teaches background; primary
papers provide credited machinery and the low-regularity approximation theorem;
this repository defines and derives the additional gate contraction and entropy
consequences. The [references](REFERENCES.md) are attribution, not an expanded
prerequisite reading list. Selecting the book implies no endorsement by its authors.

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

The gate has its own operator Schmidt probabilities, distinct from the Schmidt
probabilities of the input state. Their power sums determine the limiting
covariance. The [bridge](TUTORIAL_BRIDGE.md) defines both spectra and realignment
before using them. The entropy orders provide universal coefficients; the gate
enters through its operator power sums.

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
