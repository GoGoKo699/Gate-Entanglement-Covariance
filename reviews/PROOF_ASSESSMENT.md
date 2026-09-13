# Proof assessment of the inherited entropy covariance law

13 September 2026. Bounded review for a possible Quantum paper, not a new simulation study or an originality certification.

## Decision

**The mathematical core is defensible now within its stated fixed-support Haar limit.** I found no theorem-threatening gap in the arbitrary-boundary-gate annular contraction, the extension to every fixed positive Rényi order, or exact-mean centering in the entropy delta method. The inherited material contains a genuine all-degree argument; its status is stronger than a finite-degree conjecture supported by numerics.

**It is not yet a submission-ready proof package.** The argument is distributed over notes with historical status updates, and several steps should be made explicit in one paper appendix. This is bounded proof consolidation and exposition, not a requirement to invent another theorem or run a broad numerical campaign. Journal novelty and significance remain separate judgments.

## Scope and claim status

The statement reviewed uses a complex Haar state on a balanced `d × d` bipartition, a deterministic unitary on fixed boundary factors `r × s`, and identity spectators. Let `d` tend to infinity through common multiples of `r,s`. Entropy orders and the finite collection of gates are fixed. The operator Schmidt probabilities are the eigenvalues of `R(U)R(U)†/(rs)`, with `R(U)_(a,c),(b,e)=U_(a,b),(c,e)`.

| Claim | Assessment |
|---|---|
| Arbitrary fixed-degree polynomial covariance is diagonal in `Γ_k(x)=2T_k((x−2)/2)`, with mode weight `k Ση^k` | Supported by an all-degree derivation. The graph topology and active cycle contraction are sound as written; precise index conventions belong in the paper. |
| A finite collection of polynomial traces has a joint Gaussian limit | Supported by the connected spectator-graph cumulant bound `O(d^(2−p))` for `p≥3`. No new multi-gate regularity theorem is required. |
| The limit extends to every fixed positive Rényi order, including order one | Supported. Hu's actual primary theorem supplies variance convergence and approximation; the required hard-edge condition and cutoff removal are satisfied. |
| `d² Cov(S_α(Uψ),S_β(ψ)) → ¼ Σ_(k≥2) k c_(αk)c_(βk) Ση(U)^k` | Defensible as the central theorem, conditional only in the ordinary sense of relying on the cited established LUE result and the displayed proof. No additional unresolved assumption was identified. |
| Multiple gates use the spectrum of `U_l U_m†` | Correct. Individual gate spectra do not determine the relative-gate spectrum. The Gaussian change of variables and covariance tensor give the relative gate directly. |
| Fixed support gives a positive same-order residual-memory bound, attained by dual-unitary gates on equal factors | Direct, sound consequence of the theorem and `Ση^k ≥ R^(1−k)`, `R=min(r²,s²)`. This does not create finite-size or many-body universality claims. |
| Existing low-degree contractions and exact finite-size purity checks prove the nonpolynomial theorem | They do not. They are useful independent controls; the proof rests on topology, marginal approximation, and normalization. |
| Growing support, shrinking time with dimension, varying order, path-space Gaussian convergence, or generic prepared-state universality | Not established by this proof and not needed for the scoped paper. |

“Supported” means independently re-examined here against the inherited argument and, for the nonsmooth theorem, the primary source. It does not mean external peer review or machine-checked proof.

## 1. The non-diagonal all-degree step survives scrutiny

`foundation/GENERAL_GATE_REVIEW.md` supplies the missing ingredient that a diagonal phase argument alone would not supply. In its Gaussian representation,

`E G_l[ai,bj] conjugate(G_m[ck,ev]) = δ_ik δ_jv (U_l U_m†)[ab,ce]`.

The spectator labels obey the ordinary oriented complex-Wishart Wick identifications, while the active labels retain finite tensors. Fixed active dimensions are crucial: their tensor contractions are bounded independently of `d`, so they cannot rescue a spectator graph suppressed by a negative power of `d`.

For connected two-trace Wick graphs, the Euler identity gives `V−E=−2g`. A leading graph is therefore planar with `V=E`, hence unicyclic. Multigraphs must be allowed; the `k=1` backbone is a two-edge cycle. Every edge outside the cycle is a bridge. Each edge appears twice in total across the closed trace walks, and a closed walk crosses a bridge an even number of times. Both appearances of a bridge must consequently belong to the same trace. This is the decisive all-degree argument excluding a hidden mixed-gate tree branch.

Same-gate covariance is the complete identity by unitarity. Peeling a tree leaf supplies `r(d/r)=d` or `s(d/s)=d` and identifies the parent active labels normally. No active operator remains attached to the cycle. The two faces traverse the surviving even cycle in opposite directions, leaving exactly

`Σ ∏_(l=1)^k V[a_l b_l,c_l e_l] conjugate(V[a_(l+1) b_l,c_(l+1) e_l])`.

This is `Tr[(R(V)R(V)†)^k]`. The spectator and Wishart normalizations contribute `(rs)^(-k)`, giving the claimed `F_k(V)`. The orientation is the realignment Gram contraction, not a partial-transpose invariant. The tree count `q_(m,k)=binom(2m,m−k)` and `k` allowed cyclic gluings then reproduce the stated Chebyshev transform. Those counts agree with the exact polynomial identity, including the conserved first mode.

The higher-cumulant argument needs no analogous cycle simplification. For `p` connected trace boundaries, spectator power counting gives `d^(2−p−2g)` and all active sums remain bounded at fixed support and degree. Thus cumulants above order two vanish. Gaussian moment determinacy and Cramér–Wold give the finite-dimensional CLT, including degenerate covariance matrices and noncommuting gates.

This is a sufficiently specific proof mechanism to support the theorem. The finite-degree network code is helpful for index errors but is not what closes the arbitrary-degree step. I found no reason to repeat its gate list or enlarge its degree range.

## 2. The nonsmooth endpoint is closed, rather than merely assumed

I fetched and directly checked Henry Hu, *On the regularity conditions in the CLT for the LUE*, [arXiv:2310.08509v1](https://arxiv.org/html/2310.08509v1), on 13 September 2026. The checked parts were the ensemble normalization (1.2), variance functional (1.4), Theorem 1.1, Lemma 1.2, Corollary 1.3, the notation convention, and the Chebyshev-approximation discussion in Section 3. A source copy is retained at `../source_cache/hu_2310.08509v1.html`, with readable extraction alongside it.

Theorem 1.1 is indeed a **variance-convergence theorem**, not only a distributional CLT. Its fixed rectangularity parameter explicitly permits zero, so the square complex ensemble is covered. The normalized Gaussian variance convention is also the one used by the project. Lemma 1.2 and Section 3 support approximation in the limiting variance seminorm.

For a smooth upper cutoff of `x^α`, the stronger weighted regularity condition near the hard edge reduces, using `y=ux`, to

`[∫_0^δ x^(2α−1) dx] [∫_0^1 ((1−u^α)/(1−u))² (√u+1/√u) du]`.

Both factors are finite for every fixed `α>0`. The mixed hard-edge/soft-edge corners are integrable as well, and the function is smooth near the upper edge. The analogous condition holds for `x log x`. A cutoff beyond the limiting upper edge can be removed in `L²` using the Gaussian operator-norm tail and fixed polynomial moments; the theorem is not being asked to cover unbounded powers directly.

The passage from one marginal to a fixed vector of gates is valid. Every transformed coefficient matrix is exactly standard Gaussian marginally. Approximate each centered statistic by a polynomial in marginal `L²`, first take `d→∞`, and only then the approximation degree to infinity. The triangle inequality controls finite linear combinations, and Cauchy–Schwarz controls cross-covariance errors. Independence between gates is unnecessary. This also explains why a uniform-in-degree annular estimate is unnecessary.

## 3. Centering and logarithmic remainders are handled correctly

For `α≠1`, put `Y_α=Tr W^α`, `μ_α,d=E Y_α`, `X_α=Y_α−μ_α,d`, and `Z=Tr W−d`. The MP mean limit gives `μ_α,d/d→M_α>0`. The transferred CLT **together with** convergence of variances implies uniform integrability of `X_α²` and `Z²`; a CLT alone would not establish this.

On the event `||W||≤K` and `d/2≤Tr W≤2d`, the power trace and its deterministic center lie between positive constants times `d`. The scaled logarithmic Taylor remainder is bounded by `C|X_α|`, with its ratio to `|X_α|` tending to zero in probability. Uniform integrability makes the remainder vanish in `L²` without assuming fourth moments.

The bad-event argument in `NONSMOOTH_EXTENSION_AUDIT.md` is essential and correct: apply `0≤S_α≤log d` to the **combined normalized entropy**, not to its separate logarithms. The bound on the scaled entropy is `O(d log d)` and the bad-event probability is exponentially small. The linear statistics there are controlled by uniform integrability. If the resulting expansion is initially centered at a deterministic `s_0,d`, replacing it by `E S_α` only replaces its `L²` remainder `R_d` by `R_d−E R_d`.

For the paper, explicitly write the order-one calculation currently compressed into “the two-variable version.” Let `Y=Tr(W log W)`, `X=Y−EY`, `m_d=EY/d→1/2`, and `q=Z/d`. With `s_0,d=log d−m_d`, exact algebra gives

`d(S_1−s_0,d)=(1+m_d)Z−X + d[log(1+q)−q] − m_d Zq/(1+q) + Xq/(1+q)`.

On the good trace event, each remainder term is bounded by a constant times `|X|+|Z|`, with a multiplier tending to zero in probability. The same exceptional-event argument therefore yields

`d(S_1−E S_1)=(3/2)Z−X+o_L²(1)`.

The first cosine coefficient of `x log x` is `3`, exactly the first coefficient of `(3/2)x`, so the radial mode cancels. This is an omitted display, not a missing theorem. A separate compact subaudit independently checked the same good-event, bad-event, uniform-integrability, and centering steps.

## 4. What should be finished before submission

1. **Consolidate one self-contained theorem and proof.** State complex Haar, balanced cut, fixed active factors, fixed orders, fixed finite gate set, natural logs, exact mean centering, and the order of limits together. Historical checkpoint language should not serve as the manuscript's logical dependency map.
2. **Define the Wick graph convention explicitly.** A short indexed trace expansion or a permutation formulation should connect the contractions to the Euler identity. Include parallel edges and explain the bridge lemma before tree removal. Retain the explicit active cycle sum and its normalization.
3. **Write the marginal-transfer lemma and entropy lemma fully.** Cite Hu's exact theorem numbers and show the cutoff and finite-vector approximation in successive limits. Include the displayed von Neumann expansion and the combined-entropy exceptional-event estimate.
4. **Keep proof and evidence distinct.** Existing contraction checks, exact Haar purity formulas, and modest entropy illustrations are enough as controls. Their role and finite-dimensional limitations should remain visible. No broad new simulation study is warranted to establish this theorem.
5. **Preserve the boundary of the result.** Whole-half SWAP with growing active dimension is outside the theorem. A positive limiting correlation concerns entropy fluctuations of order `1/d`; it does not imply macroscopic retained entropy, generic thermal-state behavior, efficient experimental reconstruction, or a path-space process theorem.

These are necessary manuscript tasks, but none presently looks like a fatal mathematical gap. On proof grounds, a compact Quantum spinoff centered on the full operator-spectrum covariance law is a reasonable action now. Whether it merits acceptance depends on positioning and significance beyond this audit.
