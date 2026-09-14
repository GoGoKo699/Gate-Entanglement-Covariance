# Checkpoint 09: bounded Floquet eigenstate test

12 September 2026. Fixed before generating the circuit gates, diagonalizing the Floquet operators, or evaluating eigenstate entropies. Prior literature and the exact one-crossing constraint were checked before this freeze. This is a descriptive two-size feasibility test, not a calibrated statistical test or a finite-size extrapolation.

## Fixed scope

One open spin chain with a quenched two-layer brickwork Floquet unitary. Sizes N=8 and N=10. Label sites x=-N/2,...,N/2-1 so the cut always lies between -1 and 0. First apply independent two-qubit gates on bonds with odd left coordinate, then those with even left coordinate. Thus the same central gate is always in the first layer. Each bond gate is drawn once from complex U(4) using phase-corrected complex Gaussian QR and reused every period. Bond x uses NumPy SeedSequence([2026091209,x+100]); nesting preserves every shared gate across the size extension. No gate rejection, weak-link truncation, seed replacement, or selected eigenstate window.

The state cohort is the entire orthonormal Floquet eigenbasis at each size, sorted by eigenphase. It is a census for one operator. Eigenstates and nested sizes are dependent. Do not attach independent-state bootstrap intervals or treat these as independent disorder realizations. No symmetry is imposed. Record degeneracies, commutators with total Z, total Z parity, total X flip and reflection, circular gap ratios, computational-basis participation, and all local gate operator purities. These diagnostics describe the selected operators and do not prove absence of every hidden symmetry or thermodynamic chaos.

## Three independent probes

On the active central qubits, use identity, SWAP, and SWAP exp(-i pi ZZ/4). Their definitions do not depend on the selected circuit gates or eigenstates. The nontrivial pair has the same uniform rank-four operator Schmidt spectrum. The inherited Haar law therefore predicts identical limiting before/after entropy correlations at orders 1/2, 1 and 2. This pair tests both the magnitude and the gate-spectrum sufficiency claim. The identity is a zero-change control, not a separate prediction fit.

Record input/output mean, population variance (divide by the cohort count), centered covariance, Pearson correlation, uncentered mean squared increment, minimum Schmidt probability, and every per-state entropy/purity. Natural logarithms. No spectral-tail exclusion or coefficient fitting. Finite values are computed from singular values; zeros contribute zero to p log p.

Use the exact finite-d Haar purity mean/variance/correlation and exact von Neumann mean/variance as independent finite-size anchors. Use the existing fixed-positive-order covariance series for limiting entropy covariance and increments. Prediction constants and exact finite-size anchors are stored before eigenstate responses. For order 1/2 and order 2 entropy variances, the limiting values are benchmarks rather than exact finite-d predictions.

## Descriptive comparison criteria

At each size, report all gates/orders. Call a nontrivial entropy comparison within the declared Haar band only if: input and output variances divided by their limiting Haar variances are both in [0.75,1.25]; the absolute Pearson-correlation residual is at most 0.10; the mean squared increment divided by its limiting Haar prediction is in [0.75,1.25]; and the absolute mean shift is at most 0.25 input standard deviations. Report each component separately. Also report the two nontrivial gates' correlation difference, with 0.10 as a descriptive equality band. These tolerances are practical feasibility criteria, not confidence levels. They do not bound unknown finite-size entropy bias.

For exact purity and exact von Neumann marginal anchors, report ratios/residuals without pretending finite entropy-covariance errors are known. Agreement of the mean entropy or level statistic alone does not validate a covariance law. A finite-cohort discrepancy does not disprove the existing Haar theorem or establish asymptotic Floquet behavior.

## Exact structural anchor and validation

With this centered layer convention the period factorizes F=L Gc, where L is local across the cut and Gc is the circuit's own crossing gate. Every eigenstate therefore obeys Gc psi=exp(i theta)L†psi: its entire Schmidt spectrum is preserved. This already rules out an unconditional Haar gate-memory extension to probes correlated with the state-generating circuit. The three primary probes remain fixed independently. Check this analytical identity on 16 equally spaced eigenphase indices per size only as a numerical anchor, separately labeled from the three independent probes.

Use a complex Schur decomposition for orthonormal eigenvectors and retain residuals. Independently rebuild the Floquet matrix and probe action; compare reduced-density-matrix eigenvalue entropies against the SVD implementation on fixed representative indices. Independently recompute all saved scalar summary statistics and the finite-size Haar anchors. A fresh-directory reproduction reruns only this bounded checkpoint.

## Stop rule

No additional sizes, circuit seeds, gate optimization, or preparation-depth survey in this checkpoint. Retain failures. If the independent-probe law fails the descriptive bands, report its observed failure and whether a compact explanation exists; do not rescue it by adjusting gates or excluding states. Generic non-Haar eigenstate entropy fluctuations are already prior work, so that observation alone does not justify PRL. Keep project scope open and do not create an external repository.
