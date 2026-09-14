# Repository map

Use **LEARN** for the physical explanation, **CHECK** for the mathematical statement and derivations, and **REPRODUCE** for executable calculations.

| Question or task | Document or implementation |
|---|---|
| Understand the setup and read the selected background | [Start here](START_HERE.md), [tutorial source and conventions](TUTORIAL_SOURCE.md) |
| Translate random-matrix fluctuations into quantum entropy | [Tutorial bridge](TUTORIAL_BRIDGE.md) |
| Follow a complete two-qubit example | [Worked example](WORKED_EXAMPLE.md) |
| Check the central statement and proof | [Theorem](../theory/THEOREM.md), [Proof](../theory/PROOF.md) |
| Check product gates, SWAP, local basis changes and relative times | [Controls](../theory/CONTROLS.md) |
| Recover operator moments and assess conditioning | [Moment inversion](../theory/MOMENT_INVERSION.md), [exact checks](../checks/inverse/) |
| Relate finite-dimensional purity to entangling power | [Finite purity](../theory/FINITE_PURITY.md), [contraction checks](../checks/finite_purity/) |
| Compare the two subsystem assignments | [Two-cut modes](../theory/TWO_CUTS.md), [independent contractions](../checks/numerics/two_cut_check.py) |
| Understand the gate-design comparison | [Gate designs](../theory/GATE_DESIGNS.md), [exact computation](../checks/numerics/design_pair.py) |
| Derive instantaneous entropy-rate covariances | [Conditional response](../theory/CONDITIONAL_RESPONSE.md), [Haar study](../studies/haar/README.md) |
| Inspect sampled evidence and its limits | [Results](RESULTS.md), [study index](../studies/README.md), [scope](SCOPE.md) |
| Identify the external proof inputs | [References](REFERENCES.md) |
| Evaluate the formulas | [gate_covariance/](../gate_covariance/), [reader reference values](../results/reader_examples.json) |
| Reproduce results and check reference integrity | [Reproduction guide](../REPRODUCE.md), [integrity manifest](../reference_integrity.json) |

The default computation runs six deterministic checks and regenerates the analytical figure and table. It creates no random-state cohort. Study data remain separate by their input ensemble and protocol. New outputs go under build/ or to a separate working directory.
