# Independent audit: exact unitary 2-designs with different entropy memory

12 September 2026. Bounded analytical review by the inverse-memory subagent. No new state samples or optimized gate search are used here. The pair is a post-exploration analytical construction, not a prospectively frozen numerical hypothesis.

**Finding:** the proposed pair is sound. Its locally randomized gate ensembles are exact unitary 2-designs, while their limiting before/after Renyi-3 entropy correlations differ by `3 sqrt(5)/20000`. The entangling-power convention in the cited design paper differs by a factor three from this project's convention for active qubits and must be translated explicitly.

## 1. Fixed gates and exact operator moments

Use the Cartan form

\[
U=\exp[-i(c_1XX+c_2YY+c_3ZZ)],\qquad
u_i=\cos^2(2c_i),\quad 0\le c_i\le\pi/4.
\]

All selected u_i lie strictly between zero and one, so one may take `c_i=(1/2)arccos(sqrt(u_i))`. No particular ordering of the three commuting Pauli terms is necessary. A convention using `exp[-i(theta_i/2) sigma_i sigma_i]` instead has theta_i=2c_i.

For `x_i=sqrt(u_i)`, direct expansion of the three commuting Pauli exponentials gives the normalized operator-Schmidt probabilities

\[
\tfrac14(1+x_1x_2+x_1x_3+x_2x_3),\quad
\tfrac14(1-x_1x_2-x_1x_3+x_2x_3),
\]
\[
\tfrac14(1-x_1x_2+x_1x_3-x_2x_3),\quad
\tfrac14(1+x_1x_2-x_1x_3-x_2x_3).
\]

Therefore, writing `s_2=sum_{i<j}u_i u_j` and `t=u_1u_2u_3`,

\[
F_2(U)=\frac{1+s_2}{4},\qquad
F_3(U)=\frac{1+3s_2+6t}{16}. \tag{1}
\]

Multiplication by active SWAP replaces the u_i by 1-u_i for these invariants: its Cartan shift is pi/4 in each coefficient, and `cos^2(pi/2±2c_i)=1-u_i`.

The pair is

\[
u_A=(\tfrac12+\sqrt{3/20},\tfrac12,\tfrac12-\sqrt{3/20}),
\]
\[
u_B=(\tfrac12+\sqrt{1/20},\tfrac12+\sqrt{1/20},\tfrac12-2\sqrt{1/20}).
\]

Both have `sum u_i=3/2` and `s_2=3/5`. Their complementary pair sums are also 3/5, because `sum_{i<j}(1-u_i)(1-u_j)=3-2 sum_i u_i+s_2`. Thus

\[
F_2(U_A)=F_2(U_B)=F_2(PU_A)=F_2(PU_B)=2/5.
\]

Their products are

\[
t_A=1/20,\qquad t_B=1/20-\sqrt5/100.
\]

Equation (1) gives

\[
F_3(U_A)-F_3(U_B)=3\sqrt5/800>0. \tag{2}
\]

The active product-input **unnormalized linear-entropy** entangling power is e_p=1/5 for both gates, and gate typicality is g_t=1/2.

## 2. Why each local-randomization ensemble is an exact 2-design

Independently sample four single-qubit Haar unitaries and form

\[
\widetilde U=(v_1\otimes v_2)U(v_3\otimes v_4).
\]

The second moment of this ensemble is a known function of entangling power and gate typicality. A primary source checked for this audit is Suzuki et al., *More global randomness from less-random local gates*, arXiv:2410.24127v3 (26 August 2026), Section III.2, Eq. (25): https://arxiv.org/html/2410.24127v3 .

**Convention translation:** that source uses `e_u=(q+1)/(q-1) e_p`, hence e_u=3e_p=3/5 for q=2. Its Haar values are e_H=3/5 and g_H=1/2. In its orthonormal local-twirl basis, the source's second-moment matrix becomes

\[
\begin{pmatrix}
1/10&0&0&3/10\\
0&1/2&1/2&0\\
0&1/2&1/2&0\\
3/10&0&0&9/10
\end{pmatrix}.
\]

Both two-by-two blocks are rank-one orthogonal projectors. Their ranges are precisely the global identity and swap invariants. Input and output local twirls remove the orthogonal complement of the four-dimensional local invariant space. Thus the full moment operator equals the global Haar second-moment projector, proving that each ensemble is an exact unitary 2-design.

The parent workspace's full two-copy-superoperator calculation provides a separate deterministic numerical check. This audit does not count that calculation as newly run here.

## 3. Haar-input memory survives the local randomization

For any fixed input/output product rotations L and R, output L preserves entanglement across the full A|B cut, while input R preserves the before-gate entropy. The substitution `chi=R psi` leaves the global Haar distribution unchanged. Therefore the joint pair

\[
(S_\alpha(LUR\psi),S_\alpha(\psi))
\]

has exactly the same distribution as `(S_alpha(U chi),S_alpha(chi))`, at every finite spectator dimension and for every defined entropy order. Mixing over independent local rotations preserves that equality. The same statement holds jointly for the two exchanged cuts, because each active single-factor rotation is local with respect to either assignment.

The operator-Schmidt spectrum is also unchanged under local pre/post rotations, so the limiting covariance theorem applies identically to every gate drawn from each ensemble. There is no extra covariance from the gate draw: the conditional entropy means are the same Haar means for every fixed gate.

## 4. Exact entropy-memory separation

The already established integer-order covariance law has marginal variance coefficient V_3=3/4 and

\[
\rho_3(U)=\frac{24F_2(U)+F_3(U)}{25}.
\]

Combining this with (2) gives the claimed limiting correlation difference

\[
\boxed{\rho_3(U_A)-\rho_3(U_B)=\frac{3\sqrt5}{20000}
\simeq0.0003354102.}
\]

The corresponding scaled covariance difference is `9 sqrt(5)/80000`, because V_3=3/4. The order convention and normalization agree with the parent's formulas.

The pair proves a difference at the ordinary positive integer order three. A von Neumann or order-one-half separation is not needed to establish the counterexample. The parent's noninteger-order evaluations can be reported as deterministic evaluations of the limiting series, but this note supplies no separate exact sign proof for those differences.

## 5. Interpretation and limitations

Every averaged gate polynomial of bidegree at most (2,2), including all usual second-moment diagnostics, agrees between these two ensembles and global Haar gates on the active factors. Their third-order operator moments and resulting entropy-memory correlations need not agree. This does not contradict the definition of a 2-design: it does not constrain higher-order observables.

The useful point is an explicit entanglement-memory quantity that distinguishes two exact 2-designs under the same globally Haar initial-state ensemble. A claim that second moments generally fail to determine higher moments would be elementary and should not be framed as a new discovery. The quantitative memory law, the physical usefulness of that observable, and the novelty relative to known higher-moment diagnostics remain the substantive questions.

These local gate ensembles are exact 2-designs **on the two active qubits**. Embedding them with identity spectators does not create a global unitary 2-design on the entire d by d system. Haar randomness of the initial state is an independent assumption. All entropy correlation equalities above use the fixed-boundary large-spectator limit unless finite-d distributional invariance was explicitly stated.
