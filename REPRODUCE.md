# Reproduction

The current repository is a migration of already checked research. The default gate verifies relocation and existing deterministic consequences. It does not rerun every previous experiment.

## Default check

Use Python 3.12 with the pinned NumPy and SciPy versions:

```sh
python -m pip install -r requirements.txt
python verify_project.py
```

The script checks the hashes in `provenance/IMPORTS.json`, copies checkpoint 08 to a temporary directory, runs its six deterministic calculations, compares saved JSON references, and confirms that the imported files stayed unchanged. Reports are written to `validation/`. The files under `evidence/` are never edited by this command.

The checks cover integer-order inversion, exact finite-purity identities, two-cut identities, and the exact-design example. This is a reproduction gate, not a replacement for the all-degree nonpolynomial proof.

## Earlier Haar evidence

`evidence/checkpoint07/REPRODUCE.md` documents the exact finite-purity and contraction checks and the 192-state non-diagonal pilot. Run those commands in a copy of that directory to preserve the saved reference arrays. Its inherited 05–06 code and numerical records are also included. No previous random cohort was regenerated for this repository migration.

Compare NPZ arrays rather than compressed bytes. The original tolerances and limitations remain with each study. Floating-point sampling error bars do not bound finite-size asymptotic bias.

## Failed Floquet extension

`limits/checkpoint09/` preserves its code, frozen protocol and predictions, summary JSON, figures, and original validation records. Two large regenerable files are omitted from Git: `results/cohort_N8.npz` and `results/cohort_N10.npz`. Their original hashes and sizes are recorded in `provenance/OMITTED_GENERATED_FILES.json`; the complete original checkpoint archive was retained before this migration.

Before the optional Floquet commands, install its plotting dependency with `python -m pip install -r limits/checkpoint09/requirements-reproduction.txt`. The default deterministic gate needs only the root requirements.

The original `limits/checkpoint09/reproduce.py` is preserved unchanged and expects those two original reference files. For a fresh regeneration without that archive, first copy `limits/checkpoint09/` to a writable directory. Keep a separate copy of its saved summaries, then run there:

```sh
python theory/haar_predictions.py
python floquet_test.py
python reviews/independent_audit.py
python plot_results.py
```

The first two commands regenerate the prescribed predictions and cohorts. The following commands audit the generated cohort and redraw the figure. Compare summary values with the saved references, excluding wall time; the original JSON comparison tolerance is relative 1e-9 and absolute 1e-11. The generation uses only the two frozen sizes and gates. This longer optional computation was not rerun during migration.

The shipped checkpoint-09 MANIFEST describes its original complete package and therefore also lists the two omitted files. The current `provenance/IMPORTS.json` describes the actual imported Git files. Neither original protocol nor original manifest was silently rewritten.

## Legacy tree

The former repository tree is retained by exact Git tree identity, not by regeneration. Its original root tree is `ffb13b5f01c8c8ad18c80b521feefd3383a34e34`. In a Git checkout, verify preservation with:

```sh
git rev-parse HEAD:legacy/subset-development
git rev-parse origin/legacy/subset-development-2026-09-13^{tree}
```

Both should return that tree SHA. The current active validation does not execute historical subset-state scripts.
