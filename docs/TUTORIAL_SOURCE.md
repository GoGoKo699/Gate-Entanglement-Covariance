# Tutorial source and conventions

The [selected reading map](START_HERE.md#selected-reading) refers to the author-hosted PDF of James A. Mingo and Roland Speicher, *Free Probability and Random Matrices*, Fields Institute Monographs 35, Springer, 2017.

- [Author page and errata](https://rolandspeicher.com/literature/mingo-speicher/)
- [Author PDF](https://rolandspeicher.com/wp-content/uploads/2019/02/mingo-speicher.pdf)
- [Publisher](https://doi.org/10.1007/978-1-4939-6942-5)

The source used for this reading map was retrieved on 13 September 2026: 2,589,396 bytes and 342 physical pages, SHA-256 `a2d9770ee71ff1d8895b3cffb72d503966ecc70aaa142e2de8751e9f5c418f6c`. At the assigned locations, the physical page count from one agrees with the printed author-PDF folio. Published-book pagination differs. The PDF's internal 2019 timestamps do not establish a new published edition. The repository distributes neither the PDF nor its page images.

## Conventions used by the reading map

The Gaussian entries have complex variance one. Our square Wishart matrix is $`W=GG^\dagger/d`$. Fluctuations use unnormalized traces and exact mean centering; normalized traces describe empirical averages.

The book's first-kind convention is $`C_k(x)=2T_k(x/2)`$. At square aspect ratio, Example 42 gives our $`\Gamma_k(x)=2T_k((x-2)/2)`$. A cosine coefficient contributes half as much in this polynomial basis, producing the covariance factor $`1/4`$. The [tutorial bridge](TUTORIAL_BRIDGE.md) derives the conversion explicitly.

## Source caveats

The author's errata correct the optional Exercise 7 on folio 19 to refer to Exercise 6(ii), rather than 6(iii). The other listed corrections concern Lemma 9 on folio 24, Theorem 23 on 124, Exercise 8 on 151 and Figure 5.6 on 162. Those passages are not assigned. Figure 5.6 lies in Section 5.6.1 of this PDF; isolated published-page mappings in the errata do not establish a general pagination offset.

Two nearby passages also require care and are excluded from the reading assignment:

1. Exercise 12(iii), Eq. (5.32), folio 160, has $`C_m(y)`$ in an integral over $`x`$ and displays $`\delta_{nm}`$. Under $`C_n(x)=2T_n(x/2)`$, the positive-degree arcsine norm is $`2\delta_{nm}`$; already $`n=m=1`$ gives $`2`$. The bridge uses the explicit polynomial definition to fix normalization.
2. The informal mean-zero sentence about $`\mathop{\mathrm{Tr}}\nolimits C_n`$ in Theorem 1 on folio 128 omits centering. For example, $`C_2(x)=x^2-2`$ has semicircle mean $`-1`$. Use the preceding scaling discussion and the explicit centering at the start of Section 5.6.

These two reading cautions are not listed as additional author-issued errata. The repository's exact centering and polynomial definitions already implement the stated conventions.
