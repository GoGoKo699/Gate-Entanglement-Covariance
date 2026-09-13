# Entanglement Temporal Fluctuations

A standalone research project on how a boundary gate changes the correlation
between before-and-after equilibrium entanglement fluctuations.

**Current result:** for complex Haar states on a balanced d by d cut, every
fixed finite boundary unitary has a limiting entropy covariance determined by
its normalized operator Schmidt spectrum. Diagonal gates are a special case.
The rank limit gives a sharp residual-memory bound on equal boundary factors;
all dual-unitary gates attain it, including boundary SWAP.

This is a derived and internally checked result, not an externally reviewed
publication. PRL is the ambition; originality and broad significance remain
under assessment. No external repository is required to use this package.

## Read in this order

1. [PROJECT_STATUS.md](PROJECT_STATUS.md): current result, physical interpretation,
   numerical evidence, exact finite-size controls, and limitations.
2. [PROJECT_SCOPE.md](PROJECT_SCOPE.md): assumptions, claim registry, and boundaries.
3. [General-gate proof](checkpoints/07/reviews/GENERAL_GATE_REVIEW.md).
4. [Independent corollary audit](checkpoints/07/reviews/ADDITIONAL_COROLLARY_AUDIT.md).
5. [Letter concept](manuscript/LETTER_CONCEPT.md) and [NEXT.md](NEXT.md).
6. [REPRODUCE.md](REPRODUCE.md): reproduce the latest checks without rerunning history.

The new bounded study is under checkpoints/07. Earlier proof notes and evidence
remain under docs, numerics, and figures; their checkpoint-06 overview is archived
under docs/history. Their adverse results are preserved. VALIDATION.json covers
the current package; MANIFEST.json hashes every distributed file except itself.

Entanglement-Trajectories and Boundary-Entangling-Susceptibility are independent
projects and are neither dependencies nor destinations for this work.
