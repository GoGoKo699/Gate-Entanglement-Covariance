# Diagonal boundary gates organize equilibrium entropy memory

12 September 2026. Bounded extension of checkpoint 05. This note generalizes its reviewed phase-block Wick argument, rather than proposing a new random-matrix theorem. No originality claim is made. All entropies use natural logarithms.

## 1. Setting and statement

Fix positive integers r,s and a real array h=(h_ab). Let d tend to infinity through multiples of r and s. Each half has dimension d, with a boundary factor of dimension r on A and s on B and spectator factors of dimensions d/r and d/s. The initial pure state is Haar distributed on C^d tensor C^d. Apply only

    U(t) = exp(-it H),
    H = sum_(a,b) h_ab |a><a| tensor |b><b|,

with spectator identities understood. These boundary dimensions and H are held fixed in the limit. Put

    P(t)_ab = exp(-it h_ab),
    Q(t) = P(t)/sqrt(rs),
    eta_l(t) = eigenvalues of Q(t) Q(t)^dagger,
    F_k(t) = sum_l eta_l(t)^k.

The nonzero eta_l are the normalized operator-Schmidt probabilities of U(t). In particular, sum_l eta_l=1 and F_1=1 exactly.

Let W(t)=G(t)G(t)^dagger/d, where G has independent standard complex Gaussian entries and each entry acquires the phase associated with its two boundary labels. For Gamma_k(x)=2 T_k((x-2)/2), every fixed pair of positive degrees obeys

    lim Cov(Tr Gamma_j(W(t)), Tr Gamma_k(W(s)))
      = delta_jk k F_k(t-s).

The fixed-time joint Gaussian limit also extends from checkpoint 05. Thus every Chebyshev mode has a memory factor given by a power sum of the gate's operator-Schmidt spectrum. This is an equilibrium ensemble covariance, not a claim that the entropy of an individual state is determined by that spectrum.

## 2. Why the extension follows

The Gaussian entry covariance remains diagonal in the full row and column indices:

    E[G(t)_ij conjugate(G(s)_uv)]
      = delta_iu delta_jv exp[-i(t-s) h_(a(i),b(j))].

The leading connected two-trace Wick quotient is unicyclic. Every edge outside its cycle is a bridge, whose two appearances must belong to the same closed trace walk. Its phases cancel exactly. Consequently every attached tree has the ordinary Wishart weight, with no boundary-label dependence.

The remaining cycle with k row and k column vertices has weight

    d^(-2k) sum_(i_1,...,i_k;j_1,...,j_k)
       product_l P_(a(i_l),b(j_l))(tau)
                 conjugate(P_(a(i_(l+1)),b(j_l))(tau)).

This is Tr[(R_d R_d^dagger)^k], with R_d,ij=P_(a(i),b(j))/d. Compressing R_d to vectors uniform on each boundary-label sector gives exactly P/sqrt(rs): the normalization factor is sqrt[(d/r)(d/s)]/d. The cycle weight is therefore F_k.

The tree-decoration counts and k cyclic gluings are unchanged. Inverting the usual shifted-Chebyshev triangular identity gives the displayed diagonal covariance. Connected higher cumulants still vanish by the fixed-degree genus bound, since all entry phases have modulus one.

The normalized operator U/d has the orthonormal operator bases Pi_a/sqrt(d/r), Pi_b/sqrt(d/s), where Pi denotes a boundary projector with spectator identity. Its coefficient matrix is P/sqrt(rs). This establishes the operator-Schmidt interpretation, including every dimension factor.

## 3. Entropy normalization and the complete covariance

At every time the state is exactly Haar, so entropy means and marginal variances are stationary. Also Tr W(t) is the same random variable at every time, not a separately sampled trace.

Let M_alpha be the square Marchenko-Pastur moment,

    M_alpha = Gamma(2alpha+1) / [Gamma(alpha+1) Gamma(alpha+2)].

For alpha not equal to one and k>=2, define

    c_(alpha,k) = 2 Gamma(2alpha+1) /
      [Gamma(alpha+k+1) Gamma(alpha-k+1) (1-alpha) M_alpha].

At alpha=1 take the continuous limit. Reciprocal Gamma zeros implement terminating series at integer alpha>1. These are the cosine coefficients of the leading normalized-entropy fluctuation. Trace normalization cancels k=1. It must not be retained as an extra entropy memory term.

The checkpoint-05 marginal L2 approximation applies unchanged: each W(t) has exactly the same square-LUE marginal law, and a finite-time covariance is controlled by marginal approximation errors. Hence, for all fixed positive alpha,beta,

    lim d^2 Cov(S_alpha(t),S_beta(s))
      = (1/4) sum_(k>=2) k c_(alpha,k)c_(beta,k) F_k(t-s).

For one order,

    V_alpha(tau) := lim d^2 E[(S_alpha(tau)-S_alpha(0))^2]
      = (1/2) sum_(k>=2) k c_(alpha,k)^2 [1-F_k(tau)].

The sum is convergent for every fixed alpha>0. This is the full covariance including its nonzero static value; the increment is twice the static variance minus twice the temporal covariance. The dimension limit precedes any short-time limit.

## 4. Local terms and the small-time interaction strength

Adding a row function, a column function, and a constant to h multiplies Q(t) on its left and right by diagonal unitaries and a global phase. The eta_l and every F_k are invariant. Physically those additions commute with H and contribute only local unitaries, which preserve the Schmidt spectrum at every time for every initial state.

Define the doubly centered interaction

    h^c_ab = h_ab - (1/s) sum_b' h_ab'
                   - (1/r) sum_a' h_a'b
                   + (1/rs) sum_a',b' h_a'b',

and

    chi = (1/rs) sum_(a,b) (h^c_ab)^2.

Thus chi is the normalized squared Hilbert-Schmidt strength after removing additive local terms. It is zero exactly when H is additive across this cut. In that case U(t) is local and all entropy increments vanish identically.

For chi>0, the largest operator-Schmidt probability is simple near zero and

    eta_1(t)=1-chi t^2+O(t^4),
    sum_(l>=2) eta_l(t)=chi t^2+O(t^4).

To verify the coefficient, work in the centered gauge. Write u=1/sqrt(r), v=1/sqrt(s), K=h^c/sqrt(rs). Then Q(0)=uv^T, K v=0 and K^dagger u=0. The first perturbation of QQ^dagger vanishes; the second has u-expectation -chi. The simple largest eigenvalue is analytic and even, because Q(-t)=conjugate(Q(t)). This also gives the O(t^4) remainder. Minor probabilities are O(t^2).

For every fixed k>=2,

    F_k(t)=1-k chi t^2+O(t^4).

That fixed-k expansion alone is insufficient below alpha=1/4; the infinite sum must be treated before differentiating.

## 5. The quarter-order crossover persists

For noninteger alpha>0 the large-k coefficient has magnitude

    |c_(alpha,k)| ~ A_alpha k^(-1-2alpha),
    A_alpha = 2 Gamma(2alpha+1)|sin(pi alpha)| /
              [pi |1-alpha| M_alpha],

with its continuous interpretation at alpha=1. The low-order asymptotics only need 0<alpha<=1/4.

Let z=-log eta_1(t)=chi t^2+O(t^4). The total contribution of the minor eta_l^k to the increment-series asymptotics is O(t^4): for small t, their summed kth powers are bounded by [1-eta_1(t)]^k and k>=2. The singular term is consequently the same sum as in checkpoint 05 with exp(-kz). It yields

    0<alpha<1/4:
      V_alpha(t) ~ (A_alpha^2/2)
        [Gamma(1-4alpha)/(4alpha)] chi^(4alpha) |t|^(8alpha),

    alpha=1/4:
      V_alpha(t) ~ A_alpha^2 chi t^2 log(1/|t|),

    alpha>1/4:
      V_alpha(t) ~ (chi/2) [sum_(k>=2) k^2 c_(alpha,k)^2] t^2.

For the last line, dominated convergence is valid because the coefficient sum converges and 1-F_k is bounded by a constant times k t^2 near zero. Positive integer orders are included by their terminating series.

Thus a nonzero diagonal interaction changes the short-lag coefficient but not the crossover order or exponent. Below one quarter the coefficient is proportional to chi^(4alpha), as required by rescaling the Hamiltonian. The limiting statement does not include alpha=0 and is not uniform as alpha approaches zero.

## 6. Two compact physical corollaries

At order two, c_(2,2)=-1 and all higher coefficients vanish. Therefore

    lim d^2 Cov(S_2(t),S_2(0)) = F_2(t)/2,
    V_2(t)=1-F_2(t).

The limiting Pearson correlation of the equilibrium Renyi-2 entropy is exactly the gate's normalized operator purity. Its mean-square increment equals the linear entropy of that operator-Schmidt spectrum. This refers to normalized entropy fluctuations in the specified Haar limit, not to the mean state entanglement produced by the gate.

If m=min(r,s), then rank Q<=m and F_k>=m^(1-k). In particular, the Renyi-2 memory is at least 1/m. A fixed diagonal gate can therefore leave a nonzero equilibrium covariance even when its operator entanglement is maximal within this diagonal family.

For r=s=2, every h is additive local terms plus J Z tensor Z. This is just the original ZZ case with chi=J^2, not a genuinely larger interaction family. More Schmidt channels require min(r,s)>=3.

An exact three-channel hand check is h_ab=ab for a,b in {0,1,2}. Here h^c_ab=(a-1)(b-1) and chi=4/9. At t=2pi/3, P is the unnormalized three-dimensional Fourier matrix, so eta=(1/3,1/3,1/3), F_k=3^(1-k), and V_2=2/3. This example requires only a three-level boundary factor on each side and fixed spectators; no many-body simulation is involved.

## 7. Matched Hamiltonians separate energy spectra from entropy memory

A four-level boundary factor on each side permits the following two diagonal Hamiltonians:

    h_A = outer((1,-1,1,-1),(1,1,-1,-1)),

    h_B = [[ 1, 1,-1,-1],
           [ 1,-1,-1, 1],
           [-1,-1, 1, 1],
           [-1, 1, 1,-1]].

Both have eight +1 and eight -1 diagonal energies, norm one, zero row and column means, and chi=1. With identical spectator dimensions, their full Hamiltonian spectra including multiplicities also agree. Their local Hilbert-Schmidt interaction strength and every leading short-lag law in Section 5 consequently agree.

Because each entry is +1 or -1,

    Q_X(t)=cos(t) J/4 - i sin(t) h_X/4.

The centered h_X has row and column singular subspaces orthogonal to the uniform vectors. Its singular values therefore enter independently of the rank-one J term. The matrix h_A has one nonzero singular value 4. For h_B,

    h_B=u_1 v_1^T+u_2 v_2^T,
    u_1=(1,0,-1,0), u_2=(0,1,0,-1),
    v_1=(1,1,-1,-1), v_2=(1,-1,-1,1).

The u vectors are orthogonal with squared norm two; the v vectors are orthogonal with squared norm four. Hence h_B has two singular values sqrt(8). Exactly,

    eta_A=(cos(t)^2, sin(t)^2),
    eta_B=(cos(t)^2, sin(t)^2/2, sin(t)^2/2),

    F_k^A=cos(t)^(2k)+sin(t)^(2k),
    F_k^B=cos(t)^(2k)+2^(1-k) sin(t)^(2k).

At t=pi/2, U_A is a product of local diagonal unitaries times a global phase. Every initial state therefore has exactly zero entanglement increment. At the same time U_B has two equal operator-Schmidt probabilities, giving

    V_2^A(pi/2)=0,      V_2^B(pi/2)=1/2,
    C_2^A(pi/2)=1/2,    C_2^B(pi/2)=1/4,

where C_2=lim d^2 Cov(S_2(t),S_2(0)). At t=pi/4 the corresponding increments are 1/2 and 5/8.

More generally,

    V_alpha^B(t)-V_alpha^A(t)
      = (1/2) sum_(k>=2) k c_(alpha,k)^2
          [1-2^(1-k)] sin(t)^(2k) >= 0.

This is a matched demonstration of the theorem: equal Hamiltonian energy spectra and equal initial interaction strength do not determine finite-time entropy memory. It is not an independent novelty claim, and the return of U_A to a product gate makes its zero increment transparent. Its purpose is to connect the covariance formula to a controlled distinction at an ordinary entropy order, while keeping the low-order crossover separate.

These are fixed interactions across two four-level boundary factors, equivalently two qubits on each side. h_B is not being advertised as one nearest-neighbor two-qubit coupling. Its larger boundary support is part of the declared model.

## 8. Full-spectrum content beyond operator purity

### Majorization orders every same-order entropy memory

Compare any two gates covered by this theorem at specified times, and pad their operator-Schmidt probability vectors eta and xi with zeros to a common length. If eta majorizes xi, then convexity of x^k gives

    F_k(eta) >= F_k(xi),  k>=2.

Every coefficient in a same-order entropy autocovariance is nonnegative. Hence, for every alpha>0,

    C_alpha(eta) >= C_alpha(xi),
    V_alpha(eta) <= V_alpha(xi),

where C is the limiting rescaled entropy autocovariance and V the limiting rescaled mean-square increment. The marginal variances are gate independent, so the same ordering holds for normalized autocorrelations. A gate spectrum made more uniform in the majorization sense reduces memory for every positive Renyi order in this ensemble limit.

If the two probability vectors are not permutations and majorization holds, strict convexity gives F_2(eta)>F_2(xi). Since

    c_(alpha,2)=-2alpha/(alpha+2) != 0

for every alpha>0, both displayed inequalities are strict. This comparison is pointwise in the selected gates or times; it does not order entire trajectories unless the majorization premise holds throughout them. It is not asserted for mixed-order covariances, whose coefficient products need not all be positive.

### Equal operator purity can hide strictly different memory at every other order

This is a second comparison, separate from the equal-energy-spectrum control in Section 7. Use two qubits on each side of the cut and gates

    U_A = exp[-i (pi/4) Z_(A1) Z_(B1)],
    U_C = exp[-i theta Z_(A1) Z_(B1)]
          exp[-i theta Z_(A2) Z_(B2)],

where

    p=cos(theta)^2=(1+sqrt(sqrt(2)-1))/2,
    q=1-p.

The two factors in U_C act on disjoint crossing pairs. Their normalized operator-Schmidt spectra therefore multiply, giving

    eta_A=(1/2,1/2,0,0),
    eta_C=(p^2,pq,pq,q^2),
    F_k^A=2^(1-k),
    F_k^C=(p^k+q^k)^2.

Our choice makes p^2+q^2=1/sqrt(2), so both gates have exactly F_2=1/2. Their limiting Renyi-2 entropy autocovariances are therefore both 1/4, and their mean-square increments both 1/2. This comparison matches the selected gate operator purity, not the Hamiltonian energy spectrum, strength, or duration.

Nevertheless,

    F_k^C > F_k^A for every integer k>2.

An elementary proof avoids fitting or truncation. Let X take the values p and q with probabilities p and q. Then E X=p^2+q^2=1/sqrt(2). For k>2, strict Jensen convexity gives

    p^k+q^k = E X^(k-1) > (E X)^(k-1).

Squaring gives the claimed inequality. In particular,

    F_3^C=(11-6sqrt(2))/8 > 1/4=F_3^A.

The complete entropy covariance formula now implies

    C_alpha(U_C) > C_alpha(U_A),
    V_alpha(U_C) < V_alpha(U_A),

for every fixed alpha>0 except alpha=2. Strictness follows already from k=3, since

    c_(alpha,3)=-2alpha(alpha-2)/[(alpha+2)(alpha+3)]

is nonzero throughout that range except at alpha=2. For alpha=1 its continuous value is 1/6, so von Neumann entropy is included. At alpha=2 the expansion contains only k=2 and the memories agree exactly.

For example, the Renyi-3 autocovariance difference is the closed expression

    C_3(U_C)-C_3(U_A)=9(3-2sqrt(2))/800 > 0.

This sharpens the full-spectrum claim: two gates can be indistinguishable by this order-two entropy-memory measurement but distinguishable by every other positive Renyi order. The difference is not claimed to be large for all orders.

The two operator spectra in this example are incomparable by majorization: eta_C has the larger first partial sum, while eta_A has the larger second partial sum. Thus this example uses the explicit power-sum inequalities just proved, not a false application of the preceding majorization corollary. It adds no general claim that ordering one scalar operator-entanglement measure orders entropy memory.

## 9. Scope and counterexample discipline

The proof establishes fixed diagonal boundary Hamiltonians with fixed active dimensions as spectator dimensions grow. It does not establish the same formula for arbitrary non-diagonal gates, even if a further extension could exist. In particular it should not be described as a theorem about every gate solely from its operator entanglement, or as an equivalence to an out-of-time-order correlator.

A whole-half SWAP illustrates why unrestricted wording is false. On C^d tensor C^d it preserves every state's Schmidt spectrum exactly, so all entropy increments are zero and normalized mode memory is one. Its normalized operator-Schmidt spectrum has d^2 equal weights 1/d^2, whose kth power sum is d^(2-2k), tending to zero for k>=2. Substituting those weights would give the wrong answer. This example has active dimensions growing with d and is outside the fixed-local-dimension limit. It is therefore not a counterexample to a possible fixed-local non-diagonal theorem; that case is simply not proved in this note.

No functional-process tightness, sample-path regularity, finite-size error rate, uniform shrinking-time limit, physically prepared-state universality, or publication-level originality claim is added here. The existing LUE and Chebyshev fluctuation results remain essential prior foundations.
