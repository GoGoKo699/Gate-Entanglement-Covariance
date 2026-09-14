# Reproduce the calculations

The default run checks scientific reference hashes, verifies the formula implementation against analytical anchors, runs six deterministic calculations, and regenerates the reader figure and table. It creates no random-state cohort.

## One entry point

From the repository root, use Python 3.12 and the pinned dependencies:

```sh
python -m pip install -r requirements.txt
python scripts/check_repository.py
python scripts/check_markdown_math.py --self-test
python scripts/reproduce.py
```

The requirements pin NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. No GPU is needed. The small deterministic calculations use one numerical-library thread.

| Output below `build/reproduction/` | Meaning |
|---|---|
| `validation/PROJECT_VERIFICATION.json` | Reference-file integrity and status of the six deterministic calculations |
| `validation/DETERMINISTIC_REPRODUCTION.json` | Per-program comparisons, byte identity and numerical tolerances |
| `validation/deterministic_reproduction.log` | Output of the deterministic runner |
| `validation/maintained_calculations.json` | Analytical gates, rational witnesses, coefficient and inversion checks |
| `results/reader_examples.json` | Operator probabilities, covariance matrices, correlations and increments |
| `figures/entropy_memory.png`, `figures/entropy_memory.svg` | Analytical reader figure |

The [integrity manifest](reference_integrity.json) covers 95 reference files: study implementations, protocol text, recorded arrays and results, deterministic inputs, and analytical reference outputs. Hashes are checked before and after the six programs run in a temporary copy. The reference files are not rewritten. The working copy restores original protocol filenames where a numerical program records their hashes.

The command also works from another directory when given an absolute script path:

```sh
python /path/to/Entangling-successions/scripts/reproduce.py --output-dir /tmp/gate-covariance-reproduction
```

Replace `/path/to/Entangling-successions` with the actual clone path. Within the repository, generated outputs must be under `build/`; external output directories are also accepted. The wrapper rejects output paths that would overwrite scientific reference directories.

## What the default checks establish

The [six deterministic programs](checks/README.md) check moment inversion, the four-copy Haar purity identity, two subsystem assignments, exact symbolic identities, independent purity/product-input contractions and an exact gate-design pair. Each has internal assertions. The runner requires matching JSON structure and labels, with relative tolerance `1e-10` and absolute tolerance `5e-11` for numerical comparison. Byte identity is reported separately. These computations check finite identities; the all-degree entropy law rests on [the proof](theory/PROOF.md).

The [formula checks](scripts/check_calculations.py) use independent exact-rational witnesses, known gate spectra, the closed order-one coefficient formula and the integer-order inverse. The generated reader table is compared with [its committed reference](results/reader_examples.json). Image pixels are not used as a cross-platform scientific equality test.

For a narrower run:

```sh
python scripts/check_calculations.py
python verify_project.py --output-dir build/validation
```

The navigation checker covers local links, images and heading anchors throughout reader Markdown. The math checker requires protected inline math: `$` followed by a backtick, the formula, a backtick and `$`; alternatively use a fenced `math` block. It flags formulas attached to prose, unsupported project commands, missing delimiters and raw formula fragments. The conventions follow [GitHub's math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions). These are source checks; compiling the extracted TeX alone does not test GitHub's Markdown parsing. Plain-text protocol records retain their original bytes for their recorded hashes.

## Numerical approximation and the scientific limit

The library evaluates the theorem using an explicit coefficient cutoff `K`. The reader example uses `65536` and records the change on doubling to `131072`. At the showcased orders $`1/2`$, $`1`$, $`2`$, $`3`$ and $`4`$, the tabulated correlations change by less than $`10^{-9}`$. Integer orders $`2`$, $`3`$ and $`4`$ terminate at modes $`2`$, $`3`$ and $`4`$.

Cutoff doubling is a numerical diagnostic, not a certified remainder bound. It does not bound finite-dimensional bias. These are evaluations of the balanced-Haar limit at fixed support and fixed order. A different order can converge more slowly and requires its own cutoff assessment.

For example:

```python
import numpy as np
from gate_covariance import operator_schmidt_probabilities, correlation

u = np.diag(np.exp(-1j * np.pi / 4 * np.array([1, -1, -1, 1])))
eta = operator_schmidt_probabilities(u, r=2, s=2)
print(eta)  # two nonzero probabilities, both 1/2, up to SVD roundoff
print(correlation(2, 2, eta, cutoff=4))  # 1/2
```

For two observations at gates `U_l` and `U_m`, pass the probabilities of `U_l @ U_m.conj().T`. Abstract probability vectors are accepted for algebraic calculations; this does not show that every vector is realized by a gate of specified dimensions.

### Check the equal-purity comparison

The [worked example](docs/WORKED_EXAMPLE.md#same-operator-purity-different-higher-order-covariance) has an exact order-three covariance difference:

```sh
python - <<'PY'
from math import sqrt
from gate_covariance import covariance

p = (1 + sqrt(sqrt(2) - 1)) / 2
q = 1 - p
eta_a, eta_c = [0.5, 0.5], [p*p, p*q, p*q, q*q]
assert abs(sum(x*x for x in eta_c) - 0.5) < 1e-14
actual = covariance(3, 3, eta_c, cutoff=3) - covariance(3, 3, eta_a, cutoff=3)
exact = 9 * (3 - 2*sqrt(2)) / 800
assert abs(actual - exact) < 1e-14
print(f"Rescaled covariance difference: {actual:.12f}")
PY
```

The output is `Rescaled covariance difference: 0.001930194847`. Order three terminates, so this evaluation has floating-point roundoff but no omitted series terms.

## Optional sample regeneration

The [study pages](studies/README.md) define every cohort and its interpretation. The following commands reproduce the specified saved studies and can take substantially longer than the default run. Execute each block from the repository root; each creates an independent working copy. The temporary protocol aliases preserve the original recorded hashes. Keep the repository's reference files for comparison.

### Non-diagonal Haar samples

```sh
study_work=$(mktemp -d)
cp -a studies/non_diagonal/. "$study_work/"
cp "$study_work/protocol.txt" "$study_work/PROTOCOL.md"
cd "$study_work"
python numerics/entropy_pilot.py
```

This regenerates the same 96 inputs at each of dimensions $`32`$ and $`64`$. Compare the arrays in `results/pilot_d32.npz` and `results/pilot_d64.npz`, and the numerical values in `results/pilot_summary.json`, with the [saved references](studies/non_diagonal/results/). Compressed NPZ byte identity is not an array-equality criterion. Paired gates and orders share each initial state; standard errors describe sampling variation only.

### Haar response, finite-time and diagonal samples

```sh
study_work=$(mktemp -d)
cp -a studies/haar/. "$study_work/"
cp "$study_work/protocol.txt" "$study_work/numerics/PROTOCOL.md"
cp "$study_work/diagonal_protocol.txt" "$study_work/numerics/OPERATOR_PLAN.md"
cp "$study_work/finite_time_protocol.txt" "$study_work/numerics/FOLLOWUP_PLAN.md"
cd "$study_work/numerics"
python run_experiment.py
python analyze.py
python finite_time_followup.py
python operator_memory.py
python plot_followup.py
python plot_operator_memory.py
```

These are separate cohorts, detailed in [Haar studies](studies/haar/README.md). The diagonal comparison's adverse deviations remain part of the result. Neither rerunning its fixed samples nor the displayed error bars resolves the split between sampling error and finite-size bias. Compare numerical arrays and summaries under `numerics/results/`, `numerics/followup_results/` and `numerics/operator_results/` separately.

### Floquet eigenstate comparison

The two eigenvector arrays are regenerable and omitted from Git. [Their original sizes and hashes](studies/floquet/omitted_arrays.json) identify them. All predictions and scalar summaries are retained. The following sequence regenerates the fixed eight-spin and ten-spin cases, independently checks the outputs and redraws their figure:

```sh
study_work=$(mktemp -d)
cp -a studies/floquet/. "$study_work/"
cp "$study_work/protocol.txt" "$study_work/PROTOCOL.md"
mkdir -p "$study_work/history" "$study_work/reviews"
cp "$study_work/serialization_reference.txt" "$study_work/history/floquet_test_initial.py"
cd "$study_work"
python theory/haar_predictions.py
python floquet_test.py
python verification/independent_audit.py
python plot_results.py
```

The source-serialization record allows the independent verifier to check the recorded NumPy JSON conversion without changing the scientific implementation. Compare the regenerated summaries with [the references](studies/floquet/results/), excluding wall time, at relative tolerance `1e-9` and absolute tolerance `1e-11`. The [Floquet study](studies/floquet/README.md) explains the dependent cohorts, descriptive criteria and exact crossing-gate obstruction. The default reproduction does not regenerate these eigenstates.
