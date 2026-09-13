# Independent numerical audit of checkpoint 09

**Status: passed.** The large departures from the Haar reference survive an independently assembled Floquet matrix, an independent entropy implementation, and complete recomputation of the saved scalar summaries.

The audit imports no production functions. It creates no new state, gate, or circuit cohort and does not diagonalize the Floquet matrix again. Its source is `independent_audit.py`; all numerical findings and recomputed summaries are in `independent_audit.json`.

## Independent construction and anchors

Each saved bond gate is regenerated from its frozen seed using SciPy QR. Every gate agrees exactly with the stored array. The full Floquet matrix is rebuilt by explicit Kronecker embeddings of each gate, followed by matrix multiplication in the frozen layer order. This is independent of the production tensor-contraction implementation. All saved eigenvectors are checked against the rebuilt matrix.

The three probe matrices are redefined directly and embedded by Kronecker products. At the frozen 16 equally spaced eigenphase indices per size, all three probe outputs are reshaped into coefficient matrices; their reduced density matrices are diagonalized with a Hermitian eigensolver. The resulting entropies and purities are compared against the production singular-value calculation. No spectral value is discarded. The same anchors check preservation of the entire Schmidt spectrum under the circuit's own central crossing gate.

| Audit quantity | Eight spins | Ten spins |
|---|---:|---:|
| Eigenvectors checked | 256 | 1,024 |
| Largest eigen residual | 1.47e-14 | 2.53e-14 |
| Largest orthogonality entry error | 1.43e-14 | 2.49e-14 |
| Entropy outputs independently checked | 48 | 48 |
| Largest entropy discrepancy | 6.22e-15 | 4.88e-15 |
| Largest purity discrepancy | 2.78e-16 | 8.33e-17 |
| Largest own-gate Schmidt-probability change | 9.99e-16 | 6.52e-16 |
| Largest own-gate entropy change | 2.22e-15 | 1.78e-15 |

Eigenphases are sorted correctly. Circular gaps and gap ratios, the minimum gap, and computational-basis inverse participation ratios reproduce. No evidence of an indexing mistake or incorrect eigenvectors was found.

## Summary statistics and references

Every input/output entropy and purity mean, variance, covariance, correlation, mean shift, and mean squared increment is recomputed from every saved state, using NumPy's population covariance rather than the production routine. Every derived comparison ratio, residual, individual band criterion, joint criterion, and nontrivial-probe correlation difference is checked. The largest discrepancies in the complete summaries are 1.96e-13 and 2.59e-12, respectively, both in ratios using independently evaluated von Neumann reference variances.

Finite-dimension purity means, variances, and gate correlations are evaluated with rational arithmetic and the explicit SWAP/phase-SWAP expressions. Page's mean and the von Neumann variance are evaluated through finite harmonic sums, independently of the production digamma and trigamma calls. The limiting entropy covariances are recomputed using closed coefficients for the three chosen orders and a 64-term geometrically convergent sum, rather than the production coefficient recurrence. Reference values agree within 8.89e-16 in absolute value.

Both sizes retain the reported large input variance enhancements and large nontrivial-probe correlations. Their failure of the declared Haar bands is a feature of the selected cohorts, rather than a numerical construction error revealed by this audit. The audit does not promote these two dependent sizes of one nested disorder family into a statement about typical Floquet ensembles or their thermodynamic limit.

## Provenance and limits

The protocol and stored predictions match their original freeze hashes. The initial source retained in `history/floquet_test_initial.py` also matches its freeze hash. The current source differs from that initial version solely by a NumPy-scalar conversion in JSON serialization; the audit checks this exact textual difference. Saved result hashes agree with the current source, original protocol, and frozen predictions.

Full entropy recalculation is limited to the frozen 16 representative states per size. All eigenvectors and all saved scalar arrays are audited, but full entropy recalculation for every saved eigenvector is not claimed. The independent audit reproduces selected spectral and participation diagnostics; it does not independently recompute the production symmetry-commutator diagnostics. Its numerical tolerances concern implementation validation, not confidence intervals or asymptotic error estimates.
