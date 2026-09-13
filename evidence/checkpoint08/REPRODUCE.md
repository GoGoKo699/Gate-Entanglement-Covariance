# Reproduction

Unzip the archive in a new directory, then run from its `Entanglement-Temporal-Fluctuations-Checkpoint-08` folder:

```bash
python reproduce.py
```

The six declared checks run sequentially with one BLAS thread each. They require Python, NumPy, and SciPy. The development environment is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; `VALIDATION.json` records the fresh-run versions. If packages are missing, install NumPy and SciPy using your normal Python environment manager. No network access is used by the checks.

The programs overwrite their own generated result JSON files. `reproduce.py` first reads each reference and then compares the regenerated values. It records exact byte identity separately from a small tolerance for cross-platform floating-point differences. Exact rational expressions and textual metadata must match exactly. The individual scripts also assert their own mathematical identities and tolerances.

Outputs are `REPRODUCTION.json`, the regenerated calculation results, and `reproduction_logs/`. The packaged `VALIDATION.json` is the author's fresh-directory record and is not overwritten. The manifest hashes describe the originally packaged files; rerunning computations on another platform can legitimately change floating-point bytes and logs. They should not change the theoretical conclusions.

Only new checkpoint-08 work is rerun. The `foundation/` folder contains unchanged prior derivations and their audits, with file-level provenance, rather than an unnecessary repeat of the earlier Haar sampling studies. This checkpoint is sufficient to reproduce its new identities, examples, and inverse calculations; the historical checkpoint-07 package retains the older production datasets.
