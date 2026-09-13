# References and their roles

The [technical derivation](../theory/PROOF.md) uses established random-matrix results and evaluates the additional gate contractions. This page identifies those dependencies and distinguishes them from nearby quantum-information results. The linked source records document the underlying literature review.

## Sole background tutorial

**B1. James A. Mingo and Roland Speicher, _Free Probability and Random Matrices_.**
Fields Institute Monographs **35**, Springer, 2017.
[Author page, PDF link and errata](https://rolandspeicher.com/literature/mingo-speicher/),
[author PDF](https://rolandspeicher.com/wp-content/uploads/2019/02/mingo-speicher.pdf),
[DOI:10.1007/978-1-4939-6942-5](https://doi.org/10.1007/978-1-4939-6942-5).
This is the one assigned background tutorial. The [selected reading map](START_HERE.md#selected-reading)
uses short Gaussian, Wishart and fluctuation passages, with an optional deeper
route from the same book. [Source verification](../reviews/mingo-speicher-reader-route/IMPLEMENTATION.md)
records retrieval, SHA-256, author-PDF pagination, errata and nearby source cautions.
No source PDF or page images are redistributed.

The book teaches the background and polynomial conventions. It does not supply
the repository's gate-dependent contraction or entropy theorem. Those bridges
are explained [locally](TUTORIAL_BRIDGE.md), with the [canonical proof](../theory/PROOF.md)
retaining all external hypotheses. R1–R2 below credit established fluctuation
machinery; R4 is an actual analytic theorem input. R3 and R5 are comparison
frameworks, and R6–R9 locate quantum-information antecedents. These primary papers
are not additional assigned tutorials. The educational choice implies no author
endorsement and replaces no primary attribution.

## Mathematical foundations

**R1. James A. Mingo and Roland Speicher, _Second Order Freeness and Fluctuations of Random Matrices: I. Gaussian and Wishart matrices and cyclic Fock spaces_.** [arXiv:math/0405191v3](https://arxiv.org/abs/math/0405191v3). The saved review inspected Theorem 3.5 and its cumulant calculation, Sections 8.3 and 9. These supply weighted annular Wishart machinery and its second-order setting. The gate-specific realignment reduction is derived in this repository; it is not quoted as a theorem of this source. [Read record](../evidence/checkpoint08/foundation/GENERAL_GATE_LITERATURE.md).

**R2. Timothy Kusalik, James A. Mingo and Roland Speicher, _Orthogonal Polynomials and Fluctuations of Random Matrices_.** [arXiv:math/0503169v1](https://arxiv.org/abs/math/0503169v1). The saved review inspected the introduction's theorem and annular half-permutation interpretation, including polynomial degree versus through-block count. This is the source for the established Wishart tree-decoration and shifted Chebyshev diagonalization framework. [Read record](../evidence/checkpoint08/foundation/GENERAL_GATE_LITERATURE.md).

**R3. Mario Diaz, James Mingo and Serban Belinschi, _On the Global Fluctuations of Block Gaussian Matrices_.** [arXiv:1711.07140v1](https://arxiv.org/abs/1711.07140v1); _Probability Theory and Related Fields_ **176**, 599–648 (2020), [DOI:10.1007/s00440-019-00925-1](https://doi.org/10.1007/s00440-019-00925-1). Inspected passages: Definition 1, Theorem 2, Eqs. (5)–(6), introductory linearization and annular-pairing discussion. This is the closest general block-covariance framework. It is an attribution and comparison anchor, not a theorem invoked without adapting its selfadjoint Gaussian conventions to our complex coefficient matrices. [Assessment and read depth](../reviews/PUBLICATION_POSITIONING.md).

**R4. Henry Hu, _On the regularity conditions in the CLT for the LUE_.** [arXiv:2310.08509v1](https://arxiv.org/abs/2310.08509v1), [versioned full text](https://arxiv.org/html/2310.08509v1). Inspected passages: normalization (1.2), variance functional (1.4), Theorem 1.1, Lemma 1.2, Corollary 1.3, notation and Section 3 approximation. This is the explicit external input for square-LUE variance convergence and low-regularity approximation. Its rectangularity parameter includes zero. The repository checks the hypothesis for cut-off $x^\alpha$ with every fixed $\alpha>0$ and for $x\log x$, then supplies cutoff removal, finite-vector transfer and entropy normalization. [Assumption check](../evidence/checkpoint08/foundation/NONSMOOTH_EXTENSION.md), [independent internal assessment](../reviews/PROOF_ASSESSMENT.md).

**R5. Jeffrey Kuan and Zhengye Zhou, _Three-dimensional Gaussian fluctuations of spectra of overlapping stochastic Wishart matrices_.** [arXiv:2112.13728v1](https://arxiv.org/abs/2112.13728v1). Inspected passages: Section 1.2, Theorem 1.1 and the opening closed-walk proof. Temporal Wishart Gaussian fields are established prior work. Their homogeneous entry-time assumptions are not automatically the finite gate-covariance tensor used here. This is a scope comparison, not a dependency of the proof route. [Read record](../evidence/checkpoint08/foundation/GENERAL_GATE_LITERATURE.md).

## Quantum-information interpretation

**R6. Paolo Zanardi, _Entanglement of Quantum Evolutions_.** [arXiv:quant-ph/0010074](https://arxiv.org/abs/quant-ph/0010074). The saved record identifies inspection of the operator-state definition and Eq. (12). Operator entanglement and its relation to entangling power are established concepts. [Read record](../evidence/checkpoint07/docs/reviews/source-ledger.json).

**R7. Paolo Zanardi, Christof Zalka and Lara Faoro, _On the Entangling Power of Quantum Evolutions_.** [arXiv:quant-ph/0005031](https://arxiv.org/abs/quant-ph/0005031). The relevant inputs are the product-state definitions and average formulas. Product-input average linear entropy is a different observable from covariance of entropies of the same globally Haar input before and after a gate. Neither ensemble should silently replace the other. [Read record](../evidence/checkpoint07/docs/reviews/source-ledger.json).

**R8. Georgios Styliaris, Namit Anand and Paolo Zanardi, _Information Scrambling over Bipartitions: Equilibration, Entropy Production, and Typicality_.** [arXiv:2007.08570v3](https://arxiv.org/abs/2007.08570v3); _Physical Review Letters_ **126**, 030601 (2021). Inspected passages: Theorems 1–2, Eqs. (4)–(5), Theorem 8 and Eq. (13), with their input-ensemble interpretation. The bipartite averaged OTOC and linear operator entanglement are already related there. Our limiting order-two kernel uses that established invariant; the full actual-entropy covariance hierarchy is the project's proposed addition. [Comparison and read depth](../reviews/PUBLICATION_POSITIONING.md).

**R9. Bhargavi Jonnadula, Prabha Mandayam, Karol Życzkowski and Arul Lakshminarayan, _Entanglement measures of bipartite quantum gates and their thermalization under arbitrary interaction strength_.** [arXiv:1909.08139v2](https://arxiv.org/abs/1909.08139v2). Inspected passages: Sections II.1–II.2, Eqs. (5)–(23), entangling power versus gate typicality. Relevant antecedents include realignment and partial-transpose invariants, flat spectra of dual-unitary gates, and SWAP's maximal operator entanglement with zero product-input entangling power. The fixed-factor SWAP used here acts inside growing spectators and is not a whole-half SWAP. [Read record](../evidence/checkpoint08/foundation/GENERAL_GATE_LITERATURE.md).

## What these records establish

The [source ledger](../provenance/SOURCE_LEDGER.json) records four targeted primary-page reads on 13 September 2026, including R3, R4 and R8. It includes retrieved-page hashes and explicitly states that original page copies are not bundled. Earlier inspection levels are retained in the linked checkpoint records. A reference above indicates the documented depth of that read; it does not imply a new line-by-line audit of the source's proof.

The inspected literature does not contain a directly located statement of the full fixed-support Haar gate-to-entropy covariance law. This is a bounded search conclusion, not an exhaustive originality guarantee. The contribution assessment and its strongest overlap concerns are in [Publication positioning](../reviews/PUBLICATION_POSITIONING.md). General fluctuation machinery, operator entanglement, the second-moment connection and moment reconstruction are credited antecedents, not proposed new principles.
