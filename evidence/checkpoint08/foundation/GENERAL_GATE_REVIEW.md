# General finite-boundary gates: independent all-degree review

12 September 2026. This note independently tests the extension beyond diagonal gates. It is a mathematical derivation, not a numerical fit or an originality assessment. It uses the earlier project only for the standard tree counts and the already reviewed marginal LUE approximation. The new step is the full boundary-index contraction for a non-diagonal unitary.

## Finding

The extension works for **arbitrary deterministic unitaries on fixed boundary factors**, with balanced spectator dimensions tending to infinity. Diagonality is unnecessary. The leading annular contraction is the trace of a power of the gate's normalized realignment Gram matrix. Equivalently, it is the corresponding power sum of its normalized operator-Schmidt probabilities.

The formula fails for a whole-half SWAP with growing active dimensions, as already documented. That counterexample does not apply to a fixed-dimensional boundary SWAP. Fixed boundary support is an essential hypothesis in the present argument.

## 1. Precise setting and normalization

Fix positive integers r,s. Let d tend to infinity through common multiples of r,s. Write

    A = C^r tensor C^(d/r),
    B = C^s tensor C^(d/s).

Use boundary labels a,c in {1,...,r}, b,e in {1,...,s}, and spectator labels i in {1,...,d/r}, j in {1,...,d/s}. Let G be a d by d matrix of independent standard complex Gaussian entries, with E|G_ai,bj|^2=1. For a fixed deterministic unitary U on C^r tensor C^s, define

    G_U[ai,bj] = sum_(c,e) U[ab,ce] G[ci,ej],
    W_U = G_U G_U^dagger / d.

The normalized vector of entries of G gives the Haar initial pure state. Its evolved reduced density matrix is rho_U=W_U/T, where

    T = Tr W_U = ||G||_F^2/d

is exactly independent of U for each realization.

For any fixed list U_1,...,U_L, put V_lm=U_l U_m^dagger. The joint Gaussian entry covariance is

    E[G_Ul[ai,bj] conjugate(G_Um[ck,ev])]
      = delta_ik delta_jv V_lm[ab,ce].                    (1)

There are no unconjugated-unconjugated covariances. At equal labels l=m, unitarity reduces (1) to the full identity covariance. Thus each G_Ul is exactly an independent-entry standard complex Gaussian matrix marginally, even though the different matrices are correlated.

Define the realignment matrix of V by

    R(V)[(a,c),(b,e)] = V[ab,ce],
    Q(V) = R(V)/sqrt(rs).

The nonzero eigenvalues eta_h(V) of Q Q^dagger are the normalized operator-Schmidt probabilities of V. This follows directly by using the matrix units |a><c| and |b><e| as Hilbert-Schmidt orthonormal operator bases. Since V is unitary,

    sum_h eta_h = Tr(V V^dagger)/(rs) = 1.

Write F_k(V)=sum_h eta_h(V)^k.

## 2. Statement for polynomial modes

With Gamma_k(x)=2 T_k((x-2)/2), for each fixed pair j,k>=1,

    lim_(d to infinity) Cov(Tr Gamma_j(W_Ul),
                           Tr Gamma_k(W_Um))
      = delta_jk k F_k(V_lm).                            (2)

Consequently the convention using T_k alone has covariance delta_jk (k/4)F_k. Confusing these two mode normalizations would introduce a factor-four error.

The centered polynomial traces have a joint Gaussian limit for every fixed finite collection of degrees and gates. They need not have independent values at distinct gates. At a fixed k the matrix with entries F_k(U_l U_m^dagger) is positive semidefinite because it is a limit of covariance matrices; this is also a useful consistency check on any proposed implementation.

## 3. Why the spectator Wick graph has the usual topology

Expand two traces of degrees m,n and use Wick's rule with (1). The Kronecker deltas join **spectator** row and column indices exactly as in the ordinary complex Wishart calculation. The boundary labels carry finite tensors and are not initially identified across a cross-gate Wick edge. This distinction is what a diagonal-entry proof cannot silently omit.

For N=m+n factors of W, let a connected spectator quotient ribbon graph have V_r row vertices and V_c column vertices. Its spectator sums contribute

    (d/r)^V_r (d/s)^V_c,

while the W normalization contributes d^(-N). The remaining active-index tensor contraction is a finite sum depending on r,s and the fixed degrees. It is bounded independently of d because r,s are fixed and each unitary entry has magnitude at most one.

As usual, the product of expectations cancels contractions disconnected between the two traces. For each connected graph the orientable ribbon Euler identity is

    (V_r+V_c)-N+2 = 2-2g.

The graph is therefore O(d^(-2g)). Its leading terms have genus zero and V_r+V_c=N. They are connected and unicyclic. No additional leading graph class is created by a non-diagonal boundary tensor: the topology and d power are controlled by spectator indices.

## 4. Tree reduction uses unitarity, not diagonality

Every edge outside the unique cycle is a bridge. Each edge has exactly two appearances across the two closed trace walks. A closed walk must traverse a bridge an even number of times, so both appearances of a bridge are in the same trace. They consequently have the same gate label.

Equation (1) for a same-gate pair is precisely

    delta_ik delta_jv delta_ac delta_be.

The boundary contraction along a bridge is thus the ordinary identity contraction. Peel the attached tree from its leaves. A row leaf supplies r boundary choices times d/r spectator choices, hence exactly d; a column leaf similarly supplies s times d/s=d. The remaining identities identify the two active legs at the parent exactly as in the ordinary Wishart tree reduction. Inductively every attached tree has the usual weight and leaves no boundary operator on the cycle.

There is no assumption that a non-diagonal U has diagonal entry covariance between different gates. Cross-gate edges are confined to the annular cycle at this order; same-gate unitarity removes the trees.

## 5. Explicit all-degree cycle contraction

The planar unicyclic backbone contains k spectator row vertices and k spectator column vertices. Every backbone edge separates the two trace faces and is paired across the two gates. The two trace walks traverse the backbone in opposite directions.

Each backbone spectator row vertex now carries two active labels, a_l for one trace and c_l for the other; likewise each spectator column vertex carries b_l,e_l. After tree removal the active contraction is

    sum_(a_1,...,a_k;c_1,...,c_k;b_1,...,b_k;e_1,...,e_k)
      product_(l=1)^k V[a_l b_l,c_l e_l]
                conjugate(V[a_(l+1) b_l,c_(l+1) e_l]),    (3)

where a_(k+1)=a_1 and c_(k+1)=c_1. Expression (3) is exactly

    Tr[(R(V) R(V)^dagger)^k].

The backbone spectator sums and its 2k factors of 1/d supply

    (d/r)^k (d/s)^k d^(-2k) = (rs)^(-k).

The normalized weight is consequently

    Tr[(R(V)R(V)^dagger/(rs))^k] = F_k(V).              (4)

This directly identifies the realignment operation and every normalization factor. It also rules out a partial-transpose spectrum or an extra SWAP term in this fixed-boundary limit. Such terms cannot be added on the basis of growing-dimension gate intuition.

## 6. Tree decorations and higher cumulants

For a degree-m trace with backbone half-length k, the standard rooted plane-tree count is

    q_(m,k)=binom(2m,m-k).

One derivation uses C(z)=1+z C(z)^2 and

    (m/k) [z^(m-k)] C(z)^(2k)=binom(2m,m-k).

The two trace decorations are independent and the backbone admits k compatible cyclic gluings in the complex ensemble. Their weights are all (4), after dummy-index relabeling. Thus

    lim Cov(Tr W_Ul^m, Tr W_Um^n)
      = sum_(k=1)^min(m,n) k q_(m,k) q_(n,k) F_k(V_lm).

Use the exact identity

    x^m = binom(2m,m) + sum_(k=1)^m q_(m,k) Gamma_k(x)

and invert this triangular relation to obtain (2).

For p>=3 traces the Gaussian cumulant expansion retains only Wick graphs connected across all p trace boundaries. The spectator Euler relation now gives

    V_r+V_c-N = 2-p-2g.

At fixed active dimensions and fixed trace degrees each active-index contraction is bounded by a d-independent constant. The cumulant is O(d^(2-p)), and vanishes. The polynomial moment method, or Cramer-Wold applied to these cumulants, gives the finite-dimensional joint Gaussian limit. This argument is insensitive to whether different U_l commute.

## 7. Radial mode and the entropy extension

F_1(V)=1 for every unitary. The k=1 mode is Gamma_1(x)=x-2, and

    Cov(Tr W_Ul,Tr W_Um)=Var(T)=1

exactly at finite d. This conserved radial mode must be removed when passing from Gaussian W to normalized Haar rho. It is not a gate-dependent entropy-memory contribution.

The marginal approximation used in the project continues to apply without any change: each W_U has exactly the square-LUE law. In particular Hu's variance-convergence and approximation result for low-regularity LUE statistics applies to a smooth upper cutoff of x^alpha for every fixed alpha>0, and to x log x. The hard-edge corner integral reduces to an integrable factor integral_0^delta x^(2alpha-1) dx; Gaussian upper-edge tails remove the upper cutoff. The source is Henry Hu, *On the regularity conditions in the CLT for the LUE*, arXiv:2310.08509v1, Theorem 1.1, Lemma 1.2 and Corollary 1.3, https://arxiv.org/html/2310.08509v1. The square ensemble is covered by its fixed nonnegative integer rectangularity parameter.

The needed transfer is purely marginal. If p_N approximates a test function f in the limiting LUE variance seminorm, then

    lim_(N to infinity) limsup_(d to infinity)
      ||X_d(f,U_l)-X_d(p_N,U_l)||_2 = 0,

where X_d denotes a centered trace statistic. A fixed finite linear combination across gates is bounded by the sum of these marginal errors. Cauchy-Schwarz transfers pair covariances, and polynomial approximation transfers the finite-dimensional Gaussian limit. No independence across gates, scalar-entry correlation formula, or new joint nonsmooth theorem is required.

The existing L2 entropy delta method is also unchanged. Put

    M_alpha = Gamma(2alpha+1)/[Gamma(alpha+1)Gamma(alpha+2)].

For alpha!=1 the centered entropy obeys

    d(S_alpha(U)-E S_alpha)
      = X_d(x^alpha,U)/[(1-alpha)M_alpha]
        - alpha(T-d)/(1-alpha) + o_L2(1).

The k=1 cosine coefficient of x^alpha is 2alpha M_alpha, so the trace term cancels it. The von Neumann case follows by the x log x version. Using c_(alpha,k) as defined in the existing diagonal theorem, for any fixed alpha,beta>0,

    lim d^2 Cov(S_alpha(U_l), S_beta(U_m))
      = (1/4) sum_(k>=2) k c_(alpha,k)c_(beta,k) F_k(U_l U_m^dagger).

The series is absolutely convergent by Cauchy-Schwarz in the LUE variance seminorm. For a same-order increment relative to identity this gives

    lim d^2 E[(S_alpha(U)-S_alpha(I))^2]
      = (1/2) sum_(k>=2) k c_(alpha,k)^2 [1-F_k(U)].

This extension inherits the exact qualifications of the original marginal proof, including use of the combined normalized entropy to bound exceptional events in the logarithmic delta method. No new exceptional event is created by the gate.

## 8. Controls and physical consequences within scope

**Product gate.** If U=A tensor B, realignment has one singular value sqrt(rs), so eta=(1) and every F_k=1. All entanglement increments vanish exactly, as they must.

**Fixed boundary SWAP.** If r=s=q is fixed and U swaps just these q-dimensional boundary factors, R(U) is a q^2 by q^2 permutation matrix. Thus eta has q^2 equal entries 1/q^2, and F_k=q^(2-2k). In particular the limiting normalized Renyi-2 memory is 1/q^2. The global cut also contains increasing spectators, so this unitary does not preserve the Schmidt spectrum across the full cut. There is no contradiction with the zero-increment whole-half SWAP.

**Whole-half SWAP.** Taking r=s=d breaks the fixed-active-dimension estimate. The active tensor sums can then change the d power of the spectator topology, and suppressed contraction classes may survive. Its exact zero increment cannot be inserted into the fixed-r,s theorem.

**Local basis changes.** Pre- and postmultiplication of a single relative gate by product unitaries preserves its realignment singular values and hence the limiting covariance. In the Haar-pair formulation this invariance is exact even before taking d large, because input local unitaries can be absorbed into the Haar state and output local unitaries preserve its entanglement. This does not imply that arbitrary local terms can be deleted from a noncommuting Hamiltonian at finite times.

**Rank bound.** The realignment rank is at most min(r^2,s^2), giving F_k>=min(r^2,s^2)^(1-k). Therefore fixed local support imposes a positive residual limiting memory; the arbitrary-gate rank ceiling differs from the diagonal family ceiling min(r,s).

**Different gates at different times.** The correct pair kernel is the operator-Schmidt power sum of U(t)U(s)^dagger. For a time-independent boundary Hamiltonian this is U(t-s), giving stationarity. For a driven boundary sequence one cannot replace it by a function only of the separately listed spectra of U(t) and U(s), nor assume time-translation invariance.

## 9. Review conclusion and remaining limits

The non-diagonal step has an all-degree proof under the fixed-support limit. An independent finite-degree contraction program remains worthwhile to catch index-order mistakes in (3); such a program is a check on the derivation, not its logical replacement.

The work supports promoting the fixed-diagonal theorem to a theorem about arbitrary deterministic unitaries on fixed boundary factors. The central physical restriction is fixed spatial access in the spectator limit, not diagonal dynamics. The proof also covers a fixed finite collection of gates, including noncommuting choices, through their relative gates.

It does not establish uniform finite-dimension error rates, growing support, polynomial degrees increasing with d, time intervals shrinking with d, a sample-path process limit, Gaussian instantaneous entropy rates, physically prepared-state universality, or a publication-level novelty claim. Those claims require separate arguments.
