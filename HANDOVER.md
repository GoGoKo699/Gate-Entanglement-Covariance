# Start work here

This repository has one active research project: **Gate Entanglement Covariance**, with Quantum as the current publication target. Its GitHub name remains `GoGoKo699/Entangling-successions`. The user set the phase order explicitly: refurnish the repository first, prepare a manuscript last.

## Scientific starting point

Read [the README](README.md), [the scientific guide](docs/START_HERE.md), [the worked example](docs/WORKED_EXAMPLE.md), and [the theorem](theory/THEOREM.md). The result applies to complex-Haar states on balanced growing halves, deterministic gates on fixed boundary factors, a fixed finite gate family, and fixed positive entropy orders. The relative gate's operator Schmidt spectrum determines the rescaled entropy covariance. Absolute fluctuations vanish as the dimension grows.

[The derivation](theory/PROOF.md) assembles the current conventions and proof dependencies. [References](docs/REFERENCES.md) identifies the established random-matrix and quantum-information inputs. The underlying theorem received internal review before this refurnishing; the new documentation is not a new external peer review or an acceptance guarantee.

[Results and evidence](docs/RESULTS.md) and [the claim ledger](CLAIM_LEDGER.md) distinguish analytical results, exact calibrations, sampled illustrations, adverse deviations, and unproved extensions. The failed Floquet study remains a limit on prepared-state extrapolation. A subset-state extension is unproved and is not a prerequisite for the current paper.

## Repository starting point

The refurnishing provides a maintained reading route, reusable formulas in `gate_covariance/`, one focused entry point in `scripts/reproduce.py`, and small reference figure and table files. [The repository map](docs/REPOSITORY_MAP.md) distinguishes maintained files from preserved research records. [The reproduction guide](REPRODUCE.md) states exact commands, dependencies, outputs, and approximation limits.

```sh
python -m pip install -r requirements.txt
python scripts/check_repository.py
python scripts/reproduce.py
```

Run from the repository root. New outputs go under `build/reproduction/`; the default creates no random-state cohort. It checks 193 immutable imported files, the six inherited deterministic programs, and the maintained calculation against independent analytical references. It regenerates the reader example and figure. See [the refurnishing review](reviews/REFURNISHING_REVIEW.md) for what was actually checked.

The user prefers a clear physical insight, compact supporting theory, modest decisive numerics, simple prose, and no em dashes. Preserve scientific precision over presentation. Add calculations only for a concrete gap; no new survey is required by the current project.

## Boundaries and the final phase

[NEXT.md](NEXT.md) records the completed repository work and the deferred manuscript phase. `PAPER_OUTLINE.md` remains a future planning reference. This repository refurnishing does not include manuscript prose, journal formatting, or submission.

The user confirmed that the old Entangling-successions subset-state work was upgraded into [Subset-states](https://github.com/GoGoKo699/Subset-states) and authorized reuse of this repository. The complete old tree and original commit are preserved. That history is not a second active paper here. [The transition record](provenance/REPOSITORY_TRANSITION.md) gives the exact references.

Treat `evidence/`, `limits/checkpoint09/`, and `legacy/subset-development/` as immutable. Their historical names, local paths, and next-step notes are records of previous work. Root instructions define the current phase. Do not alter Subset-states, Entanglement Trajectories, or Boundary-Entangling-Susceptibility as part of this project. External submission and person-directed correspondence need authorization for those actions.
