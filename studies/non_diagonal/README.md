# Haar inputs and non-diagonal boundary gates

This study compares the fixed-support entropy-covariance prediction with two non-diagonal gates and checks the underlying contractions independently. It contains a fixed sample of 192 Haar inputs, leading Gaussian contractions, and exact finite-dimensional purity calculations. The [theorem](../../theory/THEOREM.md) and [proof](../../theory/PROOF.md) give the general result; the sample illustrates its predictions at two finite sizes.

## State ensemble, gates, and observables

Each input is complex Haar on a balanced bipartition with half dimension $`d=32`$ or $`d=64`$. There are 96 independent inputs at each size. A gate acts on one boundary qubit in each half, leaving spectator dimensions $`d/2`$ unchanged. The two gates are boundary SWAP and

```math
U_{mathrm C}=\exp[-i(0.37X\otimes X+0.23Y\otimes Y+0.11Z\otimes Z)].
```

For each input, both gates are applied to the same original state. All three entropy orders $`\alpha=1/2,1,2`$ are measured, with natural logarithms. Order one is von Neumann entropy; order one-half equals the pure-state logarithmic negativity. The recorded difference is

```math
\Delta S_\alpha=S_\alpha(U\psi)-S_\alpha(\psi).
```

The [sampling code](numerics/entropy_pilot.py) generates a complex Gaussian coefficient matrix and divides by its Frobenius norm. Input $`j`$ at half dimension $`d`$ uses NumPy `SeedSequence([90712026, d, j])`, with indices `0` through `95`. Entropies come from squared singular values of the coefficient matrix. Gate application is checked against an independently constructed dense unitary for the first input at each size; the largest saved state and spectrum discrepancies are below $`1.01\times10^{-16}`$ and $`1.95\times10^{-16}`$, respectively.

The gate list, dimensions, sample counts, entropy orders, and stopping rule were set before sampling in the [complete protocol record](protocol.txt). The [prediction record](results/pilot_frozen.json) stores the operator Schmidt probabilities, predictions, seed, and protocol/source hashes. SWAP has four probabilities equal to $`1/4`$. The Cartan probabilities are approximately $`(0.81420788,0.12301979,0.04612691,0.01664542)`$.

## Predicted covariances and measured increments

Write $`V_\alpha=\lim d^2\mathop{\mathrm{Var}}\nolimits(S_\alpha)`$ and $`C_\alpha(U)=\lim d^2\mathop{\mathrm{Cov}}\nolimits(S_\alpha(U\psi),S_\alpha(\psi))`$. Haar invariance makes the two marginal distributions equal, so the limiting rescaled mean-square increment is $`2[V_\alpha-C_\alpha(U)]`$. These covariance coefficients are not normalized correlations. The prediction uses the operator Schmidt power sums and entropy coefficients from the theorem, with series cutoff `65536`.

| Order | Marginal variance coefficient | SWAP covariance coefficient | Cartan covariance coefficient |
|---|---:|---:|---:|
| 1/2 | 0.125000 | 0.0215403 | 0.0737058 |
| 1 | 0.250000 | 0.0569331 | 0.1652173 |
| 2 | 0.500000 | 0.1250000 | 0.3402366 |

Every saved increment comparison is listed below. A measured entry is the sample mean of $`d^2(\Delta S_\alpha)^2`$ followed by one sample standard error over the 96 independent inputs at that size.

| Gate | Order | Limiting prediction | Measured at half dimension 32 | Measured at half dimension 64 |
|---|---:|---:|---:|---:|
| SWAP | 1/2 | 0.206919 | 0.223061 ± 0.029482 | 0.202017 ± 0.025830 |
| SWAP | 1 | 0.386134 | 0.368730 ± 0.044852 | 0.374868 ± 0.051766 |
| SWAP | 2 | 0.750000 | 0.648855 ± 0.072884 | 0.713391 ± 0.100258 |
| Cartan | 1/2 | 0.102588 | 0.095598 ± 0.011438 | 0.114490 ± 0.014935 |
| Cartan | 1 | 0.169565 | 0.164616 ± 0.021260 | 0.173503 ± 0.024518 |
| Cartan | 2 | 0.319527 | 0.300049 ± 0.042827 | 0.305910 ± 0.048248 |

The [full summary](results/pilot_summary.json) retains unrounded values. The two [input-observable arrays at dimension 32](results/pilot_d32.npz) and [dimension 64](results/pilot_d64.npz) contain `orders`, `base`, `deltas`, and `purities`. The base-entropy array has shape `(96, 3)`; increments have shape `(96, 2, 3)` in gate order SWAP, Cartan; purity columns contain the input, SWAP output, and Cartan output. These records retain paired observables, not the full input state vectors.

The results illustrate the predicted scale at this resolution. They do not establish a convergence rate. The same inputs are reused across gates and orders, so those entries are correlated. Standard errors describe input sampling, exclude bias from finite dimension and series truncation, and do not turn deviations from the limiting prediction into calibrated hypothesis tests. No inputs were added in response to agreement or disagreement. The displayed sample statistic is a mean-square increment, not a direct estimate of every cross-order covariance.

## Independent contraction and purity checks

The [Gaussian contraction program](numerics/general_gate_wick.py) explicitly evaluates the active tensor networks of every leading connected pairing. It then transforms the resulting monomial covariances to shifted Chebyshev modes and compares the entire covariance matrix, including its off-diagonal entries, with the predicted diagonal matrix $`\delta_{jk}kF_k(U)`$.

The [saved matrices and gate definitions](numerics/general_gate_wick.json) cover identity, ZZ, CNOT, iSWAP, partial SWAP, a Cartan gate, deterministic QR gates on active dimensions $`2\times2`$ and $`2\times3`$, SWAP, and phase-decorated SWAP. All ten gates are checked through degree three; the first eight are also checked through degree four. The largest absolute discrepancies are $`4.57\times10^{-13}`$ through degree three and $`3.79\times10^{-10}`$ through degree four. The higher-degree calculation involves cancellation of larger monomial terms. These are floating-point polynomial checks, not a replacement for the entropy approximation argument in the proof. The Cartan parameters here are `(0.19, 0.37, 0.53)`, distinct from the sampling gate above.

The [finite-dimensional purity program](numerics/exact_purity.py) independently contracts all 24 terms of the exact four-copy Haar moment. It covers identity, ZZ, SWAP, phase-decorated SWAP, and the sampling Cartan gate, at half dimensions `2, 4, 8, 16, 32, 64, 128, 256, 1024`. The [complete outputs](results/exact_purity.json) include product moments, covariances, and correlations. Active traces use floating point; scalar accumulation uses 60-digit decimal arithmetic.

For SWAP and $`\mathrm{SWAP}\,e^{-i\pi Z\otimes Z/4}`$, a separate [integer and rational calculation](numerics/exact_swap_audit.py) checks the closed forms and all 18 saved rows. With $`D=d^2`$, their purity correlations are

```math
\rho_{P,\mathrm{SWAP}}=\frac{D^2+D+16}{4(D-1)^2},\qquad
\rho_{P,\mathrm{phaseSWAP}}=\frac{D^2-7D+8}{4(D-1)^2}.
```

Their difference is $`2(D+1)/(D-1)^2`$, and both tend to $`1/4`$. At half dimension two, SWAP exchanges the entire halves and has correlation one, while phase-decorated SWAP has correlation $`-1/9`$. These are exact purity statements, as recorded in the [rational results](results/exact_swap_audit.json). A purity correlation at finite dimension is not a Rényi-2 entropy correlation; the entropy relation uses the asymptotic delta method. Whole-half SWAP and fixed boundary SWAP also obey different support limits.

The [reproduction guide](../../REPRODUCE.md) describes the deterministic checks and optional regeneration of this fixed sample in a temporary output directory.
