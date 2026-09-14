# What the entropy covariance hierarchy identifies

The [covariance theorem](THEOREM.md) turns ideal integer-order entropy covariances into operator Schmidt power sums. A finite triangular inversion then determines any spectrum with a known finite rank bound. The reconstruction can be severely ill-conditioned, so this identifiability statement supplies neither an efficient tomography procedure nor a finite-sample guarantee.

## Finite information determines the spectrum

Let the nonzero normalized operator Schmidt probabilities of a boundary gate be $`\eta_h`$, with known rank bound $`R`$. Pad the spectrum with zeros to length $`R`$ and write

```math
F_k(U)=\sum_{h=1}^R\eta_h(U)^k,\qquad F_1=1.
```

For integer entropy order $`m\ge2`$, define

```math
C_m(U)=\lim_{d\to\infty}d^2\mathop{\mathrm{Cov}}\nolimits
\left[S_m(U\psi),S_m(\psi)\right].
```

The input is complex Haar on balanced halves of dimension $`d`$, with fixed active factors and growing spectators. The rank bound and all entropy orders are fixed before taking this limit; logarithms are natural.

For two gates satisfying these assumptions and having ranks at most $`R`$, the following are equivalent:

1. Their nonzero operator Schmidt probabilities coincide, counting multiplicities.
2. Their limiting entropy cross-covariances agree for every pair of fixed positive orders.
3. Their same-order covariances $`C_m`$ agree for $`m=2,\ldots,R`$.

At rank bound one, normalization alone determines the spectrum $`(1)`$.

To prove the equivalence, define the Catalan number and polynomial coefficients

```math
\mathrm{Cat}_m=\frac1{m+1}\binom{2m}{m},\qquad
q_{m,k}=\binom{2m}{m-k}.
```

The [Chebyshev expansion and shared-trace normalization](PROOF.md) give

```math
C_m=\frac1{(m-1)^2\mathrm{Cat}_m^2}
\sum_{k=2}^m k\binom{2m}{m-k}^{\!2}F_k.
```

The coefficient of $`F_m`$ is nonzero. With $`Y_m=(m-1)^2\mathrm{Cat}_m^2 C_m`$, the explicit triangular inverse is

```math
F_m=\frac{Y_m}{m}
-\sum_{k=2}^{m-1}\frac{k}{m}\binom{2m}{m-k}^{\!2}F_k.
```

This recovers $`F_2,\ldots,F_R`$. Including $`F_1=1`$, Newton's identities give the elementary symmetric polynomials:

```math
e_0=1,\qquad
e_j=\frac1j\sum_{k=1}^j(-1)^{k-1}e_{j-k}F_k.
```

The spectrum, padded with zeros, is the multiset of roots of

```math
p(z)=z^R-e_1z^{R-1}+e_2z^{R-2}-\cdots+(-1)^Re_R.
```

Thus statement 3 implies statement 1. The theorem immediately gives statement 2 from statement 1, and restriction gives statement 3 from statement 2. Noninteger orders and mixed-order covariances are unnecessary for this exact reconstruction.

Same-order correlations suffice as well, because the marginal variance coefficients are gate independent and known. Equality at every integer order determines any finite spectrum even without a supplied rank bound, but that formulation provides no finite stopping order.

## One active qubit on each side

The rank is at most four. The forward equations are

```math
\begin{aligned}
C_2&=\frac12F_2,\\
C_3&=\frac{18}{25}F_2+\frac3{100}F_3,\\
C_4&=\frac89F_2+\frac{16}{147}F_3+\frac1{441}F_4.
\end{aligned}
```

Consequently,

```math
\begin{aligned}
F_2&=2C_2,\\
F_3&=\frac{100}{3}C_3-48C_2,\\
F_4&=441C_4-1600C_3+1520C_2.
\end{aligned}
```

The quartic coefficients are

```math
e_1=1,\qquad e_2=\frac{1-F_2}{2},\qquad
e_3=\frac{1-3F_2+2F_3}{6},
```

```math
e_4=\frac{1-6F_2+3F_2^2+8F_3-6F_4}{24}.
```

Zero roots make the same formulas apply to lower ranks.

## Correlation normalization and conditioning

For every integer $`m\ge2`$, the limiting marginal variance coefficient is

```math
V_m=\lim_{d\to\infty}d^2\mathop{\mathrm{Var}}\nolimits(S_m)=m/4.
```

Indeed, telescoping successive squared binomials gives

```math
\sum_{k=1}^{m}k\binom{2m}{m-k}^{\!2}
=\frac m4\binom{2m}{m}^{\!2}.
```

Subtracting the radial term, using $`q_{m,1}=m\mathrm{Cat}_m`$, and dividing by $`(m-1)^2\mathrm{Cat}_m^2`$ yields the variance above. Put $`\rho_m=C_m/V_m=4C_m/m`$. For active qubits,

```math
\begin{aligned}
F_2&=\rho_2,\\
F_3&=25\rho_3-24\rho_2,\\
F_4&=441\rho_4-1200\rho_3+760\rho_2.
\end{aligned}
```

If every supplied correlation has absolute error at most $`\delta`$, these formulas allow moment errors of $`\delta`$, $`49\delta`$ and $`2401\delta`$, respectively. These bounds are sharp for independently signed bounded errors before imposing physical-spectrum constraints. They describe conditioning of this linear inverse, not a statistical minimax bound. A perturbed moment vector need not correspond to any physical gate.

For example, correlation errors bounded by $`10^{-6}`$ allow an error of $`0.002401`$ in $`F_4`$. At the flat rank-four spectrum, $`F_4=1/64`$, this is about 15.37% of that moment.

The exact inverse matrices have the following row $`\ell_1`$ norms, which give the gains for uniformly bounded coordinate errors:

| Reconstructed moment | Gain from covariance errors | Gain from correlation errors |
|---|---:|---:|
| $`F_2`$ | $`2`$ | $`1`$ |
| $`F_3`$ | $`244/3`$ | $`49`$ |
| $`F_4`$ | $`3561`$ | $`2401`$ |
| $`F_5`$ | $`1016124/5`$ | $`145361`$ |
| $`F_6`$ | $`47770046/3`$ | $`11683841`$ |
| $`F_8`$ | $`491562858265/2`$ | $`182410990273`$ |
| $`F_{12}`$ | $`3228754002187276091543/3`$ | $`799383499057896186721`$ |

The last diagonal coefficient alone in correlation normalization grows as

```math
\frac{(m-1)^2\mathrm{Cat}_m^2}{4}
\sim\frac{16^m}{4\pi m}.
```

Full row norms grow still faster. Redundant mixed-order data, physical constraints or regularization might improve a particular estimator, but no such estimator is analyzed here.

Recovering polynomial roots adds a second instability. At a simple root,

```math
\delta\eta_i=-\frac{\delta p(\eta_i)}{p'(\eta_i)},\qquad
p'(\eta_i)=\prod_{j\ne i}(\eta_i-\eta_j).
```

Nearly colliding roots amplify coefficient errors. This occurs within the physical two-qubit gate set. For $`0\le h\le1/2`$, the attainable family

```math
\eta(h)=\left(\frac14+\frac h2,\frac14+\frac h2,
\frac14-\frac h2,\frac14-\frac h2\right)
```

obeys $`\|\eta(h)-\eta(0)\|_2=h`$, whereas $`F_2(h)-F_2(0)=h^2`$ and every finite set of moments changes only at order $`h^2`$. A uniform Lipschitz inverse near this degeneracy is impossible. Detecting rank near zero roots likewise requires a resolution criterion.

## Physical admissibility and the information boundary

A normalized probability vector need not be the operator Schmidt spectrum of a unitary at specified active dimensions. For two-qubit unitaries the possible ranks are one, two and four; rank three is excluded by the established result of Müller-Hermes and Nechita, [*Operator Schmidt ranks of bipartite unitary matrices*](https://doi.org/10.1016/j.laa.2018.07.018).

Nevertheless, the three moments above are locally independent on an open set of actual two-qubit gates. Consider

```math
U=\exp[i(aX\otimes X+bY\otimes Y+cZ\otimes Z)],
\qquad x=\cos(2a),\quad y=\cos(2b),\quad z=\cos(2c).
```

Expanding the commuting Pauli exponentials gives the probabilities

```math
\begin{aligned}
\eta_1&=(1+xy+xz+yz)/4,\\
\eta_2&=(1-xy-xz+yz)/4,\\
\eta_3&=(1-xy+xz-yz)/4,\\
\eta_4&=(1+xy-xz-yz)/4.
\end{aligned}
```

On $`0<x<y<z<1`$, the map to any three independent listed probabilities has Jacobian determinant of absolute value $`xyz/8`$. The map from three independent probabilities to $`(F_2,F_3,F_4)`$ has a nonzero Vandermonde factor whenever those probabilities are distinct. Thus no universal relation removes one of these moments on the physical gate set. Three locally independent real measurements are generically necessary for continuous recovery of the three-parameter spectrum; this is not a statement about arbitrary discontinuous encodings.

The rational choice $`(x,y,z)=(1/5,2/5,3/5)`$ gives the physical spectrum $`(9/25,13/50,1/5,9/50)`$. The near-flat family is obtained from $`(x,y,z)=(0,2h,1)`$.

Even exact recovery of the spectrum does not determine the unitary, its operator Schmidt bases, its action on a specified input or its active product-input entangling power. The SWAP and phase-SWAP family in [Two subsystem assignments](TWO_CUTS.md) demonstrates this. The equivalence concerns the complete **limiting before/after entropy covariance family with the identity reference**. It does not imply equality at finite dimension or for relative gates formed with other chosen references.

The theorem gives no uniform finite-dimensional bias bound. Any practical estimator must control that bias, covariance uncertainty and entropy-evaluation precision. Absolute covariance shrinks as $`d^{-2}`$, but this fact alone proves no particular sample-complexity scaling. The underlying operator-spectrum and moment methods are credited in [References](../docs/REFERENCES.md).

## Deterministic verification

[The exact inversion program](../checks/inverse/inverse_moments.py) uses Python's standard library and rational arithmetic. It checks forward/inverse matrix products through rank twelve, moments and Newton polynomials for five deterministic spectra including physical qubit examples, the signed-noise bounds and near-flat sensitivity. These are algebraic checks and generate no Haar-state samples. The [reproduction guide](../REPRODUCE.md) provides the maintained entry point.
