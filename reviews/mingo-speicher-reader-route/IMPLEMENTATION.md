# Mingo–Speicher reader route: implementation record

## Starting state and scope

On 13 September 2026, the GitHub connection verified the private repository
`GoGoKo699/Entangling-successions`, whose active project is **Gate Entanglement
Covariance**. The starting branch was `main`, commit
`cddb25ad8b31f18d1684f23b7324b575a3f920ff`, tree
`32a866b0694154eded00780b37ed4dc3b6b4ea7f`. This exactly matched the requested
baseline. The dedicated branch `docs/mingo-speicher-reader-route` did not exist
and was created at that commit. No reset or history rewrite was used.

Work uses an isolated filesystem snapshot, not a local Git checkout. All 235
materialized baseline files matched their remote Git blob hashes before editing;
there were no pre-existing local changes. The historical legacy subtree was read
through GitHub and is preserved by building on the existing Git tree. Its tree
identity is `ffb13b5f01c8c8ad18c80b521feefd3383a34e34`.

The root `AGENTS.md` and the instruction locations in the recursive remote tree
were inspected. The subordinate instruction in `evidence/checkpoint07/AGENTS.md`
governs an unchanged imported subtree. The specified entrance, theory, evidence,
attribution, reproduction and handover documents were read, together with the
needed proof assessments, foundation notes, maintained calculations and CI.

This task changes education and navigation, with focused regression checks.
It does not extend the theorem, add samples, draft a manuscript, or change another
project. Existing evidence, limits, legacy, provenance, reviews and validation
records are protected; this is a new implementation record.

## Verified tutorial source

James A. Mingo and Roland Speicher, *Free Probability and Random Matrices*,
Fields Institute Monographs 35, Springer, 2017, is the sole external background
tutorial. Primary research references retain their attribution and proof roles.

- Author page and errata: <https://rolandspeicher.com/literature/mingo-speicher/>.
- Author PDF linked there: <https://rolandspeicher.com/wp-content/uploads/2019/02/mingo-speicher.pdf>.
- Publisher: <https://doi.org/10.1007/978-1-4939-6942-5>.
- Retrieved: `2026-09-13T05:00:07.237402+00:00`.
- PDF: 2,589,396 bytes, 342 physical pages, SHA-256
  `a2d9770ee71ff1d8895b3cffb72d503966ecc70aaa142e2de8751e9f5c418f6c`.
- Author-page SHA-256:
  `be9a0ec2d912c44a12f00e5370ed1ffe697e75b66bb74c6c2dda47e850c95115`.

Physical PDF pages are counted from one. At every assigned location, that index
equals the printed author-PDF folio. The published book has different pagination;
no equivalence with its page numbers was verified or inferred. The PDF's internal
January 2019 timestamps do not establish a new published edition. The source PDF,
extracted text and rendered pages are temporary inspection material and are not
included in the repository.

The canonical [reading map](../../docs/START_HERE.md#selected-reading) gives the
concept, question and local destination for every selection. Required selections
are §1.4, folio 17 before Exercise 6; §4.5.1, folios 122–123 model paragraphs and
Eq. (4.18), excluding exercises; selected §5.1 material on folios 128–129; the
§5.6 opening on folios 156–157; and Example 42 on folios 160–161. Optional deeper
selections are the §1.1 cumulant introduction on 14–15, selected §§1.3–1.5 on
16–19, the §5.1 annular introduction on 130 and Theorem 9/Eq. (5.5)/Remark 10
on 135, and the opening of Remark 43 on 161. These are excerpts, not assignments
of whole chapters.

All assigned pages were checked against the actual PDF, including visual
inspection. Verified conventions include variance-one complex entries, the
Wishart aspect ratio, normalized versus unnormalized trace, explicit mean
centering, and the first-kind convention
`C_k(x)=2 T_k(x/2)`. Example 42 at square aspect ratio gives our
`Gamma_k(x)=2 T_k((x-2)/2)`. A cosine coefficient therefore contributes half as
much in this polynomial basis, producing the covariance factor `1/4`.

## Source caveats

All six corrections on the author page were inspected. The optional Exercise 7
on author-PDF folio 19 refers to Exercise 6(ii), as the errata correct, rather
than 6(iii). The other listed corrections concern Lemma 9 on 24, Theorem 23 on
124, Exercise 8 on 151 and Figure 5.6 on 162 (two corrections). Those passages
are not assigned. The figure is in §5.6.1 of this PDF, although the author page
labels its section differently. The isolated published-page mappings in the
errata do not establish a general pagination offset.

Two additional reading cautions were found and are outside the assigned text:

1. Exercise 12(iii), Eq. (5.32), folio 160, has `C_m(y)` in an integral over `x`
   and displays `delta_nm`. Under the explicitly defined convention
   `C_n(x)=2 T_n(x/2)`, the positive-degree arcsine norm is `2 delta_nm`; already
   `n=m=1` gives 2. This exercise is not assigned. The local factor-of-four
   explanation uses the explicit polynomial definition, not this exercise.
2. The informal mean-zero sentence about `Tr C_n` in Theorem 1 on folio 128
   omits centering. For example, `C_2(x)=x^2-2` has semicircle mean `-1`.
   The route assigns the preceding scaling discussion and the explicit
   centering at the start of §5.6, not that sentence literally.

Neither caution changes a repository theorem: its centered statistics and
polynomial normalizations already have the stated conventions. They are source
reading discrepancies, not silently repaired scientific claims. Neither is
listed as an additional author-issued erratum here.

## Document roles and preserved assumptions

The entrance exposes LEARN, CHECK and REPRODUCE. `docs/START_HERE.md` owns the
selected reading map; the new `docs/TUTORIAL_BRIDGE.md` owns the quantum-to-matrix
dictionary and conceptual transitions. `docs/WORKED_EXAMPLE.md` retains the
complete boundary-qubit calculation and existing analytical figure. Theorem and
proof remain canonical in `theory/`. Results and the claim ledger retain the
distinction between identities, asymptotic results, deterministic calculations,
finite-size samples and unsuccessful extensions. References separate the sole
tutorial from primary proof inputs. Maintenance and reproduction documents
point to these homes rather than create parallel guides.

The preserved scope is balanced complex Haar, fixed active dimensions, fixed
deterministic finite gate families and fixed positive entropy orders, with the
dimension limit first. Absolute fluctuations shrink. No finite-dimensional exact
entropy law, uniform error rate, growing support/order, shrinking-time or
path-space result, generic prepared-state law, or practical tomography guarantee
is introduced. Rank-based lower bounds retain their separate attainability
conditions. The failed Floquet comparison and adverse finite-size samples stay
visible. Exact purity identities are not exact finite-dimensional entropy laws.

## Checks and integration

Before edits, using Python 3.12.14 and the existing pinned dependencies:

```sh
python scripts/check_repository.py
python scripts/reproduce.py --output-dir ../baseline_reproduction
```

Both passed. Navigation checked 14 maintained pages and 184 local destinations.
Reproduction verified 193 immutable imported hashes, maintained calculations and
all six inherited deterministic programs. Five inherited JSON outputs reproduced
byte for byte; the sixth passed its existing numerical tolerance. There was no
inherited failure and no new sampling.

After implementation, a fresh virtual environment was created and the existing
requirements were installed without changing the pins:

```sh
python -m venv ../validation_venv
../validation_venv/bin/python -m pip install -r requirements.txt
source ../validation_venv/bin/activate
python scripts/reproduce.py
python scripts/check_repository.py
```

Both checks passed. Outputs were generated under `build/reproduction/`.
Navigation now checks 15 maintained pages, 284 local destinations and 27 section
fragments, including image targets and same-page anchors. Isolated temporary
probes confirmed that missing anchors and images fail, while repeated headings,
explicit HTML anchors, and fenced examples are handled. The checker is scoped to
the maintained route, not all historical external links.

Reproduction again verified all 193 imported hashes and all six inherited
programs. Five JSON outputs were byte-identical; `check_two_cut_modes.py` passed
its inherited tolerance. The maintained covariance and gate-spectrum maximum
errors were both `1.11e-16`; the closed order-one coefficient error was
`3.47e-18` and the hierarchy error `1.23e-13`. Ten invalid inputs were rejected.
The reader reference values changed by exactly zero. Cutoff doubling changed the
showcased correlations by less than `1e-9`, a diagnostic rather than a rigorous
remainder bound. No new random states were generated.

The exact runnable snippet in `REPRODUCE.md`, “Check the equal-purity comparison,”
was also executed in that fresh environment. It printed
`Rescaled covariance difference: 0.001930194847` and passed comparison with
`9(3-2 sqrt(2))/800` at tolerance `1e-14`. A separate direct gate-matrix
realignment check agreed with the displayed probabilities within `1.11e-16`
and the order-three difference within `3.29e-16`. These are small deterministic
checks of the existing witness, not new scientific evidence or a sampling study.

## Reader walkthrough and editorial checks

An agent walkthrough used the assigned book passages and maintained documents,
without requiring old chats or checkpoint chronology. It repaired the §1.3
Gaussian-vector label, the endpoint wording around Eq. (4.18), the explanation of
possibly degenerate joint Gaussian covariance, and the explicit centered/scaled
left-hand side at entropy order one. The trace symbol and spectator label are
also distinguished locally. The book-to-project mode normalization and the full
inherited Hu weighted hypothesis were checked against their source conventions.
No project mathematical discrepancy or unresolved hidden prerequisite was found
in this bounded documentation review.

Markdown headings, tables, local anchors, math fences and inline delimiters were
inspected. Eight principal pages were converted using
`pandoc -f gfm+tex_math_dollars -t json`, mapping GitHub `math` code blocks to
Pandoc `Math(DisplayMath)` nodes, then
`pandoc -f json -t html5 --mathml`. All 63 display equations and their inline math
converted without warnings, empty mathematical bodies or error nodes. A first
temporary preview converter mishandled display delimiters; that converter was
corrected and its outputs replaced. The repository's math source was unaffected.
The existing analytical PNG was visually inspected for labels, curves, units and
legend. It was retained unchanged. Temporary previews stay under `build/`.

Actual GitHub browser layout was not exercised: the available Playwright runtime
had no installed browser binary. The checks establish source compatibility and
HTML/MathML conversion, not a pixel-level GitHub rendering test. No actual human
reader test, external peer review or independent scientific replication is claimed.

## Final diff and integration

There are 16 changed paths: the existing README, START_HERE, WORKED_EXAMPLE,
RESULTS, REFERENCES, REPOSITORY_MAP, THEOREM, PROOF, CLAIM_LEDGER, REPRODUCE,
HANDOVER, NEXT and AGENTS documents; the navigation checker; and the new bridge
and this record. The only code edit extends navigation checking. The scientific
library, reproduction entry point, pinned dependencies, CI configuration,
reference figure/table and manuscript-planning file are unchanged.

All 207 materialized baseline files in the protected record directories retained
their exact Git blob hashes after reproduction. The remote tree comparison also
preserved the legacy subtree identity stated above, including its unmaterialized
files. Existing paths and headings in the maintained guides were retained.
The full diff was reviewed against `main`, which remained at the verified
`cddb25ad8b31f18d1684f23b7324b575a3f920ff` baseline. No unrelated research,
manuscript drafting, historical deletion or repository migration is included.

Source/structure verification is commit
`3d3fe3220656ae1a2872b36d8c1acb0ffc79949a`; educational implementation is commit
`b126961218975a001bffd52eadf92e6b37f0fa7e`. On that implementation head,
[GitHub Actions run 34740081003](https://github.com/GoGoKo699/Entangling-successions/actions/runs/34740081003)
passed the clean checkout, pinned install, navigation, full reproduction and
legacy-tree check. This final validation record is committed separately.
[PR 1](https://github.com/GoGoKo699/Entangling-successions/pull/1) records the final
head, final-head CI and merge outcome, avoiding a self-referential merge hash in
this pre-merge record. Integration requires those checks and another current-main
comparison; pending runs must not be described as passed.

There is no unresolved documentation or scientific-scope blocker. The browser
layout limitation is stated above. Stop after checked integration and the
completion report. Manuscript preparation remains a separate final phase.

