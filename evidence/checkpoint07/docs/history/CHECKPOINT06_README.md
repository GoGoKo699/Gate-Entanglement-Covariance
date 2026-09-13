# Entanglement Temporal Fluctuations

Standalone research project, checkpoint 06, 12 September 2026.

**Question:** How does a specified boundary gate determine the temporal covariance of equilibrium entanglement?

The current result concerns complex Haar pure states on a balanced bipartition of dimension `d × d`. A deterministic diagonal gate acts on fixed finite boundary factors while the spectator dimensions grow. Its normalized operator-Schmidt probabilities determine the covariance of every pair of positive-order Rényi entropies in the large-`d` limit. Randomness is in the initial state; the gate is fixed.

For a single order, write `Cα(τ) = lim d² Cov[Sα(τ), Sα(0)]`. With explicitly known entropy coefficients,

\[
C_\alpha(\tau)=\frac14\sum_{k\ge2}k c_{\alpha k}^{,2}
\sum_\ell\eta_\ell(\tau)^k.
\]

The gate's operator-Schmidt power sums are the memory factors of the spectral fluctuation modes. At order two, the normalized entropy covariance is just operator purity. At other orders it also depends on higher power sums. In particular, we give two diagonal gates with identical operator purity but strictly different entropy autocovariances at every positive order except two.

The derivation and its diagonal-gate extension have internal mathematical reviews. This is a research result under stated assumptions, not external peer review or an originality certificate. A focused literature review found substantial foundations in Wishart fluctuations, operator entanglement, and bipartite OTOCs. PRL significance remains an open assessment.

Start with:

1. [Project scope and claims](PROJECT_SCOPE.md).
2. [Current research assessment](PROJECT_STATUS.md).
3. [Concise manuscript feasibility draft](manuscript/LETTER_DRAFT.md).
4. [General diagonal-gate derivation](docs/proofs/DIAGONAL_GATE_THEORY.md).
5. [Reproduction instructions](REPRODUCE.md).

The package contains the inherited checkpoint-05 proof and data records, a new bounded matched-interaction calculation, figures, and internal reviews. `IMPORTS.json` identifies unchanged imported files; `MANIFEST.json` records the distributed file hashes.

This project is independent of Entanglement-Trajectories and Boundary-Entangling-Susceptibility. Neither repository is a dependency. The former remains a frozen trajectory atlas; the latter studies fresh-gate response and neighboring-cut information. See [the separation document](PROJECT_SCOPE.md) and [the new-workspace handover](START_NEW_WORKSPACE.md).

This folder is ready to become its own research repository. It has no configured Git remote, release, or selected redistribution license. Repository creation and journal submission are separate decisions.
