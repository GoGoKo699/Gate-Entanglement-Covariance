# Reproduce the current checkpoint

Python 3.11 or newer; dependencies are in requirements.txt. Work on a copy to keep
saved results unchanged. Commands run from this folder and need no external repository.

```bash
OPENBLAS_NUM_THREADS=1 python checkpoints/07/numerics/general_gate_wick.py
OPENBLAS_NUM_THREADS=1 python checkpoints/07/numerics/exact_purity.py
python checkpoints/07/numerics/exact_swap_audit.py
OPENBLAS_NUM_THREADS=1 python checkpoints/07/numerics/entropy_pilot.py
```

The first command contracts 68,786 deterministic leading Wick networks across ten
gates. Read the JSON status as well as the exit code. The second evaluates 24
Haar permutation terms for five gates at nine dimensions. It computes exact
finite-d purity moments with floating-point active traces; its entropy delta-method
column is asymptotic. The third independently counts SWAP and phaseSWAP terms in exact integer and
rational arithmetic, checking the saved moments and correlations. The fourth
generates exactly 192 independent Haar inputs and
384 gate applications, with seed 90712026 and the declared SeedSequence recipe.
It saves its predictions and source/protocol hashes before sampling.

Compare pilot NPZ arrays, not compressed file bytes, when checking reproducibility.
Floating-point reductions may vary slightly across BLAS/library versions. Wick
runtime fields are timing metadata and are not expected to match. The polynomial
comparison tolerance is absolute 1e-8, reflecting cancellation at degree four;
observed maximum error is 3.79e-10. No simulation error bars are used as a proof gate.

The entropy pilot truncates its ordinary-order series at k=65536. The largest
static-variance truncation error for its three declared orders is below 7e-11;
this is not a low-order or arbitrary near-recurrence evaluation API.

Historical checkpoint-05/06 reproduction commands and limitations are preserved
in docs/history/CHECKPOINT06_REPRODUCE.md. Those campaigns were not rerun for 07.
