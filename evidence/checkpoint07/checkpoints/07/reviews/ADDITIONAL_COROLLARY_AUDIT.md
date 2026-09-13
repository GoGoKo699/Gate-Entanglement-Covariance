# Independent audit: dual-unitary control and finite-dimension purity

12 September 2026. Reviewed `numerics/exact_purity.py` and `results/exact_purity.json` independently of the leading Wick calculation. No random-state simulation was run. The supplementary SWAP check below uses exact rational arithmetic and an independent factor-permutation reduction.

The independent counting is reproducible with `python numerics/exact_swap_audit.py`; its complete 24-term integer counts, rational moments, closed-form checks, and comparisons with all saved rows are in `results/exact_swap_audit.json`. The script uses only the Python standard library and does not import `exact_purity.py` or construct its dense active K.

## Finding

The four-copy Haar calculation is correctly normalized and correctly factored into active and spectator contributions. The saved SWAP purity correlation has the stated exact closed form. The proposed dual-unitary pair has the same limiting equilibrium covariance at every positive Rényi order, despite different behavior on the specified active product input. This last equality is a limiting covariance statement relative to identity, not equality of finite-dimension entropy statistics or of the whole parameter-dependent process.

## Exact Haar moment calculation

Let D=d^2 be the global Hilbert-space dimension and P_U=Tr(rho_A(U)^2). On four copies of the initial pure state,

    P_I P_U = Tr[|psi><psi|^(tensor 4) K],

where K applies the A swap to copies 1,2, and U^(dagger tensor 2) times the A swap times U^(tensor 2) to copies 3,4. The exact complex-Haar moment is

    E[|psi><psi|^(tensor 4)]
      = sum_(pi in S_4) P_pi / [D(D+1)(D+2)(D+3)].

The code's `K=kron(sw,uu.conj().T@sw@uu)` is the active part of this operator. With tau=(12)(34), each term factors as

    Tr(K_active P_pi_active)
      (d/r)^(cycles(tau*pi)) (d/s)^(cycles(pi)).

The row spectator swaps both pairs, and the column spectator swaps neither; these are exactly the powers `nr,nc` used by the code. The `digits[:,inv]` convention evaluates the corresponding active permutation matrix trace. Summing all 24 permutations with the Haar denominator gives the product moment at every admissible finite d.

The common purity mean and variance used in the code are

    E P_U = 2d/(D+1),
    Var(P_U) = 2(D-1)^2/[(D+1)^2(D+2)(D+3)].

Subtracting the square of this exact mean, then dividing by this exact marginal variance, therefore gives the finite-dimension purity correlation. Generic active traces are computed in floating point; 60-digit scalar arithmetic prevents further subtraction loss but does not turn those traces into exact numbers. The JSON states that limitation correctly.

The column `renyi2_delta_method_scaled_covariance` is d^4 Cov(P_I,P_U)/4. It uses the leading entropy linearization around mean purity 2/d. It is **not** the exact finite-dimension covariance of -log P. Its present name and accompanying limitation correctly retain that distinction.

## Independent exact SWAP reduction

For r=s=2 write each half as one active qubit and a spectator of dimension n=d/2. After swapping the active qubits, the first purity swaps original A-active and A-spectator factors on copies 1,2; the second swaps original B-active and A-spectator factors on copies 3,4.

Let a=(12), b=(34), tau=ab. The numerator can therefore be evaluated without constructing the code's active K:

    sum_(pi in S_4)
      2^[cycles(a*pi)+cycles(b*pi)]
      n^[cycles(tau*pi)+cycles(pi)]
      = 256 n^6 + 264 n^4 + 32 n^2
      = 4d^6 + (33/2)d^4 + 8d^2.

The count was recomputed directly and checked with rational arithmetic. It gives

    Cov(P_I,P_SWAP)
      = (D^2+D+16)/[2(D+1)^2(D+2)(D+3)],

    Corr(P_I,P_SWAP)
      = (D^2+D+16)/[4(D-1)^2].

All saved SWAP correlations at d=2,4,8,16,32,64,128,256,1024 agree with this exact expression to the displayed floating-point precision. It is one at d=2, where the gate is whole-half SWAP, and tends to one quarter for fixed one-qubit boundary support as d grows. These checks resolve the distinction between the two limits without invoking the all-degree covariance theorem.

## Dual-unitary family and product-input control

Take

    U_theta = SWAP exp(-i theta Z tensor Z).

In the computational basis,

    U_theta[ab,ce] = delta_(a,e) delta_(b,c)
                    exp(-i theta z_c z_e).

Its realignment R[(a,c),(b,e)] has exactly one nonzero entry of unit modulus in each row and column, at (b,e)=(c,a). Hence R is unitary for every theta, and the normalized operator-Schmidt probabilities are exactly

    eta=(1/4,1/4,1/4,1/4),
    F_k=4^(1-k).

The general fixed-boundary theorem consequently gives the same limiting covariance with the initial equilibrium entropy for every member of this family, at every fixed positive Rényi order. It also gives the same entire matrix of limiting mixed-order covariances between initial and post-gate entropies.

Meanwhile,

    U_theta |++> = (1/2) [e^(-i theta)(|00>+|11>)
                         +e^(i theta)(|01>+|10>)].

The two Schmidt probabilities are (1+|cos(2theta)|)/2 and (1-|cos(2theta)|)/2. At theta=0 the output remains product; at theta=pi/4 it is a maximally entangled two-qubit state. If spectator factors are included in this product-input comparison, they remain product spectators; the conclusion is one Bell pair across the active cut, not a maximally entangled d by d state.

The operator-entanglement versus product-state entangling-power distinction and dual-unitary terminology have substantial prior literature. In particular, Rather, Aravinda and Lakshminarayan, *Creating ensembles of dual unitary and maximally entangling quantum evolutions*, arXiv:1912.12021v3, and Aravinda, Rather and Lakshminarayan, *From dual-unitary to quantum Bernoulli circuits*, arXiv:2101.04580v2, explicitly distinguish maximal operator entanglement from product-state entangling power. The project should claim its equilibrium covariance consequence, not claim to discover that older distinction.

Two scope warnings are material:

1. Equality for the pair (I,U_theta) does not make the full theta process constant: U_theta U_phi^dagger=exp[-i(theta-phi)ZZ], whose operator spectrum generally differs from the flat dual-unitary spectrum.
2. Equality is a statement after the spectator limit. Neither the theorem nor this audit asserts equal finite-dimension purity correlations, equal exact finite-dimension Rényi-2 covariance, or equality of individual-state entanglement changes.

The second warning has an exact illustration in the newly added `phaseSWAP` calculation. At theta=pi/4 a global phase converts U_theta into SWAP diag(1,i,i,1). I independently evaluated its active four-copy trace by its monomial action, without using the code's dense active K. If copies 3,4 initially have bits (a,b),(c,e), their transformed contribution swaps the B bits and multiplies the result by

    i^[(a xor b)+(c xor e)-(a xor e)-(c xor b)].

This is always +1 or -1. Directly counting its 24 permutation traces gives the numerator

    4d^6 + (33/2)d^4 + 4d^2,

and therefore

    Corr(P_I,P_phaseSWAP)
      = (D^2-7D+8)/[4(D-1)^2].

This agrees with the revised saved rows to their displayed floating-point precision and was checked in exact rational arithmetic. Subtraction yields the strictly positive finite-dimension difference

    Corr(P_I,P_SWAP)-Corr(P_I,P_phaseSWAP)
      = 2(D+1)/(D-1)^2.

At d=2 the correlations are respectively 1 and -1/9. Both approach 1/4 as fixed boundary support is embedded in increasing spectators. Thus the equivalence is demonstrably asymptotic, and the exact Haar calculation independently verifies how this particular finite-size distinction disappears. These are purity formulas, not exact logarithmic-entropy formulas.

The proposed corollary is sound with these qualifications.
