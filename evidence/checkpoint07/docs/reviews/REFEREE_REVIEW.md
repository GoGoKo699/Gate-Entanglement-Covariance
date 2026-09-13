# Independent skeptical review of the temporal-fluctuation candidate

Review date: 2026-09-12. Scope: the fixed-time, balanced complex-Haar ensemble covariance under the stated norm-one ZZ gate. This is an internal scientific review, not external peer review. I read checkpoint 05's REPORT.md, ALL_DEGREE_REVIEW.md, NONSMOOTH_EXTENSION.md, LETTER_CONCEPT.md, and the supporting polynomial and nonsmooth audit notes. I also inspected the primary text of Hu's low-regularity theorem. No new simulation was run and checkpoint 05 was not changed.

## Decision

The current result justifies a separate, clearly scoped research project now. It has its own ensemble, observable, analytical mechanism, reproducible data, and limiting statement. Its intellectual center is equilibrium temporal covariance under a prescribed local gate, not the former repository's trajectory atlas or chronology-dependent metric disagreements.

I did not identify a material mathematical gap in the stated fixed-time covariance argument. The passage from that covariance to the three short-lag regimes is consistent, provided the dimension limit is taken first as stated. This finding does not validate stronger process-topology, sample-path, finite-size crossover, or generic quench claims.

The PRL case is still unsettled. A specific comparison below makes the originality risk sharper: the leading anomalous exponent and its coefficient are also produced by a smooth scalar-correlated Gaussian interpolation. The ZZ-specific addition to the kernel affects finite-time memory but not the leading short-lag law. The paper should directly acknowledge this comparison before presenting the quarter-order crossover as its main physical novelty.

## Mathematical assessment

### The polynomial kernel

The connected Wick graph reasoning is coherent. For two trace faces the leading quotient graph is planar and unicyclic. A bridge occurs twice in total across the two trace walks, and a closed walk must traverse that bridge an even number of times. Both occurrences therefore belong to the same trace. Its entry phases cancel exactly, so the attached tree decorations have the ordinary Wishart weights.

Only the unique alternating cycle retains cross-time phases. Its normalized index sum is a trace power of the phase matrix times its adjoint. For equal Pauli sign sectors that matrix reduces to the displayed 2 by 2 block with squared singular values cos²τ and sin²τ. The Catalan forest count and cyclic gluing factor then yield the stated shifted-Chebyshev covariance. The higher connected-cumulant power count is compatible with finite-dimensional Gaussian convergence at fixed degrees and fixed times.

I found no extra leading mixed-time branch omitted by that argument. Exact enumeration through degree four supports the derivation but is correctly treated separately from the all-degree argument.

### The nonsmooth extension and normalization

Hu's Theorem 1.1 supplies variance convergence for bounded test functions satisfying its weighted difference-quotient condition, and Corollary 1.3 supplies the corresponding scalar CLT. The author's rectangularity convention includes zero. The power-function hard-edge check reduces to an integrable radial factor x^(2α−1) for every fixed α>0. Thus the theorem genuinely addresses the low-order range that matters here; the quarter-order dividing point is not a failure of the static entropy CLT.

Stationary one-time L2 approximation is sufficient to transfer a polynomial covariance and Gaussian limit to any fixed finite collection of times. It does not require an independently known temporal Wishart CLT. The combined entropy delta-method argument is also sound in its stated form: use variance convergence and distributional convergence for uniform integrability of centered linear-statistic squares; control the high-probability logarithmic remainder in L2; control the exceptional event using the entropy bound together with exponentially small Gaussian probability. For increments, the trace-normalization logarithm cancels exactly because the actual ZZ flow preserves the Frobenius norm.

Primary theorem inspected: Henry Hu, *On the regularity conditions in the CLT for the LUE*, arXiv:2310.08509v1, Theorem 1.1, Lemma 1.2, Corollary 1.3, and Section 1.2. https://arxiv.org/html/2310.08509v1

### What the mean-square conclusion does and does not say

The derived series is a legitimate limiting second moment. The coefficient decay c_(α,k) approximately k^(−1−2α) and the mode crossover kτ² approximately 1 give |τ|^(8α), τ² log(1/|τ|), and τ² in the three stated ranges. At ordinary orders 1/2, 1, and 2 the result is quadratic.

Finite-dimensional Gaussian limits are enough to specify a Gaussian field with this covariance. They do not, by themselves, give convergence of entire finite-dimension trajectories in a path-space topology. The existing documents appropriately avoid almost-sure nondifferentiability and fractional Brownian motion claims.

The phrase “temporal mean-square regularity” is defensible if the limit and rescaling are written beside it. Bare statements that “entanglement becomes rough” or “smooth evolution generates nonsmooth entanglement trajectories” would exceed the result. Each finite-dimension generic full-rank sample remains locally smooth. The absolute entropy-fluctuation amplitude shrinks as 1/d.

## A concrete originality comparison

Consider an auxiliary smooth Gaussian matrix family

    G_sc(t)=cos(t)G_0+sin(t)G_1,

where G_0 and G_1 are independent standard complex Gaussian matrices. Its entry covariance at two times is the scalar cos(t−s). Repeating the same fixed-polynomial Wick cycle argument gives the ordinary scalar-correlated mode kernel

    F_sc,k(τ)=cos(τ)^(2k).

This is a comparison derived from the same established Gaussian fluctuation machinery, not an assertion that an earlier paper has already printed the present Rényi exponent. The normalized entropy fluctuation removes mode k=1 as before. Therefore its limiting increment variance is

    V_sc,α(τ)=(1/2) Σ_(k≥2) k c_(α,k)^2 [1−cos(τ)^(2k)].

The actual local ZZ result obeys the exact relation

    V_ZZ,α(τ)−V_sc,α(τ)
      =−(1/2) Σ_(k≥2) k c_(α,k)^2 sin(τ)^(2k).

For every fixed α>0, the static variance series Σ k c_(α,k)^2 converges. Consequently,

    |V_ZZ,α(τ)−V_sc,α(τ)|
      ≤ (sin(τ)^4/2) Σ_(k≥2) k c_(α,k)^2
      = O(τ^4).

Thus the entire leading three-regime law, including its leading constants, is shared by the smooth scalar-correlated interpolation. It cannot distinguish the physical local gate from that comparison. This is not a mathematical objection to the ZZ theorem. It is a substantive objection to presenting its short-lag exponent alone as a specifically local-unitary physical discovery.

The finite-time kernels are genuinely different. At τ=π/2 the ZZ gate is a product unitary and entanglement returns exactly, whereas G_sc(π/2)=G_1 is independent of G_0. The extra sin term encodes that distinction. This gives a cleaner place to look for the contribution: the complete relation between a physical gate and the memory of equilibrium entanglement, with the hard-edge temporal law as a consequence.

Within the current proved example, cos²τ and sin²τ are precisely the normalized operator-Schmidt weights of

    exp(−iτ Z⊗Z)=cos(τ) I⊗I−i sin(τ) Z⊗Z.

Accordingly, F_k is their k-th power sum. This observation needs attribution against established operator-entanglement and entangling-power work before being promoted as new. It is an interpretation of the existing kernel, not a claim here of a theorem for arbitrary gates.

Relevant established background includes Kusalik, Mingo, and Speicher's Wishart fluctuation framework, https://arxiv.org/abs/math/0503169, and Kuan and Zhou's temporal overlapping-Wishart fields, https://arxiv.org/abs/2112.13728. The latter confirms that temporal Gaussian Wishart fields themselves are established territory; its abstract does not settle exact overlap with the present gate kernel. The direct scalar-interpolation comparison above is the relevant concrete warning, not an originality verdict from a keyword search.

## Physical scope and PRL assessment

Haar stationarity is a strength for isolating a clean covariance and a limitation for physical interpretation. It removes mean growth exactly. It does not demonstrate thermalization, transport, a many-body quench mechanism, or finite-depth circuit preparation. The randomness is in the initial state; the Hamiltonian is fixed. Calling the setup a Haar equilibrium reference is appropriate. Calling it a demonstrated law of typical physical many-body equilibrium requires additional assumptions that this project does not establish.

The most serious significance issue is the restriction of the anomaly to very low Rényi orders. Tiny Schmidt channels matter strongly to those observables by construction. The threshold can therefore look like known random-matrix edge regularity translated into entropy notation. More sizes, additional small ensembles, or a better exponent fit would not answer this criticism.

The exact physical gate kernel and its recurrence are stronger than the derivative-variance result, but a PRL reader still needs to learn something about physical entanglement that is not exhausted by the general scalar-correlated comparison. A compact analytical interpretation is more valuable here than expanding the simulation campaign. The existing finite-pulse data are adequate supporting diagnostics if the analytical claim remains the center and their finite-size deviations remain visible. They should not be called a numerical confirmation of the asymptotic exponent.

My assessment is therefore: scientifically coherent and worth developing; separate-project ready; not yet a secure PRL submission case. This is a judgment about originality and broad physical interest, not a reason to manufacture additional technical requirements for the already stated theorem.

## The single most important remaining question

**What information about physical local evolution is carried by the exact finite-time entanglement covariance that is absent from a generic smooth correlated-Wishart interpolation?**

Answer that comparison explicitly, within the fixed-time covariance scope. The existing operator-Schmidt interpretation and recurrence are concrete starting points. If the answer yields a clear physical relation beyond a new calculable kernel, the Letter has a stronger center. If its only answer is that one can realize the already generic edge exponent with ZZ, the PRL ambition should be downgraded instead of supported by a larger numerical campaign.

## Separation and repository timing

The right moment to separate the project has arrived. A private research repository can contain a concise scope, claim registry, derivation, attributed foundations, one supporting numerical figure, reproduction code, and this open significance question. Its scientific identity should be “temporal entanglement fluctuations under local gates,” without “universal” or a promised journal in the name.

The frozen Entanglement-Trajectories repository should remain unchanged. Link to it only as research history if useful; its model survey, chronology controls, metric-disagreement claims, and failed intermediate research branches are not prerequisites for understanding this project. A clean handover should distinguish the current proven fixed-time claim from conjectures and optional future extensions. Creating the repository establishes a stable research boundary, not a declaration that the PRL case is settled.
