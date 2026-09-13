# Final adversarial framing review

12 September 2026. Reviewed `REPORT.md` and the standalone project's `manuscript/LETTER_CONCEPT.md`. Scope: claim boundaries, attribution, physical interpretation, and publication framing. This is not a repeat of the independent mathematical or numerical audits.

## Verdict

**No material scientific framing correction is required in the report.** The 25% statement is explicitly a limiting balanced-Haar Rényi-2 correlation bound for a gate acting on one fixed boundary qubit per side. The report does not present it as a finite-dimensional bound or a bound shared by every entanglement measure. Its exact purity comparison demonstrates why that limitation matters.

The Letter concept is suitable as a research concept, with two small wording refinements recommended before reuse in an abstract:

- State that the memory floor is proved sharp **for equal active boundary dimensions**. The report makes this qualification; the shorter concept compresses it away. The unequal-dimension rank bound remains valid, but this report has not established its attainability in every dimension pair.
- Prefer “every fixed positive Rényi order” to unrestricted “all entropy” when the sentence will stand alone. The report's equations and initial scope already supply the correct meaning.

Neither suggestion changes the displayed results or calls for additional simulation.

## Scope checks

| Possible overclaim | Assessment of current text |
|---|---|
| 25% survives at finite d | Explicitly excluded; the phase-decorated SWAP has a smaller finite-d purity correlation, including a negative value at d=2. |
| Every entropy retains 25% | Not claimed. The table gives distinct values for order 1/2, 1, and 2. |
| Haar mean entanglement changes | Correctly states stationarity; the observable is before/after covariance on the same input. |
| Residual memory means a macroscopic fluctuation | Explicitly excluded; fluctuation amplitude is of order 1/d. |
| Any globally acting unitary obeys the floor | Fixed active dimensions and growing spectators are specified; whole-half SWAP is excluded by an explicit counterexample. |
| Equal operator spectra imply identical gate dynamics | Explicitly excluded for interpolating trajectories, multi-step dynamics, and higher finite-d cumulants. The relative gate is correctly identified. |
| Exact purity formulas are exact entropy formulas | Explicitly excluded; the entropy statement transfers only in the large-d limit by the delta method. |
| Finite-pulse data prove a convergence rate or exponent | Explicitly excluded. Pilot sample errors do not include finite-size bias. |
| Independent internal reviews establish external acceptance | Explicitly excluded. |
| Dual unitaries and their entangling-power variation are new | Correctly attributed to prior literature. |

The balanced global Haar distribution is mathematical equilibrium for this question. The report correctly avoids asserting that an arbitrary physical quench reaches this ensemble. “Fixed access” must retain this support-and-ensemble meaning in later abstracts; it is not yet an operational lower bound for noisy protocols, measurement-assisted control, or gate sequences whose active support grows.

## Newly cited primary source checked

Rather, Aravinda, and Lakshminarayan, *Creating ensembles of dual unitary and maximally entangling quantum evolutions*, arXiv:1912.12021v3 / PRL 125, 070501 (2020).

Text: https://arxiv.org/html/1912.12021v3

Inspected the definitions around equations (1), the realignment criterion, and the discussion headed “Characterization of dual unitaries via their entangling power.” The source explicitly identifies dual unitaries with maximal operator entanglement and flat normalized operator-Schmidt probabilities. It identifies the additional invariant E(US) as determining entangling power within the dual-unitary class, and includes SWAP as a dual-unitary example. These statements support the report's attribution. The source does not provide the before/after Haar-state entropy covariance claimed here.

The proposed all-order common memory is therefore a corollary of the current project theorem applied to an established gate class. It should not be advertised as discovering that operator entanglement and entangling power differ.

## Adversarial significance assessment

The clearest insight is that a fixed local operation can change which near-equilibrium entanglement fluctuation a state carries without changing its distribution, and the whole positive-order Rényi family has a quantitative dependence on one microscopic operator spectrum. The rank bound turns this into a simple locality consequence. The dual-unitary comparison makes the observable's blindness to some product-input capabilities explicit.

A skeptical referee could regard the rank bound and dual-unitary equality as elementary corollaries once the covariance formula is available. That objection is reasonable. They clarify the physical meaning but cannot substitute for demonstrating why the formula itself matters. The strongest economical presentation therefore combines:

1. The full operator-spectrum-to-entropy-covariance law.
2. The sharp fixed-support memory floor in equal boundary dimensions.
3. Both directions of distinguishability: equal operator purity can hide different higher-order entropy memories; different product-input capabilities can give identical equilibrium memories.

This is a coherent compact Letter argument. It remains a specialized Haar fluctuation result with shrinking absolute signal, and the second-order random-matrix machinery is established. The current report acknowledges both limitations. No broad thermalization, experimental advantage, new universality class, or guaranteed PRL suitability follows.

**Recommendation:** retain the central result and the cautious publication ambition. Apply the two small scope refinements when condensing the report. Do not enlarge the numerical campaign merely to improve apparent evidential weight; the next useful work is to clarify the information the covariance family contains and the physical circumstances in which that distinction matters.
