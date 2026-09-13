# Entanglement Temporal Fluctuations: checkpoint 08

12 September 2026. Research checkpoint, without an external repository.

Read `REPORT.md` first. This checkpoint clarifies what equilibrium entanglement memory distinguishes, relates two exchanged cuts to established gate invariants, and constructs two exact active-gate 2-designs with different entropy memory. It also records substantial novelty limitations. It is not a submission-ready Letter or a claim of PRL suitability.

The project is separate from Entanglement Trajectories and Boundary-Entangling-Susceptibility. Its scope remains open. No external repository was created or modified. The checkpoint-07 source package was left unchanged.

Contents:

- `REPORT.md`: results, interpretation, limits, and research decision.
- `PROTOCOL.md`: the prospective scope of the new two-cut calculation. Later analytical constructions are identified as exploratory in their notes.
- `foundation/`: unchanged copies of the core covariance derivation and supporting proofs from checkpoint 07, with provenance hashes. Historical references to other old files are not dependencies of the new calculations.
- `finite_purity/`: exact finite-dimensional proof and an independent numerical contraction implementation.
- `inverse/`: exact moment inversion and conditioning analysis.
- `options/`: two-cut entropy derivation and literature assessment.
- `reviews/`: independent mathematical audits and exact symbolic checks.
- `numerics/`, `results/`: direct two-cut contraction and exact-design superoperator checks.
- `REPRODUCE.md`, `reproduce.py`, `VALIDATION.json`: fresh-directory reproduction.
- `MANIFEST.json`: file hashes for the packaged checkpoint, excluding the manifest itself.

Only Python, NumPy, and SciPy are needed for the new checks. No network access, credentials, prior datasets, or state-sampling campaign is required. Run `python reproduce.py` from this directory. The script runs the six declared checks, compares their output JSON with the saved reference, and writes `REPRODUCTION.json` and individual logs. Floating-point checks evaluate exact identities numerically; they are not interval-arithmetic proofs.
