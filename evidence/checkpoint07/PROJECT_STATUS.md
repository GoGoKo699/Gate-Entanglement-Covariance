# Entanglement Temporal Fluctuations: general boundary gates

Checkpoint 07, 12 September 2026.

**The operator-spectrum covariance law extends beyond diagonal gates.** The
derivation now covers any deterministic unitary on fixed boundary factors,
with a complex-Haar initial state and a balanced cut whose spectator dimensions
grow. Independent all-degree review, explicit tensor contractions, an exact
finite-dimensional Haar calculation, and a small entropy pilot support this
extension within its stated scope.

The most useful physical consequence is a limit on how much a gate with fixed
spatial access can decorrelate equilibrium entanglement. It also separates
equilibrium entropy memory from the familiar ability to entangle product inputs.

This is the current standalone project. Entanglement-Trajectories and
Boundary-Entangling-Susceptibility are separate projects and are not dependencies
or editing targets. No external repository has been created. Earlier reports
and their adverse results are retained in the accompanying project package.

## 1. What the general law says

Let each half have Hilbert-space dimension d. A fixed unitary U acts on boundary
factors of dimensions r and s; it acts as identity on spectators of dimensions
d/r and d/s. Take d to infinity through common multiples, keeping U,r,s fixed.
The initial state is complex Haar on the full d by d bipartition. Both entropy
values refer to this same input state, before and after U.

Realign the active gate as

\[
\mathscr R(U)_{(a,c),(b,e)}=U_{ab,ce},\qquad
\eta_\ell=\operatorname{eig}_\ell
 \frac{\mathscr R(U)\mathscr R(U)^\dagger}{rs}.
\]

The eta values are the normalized operator Schmidt probabilities and sum to one.
Put F_k(U)=sum_l eta_l^k. For every fixed positive pair of Rényi orders,

\[
\lim_{d\to\infty}d^2\operatorname{Cov}
 [S_\alpha(U\psi),S_\beta(\psi)]
 =\frac14\sum_{k\ge2}k c_{\alpha k}c_{\beta k}F_k(U).
\]

For alpha different from one,

\[
 c_{\alpha k}=
 \frac{2\Gamma(2\alpha+1)}
 {\Gamma(\alpha+k+1)\Gamma(\alpha-k+1)(1-\alpha)M_\alpha},
 \quad
 M_\alpha=\frac{\Gamma(2\alpha+1)}
 {\Gamma(\alpha+1)\Gamma(\alpha+2)}.
\]

Reciprocal Gamma zeros terminate the series at integer orders above one.
At alpha=1 the continuous value is
c_(1,k)=4(-1)^(k-1)/[k(k^2-1)]. All entropies use natural logarithms.

For a finite collection of gates the same result holds pairwise with the
relative gate U_l U_m^dagger, and the centered rescaled entropies have a joint
Gaussian limit. The separate operator spectra of U_l and U_m do not determine
their relative spectrum. This qualification matters for driven sequences.

The new proof step is short to state. Spectator-index contractions have the
usual Wishart topology. Unitarity removes tree attachments. The remaining
annular cycle contracts to Tr[(R(U)R(U)^dagger/(rs))^k]. The inherited
Chebyshev counting and marginal LUE approximation then give the entropy formula.
The full derivation, normalization, and higher-cumulant argument are in
checkpoints/07/reviews/GENERAL_GATE_REVIEW.md. The square-LUE and second-order fluctuation
foundations are established prior work [1–4].

## 2. Fixed spatial access imposes residual memory

Define the limiting entropy correlation coefficient

\[
\rho_\alpha(U)=
\frac{\sum_{k\ge2} k c_{\alpha k}^2 F_k(U)}
     {\sum_{k\ge2} k c_{\alpha k}^2}.
\]

The numerator and denominator are covariance and variance in the same
stationary Haar ensemble. The absolute entropy fluctuations still vanish as
1/d. A nonzero correlation coefficient does not imply macroscopic fluctuations.

The operator Schmidt rank is at most R=min(r^2,s^2). Convexity gives
F_k>=R^(1-k), hence

\[
\rho_\alpha(U)\ge
\frac{\sum_{k\ge2} k c_{\alpha k}^2 R^{1-k}}
     {\sum_{k\ge2} k c_{\alpha k}^2}>0.
\]

For equal boundary dimensions r=s=q, the bound is attained by any dual-unitary
gate: a gate whose realignment is also unitary. Its q^2 operator probabilities
are all 1/q^2. This recognized gate class and its maximal operator entanglement
are prior concepts [6,7]. The new corollary here is their common limiting
entropy-memory value and its optimality among gates on that fixed support.

For one boundary qubit on each side, all dual-unitary gates attain:

| Entropy | Minimum limiting correlation | Limiting d^2 mean-square increment |
|---|---:|---:|
| S_(1/2), pure-state logarithmic negativity | 0.17232220 | 0.20691945 |
| S_1, von Neumann | 0.22773244 | 0.38613378 |
| S_2 | 0.25000000 | 0.75000000 |

In particular, every gate with this support retains at least **25% of the
Rényi-2 correlation**. This is an asymptotic bound; it is not claimed at each
finite d. A diagonal two-qubit gate has at most two operator channels, giving
the stronger 50% lower bound in that restricted class.

## 3. Same equilibrium memory, different product-input action

Consider the boundary gates

\[
U_0=\mathrm{SWAP},\qquad
U_1=\mathrm{SWAP}\,e^{-i\pi Z\otimes Z/4}.
\]

More generally, SWAP exp(-i theta ZZ) has a realignment that is a permutation
matrix decorated with phases. All these gates have exactly four operator
probabilities equal to 1/4. Their limiting before/after covariance is therefore
identical for every fixed positive pair of entropy orders.

Yet U_0 preserves every two-qubit product input as a product, while U_1 maps
|++> to a maximally entangled two-qubit state. Thus the first has zero average
product-input entangling power, and the second has positive average entangling
power by continuity. The elementary distinction between SWAP's operator
entanglement and its entangling power is well established [5–7]. We do not claim
to discover that distinction. Our result determines its exact consequence for
the entire family of equilibrium entropy covariances.

This comparison concerns the action on a large globally Haar state for the
memory measurement, and a separate two-qubit product input for the capability
comparison. SWAP can change entanglement across the large cut by transferring
correlations already present with the spectators. No entanglement conservation
paradox arises.

The equality is about selected before/after measurements. It does not say that
the two gates have identical multi-step dynamics, higher finite-d cumulants,
or time-dependent covariance at every lag under their separate interpolations.

## 4. Exact finite-dimensional check of the limiting distinction

An independent calculation uses the exact four-copy Haar identity

\[
\mathbb E(|\psi\rangle\langle\psi|)^{\otimes4}
 =\frac{\sum_{\pi\in S_4}P_\pi}{D(D+1)(D+2)(D+3)},
 \qquad D=d^2.
\]

Contract it with the two purity measurements. All 24 terms factor into small
active traces and spectator permutation cycles. This calculation retains
finite-size terms and uses neither Gaussian leading-order truncation nor
random-state sampling.

For the two gates above, the exact purity correlation coefficients are

\[
\rho_{P,0}(d)=\frac{D^2+D+16}{4(D-1)^2},\qquad
\rho_{P,1}(d)=\frac{D^2-7D+8}{4(D-1)^2}.
\]

Their difference is 2(D+1)/(D-1)^2, which vanishes as 2/d^2. Both tend to 1/4.

| Half dimension d | Boundary SWAP | Phase-decorated SWAP |
|---|---:|---:|
| 2, no spectators | 1.000000 | -0.111111 |
| 4 | 0.320000 | 0.168889 |
| 16 | 0.253010 | 0.245106 |
| 64 | 0.250183 | 0.249695 |
| Infinite spectators | 0.250000 | 0.250000 |

These are **purity** correlations, not exact finite-d Rényi-2 entropy
correlations. Their common large-d limit transfers to S_2 through the entropy
delta method. In particular, the phase-decorated gate can have negative purity
correlation at d=2 even though the fixed-support limiting bound is positive.

The d=2 SWAP exchanges the complete halves and preserves their entanglement.
Holding the boundary dimension at two while increasing d is a different limit.
Taking the active dimensions to grow with d is outside the theorem.

## 5. Bounded validation

The declared test was an analytical discriminator, followed by a small
illustration only if it passed. checkpoints/07/PROTOCOL.md records its scope and stopping rule.

| Check | Result |
|---|---|
| All-degree general-gate derivation | Independent internal review supports the stated fixed-support theorem |
| Explicit leading Wick networks | 68,786 contractions across ten gates, including an active 2 by 3 gate |
| All mixed Chebyshev degrees through three | Maximum absolute discrepancy 4.57e-13 |
| Degree-four extension for eight gates | Maximum absolute discrepancy 3.79e-10, with cancellation of larger monomial terms |
| Exact four-copy Haar calculation | Five gates, nine half dimensions; identity and SWAP formula controls pass |
| New entropy illustration | 192 independent Haar inputs, 384 gate applications, three entropy orders |
| Gate-embedding and spectral anchors | State error at most 1.01e-16; spectrum error at most 1.95e-16 |

The degree-four extension and the dual-unitary algebraic controls were added
after the first degree-three result; they are diagnostic follow-ups. The
192-state pilot, its two gates and sizes, was specified before sampling and
its predictions were saved before generating its inputs. No data-dependent
increase in sample size was made.

The non-diagonal pilot uses boundary SWAP and
exp[-i(0.37 XX+0.23 YY+0.11 ZZ)]. At d=64 it gives the following estimates of
d^2 E[(Delta S)^2]. Errors are one sample standard error over 96 independent
inputs at that size.

| Gate | Order | Measured | Sample SE | Prediction |
|---|---:|---:|---:|---:|
| SWAP | 1/2 | 0.202017 | 0.025830 | 0.206919 |
| SWAP | 1 | 0.374868 | 0.051766 | 0.386134 |
| SWAP | 2 | 0.713391 | 0.100258 | 0.750000 |
| Cartan gate | 1/2 | 0.114490 | 0.014935 | 0.102588 |
| Cartan gate | 1 | 0.173503 | 0.024518 | 0.169565 |
| Cartan gate | 2 | 0.305910 | 0.048248 | 0.319527 |

The d=32 results are also retained in checkpoints/07/results/pilot_summary.json. Both cohorts
are broadly compatible with the predictions at this resolution. They do not
establish an asymptotic exponent or a convergence rate. Observables sharing an
input are correlated; sample errors exclude finite-size bias. Internal review
and floating-point contractions are not external peer review.

A fresh-directory reproduction passed. Both pilot NPZ files reproduced with
identical arrays; frozen prediction and summary records matched exactly. The
Wick covariance arrays also matched, and the independent rational SWAP audit
verified all 18 saved gate/size rows. VALIDATION.json records the checks.

## 6. Research decision

**Continue this as the project's current central result.** The extension removes
the special diagonal restriction and produces a concrete interpretation:
fixed access limits equilibrium decorrelation, and all dual-unitary gates
reach the same limit despite their different product-input entangling powers.

This fits the preferred balance of a clear insight, compact theory, and modest
numerics. It strengthens the PRL candidate but does not establish its suitability
for PRL. The closest additional mathematical precedent is block-Gaussian
fluctuation theory [3], while the order-two operator-entanglement/OTOC relation
is established [5]. The prospective contribution is the explicit full-spectrum
conversion into all entropy memories and its physical consequences. A referee
could still regard the result as an elegant specialization of existing methods.

The next stage should organize and challenge that compact Letter argument:
one general theorem, the fixed-access limit, and the dual-unitary comparison.
The equal-purity/different-memory example from checkpoint 06 supplies the
separate reason higher operator moments matter. Establishing what these
observables can and cannot distinguish is more relevant to this stage than
fitting additional Haar samples. No experimental efficiency or generic
many-body thermalization claim has been established.

## Primary sources and attribution

1. Mingo and Speicher, *Second Order Freeness and Fluctuations of Random
   Matrices: I. Gaussian and Wishart matrices and cyclic Fock spaces*.
   https://arxiv.org/abs/math/0405191v3
2. Kusalik, Mingo, and Speicher, *Orthogonal Polynomials and Fluctuations of
   Random Matrices*. https://arxiv.org/abs/math/0503169v1
3. Diaz, Mingo, and Belinschi, *On the Global Fluctuations of Block Gaussian
   Matrices*. https://arxiv.org/abs/1711.07140v1
4. Hu, *On the regularity conditions in the CLT for the LUE*.
   https://arxiv.org/abs/2310.08509v1
5. Styliaris, Anand, and Zanardi, *Information Scrambling over Bipartitions:
   Equilibration, Entropy Production, and Typicality*, PRL 126, 030601 (2021).
   https://arxiv.org/abs/2007.08570v3
6. Jonnadula et al., *Entanglement measures of bipartite quantum gates and their
   thermalization under arbitrary interaction strength*, PR Research 2, 043126
   (2020). https://arxiv.org/abs/1909.08139v2
7. Rather, Aravinda, and Lakshminarayan, *Creating ensembles of dual unitary and
   maximally entangling quantum evolutions*, PRL 125, 070501 (2020).
   https://arxiv.org/abs/1912.12021v3

The source review records which sections were inspected and which comparisons
are our inferences. No exhaustive originality certification has been performed.
