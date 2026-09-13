# Reproduction

Extract the ZIP into a fresh directory, enter its `Entanglement-Temporal-Fluctuations-Checkpoint-09` folder, and run:

```bash
python reproduce.py
```

Python, NumPy, SciPy, and Matplotlib are required. The recorded versions are in `VALIDATION.json` and `requirements-reproduction.txt`. No network access, credentials, previous datasets, or external repository is required.

This command independently recalculates the Haar references, rebuilds and diagonalizes the same two frozen Floquet operators, regenerates every saved response, runs the separate numerical audit, and rebuilds the scientific figure. It uses one BLAS thread and does not add a scientific sample. Outputs overwrite the calculation's own generated arrays and summaries.

Before rerunning, `reproduce.py` retains the saved physical arrays in memory. It then compares regenerated arrays, allowing arbitrary eigenvector phases, and compares summaries with elapsed wall time excluded. Individual mathematical and residual checks remain separate. The production file checks that the existing frozen predictions have not changed; a mismatch is retained as an error rather than silently replacing those predictions.

Results are written to `REPRODUCTION.json` and `reproduction_logs/`. The packaged `VALIDATION.json` records the original fresh-directory reproduction and is not overwritten. Floating-point array bytes may differ on another platform; the script reports byte identity separately from numerical agreement. NPZ archive bytes include packaging metadata, so array contents are the relevant comparison.

The initial source freeze is preserved in `FREEZE.json` and `history/floquet_test_initial.py`. `IMPLEMENTATION_AMENDMENTS.md` records the sole serialization repair. The independent audit verifies that this is exactly the difference between the initial source and the running source. No scientific settings or thresholds changed.

`foundation/` contains unchanged prior theory. Its provenance records the source checkpoint hashes. Those historical numerical campaigns are not repeated by this command. `MANIFEST.json` describes the original delivered package; rerunning changes generated runtime fields, logs, and potentially floating-point bytes.
