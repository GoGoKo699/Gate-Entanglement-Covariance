# Numerical studies

Each study has a defined input ensemble and a separate sample cohort. Their data are not pooled.

| Study | Purpose and result | Contents |
|---|---|---|
| [Non-diagonal gates](non_diagonal/README.md) | Small Haar illustration of SWAP and Cartan gates, with exact-purity and Wick-contraction controls | 192 Haar inputs, fixed predictions, sample arrays, summaries and implementation |
| [Haar response and diagonal gates](haar/README.md) | Response diagnostics, finite-time samples and a matched diagonal-gate comparison | Separate protocols and cohorts, including adverse finite-size deviations |
| [Floquet eigenstates](floquet/README.md) | Test whether the same Haar prediction describes a prepared eigenstate ensemble | All twelve nontrivial comparisons fail the declared bands; code, criteria, summaries and figure are retained |

The [results page](../docs/RESULTS.md) compares the evidence, and the [reproduction guide](../REPRODUCE.md) gives commands for sample regeneration. Protocols and numerical reference files are covered by the [integrity manifest](../reference_integrity.json).
