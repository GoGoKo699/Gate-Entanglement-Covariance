# Independent audit of the two-cut formulas

12 September 2026. Independent inverse-memory subagent review. The audit reads the two-cut proposal and the two finite-purity implementations, derives the mode formulas separately, and checks the algebra with exact sparse-polynomial arithmetic. No new state samples were generated.

**Finding:** the proposed exact finite-purity sum and difference correlations are correct under the stated equal-dimension, globally Haar, boundary-gate assumptions. The asymptotic entropy extension has the right matrix structure and normalization. The difference-mode identity requires a nonzero spectator space beyond dimension one. Neither the finite-purity theorem nor its numerical checks alone proves an exact finite-d entropy identity.

## 1. Definitions that must remain visible

There are two active factors a,b of dimension q>=2 and two spectator factors A0,B0 of dimension n. Set d=qn and D=d^2. The two balanced subsystems are A=A0a and C=A0b. C need not be a contiguous spatial region. A gate U acts on a,b and identity acts on spectators. The input is Haar on the full D-dimensional pure-state space.

Let P exchange a,b, and define

\[
a=\mathcal P_{\rm op}(U),\qquad b=\mathcal P_{\rm op}(PU),
\]

where these operator purities refer to active q by q factors and use normalized operator-Schmidt weights. The overloading of a,b as both subsystem labels and scalar invariants is harmless in a proof but should be removed in reader-facing prose, for example by using f and g for the scalars.

The active product-input linear-entropy entangling power and gate typicality are

\[
e_p=\frac{q^2}{(q+1)^2}(1+q^{-2}-a-b),\qquad
g_t=\tfrac12\left(1-\frac{a-b}{1-q^{-2}}\right).
\]

The first formula must not silently become a product-input average over the full d-dimensional halves.

## 2. Global finite-purity identity used in the audit

For any unitary V on a d by d system, let f and f_S be the normalized operator purities of V and VS_d, where S_d exchanges the full halves. A Haar four-copy moment gives

\[
\mathbb E[P_A(V\psi)P_A(\psi)]
=\frac{4d^6+16d^4+2d^4(f+f_S)}
{d^2(d^2+1)(d^2+2)(d^2+3)}.
\]

The 24 permutation traces have four disconnected-pair terms d^6, sixteen terms d^4, two realignment terms d^4 f, and two exchanged realignment terms d^4 f_S. The four disconnected permutations preserve each of the two purity-copy pairs. The two realignment pair exchanges identify the boundary indices into the operator-purity contraction; the alternating pair exchanges supply VS_d. The remaining contractions remove V against V-dagger by unitarity. This is the appropriate fourth-moment identity; inserting only f and dropping f_S at finite d would be incorrect.

Using

\[
\mathbb E P_A=\frac{2d}{D+1},\qquad
v:=\operatorname{Var}(P_A)=\frac{2(D-1)^2}{(D+1)^2(D+2)(D+3)},
\]

centering gives the exact correlation

\[
r(V)=\frac{D[(D+1)(f+f_S)-4]}{(D-1)^2}. \tag{1}
\]

The supplied exact-global-purity calculator independently contracts these 24 terms on its declared gate list. This audit does not count rerunning that implementation as new evidence; it verifies the centering of the displayed identity by exact polynomial arithmetic.

## 3. Embedding the active gate

Embedding U with identity spectators leaves its operator purity equal to a. The full swap is the product of the active swap P and the spectator swap. Therefore the operator-Schmidt spectrum of the embedded U times the full swap is the tensor product of the spectrum of UP and a flat spectrum of rank n^2. Its purity is b/n^2. Left versus right active multiplication by P does not matter for this spectrum, because conjugating by P exchanges the two tensor factors.

Write r(a,b) for the same-cut correlation. Equation (1) yields

\[
r(a,b)=\frac{(D+1)(Da+q^2b)-4D}{(D-1)^2}. \tag{2}
\]

The crossed-cut correlation is r(b,a), and the static correlation between the two cuts is

\[
r_0=\frac{(D+1)(D/q^2+q^2)-4D}{(D-1)^2}. \tag{3}
\]

The before/after covariance matrix of the two purities is consequently

\[
v\begin{pmatrix}r(a,b)&r(b,a)\\r(b,a)&r(a,b)\end{pmatrix},
\]

and the marginal covariance matrix is the same matrix at U=I, with diagonal v and off-diagonal vr_0.

## 4. Exact sum and difference modes

Set Y_+=P_A+P_C and Y_-=P_A-P_C. Their before and after variances are equal by global Haar invariance. The correlations are thus

\[
\rho_+=\frac{r(a,b)+r(b,a)}{1+r_0},\qquad
\rho_-=\frac{r(a,b)-r(b,a)}{1-r_0}.
\]

Define

\[
H=(q^2+1)D^2+(q^4+1-6q^2)D+q^2+q^4.
\]

Direct simplification gives exactly

\[
\boxed{\rho_+=1-\frac{(q+1)^2(D+1)(D+q^2)}{H}\,e_p,}
\]

\[
\boxed{\rho_-=\frac{a-b}{1-q^{-2}}=1-2g_t\quad(n>1).}
\]

The sum-mode variance is

\[
\operatorname{Var}(Y_+)=
\frac{4H}{q^2(D+1)^2(D+2)(D+3)}.
\]

The difference-mode variance is

\[
\operatorname{Var}(Y_-)=
\frac{4(D-q^2)(q^2-1)}{q^2(D+1)(D+2)(D+3)}.
\]

This expression proves positivity for q>=2,n>1 and proves exact degeneracy at n=1. At n=1, P_A=P_C state by state, so assigning any finite correlation to Y_- would be erroneous. The cancellation producing rho_- divides by `(D-q^2)`, and therefore cannot extend to that case by substitution.

The sum denominator is positive for all q>=2,n>=1 because

\[
H=(q^2+1)(D-q^2)^2+(q^2-1)(3q^2-1)(D-q^2)
+2q^2(q^2-1)^2.
\]

The exact squared-change formula may be easier to interpret than a normalized correlation:

\[
\boxed{\mathbb E[(Y_+(U\psi)-Y_+(\psi))^2]
=\frac{8(q+1)^2(D+q^2)}{q^2(D+1)(D+2)(D+3)}\,e_p.}
\]

It is an equality of uncentered increments, since before and after means agree. The coefficient reduces to the global two-part formula when n=1 and has the stated spectator limit.

## 5. Entropy cross symmetry and normalization

At every finite dimension, `S_{alpha,C}(psi)=S_{alpha,A}(P psi)`. The four covariance entries are therefore functions of U, UP, PU, and PUP in the natural row/column ordering. Their limiting reduction to the symmetric matrix in the proposal is correct: PVP exchanges the two active tensor factors, leaving the operator-Schmidt spectrum unchanged.

There is also a direct finite-dimensional symmetry argument for the matrix form. Let W swap the two full d-dimensional halves. For a pure state, entropy across A is unchanged by W, and WUW=PUP for an active-only gate. Haar invariance then gives the same diagonal and crossed-entry equalities without an asymptotic assumption. This symmetry alone does not evaluate the entries for nonpolynomial entropies.

For fixed positive orders, the checkpoint-07 law evaluates those limiting entries as kappa(U) and kappa(PU). The mode correlations are

\[
M_{\alpha,\pm}=
\frac{\kappa_{\alpha\alpha}(U)\pm\kappa_{\alpha\alpha}(PU)}
{\kappa_{\alpha\alpha}(I)\pm\kappa_{\alpha\alpha}(P)}.
\]

The factor of two in the mode covariance cancels the corresponding factor of two in the variance. In particular `kappa_22(V)=f_op(V)/2` gives

\[
M_{2,+}=1-\frac{(q+1)^2}{q^2+1}e_p,
\qquad M_{2,-}=1-2g_t.
\]

For the entropy sum, the limiting scaled squared change is

\[
\lim_{n\to\infty}d^2\mathbb E[(X_{2,+}(U\psi)-X_{2,+}(\psi))^2]
=2\frac{(q+1)^2}{q^2}e_p.
\]

This factor agrees independently with the exact purity-increment formula and the entropy delta method `delta S_2=-(d/2)delta P+o_L2(d^-1)`.

**Critical distinction:** `S_{2,A}+S_{2,C}=-log(P_A P_C)`, which is not a function of `P_A+P_C` alone. Accordingly the exact finite-purity sum formula must not be advertised as an exact finite-d Renyi-2 entropy sum formula. The same caution applies to the difference. Only their large-spectator correlations have been linked here.

## 6. Claim and interpretation limits

- This is a valid bridge from fluctuations of globally entangled Haar inputs to a gate's active product-input entangling power. It is not evidence that an initially Haar state gains mean entanglement.
- The difference mode is an entanglement-assignment observable associated with exchanging a,b. Its correlation is gate typicality. It is not a measured transport current, transport velocity, or generic separation of physical transport and entanglement generation in many-body Hamiltonians.
- q, the support, and the entropy orders remain fixed in the limiting entropy theorem. The exact purity identities need no spectator limit, but retain equal dimensions and Haar input.
- Gates within a full half can cross the alternate subsystem C. Changing the allowed gate support changes the physical interpretation.
- The identities use known operator-purity and entangling-power invariants. Whether the equilibrium-fluctuation reformulation is a sufficiently useful contribution for PRL remains a novelty/significance question, not a mathematical question settled by this audit.

## 7. Audit evidence

`two_cut_symbolic_audit.py` uses only exact rational sparse polynomials. Eight independent identities check global centering, the two mode denominators and numerators, denominator positivity, the n=1 sum coefficient, and the n=1 difference degeneracy. All pass, with output in `two_cut_symbolic_audit.json`.

The audit also inspected the separate direct-active-factor and full-embedded-Hilbert-space Haar-fourth-moment codes. Their declared contractions test different implementations; no additional Haar sampling was needed or performed here. The symbolic code does not import either implementation.
