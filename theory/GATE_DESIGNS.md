# Exact gate 2-designs with different entropy covariance

Two gate ensembles can have exactly the same second moments as Haar-random gates on the active factors while producing different limiting Rényi-3 entropy correlations on globally Haar input states. This page gives an explicit pair and derives its correlation difference from the [covariance theorem](THEOREM.md). The initial-state ensemble remains complex Haar throughout.

## Fixed gates and operator moments

Use the two-qubit Cartan form

```math
U=\exp[-i(c_1X\otimes X+c_2Y\otimes Y+c_3Z\otimes Z)],
\qquad u_i=\cos^2(2c_i),\quad 0\le c_i\le\pi/4.
```

Here $`X,Y,Z`$ are Pauli matrices. The three generators commute. For any chosen $`u_i\in(0,1)`$, take $`c_i=\tfrac12\cos^{-1}\sqrt{u_i}`$, using the principal inverse cosine. A convention with an additional factor one half in the exponent would instead use angles $`2c_i`$.

Writing $`x_i=\sqrt{u_i}`$, expansion of the Pauli exponentials gives the normalized operator Schmidt probabilities

```math
\begin{aligned}
\eta_1&=(1+x_1x_2+x_1x_3+x_2x_3)/4,\\
\eta_2&=(1-x_1x_2-x_1x_3+x_2x_3)/4,\\
\eta_3&=(1-x_1x_2+x_1x_3-x_2x_3)/4,\\
\eta_4&=(1+x_1x_2-x_1x_3-x_2x_3)/4.
\end{aligned}
```

Consequently, with $`s_2=\sum_{i<j}u_i u_j`$ and $`t=u_1u_2u_3`$,

```math
F_2(U)=\frac{1+s_2}{4},\qquad
F_3(U)=\frac{1+3s_2+6t}{16}.
```

Let $`P`$ swap the two active qubits. Multiplication by $`P`$ replaces the $`u_i`$ by $`1-u_i`$ in these invariants: its Cartan shift changes the squared cosines to the corresponding squared sines.

Choose gates $`U_A,U_B`$ through the exact triples

```math
u_A=\left(\frac12+\sqrt{\frac3{20}},\frac12,
\frac12-\sqrt{\frac3{20}}\right),
```

```math
u_B=\left(\frac12+\sqrt{\frac1{20}},
\frac12+\sqrt{\frac1{20}},\frac12-2\sqrt{\frac1{20}}\right).
```

Both triples have sum $`3/2`$ and pair sum $`s_2=3/5`$. The complementary pair sum is also $`3/5`$, since

```math
\sum_{i<j}(1-u_i)(1-u_j)=3-2\sum_i u_i+s_2.
```

Thus all four relevant second moments agree:

```math
F_2(U_A)=F_2(U_B)=F_2(PU_A)=F_2(PU_B)=2/5.
```

Their products differ:

```math
t_A=\frac1{20},\qquad
t_B=\frac1{20}-\frac{\sqrt5}{100}.
```

Therefore

```math
F_3(U_A)-F_3(U_B)=\frac{3\sqrt5}{800}>0.
```

Both gates have unnormalized active linear-entropy entangling power $`e_p^{(2)}=1/5`$ and gate typicality $`g_t=1/2`$, using the definitions in [Two subsystem assignments](TWO_CUTS.md).

## Local randomization gives exact unitary 2-designs

For each fixed gate, independently sample four single-qubit Haar unitaries and form

```math
\widehat U=(v_1\otimes v_2)U(v_3\otimes v_4).
```

An exact unitary 2-design means that the ensemble's two-copy conjugation average equals the Haar two-copy conjugation average on the two-qubit space. Equivalently, it reproduces all gate polynomials of bidegree at most $`(2,2)`$ in unitary entries and their conjugates.

The local-twirl second-moment formula of Suzuki et al., [*More global randomness from less-random local gates*](https://arxiv.org/abs/2410.24127v3), Section III.2, Eq. 25, depends on entangling power and gate typicality. Their entangling-power normalization is

```math
e_u=\frac{q+1}{q-1}e_p^{(q)}.
```

For qubits this gives $`e_u=3/5`$, and their Haar values are $`e_H=3/5`$, $`g_H=1/2`$. The factor of three is essential when comparing conventions.

Substitution into the orthonormal local-twirl basis gives the reduced second-moment matrix

```math
\begin{pmatrix}
1/10&0&0&3/10\\
0&1/2&1/2&0\\
0&1/2&1/2&0\\
3/10&0&0&9/10
\end{pmatrix}.
```

The two nonzero blocks are rank-one orthogonal projectors. Together, their ranges span the global identity and copy-swap invariants. The input and output local twirls annihilate the complement of the four-dimensional local invariant space. Hence the full moment operator is the global Haar second-moment projector. This proves that both local-randomization ensembles are exact unitary 2-designs on the two active qubits.

These ensembles need not be finite sets. Embedding their gates with identity spectators does not make them global unitary 2-designs on the larger system.

## Entropy covariance is unchanged by the local rotations

Embed the active factors in balanced halves with spectator dimension $`n`$, and let the global input $`\psi`$ be Haar. Fix product rotations $`L,R`$ acting on the active factors. The output rotation $`L`$ preserves the cut entropy. Under $`\chi=R\psi`$, the input entropy also satisfies $`S_\alpha(\psi)=S_\alpha(\chi)`$, and $`\chi`$ remains Haar. Thus

```math
\left(S_\alpha(LUR\psi),S_\alpha(\psi)\right)
\quad\text{and}\quad
\left(S_\alpha(U\chi),S_\alpha(\chi)\right)
```

have exactly the same joint distribution at every finite spectator dimension. Averaging independently over the local rotations preserves this equality. The statement also holds for both exchanged subsystem assignments because every single-factor rotation is local to each assignment.

The operator Schmidt probabilities are likewise unchanged under local pre- and postmultiplication. Hence every gate in an ensemble has the same limiting covariance as its fixed representative. Mixing over the gate draw adds no conditional-mean covariance: for every deterministic gate the conditional entropy means are the same Haar means.

## Exact entropy-correlation separation

The integer-order coefficients of the theorem give

```math
\lim_{d\to\infty}d^2\mathop{\mathrm{Var}}\nolimits S_3=3/4,
\qquad
\rho_3(U)=\frac{24F_2(U)+F_3(U)}{25}.
```

Since the two second moments agree, their limiting correlation difference is exactly

```math
\rho_3(U_A)-\rho_3(U_B)
=\frac{3\sqrt5}{20000}
\simeq0.0003354102.
```

The corresponding rescaled covariance difference is $`9\sqrt5/80000`$, obtained by multiplying by the common variance coefficient $`3/4`$. This order-three calculation terminates exactly and has no series truncation. It supplies a difference at an ordinary positive integer entropy order; no sign claim at every noninteger order follows from this calculation.

## Meaning and verification

Both gate ensembles agree with active Haar gates on every second-moment observable, while their third operator moments and entropy correlations differ. This is consistent with the definition of a 2-design, which constrains no higher moment. The example uses the full [entropy covariance law and its proof](PROOF.md) to identify an explicit entropy observable that distinguishes the two designs; the general fact that second moments do not determine higher moments is established background. See [References](../docs/REFERENCES.md) for the surrounding attribution.

Haar randomness of the initial state is independent of the gate-design property. All entropy-correlation values above use the balanced, fixed-support, large-spectator limit. The stated local-rotation invariance is exact before that limit. The example supplies no replacement of the initial Haar state by a state 2-design, finite-dimensional entropy formula or practical estimation guarantee.

[The deterministic implementation](../checks/numerics/design_pair.py) constructs the two fixed gates and checks their full two-copy twirling superoperators against Haar. The reference Frobenius-norm discrepancies are at most approximately $`3.25\times10^{-16}`$. This numerical comparison is separate from the analytical projector argument above; it is not a certified floating-point error bound and uses no global state samples. The [reproduction guide](../REPRODUCE.md) gives the maintained entry point and reference comparisons.
