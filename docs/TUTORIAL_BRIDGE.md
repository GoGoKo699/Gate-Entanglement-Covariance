# From Wishart fluctuations to gate entanglement covariance

For each random pure state, compare its entanglement before and after a gate on a small part of each half. Does an input with above-average entanglement remain above average? The marginal entropy distribution cannot answer this paired question.

This bridge continues the selected passages of Mingo and Speicher in the [reading map](START_HERE.md). The book supplies Gaussian contractions, Wishart spectra, and the language of trace fluctuations. The quantum dictionary, gate contraction, and entropy normalization below connect that background to this project. [Theorem](../theory/THEOREM.md) is the canonical statement; [Proof](../theory/PROOF.md) is the complete derivation. Readers comfortable with the dictionary may use CHECK directly.

## 1. The observable compares the same state

A complex-Haar pure state is uniformly distributed on the unit sphere, with an irrelevant overall phase. Multiplication by a fixed unitary preserves that distribution. Thus, for $X=S_\alpha(\psi)$ and $Y=S_\alpha(U\psi)$, the marginal means and variances agree exactly at every dimension. This does not make $X$ and $Y$ independent: both use the same $\psi$.

The three related observables are

```math
\mathop{\mathrm{Cov}}\nolimits (X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)],\qquad
\mathop{\mathrm{Corr}}\nolimits (X,Y)=\frac{\mathop{\mathrm{Cov}}\nolimits (X,Y)}{\mathop{\mathrm{Var}}\nolimits X},
```

```math
\mathbb E[(Y-X)^2]=2\mathop{\mathrm{Var}}\nolimits X-2\mathop{\mathrm{Cov}}\nolimits (X,Y).
```

The correlation formula uses the equal, nonzero marginal variances. Covariance retains the fluctuation scale; correlation divides it out; the mean-square increment measures a typical squared change. Independently resampling the second input would instead give zero covariance. “Memory” here means this ensemble correlation, with no storage protocol or general time-decay law implied. The gate need not belong to a time evolution.

## 2. A quantum state becomes a normalized Wishart matrix

Choose bases for two halves of equal dimension $d$ and write

```math
|\psi\rangle=\sum_{A,B=1}^d C_{AB}|A\rangle|B\rangle,
\qquad \mathop{\mathrm{Tr}}\nolimits (CC^\dagger)=1.
```

Tracing out the second half means summing its matching basis index: $(\rho_A)_{AA'}=\sum_B C_{AB}\overline{C_{A'B}}$. Hence $\rho_A=CC^\dagger$. Its eigenvalues $\lambda_j$ are the squared singular values of $C$, or **state Schmidt probabilities**. They sum to one. Entanglement of this pure state is measured by a spectral function:

```math
S_\alpha=\frac{\log\sum_j\lambda_j^\alpha}{1-\alpha}\quad(\alpha>0,\ \alpha\ne1),
\qquad S_1=-\sum_j\lambda_j\log\lambda_j.
```

All logarithms are natural; $0\log0=0$. Order two is negative log purity; order one half is pure-state logarithmic negativity. No separate mixed-state negativity result is involved.

Let $G$ have independent entries $(x+iy)/\sqrt2$, with independent real $x,y\sim N(0,1)$. Thus $\mathbb E|G_{AB}|^2=1$ and unconjugated Gaussian covariances vanish. Then $C=G/\|G\|_F$ is exactly Haar. Split the half-indices as $A=(a,i)$ and $B=(b,j)$, where $a,b$ have fixed dimensions $r,s$ and $i,j$ have growing spectator dimensions $d/r,d/s$. A gate $U_\ell$ acts only on $ab$:

```math
(G_\ell)_{ai,bj}=\sum_{c,e}(U_\ell)_{ab,ce}G_{ci,ej},\qquad
W_\ell=G_\ell G_\ell^\dagger/d,\qquad
\rho_\ell=W_\ell/T,
```

```math
T=\mathop{\mathrm{Tr}}\nolimits W_\ell=\|G\|_F^2/d.
```

Here $T$ is a scalar trace; the spectator subsystem labelled $T$ in the setup and worked example is a separate use of the letter. Unitarity makes the shared $T$ exact, not an asymptotic replacement by its mean $d$. Each $G_\ell$ separately is an iid standard complex Gaussian matrix; each $W_\ell$ is square Wishart. The book's $XX^*/N$ in Section 4.5.1 matches our $W$ when $N=d$ and the aspect ratio is one. Its limiting empirical density is

```math
\mu_{\mathrm{MP}}(x)=\frac{1}{2\pi}\sqrt{\frac{4-x}{x}},\qquad 0<x<4.
```

This density integrates to one and has no atom at zero in the square case. Its integrable divergence there is the hard edge encountered below. The eigenvalues of $\rho_\ell$, in contrast, have size $1/d$. For an even total qubit count $n$ with a balanced cut, $d=2^{n/2}$; $d$ is the half-dimension, not the number of qubits.

The joint matrices retain the gate through

```math
\mathbb E[(G_\ell)_{ai,bj}\overline{(G_m)_{cu,ev}}]
=\delta_{iu}\delta_{jv}(V_{\ell m})_{ab,ce},\qquad
V_{\ell m}=U_\ell U_m^\dagger.
```

The Kronecker deltas identify matching spectator indices. The joint family is a linear image of the same Gaussian array and may have singular covariance. The book initially defines Gaussian vectors using a positive-definite covariance; Wick's rule extends to these degenerate linear images by continuity. This correlated Gaussian representation is the starting point of the proof. Wishart marginals alone imply neither independence, asymptotic freeness, nor second-order freeness between the gate-related matrices.

## 3. Fluctuation modes separate the spectral contributions

The book distinguishes normalized $\mathrm{tr}=d^{-1}\mathop{\mathrm{Tr}}\nolimits $ for a limiting eigenvalue distribution from unnormalized $\mathop{\mathrm{Tr}}\nolimits $ for fluctuations. Our centered statistic is

```math
X_d(f,\ell)=\mathop{\mathrm{Tr}}\nolimits f(W_\ell)-\mathbb E\mathop{\mathrm{Tr}}\nolimits f(W_\ell).
```

Its typical size is order one for the fixed test functions used here. A central limit theorem for these traces concerns spectral fluctuations around the mean, not the order-$d$ trace itself.

The normalization dictionary is important. The book's first-kind convention on author-PDF folio 129 is $C_k(x)=2T_k(x/2)$, with $T_k(\cos\theta)=\cos(k\theta)$. Example 42 on folios 160–161 applies a further Wishart shift and scale. In its square case, the shift is $2$ and the scale is $1$, giving our

```math
\Gamma_k(x)=C_k(x-2)=2T_k((x-2)/2),\qquad k\ge1.
```

In particular, $\Gamma_1=x-2$ and $\Gamma_2=x^2-4x+2$. These are first-kind fluctuation polynomials. They need not be the polynomials orthogonal for the Marchenko–Pastur density used in first-order spectral averages.

Writing $f(2+2\cos\theta)=a_0+\sum_{k\ge1}a_k\cos(k\theta)$ means the coefficient of $\Gamma_k$ is $a_k/2$. For a single Wishart matrix, the limiting covariance of the $\Gamma$ traces is $\delta_{jk}k$. Replacing each $\Gamma_k$ by $T_k((x-2)/2)$ divides the covariance by four. Constant terms disappear on centering.

Use the book's explicit exact-mean centering on folios 156–157 when reading fluctuation limits. The selected route excludes the uncentered convergence wording in Theorem 1 on folio 128 and the inconsistent orthogonality formula in Exercise 12(iii), Eq. (5.32). Neither is needed for our argument: $X_d$ above fixes the centering, and the displayed definition of $C_k$ fixes the amplitudes. The [source caveats](../reviews/mingo-speicher-reader-route/IMPLEMENTATION.md#source-caveats) record these discrepancies and their scope.

Why label by $k$ instead of just using powers of $W$? A power trace contains a sum of fluctuation modes. In the leading connected two-trace contraction, $k$ is the half-length of the surviving alternating row-column cycle: there are $k$ row and $k$ column vertices. Tree attachments can increase polynomial degree without changing this cycle. Thus $k$ is not an entropy order or a Schmidt rank. Chebyshev polynomials separate these contributions, so different mode indices have zero limiting covariance. The book explains diagonalization; the following step determines what couples the two observations in this project.

## 4. The surviving cycle carries the gate spectrum

For jointly Gaussian entries, Wick's rule computes a product expectation by summing products of two-entry covariances over pairings. In our complex convention only conjugated pairings survive. Covariance subtracts the pairings disconnected between its two trace factors. More generally, a joint cumulant subtracts all contributions disconnected across its arguments: the second cumulant is covariance, and Gaussian limits have vanishing higher cumulants.

At fixed active dimensions, leading connected spectator contractions are planar and have one cycle. Every attached tree uses same-gate pairings, where unitarity gives identity covariances. These attachments have ordinary Wishart weights. The remaining cycle carries the relative gate $V$, not an additional assumption of freeness. [Proof, Section 2](../theory/PROOF.md#2-connected-contractions-and-the-surviving-cycle) gives the indices and the power counting; Section 3 controls the higher cumulants.

To read its weight, **realign** the active gate matrix by grouping its first-half input and output indices together:

```math
\mathcal R(V)_{(a,c),(b,e)}=V_{ab,ce},\qquad
Q(V)=\mathcal R(V)\mathcal R(V)^\dagger/(rs).
```

Realignment is a rearrangement into an $r^2\times s^2$ matrix, not a partial trace of the input state. Unitarity gives $\mathop{\mathrm{Tr}}\nolimits Q=\|V\|_F^2/(rs)=1$. Its nonzero eigenvalues $\eta_h$ are the **operator Schmidt probabilities** of the gate. Equivalently, in Hilbert–Schmidt orthonormal operator bases,

```math
V=\sqrt{rs}\sum_h\sqrt{\eta_h}\,A_h\otimes B_h.
```

These probabilities concern product operators in $V$, not entanglement probabilities $\lambda_j$ in $\psi$.

For one link of the cycle, summing the second-half indices gives

```math
(\mathcal R\mathcal R^\dagger)_{(a,c),(a',c')}
=\sum_{b,e}V_{ab,ce}\overline{V_{a'b,c'e}}.
```

Closing $k$ such links takes a matrix trace. The spectator normalization supplies $(rs)^{-k}$, leaving

```math
F_k(V)=\mathop{\mathrm{Tr}}\nolimits Q(V)^k=\sum_h\eta_h(V)^k.
```

The familiar tree count and the additional gate contraction therefore combine as

```math
\lim_{d\to\infty}\mathop{\mathrm{Cov}}\nolimits 
\left(X_d(\Gamma_j,\ell),X_d(\Gamma_k,m)\right)
=\delta_{jk}\,kF_k(V_{\ell m}).
```

This gate factor is derived in the repository, not quoted from Mingo and Speicher. The primary annular-Wishart and Chebyshev sources are credited as [R1–R2](REFERENCES.md). For two nonidentity gates, use $U_\ell U_m^\dagger$: knowing their individual operator spectra generally does not supply this relative spectrum.

## 5. Normalization turns spectral modes into entropy fluctuations

Polynomial covariance is not yet entropy covariance. For fractional $\alpha$, $x^\alpha$ is not a polynomial and can have singular derivatives at the hard edge $x=0$. At order one the statistic involves $x\log x$. The book itself flags the need for additional analytic justification beyond polynomials on author-PDF folio 160. The following input supplies the needed control here.

The analytic input is Henry Hu's square-LUE variance convergence and approximation result [R4](REFERENCES.md), explained in [Proof, Section 4](../theory/PROOF.md#4-transfer-to-entropy-test-functions). Its hypotheses require bounded real test functions with a finite weighted squared difference-quotient integral on a neighborhood of $[0,4]$; the weights account for the square-root singularities at both spectral edges. The matrix is complex LUE with fixed nonnegative integer rectangularity; our square case has rectangularity zero. That source's rectangularity parameter is unrelated to entropy order. This is a credited proof input, not a second assigned tutorial.

Here one first multiplies $x^\alpha$ by a bounded smooth upper cutoff equal to one near $[0,4]$. The hard-edge condition contains $\int_0^\delta x^{2\alpha-1}dx$, finite for every fixed $\alpha>0$; the remaining edge factors are integrable. The analogous condition holds for $x\log x$, defined as zero at zero. Gaussian norm tails and fixed polynomial moments then remove the upper cutoff in $L^2$.

The resulting approximation controls the centered traces in mean square:

```math
\lim_{M\to\infty}\limsup_{d\to\infty}
\|X_d(f,\ell)-X_d(p_M,\ell)\|_2=0.
```

Thus polynomial mode formulas transfer to the entropy test functions. Marginal $L^2$ control and Cauchy–Schwarz bound errors in cross-covariances even though the gates are correlated. A distributional CLT alone would not justify covariance convergence: rare large values can carry second moments without altering a distributional limit. Dimension goes first, approximation degree second.

Now use the exact shared trace. For $\alpha\ne1$,

```math
S_\alpha=\frac{\log Y_\alpha-\alpha\log T}{1-\alpha},\qquad
Y_\alpha=\mathop{\mathrm{Tr}}\nolimits W_\ell^\alpha.
```

Both $Y_\alpha$ and $T$ are order $d$, with centered fluctuations of order one. Let $M_\alpha=\lim_d\mathbb EY_\alpha/d$ and $Z=T-d$. The controlled logarithmic expansion gives

```math
d(S_\alpha-\mathbb ES_\alpha)
=\frac{X_d(x^\alpha,\ell)}{(1-\alpha)M_\alpha}
-\frac{\alpha}{1-\alpha}Z+o_{L^2}(1).
```

Mode one is precisely $X_d(\Gamma_1,\ell)=Z$, common to all gates with $F_1=1$. Its coefficient in $x^\alpha$ is $2\alpha M_\alpha$ in the cosine convention, so it cancels in the displayed entropy combination. This is the radial Gaussian-norm fluctuation: normalizing the state removes it. At order one, $S_1=\log T-\mathop{\mathrm{Tr}}\nolimits (W_\ell\log W_\ell)/T$ gives $d(S_1-\mathbb ES_1)=(3/2)Z-X_d(x\log x,\ell)+o_{L^2}(1)$, with the same cancellation.

The $L^2$ remainder requires more than formal Taylor expansion. The proof uses variance convergence for uniform integrability and bounds the combined normalized entropy on exceptional events by $0\le S_\alpha\le\log d$. Subtracting its exact finite-$d$ mean preserves the vanishing remainder; replacing that mean by only its leading asymptotic value is unnecessary.

The surviving cosine coefficients are the $c_{\alpha,k}$ defined canonically in [Theorem](../theory/THEOREM.md). Their kernel starts at $k=2$:

```math
K_{\alpha\beta}(V)=\frac14\sum_{k\ge2}k c_{\alpha,k}c_{\beta,k}F_k(V)
=\lim_{d\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits (S_\alpha(U_\ell\psi),S_\beta(U_m\psi)).
```

Centered entropies scale as $1/d$, hence the $d^2$ covariance scaling. A finite normalized correlation concerns shrinking absolute fluctuations.

## 6. Return to what boundary access permits

For the same entropy order, the kernel is a positive weighted average of the $F_k$ after dividing by its value at the identity gate. At most $R=\min(r^2,s^2)$ operator probabilities are nonzero, so convexity gives $F_k\ge R^{1-k}$. This yields the positive fixed-access correlation floor. For equal active dimensions, gates whose realignment is also unitary are called dual-unitary. They have $R$ flat probabilities and attain the floor. The universal rank bound does not assert attainability for every unequal pair of active dimensions.

Order two uses only $F_2$, the operator purity. Other orders include further modes. The existing [equal-purity example](WORKED_EXAMPLE.md#same-operator-purity-different-higher-order-covariance) illustrates that these can distinguish gates with the same $F_2$. Integer orders successively reveal power sums: with known finite rank, ideal exact hierarchy data determine the probability multiset. This inversion can amplify small errors severely, and recovers neither operator bases nor a complete gate. Its precise conditions are in [Theorem](../theory/THEOREM.md#what-the-hierarchy-identifies).

Continue with the uninterrupted [gate-to-prediction example](WORKED_EXAMPLE.md), then [results and evidence](RESULTS.md). These conclusions assume balanced complex-Haar input, fixed active dimensions, fixed deterministic gates in finite families, and fixed positive orders. The failed Floquet comparison remains a limitation on a proposed prepared-state extension. There is no uniform finite-size error, growing-support, growing-order, shrinking-time, or sample-path theorem here.

## Self-checks

1. **If before and after means agree, must the entropy be unchanged for each state?** No. Equal Haar marginals fix one-observation statistics; the paired covariance measures their relation.
2. **Can two separately generated Wishart matrices reproduce the gate comparison?** Their marginals can match, but their joint law and shared trace generally do not. The relative-gate entry covariance is needed.
3. **Is $\eta_h$ a small eigenvalue of the reduced density matrix?** No. $\eta_h$ is an operator probability of the gate; $\lambda_j$ is a state probability. They enter different steps.
4. **Why is the conserved mode $k=1$ absent from the entropy kernel?** It fluctuates only with the common Gaussian norm. Dividing $W$ by its exact trace cancels its leading contribution to entropy.
5. **Does a limiting correlation of $1/4$ mean a quarter of the total entanglement survives?** No. It compares centered fluctuations whose amplitude vanishes as $1/d$; it is not a fraction of the entropy itself.
