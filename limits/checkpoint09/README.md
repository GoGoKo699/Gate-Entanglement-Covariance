# Entanglement Temporal Fluctuations: checkpoint 09

12 September 2026. A bounded test of the Haar entropy-memory law on one nested Floquet eigenstate family. No external repository is needed or created. Entanglement Trajectories and Boundary-Entangling-Susceptibility remain separate.

Read `REPORT.md` first. The test fails its declared comparison bands at both sizes. The exact Haar theorem is unaffected. This is a negative feasibility checkpoint, not a new asymptotic result or a PRL-ready claim.

- `PROTOCOL.md`, `FREEZE.json`: model, probes, predictions, criteria, and pre-response hashes.
- `floquet_test.py`: fixed two-size calculation and summary generation.
- `results/`: frozen reference predictions, complete eigenbases, local gate matrices, every entropy/purity observation, and summaries.
- `theory/`: independently calculated Haar references and exact one-crossing stationarity argument.
- `reviews/`: primary-source review, independent numerical audit, and interpretation.
- `foundation/`: unchanged inherited covariance and finite-purity derivations, with provenance.
- `figures/`, `plot_results.py`: standalone scientific figure and source.
- `IMPLEMENTATION_AMENDMENTS.md`, `history/`: one serialization-only repair after the source freeze. Scientific inputs and criteria were unchanged.
- `REPRODUCE.md`, `reproduce.py`, `VALIDATION.json`: fresh-directory reproduction.
- `MANIFEST.json`: original packaged file hashes, excluding the manifest itself.

There are 256 eigenstates at N=8 and 1,024 at N=10. Each is evaluated for identity and two independent nontrivial probes at three entropy orders. These are correlated complete eigenbases of one nested circuit family, not 1,280 independent circuit realizations. No state bootstrap intervals, new circuit seeds, or additional sizes are used.
