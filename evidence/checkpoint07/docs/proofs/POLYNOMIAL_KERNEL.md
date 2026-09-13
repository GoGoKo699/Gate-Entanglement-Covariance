# Fixed-polynomial covariance for the ZZ phase-block trajectory

Current status update: ALL_DEGREE_REVIEW.md now independently justifies the arbitrary fixed-degree contraction argument. Combined with NONSMOOTH_EXTENSION_AUDIT.md, no remaining internal gap has been identified in the fixed-time covariance and finite-dimensional Gaussian limit. Earlier references below to a pending all-degree review record the argument's development. No external peer review or uniform finite-size claim is implied.

Status: analytical derivation at fixed polynomial degrees. Independent exact Wick enumeration confirms every mode pair through degree four; see annular_polynomial_audit05.py and its JSON record. The subsequent NONSMOOTH_EXTENSION.md uses Hu (2023) to extend fixed-time covariance and finite-dimensional convergence to every fixed positive Rényi order. A functional process limit remains unproved.

## Statement

Let d be even, G a d-by-d matrix of independent standard complex Gaussian variables, and z_i in {+1,-1} with each sign occurring d/2 times. Define

    G(t)_ij = exp(-it z_i z_j) G_ij,
    W(t)=G(t)G(t)^dagger/d.

For k>=1 define Gamma_k(x)=2 T_k((x-2)/2), where T_k(cos theta)=cos(k theta). Additive constants in Gamma_k are irrelevant. For fixed positive integers k,l and fixed times s,t,

    lim_(d to infinity) Cov(Tr Gamma_k(W(t)), Tr Gamma_l(W(s)))
       = delta_kl k F_k(t-s),

    F_k(t)=cos(t)^(2k)+sin(t)^(2k).

More generally, any finite collection of centered traces of fixed-degree polynomials at fixed times has a joint Gaussian limit, with the preceding covariance. The degrees, number of times, and time values are held fixed in this statement. No uniformity in degree is asserted.

For real polynomial functions written as

    f(2+2cos theta)=a_0(f)+sum_(k>=1) a_k(f) cos(k theta),

the covariance is equivalently (1/4) sum_k k a_k(f)a_k(h)F_k(t-s).

## 1. Wick expansion and the leading connected diagrams

The entry covariances are exact:

    E[G(t)_ij conjugate(G(s)_uv)]
       =delta_iu delta_jv r_ij(t-s),
    r_ij(tau)=exp(-i tau z_i z_j),
    E[G(t)_ij G(s)_uv]=0.

Expand each trace power as an alternating closed row-column walk. Complex Gaussian Wick pairing identifies row indices with row indices and column indices with column indices. Subtracting the product of the two expectations removes diagrams which do not connect the two trace boundaries. For fixed powers m,n, the connected diagrams with the largest number of free indices are the usual planar annular diagrams; all others have fewer free indices and vanish after division by d^(m+n).

This power counting is unchanged by r_ij: every added phase has modulus one, so weighting an index assignment cannot increase its order in d. The standard enumeration of the leading complex-Wishart annular diagrams can therefore be reused with phase weights attached to their through-connections.

Any tree attached entirely to one trace boundary contains only equal-time entry contractions. Such contractions have r_ij(0)=1. Summing its internal indices consequently gives exactly the ordinary Wishart tree weight. Removing all attached trees leaves a cycle which alternates between the two trace boundaries.

For a through-cycle with k row vertices and k column vertices, the time-dependent weight is

    L_k(tau)=lim_(d to infinity) d^(-2k)
      sum_(i_1,...,i_k;j_1,...,j_k)
      product_(ell=1)^k r_(i_ell,j_ell)(tau)
                         conjugate(r_(i_(ell+1),j_ell)(tau)),

where i_(k+1)=i_1. The original leading diagrams require distinct generic free vertices; allowing repeated vertices changes the normalized sum only by O(1/d) for fixed k because the summands are bounded. This replacement permits the matrix trace formula below.

There are k cyclic ways to glue the two oriented cycles in the complex Gaussian case. Their phase weights coincide after relabeling the dummy indices. This yields the factor k L_k(tau). There is no additional real-ensemble reflected contribution because the anomalous Gaussian covariance E[GG] is zero.

## 2. Evaluation of the cycle weight

Set R_d(tau)_ij=r_ij(tau)/d. The unrestricted cycle sum is exactly

    Tr[(R_d R_d^dagger)^k].

The matrix R_d is constant on the four sign blocks and has rank at most two. On the normalized vectors uniform in the + and - sectors, its nonzero action is

    Q(tau)=(1/2)[[exp(-i tau),exp(i tau)],
                 [exp(i tau),exp(-i tau)]].

The eigenvalues of Q Q^dagger are cos(tau)^2 and sin(tau)^2. Consequently

    L_k(tau)=Tr[(Q Q^dagger)^k]=F_k(tau).

This derivation depends on the actual ZZ phases, not on replacing the family by a scalar-correlated Gaussian interpolation.

## 3. Removing the trees by Chebyshev polynomials

At aspect ratio one the exact polynomial identity is

    x^m = binom(2m,m)
          +sum_(k=1)^m binom(2m,m-k) Gamma_k(x).

The coefficients q_(m,k)=binom(2m,m-k) count the same planar tree attachments that leave k through-connections on one annular boundary. Their weights are unchanged here because every attached tree stays at one time. Therefore the leading trace-power covariance is

    lim Cov(Tr W(t)^m,Tr W(s)^n)
       =sum_(k=1)^min(m,n) k q_(m,k)q_(n,k)F_k(t-s).

Inverting the triangular polynomial identity removes these attachments and gives the stated diagonal covariance for Gamma_k.

The standard Wishart annular expansion and its Chebyshev diagonalization are established prior tools; see Kusalik, Mingo, Speicher, *Orthogonal Polynomials and Fluctuations of Random Matrices*, J. Reine Angew. Math. 604 (2007), 1-46, https://arxiv.org/abs/math/0503169 . The extension performed here is retaining the sector-dependent phase weight on the surviving through-cycle. For an independent verification, enumerate the Gaussian pairings for small m,n directly instead of assuming the diagonal result.

## 4. Higher cumulants

A connected diagram joining r fixed trace boundaries has order at most d^(2-r) in the usual complex Gaussian genus count. Sector phases are bounded by one, so the same upper bound applies term by term. Thus cumulants of order r>=3 vanish for each fixed collection of trace powers. Wick expansion also controls their moments. Together with the limiting covariance this yields finite-dimensional Gaussian convergence for fixed polynomials, allowing degenerate covariance matrices.

This argument does not establish tightness as a process in time or uniform control for a polynomial degree growing with d.

## 5. Low-degree consequences and checks

The first identities are

    x=2+Gamma_1,
    x^2=6+4Gamma_1+Gamma_2,
    x^3=20+15Gamma_1+6Gamma_2+Gamma_3,
    x^4=70+56Gamma_1+28Gamma_2+8Gamma_3+Gamma_4.

Hence the candidate limits which a direct pairing enumeration should reproduce include

    Cov(Tr W(t),Tr W(s))=1,
    Cov(Tr W(t)^2,Tr W(s)^2)=16+2F_2,
    Cov(Tr W(t)^2,Tr W(s)^3)=60+12F_2,
    Cov(Tr W(t)^3,Tr W(s)^3)=225+72F_2+3F_3,
    Cov(Tr W(t)^4,Tr W(s)^4)=3136+1568F_2+192F_3+4F_4.

For normalized states, the leading entropy fluctuation subtracts the trace mode. For alpha=2 the resulting fluctuation has only Gamma_2, with coefficient -1/2. Thus

    lim d^2 Cov(S_2(t),S_2(s))=F_2(t-s)/2,
    lim d^2 E[(S_2(t)-S_2(s))^2]=1-F_2(t-s)=sin(2(t-s))^2/2.

Its short-time coefficient is 2, matching the conditional derivative-variance limit independently obtained from Haar Schmidt bases.

## 6. Exact boundary of this derivation

The preceding result justifies a fixed-polynomial mode kernel. It does not on its own justify inserting an infinite Chebyshev series for x^alpha at the hard edge, differentiating that series, or taking a time increment to zero after d tends to infinity.

The subsequent NONSMOOTH_EXTENSION.md supplies the marginal L2 approximation using Hu, arXiv:2310.08509, checks its assumptions at the hard edge for every positive Rényi order, and explains trace normalization and the entropy delta-method. This closes the previously identified nonsmooth-function gap, conditional on the all-degree polynomial derivation above. It also makes the small-time powers consequences of the limiting covariance series, with the dimension limit taken first.

The all-degree annular reasoning should still receive independent mathematical review; the exact low-degree enumeration verifies examples rather than every degree. No process tightness, sample-path regularity theorem, or uniform finite-size rate is asserted.
