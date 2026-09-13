# Independent scientific interpretation

Checkpoint 09, 12 September 2026. This review reads the frozen protocol and
the saved N=8 and N=10 summary JSON files. It generates no new states, changes
no thresholds, and performs no rescue search. Numerical implementation auditing
is a separate task.

## Decision under the frozen rule

All 12 nontrivial gate/order/size comparisons fail the declared combined Haar
band. Input variance, output variance, and correlation fail in every case.
Eleven of 12 squared-increment comparisons fail; the half-order phaseSWAP
comparison at N=8 is just within the prescribed increment ratio band. All
mean-shift criteria pass at N=8 and fail at N=10. Identity remains an exact
zero-change implementation control.

The most secure discrepancy is the absolute input fluctuation scale. The
von Neumann variance is 8.17085 times its **exact finite-d Haar value** at
N=8 and 5.68612 times at N=10. Purity variance is 15.92769 and 8.52638 times its
exact Haar value. These are not ambiguities in the asymptotic entropy
coefficient or unresolved small Schmidt tails. The reported minimum Schmidt
probabilities are positive and no observations were excluded.

The bounded physical-reach test therefore fails its declared criterion.
The protocol calls for stopping here, retaining the discrepancy, and leaving
the scientific scope open. It supplies no authority to improve agreement by
changing gates, adding circuit seeds, extending size, or removing states.

## What the data explain, and what they do not

A useful distinction is visible without a fitted model: **large normalized
memory does not mean a small absolute entropy response**. Correlations range
from about 0.661 to 0.851, much larger than the Haar limits of 0.172 to 0.25.
Nevertheless every recorded squared increment is larger than the Haar
prediction, by factors about 1.25 to 2.47. The cohort starts with much broader
entropy variation than Haar, and substantial variation survives either probe.

Both probes reduce the entropy variance while increasing the mean entropy.
For von Neumann entropy at N=10, the output variance is still approximately
3.1 to 3.4 times the asymptotic Haar variance; the input ratio is about 5.7.
The large correlation is therefore a statement about the retained variation
between eigenstates. It cannot be interpreted as protection against a gate
or as a smaller absolute perturbation.

This is a descriptive explanation of the covariance pattern, not a derived
microscopic mechanism for the excess variance. The data do not identify a
slow mode, transport bottleneck, weak-link hierarchy, conserved quantity,
scar population, or universal spectral component responsible for it. The
recorded level and participation diagnostics do not establish the high-order
joint eigenstate statistics required by the entropy covariance formula.

The mean von Neumann entropy approaches the exact Haar mean between the two
sizes: its deficit changes from about 0.084 to 0.038 natural-log units.
Meanwhile the fluctuation variance remains several times larger than Haar.
Thus agreement in a mean entropy, even if judged numerically close, would
not by itself validate a fluctuation law. This general distinction is
established in the eigenstate-statistics literature and is not a new PRL
mechanism demonstrated by this checkpoint.

## The equal-spectrum probe comparison is unresolved

The two independent probes have identical normalized operator Schmidt
spectra. Their correlation differences have magnitude at most 0.0621 across
the recorded orders and sizes, within the frozen descriptive equality band
of 0.10. Accordingly this test does **not** resolve a violation of
operator-Schmidt-spectrum sufficiency for independent probes. It also does
not confirm sufficiency: two close but inaccurate predictions cannot test
the entire functional dependence, and the cohort has no independent-circuit
sampling intervals.

The legitimate distinction is:

- The quantitative Haar prediction fails in this finite eigenstate cohort.
- Equality between the chosen equal-spectrum probes is not resolved as
  failing at the declared tolerance.

Do not collapse these into a claim that the equal-spectrum principle itself
has been disproved for independent probes.

## The exact own-gate constraint has a different logical role

The period was written in the frozen protocol as F=L G_c with L local across
the cut. On every Floquet eigenstate, G_c acts as a local unitary up to a
phase. The complete Schmidt spectrum is consequently unchanged. The fixed
anchors agree, with maximum entropy changes of order 10^-15.

That identity gives a rigorous counterexample to a **blanket** Haar-law
extension that allows the probe to be correlated with the circuit defining
the eigenstates. It was known before the numerical results and does not
explain the quantitative values for the two independent probes. In
particular, it does not establish that their correlations must stay above
the Haar values at large system size.

The physically relevant missing information for the own-gate example is the
alignment of the state with its dynamics. The stationarity identity exposes
that information exactly. Turning the independent-probe discrepancies into
a predictive mechanism would require an additional relation; none has been
derived here. The elementary stationarity identity alone should not be
promoted as a new many-body result.

## Limits and research consequence

There are only two nested sizes and one circuit at each size. The ratios and
correlation residuals decrease with size in several comparisons, while
increment ratios do not uniformly do so. No exponent, nonzero limiting
residual, or eventual convergence can be inferred from these two points.
Exact finite-d Haar anchors remove Haar finite-size bias as an explanation
for the present excess, but do not remove finite-size effects of the
**Floquet eigenstate ensemble itself**.

The existing Haar theorem is unaffected. The current numerical evidence
does not support the proposed physical extension, a thermodynamic no-go for
independent probes, or a new theory of static eigenstate fluctuations.
Given the user's preference for a compact physical insight and bounded
calculations, this is a reason to stop this feasibility test rather than
begin a larger convergence campaign. The checkpoint clarifies what remains
missing: a physical principle predicting joint state-probe statistics
beyond Haar, with a consequence not already contained in known eigenstate
correlation theory.
