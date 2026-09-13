# Repository map

Choose **LEARN** in [Start here](START_HERE.md), **CHECK** in [the theorem](../theory/THEOREM.md) and [proof](../theory/PROOF.md), or **REPRODUCE** in [the reproduction guide](../REPRODUCE.md). This page assigns each maintained document a role. The repository holds one active covariance project; it also preserves the evidence on which that project was built.

## Maintained project

| Material | Canonical location | Purpose |
|---|---|---|
| Physical question and selected reading map | [START_HERE.md](START_HERE.md) | LEARN entry, with the exact Mingo and Speicher passages and a route requiring no checkpoint history |
| Book-to-project bridge | [TUTORIAL_BRIDGE.md](TUTORIAL_BRIDGE.md) | Quantum-to-matrix dictionary, mode conventions, gate contraction, normalization, and interpretation |
| Concrete gate example | [WORKED_EXAMPLE.md](WORKED_EXAMPLE.md) | Connect the formula to identity, ZZ, and active SWAP gates |
| Precise statement | [THEOREM.md](../theory/THEOREM.md) | Definitions, limits, coefficients, and consequences |
| Technical reasoning | [PROOF.md](../theory/PROOF.md) | One derivation route with its mathematical dependencies |
| Claim-to-evidence map | [RESULTS.md](RESULTS.md), [CLAIM_LEDGER.md](../CLAIM_LEDGER.md) | Distinguish theorem, exact calibration, sampled evidence, and exclusions |
| Literature attribution | [REFERENCES.md](REFERENCES.md) | Explain which external results enter the argument |
| Reusable formulas | [gate_covariance/](../gate_covariance/) | Gate realignment and truncated entropy covariance sums |
| Default computation | [scripts/reproduce.py](../scripts/reproduce.py) | Focused checks and the analytical reader figure |
| Reader reference outputs | [figures/](../figures/), [results/](../results/) | Small deterministic outputs with generating commands |
| Reproduction instructions | [REPRODUCE.md](../REPRODUCE.md) | Environment, output locations, and optional longer calculations |
| Reader-route source and implementation checks | [IMPLEMENTATION.md](../reviews/mingo-speicher-reader-route/IMPLEMENTATION.md) | Verified source metadata, editorial changes, checks, and remaining limitations |

New outputs go under the ignored `build/` directory. Maintained code can be revised to correct an identified problem; reference changes must be explained. Reference values are not evidence that a general theorem is true.

Mingo and Speicher is the sole assigned external tutorial. The exact reading assignment belongs in `START_HERE.md`; the local bridge translates it into this problem. The canonical theorem and proof remain in `theory/`, and [References](REFERENCES.md) retains the primary attribution. A proof dependency cited there is not an additional assigned tutorial. No third-party book PDF or page images are distributed here.

## Preserved evidence

| Record | What it contains | How it is used now |
|---|---|---|
| [checkpoint07](../evidence/checkpoint07/) | General-gate derivations, exact finite-purity controls, a 192-state non-diagonal pilot, and earlier inherited studies | Source evidence for the current theorem and illustrations |
| [checkpoint08](../evidence/checkpoint08/) | Foundation notes, exact moment inversion, finite-purity and two-cut checks, and the gate-design example | Six deterministic calculations run by the default reproduction |
| [checkpoint09](../limits/checkpoint09/) | Frozen Floquet protocol, code, summary values, figures, and reviews | Limits on extrapolating the Haar theorem; not part of the default computation |
| [validation](../validation/) | Saved migration and reproduction records | Historical runs, distinct from newly generated validation |
| [reviews](../reviews/) | Internal proof, positioning, scope, and repository reviews | Assessment records, not external referee reports |

The immutable import manifest is [IMPORTS.json](../provenance/IMPORTS.json). It covers 193 actual imported files. Two regenerable Floquet cohort NPZ files are omitted from Git and listed with their original hashes in [OMITTED_GENERATED_FILES.json](../provenance/OMITTED_GENERATED_FILES.json). The [reproduction instructions](../REPRODUCE.md) explain how to regenerate that optional study without modifying its saved records.

Some inherited documents use earlier project names, local scratch paths, or historical next-step instructions. They record the work at that time. Current root instructions and the maintained reading route define today's project. The primary-source ledger records earlier retrievals; downloaded third-party paper texts are not bundled.

The entire former Entangling-successions tree is retained under `legacy/subset-development/` and on branch `legacy/subset-development-2026-09-13`. Its root tree SHA is `ffb13b5f01c8c8ad18c80b521feefd3383a34e34`. These scripts are historical subset-state work. [Subset-states](https://github.com/GoGoKo699/Subset-states) is the home of the upgraded subset-state manuscript.

## Future work

[AGENTS.md](../AGENTS.md) records project instructions, [HANDOVER.md](../HANDOVER.md) gives the starting route for another workspace, and [NEXT.md](../NEXT.md) records the phase order. Completion of the educational route does not automatically start manuscript work. The manuscript outline is future planning material. Any new ensemble extension needs its own stated assumptions and evidence before it can change the current claims.
