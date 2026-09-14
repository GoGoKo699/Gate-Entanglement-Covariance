# One Quantum article: proposed outline

**Reserved for the final phase.** The current task is repository refurnishing under [NEXT.md](NEXT.md). This outline is retained for later use and does not authorize manuscript drafting during that phase.

Working title: **Operator Schmidt spectra and entanglement covariance under local gates**

Purpose: present the completed fixed-boundary Haar theorem as a self-contained quantum-information result. The scoped core has passed the present internal proof audit. Submission preparation should consolidate the established argument and evidence; it need not await a broader physical application.

## Abstract and organizing claim

Open with the question: how much of the entanglement fluctuation of an equilibrium random pure state survives a deterministic operation across its cut? State the answer: for a balanced bipartition with growing spectators and fixed active dimensions, the normalized operator Schmidt spectrum of the operation determines the limiting covariance of every fixed positive-order Rényi entropy. Mention von Neumann entropy explicitly. State two consequences: fixed spatial access leaves a positive correlation, and equal operator purity need not imply equal entropy memory. Close with the exact ensemble and support restrictions. Avoid generic thermalization, efficient tomography, and a new scrambling diagnostic as abstract claims.

## 1. Question, setting, and nearest antecedents

Define a complex Haar pure state on equal halves of dimension d, with a deterministic unitary acting only on fixed active factors of dimensions r and s. Both observations use the same input state. Natural-log entropy means are stationary; absolute entropy fluctuations vanish as d grows. “Memory” denotes ensemble correlation of those fluctuations.

Explain why operator entanglement is a natural candidate, while citing its established relation to entangling power and bipartite OTOCs. Identify weighted annular Wishart fluctuations, Chebyshev diagonalization, and block-Gaussian second-order covariance as mathematical antecedents. The addition is their explicit gate-spectrum reduction and conversion into actual entropy covariance at every fixed positive order.

## 2. Main covariance theorem

State one theorem with all hypotheses. Define normalized operator Schmidt probabilities η and their moments F_k. Present the covariance series

```math
\lim_{d\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits 
 [S_\alpha(U\psi),S_\beta(\psi)]
=\frac14\sum_{k\ge2}k c_{\alpha k}c_{\beta k}F_k(U).
```

Give the explicit coefficient formula, its integer truncations, and continuous order-one value. Extend the statement to a fixed finite collection of gates using the relative gate and the joint Gaussian limit. Emphasize that separate gate spectra do not determine relative spectra.

Provide a readable proof overview: Gaussian coefficient blocks, spectator topology, unitarity cancellation of tree attachments, realignment cycle contraction, Chebyshev modes, shared trace normalization, and entropy approximation. Full proofs belong in appendices with precise citations and conventions. The novelty resides in the special reduction and entropy result, not the general fluctuation machinery.

## 3. Fixed access limits decorrelation

Derive the correlation bound from the rank constraint R ≤ min(r²,s²) and F_k ≥ R^(1−k). Explain why dual-unitary gates attain it for equal active dimensions. Give the existing active-qubit values for orders one half, one, and two; the Rényi-2 minimum is 1/4.

Use the existing boundary SWAP/phase-SWAP comparison to explain what one-cut memory omits. Distinguish active product-input entangling power from entangling power on product states of the whole halves. Include the exact finite-dimensional purity identity as a calibration, expressly separating purity from logarithmic purity. Whole-half SWAP lies outside the growing-spectator theorem.

## 4. What higher entropy orders distinguish

Use one existing equal-purity/different-memory construction to demonstrate why higher operator moments matter. State ideal spectrum identifiability through finite integer-order moment inversion, followed immediately by the existing conditioning limitations. No reconstruction-efficiency claim follows.

The exchanged-subsystem identities and exact gate-design pair can be compact appendix material. Attribute established entangling-power, gate-typicality, design, and replica structures. Do not present every corollary as an independent discovery.

## 5. Verification and physical scope

Use only saved results: the exact four-copy Haar checks, Wick-contraction controls, and checkpoint-07 non-diagonal entropy pilot. A compact figure or table should distinguish deterministic predictions from sampled estimates and finite-size effects. Describe internal independent implementations and fresh-directory reproduction accurately.

Retain the checkpoint-09 Floquet failure in a short scope subsection, with details and its existing figure in an appendix. All twelve nontrivial comparisons failed the declared descriptive tolerances in one nested two-size circuit family. Neither fluctuation scale nor normalized memory followed Haar predictions. Dependent eigenstate cohorts provide no independent-disorder error bars; two sizes establish no thermodynamic limit. Cite the existing literature on enhanced Floquet entropy fluctuations. The result restricts extrapolation and is not a new anomaly claim.

## Submission completion tasks

- Consolidate the internally audited theorem and appendices into one notation-consistent proof; resolve every dependency and attribution explicitly.
- Assemble the bibliography from the existing primary-source ledger, including the closest block-Gaussian and OTOC statements and the Floquet precedents.
- Select existing examples, tables, and figures; preserve units, scaling, uncertainty labels, ensemble distinctions, and finite-size qualifications.
- Create one reproduction entry point with pinned environment information, immutable inputs, expected outputs, and provenance for retained negative results.
- Complete author and acknowledgment information, journal formatting, figure legibility, cross-references, and a claim-by-claim final read against the proofs.

No new model, larger sampling campaign, or additional algebraic example is required by this outline.
