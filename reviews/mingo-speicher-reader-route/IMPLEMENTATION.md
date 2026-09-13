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

Implementation, final reader-route checks, protected-file comparison and remote
integration are in progress. Their exact outcomes will be recorded here before
completion. These checks are documentation review and regression validation,
not human reader testing, independent scientific replication or external peer
review.
