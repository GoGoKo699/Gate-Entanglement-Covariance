# Derivation of the entropy covariance law

This note derives [the covariance theorem](THEOREM.md), with explicit conventions and proof dependencies. It separates the spectator topology, the gate contraction, the nonpolynomial approximation and the entropy normalization. Established external inputs are identified in [References](../docs/REFERENCES.md).

For **CHECK**, proceed directly through Sections 1–6. For **LEARN**, the
[tutorial bridge](../docs/TUTORIAL_BRIDGE.md) explains the quantum dictionary and
the book's trace and Chebyshev conventions first. The selected book supplies
background, R1–R2 supply credited annular-Wishart machinery, and R4 supplies the
nonpolynomial approximation input. The gate-specific cycle reduction is derived
in Section 2, rather than assumed from Wishart marginals or quoted from the book.

## 1. Assumptions and Gaussian representation

Fix active dimensions $`r,s`$, a finite list of deterministic gates $`U_1,\ldots,U_L`$ on $`\mathbb C^r\otimes\mathbb C^s`$, and finitely many positive entropy orders. Let $`d\to\infty`$ through common multiples of $`r,s`$. Each half has dimension $`d`$, with spectator dimensions $`d/r,d/s`$. Logs are natural. The initial state is complex Haar on the full $`d\times d`$ cut.

Let $`G`$ have independent standard complex Gaussian entries, with $`\mathbb E|G_{ai,bj}|^2=1`$. Active indices are $`a,c\in\{1,\ldots,r\}`$ and $`b,e\in\{1,\ldots,s\}`$; $`i,j`$ index the spectators. Define

```math
G_\ell[ai,bj]=\sum_{c,e}(U_\ell)_{ab,ce}G[ci,ej],\qquad
W_\ell=G_\ell G_\ell^\dagger/d,\qquad
T=\mathop{\mathrm{Tr}}\nolimits W_\ell=\|G\|_F^2/d.
```

The normalized coefficient array gives the Haar state, and its reduced density matrix after the gate is $`\rho_\ell=W_\ell/T`$. The same $`T`$ is shared exactly by every gate. Unitarity gives the joint covariance

```math
\mathbb E\!\left[G_\ell[ai,bj]\overline{G_m[ck,ev]}\right]
=\delta_{ik}\delta_{jv}(V_{\ell m})_{ab,ce},\qquad
V_{\ell m}=U_\ell U_m^\dagger.
```

Unconjugated pairings vanish. At $`\ell=m`$ this is the complete identity covariance, so each $`G_\ell`$ separately has independent standard Gaussian entries. Distinct gates are correlated. In particular, their individual operator spectra cannot replace the spectrum of the relative gate $`V_{\ell m}`$.

Use the realignment convention

```math
\mathcal R(V)_{(a,c),(b,e)}=V_{ab,ce},\qquad
\eta_h(V)=\lambda_h\!\left(\frac{\mathcal R(V)\mathcal R(V)^\dagger}{rs}\right)>0,
\qquad F_k(V)=\sum_h\eta_h(V)^k.
```

Matrix units are Hilbert–Schmidt orthonormal, so these eigenvalues are the normalized squared operator Schmidt coefficients. Their sum is $`\mathop{\mathrm{Tr}}\nolimits (VV^\dagger)/(rs)=1`$.

## 2. Connected contractions and the surviving cycle

For a product of traces with total degree $`N`$, label the $`W`$ factors by $`h=1,\ldots,N`$ and let the permutation $`\gamma`$ cycle around each trace. Before Wick pairing, the indexed expansion has the form

```math
d^{-N}\sum_{A_1,\ldots,A_N;B_1,\ldots,B_N}
\prod_{h=1}^N
G_{\ell_h}[A_h,B_h]\,
\overline{G_{\ell_h}[A_{\gamma(h)},B_h]}.
```

Here $`A=(a,i)`$ and $`B=(b,j)`$, and $`\ell_h`$ is constant along each trace. If a Wick permutation $`\pi`$ pairs the unconjugated factor at $`h`$ with the conjugated factor at $`\pi(h)`$, the spectator identifications are $`i_h=i_{\gamma\pi(h)}`$ and $`j_h=j_{\pi(h)}`$. Active indices instead retain the finite tensors $`V_{\ell_h\ell_{\pi(h)}}`$.

This is the usual orientable bipartite Wishart ribbon graph convention. With $`v_r,v_c`$ spectator vertices, $`N`$ edges, $`p`$ trace faces and genus $`g`$, a connected graph obeys

```math
v_r+v_c-N+p=2-2g.
```

Its spectator sums contribute $`(d/r)^{v_r}(d/s)^{v_c}d^{-N}`$. At fixed support and degrees every active contraction is bounded independently of $`d`$. Connected terms with $`p`$ traces therefore scale as $`O(d^{2-p-2g})`$. Covariance subtracts disconnected two-trace pairings; higher cumulants retain pairings connected across all their trace faces.

For two traces, leading graphs have $`g=0`$ and $`v_r+v_c=N`$. They are unicyclic. Parallel edges are allowed: the shortest backbone is a two-edge cycle. Every edge outside the unique cycle is a bridge. Across the trace walks each edge appears twice, whereas a closed walk traverses a bridge an even number of times. Both appearances of a bridge must therefore lie in the same trace. Its gate covariance is the identity.

Peeling a tree leaf supplies $`r(d/r)=d`$ for a row leaf or $`s(d/s)=d`$ for a column leaf. The remaining active identities identify the parent legs normally. Thus tree decorations have the ordinary Wishart weights and leave no gate tensor on the backbone. This bridge argument is why arbitrary non-diagonal gates reduce to one cycle invariant.

For a backbone with $`k`$ row and $`k`$ column vertices, its two faces run in opposite directions. With cyclic subscripts, the active contraction is

```math
\sum_{a_1,\ldots,a_k;c_1,\ldots,c_k;
      b_1,\ldots,b_k;e_1,\ldots,e_k}
\prod_{h=1}^k
V_{a_hb_h,c_he_h}
\overline{V_{a_{h+1}b_h,c_{h+1}e_h}}
=\mathop{\mathrm{Tr}}\nolimits \!\left[(\mathcal R(V)\mathcal R(V)^\dagger)^k\right].
```

The backbone spectator sums and its $`2k`$ Wishart factors contribute $`(d/r)^k(d/s)^kd^{-2k}=(rs)^{-k}`$. Its weight is exactly $`F_k(V)`$. The displayed orientation gives realignment; it does not produce a partial-transpose term. Fixed support is essential to the preceding power counting.

## 3. Chebyshev modes and polynomial Gaussian limits

The plane-tree count for a trace of degree $`m`$ and backbone half-length $`k`$ is

```math
q_{m,k}=\binom{2m}{m-k}
=\frac{m}{k}[z^{m-k}]C(z)^{2k},\qquad C(z)=1+zC(z)^2.
```

There are $`k`$ compatible cyclic gluings. Consequently

```math
\lim_{d\to\infty}\mathop{\mathrm{Cov}}\nolimits 
(\mathop{\mathrm{Tr}}\nolimits W_\ell^m,\mathop{\mathrm{Tr}}\nolimits W_n^j)
=\sum_{k=1}^{\min(m,j)}kq_{m,k}q_{j,k}F_k(V_{\ell n}).
```

Define $`\Gamma_k(x)=2T_k((x-2)/2)`$, where $`T_k`$ is the first-kind Chebyshev polynomial, $`T_k(\cos\theta)=\cos(k\theta)`$. This is $`C_k(x-2)`$ in the book's convention, the square case of its Example 42. All covariances here use unnormalized $`\mathop{\mathrm{Tr}}\nolimits `$ and exact mean centering; normalized $`\mathrm{tr}=d^{-1}\mathop{\mathrm{Tr}}\nolimits `$ describes empirical spectral averages instead. The exact triangular identity

```math
x^m=\binom{2m}{m}+\sum_{k=1}^m q_{m,k}\Gamma_k(x)
```

then yields mode covariance $`\delta_{jk}kF_k(V_{\ell n})`$. Using $`T_k`$ instead of $`\Gamma_k`$ divides this covariance by four. These tree counts and diagonalization build on the established annular Wishart and Chebyshev literature, [R1–R2](../docs/REFERENCES.md).

For $`p\ge3`$, the connected-graph bound is $`O(d^{2-p})`$ and tends to zero. The fixed-degree moment/cumulant argument and Cramér–Wold give a joint Gaussian limit for any fixed finite polynomial family. Degenerate covariance matrices and noncommuting gates are allowed. No estimate uniform in degree is used.

## 4. Transfer to entropy test functions

Write

```math
f(2+2\cos\theta)=a_0(f)+\sum_{k\ge1}a_k(f)\cos(k\theta),\qquad
\mathcal V[f]=\frac14\sum_{k\ge1}k\,a_k(f)^2.
```

Henry Hu's square-LUE variance convergence and approximation results [R4](../docs/REFERENCES.md), specifically Theorem 1.1, Lemma 1.2, Corollary 1.3 and Section 3, provide the external nonpolynomial input. Its fixed rectangularity parameter permits zero and is unrelated to entropy order. It gives variance convergence as well as a CLT; a distributional CLT alone would not suffice below.

In the convention used here, the matrix is complex LUE with fixed nonnegative
integer rectangularity, zero for the square case. The sufficient hypothesis on
a bounded real $`f:[0,\infty)\to\mathbb R`$ is that, for some $`\varepsilon>0`$,

```math
\int_0^{4+\varepsilon}\!\int_0^{4+\varepsilon}
\left(\frac{f(x)-f(y)}{x-y}\right)^2 w(x,y)\,dx\,dy<\infty,
```

```math
w(x,y)=\frac1{8\pi^2}\left[
\frac{\sqrt{|(4-x)y|}}{\sqrt{|(4-y)x|}}
+\frac{\sqrt{|(4-y)x|}}{\sqrt{|(4-x)y|}}
\right].
```

The following estimates verify this weighted condition for the entropy test functions.
Together with Hu's variance convergence and approximation results, it controls
centered polynomial approximation in $`L^2`$, not only in distribution. That
second-moment control is what permits covariance transfer and the entropy
normalization below. No independence between the different gate marginals is
part of this input.

For a bounded smooth upper cutoff of $`x^\alpha`$, equal to that power near $`[0,4]`$, the weighted hard-edge regularity test reduces near $`0<y<x<\delta`$, with $`y=ux`$, to

```math
\left[\int_0^\delta x^{2\alpha-1}\,dx\right]
\left[\int_0^1
\left(\frac{1-u^\alpha}{1-u}\right)^2
(\sqrt u+u^{-1/2})\,du\right]<\infty
\quad(\alpha>0).
```

The mixed edge corners are integrable and the function is smooth near $`4`$. The same regularity check holds for $`x\log x`$, defined as zero at zero. A cutoff beyond the upper edge is removed in $`L^2`$ using the Gaussian operator-norm tail and fixed polynomial moments. Thus the bounded-function theorem is not being applied directly to an unbounded power.

Let $`X_d(f,\ell)=\mathop{\mathrm{Tr}}\nolimits f(W_\ell)-\mathbb E\mathop{\mathrm{Tr}}\nolimits f(W_\ell)`$. Polynomial approximation in $`\mathcal V`$ gives

```math
\lim_{M\to\infty}\limsup_{d\to\infty}
\|X_d(f,\ell)-X_d(p_M,\ell)\|_2=0.
```

Cut off the approximating polynomials when invoking Hu, then remove their cutoffs as above. The triangle inequality controls every fixed linear combination over gates, and Cauchy–Schwarz controls covariance errors. Independence between gates is unnecessary. Taking dimension first and approximation degree second transfers the polynomial Gaussian limit and gives

```math
\lim_{d\to\infty}\mathop{\mathrm{Cov}}\nolimits (X_d(f,\ell),X_d(h,n))
=\frac14\sum_{k\ge1}k\,a_k(f)a_k(h)F_k(V_{\ell n}).
```

Absolute convergence follows from Cauchy–Schwarz and $`0\le F_k\le1`$.

## 5. Normalization and exact mean centering

For $`\alpha\ne1`$, put $`Y_\alpha=\mathop{\mathrm{Tr}}\nolimits W_\ell^\alpha`$, $`\mu_{\alpha,d}=\mathbb EY_\alpha`$, $`X_\alpha=Y_\alpha-\mu_{\alpha,d}`$ and $`Z=T-d`$. The Marchenko–Pastur moment is

```math
\frac{\mu_{\alpha,d}}d\longrightarrow
M_\alpha=\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha+1)\Gamma(\alpha+2)}>0,
\qquad
S_\alpha=\frac{\log Y_\alpha-\alpha\log T}{1-\alpha}.
```

Convergence in distribution together with convergence of second moments makes $`X_\alpha^2`$ and $`Z^2`$ uniformly integrable. On $`\|W_\ell\|\le K`$ and $`d/2\le T\le2d`$, power-trace and trace arguments of the logarithms are bounded above and below by constants times $`d`$. Their scaled Taylor remainders are bounded by constants times $`|X_\alpha|+|Z|`$, with vanishing multipliers in probability. Uniform integrability then gives vanishing $`L^2`$ remainders.

The exceptional event has exponentially small probability. Bound the **combined normalized entropy** by $`0\le S_\alpha\le\log d`$, giving an $`O(d\log d)`$ bound after scaling and deterministic centering. This controls the entropy on that event; uniform integrability controls the linear statistics. Bounding the separate logarithms would not establish this step. Finally, exact mean centering subtracts the expectation of an $`o_{L^2}(1)`$ remainder. Hence

```math
d(S_\alpha-\mathbb ES_\alpha)
=\frac{X_\alpha}{(1-\alpha)M_\alpha}
-\frac{\alpha}{1-\alpha}Z+o_{L^2}(1).
```

At order one let $`Y=\mathop{\mathrm{Tr}}\nolimits (W_\ell\log W_\ell)`$, $`X=Y-\mathbb EY`$, $`m_d=\mathbb EY/d\to1/2`$, $`q=Z/d`$ and $`s_{0,d}=\log d-m_d`$. Exact algebra gives

```math
d(S_1-s_{0,d})=(1+m_d)Z-X
+d[\log(1+q)-q]-\frac{m_d Zq}{1+q}+\frac{Xq}{1+q}.
```

On the good trace event, each remainder is bounded by $`C(|X|+|Z|)`$ with a multiplier tending to zero in probability. The same exceptional-event and centering argument gives

```math
d(S_1-\mathbb ES_1)=\frac32Z-X+o_{L^2}(1).
```

## 6. Entropy coefficients and final kernel

The first cosine coefficient of $`x^\alpha`$ is $`2\alpha M_\alpha`$. Thus the trace term cancels mode one. At order one, $`x\log x`$ has first coefficient $`3`$, matching $`(3/2)x`$. This removes the shared radial fluctuation, for which $`F_1=1`$ and $`\mathop{\mathrm{Var}}\nolimits T=1`$ exactly.

For $`k\ge2`$, the remaining entropy coefficients are

```math
c_{\alpha,k}=
\frac{2\Gamma(2\alpha+1)}
{(1-\alpha)M_\alpha\Gamma(\alpha+k+1)\Gamma(\alpha-k+1)},
\qquad
c_{\alpha,2}=-\frac{2\alpha}{\alpha+2},\quad
c_{\alpha,k+1}=c_{\alpha,k}\frac{\alpha-k}{\alpha+k+1}.
```

Use the continuous limit at $`\alpha=1`$; reciprocal Gamma zeros give termination at integer orders at least two. The recurrence avoids the removable singularity. Combining the preceding steps yields

```math
\lim_{d\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits 
\bigl(S_\alpha(U_\ell\psi),S_\beta(U_n\psi)\bigr)
=\frac14\sum_{k\ge2}k\,c_{\alpha,k}c_{\beta,k}F_k(U_\ell U_n^\dagger).
```

It also gives the exact-mean-centered finite-family Gaussian limit. Identical Haar marginals turn this covariance into the mean-square increment formula in [the theorem](THEOREM.md). Physical consequences and evidence are separate from these dependencies.

The argument establishes no uniform finite-size error, growing-support or growing-order limit, joint shrinking-time limit, path-space convergence, or extension to prepared-state ensembles. The retained [Floquet test](../studies/floquet/README.md) failed its declared Haar comparisons. Finite-degree contraction checks diagnose implementation errors; they do not replace the all-degree topology or Hu's external approximation theorem.
