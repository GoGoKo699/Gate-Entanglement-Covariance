# Focused literature review: general boundary gates

12 September 2026. Primary-source screening for the proposed extension from fixed diagonal gates to arbitrary fixed bipartite boundary gates. Read against project 06 `docs/reviews/NOVELTY_REVIEW.md` and `docs/proofs/DIAGONAL_GATE_THEORY.md`. This is a literature and significance review, not an independent proof of the extension. Six primary papers anchor the assessment. No new numerical campaign was run for this review.

## Assessment

The closest additional mathematical predecessor is **Diaz, Mingo, and Belinschi's block-Gaussian fluctuation theory**. General finite boundary gates mix a finite array of Gaussian blocks, so this is closer to the proposed extension than a scalar-correlated temporal Wishart process. Existing mathematics already supplies the general language of weighted annular contractions and matrix-valued covariance. A proof that the physical gate reduces this machinery to its operator-Schmidt power sums would be the substantive simplification, not a new Gaussian fluctuation theory.

The closest quantum antecedents remain the operator-entanglement/bipartite-OTOC identity and the two sets of gate invariants associated with realignment and partial transpose. The latter give an important warning: familiar product-input entangling power depends on both the operator spectra of U and U composed with SWAP. They do **not** by themselves settle which invariants survive the different globally Haar, fixed-boundary, large-spectator covariance considered here.

No direct prior statement of the complete all-positive-order equilibrium entropy covariance in this setting was located in the checked sources. Search non-detection does not establish originality. The PRL assessment remains conditional on the proof and on a concise physical consequence of this reduction.

## Sources and inspected claims

### 1. Mingo and Speicher: general weighted annular machinery

James A. Mingo and Roland Speicher, *Second Order Freeness and Fluctuations of Random Matrices: I. Gaussian and Wishart matrices and cyclic Fock spaces*.

- Stable text: https://arxiv.org/html/math/0405191v3
- Abstract/PDF: https://arxiv.org/abs/math/0405191v3 ; https://arxiv.org/pdf/math/0405191v3
- Inspected: Theorem 3.5, its cumulant calculation, Sections 8.3 and 9.

**Source claim.** Theorem 3.5 gives leading cumulants for compound Wishart traces as sums over annular/noncrossing permutations, weighted by cyclic moments of deterministic matrix labels. Section 8.3 specializes fluctuation diagonalization to the Poisson/Wishart case. Section 9 relates Gaussian and constant matrices at second order.

**Our inference.** A finite quantum boundary index is a deterministic matrix label, so proving arbitrary-gate covariance by a colored Wick expansion is an application or specialization of established second-order machinery. The source does not state that quantum-gate contractions depend only on realignment singular values. Its formulas also show why that simplification requires a derivation: generic weights retain cyclic products of labels.

### 2. Kusalik, Mingo, and Speicher: mode diagonalization

Timothy Kusalik, James A. Mingo, and Roland Speicher, *Orthogonal Polynomials and Fluctuations of Random Matrices*.

- Stable text: https://arxiv.org/html/math/0503169v1
- Abstract/PDF: https://arxiv.org/abs/math/0503169v1 ; https://arxiv.org/pdf/math/0503169v1
- Inspected: introduction's theorem and its annular half-permutation interpretation, including the distinction between polynomial degree and the number of through-blocks.

**Source claim.** Shifted first-kind Chebyshev polynomials diagonalize single-Wishart trace fluctuations. The combinatorial proof identifies the mode number with surviving open/through-blocks; the paper also treats cyclically alternating statistics of independent Wishart matrices.

**Our inference.** This is the natural source for the unchanged tree-decoration/Chebyshev part of a general-gate proof. It does not itself identify the weight left on a through-cycle by a fixed local quantum gate. Equal single-time Wishart marginals alone do not imply diagonal cross-time covariance.

### 3. Diaz, Mingo, and Belinschi: the closest additional framework

Mario Diaz, James Mingo, and Serban Belinschi, *On the Global Fluctuations of Block Gaussian Matrices*, Probability Theory and Related Fields 176 (2020), 599–648.

- Inspected arXiv text: https://arxiv.org/html/1711.07140v1
- Abstract/PDF: https://arxiv.org/abs/1711.07140v1 ; https://arxiv.org/pdf/1711.07140v1
- Published DOI: https://doi.org/10.1007/s00440-019-00925-1
- Inspected: Definition 1, Theorem 2 and equations (5)–(6), introductory linearization discussion and stated annular-pairing structure. This was not a line-by-line audit of the full proof.

**Source claim.** For a fixed number of Gaussian blocks with a general covariance mapping, the paper gives the matricial second-order Cauchy transform and its scalar trace covariance. Linearization extends the approach to selfadjoint noncommutative polynomials and rational functions of Gaussian matrices.

**Our inference.** Hermitization of the Gaussian coefficient matrix is a plausible bridge to this framework. A finite collection of input and gate-transformed blocks should admit such a formulation after checking the exact complex covariance conventions. This is a framework-level comparison, not an assertion that the paper's theorem can be substituted without adaptation. It makes the novelty of the fluctuation machinery especially limited while leaving the gate-specific collapse to one operator spectrum a potentially useful physical result.

### 4. Kuan and Zhou: temporal Wishart fluctuations already exist

Jeffrey Kuan and Zhengye Zhou, *Three-dimensional Gaussian fluctuations of spectra of overlapping stochastic Wishart matrices*.

- Stable text: https://arxiv.org/html/2112.13728v1
- Abstract/PDF: https://arxiv.org/abs/2112.13728v1 ; https://arxiv.org/pdf/2112.13728v1
- Inspected: Section 1.2 assumptions, Theorem 1.1 and the opening of the closed-walk proof.

**Source claim.** Entries evolve as stochastic processes, not necessarily Markovian; an explicit covariance describes the limiting joint Gaussian field of polynomial trace statistics of overlapping Wishart matrices. Entry moment and cross-time assumptions are imposed uniformly across matrix indices.

**Our inference.** The general boundary gate changes the cross-time covariance into a finite tensor rather than one homogeneous scalar entry-correlation function. The source therefore blocks novelty claims about temporal Wishart Gaussian fields but does not directly establish the proposed gate kernel. Its assumptions should not be quoted as automatically covering correlated real and imaginary components produced by complex block mixing.

### 5. Styliaris, Anand, and Zanardi: order-two overlap

Georgios Styliaris, Namit Anand, and Paolo Zanardi, *Information Scrambling over Bipartitions: Equilibration, Entropy Production, and Typicality*, Physical Review Letters 126, 030601 (2021).

- Stable text: https://arxiv.org/html/2007.08570v3
- Abstract/PDF: https://arxiv.org/abs/2007.08570v3 ; https://arxiv.org/pdf/2007.08570v3
- Inspected: Theorems 1–2, equations (4)–(5), and the surrounding ensemble interpretation.

**Source claim.** The bipartite averaged OTOC has an exact doubled-space swap expression and equals linear operator entanglement. The relation to product-input entangling power uses the quantities for U, U composed with the subsystem SWAP, and SWAP itself.

**Our inference.** If the general-boundary extension yields the proposed order-two memory, its mean-square increment equals an already established operator-entanglement/OTOC quantity in the stated limit. The novelty cannot be that order-two quantity itself. Converting its full operator spectrum into every entropy's equilibrium memory is the candidate contribution; it is a different input ensemble and observable from the theorem in this source.

### 6. Jonnadula et al.: two gate spectra and the SWAP caution

Bhargavi Jonnadula, Prabha Mandayam, Karol Życzkowski, and Arul Lakshminarayan, *Entanglement measures of bipartite quantum gates and their thermalization under arbitrary interaction strength*.

- Stable text: https://arxiv.org/html/1909.08139v2
- Abstract/PDF: https://arxiv.org/abs/1909.08139v2 ; https://arxiv.org/pdf/1909.08139v2
- Inspected: Section II.1–II.2, equations (5)–(23), and the distinction between product-input entangling power and gate typicality.

**Source claim.** The operator-Schmidt spectra of U and US provide two sets of local invariants. Their purities are expressible through realignment and partial transpose. Product-input entangling power combines both. SWAP has maximal operator entanglement but zero product-input entangling power; dual-unitary gates have a flat realignment spectrum.

**Our inference.** A theorem retaining only U's operator spectrum would be informative precisely because this need not characterize other state-entanglement questions. SWAP is a required scope test. A fixed boundary-factor SWAP inside large spectators and a SWAP of the whole balanced halves are different limits. The paper does not provide the proposed equilibrium entropy covariance for either embedding.

## What must change in the diagonal argument

The following are our derivational checks, not results quoted from the papers.

Write the initial coefficient array as Gaussian blocks G_ab indexed by the finite active factors, with large spectator indices mu,nu. For a general gate,

    G'_ab(mu,nu) = sum_cd U_ab,cd G_cd(mu,nu),
    E[G'_ab(mu,nu) conjugate(G_cd(mu',nu'))]
      = delta_mu,mu' delta_nu,nu' U_ab,cd.

The spectator Kronecker deltas remain; the active-index covariance is now a four-index tensor. Same-time independent Gaussian marginals follow from unitarity, but cross-time entrywise phases no longer cancel automatically. A sound extension must show:

1. Leading connected spectator contractions have the asserted annular topology, with no additional leading families lost because active loops have fixed dimension.
2. Same-time tree contractions reduce by the correct unitarity identities, independently of the remaining active cycle labels.
3. The remaining active cycle contracts to `Tr[(R(U) R(U)^dagger/(rs))^k]`, where `R(U)_(a,c),(b,d)=U_(a,b),(c,d)`.
4. No partial-transpose or alternative orientation invariant survives at the same spectator order, and the Chebyshev transform removes every off-diagonal mode covariance.
5. Shared trace normalization removes mode one, and the already checked marginal low-regularity argument remains sufficient for the finite collection of entropy covariances.

The fixed-boundary condition is essential. A whole-half SWAP preserves the Schmidt spectrum of every input, while its operator purity tends to zero. That counterexample invalidates unrestricted global-gate wording regardless of what a fixed-local-gate theorem proves.

## Compact significance test

If the extension holds, the useful headline is a quantitative correspondence: **one finite boundary operation determines the memory of every equilibrium entanglement statistic through the spectrum of its operator state**. Ordinary entropy orders and the equal-purity/different-memory example should carry the explanation; the low-alpha temporal exponent remains a supporting consequence.

One particularly clean additional consequence would be that all fixed-dimensional dual-unitary boundary gates have the same limiting spectral and entropy memory, despite their different product-input entangling powers. A boundary SWAP would then be a useful illustration, rather than an exception. This is a proposed corollary conditional on the extension, not a claim established by this literature review. It connects the result to a recognized gate class and avoids a broad many-body simulation campaign.

The result would still describe rescaled Haar-equilibrium fluctuations with growing inactive spectators. It would not by itself describe generic quenches, thermal states, long circuits with growing support, or experimentally efficient entropy-memory estimation. Whether the correspondence is broad enough for PRL remains an editorial and originality question; adding more Gaussian samples would not settle it.

## Search record and limitations

Both search engines were used on 12 September 2026. Queries covered operator-Schmidt entropy covariance, Haar purity covariance under a fixed unitary, entanglement autocorrelation, operator-spectrum memory, annular Wishart contractions, and block Gaussian fluctuations. A separate search used a 365-day recency filter. Several exact-phrase searches were weak or irrelevant; these failures were not treated as evidence of novelty. Primary papers were opened and the sections listed above checked. Friesen–Löwe–Stolz's dependent-data Wishart paper was also opened but is not needed as a seventh anchor because the block-Gaussian framework is more directly relevant to the extension.

No exhaustive forward-citation search, external expert review, or originality certification was performed. The existing project-06 review remains the source for the broader entropy-fluctuation and low-regularity literature; this note supplements that record for the general-gate discriminator.
