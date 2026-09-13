# Publication positioning: the completed Haar benchmark

Assessment date: 13 September 2026. Scope: reports 07–08 and their inherited novelty reviews; three targeted primary-source reads. This is a publication and contribution assessment, not a new mathematical audit or an exhaustive originality search.

## Decision

**Yes: subject to the focused correctness audit clearing the central theorem, the completed fixed-boundary Haar result is a credible standalone paper to develop for Quantum, and it is sensible to separate that paper before continuing the search for a stronger PRL result.** This means that the existing scientific contribution justifies a serious submission effort. It does not mean that the present checkpoint package is a finished submission or that acceptance is assured.

The positive case rests on an explicit, interpretable theorem: the normalized operator Schmidt spectrum of a deterministic finite boundary gate determines the limiting covariance of actual entropies at every fixed positive Rényi order. For two operations, the spectrum is that of the relative gate. The theorem produces a complete covariance family, including von Neumann entropy and pure-state logarithmic negativity, and quantitative consequences about residual memory and distinguishability. This is enough substance for a focused quantum-information article if the proof is complete and the contribution is positioned honestly.

The main adverse case remains serious: a referee could judge the answer to be a useful but insufficiently significant specialization of established block-Gaussian fluctuation machinery, supplemented by familiar operator-entanglement consequences. Repackaging the existing purity/OTOC connection, the SWAP distinction, or the low-order temporal exponent would not answer that objection. The all-positive-order entropy result must bear the paper's weight.

## What Quantum itself says

The official [About page](https://quantum-journal.org/about/), fetched and read on the assessment date, describes Quantum as an “open-access peer-reviewed journal for quantum science and related fields.” Its Mission section says:

> “The main editorial criteria are correctness, significance, and clarity.”

The same section says it publishes “high quality research, both theoretical and experimental.” These are the official statements used here. I have not substituted a remembered acceptance rubric or inferred that Quantum accepts work merely because a broader-interest journal might decline it. The page is an editorial mission statement, not an acceptance guarantee or a numerical threshold.

This project is directly within the stated scope: it connects quantum gates, operator entanglement, and state-entanglement statistics. Its significance can be presented as an exact quantum-information benchmark with a clear explanatory content. A demonstrated many-body universality law is not necessary to state that contribution. Whether the contribution is significant enough remains an editorial and referee judgment.

## Closest precedent and the actual addition

| Established antecedent | What the present work adds, if its theorem is sound | Novelty consequence |
|---|---|---|
| Mingo–Speicher weighted annular Wishart fluctuations; Kusalik–Mingo–Speicher Chebyshev diagonalization; low-regularity square-LUE entropy approximation | Evaluate the mixed quantum-gate contractions, establish the operator-spectrum mode factors, remove shared trace normalization, and transfer the joint result to the entropy functions | These foundations must be credited. A new CLT or new second-order-freeness formalism is not the contribution. |
| Diaz–Mingo–Belinschi, *On the Global Fluctuations of Block Gaussian Matrices*, Definition 1, Theorem 2 and Eqs. (5)–(6) | A collapse from a finite tensor of block covariances to one familiar quantum-gate spectrum, followed by explicit entropy coefficients for all fixed positive orders | This is the strongest mathematical overlap. The general source contains matrix-valued covariance machinery and polynomial/rational linearization, but the inspected statements do not state this gate-specific entropy law. |
| Styliaris–Anand–Zanardi, *Information Scrambling over Bipartitions*, Theorems 1–2 | The order-two increment has a direct normalization-matched connection to their existing linear operator-entanglement/bipartite-OTOC quantity; higher entropy orders sample the higher operator moments | The order-two invariant itself is established. The complete conversion into actual globally Haar-state entropy covariance is the candidate new result. |
| Operator entanglement, dual unitarity, and the two-invariant formula for product-input entangling power | A sharp support-dependent lower bound on limiting entropy correlation, attained by dual-unitary gates when active factors have equal dimension | A useful physical corollary of the new law. Flat operator spectra and SWAP's maximal operator entanglement with zero active product-input entangling power are established facts. |
| Replica entanglement features, unitary designs, and finite moment reconstruction | Quantified equal-purity/different-entropy-memory examples and exact recovery of the operator spectrum from an ideal finite integer-order hierarchy | Good illustrations and corollaries. Neither the failure of second moments to fix higher moments nor Newton-identity reconstruction is itself a new principle. |

The block-Gaussian paper is more threatening than an ordinary scalar-correlated Wishart interpolation: fixed gate support gives precisely a finite array of mixed Gaussian blocks with growing spectator indices. Its introduction already identifies noncrossing annular pairings as the covariance mechanism. It provides a second-order Cauchy transform for general block covariance and a linearization route to noncommutative polynomials and rational functions. A manuscript must show the special reduction explicitly; changing names from block labels to boundary indices is insufficient.

There is nevertheless a defensible residual contribution. The inspected block-Gaussian theorem uses selfadjoint Gaussian-block conventions and does not directly state the complex coefficient-matrix/relative-unitary entropy setting. Its general expressions retain a tensor of covariance information. Showing why unitarity removes tree attachments, why the remaining cycle gives precisely the realignment power sum, and why no competing orientation invariant survives is a genuine derivational task. Obtaining the explicit nonpolynomial entropy family at the balanced hard edge completes an answer the general framework does not present. This is an application and simplification of existing mathematics with a quantum-information payoff; it need not be described as new fluctuation machinery to be worth publishing.

The OTOC source makes the distinction equally concrete. Its Theorems 1–2 identify the averaged bipartite OTOC with linear operator entanglement and relate product-input entangling power to the quantities for U and U composed with SWAP. Its Theorem 8 interprets linear entropy production for a reduced channel with a maximally mixed environment and random pure subsystem input. Those are different observables and input ensembles from the covariance of before/after entropies of one globally Haar pure state. At order two, the present law connects to a known quantity. At other orders, it resolves how the complete operator spectrum enters a different fluctuation measurement.

## A compact standalone contribution

The core paper can consist of the covariance theorem and three tightly connected consequences already established in the inherited work:

1. Fixed spatial access imposes positive residual entropy correlation in the spectator limit; equal-size dual-unitary gates attain the optimum.
2. Equal operator purity can coexist with different ordinary entropy memories, making clear why the full spectrum is needed. One existing example suffices.
3. The ideal covariance hierarchy determines the operator Schmidt spectrum, with the already documented severe conditioning limitations.

The exact finite-dimensional purity identity is particularly useful as a scope check and calibration: global Haar purity memory is exactly tied to entangling power defined using product states of the whole halves. It prevents an overbroad “memory is unrelated to entangling power” claim. The exchanged-subsystem sum/difference identities and exact two-design pair can be supporting material if they improve that account. They should not become independent headline discoveries solely to enlarge the paper.

The fixed-support theorem already has a coherent end point. A failed or inconclusive later Floquet/eigenstate test would restrict physical extrapolation without undoing this theorem. The standalone paper should retain the exact Haar statement and any relevant adverse controls; a separate PRL search should ask a scientifically stronger question rather than count another algebraic corollary as the needed advance.

## Minimum work remaining

These are completion tasks for a submission, not a demand for a broad new research campaign.

- Consolidate a complete, self-contained proof of the general-gate theorem. The decisive checks are the all-degree mixed contraction reduction, complex orientation conventions, relative-gate convention, higher-cumulant control, common-trace normalization, and the approximation/delta-method passage for every fixed positive order. The existing internal proof and reproduction records are evidence; this review has not independently re-proved them.
- Write one exact assumptions statement and use it consistently: complex Haar input, balanced growing halves, deterministic fixed active dimensions and gate, fixed positive entropy orders, and a fixed finite collection of operations. State the d-squared covariance scaling and vanishing absolute fluctuations. Do not silently allow support to grow with d, a whole-half SWAP, path-space limits, finite-dimensional entropy identities inferred from purity, or generic thermal-state universality.
- Integrate the nearest-prior-work comparison into the actual argument, including the block-Gaussian framework, the order-two OTOC relation, and checkpoint 08's correction distinguishing active product inputs from whole-half product inputs. For the exact finite-dimensional normalized purity identity, use “derived here” unless its independent novelty has been specifically established; algebraic reformulation can still be useful without a priority claim.
- Turn the existing sufficient validation into a compact, reproducible presentation with no new sampling requirement. Separate exact algebra, deterministic floating-point checks, asymptotic predictions, and finite-size illustrations. Preserve the reported discrepancies and scope limits. The large existing checkpoint package needs editorial consolidation, not a larger collection of examples.

An external expert reading the proof would improve confidence, but contacting one is not a prerequisite imposed by this assessment for separating the project now. Any unresolved mathematical gap found in the focused audit must be repaired before treating the central claim as submission-ready. The current evidence does not justify a percentage acceptance estimate.

## Source ledger and read depth

Exactly three primary pages were fetched for this assessment. No general web search tool was exposed; direct public URL retrieval was used. No failed search was used as evidence of originality.

| Source | Read level in this assessment |
|---|---|
| [Quantum, About](https://quantum-journal.org/about/) | Official Mission text and scope; exact quotations above. This is the sole source for the journal's stated criteria here. |
| [Diaz, Mingo, Belinschi, arXiv:1711.07140v1](https://arxiv.org/html/1711.07140v1) | Abstract, introduction, Definition 1, Theorem 2, Eqs. (5)–(6), the linearization discussion, and the definitions/annular formulation in the opening sections. Framework and theorem-statement comparison, not a line-by-line proof audit. |
| [Styliaris, Anand, Zanardi, arXiv:2007.08570v3](https://arxiv.org/html/2007.08570v3) | Abstract; Theorems 1–2 and Eqs. (4)–(5); reduced-channel interpretation, Theorem 8 and Eq. (13); concluding discussion. These passages establish the overlap and input-ensemble distinction used above. |

The other literature comparisons are inherited from the read reports `Entanglement-Temporal-Fluctuations-Report-07.md` and `-08.md`, checkpoint 08's `foundation/GENERAL_GATE_LITERATURE.md`, and checkpoint 07's `docs/reviews/NOVELTY_REVIEW.md`. Their documented primary inspection levels are retained there; these additional papers were not fetched again. Consequently, “no direct prior statement located” refers to this bounded cumulative record and is not an exhaustive originality certification.
