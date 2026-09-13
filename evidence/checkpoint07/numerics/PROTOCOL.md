# Checkpoint 05: prospectively specified bounded test

Written 2026-09-12 before generating the data in this directory. This is an internal analysis plan, not an external preregistration. Earlier exploratory directions are preserved separately.

Question: does the exact Schmidt-basis conditional variance of a local Renyi-entropy rate show the predicted quarter-order crossover, and does it have a finite-pulse consequence worth pursuing?

Theory predicts, for balanced dimensions d by d, conditional variance of order d^-2 for alpha>1/4, d^-2 log d at alpha=1/4, and d^(-1-4alpha) for fixed 0<alpha<1/4. For dimensions d/2 by 2d at the same total Hilbert-space dimension, every fixed alpha>0 has the ordinary d^-2 scale. These are asymptotic predictions; five finite sizes cannot establish the exponents.

## Main calculation

- Complex Haar pure states, sampled as independent complex Gaussian entries and normalized.
- d=8,16,32,64,128; 256 independent states at each d. A single global state is evaluated at both cuts, with dimensions (d,d) and (d/2,2d).
- Natural-log Renyi orders: 1/8,1/4,1/2,1,2. No eigenvalue thresholds, clipping, or exclusions. Schmidt probabilities from singular values of the state coefficient matrix.
- Physical probe at each cut: Z on the last qubit of the left half times Z on the first qubit of the right half; operator norm one. This is a different boundary bond for the two cuts.
- Record exact physical derivatives and full conditional covariance predicted by Haar randomization of the two Schmidt bases at fixed spectrum.
- Primary summaries: median and interquartile range over spectra of D times the conditional variance. Low-order means of squared physical rates will not receive ordinary variance-based error bars: their required fourth moments can fail to exist.
- Save complete spectra, derivatives, conditional covariances, per-state seed identifiers, and one actual state per size. Code and deterministic seed construction regenerate every Haar state.

## Independent checks

- Two fixed positive spectra of shapes (8,8) and (4,16). Sample 4000 independent pairs of Haar Schmidt bases for each. Compare empirical second moments of all five rates with the exact covariance, reporting uncertainty conditional on those fixed spectra.
- On one saved state per size and both cuts, use exact pulses exp(-itZZ)=cos(t)I-i sin(t)ZZ. Compare symmetric finite differences at t=1e-4,1e-5,1e-6 to the analytical derivatives. Retain small-tail numerical limitations.

## Finite-pulse diagnostic

Before examining main results, add a finite-duration test on the first 64 states at each size. The exact same physical ZZ probe is used at durations 0.02,0.1,0.1/sqrt(d),0.5/sqrt(d). Record entropy changes for both signs of duration.

Compare change divided by duration to the actual initial derivative, and compare robust quantiles of changes with derivative-based predictions. Any d^-1/2 duration scale is a heuristic to test, not an established law. Finite pulses are exact, but finite-size trends cannot settle an asymptotic dynamic scaling limit. No local-circuit or Hamiltonian ensemble is added in this checkpoint.

## Interpretation and stop rule

The Haar ensemble has no spatial dynamics; a one-qubit cut shift changes the aspect ratio from 1 to 1/4. Do not claim a spatial protection mechanism, macroscopic unstable entanglement, Gaussian rates, or a PRL-ready discovery. The usual entropies alpha=1/2,1,2 all lie above the proposed quarter-order crossover. If the result is only an insertion of known hard-edge random-matrix moments, or instantaneous sensitivity without a resolved physical consequence, preserve the result and downgrade its PRL prospects rather than expanding the numerical campaign.
