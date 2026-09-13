# Independent all-degree review of the phase-block polynomial kernel

Completed 2026-09-12. This is a mathematical review of the fixed-degree statement in `POLYNOMIAL_KERNEL.md`, not another numerical test. The previous exact enumeration through degree four is a useful check, but the reasoning below addresses arbitrary fixed degrees.

## Finding

The stated polynomial covariance and joint Gaussian limit follow from the connected Wick quotient graph. The decisive fact is that every leading connected two-trace graph is unicyclic. It rules out an omitted cross-time branch: tree edges necessarily pair entries from the same time, while the unique cycle contains every surviving cross-time phase. The tree counts and cyclic gluing factors reproduce the claimed shifted-Chebyshev diagonalization at every fixed degree.

This supplies an independent internal justification of the all-degree step. Combined with the Hu-based argument already reviewed in `NONSMOOTH_EXTENSION_AUDIT.md`, there is no remaining identified gap in the stated finite-time, finite-dimensional limiting covariance argument. This is an internal derivation and review, not external peer review or a claim that every possible defect has been excluded.

## 1. Quotient graph and power counting

Consider two traces of powers m and n at times t and s. Put `N=m+n`. Each Wick contraction pairs an unconjugated Gaussian entry with a conjugated one. Regard each pair as an edge joining its free row-index vertex to its free column-index vertex. The resulting graph is bipartite and may have parallel edges. Its edges carry the cyclic ordering inherited from the two traces, so it is an orientable ribbon graph.

Each Gaussian edge has two appearances in the trace walks: one unconjugated and one conjugated. The normalization of `W=GG†/d` supplies `d^(-N)`. If the quotient has V free index vertices, its unrestricted index sum is bounded by `d^V`, since every phase has modulus one.

Contractions disconnected between the two trace boundaries cancel against the product of expectations. For a remaining connected contraction, the ribbon Euler relation is

    V-N+2 = 2-2g,

where the two trace walks are the two faces and g is the nonnegative genus. Thus its order is `d^(-2g)`. The leading terms have `V=N`, `g=0`, and exactly one graph cycle because a connected graph has cycle rank `N-V+1=1`.

Equivalently, if gamma contains the two trace cycles and pi is the Wick pairing permutation, the row vertices are cycles of `gamma*pi` and the column vertices are cycles of pi. This is the same convention independently implemented in `annular_polynomial_audit05.py`. The leading condition is `cycles(gamma*pi)+cycles(pi)=N`.

## 2. Why no mixed-time tree branch survives

An edge outside the unique cycle is a bridge: removing it disconnects the graph. Every closed walk traverses a bridge an even number of times, since each crossing between the two components must be followed by a crossing back.

Each Wick edge appears exactly twice in total across the two trace walks. Therefore, if it is a bridge, both appearances must occur in the same trace. Its unconjugated and conjugated entries have the same time label and, after Wick identification, the same row and column indices. Their phase product is exactly one, point by point in the index sum. This is stronger than an average cancellation.

All attached trees consequently have precisely their ordinary complex-Wishart weight. Their vertices can be summed without producing any sign-sector-dependent correction to the backbone.

The remaining cycle is even, with k row vertices and k column vertices. In a planar unicyclic ribbon graph, the cycle separates the two faces; every cycle edge has one appearance in each face. Thus every cycle edge is paired across the two times. The two faces traverse that cycle in opposite directions. Because the graph is bipartite and the Wick pairs are unconjugated against conjugated entries, the phase products alternate between a cross-time entry covariance and its conjugate.

This gives exactly

    product_(ell=1)^k r_(i_ell,j_ell)(t-s)
                         conjugate(r_(i_(ell+1),j_ell)(t-s)),

with cyclic row index `i_(k+1)=i_1`. There is neither a second independently weighted cycle nor a cross-time tree contribution at leading order.

## 3. Cycle average and the ZZ factor

Write `r_ij(tau)=exp(-i tau z_i z_j)` and `R_d=r/d`. Summing the preceding product over the k row and k column vertices, with the normalization supplied by the cycle edges, is exactly

    Tr[(R_d R_d†)^k].

The d-by-d matrix R_d is constant on the two row-sign sectors and two column-sign sectors. Each has exactly d/2 indices. Its only nonzero action is the two-dimensional matrix

    Q(tau) = (1/2) [[exp(-i tau), exp(i tau)],
                    [exp(i tau), exp(-i tau)]].

The eigenvalues of `Q Q†` are `cos(tau)^2` and `sin(tau)^2`, giving

    F_k(tau)=cos(tau)^(2k)+sin(tau)^(2k).

Distinct abstract quotient vertices are summed independently; their numerical indices need not be distinct. The matrix-trace expression therefore already includes all such assignments. If the combinatorial derivation is instead formulated with distinct generic numerical indices, allowing coincidences changes the normalized sum by at most `O(1/d)` at fixed degree because there are finitely many vertices and bounded summands. Neither convention changes the limit.

## 4. Tree decoration counts at arbitrary degree

Fix a backbone cycle with k row and k column vertices. Its boundary on the m-th trace uses 2k of that trace's 2m steps. The remaining `m-k` edges form plane trees attached in the 2k cyclic slots of that face.

Let `C(z)=1+z C(z)^2` be the plane-tree Catalan generating function. With a distinguished cycle starting position, the number of ordered forests with `m-k` tree edges is

    [z^(m-k)] C(z)^(2k)
      = (k/m) binom(2m,m-k).

This coefficient identity follows from the Catalan equation or Lagrange inversion. To convert the distinguished cycle start into the fixed trace start, double count representations: there are m permissible row-starting trace positions and k permissible row-starting cycle positions. Thus the number of decorations associated with a rooted trace boundary is

    q_(m,k) = (m/k) [z^(m-k)] C(z)^(2k)
            = binom(2m,m-k).

The same count holds on the n boundary, and their tree decorations are independent. The two oriented bipartite cycles have k compatible cyclic gluings. All yield the same phase average after relabeling dummy indices. There is no additional reflected gluing factor: the complex ensemble pairs only unconjugated with conjugated entries, with `E[GG]=0`.

Consequently, for arbitrary fixed m,n,

    lim Cov(Tr W(t)^m, Tr W(s)^n)
      = sum_(k=1)^min(m,n) k q_(m,k) q_(n,k) F_k(t-s).

The same coefficients occur in the exact polynomial identity

    x^m=binom(2m,m)+sum_(k=1)^m q_(m,k) Gamma_k(x),
    Gamma_k(x)=2 T_k((x-2)/2).

Inverting this triangular identity gives the claimed diagonal covariance

    lim Cov(Tr Gamma_j(W(t)),Tr Gamma_k(W(s)))
      = delta_jk k F_k(t-s).

The low-degree enumeration is consistent with, but not needed to replace, this all-degree count.

## 5. Higher cumulants

For r fixed trace factors at arbitrary fixed times, the cumulant expansion retains the connected Wick ribbon graphs joining all r trace boundaries. Their Euler relation gives

    V-E = 2-r-2g.

Phase weights remain bounded by one, and for fixed trace degrees there are only finitely many Wick contractions. Every cumulant of order r>=3 is therefore `O(d^(2-r))` and tends to zero. Second cumulants have the covariance derived above; first cumulants are removed by centering. Wick expansion supplies convergence of the corresponding moments, and the Gaussian moment sequence is determinate. Applying this to finite linear combinations yields the joint Gaussian limit for any fixed finite collection of polynomial traces and times, including degenerate covariance matrices.

This part does not require tree reduction for higher-r graphs. The genus bound and bounded phase factors are enough.

## 6. Exact scope of the conclusion

The polynomial degrees, number of observables, and time values are fixed before the dimension limit. The argument is specific to the complex Gaussian/Haar ensemble and the stated deterministic phase-block probe. The tree cancellation works because the two occurrences of a bridge are at one time; the cycle evaluation uses the actual ZZ block phases.

The reviewed marginal approximation extends this result to fixed positive Rényi orders and finite sets of fixed times. Taking the short-time limit of that limiting covariance is then justified by its displayed convergent series. This does not supply a finite-size convergence rate, a limit uniform in a shrinking time increment, functional-process tightness, sample-path regularity, or generalization to arbitrary Hamiltonian dynamics. Those limitations remain substantive and should be retained.
