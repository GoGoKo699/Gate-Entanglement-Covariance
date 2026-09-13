# Reproduction

Use Python 3.11 or newer with the package versions recorded in requirements.txt. The production environment and exact installed versions are recorded in VALIDATION.json. These instructions use relative paths and do not require either earlier GitHub project.

Create a separate working copy if you want to preserve the distributed numerical records unchanged. Production scripts write their own result files.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python numerics/audit05.py
python numerics/annular_polynomial_audit05.py
python numerics/diagonal_gate_handcheck.py
python numerics/generalized_wick_check.py
python numerics/plot_operator_memory.py
```

The first two commands independently recheck the inherited numerical implementation and the original ZZ Wick algebra. The next two check the new operator spectra and the generalized phase kernel. The plotting command uses saved records and evaluates explicit analytic expressions.

To reproduce the new physical cohort, run:

```bash
python numerics/operator_memory.py
python numerics/plot_operator_memory.py
```

This uses exactly 64 independent Haar states at each of d=64 and d=128, two declared diagonal interactions, and two pulse times. The same state is reused across the four pulses. The seed recipe, observables, interactions, and pre-computation prediction are in numerics/OPERATOR_PLAN.md and numerics/operator_results/frozen_prediction.json. There are 128 independent states and 512 entropy-pulse evaluations. Reusing observations across gates and times does not create additional independent samples.

To regenerate the inherited checkpoint-05 campaigns and figures:

```bash
python numerics/run_experiment.py
python numerics/finite_time_followup.py
python numerics/analyze.py
python numerics/plot_followup.py
```

These are the original scripts, retained byte for byte. They produce 1,536 independent global Haar states in total across their two disjoint seed cohorts, and 6,656 finite-pulse entropy evaluations in addition to their derivative and orientation checks. Original analysis figures are generated under numerics/figures; the distributed copies are under figures. They are supporting evidence for the original ZZ result and its limitations, rather than new production for checkpoint 06.

Historical frozen prediction metadata in numerics/followup_results says that the nonanalytic extension was unresolved. That records the state of knowledge when those predictions were made. Later proof notes resolve the stated fixed-time extension; the frozen metadata has deliberately not been rewritten.

The series evaluator in finite_time_followup.py is a research helper for its declared finite pulses, not a general endpoint-safe numerical API. Its asymptotic tail treatment should not be used at zero, at exact recurrences, or at arbitrarily small lags with an unchanged cutoff. The new operator_memory.py helper handles the exact identity explicitly and rejects spectra too close to it for the selected cutoff. These numerical helper domains do not restrict the analytical series.

No tolerance was widened to obtain the distributed validation. The numerical summaries report sample standard errors as descriptive errors of sample means; repeated orders, times, and paired gates are correlated. They are not uniformly calibrated significance tests against an asymptotic model at finite d.
