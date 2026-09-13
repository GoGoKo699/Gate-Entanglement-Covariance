# Fresh-state test of the finite-time series

Written after inspecting the original checkpoint data and deriving the polynomial kernel, but before sampling this new cohort. Date 2026-09-12. This is an internal frozen prediction, not external preregistration.

The original data motivated the temporal question; they are not held-out confirmation of it. The following test uses independent seeds and separately saved results.

- Balanced cuts only, d=128 and 256, with 128 new complex Haar states at each size.
- SeedSequence [90512506,d,sample], distinct from all original seeds.
- Same physical boundary ZZ, operator norm one. Exact pulses at tau=0.1,0.2,0.4 and their negatives.
- Orders 1/8,1/4,1/2,1,2; no exclusions or thresholds.
- Primary estimate for each order and duration: mean of Y=D[(S(tau)-S(0))^2+(S(-tau)-S(0))^2]/2 over independent global states. Error scale is sample standard deviation of Y divided by sqrt(128). The two pulse signs are not independent observations.
- Compare to the parameter-free limiting series in FOLLOWUP_HYPOTHESIS.md. This series has a fixed-polynomial derivation. Its extension to low-order entropy functions is not yet proved. The series is a large-d limit, so finite-size deviations must not be labeled formula failures without controlling the limit.
- Save predicted values and source hash before state generation. No coefficient fits, optimized pulse choices, supplementary sizes, or spectral tail exclusions after viewing this cohort.

This bounded check can support or challenge a finite-time mechanism. Three fixed pulse durations and two sizes cannot establish a fractional temporal exponent, Gaussian process, or thermodynamic theorem. The raw cohort will remain even if it does not support the proposed series.
