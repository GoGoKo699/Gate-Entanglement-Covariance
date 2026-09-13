# Focused adversarial novelty review

12 September 2026. Scope: the fixed local ZZ gate, Haar equilibrium entropy autocovariance, and the dimension-first short-time law in checkpoint 05. This is a primary-literature screening and significance assessment, not a mathematical audit or an originality certificate. Checkpoint 05 was read without changes. No new numerical production was run.

## Decision

**No direct prior statement of the complete local-ZZ entropy covariance or its low-order temporal law was located. The project has a defensible independent question, but the novelty risk is substantial if the exponent alone carries the proposed Letter.**

The most important finding is that the exponent and quarter-order threshold also follow for an established smooth Gaussian matrix interpolation. They are consequences of a hard spectral edge, the low-order entropy test function, and quadratic microscopic decorrelation. Local quantum dynamics supplies a particularly constrained physical realization and an exact recurrence kernel. It does not uniquely generate that exponent.

The credible new claim is therefore the physical connection between a fixed bounded local gate and the equilibrium memory of the entanglement spectrum, including all positive Rényi orders. A proved relation to the gate's operator-Schmidt spectrum could organize that connection. Neither operator entanglement nor its relation to average entanglement production is itself new.

The present result warrants an independent research project and a concise manuscript feasibility draft. This review does not establish that its physical significance meets the PRL bar.

## Exact claim being compared

The state is Haar distributed in a balanced complex space of dimension d by d. The deterministic Hamiltonian is a norm-one two-qubit ZZ interaction across the cut, with identity on all other qubits. Define X_(alpha,d)(t)=d[S_alpha(t)-E S_alpha]. The mean is time independent. The proposed fixed-time Gaussian covariance follows from Chebyshev modes with

    F_k(t-s)=cos(t-s)^(2k)+sin(t-s)^(2k).

The limiting mean-squared increment has exponent 8 alpha for 0<alpha<1/4, a quadratic logarithm at 1/4, and quadratic behavior above 1/4. Dimension tends to infinity before the time increment tends to zero. Finite-dimensional convergence and limiting mean-square regularity are the stated scope. Path-space convergence, almost-sure trajectory roughness, Brownian motion, and arbitrary-Hamiltonian universality are not claims under review.

## Nearest mathematical predecessors

| Primary source | What is already established | Residual distinction |
|---|---|---|
| Kusalik, Mingo, Speicher, [math/0503169](https://arxiv.org/abs/math/0503169), J. Reine Angew. Math. 604 (2007) | Wishart trace fluctuations, annular diagrams, and shifted-Chebyshev diagonalization. | The phase carried around an annular cycle must be evaluated for the physical gate. This is a bounded-weight extension of an established calculation, not new fluctuation machinery. |
| Borodin, [1011.3544](https://arxiv.org/html/1011.3544), especially Proposition 3 | Time-dependent Wigner fluctuations have a Chebyshev covariance controlled by powers of the entry correlation. The Ornstein-Uhlenbeck specialization is explicit. | This is Wigner rather than Wishart and does not state a quantum entropy result. It prevents claiming the invention of a temporal Gaussian spectral field. |
| Kuan and Zhou, [2112.13728v1](https://arxiv.org/html/2112.13728v1), Theorem 1.1 and proof | Joint Gaussian fluctuations for overlapping Wishart matrices whose entries evolve in time. The entry processes need not be Markov. Their temporal correlation assumptions are homogeneous in matrix indices. | Our two sign sectors have different complex cross-time phases. The theorem cannot simply be quoted with one scalar correlation, and the coupled real/imaginary phase process also needs care. The annular proof is nevertheless a very close precedent. |
| Friesen, Löwe, Stolz, [1203.4387](https://arxiv.org/html/1203.4387), Theorem 2.3 | Gaussian polynomial fluctuations and Chebyshev diagonalization survive classes of dependent entries; the surviving covariance is a weighted pairing sum. | This is not a ready-made statement for the collection of phase-related Wishart matrices, but weighted dependence and polynomial covariance are established territory. |
| Hu, [2310.08509v1](https://arxiv.org/html/2310.08509v1), Theorem 1.1, Lemma 1.2, Corollary 1.3 | At fixed rectangularity, including square complex LUE, a weighted difference-quotient condition gives variance convergence, a CLT, and approximation for nonsmooth spectral statistics. | The checkpoint's marginal approximation and entropy normalization extend the physical temporal kernel. The low-order marginal CLT is inherited mathematics. |

These sources were checked at the indicated theorem or argument level, except Kusalik et al., whose bibliographic statement and role were checked against the checkpoint's already documented derivation. This review does not re-prove their theorems.

## The adverse comparison that a referee can make

Take two independent standard complex Gaussian matrices G_0,G_1 and set

    G_std(t)=cos(t)G_0+sin(t)G_1,
    W_std(t)=G_std(t)G_std(t)^dagger/d.

Every matrix entry has correlation cos(t-s), and every fixed-time marginal is square LUE. The usual Gaussian annular calculation gives the mode factor cos(t-s)^(2k). This comparison is an inference from the established temporal-fluctuation framework above, not a formula identified in a paper about entanglement.

Applying the same entropy approximation and normalization gives an increment series proportional to

    sum_(k>=2) k c_(alpha,k)^2 [1-cos(tau)^(2k)].

Since |c_(alpha,k)| is proportional to k^(-1-2alpha), exactly the same threshold and powers follow. In the low-order regime, the relevant modes satisfy k tau^2 of order one. The extra sin(tau)^(2k) term from ZZ has no leading contribution in that region.

Consequently, one should not claim that the quarter-order exponent is unique to quantum locality, proves chaotic motion, or reveals a new stochastic spectral universality class by itself. The standard interpolation is not evolution by one fixed local quantum Hamiltonian acting on the original state, and does not preserve the ZZ entanglement recurrence. **The fixed physical realization and its complete covariance remain substantive distinctions.**

This comparison also explains why a smooth microscopic trajectory can have a less regular limiting fluctuation statistic without contradicting unitary smoothness. The limiting observable sums infinitely many spectral modes with increasingly short correlation scales. The final result is an explicit instance of this established general mechanism.

## Closest quantum fluctuation work

| Primary source | Overlap | Distinction from the present claim |
|---|---|---|
| Cotler, Hunter-Jones, Ranard, [2010.11922v2](https://arxiv.org/html/2010.11922), Phys. Rev. A 105, 022416 (2022) | Entropy fluctuations after equilibration, Haar-state bounds, random circuits, and Hamiltonian examples. | Main results concern the size and rarity of von Neumann entropy deficits and their suppression with evolution depth, especially smaller subsystems. They do not provide this balanced-cut stationary two-time kernel or low-order increment threshold. |
| Lim, Lou, Tian, [2305.09962](https://arxiv.org/html/2305.09962), Nature Communications 15, 1775 (2024) | Temporal entanglement fluctuations, universality claims, Rényi extensions, and relations to phase derivatives. | Uses long-time dynamics of lattice models and a torus of dynamical phases. Supplementary Eq. 107 relates an observable's variance to its phase-gradient norm. The physical ensemble and observable differ from short-lag Haar-equilibrium covariance; this is nonetheless close framing prior art. |
| Shekhar and Shukla, [2402.01102](https://arxiv.org/html/2402.01102) | Distributions and fluctuations of entanglement measures in parametrized fixed-trace Wishart ensembles. | The evolution parameter is a distribution-level complexity or pseudo-time, as explicitly discussed near Eq. 9. It is not the coherent same-input local-unitary two-time process here. |
| Nadal, Majumdar, Vergassola, [1006.4091](https://arxiv.org/abs/1006.4091) | Large-system statistics of Rényi and von Neumann entropies of random bipartite pure states. | The checked abstract concerns static distributions and large deviations. Static random-state entropy fluctuations should not be presented as the new contribution. |

Cotler et al. and Lim et al. deserve explicit positioning in the introduction. Calling the project simply a theory of temporal entanglement fluctuations would conceal how much of that research theme already exists.

## Operator entanglement and the kernel

For the normalized operator state associated with U_ZZ(t), the nonzero squared operator-Schmidt coefficients are cos(t)^2 and sin(t)^2. Thus the proposed F_k is precisely the kth power sum of this operator-state spectrum. This observation is algebraic, and it is already implicit in the checkpoint's two-sector phase matrix.

Two primary foundations are particularly relevant:

- Zanardi, Zalka, Faoro, [quant-ph/0005031](https://arxiv.org/html/quant-ph/0005031), define average entangling power on product inputs. Zanardi, [quant-ph/0010074](https://arxiv.org/html/quant-ph/0010074), Eq. 12, relates linear-entropy entangling power to operator entanglement of U and U composed with SWAP. These do not assert the same-input equilibrium autocovariance under review.
- Styliaris, Anand, Zanardi, [2007.08570v3](https://arxiv.org/html/2007.08570v3), PRL 126, 030601 (2021), Theorems 1 and 2, prove that the bipartite averaged OTOC equals linear operator entanglement. Their entropy-production interpretation and Appendix C use reduced-channel outputs and random pure states on one subsystem, not the covariance of two entropies of a globally Haar initial state.

For ZZ, the checkpoint's Rényi-2 increment law equals 1-F_2, which is the familiar linear operator entanglement and hence this bipartite OTOC. This is a derived connection between our observable and an existing quantity, not an independent scrambling diagnostic. It must be acknowledged if used for physical interpretation.

No checked source stated that all equilibrium Rényi entropy autocovariances under a finite boundary gate are determined by the gate's complete operator-Schmidt spectrum. A result of that kind would have a more useful conceptual scope than another evaluation of the familiar linear operator entanglement. It must be proved within an explicit gate class before being advertised; diagonal phases are the immediate candidate, and arbitrary gates are not automatically covered.

A recent neighboring preprint, Dowling and Pappalardi, [2605.02995](https://arxiv.org/abs/2605.02995), computes Haar late-time local-operator entanglement for all Rényi indices using free probability. Its v1 text and Appendix D, plus the current v2 abstract, were checked. The setting is an evolved Heisenberg operator and its average operator entropies, including fluctuation control for annealed averages. It does not supply the Haar-state entropy memory law here. It does reinforce that free-probability plus all-order operator-entanglement calculations are an active, established direction.

### Assessment of the proposed isospectral control

During this review the root study selected two diagonal boundary involutions with the same balanced energies +1 and -1, the same norm, and the same initial quadratic entangling strength. Their gate operator-Schmidt weights are proposed to be (cos(t)^2,sin(t)^2) and (cos(t)^2,sin(t)^2/2,sin(t)^2/2). This review does not independently certify that construction or the general diagonal-gate theorem.

Conditional on those checks, the example gives a useful distinction: equal energy spectra and equal short-time coefficients need not imply equal finite-time entanglement memory. One operation has an entanglement revival at pi/2, whereas the other retains only partial ensemble memory. The Hamiltonian spectrum alone cannot detect the operator's factorization across the cut.

This is a suitable compact control for the proposed all-entropy covariance law. It would not by itself be a surprising new theorem about entangling power: local versus entangling operations with the same energy spectrum can already be distinguished by familiar operator entanglement. The new content must remain the exact translation from the gate's operator-Schmidt power sums to the full family of equilibrium entropy covariances, including ordinary orders. The revival contrast illustrates that law and helps make the paper relevant beyond its low-alpha regularity consequence.

## Claims to avoid and a credible compact claim

Avoid the following:

- A new Gaussian or nonsmooth Wishart CLT.
- A universal quarter-order law for physical quantum dynamics.
- Brownian entanglement, fractal trajectories, or almost-sure roughness without the relevant process theorem.
- A finite-dimensional loss of smoothness or a macroscopic fluctuation that survives without rescaling.
- A better small-incremental-entangling threshold. The worst-case alpha=1/2 theorem in [2509.12014v2](https://arxiv.org/abs/2509.12014v2) answers a different question.
- A new way to quantify operator entanglement or another generic discovery that entropies miss spectral structure. The latter would also overlap the recent Schmidt-scale transport study [2609.06643v1](https://arxiv.org/abs/2609.06643v1).

A defensible sentence is:

> We determine how a bounded deterministic local interaction changes the temporal correlations of equilibrium entanglement fluctuations, and show that the dimension-limit mean-square regularity depends on the Rényi order because the balanced Schmidt spectrum reaches zero.

If the diagonal-gate generalization is proved, a stronger organizing statement would identify operator-Schmidt power sums as the spectral-mode memory factors. That could tie a microscopic operation to an entire family of equilibrium fluctuations while retaining the short analytical story.

## PRL assessment and stopping rule

The result has advantages: one elementary physical interaction, parameter-free covariance, modest simulation, and a sharp distinction between microscopic and limiting-observable regularity. It is scientifically separable from the trajectory atlas.

The main editorial weakness remains that the anomalous first-increment orders are below 1/4, outside von Neumann entropy and pure-state logarithmic negativity. The derivation's mechanism is also close to standard random-matrix regularity. A manuscript that advertises only a new exponent in an exotic entropy family risks appearing as a technical application.

The focused next step should clarify whether the fixed gate has an explanatory consequence beyond that exponent. The operator-Schmidt connection is a promising bounded test of this, because it reuses the current calculation rather than adding a model survey. If no such concise physical interpretation survives scrutiny, a specialist quantum-information or mathematical-physics article remains reasonable, but the PRL framing should be downgraded. More Haar samples would not resolve this issue.

## Search record and limits

Two search engines were used, with primary-source follow-up and a recent-paper filter. Searches covered temporal and parametric Wishart fluctuations; Rényi regularity, quarter-order and hard-edge terms; equilibrium entropy autocorrelation; operator-Schmidt spectra; entangling-power variance; and bipartite OTOCs. Search relevance was uneven, including irrelevant results for some exact phrases. Reference following, not keyword absence, supported the comparisons above.

No direct complete overlap was identified in the checked sources. This is not proof of originality, an exhaustive citation-graph search, or external peer review. The source ledger records inspection depth and which distinctions are our inferences.
