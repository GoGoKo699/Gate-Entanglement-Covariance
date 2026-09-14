# Entropy rates at a fixed Schmidt spectrum

The [Haar response study](../studies/haar/README.md) uses an exact finite-dimensional identity for instantaneous entropy rates. It averages over Schmidt bases while holding the Schmidt probabilities fixed. This identity explains the study's conditional covariance diagnostic and the distinction between its conditional error bars and its summaries over random spectra.

The identity is separate from the [finite-time entropy covariance theorem](THEOREM.md). It neither differentiates that theorem through a nonuniform limit nor establishes Gaussian instantaneous rates or a uniform shrinking-time law.

## Ensemble and boundary probe

Let the subsystem dimensions be $`2\le a\le b`$. A pure state is complex Haar on $`\mathbb C^a\otimes\mathbb C^b`$, independently of a fixed interaction

```math
H=A\otimes B,\qquad A=A^\dagger,\quad B=B^\dagger,
\qquad \mathop{\mathrm{Tr}}\nolimits A
=\mathop{\mathrm{Tr}}\nolimits B=0.
```

Condition on positive Schmidt probabilities $`\lambda_1,\ldots,\lambda_a`$, with $`\sum_i\lambda_i=1`$. The two Schmidt bases are independently Haar-distributed, apart from the irrelevant paired-phase redundancy. In the larger subsystem, the Schmidt vectors occupy the first $`a`$ columns of a Haar basis of dimension $`b`$.

The study's probe is a Pauli $`Z`$ on one boundary qubit in each half, tensored with spectator identities. Its local factors are traceless Hermitian involutions:

```math
A^2=I_a,\qquad B^2=I_b,
\qquad \mathop{\mathrm{Tr}}\nolimits A^2=a,
\quad \mathop{\mathrm{Tr}}\nolimits B^2=b.
```

Rates are derivatives at time zero under $`e^{-itH}`$, using natural logarithms and units in which the reduced Planck constant is one. This is the response of a randomly drawn state to a specified perturbation. It does not describe growth from product states or assume that the input is an eigenstate of the probe Hamiltonian.

## Exact conditional covariance

For a differentiable real spectral objective $`F(\lambda)`$, write $`h_i=\partial F/\partial\lambda_i`$. Let $`U,W`$ specify the two Schmidt bases and put

```math
X=U^\dagger A U,\qquad Y=W^\dagger B W.
```

Expanding the Schrödinger equation in those bases gives the unordered-pair expression

```math
\partial_t F=2\sum_{i<j}\sqrt{\lambda_i\lambda_j}
(h_i-h_j)\,\mathop{\mathrm{Im}}\nolimits(X_{ij}Y_{ij}).
```

A reversed matrix-element convention can reverse its overall sign; the covariances below are unchanged. Adding a constant to every $`h_i`$ also changes nothing because the probabilities sum to one.

The unitary Haar second moment for a traceless Hermitian matrix is

```math
\mathbb E[X_{ij}X_{kl}]
=v_A\left(\delta_{il}\delta_{jk}
-\frac{\delta_{ij}\delta_{kl}}{a}\right),
\qquad v_A=\frac{\mathop{\mathrm{Tr}}\nolimits A^2}{a^2-1}.
```

It follows from unitary invariance: the two invariant index contractions have coefficients fixed by $`\mathop{\mathrm{Tr}}\nolimits X=0`$ and $`\mathop{\mathrm{Tr}}\nolimits X^2=\mathop{\mathrm{Tr}}\nolimits A^2`$. The same formula holds for $`Y`$, with

```math
v_B=\frac{\mathop{\mathrm{Tr}}\nolimits B^2}{b^2-1}.
```

Independence of the two bases then gives, for $`i<j`$ and $`k<l`$,

```math
\mathbb E\left[\mathop{\mathrm{Im}}\nolimits(X_{ij}Y_{ij})
\mathop{\mathrm{Im}}\nolimits(X_{kl}Y_{kl})\right]
=\frac{v_Av_B}{2}\delta_{ik}\delta_{jl}.
```

All conditional first moments vanish. If a second spectral objective $`G`$ has derivatives $`k_i`$, the rate covariance is therefore

```math
\mathop{\mathrm{Cov}}\nolimits(\partial_t F,\partial_t G\mid\lambda)
=2v_Av_B\sum_{i<j}\lambda_i\lambda_j
(h_i-h_j)(k_i-k_j),
```

```math
\mathop{\mathrm{Cov}}\nolimits(\partial_t F,\partial_t G\mid\lambda)
=2v_Av_B\left[
\sum_i\lambda_i h_i k_i
-\left(\sum_i\lambda_i h_i\right)
\left(\sum_j\lambda_j k_j\right)\right].
```

The second equality expands the pair sum and uses normalization. The bracket is a classical covariance under the probability weights $`\lambda_i`$ themselves.

For the boundary involution probe, the prefactor is exactly

```math
2v_Av_B=\frac{2ab}{(a^2-1)(b^2-1)}.
```

This holds for every fixed positive spectrum at finite dimension, before any random-matrix spectral approximation. The dependence on the probe in this product-interaction calculation enters through its two Hilbert-Schmidt norms. The identity alone is not sensitive to where the chosen factors sit inside their respective halves.

## Rényi and von Neumann rates

Let $`p_\alpha=\sum_i\lambda_i^\alpha`$. For $`\alpha>0`$ and $`\alpha\ne1`$,

```math
S_\alpha=\frac{\log p_\alpha}{1-\alpha},\qquad
h_{\alpha i}=\frac{\alpha\lambda_i^{\alpha-1}}
{(1-\alpha)p_\alpha}.
```

At order one one may use $`h_{1i}=-\log\lambda_i`$, dropping the irrelevant constant in the entropy derivative. With

```math
w_{\alpha i}=h_{\alpha i}-\sum_j\lambda_jh_{\alpha j},
```

the exact diagnostic used by the study is

```math
\mathbb E[(\partial_tS_\alpha)(\partial_tS_\beta)\mid\lambda]
=\frac{2ab}{(a^2-1)(b^2-1)}
\sum_i\lambda_iw_{\alpha i}w_{\beta i}.
```

For either general product factor pair, the conditional variance has the equivalent scalar form

```math
V_\alpha(\lambda)
=2v_Av_B\left(\frac{\alpha}{1-\alpha}\right)^2
\left[\frac{p_{2\alpha-1}}{p_\alpha^2}-1\right]
\qquad(\alpha\ne1).
```

For distinct orders neither equal to one, the cross-covariance is

```math
2v_Av_B\frac{\alpha\beta}{(1-\alpha)(1-\beta)}
\left[\frac{p_{\alpha+\beta-1}}{p_\alpha p_\beta}-1\right].
```

Negative powers in these expressions are well defined for the fixed positive spectrum. At order one,

```math
V_1(\lambda)=2v_Av_B
\left[\sum_i\lambda_i(\log\lambda_i)^2
-\left(\sum_i\lambda_i\log\lambda_i\right)^2\right].
```

The spectral bracket is the established capacity of entanglement. The Haar integration identity and this capacity interpretation are background ingredients, not new spectral susceptibilities. [References](../docs/REFERENCES.md) explains the random-matrix and quantum-information setting of the main covariance result; its finite-time [proof](PROOF.md) is logically separate from this direct rate calculation.

## Random spectra and moment limitations

At a fixed positive spectrum, a rate is bounded as the Schmidt bases vary over their compact unitary groups. All its conditional moments are finite. Sample standard errors for the fixed-spectrum orientation tests are therefore appropriate. Their conditional mean rates are exactly zero, so those tests compare empirical second moments without subtracting an estimated mean.

Randomizing the spectrum introduces a separate small-eigenvalue issue. At every finite balanced dimension, the complex-Haar smallest-Schmidt-probability density is nonzero at zero. If its value $`\varepsilon`$ tends to zero while the other probabilities remain positive, the singular part of a generic rate has scale

```math
\partial_t S_\alpha\ \sim\ \varepsilon^{\alpha-1/2}
\quad (0<\alpha<1/2),
```

with a generically nonzero coefficient depending on the bases and remaining probabilities. This scale follows directly from the factor $`\sqrt{\lambda_i\lambda_j}`$ and the entropy derivative $`\lambda_i^{\alpha-1}`$ in the pair expression. It identifies the local integrability test; it is not an asserted full probability-tail asymptotic with a specified coefficient.

The singular contribution to the second rate moment involves

```math
\int_0^\delta\varepsilon^{2\alpha-1}\,d\varepsilon,
```

which is finite for every fixed $`\alpha>0`$. The corresponding fourth-moment integral is

```math
\int_0^\delta\varepsilon^{4\alpha-2}\,d\varepsilon,
```

which diverges for $`\alpha\le1/4`$ when the singular coefficient is nonzero. Likewise, in this regime the conditional variance as a random function of the spectrum has finite mean but generically infinite second moment. Degenerate probes can cancel the singular term; these are generic integrability qualifications, not statements about every interaction.

Thus ordinary sample-variance error bars for an unconditional mean squared rate need not be valid at low order. The study instead reports medians and interquartile ranges of the conditional variance over spectra, retaining all sampled states. These quantiles describe a typical conditional response. They are not estimates of its unconditional mean, and a few small eigenvalues do not establish a fitted asymptotic exponent.

For a rectangular ensemble with dimension difference $`\ell=b-a`$, the small-eigenvalue density contains an additional factor $`\varepsilon^\ell`$. The fixed-dimensional integrability test changes accordingly. A fixed aspect ratio below one and a fixed dimension difference are distinct limits.

These moment cautions concern instantaneous derivatives. Exact finite-pulse entropy differences do not require a spectral cutoff, and agreement with a derivative on sampled states does not give an approximation uniform over the Haar ensemble. No rate Gaussian limit, rigorous large-dimension exponent, exact tail coefficient or shrinking-time theorem is asserted here.

## Verification

The study's [production calculation](../studies/haar/numerics/run_experiment.py) evaluates both the physical derivative and the conditional covariance. [Separate response checks](../studies/haar/numerics/audit05.py) use the unordered-pair formula, reduced-density commutators and direct matrix exponentials. The [study page](../studies/haar/README.md) records the fixed-spectrum orientation tests, their sample errors and numerical limitations. Use the [reproduction guide](../REPRODUCE.md) for saved-result checks or optional regeneration.
