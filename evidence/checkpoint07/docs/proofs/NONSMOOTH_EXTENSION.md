# Extending the polynomial kernel to positive Rényi orders

Current status update: ALL_DEGREE_REVIEW.md now independently justifies the arbitrary fixed-degree contraction argument. Combined with NONSMOOTH_EXTENSION_AUDIT.md, no remaining internal gap has been identified in the fixed-time covariance and finite-dimensional Gaussian limit. Earlier references below to a pending all-degree review record the argument's development. No external peer review or uniform finite-size claim is implied.

Checkpoint 05, 12 September 2026. This note supplies the previously missing marginal approximation argument. It uses an existing LUE theorem, rather than proposing a new random-matrix regularity theorem. The phase-weighted all-degree annular derivation in POLYNOMIAL_KERNEL.md still merits independent mathematical review. No process tightness, almost-sure roughness, or finite-size error bound is established here.

## 1. Applicable primary result

Henry Hu, *On the regularity conditions in the CLT for the LUE*, arXiv:2310.08509v1 (2023), Theorem 1.1, Lemma 1.2, and Corollary 1.3:

https://arxiv.org/html/2310.08509v1

The matrix is W=X*X/n with independent standard complex Gaussian entries and a fixed nonnegative integer rectangularity m-n. In particular, the square case used here is included. For bounded real f on [0,infinity), Hu assumes that, for some epsilon>0,

    integral_[0,4+epsilon]^2 ((f(x)-f(y))/(x-y))^2 w(x,y) dx dy < infinity,

    w(x,y) = (1/(8 pi^2)) [sqrt(|(4-x)y|)/sqrt(|(4-y)x|)
                          +sqrt(|(4-y)x|)/sqrt(|(4-x)y|)].

The centered linear statistic then has variance converging to the usual LUE variance V[f] (the same integral restricted to [0,4]^2), a centered Gaussian limit, and approximation by smooth functions / Chebyshev polynomials in V. This is a variance-convergence result, which is stronger for our purpose than a distributional CLT alone. The author's rectangularity symbol alpha is unrelated to our Rényi order.

## 2. Verification for every fixed positive power

Choose a bounded cutoff f(x)=chi(x)x^alpha, with chi=1 throughout [0,4+epsilon] and smooth compact support. Away from x=0 the weighted integral is finite, including near x=4, since f is smooth and the square-root edge weights are integrable.

Near the hard edge, consider 0<y<x<delta and set y=ux. Up to bounded constants, the relevant integral becomes

    integral_0^delta x^(2alpha-1) dx
      * integral_0^1 [(1-u^alpha)/(1-u)]^2 (sqrt(u)+1/sqrt(u)) du.

Both integrals are finite for every alpha>0. The ratio tends to alpha at u=1 and to one at u=0; the remaining u^(-1/2) singularity is integrable. Thus the theorem applies even when alpha<=1/4. The analogous check for x log x is also finite.

Removing the upper cutoff uses the Gaussian largest-singular-value tail together with finite polynomial moments. For a fixed cutoff beyond 4, the probability of encountering it is exponentially small in d, and the uncut power statistic grows only polynomially in the matrix norm. This is an elementary Gaussian tail step, separate from Hu's bounded-function theorem; it is not necessary to ask that theorem to cover unbounded f directly.

## 3. Why a marginal theorem is enough for the nonstandard trajectory

At every fixed t, W(t)=G(t)G(t)* / d has exactly the square-LUE marginal distribution because G(t)_ij=exp(-it z_i z_j)G_ij only rotates independent complex Gaussian entries. For a test function f let X_d(f,t) be its centered trace statistic. Let p_N approximate f on [0,4] in the V seminorm; use smooth cutoffs when applying Hu to f-p_N. Then

    lim_(N to infinity) limsup_(d to infinity)
        E|X_d(f,t)-X_d(p_N,t)|^2 = 0.

The bound is the same for every t by exact stationarity. For two fixed times, Cauchy-Schwarz bounds each covariance approximation error by the marginal L2 errors. A finite linear combination over finitely many fixed times has the same approximation property. Consequently the fixed-polynomial covariance and joint Gaussian limit extend to these functions by successive limits (first d, then N).

No uniform-degree annular estimate and no pre-existing parametric-Wishart CLT is required for this passage. The matrix process remains the actual ZZ phase-block process.

Writing f(2+2cos theta)=a_0+sum_(k>=1) a_k cos(k theta), the result is

    lim Cov(X_d(f,t),X_d(h,s))
      = (1/4) sum_(k>=1) k a_k(f)a_k(h)
          [cos(t-s)^(2k)+sin(t-s)^(2k)].

The series is absolutely convergent by Cauchy-Schwarz in the finite V seminorm. At every finite set of times the centered statistics have the corresponding joint Gaussian limit, conditional on the all-degree polynomial combinatorial result.

## 4. Trace normalization and the logarithmic delta method

Let T=Tr W and Y_alpha=Tr W^alpha. The normalized Haar reduced density matrix is rho=W/T, and exactly

    S_alpha = [log Y_alpha - alpha log T]/(1-alpha).

Put mu_alpha,d=E Y_alpha, X_alpha=Y_alpha-mu_alpha,d, and Z=T-d. The MP law gives mu_alpha,d/d -> M_alpha. The preceding variance convergence and Gaussian limit imply that X_alpha^2 is uniformly integrable; likewise for Z^2.

On the event ||W||<=K and d/2<=T<=2d, with fixed sufficiently large K, Y_alpha lies between c_alpha d and C_alpha d. For alpha<1 use x^alpha>=K^(alpha-1)x for the lower bound and concavity for the upper bound. For alpha>1 use convexity for the lower bound and x^alpha<=K^(alpha-1)x for the upper bound. The scaled logarithmic Taylor remainder is bounded by C|X_alpha| and is o(|X_alpha|) in probability. Uniform integrability of X_alpha^2 therefore makes this remainder vanish in L2. The complementary event has exponentially small Gaussian probability; 0<=S_alpha<=log d controls the entropy there, while uniform integrability controls the centered statistics.

It follows, after deterministic centering and then centering by the exact mean, that

    d[S_alpha(t)-E S_alpha]
      = X_alpha(t)/[(1-alpha) M_alpha]
        -alpha Z/(1-alpha) + o_L2(1).

In the cosine expansion, the k=1 coefficient of x^alpha is 2alpha M_alpha. Thus trace normalization removes that mode exactly at leading order. For alpha=1, use S_1=log T-(Tr W log W)/T and the two-variable version of the same argument. Its k=1 mode cancels as well.

This argument does not require finite fourth moments of the entropy *rate*: it concerns centered entropy-value linear statistics, which have a different regularity problem.

## 5. Consequence for the finite-time entropy covariance

For alpha!=1 define, for k>=2,

    c_(alpha,k) = 2 Gamma(2alpha+1)
                  /[Gamma(alpha+k+1) Gamma(alpha-k+1)
                    (1-alpha) M_alpha].

For alpha=1 take the continuous limit, equivalently use the cosine coefficients of -x log x for k>=2. The cancellation just described gives

    lim_(d to infinity) d^2 E[(S_alpha(t)-S_alpha(s))^2]
      = (1/2) sum_(k>=2) k c_(alpha,k)^2 [1-F_k(t-s)],

    F_k(tau)=cos(tau)^(2k)+sin(tau)^(2k).

Both times are fixed while d tends to infinity. The left side needs no mean subtraction because the exact Haar entropy mean is stationary.

For noninteger alpha>0 the large-k coefficients obey |c_(alpha,k)|~A_alpha k^(-1-2alpha). For positive integer alpha the power is polynomial and the expansion terminates. Taking tau->0 *after* this dimension limit gives a mathematical consequence of the displayed convergent series:

    0<alpha<1/4:  limiting mean-square increment ~ C_alpha |tau|^(8alpha),
    alpha=1/4:    limiting mean-square increment ~ C_alpha tau^2 log(1/|tau|),
    alpha>1/4:    limiting mean-square increment ~ C_alpha tau^2.

Here C_alpha is positive and computable from the series. Below one quarter the integral producing the coefficient is integral_0^infinity u^(-1-4alpha)(1-exp(-u))du = Gamma(1-4alpha)/(4alpha). At the threshold, the harmonic sum produces the logarithm. Above it, sum k^2 c_(alpha,k)^2 converges, allowing the quadratic expansion.

This establishes a route to finite-dimensional Gaussian entropy fluctuations with a nonquadratic limiting increment variance. It does not by itself establish convergence in a sample-path function space, identify a fractional Brownian process, prove almost-sure nondifferentiability, or provide a uniform finite-d time-step bound. The limiting covariance is periodic and is determined by the local gate, not a Markov or Brownian interpolation.

## 6. Current proof status

The prior missing ingredient was a suitable nonsmooth marginal LUE approximation theorem. Hu's result supplies it with directly checkable assumptions; the preceding argument explains its application to the trajectory and entropy normalization. The remaining main proof-review obligation is the all-degree phase-weighted annular contraction argument in POLYNOMIAL_KERNEL.md. Exact enumeration through degree four and the numerical finite-time checks are evidence for that argument, not substitutes for reviewing it.

The worthwhile physical claim is consequently sharper than an instantaneous singular derivative: smooth finite-dimensional local unitary motion can acquire a dimension-limit temporal fluctuation law whose mean-square smoothness depends on the Rényi order. Its balanced-cut hard edge is essential. This claim remains restricted to the specified Haar equilibrium ensemble and fixed ZZ gate unless additional work proves an extension.
