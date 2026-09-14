# Deterministic checks

Run these calculations through `python scripts/reproduce.py` from the repository root. The wrapper checks reference hashes and works in a temporary copy, so saved results remain intact.

| Calculation | Implementation | Derivation |
|---|---|---|
| Exact moment inversion and conditioning | [inverse/inverse_moments.py](inverse/inverse_moments.py) | [Moment inversion](../theory/MOMENT_INVERSION.md) |
| Four-copy Haar purity identity | [finite_purity/check_exact_global_purity.py](finite_purity/check_exact_global_purity.py) | [Finite purity](../theory/FINITE_PURITY.md) |
| Two subsystem assignments, full-system contraction | [finite_purity/check_two_cut_modes.py](finite_purity/check_two_cut_modes.py) | [Two-cut modes](../theory/TWO_CUTS.md) |
| Two-assignment symbolic identities | [symbolic/two_cut_symbolic_audit.py](symbolic/two_cut_symbolic_audit.py) | [Two-cut modes](../theory/TWO_CUTS.md) |
| Independent purity-sum and product-input contractions | [numerics/two_cut_check.py](numerics/two_cut_check.py) | [Two-cut modes](../theory/TWO_CUTS.md) |
| Exact gate-design pair | [numerics/design_pair.py](numerics/design_pair.py) | [Gate designs](../theory/GATE_DESIGNS.md) |

The scientific implementations, reference JSON files and [original protocol text](protocol.txt) retain their exact bytes. These are finite deterministic checks. They neither generate a Haar-state cohort nor replace the proof of the all-order entropy theorem. The [reproduction guide](../REPRODUCE.md) documents comparison tolerances and generated reports.
