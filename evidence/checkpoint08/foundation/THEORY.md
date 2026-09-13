# Equilibrium local entropy-response fluctuations: theory checkpoint

This note concerns instantaneous rates. Later finite-time entropy fluctuation results are in POLYNOMIAL_KERNEL.md and NONSMOOTH_EXTENSION.md. Their Gaussian entropy-value limit does not imply Gaussian instantaneous rates in the small-order regime.

Status: exact conditional second-moment identity, followed by asymptotic predictions to test. No Gaussian limit, deterministic same-state angle law, or finite-time dynamics theorem is claimed. Natural logarithms and hbar=1 throughout. Dimensions are a<=b and the global dimension is D=ab.

## 1. Ensemble and physical probe

A pure state is sampled from the complex Haar ensemble on C^a tensor C^b. Conditional on its Schmidt probabilities lambda_1,...,lambda_a>0, its two Schmidt bases are independently Haar distributed, with the usual irrelevant paired-phase redundancy. Apply a fixed interaction H=A tensor B where A and B are traceless Hermitian matrices. The principal physical example is a Pauli Z on one boundary qubit of each half, tensored with identities: A^2=I_a, B^2=I_b, and ||H||=1. Thus Tr A^2=a and Tr B^2=b.

The derivative is at time zero under exp(-itH). The state is sampled independently of H. This is a perturbation response of an equilibrium ensemble; it is not a claim about entanglement growth from product states, a finite-time thermalization law, or an autonomous Hamiltonian eigenstate response.

For any differentiable spectral objective F, let h_i be its derivative with respect to lambda_i. Additive constants in h do not matter because sum_i dot(lambda_i)=0.

## 2. Exact covariance conditional on the spectrum

In the Schmidt basis let X=U^dagger A U and Y=W^dagger B W. Expanding the Schrödinger equation gives

    dot(F) = 2 sum_{i<j} sqrt(lambda_i lambda_j) (h_i-h_j) Im(X_ij Y_ij).

The overall sign can change with the convention for matrix elements; all covariance formulas below are unchanged. For traceless Hermitian A, the exact Haar second moment is

    E[X_ij X_kl] = v_A (delta_il delta_jk - delta_ij delta_kl/a),
    v_A = Tr(A^2)/(a^2-1),

and similarly v_B=Tr(B^2)/(b^2-1). For off-diagonal unordered pairs the independent-basis average gives

    E[Im(X_ij Y_ij) Im(X_kl Y_kl)] = (v_A v_B/2) delta_{(ij),(kl)}.

All first moments vanish. Hence, for two spectral objectives with derivative vectors h and k,

    Cov(dot(F),dot(G) | lambda)
      = 2 v_A v_B sum_{i<j} lambda_i lambda_j (h_i-h_j)(k_i-k_j)
      = 2 v_A v_B [sum_i lambda_i h_i k_i
                     -(sum_i lambda_i h_i)(sum_j lambda_j k_j)].

The last equality uses sum_i lambda_i=1. The expression in brackets is the classical covariance of h(lambda) and k(lambda) under the probability weights lambda themselves.

For the boundary ZZ probe the prefactor is exactly

    2ab/[(a^2-1)(b^2-1)].

This identity holds for every fixed positive spectrum, before any Marchenko-Pastur approximation. It is elementary Haar second-moment algebra; originality is not claimed for the integration identity.

More generally, averaging over independent Schmidt bases gives the same spectral covariance multiplied by 2||H_corr||_HS^2/[(a^2-1)(b^2-1)], where H_corr is the interaction with its identity and one-half-only pieces removed. Thus the second moment alone does not retain detailed spatial locality. The fixed ZZ example supplies a physically local realization, not a locality-sensitive covariance theorem.

## 3. Rényi rates and the familiar alpha=1 connection

Write p_alpha=sum_i lambda_i^alpha and S_alpha=log(p_alpha)/(1-alpha). For alpha>0, alpha!=1, take

    h_alpha(lambda_i)=alpha lambda_i^(alpha-1)/[(1-alpha)p_alpha].

For alpha=1 take h_1=-log(lambda_i). The exact conditional variance is

    V_alpha(lambda) = 2 v_A v_B [alpha/(1-alpha)]^2
                     [p_(2alpha-1)/p_alpha^2 - 1].

For distinct alpha,beta neither equal to one, replace the squared prefactor by alpha beta/[(1-alpha)(1-beta)] and p_(2alpha-1)/p_alpha^2 by p_(alpha+beta-1)/(p_alpha p_beta).

At alpha=1,

    V_1(lambda)=2 v_A v_B Var_lambda(log lambda).

The spectral factor is exactly the established capacity of entanglement. Its statistics for random pure states and its use in entropy-rate bounds have prior literature. This case cannot be advertised as a newly discovered spectral susceptibility.

## 4. Balanced cut: a proposed bulk-to-small-eigenvalue change at alpha=1/4

Let a=b=d and take d large at fixed alpha. For x=d lambda, the limiting number-weighted Marchenko-Pastur density is

    rho(x)=sqrt((4-x)/x)/(2 pi), 0<x<4.

Its moments are M_s=4^s Gamma(s+1/2)/[sqrt(pi) Gamma(s+2)] for s>-1/2. The lambda-weighted measure is x rho(x) dx. It is a semicircle density centered at 2 with radius 2, and it behaves as x^(1/2) at its lower edge.

Squaring the rate weight x^(alpha-1) produces an integrand x^(2alpha-3/2). The bulk integral is finite exactly when alpha>1/4. The resulting predictions for conditional variances are:

| Fixed order | Predicted conditional-variance scale |
|---|---|
| alpha>1/4 | d^(-2), with a deterministic bulk limit after rescaling |
| alpha=1/4 | d^(-2) log d |
| 0<alpha<1/4 | d^(-1-4alpha), with a random limiting coefficient from the smallest Schmidt probabilities |

For alpha>1/4 and alpha!=1 the candidate bulk limit is

    d^2 V_alpha -> 2 [alpha/(1-alpha)]^2 [M_(2alpha-1)/M_alpha^2 - 1].

At alpha=1 the bracket is replaced by the corresponding logarithmic covariance. The alpha=1 expression is a continuous limit.

At alpha=1/4, the microscopic cutoff x_min is of order d^(-2). Since rho(x)~1/(pi sqrt(x)), the leading logarithmic candidate is

    d^2 V_(1/4)/log d -> 4/[9 pi M_(1/4)^2].

For alpha<1/4, write lambda_i approximately xi_i/d^3 for the lowest ordered eigenvalues, where xi_i are hard-edge variables of order one for fixed i. Then

    d^(1+4alpha) V_alpha
      approximately [2 alpha^2/((1-alpha)^2 M_alpha^2)]
                    sum_i xi_i^(2alpha-1).

The large-i behavior xi_i of order i^2 explains convergence of this sum precisely below alpha=1/4. The coefficient stays random; it is not replaced by a deterministic Marchenko-Pastur integral. Turning these statements into rigorous distributional or moment limits requires appropriate hard-edge convergence and integrability arguments. They are asymptotic predictions in this checkpoint.

All these rates still vanish with size. The anomaly is slower suppression relative to d^(-2), not an absolute divergence of a typical physical rate, a failure of unitary dynamics, or an escape from exponentially small gradients in qubit number.

## 5. One-qubit shift at the same global dimension

Compare balanced a=b=d with a=d/2,b=2d, so D=d^2 is unchanged while the aspect ratio becomes c=a/b=1/4. This corresponds to moving a bipartition by one qubit in an even-qubit system.

For x=a lambda, the Marchenko-Pastur support becomes [(1-sqrt(c))^2,(1+sqrt(c))^2]=[1/4,9/4]. It is bounded away from zero. Every fixed alpha>0 therefore has a finite bulk integral and the predicted variance returns to D^(-1)=d^(-2).

The proposed observable distinction is thus: balanced cuts have a low-order response regime governed by their smallest Schmidt channels, while the one-qubit-shifted cut at equal D has a bulk-controlled response for every fixed positive order. This is an ensemble/aspect-ratio claim. It does not assert that every individual pair of cuts in a given state follows the asymptotic comparison, or that arbitrary near-balanced limits behave like fixed c=1/4.

For general c<1, the lambda-weighted MP measure is exactly

    x rho_c(x) dx = sqrt[4c-(x-1-c)^2]/(2 pi c) dx,

a shifted semicircle. A fixed difference b-a as d grows remains a hard-edge regime and must not be conflated with fixed unequal aspect ratio.

## 6. Typical conditional variance, annealed moments, and heavy tails

The physical derivative varies both with the spectrum and with its bases. The conditional V_alpha averages only the bases. A sample median of V_alpha over spectra estimates a typical conditional scale. Its mean is a different quantity. For alpha<1/4 the rescaled conditional variance is predicted not to concentrate, so median and mean coefficients need not agree.

The complex square-Haar smallest-eigenvalue density remains nonzero at zero at every finite d. For a generic interaction the singular part of dot(S_alpha) as lambda_min tends to zero is proportional to lambda_min^(alpha-1/2), with a generically nonzero random coefficient. For 0<alpha<1/2 this suggests the fixed-d survival tail

    Pr(|dot(S_alpha)|>z) proportional to z^[-2/(1-2alpha)]

at sufficiently large z. This tail assertion needs separate coefficient and regularity verification; it is not used as an established limit theorem in the experiment.

The integrability consequence is nevertheless a concrete warning: second moments are finite for fixed alpha>0, while fourth moments are generically infinite for alpha<=1/4 in the balanced complex-Haar ensemble. Similarly, the random conditional variance has a finite mean but an infinite second moment in that regime. Ordinary sample-variance error bars based on a finite fourth moment are then unjustified. Report medians/quantiles of conditional V_alpha and retain outliers. Do not use a small number of exceptionally tiny eigenvalues to claim a fitted critical exponent.

For rectangular ensembles with b-a=nu, the edge density has extra power lambda_min^nu; fixed-d moment thresholds change. This is another reason to distinguish fixed-aspect and fixed-dimension-difference limits.

## 7. What is deliberately not claimed

- The exact covariance does not prove joint Gaussian rates or any arcsine sign law.
- Nine local response-vector components do not become an infinite statistical sample as d grows. Their same-state angles need not concentrate to covariance correlations.
- alpha=0 is rank entropy and has zero derivative at a full-rank state. The limits alpha to zero and d to infinity are nonuniform; fixed-positive-alpha statements cannot be extended to rank entropy.
- The worst-case spectral SIE threshold alpha=1/2 is a different question. Nothing here improves or contradicts that bound.
- The singularity of an entropy derivative alone is known and not a sufficient novelty claim. The target is a tested dimension/aspect-ratio fluctuation law with a physical local probe.
- An independent random local circuit preparation check would address physical relevance only for the specified circuit and depths. It would not prove generic Hamiltonian thermalization.
