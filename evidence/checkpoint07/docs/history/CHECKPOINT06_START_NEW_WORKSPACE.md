# Start the separate research workspace

Use a new GPT project named **Entanglement Temporal Fluctuations** and attach this standalone package. If creating its repository, use `Entanglement-Temporal-Fluctuations` as the working name. This package is intended for that new repository, never as an overwrite patch for Entanglement-Trajectories.

The following text is a self-contained handover for the new GPT project:

> We are developing a separate research project on equilibrium temporal entanglement fluctuations. Read README.md, PROJECT_SCOPE.md, PROJECT_STATUS.md, docs/proofs/DIAGONAL_GATE_THEORY.md, and manuscript/LETTER_DRAFT.md first. The goal is an interesting physical insight supported by modest theory and modest numerics, with PRL as an ambition rather than an assumed outcome.
>
> The current theorem concerns complex Haar states on a balanced d-by-d cut and a fixed diagonal gate on finite boundary factors. As d grows, the covariance of each Chebyshev spectral mode is its static variance times a power sum of the gate's normalized operator-Schmidt probabilities. A convergent entropy-mode expansion gives all fixed positive-order Rényi covariances. The proof uses established Wishart fluctuation and low-regularity LUE results; these foundations must be credited.
>
> A useful consequence is that equal gate operator purity fixes the limiting Rényi-2 memory but does not fix von Neumann or logarithmic-negativity memory. An explicit pair has strictly different same-order covariance at every positive order except two. The low-order quarter-threshold and 8α increment exponent are retained as consequences, with the explicit warning that their leading law also follows from standard smooth Gaussian interpolation.
>
> Preserve the distinction between fixed-time covariance/finite-dimensional Gaussian limits and unproved path-space or shrinking-time limits. Do not claim arbitrary non-diagonal gates, physically prepared-state universality, or a new OTOC identity. The numerical package contains finite-size deviations; do not describe it as precise confirmation of every asymptotic prediction.
>
> The project is independent of Entanglement-Trajectories, which remains frozen, and of Boundary-Entangling-Susceptibility. Do not edit either project or import their claims as premises. The earlier metric-disagreement and weak-link pilots are history, not this project's current agenda.
>
> Continue by asking what physical information the full covariance relation adds beyond known operator entanglement. A small analytical test of a non-diagonal local gate is a possible next discriminator. Before broadening the model, state the question, the decisive outcome, and the stopping rule. More sampling by itself will not settle PRL significance.

The project package includes reproducible source, saved arrays, proof notes, adverse internal reviews, a focused literature ledger, and a concise feasibility draft. The previous checkpoint records are preserved and explicitly identified in IMPORTS.json. No external repository has been created by this handover.
