# Exact Haar purity memory, entangling power, and two exchanged cuts

Independent derivation and check, checkpoint 08, 2026-09-12.

## 1. Scope and main result

Let both halves A and B have dimension d >= 2. Let psi be a complex Haar random
unit vector in A tensor B, and let U be any fixed unitary on the full d by d
space. Put P(psi) = Tr(rho_A squared), and P_U(psi) = P(U psi). The statements
below are **exact for purity at finite d**. They do not assert an exact
finite-dimensional formula for log purity or other entropies.

Write D=d^2. Realign the unitary by

\[
(U^R)_{aa',bb'}=U_{ab,a'b'},\qquad
f(U)=d^{-4}\operatorname{Tr}[(U^R U^{R\dagger})^2].
\]

Thus f(U) is the purity of the normalized operator Schmidt probabilities.
Let S exchange the **entire** d-dimensional halves and put f_s(U)=f(US).
The exact normalized memory is

\[
\boxed{\rho_P(U)=\operatorname{Corr}_{\psi}(P_U,P)
=\frac{D[(D+1)(f(U)+f_s(U))-4]}{(D-1)^2}.}
\tag{1}
\]

Both operator invariants matter for a global unitary. Keeping only f(U) is
justified in the earlier fixed-active-factor limit, not for arbitrary
dimension-growing support.

Define the standard, unnormalized linear-entropy entangling power on **whole
halves** by

\[
e_p^{(d)}(U)=\mathbb E_{a,b}[1-P(U|a\rangle|b\rangle)],
\]

where a and b are independent Haar vectors on the whole A and B spaces. Then

\[
\boxed{\rho_P(U)=1-\frac{d^2+1}{(d-1)^2}e_p^{(d)}(U)
=1-\frac{e_p^{(d)}(U)}{\mathbb E_{V\sim\mathrm{Haar}}e_p^{(d)}(V)}.}
\tag{2}
\]

Equivalently,

\[
\boxed{\mathbb E_{\psi}[(P_U-P)^2]
=\frac{4(d+1)^2}{(d^2+1)(d^2+2)(d^2+3)}e_p^{(d)}(U).}
\tag{3}
\]

Equation (2) is an exact bridge between fluctuations on entangled Haar inputs
and average entanglement production on product inputs. It follows from
standard Haar moments and established entangling-power invariants. The present
focused source check did not locate this exact normalized covariance identity
stated verbatim; this is not a claim that it is new.

## 2. Complete four-copy proof

Let X=F_A on two global copies: it exchanges their A factors only. Let
F=F_A F_B exchange the entire copies, and set

\[
Y=(U^\dagger)^{\otimes2}F_A U^{\otimes2}.
\]

Both X and Y commute with F. For either T=X or T=Y,

\[
\operatorname{Tr}T=\operatorname{Tr}(TF)=d^3,\qquad
\operatorname{Tr}_1T=\operatorname{Tr}_2T=dI_D,\qquad
\operatorname{Tr}_1(TF)=\operatorname{Tr}_2(TF)=dI_D.
\tag{4}
\]

For X these follow immediately from the swap. For Y, unitary conjugation on
the untraced copy leaves dI_D unchanged, and conjugation on the traced copy
disappears by partial-trace cyclicity. For YF use
YF=(U^dagger)^{tensor2} F_B U^{tensor2}.

The fourth moment of a Haar vector gives

\[
\mathbb E[P P_U]=\frac{1}{D(D+1)(D+2)(D+3)}
\sum_{\pi\in S_4}\operatorname{Tr}[(X_{12}\otimes Y_{34})P_\pi].
\tag{5}
\]

The 24 permutations split into double cosets of
H=\{e,(12),(34),(12)(34)\}. This gives a short exhaustive classification:

| Permutations, in one-line notation on 1,2,3,4 | Count | Trace |
|---|---:|---:|
| 1234, 1243, 2134, 2143 | 4 | d^6 |
| 3412, 4321 | 2 | Q=Tr(XY)=d^4 f(U) |
| 3421, 4312 | 2 | Q_s=Tr(XYF)=d^4 f(US) |
| Every other permutation | 16 | d^4 |

Here one-line 3412 means pi(1)=3, pi(2)=4, pi(3)=1, pi(4)=2;
it is not cycle notation.

Why these are all the terms:

* H itself gives the four products Tr(XF^a) Tr(YF^b), each d^6 by (4).
* H(23)H has 16 elements. X tensor Y commutes with the left and right H
  factors, so each trace reduces to the single bridge (23) with X and Y
  optionally replaced by XF and YF. Contracting that bridge gives the trace
  of their one-copy partial traces, Tr[(dI_D)(dI_D)]=d^4.
* H(13)(24)H has four elements. The pair exchange identifies the two-copy
  operators, giving Tr(XYF^{a+b}); two terms have even parity and two odd.
  Expanding U in matrix elements gives Q=Tr[(U^R U^{Rdagger})^2]. Replacing
  F_A with F_B in the second contraction is precisely realigning US, so
  Q_s=Tr[((US)^R (US)^{Rdagger})^2].

Consequently,

\[
\mathbb E[P P_U]
=\frac{4d^6+16d^4+2d^4[f(U)+f(US)]}
{d^2(d^2+1)(d^2+2)(d^2+3)}.
\tag{6}
\]

The first and second single-state moments, or (6) at U=I, give

\[
\mu=\frac{2d}{d^2+1},\qquad
\operatorname{Var}P=\frac{2(d^2-1)^2}
{(d^2+1)^2(d^2+2)(d^2+3)}.
\tag{7}
\]

Subtracting mu squared and dividing by (7) proves (1).

The independent implementation evaluates the 24 traces by explicit global
basis-label contraction, without invoking this classification or the closed
formula. It stores only a two-copy operator, unlike the prior checkpoint's
dense four-copy implementation.

## 3. Relation to established entangling power

The product-input second moment is

\[
\mathbb E_{a,b}[(|ab\rangle\langle ab|)^{\otimes2}]
=\frac{(I+F_A)(I+F_B)}{d^2(d+1)^2}.
\]

Its contraction with Y yields the established relation

\[
e_p^{(d)}(U)=\frac{d^2}{(d+1)^2}
\left[1+\frac{1}{d^2}-f(U)-f(US)\right].
\tag{8}
\]

Zanardi, Zalka and Faoro (2000), Proposition 1, equation (4), supplies the
two-invariant contraction; Proposition 2, equation (5), gives the unitary-Haar
mean (d-1)^2/(d^2+1). Substitution in (1) proves (2). Haar invariance implies
equal marginals for P_U and P, so twice their variance minus twice their
covariance gives (3).

This also explains why greater-than-unitary-average entangling power gives
negative purity covariance. No negative entropy production is implied: the
input-output covariance is an ensemble fluctuation statistic.

## 4. Examples and the support limit

| Global gate | f(U) | f(US) | Exact purity correlation |
|---|---:|---:|---:|
| Identity | 1 | 1/d^2 | 1 |
| Whole-half SWAP | 1/d^2 | 1 | 1 |
| CNOT, d=2 | 1/2 | 1/4 | -1/9 |
| Two-unitary qutrit permutation | 1/9 | 1/9 | -1/4 |

The qutrit gate is U|i,j> = |i+j,i+2j> with arithmetic modulo 3. It is the
odd-dimensional perfect permutation already given by Zanardi et al. (2000),
up to a trivial sign relabeling. It is a control and not a new construction.

Generally f and f_s are at least 1/d^2, giving rho_P >= -2/(d^2-1).
Whenever a two-unitary exists it saturates this bound. A gate independent
positive floor is therefore false at finite d with global spatial access.

For an active q by q unitary u embedded in halves of dimension d=qn, where n
is the spectator dimension, define a=f_q(u), b=f_q(uS_q). Tensor-product
factorization of operator Schmidt spectra gives

\[
f_d(U)=a,\qquad f_d(US_d)=b/n^2=(q^2/d^2)b.
\tag{9}
\]

Therefore the checkpoint-07 fixed-q limit rho_P -> a follows directly from
the exact finite-size formula. The second invariant disappears because the
whole-half swap necessarily exchanges the n-dimensional spectators too.
The fixed-q memory floor a >= 1/q^2 is consistent with all the global examples.

The input ensemble matters: e_p^(d)(U) describes product vectors across the
whole d-dimensional halves, which can be entangled between active factor and
spectator inside each half. It is not the active gate's product-input
entangling power e_p^(q)(u). Consequently the earlier distinction between
active-gate entangling power and fixed-cut entropy memory remains valid, but
it must not be stated as a distinction from entangling power for every choice
of input ensemble.

## 5. Two balanced cuts expose the two invariants

Take A=aR and B=bT, with a,b dimension q and R,T dimension n. The second cut
C=bR, with complement aT, is obtained by exchanging the active factors. Put
P_A(psi)=Tr rho_A^2 and P_C(psi)=P_A(S_q psi). The gate u acts on ab.

Let Y_plus=P_A+P_C and Y_minus=P_A-P_C. Define

\[
D=d^2,\quad L=\frac{D(D+1)}{(D-1)^2},\quad
B=\frac{4D}{(D-1)^2},\quad \lambda=\frac{q^2}{D}.
\]

The exact purity cross-correlations normalized by the common single-cut
variance are

\[
\rho_{\rm same}=L(a+\lambda b)-B,\qquad
\rho_{\rm cross}=L(b+\lambda a)-B,
\tag{10}
\]

and the same-time correlation between the cuts is

\[
\rho_0=L(q^{-2}+\lambda)-B.
\tag{11}
\]

Symmetry of the equal-dimensional active factors makes the 2 by 2 temporal
covariance matrix symmetric with these diagonal/off-diagonal entries. Thus
the normalized mode correlations are

\[
\rho_+=\frac{\rho_{\rm same}+\rho_{\rm cross}}{1+\rho_0},\qquad
\rho_-=\frac{\rho_{\rm same}-\rho_{\rm cross}}{1-\rho_0}.
\]

For the sum mode, direct simplification gives

\[
\boxed{\rho_+=1-K(q,d)e_p^{(q)}(u),}
\tag{12}
\]

\[
K(q,d)=\frac{(q+1)^2(D+1)(D+q^2)}
{(q^2+1)D^2+(q^4+1-6q^2)D+q^2+q^4}.
\tag{13}
\]

For n>1, the difference mode has an especially simple exact relation:

\[
\boxed{\rho_-=\frac{a-b}{1-q^{-2}}=1-2g_t(u),}
\tag{14}
\]

where g_t=[1-(a-b)/(1-q^{-2})]/2 is the established normalized gate typicality.
This mode's correlation is independent of spectator size. When n=1 the two
cuts are complementary and P_A=P_C for every pure state, so Y_minus is zero
and its correlation is undefined. The plus formula still applies.

At fixed q and n going to infinity,

\[
\rho_+\longrightarrow1-\frac{(q+1)^2}{q^2+1}e_p^{(q)}(u).
\]

For a bare active SWAP, Y_plus is exactly conserved and Y_minus exactly
changes sign. These are direct statewise identities. The covariance mode
relations extend that distinction to general gates. They are algebraic
consequences of the two established invariants, so any novelty claim must
compare with entanglement-feature transfer matrices and gate-typicality work.

## 6. Numerical checks

Run:

```
python finite_purity/check_exact_global_purity.py
python finite_purity/check_two_cut_modes.py
```

The first script tested 14 global gates at d=2,3,4 and all 24 permutation
traces for each. Maximum discrepancy in an unnormalized trace was
1.14e-13. Identity and full SWAP had correlation one, CNOT had -1/9, and the
qutrit perfect permutation had -1/4. No state sampling was used.

The second script tested 14 active-gate/spectator cases: seven gates with
q=2 or 3, each at n=1 and n=2, hence full-half dimensions through d=6. For
each case it used three direct global four-copy contractions to obtain
same-cut, crossed-cut and baseline covariances. Both mode formulas passed.
The n=1 zero-variance difference mode is explicitly excluded. The resulting
JSON files preserve all exact-moment estimates and comparisons.

These are floating-point evaluations of exact Haar moment identities.
They validate algebra and conventions, not a new statistical law inferred
from samples, and are not rigorous interval bounds on floating-point error.

## 7. Focused source audit

1. P. Zanardi, C. Zalka and L. Faoro, *Entangling power of quantum evolutions*,
   Physical Review A 62, 030301 (2000),
   https://arxiv.org/html/quant-ph/0005031v1 . Proposition 1 supplies the
   two-invariant formula; Proposition 2 the unitary-Haar mean. The explicit
   odd-dimensional perfect permutation and CNOT entangling-power control
   already appear here.
2. X. Wang and P. Zanardi, *Entangling power and operator entanglement in qudit
   systems*, Physical Review A 66, 044303 (2002),
   https://arxiv.org/html/quant-ph/0210156v2 . Existing operator-entanglement
   and ancilla interpretation of the entangling-power relations.
3. L. Clarisse, S. Ghosh, S. Severini and A. Sudbery, *The disentangling power
   of unitaries*, Physics Letters A 365, 400–402 (2007),
   https://arxiv.org/html/quant-ph/0611075v2 . Average entanglement loss from
   maximally entangled inputs is proportional to entangling power. This is a
   different input ensemble and a different average from (2), but the
   conceptual bridge predates this project.
4. J. Batle et al., *Entanglement Distribution and Entangling Power of Quantum
   Gates*, https://arxiv.org/html/quant-ph/0603059v1 . Numerically studies
   entropy-change distributions from Haar pure states, and proposes their
   widths as gate diagnostics. The present exact purity covariance relation
   was not located there. The general idea that fluctuation width measures
   a gate's ability to change entanglement is prior work.
5. B. Jonnadula, P. Mandayam, K. Zyczkowski and A. Lakshminarayan,
   *Entanglement measures of bipartite quantum gates and their thermalization
   under arbitrary interaction strength*, Physical Review Research 2,
   043126 (2020), https://arxiv.org/html/1909.08139v2 . Equation (18) is exactly
   the normalized gate typicality used in (14). Their entangling power in
   equation (15) includes an extra factor (q+1)/(q-1) relative to ours; the
   two conventions must not be mixed. Entangling power and gate typicality
   are established complementary invariants, including dynamics under
   interlaced local random unitaries. A priority overlap check for (12)-(14).
6. A. Bouland, T. Giurgica-Tiron and J. Wright, *The state hidden subgroup
   problem and an efficient algorithm for locating unentanglement*,
   https://arxiv.org/html/2410.12706v1 , Appendix A, explicitly computes
   internal purity covariances of Haar states. A direct antecedent of the
   static two-cut covariance used in (11).
7. K. Mirsohi, *Exact Haar Statistics of Planar k-Purity in Multipartite
   Quantum Systems*, https://arxiv.org/html/2608.28914v1 , Section III.2,
   uses all 24 Haar contractions to obtain a pair-of-cuts covariance kernel.
   It explicitly attributes the underlying two-subsystem Haar moment to
   older absolute-purity calculations. Its temporal-dynamics section lists
   extensions rather than proving the present arbitrary-gate relation.

The targeted searches returned no explicit match for equation (2), but a
complete priority claim would require inspecting the entanglement-feature
and local-twirling literature more closely. The result should currently be
presented as an independently derived identity and conceptual clarification,
not an established new physical principle.
