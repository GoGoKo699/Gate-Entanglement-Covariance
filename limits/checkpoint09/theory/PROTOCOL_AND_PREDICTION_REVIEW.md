# Independent prediction and protocol review

Checkpoint 09, 12 September 2026. This note and its deterministic predictor do
not read the Floquet eigenstates or their entropy responses. It reviews the
proposed eight- and ten-qubit comparison with the complex-Haar reference.

## 1. Scope and the useful comparison

The proposed input ensemble is the complete eigenbasis of one generic complex
nearest-neighbor brickwork Floquet circuit at each size. The probes are identity,
boundary SWAP, and boundary SWAP exp(-i pi ZZ/4). The two nontrivial probes have
the same four normalized operator Schmidt weights, each 1/4. They therefore
have identical **limiting** Haar entropy covariance at every fixed positive
Renyi order. They have slightly different exact finite-dimensional Haar purity
covariances.

This is a test of the reach of a Haar prediction in one physical model family.
It is not a theorem about eigenstates and does not test autonomous evolution
of these states under their own Floquet operator: that evolution is a global
phase at integer periods. The experiment applies separate, prescribed probes.

At each size report the baseline and both output means and variances, the
centered covariance, the Pearson correlation, and the uncentered mean-square
increment. A satisfactory correlation can conceal incorrect marginal scales.
No invariance principle makes the output marginals stationary for this
non-Haar cohort. In particular

    E[(S_out-S_in)^2]
      = Var(S_out)+Var(S_in)-2 Cov(S_out,S_in)
        +(E[S_out]-E[S_in])^2.

Dropping the last term, or replacing both variances by the baseline variance,
would silently assume part of the claim under test.

## 2. Asymptotic entropy benchmarks

Natural logarithms are used. Let the half dimension be d=2^(N/2). The inherited
fixed-boundary Haar theorem gives

    V_alpha = lim d^2 Var(S_alpha) = (1/4) sum_(k>=2) k c_alpha,k^2,
    C_alpha = lim d^2 Cov(S_alpha(U psi),S_alpha(psi))
            = (1/4) sum_(k>=2) k c_alpha,k^2 4^(1-k)

for either nontrivial probe. The coefficients start at
c_alpha,2=-2 alpha/(alpha+2) and follow
c_alpha,k+1/c_alpha,k=(alpha-k)/(alpha+k+1). At alpha=1 use
c_1,k=4(-1)^(k-1)/(k(k^2-1)). The reference mean shift is zero exactly under Haar.

| Order | d^2 variance limit | Correlation limit | d^2 mean-square increment limit |
|---|---:|---:|---:|
| 1/2 | 0.125 | 0.1723221985 | 0.2069194504 |
| 1 | 0.25 | 0.2277324385 | 0.3861337807 |
| 2 | 0.5 | 0.25 | 0.75 |

The predictor sums 131,072 modes. The displayed half-order static sum differs
from 1/8 by about 1.64e-11 because of truncation. This is a numerical evaluation
of the inherited analytic series, not a finite-dimension entropy formula.

## 3. Exact finite-dimension references

The established Haar purity moments at a balanced d by d cut are

    mu_P=2d/(d^2+1),
    v_P=2(d^2-1)^2/[(d^2+1)^2(d^2+2)(d^2+3)].

For a fixed active-qubit gate let a=f(U), b=f(U SWAP), where f is normalized
operator Schmidt purity on the active factors. Checkpoint 08 gives, with D=d^2,

    Corr(P_U,P) = D[(D+1)(a+4b/D)-4]/(D-1)^2.

For SWAP, (a,b)=(1/4,1); for phaseSWAP, (a,b)=(1/4,1/2). Consequently

    rho_SWAP=(D^2+D+16)/[4(D-1)^2],
    rho_phaseSWAP=(D^2-7D+8)/[4(D-1)^2].

The variance and squared-increment scales for purity are d^4, whereas entropy
uses d^2. The exact squared increment is 2 v_P(1-rho).

| N | d | d^4 v_P | rho_SWAP | rho_phaseSWAP |
|---|---:|---:|---:|---:|
| 8 | 16 | 1.9310991400 | 0.2530103806 | 0.2451057286 |
| 10 | 32 | 1.9825111622 | 0.2507374378 | 0.2487785814 |

There is also an exact, established finite-dimensional Haar **von Neumann
variance**. Wei's proof of the Vivo-Pato-Oshanin formula gives, at balance,

    Var_Haar(S_1) = -psi_1(d^2+1)
       + 2d psi_1(d)/(d^2+1)
       - (d+1)(3d+1)/[4d^2(d^2+1)].

Here psi_1 is the trigamma function. Thus d^2 Var_Haar(S_1) is
0.247410012380 at d=16 and 0.249349847450 at d=32. Its deviation from the
asymptotic 1/4 is only about 1.04% and 0.26%, respectively. This benchmark helps
distinguish finite-dimensional Haar bias from a large eigenstate fluctuation
excess. It does not provide an exact temporal entropy covariance.

Primary source: Lu Wei, *A Proof of Vivo-Pato-Oshanin's Conjecture on the
Fluctuation of von Neumann Entropy*, Physical Review E 96, 022106 (2017),
https://arxiv.org/abs/1706.08199 and
https://journals.aps.org/pre/abstract/10.1103/PhysRevE.96.022106 .
The formula is explicit in the primary article abstract, inspected for this
checkpoint. `haar_predictions.py` evaluates these exact references without
loading production data. Rational purity values are retained in its JSON.

## 4. Complete-eigenbasis dependence and decision language

A complete eigenbasis is an orthonormal finite cohort. Its members are not
independent draws from any specified state distribution. One circuit at each
size supplies no circuit-to-circuit sampling uncertainty. Use population
variance and covariance (denominator equal to the number of eigenstates) and
avoid iid state bootstrap intervals or a claimed inverse-square-root sample
error. An uncertainty range from splitting that same eigenbasis is only a
within-circuit descriptive range, not a calibrated confidence interval.

If a binary feasibility rule is desired before outcomes, an absolute
correlation error of 0.10 and variance/increment ratios in [0.75,1.25] are
reasonable **descriptive engineering tolerances** for this small first test.
They are not derived statistical critical values and are not claims of 25%
finite-size bounds. Always retain the continuous discrepancies. The root
protocol determines whether to adopt these proposed tolerances.

Two sizes cannot establish a thermodynamic scaling law. A trend toward the
Haar values could justify a later controlled test; a sizable discrepancy says
that the tested eigenstates do not yet support the desired physical reach.
It does not falsify the Haar theorem. Identity is an exact implementation
control for any state, and should preserve every entropy and purity.

## 5. An exact obstruction for the circuit's own crossing gate

The root identified the following stationarity constraint before production
responses were available. It is exact and more informative than a generic
appeal to non-Haar behavior.

An open nearest-neighbor two-layer brickwork period has exactly one gate G_c
crossing a specified single cut. Every other gate is a product unitary across
that cut. By grouping gates before and after G_c, write

    F=L_2 G_c L_1,

where L_1 and L_2 are local with respect to the two entire halves. If
F psi=exp(i theta) psi, define the state immediately before the crossing gate
by phi=L_1 psi. The shifted-period operator is

    F'=L_1 F L_1^dagger=(L_1 L_2)G_c.

The eigenstate equation becomes

    G_c phi=exp(i theta)(L_1 L_2)^dagger phi.

The right-hand side is a product unitary across the cut applied to phi, up to
a global phase. Therefore **the entire Schmidt spectrum is unchanged by
G_c on phi**, separately for every Floquet eigenstate and every system size.
All entropy and purity increments vanish exactly. If their across-eigenstate
variance is nonzero, the corresponding normalized temporal correlation is one.
At zero variance the correlation is undefined, not one.

The gate in this statement is G_c, not G_c^dagger. The input frame matters.
In the original frame an equivalent probe is

    W=L_1^dagger G_c L_1.

Since S(W psi)=S(G_c L_1 psi)=S(L_1 psi)=S(psi), it has the same exact zero
response. Product-unitary pre- and postmultiplication leave the normalized
operator Schmidt spectrum of W identical to that of G_c. The physical support
can expand under L_1, but only within its finite-depth causal neighborhood.

For a nonproduct G_c the Haar reference predicts a strictly positive scaled
entropy increment, because F_k(G_c)<1 for k>=2 and c_alpha,2 is nonzero for
every alpha>0. Thus any unconditional extension from Haar states to Floquet
eigenstates is impossible, even if single-state spectral statistics look
Haar-like. The missing information is the correlation of eigenstate Schmidt
bases with the gate that defines the dynamics.

This is not a contradiction with ETH: the entropy is a nonlinear nonlocal
observable and the gate is tied to the eigenbasis itself. It also does not
force independent prescribed probes such as SWAP or phaseSWAP to have zero
response. It does not establish a new mechanism merely by restating periodic
stationarity. Its role here is a sharp boundary on the universality claim.

With multiple crossing gates in a period, only their total entropy increments
sum to zero on an eigenstate orbit. Individual increments need not vanish.
With periodic spatial boundaries a balanced contiguous cut generally has two
crossing bonds, so the one-crossing conclusion need not apply.

## 6. Literature boundary

A focused search found a close general antecedent: D. Hahn, D. J. Luitz, and
J. T. Chalker, *Eigenstate correlations, the eigenstate thermalization
hypothesis, and quantum information dynamics in chaotic many-body quantum
systems*, arXiv:2309.12982, Physical Review X 14, 031029 (2024),
https://arxiv.org/abs/2309.12982 . Its primary abstract explicitly emphasizes
spatial eigenstate correlations that govern entanglement dynamics and operator
spreading in Floquet systems without conserved densities. The general message
that dynamical correlations contain information beyond simple eigenstate
randomness is therefore established. The present search did not establish
priority for the elementary one-crossing identity, and no novelty claim is
made for it.

The theory in this note is a protocol audit and a scope clarification.
Independent-probe numerical results must be assessed separately.
