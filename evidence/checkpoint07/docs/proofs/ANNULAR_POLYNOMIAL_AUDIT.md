# Post-protocol audit of the proposed finite-pulse covariance

This is a bounded analytical followup developed after the original experiment. It is not part of the prospectively specified checkpoint protocol. It checks the proposed transfer-matrix result directly for polynomial degrees through four, without assuming an annular diagonalization theorem or extrapolating to nonanalytic Rényi functions.

## Exact result of the enumeration

Let `W(0)=GG†/d`, where G is a balanced d by d standard complex Gaussian matrix, and set `G(t)_ij=exp(-it a_i b_j)G_ij`, with equal numbers of Pauli signs `a_i=±1` and `b_j=±1`. Let `P_k(W)=Tr T_k((W-2I)/2)`, where T_k is the ordinary first-kind Chebyshev polynomial.

Enumerating all Gaussian Wick pairings for every pair of trace powers `p,q=1,...,4` gives, at leading order as d grows,

    Cov(P_j(W(0)), P_k(W(t)))
      = delta_jk (k/4) [cos(t)^(2k) + sin(t)^(2k)],   1<=j,k<=4.

The equality was verified as an exact Fourier polynomial for every time t: after expressing both sides with the common integer denominator 1024, the maximum discrepancy of any Fourier coefficient is exactly zero. This is symbolic finite combinatorial verification, not a Monte Carlo comparison or a fit at selected times.

Raw trace-power covariances contain mixed contributions. They combine into the diagonal expression after changing to the shifted Chebyshev basis. Thus mixed cycles do not invalidate the proposed formula through degree four.

## Method

Write each trace power as a cyclic product of a matrix entry and its conjugate. For total degree `n=p+q`, a Gaussian Wick contraction is a permutation pi pairing n unconjugated entries with n conjugated entries. Let gamma be the permutation containing the two trace cycles. Its free row indices are the cycles of `gamma*pi`, and its free column indices are the cycles of pi.

Pairings that preserve the two trace blocks cancel against the product of expectations. A remaining connected contraction contributes order `d^(nr+nc-n)`, where nr and nc count those free row and column indices. The leading covariance terms have `nr+nc=n`.

For each such contraction, assign an independent equiprobable Pauli sign to every free row and column index. The phase of the second trace is then an integer multiple of t. Average that phase exactly over all `2^(nr+nc)` assignments, retain its full Fourier histogram, and sum over the leading connected contractions.

The counts of leading contractions are:

| p against q | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| 1 | 1 | 4 | 15 | 56 |
| 2 | 4 | 18 | 72 | 280 |
| 3 | 15 | 72 | 300 | 1200 |
| 4 | 56 | 280 | 1200 | 4900 |

The largest enumeration examines all `8!=40320` pairings. No diagram class was selected according to the proposed answer. Conversion from monomials to the four shifted Chebyshev polynomials is exact rational arithmetic, implemented as integers with a common denominator.

## Relation to normalized pure states and remaining limits

Dividing the Gaussian state by its norm fixes `Tr(d rho)=d`. At leading order, this removes the fluctuating k=1 mode. For k>=2, the relevant normalization correction vanishes because the Marchenko–Pastur integral of `x d[T_k((x-2)/2)]/dx` is zero. The checked higher modes therefore support the candidate normalized-Haar linear-statistic expression.

For the purity-derived order-two entropy, only k=2 remains after normalization. Its coefficient gives the proposed large-d result

    d^2 Var[S_2(t)-S_2(0)] -> (1/2) sin(2t)^2.

The calculation does not prove the formula for arbitrary polynomial degree, although its agreement through degree four and the free-index phase structure support the transfer-matrix interpretation. More importantly, it does not justify interchanging the infinite Chebyshev expansion, the large-d limit, and the short-time limit for `x^alpha` at the zero spectral edge. Those are the substantive gaps before using this result as a Rényi finite-time covariance theorem or claiming a fractional short-time law.

Reproduce with `python annular_polynomial_audit05.py`. The complete exact coefficients and diagram counts are saved in `annular_polynomial_audit05.json`.
