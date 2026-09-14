# Repository maintenance

This repository presents the fixed-support Haar entropy-covariance law and its supporting calculations. Read README.md, docs/SCOPE.md, theory/THEOREM.md and theory/PROOF.md before scientific changes. Use docs/REPOSITORY_MAP.md for file responsibilities and REPRODUCE.md for commands.

- Keep LEARN, CHECK and REPRODUCE as distinct entrances. Mingo and Speicher, Free Probability and Random Matrices, is the sole assigned background tutorial; primary proof inputs retain their attribution.
- Keep the theorem and proof canonical in theory/. Supporting identities belong in their named theory notes. Present a current scientific account, without development-status pages or numbered checkpoint directories.
- Preserve balanced complex-Haar input, fixed active dimensions, fixed positive orders, a fixed finite gate family and the order of limits. Absolute covariance vanishes with dimension.
- Distinguish exact identities, asymptotic theorems, deterministic evaluations, sample uncertainty and unresolved extensions. Preserve adverse diagonal results and the failed Floquet comparisons.
- Reference data, original study implementations and original protocol text are covered by reference_integrity.json. Do not rewrite their bytes or replace hashes merely to make a failing check pass. Explain an intentional correction and its scientific effect separately.
- The default reproduction runs the six deterministic programs in a temporary copy. Write new outputs under build/ or outside the repository. Sample generation is optional and is not part of the default run.
- Use protected inline math (`$` followed by a backtick, TeX, a backtick and `$`) and fenced math. Put formulas below plain-text headings. Write “degree” or “dimension” before an inline formula with a space, and keep prose hyphens outside it. Named operators use `\mathop{\mathrm{NAME}}\nolimits`.
- Use plain prose and no em dashes. Do not confuse repository validation with external peer review or publication acceptance.
- After changes, run python scripts/check_repository.py, python scripts/check_markdown_math.py --self-test, and python scripts/reproduce.py using the pinned requirements. Run broader calculations only for a concrete need.
- Keep the default branch focused on scientific content and reproducibility. Earlier layouts and superseded records remain in Git history; they are not prerequisites for reading or executing the current repository.
- Work autonomously on reversible maintenance. Publishing, journal submission, contacting others, changing the scientific scope or launching a new sampling campaign requires authorization for that action.
