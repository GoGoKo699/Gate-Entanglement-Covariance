# What the entropy-memory family identifies

Checkpoint 08 independent mathematical note, 12 September 2026.

This note assumes the fixed-boundary covariance theorem reviewed in checkpoint 07. It supplies a finite algebraic inversion and a deterministic conditioning analysis. It introduces no further Haar simulation and no tomography or experimental-efficiency claim.

## 1. Complete invariant, with finite information

Let `eta(U)` be the nonzero normalized operator-Schmidt probabilities of a boundary gate U. Suppose its rank is at most the known fixed integer R. Pad with zeros to length R, and write

\[
F_k(U)=\sum_{h=1}^R\eta_h(U)^k,\qquad F_1=1.
\]

For natural-log Renyi entropy define the same-order before/after covariance

\[
C_m(U)=\lim_{d\to\infty}d^2\operatorname{Cov}
 [S_m(U\psi),S_m(\psi)],\quad m=2,3,\ldots.
\]

The hypotheses are Haar input, a balanced d by d cut, fixed active boundary factors, and increasing spectators. Both R and every entropy order used below are fixed before d tends to infinity.

**Proposition.** For two such gates with ranks at most R, these statements are equivalent:

1. They have the same nonzero normalized operator-Schmidt spectrum, counting multiplicities.
2. Their limiting entropy covariances agree for every pair of fixed positive orders alpha,beta.
3. Their same-order covariances C_m agree for m=2,...,R.

When R=1 there are no data to collect: normalization already fixes the spectrum to (1).

**Proof and explicit inversion.** Let `Cat_m=binom(2m,m)/(m+1)`. In the polynomial Chebyshev expansion, the coefficient of `Gamma_k(x)=2T_k((x-2)/2)` in x^m is `q_mk=binom(2m,m-k)`. Radial normalization removes k=1. The checkpoint-07 law gives exactly

\[
C_m=\frac{1}{(m-1)^2\mathrm{Cat}_m^2}
 \sum_{k=2}^m k\binom{2m}{m-k}^{\!2}F_k. \tag{1}
\]

Consequently, with `Y_m=(m-1)^2 Cat_m^2 C_m`,

\[
F_m=\frac{Y_m}{m}
-\sum_{k=2}^{m-1}\frac{k}{m}\binom{2m}{m-k}^{\!2}F_k. \tag{2}
\]

The diagonal coefficient is nonzero because q_mm=1. Equations (1)-(2) recover F_2,...,F_R from C_2,...,C_R. Include known F_1=1 and use Newton's identities,

\[
e_0=1,\qquad
e_j=\frac1j\sum_{k=1}^j(-1)^{k-1}e_{j-k}F_k.
\]

Then eta, padded with zeros, is exactly the multiset of roots of

\[
z^R-e_1z^{R-1}+e_2z^{R-2}-\cdots+(-1)^Re_R.
\]

This proves 3 implies 1. Statement 1 implies 2 directly from the checkpoint-07 covariance law, and 2 implies 3 by restriction. No noninteger entropies or mixed-order covariances are needed for this exact identifiability result.

The same conclusion holds if same-order **correlations** are supplied, because their marginal variances are gate independent and explicitly known. Equality of all integer-order covariances also determines any finite spectrum without a supplied R; however, no finite stopping order is asserted in that formulation.

## 2. Explicit result for one boundary qubit per side

Here R<=4. Equation (1) becomes

\[
\begin{aligned}
C_2&=\tfrac12F_2,\\
C_3&=\tfrac{18}{25}F_2+\tfrac{3}{100}F_3,\\
C_4&=\tfrac89F_2+\tfrac{16}{147}F_3+\tfrac1{441}F_4.
\end{aligned}
\]

Thus

\[
\boxed{\begin{aligned}
F_2&=2C_2,\\
F_3&=\tfrac{100}{3}C_3-48C_2,\\
F_4&=441C_4-1600C_3+1520C_2.
\end{aligned}} \tag{3}
\]

The quartic has coefficients

\[
e_1=1,\quad e_2=(1-F_2)/2,\quad
e_3=(1-3F_2+2F_3)/6,
\]
\[
e_4=(1-6F_2+3F_2^2+8F_3-6F_4)/24.
\]

These formulas remain valid at rank one or two through zero roots.

## 3. Correlation normalization and exact noise gains

The limiting marginal variance coefficient is particularly simple for positive integer m>=2:

\[
V_m:=\lim d^2\operatorname{Var}(S_m)=m/4.
\]

For completeness, the identity

\[
\sum_{k=1}^{m}k\binom{2m}{m-k}^{\!2}
=\tfrac m4\binom{2m}{m}^{\!2}
\]

follows by telescoping the difference of successive squared binomials of degree 2m-1. Subtracting the k=1 term, using `q_m1=m Cat_m`, and dividing by `(m-1)^2 Cat_m^2` gives V_m=m/4.

Put `rho_m=C_m/V_m=4C_m/m`. For one boundary qubit per side,

\[
\boxed{\begin{aligned}
F_2&=\rho_2,\\
F_3&=25\rho_3-24\rho_2,\\
F_4&=441\rho_4-1200\rho_3+760\rho_2.
\end{aligned}} \tag{4}
\]

If each input correlation has absolute error at most delta, direct inversion (4) has worst-case absolute moment-error bounds `delta`, `49 delta`, and `2401 delta`, respectively. Each bound is sharp for independent signed input errors, before imposing any physical-spectrum constraints. This is a conditioning statement about this linear inversion, **not a minimax statistical lower bound** and not a claim that every perturbed moment vector is physically valid.

For example, errors bounded by 10^-6 in each correlation permit a 0.002401 error in F_4. At the flat rank-four spectrum F_4=1/64, this is already 15.37% of that moment. Reconstructing the roots may amplify errors further.

The exact rational matrix calculation gives:

| Reconstructed moment | Gain from errors in C_2,...,C_m | Gain from errors in rho_2,...,rho_m |
|---|---:|---:|
| F_2 | 2 | 1 |
| F_3 | 244/3 | 49 |
| F_4 | 3561 | 2401 |
| F_5 | 1016124/5 | 145361 |
| F_6 | 47770046/3 | 11683841 |
| F_8 | 491562858265/2 | 182410990273 |
| F_12 | 3228754002187276091543/3 | 799383499057896186721 |

These are row l1 norms of the exact inverse matrices. The final diagonal coefficient alone is

\[
\frac{(m-1)^2\mathrm{Cat}_m^2}{4}
\sim\frac{16^m}{4\pi m}
\]

in correlation normalization; the full row norms are substantially larger. This already warns against promoting a finite-moment uniqueness theorem into a practical large-rank reconstruction protocol. Redundant mixed-order data, physical constraints, or regularization could help a particular estimator, but none is analyzed here.

There is a second instability at the root step. For simple roots, the first variation obeys

\[
\delta\eta_i=-\frac{\delta P(\eta_i)}{P'(\eta_i)},\qquad
P'(\eta_i)=\prod_{j\ne i}(\eta_i-\eta_j).
\]

Nearly colliding roots therefore cause additional sensitivity. It is present even inside the physical two-qubit set. The family

\[
\eta(h)=(\tfrac14+\tfrac h2,\tfrac14+\tfrac h2,
          \tfrac14-\tfrac h2,\tfrac14-\tfrac h2)
\]

has `||eta(h)-eta(0)||_2=h` but `F_2(h)-F_2(0)=h^2`; all finitely many moments change only at order h^2. There can therefore be no uniform Lipschitz inverse near this physically attainable degeneracy. Rank detection near zero roots likewise needs a resolution criterion.

## 4. Quantum admissibility and limitations of the invariant

Not every probability vector of length four is an operator-Schmidt spectrum of a two-qubit unitary. In particular ranks 1,2,4 are possible and rank 3 is forbidden; see Mueller-Hermes and Nechita, *Operator Schmidt ranks of bipartite unitary matrices*, Linear Algebra and its Applications 557, 174-187 (2018), DOI https://doi.org/10.1016/j.laa.2018.07.018. That paper is cited for this established rank restriction, not for the inversion above.

The three moments nevertheless carry independent information on an open set of actual two-qubit gates. For

\[
U=\exp[i(a X\otimes X+b Y\otimes Y+c Z\otimes Z)],
\]

put `x=cos(2a)`, `y=cos(2b)`, `z=cos(2c)`, and choose an interior region with `0<x<y<z<1`. Expanding the commuting Pauli exponentials gives the four probabilities

\[
\frac14(1+xy+xz+yz),\quad
\frac14(1-xy-xz+yz),\quad
\frac14(1-xy+xz-yz),\quad
\frac14(1+xy-xz-yz).
\]

The Jacobian of `(x,y,z)` to any three independent listed probabilities has absolute determinant `xyz/8`, which is nonzero in the interior. The Jacobian from three independent probabilities to `(F_2,F_3,F_4)` has a nonzero Vandermonde factor when the probabilities are distinct. Thus there is no universal relation eliminating one of those three moments on the physical gate set. Three locally independent real measurements are generically necessary to recover this three-parameter spectrum continuously. This is not a minimality claim about arbitrary nonlinear or discontinuous encodings.

The rational choice `(x,y,z)=(1/5,2/5,3/5)` gives the physical spectrum `(9/25,13/50,1/5,9/50)` and provides an exact inversion check. The near-flat family above is also physical: take `(x,y,z)=(0,2h,1)` with `0<=h<=1/2`.

Even exact recovery of eta does **not** recover U, its operator-Schmidt bases, its action on specified inputs, or its product-input entangling power. The existing SWAP and SWAP-times-ZZ comparison is a direct counterexample. More generally all gates with identical eta are indistinguishable by this entire **limiting before/after entropy covariance family**. This statement does not assert that their finite-d covariances coincide, or that their responses relative to other separately chosen reference gates coincide.

## 5. Assessment

The useful physical corollary is that the entropy-memory hierarchy contains exactly the normalized operator-Schmidt spectrum: purity memory alone collapses the information to F_2, while additional integer orders resolve higher moments. Conversely, the entire hierarchy has an exact information boundary and cannot recover other gate properties.

The proof is elementary triangular inversion plus Newton identities once the covariance theorem is available. It is a clean completeness corollary and may sharpen how the central law is explained. It is not a separate PRL-level mechanism, efficient tomography result, or a reason to expand numerical sampling. The sharp noise growth makes restraint especially appropriate.

The covariance theorem supplies no uniform finite-d bias rate. An experiment or numerical estimator would have to control that bias, the ensemble-covariance uncertainty, and the precision of entropy evaluation. Absolute covariances vanish like d^-2, while suitably rescaled ideal observables have order-one fluctuations; the former observation alone does not prove any particular sample-complexity scaling.

## 6. Reproduction

Run `python inverse_moments.py`. It uses only Python's standard library and writes `inverse_results.json`. It verifies the exact forward/inverse products through rank 12; checks moments and Newton characteristic polynomials for five deterministic spectra, including physical qubit examples; verifies sharp signed-noise bounds; and checks physical near-flat root sensitivity with rational arithmetic. No finite-dimensional entropy prediction or new Haar-state data is generated.
