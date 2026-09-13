# Repository refurnishing review

13 September 2026. Starting commit: `8121d08f81d37776bc065c47a9afcc5a7074c4df` in `GoGoKo699/Entangling-successions`.

The user requested repository refurnishing, with manuscript preparation last. This work reorganizes the explanation and provides maintained calculation entry points. It does not add a theorem, a state-sampling cohort, a physical model, manuscript prose, or journal formatting.

## What changed

- The README now starts with the scientific question and an analytical gate example. A maintained route connects intuition, the worked example, the precise theorem, technical derivation, references, and evidence.
- The technical note consolidates the existing indexed Gaussian/Wick convention, spectator power counting, realignment cycle, Chebyshev coefficients, nonpolynomial transfer, shared normalization, and order-one remainder. It identifies external mathematical inputs and preserves the existing limits.
- The evidence page maps claims to proof/code/results, separates the 192 independent non-diagonal Haar inputs from older cohorts, and retains both earlier sampling discrepancies and all twelve failed Floquet comparisons.
- `gate_covariance/` provides maintained formula evaluations with an explicit series cutoff. `scripts/reproduce.py` combines independent analytical implementation checks, the existing six-program reproduction, and generation of the reader table and figure.
- New outputs use `build/` or an explicit separate destination. The imported evidence and historical validation files remain unchanged. The root validation script now accepts `--output-dir` and rejects preserved research-record directories.
- The handover, phase roadmap, repository map, and GitHub Actions workflow follow this structure. The paper outline remains deferred.

## Checks performed

| Check | Outcome and scope |
|---|---|
| Starting files | All 218 active baseline files matched their remote Git blob hashes before editing |
| Imported evidence | All 193 SHA-256 entries in `provenance/IMPORTS.json` verified; inputs remained unchanged after reproduction |
| Existing deterministic calculations | All six passed in a temporary copy; five JSON outputs matched byte for byte and the sixth passed its recorded floating-point tolerance |
| Maintained covariance code | Agreed with saved independently generated rational witnesses, a mixed-order exact anchor, known gate spectra, the closed order-one coefficients, and the integer-order inverse |
| Reader example | Regenerated JSON, PNG and SVG were byte-identical in the local fresh-output run; the committed JSON is also compared numerically during the default command |
| Numerical series diagnostic | `K=65536` versus `2K=131072` changed the showcased correlations by less than `1e-9`; this is not a certified tail or finite-size error bound |
| Reader and scientific consistency | Separate internal readers checked normalization, examples, theorem/derivation consistency, evidence qualifications, and the actual figure; no remaining blocker identified |
| Navigation | Local path destinations in maintained Markdown checked by `scripts/check_repository.py`; external URLs and historical navigation are outside that script's scope |

The combined reproduction was run from outside the repository, into a fresh output directory, in approximately 20 seconds. The local environment was Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. The README figure was visually inspected. Reproducibility of PNG and SVG bytes is an observed local result, not a requirement across operating systems and font renderers; the scientific table uses the recorded numerical tolerance.

The default GitHub workflow installs the pinned dependencies under Python 3.12 in a fresh hosted checkout, runs navigation and complete focused reproduction, and verifies the legacy tree identity. Its run attached to the refurnishing commit records the hosted outcome; this source report does not predict that outcome before the commit exists.

## Preservation and limits

The complete former repository tree is still `ffb13b5f01c8c8ad18c80b521feefd3383a34e34` under `legacy/subset-development/`. The historical branch remains at original commit `1154a87b699d1a17f9e40aaf16a141db62e96041`. The inherited `evidence/` and `limits/` trees and their original manifests are unchanged. Subset-states and the other research repositories are outside this refurnishing.

This is a bounded internal repository and consistency review. It does not repeat the all-degree scientific audit, certify numerical interval bounds, check every historical command, or establish exhaustive originality. The complete Haar sampling and optional Floquet regeneration were not rerun. Their data, methods and limits remain documented separately.

The standalone repository requirements are met by the maintained reading route and checked reproduction. Manuscript drafting remains the final phase. See [NEXT.md](../NEXT.md) and [HANDOVER.md](../HANDOVER.md).
