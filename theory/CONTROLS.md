# Gate controls and limiting cases

These six checks explain the scope of [the covariance theorem](THEOREM.md). They are the controls from [Section 8 of the original general-gate review](../evidence/checkpoint08/foundation/GENERAL_GATE_REVIEW.md#8-controls-and-physical-consequences-within-scope), with typeset notation. The original review remains available as a preserved source record.

**Product gate.** If $U=A\otimes B$, realignment has one singular value $\sqrt{rs}$, so $\eta=(1)$ and every $F_k=1$. All entanglement increments vanish exactly, as they must.

**Fixed boundary SWAP.** If $r=s=q$ is fixed and $U$ swaps just these $q$-dimensional boundary factors, $\mathcal R(U)$ is a $q^2\times q^2$ permutation matrix. Thus $\eta$ has $q^2$ equal entries $1/q^2$, and

```math
F_k=q^{2-2k}.
```

In particular the limiting normalized Rényi-2 memory is $1/q^2$. The global cut also contains increasing spectators, so this unitary does not preserve the Schmidt spectrum across the full cut. There is no contradiction with the zero-increment whole-half SWAP.

**Whole-half SWAP.** Taking $r=s=d$ breaks the fixed-active-dimension estimate. The active tensor sums can then change the power of $d$ in the spectator topology, and suppressed contraction classes may survive. Its exact zero increment cannot be inserted into the theorem with fixed $r,s$.

**Local basis changes.** Pre- and postmultiplication of a single relative gate by product unitaries preserves its realignment singular values and hence the limiting covariance. In the Haar-pair formulation this invariance is exact even before taking $d$ large, because input local unitaries can be absorbed into the Haar state and output local unitaries preserve its entanglement. This does not imply that arbitrary local terms can be deleted from a noncommuting Hamiltonian at finite times.

**Rank bound.** The realignment rank is at most $\min(r^2,s^2)$, giving

```math
F_k\ge\min(r^2,s^2)^{1-k}.
```

Therefore fixed local support imposes a positive residual limiting memory; the arbitrary-gate rank ceiling differs from the diagonal family ceiling $\min(r,s)$.

**Different gates at different times.** The correct pair kernel is the operator Schmidt power sum of

```math
U(t)U(s)^\dagger.
```

For a time-independent boundary Hamiltonian this is $U(t-s)$, giving stationarity. For a driven boundary sequence one cannot replace it by a function only of the separately listed spectra of $U(t)$ and $U(s)$, nor assume time-translation invariance.
