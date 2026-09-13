# Bounded matched-interaction check

Written before this cohort is generated, 2026-09-12. Internal frozen protocol, not external preregistration. This follows the novelty review and is a small finite-time control, not a new model survey.

Question: do two boundary Hamiltonians with the same energy spectrum, norm, and leading short-time entangling strength have the distinct entropy-memory curves predicted by their operator Schmidt spectra?

Both diagonal Hamiltonians act on two boundary qubits in each half. In the product basis their diagonal values are the entries of a 4 by 4 real matrix h.

- A: h_A=outer([1,-1,1,-1],[1,1,-1,-1]).
- B: rows [1,1,-1,-1], [1,-1,-1,1], [-1,-1,1,1], [-1,1,1,-1].

Both have eight +1 and eight -1 eigenvalues, norm one, square equal to identity, and zero row/column means. Their mean-square interaction after removing one-side terms is chi=1. Their normalized gate operator-Schmidt probabilities are respectively (cos²t,sin²t) and (cos²t,sin²t/2,sin²t/2).

Use balanced cuts d=64 and 128, 64 independent complex Haar states per size, SeedSequence [90612026,d,sample]. Each same state is used for both Hamiltonians. Exact pulses at t=pi/4 and pi/2. Orders are 1/8,1/4,1/2,1,2, using natural logs. Save every entropy change, initial spectrum, prediction, source hash, and seed rule. No exclusions, fitted coefficients, or extra sizes after inspection.

At t=pi/2, A is a product unitary and every entropy returns exactly in exact arithmetic. B has operator-Schmidt probabilities (1/2,1/2), giving the predicted large-d value D E[(Delta S2)²]=1/2. At t=pi/4 these values are 1/2 for A and 5/8 for B.

The order-two relation is a transparent control of an established operator-entanglement distinction. It is not itself claimed as new. The proposed result is the full mode-resolved relation to entropy covariances. These finite-size checks do not prove that theorem or establish novelty.
