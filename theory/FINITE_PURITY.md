# Exact finite-dimensional purity covariance

Purity admits an exact finite-dimensional identity relating Haar-input covariance to product-input entangling power. This provides a calibration of the [entropy covariance theorem](THEOREM.md). The calculation below applies to any deterministic global unitary; the fixed-support assumption enters only when taking the large-spectator limit. Taking the logarithm of purity changes the observable, so these finite-dimensional formulas are not exact Rényi-2 entropy formulas.

## Statement and conventions

Let the two halves $`A,B`$ have equal dimension $`d\ge2`$, and let $`\psi`$ be a complex-Haar unit vector on their product. Put

```math
D=d^2,\qquad
P(\psi)=\mathop{\mathrm{Tr}}\nolimits\rho_A(\psi)^2,
\qquad P_U(\psi)=P(U\psi).
```

For a unitary on the complete two-half space, define

```math
(U^R)_{aa',bb'}=U_{ab,a'b'},\qquad
f_d(U)=d^{-4}\mathop{\mathrm{Tr}}\nolimits
\left[(U^R U^{R\dagger})^2\right].
```

Thus $`f_d(U)`$ is the purity of the normalized operator Schmidt probabilities. Let $`S_d`$ exchange the entire halves. The exact input-output purity correlation is

```math
\rho_P(U)=\mathop{\mathrm{Corr}}\nolimits_\psi(P_U,P)
=\frac{D\left[(D+1)\left(f_d(U)+f_d(US_d)\right)-4\right]}
{(D-1)^2}.
```

Both invariants are required for global gates. Define the unnormalized linear-entropy entangling power on the **whole halves** by

```math
e_p^{(d)}(U)=\mathbb E_{a,b}
\left[1-P\left(U\bigl(|a\rangle\otimes|b\rangle\bigr)\right)\right],
```

where the two input vectors are independently Haar-distributed in dimension $`d`$. The same identity becomes

```math
\rho_P(U)=1-\frac{d^2+1}{(d-1)^2}e_p^{(d)}(U)
=1-\frac{e_p^{(d)}(U)}
{\mathbb E_{V\sim\mathrm{Haar}}e_p^{(d)}(V)}.
```

Equivalently,

```math
\mathbb E_\psi\left[(P_U-P)^2\right]
=\frac{4(d+1)^2}{(d^2+1)(d^2+2)(d^2+3)}e_p^{(d)}(U).
```

The Haar ensemble here contains highly entangled inputs. Entangling power uses a different ensemble of product inputs. The equality connects their averages; it does not equate their statewise behavior.

## Four-copy derivation

On two copies of the full system, let $`F_A`$ exchange their first-half factors and $`F_B`$ exchange their second-half factors. Write

```math
X=F_A,\qquad F=F_AF_B,\qquad
Y=(U^\dagger)^{\otimes2}F_AU^{\otimes2}.
```

Both $`X`$ and $`Y`$ commute with the full-copy swap $`F`$. For either $`T=X`$ or $`T=Y`$,

```math
\mathop{\mathrm{Tr}}\nolimits T
=\mathop{\mathrm{Tr}}\nolimits(TF)=d^3,
\qquad
\mathop{\mathrm{Tr}}\nolimits_1T
=\mathop{\mathrm{Tr}}\nolimits_2T=dI_D,
```

```math
\mathop{\mathrm{Tr}}\nolimits_1(TF)
=\mathop{\mathrm{Tr}}\nolimits_2(TF)=dI_D.
```

The partial traces are over an entire global copy. For $`X`$ these identities follow directly from the swap. For $`Y`$, conjugation on the traced copy disappears under the partial trace, and conjugation on the untraced copy preserves $`dI_D`$. The same reasoning applies to $`YF=(U^\dagger)^{\otimes2}F_BU^{\otimes2}`$.

Let $`P_\pi`$ permute four global copies according to $`\pi\in S_4`$. The fourth Haar-vector moment gives

```math
\mathbb E[P P_U]
=\frac{\sum_{\pi\in S_4}
\mathop{\mathrm{Tr}}\nolimits[(X_{12}\otimes Y_{34})P_\pi]}
{D(D+1)(D+2)(D+3)}.
```

All 24 contractions are exhausted by the following table. Permutations are written in one-line notation, so $`3412`$ means $`\pi(1)=3,\pi(2)=4,\pi(3)=1,\pi(4)=2`$.

| Permutations | Count | Trace |
|---|---:|---|
| 1234, 1243, 2134, 2143 | 4 | $`d^6`$ |
| 3412, 4321 | 2 | $`\mathop{\mathrm{Tr}}\nolimits(XY)=d^4f_d(U)`$ |
| 3421, 4312 | 2 | $`\mathop{\mathrm{Tr}}\nolimits(XYF)=d^4f_d(US_d)`$ |
| All remaining permutations | 16 | $`d^4`$ |

To see why these are the only classes, use the subgroup

```math
H=\{e,(12),(34),(12)(34)\}.
```

Its four elements yield products $`\mathop{\mathrm{Tr}}\nolimits(XF^a)\mathop{\mathrm{Tr}}\nolimits(YF^b)=d^6`$. The double coset $`H(23)H`$ has sixteen elements. Moving the within-pair swaps through $`X`$ and $`Y`$ reduces each to one bridge between the pairs, optionally replacing either operator by its product with $`F`$. That bridge contracts their one-copy partial traces, giving $`\mathop{\mathrm{Tr}}\nolimits[(dI_D)(dI_D)]=d^4`$.

The remaining double coset, $`H(13)(24)H`$, has four elements. Exchanging the pairs gives $`\mathop{\mathrm{Tr}}\nolimits(XYF^{a+b})`$, with two even and two odd parities. Expansion in matrix elements identifies the even contraction with the realignment expression for $`d^4f_d(U)`$. In the odd contraction the second subsystem swap is $`F_B`$ instead of $`F_A`$, giving $`d^4f_d(US_d)`$.

Consequently,

```math
\mathbb E[P P_U]
=\frac{4d^6+16d^4+2d^4\left[f_d(U)+f_d(US_d)\right]}
{d^2(d^2+1)(d^2+2)(d^2+3)}.
```

The single-state moments give

```math
\mu_P=\frac{2d}{d^2+1},\qquad
\mathop{\mathrm{Var}}\nolimits P
=\frac{2(d^2-1)^2}{(d^2+1)^2(d^2+2)(d^2+3)}.
```

Subtracting $`\mu_P^2`$ and dividing by this variance proves the correlation formula.

## Product-input contraction

The second moment of the whole-half product-input ensemble is

```math
\mathbb E_{a,b}\left[(|ab\rangle\langle ab|)^{\otimes2}\right]
=\frac{(I+F_A)(I+F_B)}{d^2(d+1)^2}.
```

Contracting with $`Y`$ gives the established entangling-power formula

```math
e_p^{(d)}(U)=\frac{d^2}{(d+1)^2}
\left[1+d^{-2}-f_d(U)-f_d(US_d)\right].
```

Its unitary-Haar mean is $`(d-1)^2/(d^2+1)`$. Substitution proves the entangling-power form of $`\rho_P`$. Equal Haar marginals imply

```math
\mathbb E[(P_U-P)^2]
=2\mathop{\mathrm{Var}}\nolimits(P)\,[1-\rho_P(U)],
```

which gives the stated increment identity. Entangling power above its unitary-Haar mean therefore gives negative purity covariance. This is a correlation of fluctuations, not negative entanglement production.

The two-invariant formula and its Haar mean are due to Zanardi, Zalka and Faoro, [*Entangling power of quantum evolutions*](https://arxiv.org/abs/quant-ph/0005031v1), Propositions 1–2. Operator-entanglement conventions and related quantum-information antecedents are described in [References](../docs/REFERENCES.md). This derivation uses those established identities and the Haar fourth moment.

## Controls and the fixed-support limit

| Global gate | $`f_d(U)`$ | $`f_d(US_d)`$ | Exact purity correlation |
|---|---:|---:|---:|
| Identity | $`1`$ | $`1/d^2`$ | $`1`$ |
| Whole-half SWAP | $`1/d^2`$ | $`1`$ | $`1`$ |
| CNOT with $`d=2`$ | $`1/2`$ | $`1/4`$ | $`-1/9`$ |
| Qutrit permutation described below | $`1/9`$ | $`1/9`$ | $`-1/4`$ |

The qutrit permutation is $`U|i,j\rangle=|i+j,i+2j\rangle`$ with arithmetic modulo three. It is an established perfect permutation from the entangling-power construction above, up to local relabeling.

Both operator purities are at least $`1/d^2`$, so

```math
\rho_P(U)\ge-\frac{2}{d^2-1}.
```

Whenever a gate with both operator purities equal to $`1/d^2`$ exists, it attains this bound. Thus arbitrary global spatial access has no gate-independent positive purity-correlation floor at finite dimension.

For a gate $`u`$ on two active factors of dimension $`q`$, embedded in halves of dimension $`d=qn`$, put

```math
a=f_q(u),\qquad b=f_q(uS_q).
```

Tensor-product factorization of operator Schmidt spectra gives

```math
f_d(U)=a,\qquad f_d(US_d)=b/n^2=(q^2/d^2)b.
```

The global swap also exchanges the spectators. Its contribution therefore vanishes at fixed $`q`$ as $`n\to\infty`$, and the exact formula yields $`\rho_P(U)\to a`$. This agrees with the limiting Rényi-2 correlation in [the theorem](THEOREM.md), whose [proof](PROOF.md) separately justifies the entropy transformation.

Whole-half product inputs can be entangled between an active factor and its spectator inside each half. Therefore $`e_p^{(d)}(U)`$ generally differs from the active gate's product-input entangling power $`e_p^{(q)}(u)`$. [Two subsystem assignments](TWO_CUTS.md) explain how the latter enters sum and difference fluctuations.

## Deterministic verification

[The direct contraction program](../checks/finite_purity/check_exact_global_purity.py) evaluates all 24 Haar traces independently of the contraction classification. Its reference calculation covers 14 global gates at half-dimensions two, three and four. The largest discrepancy in an unnormalized trace is approximately $`1.14\times10^{-13}`$; identity, whole-half SWAP, CNOT and the qutrit control give the correlations above.

These are floating-point evaluations of exact moment identities. They check the algebra and conventions without state sampling, and do not provide certified interval error bounds. Use the [reproduction guide](../REPRODUCE.md) for the maintained commands and output locations.
