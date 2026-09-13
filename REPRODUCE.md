# Reproduce the repository

The default run verifies the imported records, checks maintained formulas against independent analytical references, reruns six existing deterministic calculations, and regenerates the analytical reader figure. It creates no new random-state cohort.

This is the **REPRODUCE** route. For the physical meaning of the outputs, use **LEARN** in [Start here](docs/START_HERE.md), which gives the selected Mingo and Speicher passages and the local reading map. For the mathematical statement and its dependencies, use **CHECK** in [the theorem](theory/THEOREM.md) and [proof](theory/PROOF.md). The reproduction does not require reading the tutorial first.

## One entry point

From the repository root, use Python 3.12 and the pinned dependencies:

```sh
python -m pip install -r requirements.txt
python scripts/reproduce.py
python scripts/check_repository.py
```

The root requirements pin NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. No GPU is needed. The scripts set one numerical-library thread for the focused run.

| Generated output under `build/reproduction/` | Meaning |
|---|---|
| `validation/PROJECT_VERIFICATION.json` | Integrity of all 193 imported files and status of the six inherited deterministic programs |
| `validation/CHECKPOINT08_REPRODUCTION.json` | Per-program reference comparisons and their tolerances |
| `validation/deterministic_reproduction.log` | Complete output of those programs |
| `validation/maintained_calculations.json` | Maintained-code comparison with exact rational witnesses, known gate spectra, and the saved reader table |
| `results/reader_examples.json` | Operator probabilities, covariance matrices, correlations, and increments for identity, ZZ, and active SWAP |
| `figures/entropy_memory.png`, `figures/entropy_memory.svg` | Analytical correlation curves shown on the README |

New outputs are kept outside the preserved records. The inherited calculations run in a temporary copy; their saved inputs and results are checked again afterwards. The committed reader references are [results/reader_examples.json](results/reader_examples.json) and [figures/entropy_memory.png](figures/entropy_memory.png). A numerical tolerance comparison checks the table; image pixels are not a cross-platform scientific equality test.

The uninterrupted identity, ZZ, and active-SWAP calculation in [the worked example](docs/WORKED_EXAMPLE.md) uses that same reader table. The [tutorial bridge](docs/TUTORIAL_BRIDGE.md) explains the coefficient-matrix dictionary, common trace normalization, and fluctuation modes used by the calculation. Neither document introduces a new sample cohort or a separate numerical pipeline.

To reproduce into a separate directory, including from another working directory, use an absolute script path:

```sh
python /path/to/Entangling-successions/scripts/reproduce.py --output-dir /tmp/gate-covariance-reproduction
```

Replace `/path/to/Entangling-successions` with the actual checkout path. Source lookup is relative to the script, not the shell's working directory.

## Numerical approximation and the scientific limit

The maintained formulas in [gate_covariance/core.py](gate_covariance/core.py) evaluate the theorem with explicit coefficient cutoff `K`. The reader example uses `K=65536` and records changes on doubling to `131072`. At the showcased orders `1/2`, `1`, `2`, `3`, and `4`, the displayed correlations change by less than `1e-9` in that diagnostic. Integer orders 2, 3, and 4 terminate exactly at modes 2, 3, and 4. A different order can converge more slowly and needs its own justified cutoff.

The cutoff comparison is a numerical diagnostic, not a certified bound on omitted terms. It also says nothing about finite-dimensional bias. These are calculations of the balanced-Haar, fixed-active-support limit; they are not finite-state simulations or fitted estimates. [The worked example](docs/WORKED_EXAMPLE.md) explains the quantities and units.

For example, from the repository root:

```python
import numpy as np
from gate_covariance import operator_schmidt_probabilities, correlation

u = np.diag(np.exp(-1j * np.pi / 4 * np.array([1, -1, -1, 1])))
eta = operator_schmidt_probabilities(u, r=2, s=2)
print(eta)  # two nonzero probabilities, both 1/2, up to SVD roundoff
print(correlation(2, 2, eta, cutoff=4))  # 1/2
```

For two observations at gates `U_l` and `U_m`, pass the operator probabilities of `U_l @ U_m.conj().T`. The core also accepts abstract normalized probability vectors for algebraic calculations; this does not establish that every vector is realized by a gate at specified dimensions.

### Check the equal-purity comparison

The [worked example's two-pair gate witness](docs/WORKED_EXAMPLE.md#same-operator-purity-different-higher-order-covariance) has an exact order-three covariance difference. To check it separately from the default three-gate table, run this from the repository root:

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

The output is `Rescaled covariance difference: 0.001930194847`. The independently derived radical follows from the exact $F_3$ difference in the worked example. Order three terminates at $k=3$, so this calculation has floating-point roundoff but no omitted series terms. It evaluates a large-$d$ coefficient, not a finite-dimensional sample.

## What the default checks establish

The six inherited checks cover exact moment inversion, finite-dimensional purity identities, two subsystem assignments, and a gate-design example. [Results and evidence](docs/RESULTS.md) maps each program to its saved output and qualification. Five historical JSON outputs match byte for byte; the sixth uses its documented floating-point tolerance.

The maintained calculations are checked against those independently generated rational witnesses, exact spectra of specific gates, a closed order-one coefficient expression, and the integer-order moment inverse. They also compare the regenerated reader table with its committed reference. Neither the reference agreement nor the inherited finite-degree checks replace the all-degree entropy derivation.

For a narrower run:

```sh
python scripts/check_calculations.py
python verify_project.py --output-dir build/validation
python scripts/check_repository.py
```

The last command checks local paths, image destinations, and Markdown section anchors linked from the maintained reading route, including same-page anchors. It does not fetch external references or crawl historical navigation. GitHub Actions runs the navigation check and complete default reproduction, then verifies the legacy tree identity. Source verification and the documentation walkthrough are recorded separately in [the reader-route implementation record](reviews/mingo-speicher-reader-route/IMPLEMENTATION.md); they are not independent scientific replication or external peer review.

## Existing Haar samples

The saved [non-diagonal pilot summary](evidence/checkpoint07/checkpoints/07/results/pilot_summary.json) and its NPZ arrays support the finite-size table in [Results](docs/RESULTS.md). Earlier cohorts remain separate. No cohort is regenerated by the default command.

[The inherited reproduction guide](evidence/checkpoint07/REPRODUCE.md) gives the original commands for finite-purity, contraction, and sampling studies. Run them in a writable copy of that checkpoint to retain its reference arrays. Some commands are longer calculations and are not needed to reproduce the new analytical figure. Compare NPZ array values rather than compressed archive bytes; retain each original protocol and tolerance.

## Optional failed Floquet extension

[limits/checkpoint09/](limits/checkpoint09/) contains the frozen protocol, code, predictions, summaries, figures, and validation records. Two large regenerable files are omitted from Git: `results/cohort_N8.npz` and `results/cohort_N10.npz`. Their original hashes and sizes are listed in [OMITTED_GENERATED_FILES.json](provenance/OMITTED_GENERATED_FILES.json). The complete original checkpoint archive was retained before the repository migration.

The original `reproduce.py` there expects the omitted reference files. To regenerate without that archive, copy `limits/checkpoint09/` to a separate writable directory and preserve another copy of its summary JSON files. In the writable copy run:

```sh
python -m pip install -r requirements-reproduction.txt
python theory/haar_predictions.py
python floquet_test.py
python reviews/independent_audit.py
python plot_results.py
```

These commands regenerate the two frozen-size cohorts, audit them, and redraw their figure. Compare summary values with the preserved summaries, excluding wall time; the original comparison uses relative tolerance `1e-9` and absolute tolerance `1e-11`. This optional calculation was not rerun during refurnishing. Its original manifest lists the two omitted archives; the current import manifest describes the actual Git files.

## Preserved repository history

In a normal Git clone, the following commands should both return `ffb13b5f01c8c8ad18c80b521feefd3383a34e34`:

```sh
git rev-parse HEAD:legacy/subset-development
git rev-parse origin/legacy/subset-development-2026-09-13^{tree}
```

The second command requires the historical remote branch to have been fetched, as in a normal full clone. These checks establish exact preservation of the former tree. The active validation does not execute historical subset-state scripts. The [repository map](docs/REPOSITORY_MAP.md) distinguishes maintained content from those records.
