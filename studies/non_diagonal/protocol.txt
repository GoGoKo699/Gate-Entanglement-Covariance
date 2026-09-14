# Checkpoint 07: arbitrary fixed boundary gates

12 September 2026. Written before the new calculations.

Question: does the checkpoint-06 covariance law depend only on the normalized
operator Schmidt spectrum for a general, non-diagonal unitary on fixed boundary
factors? The initial state remains complex Haar on a balanced d by d cut. The
boundary dimensions are fixed while both spectator dimensions grow.

Decisive analytical check: enumerate leading connected Wick contractions for
Chebyshev degrees 1 through 3, including mixed degrees, for identity, diagonal,
controlled, exchange, Cartan, and generic gates, including unequal boundary
dimensions. Any resolved discrepancy stops promotion of the general law until
explained. Independently review the all-degree contraction argument.

Independent finite-size check: evaluate the exact four-copy Haar purity
covariance by summing all 24 permutations. Include both a boundary SWAP with
growing spectators and a whole-half SWAP with no spectators. These limits must
not be confused. This is an exact moment calculation, not sampling.

Bounded entropy illustration, if the analytical tests pass: 96 independent Haar
states at each of d=32 and d=64, applying a boundary SWAP and one fixed Cartan
gate exp[-i(0.37 XX+0.23 YY+0.11 ZZ)]. Use orders 1/2, 1, 2. Report all paired
increments and predictions; do not extend sample size in response to agreement
or disagreement. Independent sample standard errors describe sampling only.
At one state per size verify gate application against a dense full unitary.

The new theoretical target is a finite-access memory bound and its saturation
by a boundary SWAP. Do not infer efficient measurement, generic prepared-state
universality, path-space convergence, or PRL-level originality from this test.
Stop at a reviewed and reproducible checkpoint. Do not extend the older
trajectory, weak-link, or control-obstruction searches.
