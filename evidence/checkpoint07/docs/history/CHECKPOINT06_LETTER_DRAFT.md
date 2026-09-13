# Equilibrium Entanglement Memory under Diagonal Local Gates

**Feasibility draft, 12 September 2026.** This is a proposed scientific narrative for internal assessment. It is not submission-ready, does not establish originality, and retains the adverse numerical comparisons. The analytical statements are restricted to the setting below. References are primary-source links pending a manuscript bibliography.

## Abstract

The average entanglement of a Haar-distributed state is unchanged by any fixed unitary, but its correlation with the initial entanglement can change. We derive that correlation for fixed diagonal interactions across a balanced bipartition, as the spectator dimensions grow. Every spectral fluctuation mode has a memory factor equal to a power sum of the gate's normalized operator-Schmidt spectrum. This gives the covariance of every pair of positive-order Rényi entropies. Equal linear operator entanglement therefore fixes Rényi-2 memory but does not fix von Neumann or logarithmic-negativity memory; an explicit pair of gates has strictly ordered covariance for every positive order except two. The same formula yields a quarter-order crossover in dimension-limit temporal mean-square regularity. Modest exact-pulse calculations resolve a recurrence control, while substantial finite-size deviations prevent a quantitative numerical confirmation of the general covariance formula.

## An equilibrium question about a local operation

A unitary acting on a Haar-distributed pure state preserves its distribution. Any single-time average entanglement measure is consequently insensitive to that operation. A two-time question retains physical information: how much does an initially larger-than-average entanglement remain correlated with the entanglement after a local interaction?

We call this ensemble covariance entanglement memory. It is neither a memory channel capacity nor an individual state's fidelity. The state distribution is stationary, while its correlations across time depend on the operation. This separates an equilibrium fluctuation problem from mean entanglement production on initially separable states.

Entanglement fluctuations after equilibration have established theories, including entropy-deficit bounds in random circuits and Hamiltonian systems [Cotler, Hunter-Jones, Ranard](https://arxiv.org/abs/2010.11922), and mesoscopic temporal fluctuations in lattice dynamics [Lim, Lou, Tian](https://arxiv.org/abs/2305.09962). Our question is narrower: can a fixed finite interaction specify the complete covariance of equilibrium spectral observables?

## A gate spectrum determines the covariance

Let each half have dimension \(d\). The interaction acts on boundary factors of dimensions \(r\) and \(s\), with identities on the remaining factors. Hold \(r,s\), and the real matrix \(h_{ab}\), fixed as \(d\) grows through compatible multiples. The Hamiltonian and gate are

\[
H=\sum_{a,b}h_{ab}|a\rangle\langle a|\otimes|b\rangle\langle b|,
\qquad U(t)=e^{-itH}.
\]

The initial state is complex Haar distributed on the full \(d\times d\) space. Natural logarithms define \(S_\alpha=(1-\alpha)^{-1}\log\operatorname{Tr}\rho_A^\alpha\), with the continuous von Neumann limit at one.

Form the finite matrix

\[
Q_{ab}(t)=\frac{e^{-it h_{ab}}}{\sqrt{rs}},\qquad
F_k(t)=\operatorname{Tr}[(Q(t)Q(t)^\dagger)^k].
\]

The eigenvalues \(\eta_\ell(t)\) of \(QQ^\dagger\) are the normalized operator-Schmidt probabilities of \(U(t)\). Thus \(F_k=\sum_\ell\eta_\ell^k\), and \(F_1=1\). This is the familiar operator-state spectrum, not a newly defined entanglement measure [Zanardi](https://arxiv.org/abs/quant-ph/0010074).

Define \(X_{\alpha,d}=d(S_\alpha-\mathbb E S_\alpha)\). At every finite set of fixed times and positive orders, these variables have a joint Gaussian limit with covariance

\[
\boxed{\mathcal C_{\alpha\beta}(\tau)
=\lim_{d\to\infty}d^2\operatorname{Cov}[S_\alpha(\tau),S_\beta(0)]
=\frac14\sum_{k\ge2}k\,c_{\alpha,k}c_{\beta,k}F_k(\tau).}
\]

Here

\[
M_\alpha=\frac{\Gamma(2\alpha+1)}{\Gamma(\alpha+1)\Gamma(\alpha+2)},\qquad
c_{\alpha,k}=\frac{2\Gamma(2\alpha+1)}{(1-\alpha)M_\alpha\Gamma(\alpha+k+1)\Gamma(\alpha-k+1)},
\]

with continuous interpretation at one. Integer orders greater than one terminate through reciprocal-Gamma zeros. The corresponding mean-squared increment is

\[
\mathcal V_\alpha(\tau)=\frac12\sum_{k\ge2}k c_{\alpha,k}^2[1-F_k(\tau)].
\]

The entropy selects the spectral-mode weights; the operation selects their memory factors. The operator-Schmidt spectrum determines an ensemble covariance, not the entanglement change of a specified individual input.

The derivation uses a Gaussian representation of the Haar state. Diagonal evolution rotates each matrix entry by its boundary-dependent phase. In the leading connected Wishart contraction, attached trees contain equal-time pairings and retain their usual weights. The remaining cycle contributes \(\operatorname{Tr}(QQ^\dagger)^k\). Established shifted-Chebyshev diagonalization removes the attached trees [Kusalik, Mingo, Speicher](https://arxiv.org/abs/math/0503169). Higher connected cumulants vanish at fixed degree.

Each fixed-time marginal remains square LUE. Hu's variance-convergent approximation for nonsmooth linear statistics extends the polynomial covariance to every fixed positive order [Hu](https://arxiv.org/abs/2310.08509). Normalizing the state removes the trace mode \(k=1\). Temporal Wishart Gaussian fields themselves are established mathematics [Kuan, Zhou](https://arxiv.org/abs/2112.13728); the retained phase cycle supplies the physical gate dependence here.

## Equal operator purity does not fix entropy memory

Rényi-2 has only one nonzero coefficient, \(c_{2,2}=-1\). Consequently,

\[
\mathcal C_{22}(\tau)=F_2(\tau)/2,\qquad
\mathcal V_2(\tau)=1-F_2(\tau).
\]

Its limiting Pearson correlation is the gate's operator purity. The increment equals linear operator entanglement, already identified with the bipartite averaged OTOC [Styliaris, Anand, Zanardi](https://arxiv.org/abs/2007.08570). This relation does not make every entropy covariance an OTOC.

A stronger distinction uses two diagonal gates on two boundary qubits per half. A single \(ZZ\) pulse at angle \(\pi/4\), with spectators, has operator probabilities \(\eta^A=(1/2,1/2)\). Two independent commuting \(ZZ\) pulses of equal angle \(\theta\) have

\[
\eta^C=(p^2,pq,pq,q^2),\qquad
p=\cos^2\theta=\frac{1+\sqrt{\sqrt2-1}}2,\quad q=1-p.
\]

Both have \(F_2=1/2\). Their higher power sums differ strictly: \(F_k^C>F_k^A\) for every integer \(k>2\). To see this, let a random variable take values \(p,q\) with probabilities \(p,q\). Its mean is \(p^2+q^2=1/\sqrt2\); strict Jensen inequality gives the result from \(F_k^C=(p^k+q^k)^2\).

All same-order covariance weights are nonnegative. Moreover,

\[
c_{\alpha,3}=-\frac{2\alpha(\alpha-2)}{(\alpha+2)(\alpha+3)}
\]

is nonzero for every positive \(\alpha\ne2\). Therefore gate C retains strictly greater same-order entropy covariance than A for every such order, including von Neumann entropy and pure-state logarithmic negativity \(S_{1/2}\). Rényi-2 memory is exactly equal. This analytical comparison matches operator purity; it does not also match the Hamiltonian energies or interaction norm. No additional simulation was used for this corollary.

## Short-time regularity is a consequence

Double-center \(h\) by subtracting its row and column means and adding its overall mean, obtaining its nonlocal part \(h^c\). Additive local terms leave every \(F_k\) unchanged. For

\[
\chi=\frac1{rs}\sum_{a,b}(h^c_{ab})^2>0,
\]

the largest operator probability is \(1-\chi\tau^2+O(\tau^4)\). Meanwhile \(c_{\alpha,k}\) decays as \(k^{-1-2\alpha}\) at low noninteger order. The increment series gives

\[
\mathcal V_\alpha(\tau)\sim
\begin{cases}
C_\alpha\chi^{4\alpha}|\tau|^{8\alpha},&0<\alpha<1/4,\\
C_\alpha\chi\tau^2\log(1/|\tau|),&\alpha=1/4,\\
C_\alpha\chi\tau^2,&\alpha>1/4.
\end{cases}
\]

The constants are positive and explicitly determined by the coefficient series. Dimension tends to infinity first. Every generic finite-dimensional entropy remains smooth locally, and absolute fluctuations vanish as \(1/d\). No sample-path roughness theorem is implied.

This exponent is not unique to local quantum evolution. A standard smooth Gaussian interpolation \(G(t)=\cos t\,G_0+\sin t\,G_1\) has mode factors \(\cos^{2k}\tau\) and gives the same short-time powers. The fixed-gate calculation supplies a constrained physical realization and complete temporal covariance, including recurrences. Its quarter-order consequence should not be presented as a separate discovery of stochastic spectral fluctuations.

## A bounded numerical illustration and its limits

A distinct control matches the energy spectrum and initial strength. Two four-level diagonal boundary Hamiltonians, A and B, are norm-one involutions with eight positive and eight negative energies and \(\chi=1\). Their gate spectra are respectively

\[
\eta^A(t)=(\cos^2t,\sin^2t),\qquad
\eta^B(t)=(\cos^2t,\tfrac12\sin^2t,\tfrac12\sin^2t).
\]

Their leading short-time laws agree, but finite-time memory differs. At \(t=\pi/2\), A is a product unitary and every state's entanglement returns exactly. B has two equal operator probabilities, giving \(\mathcal V_2=1/2\).

We fixed this comparison before sampling 128 new Haar states: 64 each at \(d=64,128\). Both gates and two pulse times gave 512 exact state evolutions; five entropy orders were evaluated without exclusions or fitted parameters. A's recurrence error was at most \(1.78\times10^{-15}\). For B at \(d=128,t=\pi/2\), the estimate of \(d^2\mathbb E(\Delta S_2)^2\) was \(0.55194\pm0.09013\), consistent with its limiting value \(1/2\).

Other comparisons are unfavorable. For B at \(d=128,t=\pi/4\), von Neumann entropy gave \(0.188963\pm0.027740\), versus the limit \(0.326083\); order one half gave \(0.107929\pm0.016960\), versus \(0.181407\). Errors are sample standard errors over independent states. These differences cannot be described as quantitative confirmation. The small cohort resolves the exact recurrence control and illustrates fluctuation scales, while leaving finite-size accuracy unresolved. The theorem rests on its analytical argument.

## Scope and physical interpretation

The result distinguishes operations through correlations invisible to their unchanged Haar-state marginals. Equal operator purity does not determine that entire response: ordinary entropy orders weight additional operator-Schmidt moments. This is the central conceptual claim; the low-order temporal exponent is a secondary consequence.

The finite active space also imposes a memory floor. If \(m=\min(r,s)\), the operator spectrum has at most \(m\) nonzero probabilities, so \(F_k\ge m^{1-k}\). In particular, the limiting Rényi-2 correlation remains at least \(1/m\), however large the spectator systems become. The same positive spectral weights give a nonzero covariance bound for every fixed positive order. Large spectator dimension supplies the Gaussian fluctuation limit but does not grant a small diagonal contact unlimited ability to erase those fluctuations' initial correlations.

This observation is specific to the declared family. It is not a bound on the information-processing capacity of a general local circuit. Nor does the matched-purity example establish that one gate is uniformly better at preserving a quantum resource: the ordering concerns an equilibrium ensemble covariance, and reverses when expressed as the corresponding mean-squared entropy increment.

The theorem requires diagonal gates with fixed active dimensions. It does not cover arbitrary gates, growing support, physically prepared equilibrium states, chaotic Hamiltonian universality, or a uniform shrinking-time limit. Establishing those extensions is separate work. Within the stated setting, the result provides an explicit correspondence between a finite operation and the memory of collective entanglement fluctuations, with numerical limitations retained rather than absorbed into the asymptotic claim.
