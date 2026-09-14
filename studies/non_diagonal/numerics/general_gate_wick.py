"""Independent leading connected Wick contractions for a finite boundary gate.

No Haar-state Monte Carlo is used. A complex Gaussian coefficient matrix is
viewed as an r-by-s active block matrix with large spectator indices. Every
connected Wick pairing with leading spectator-loop count is retained, and
its *active* tensor network is evaluated explicitly from the unitary entries.
The operator-Schmidt moment formula is computed only as a separate comparator.

Run: python numerics/general_gate_wick.py
"""
from pathlib import Path
from itertools import permutations
from functools import lru_cache
from time import perf_counter
import json
import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent


def cycle_count(perm):
    seen = set()
    count = 0
    for start in range(len(perm)):
        if start in seen:
            continue
        count += 1
        j = start
        while j not in seen:
            seen.add(j)
            j = perm[j]
    return count


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x


@lru_cache(None)
def leading_networks(p, q):
    """Return raw active networks; no unitarity or Schmidt simplification."""
    n = p + q
    gamma = list(range(1, p)) + [0] + list(range(p + 1, n)) + [p]
    output = []
    all_connected = 0
    for sigma in permutations(range(n)):
        if all(sigma[i] < p for i in range(p)):
            continue
        all_connected += 1
        nr = cycle_count([gamma[sigma[i]] for i in range(n)])
        nc = cycle_count(sigma)
        if nr + nc != n:
            continue
        inv_sigma = np.argsort(sigma)
        # R_i, C_i, X_i, Y_i have distinct labels before time-zero deltas.
        R = list(range(n))
        C = list(range(n, 2 * n))
        X = list(range(2 * n, 3 * n))
        Y = list(range(3 * n, 4 * n))
        uf = UnionFind(4 * n)
        for i in range(p):
            uf.union(X[i], R[i])
            uf.union(Y[i], C[i])
        for j in range(p):
            uf.union(X[inv_sigma[j]], R[gamma[j]])
            uf.union(Y[inv_sigma[j]], C[j])
        tensors = []
        for i in range(p, n):
            tensors.append((False, [R[i], C[i], X[i], Y[i]]))
        for j in range(p, n):
            tensors.append((True, [R[gamma[j]], C[j],
                                   X[inv_sigma[j]], Y[inv_sigma[j]]]))
        root_labels = {uf.find(i) for i in range(4 * n)}
        compact = {r: i for i, r in enumerate(sorted(root_labels))}
        contracted = []
        tensor_roots = set()
        for conjugate, labels in tensors:
            roots = [uf.find(i) for i in labels]
            tensor_roots.update(roots)
            contracted.append((conjugate, tuple(compact[r] for r in roots)))
        # Entirely time-zero active loops contribute a dimension without
        # appearing in any tensor. Keep them rather than silently dropping.
        unused = root_labels - tensor_roots
        row_roots = {uf.find(i) for i in R + X}
        col_roots = {uf.find(i) for i in C + Y}
        assert row_roots.isdisjoint(col_roots)
        free_rows = len(unused & row_roots)
        free_cols = len(unused & col_roots)
        output.append((nr, nc, tuple(contracted), free_rows, free_cols))
    return tuple(output), all_connected


def power_covariance(unitary, r, s, p, q):
    u = np.asarray(unitary).reshape(r, s, r, s)
    uc = u.conj()
    total = 0.0j
    networks, all_connected = leading_networks(p, q)
    # Most permutations give identical networks. Evaluate them independently
    # here to retain a direct, uncomplicated contraction audit.
    for nr, nc, network, free_rows, free_cols in networks:
        args = []
        for conjugate, labels in network:
            args.extend([uc if conjugate else u, list(labels)])
        args.append([])
        active = np.einsum(*args, optimize='greedy')
        total += active * r ** (free_rows - nr) * s ** (free_cols - nc)
    return total, len(networks), all_connected


def operator_schmidt_weights(u, r, s):
    realigned = u.reshape(r, s, r, s).transpose(0, 2, 1, 3).reshape(r*r, s*s)
    return np.linalg.svd(realigned, compute_uv=False)**2 / (r*s)


def qr_unitary(dim, seed):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(dim, dim)) + 1j*rng.normal(size=(dim, dim))
    q, rr = np.linalg.qr(z)
    return q @ np.diag(np.diag(rr) / abs(np.diag(rr)))


def gates():
    x = np.array([[0, 1], [1, 0]], complex)
    y = np.array([[0, -1j], [1j, 0]], complex)
    z = np.diag([1., -1.])
    swap = np.eye(4, dtype=complex)[[0, 2, 1, 3]]
    yield 'identity', np.eye(4, dtype=complex), 2, 2
    yield 'ZZ_0.37', expm(-0.37j*np.kron(z, z)), 2, 2
    yield 'CNOT', np.eye(4, dtype=complex)[[0, 1, 3, 2]], 2, 2
    yield 'iSWAP', np.array([[1,0,0,0], [0,0,1j,0],
                            [0,1j,0,0], [0,0,0,1]], complex), 2, 2
    yield 'partialSWAP_0.41', expm(-0.41j*swap), 2, 2
    yield 'Cartan_0.19_0.37_0.53', expm(-1j*(0.19*np.kron(x,x)
          + 0.37*np.kron(y,y) + 0.53*np.kron(z,z))), 2, 2
    yield 'QR_U4_seed_7201', qr_unitary(4, 7201), 2, 2
    yield 'QR_U6_2x3_seed_7202', qr_unitary(6, 7202), 2, 3
    yield 'SWAP', swap, 2, 2
    yield 'phaseSWAP_pi_over_4', swap @ expm(-0.25j*np.pi*np.kron(z,z)), 2, 2


def real_and_imag(a):
    return dict(real=np.asarray(a).real.tolist(), imaginary=np.asarray(a).imag.tolist())


def main():
    start = perf_counter()
    # Positive-power coefficients of Gamma_1,...,Gamma_4. Constants have
    # zero covariance, so need not be represented in the contractions.
    full_transform = np.array([[1,0,0,0], [-4,1,0,0], [9,-6,1,0],
                               [-16,20,-8,1]], dtype=float)
    results = {}
    for name, unitary, r, s in gates():
        tick = perf_counter()
        degree = 3 if name in ('SWAP', 'phaseSWAP_pi_over_4') else 4
        transform = full_transform[:degree,:degree]
        power = np.zeros((degree,degree), complex)
        counts = np.zeros((degree,degree), dtype=int)
        connected = np.zeros((degree,degree), dtype=int)
        for p in range(1,degree+1):
            for q in range(1,degree+1):
                power[p-1,q-1], counts[p-1,q-1], connected[p-1,q-1] = \
                    power_covariance(unitary, r, s, p, q)
        got = transform @ power @ transform.T
        eta = operator_schmidt_weights(unitary, r, s)
        expected = np.diag([k*np.sum(eta**k) for k in range(1,degree+1)])
        discrepancy = float(np.max(abs(got-expected)))
        results[name] = dict(active_dimensions=[r,s],
            maximum_chebyshev_degree=degree,
            unitary_residual=float(np.linalg.norm(unitary.conj().T@unitary-np.eye(r*s))),
            unitary=real_and_imag(unitary), operator_schmidt_weights=eta.tolist(),
            leading_pairing_counts=counts.tolist(), all_connected_pairing_counts=connected.tolist(),
            power_covariances=real_and_imag(power),
            chebyshev_covariances=real_and_imag(got),
            predicted_chebyshev_covariances=expected.tolist(),
            chebyshev_discrepancies=real_and_imag(got-expected),
            maximum_absolute_discrepancy=discrepancy,
            through_degree_three_maximum_discrepancy=float(
                np.max(abs(got[:3,:3]-expected[:3,:3]))),
            maximum_imaginary_residual=float(abs(got.imag).max()),
            elapsed_seconds=perf_counter()-tick)
        print(name, 'max discrepancy', discrepancy, flush=True)
        if discrepancy > 1e-8:
            print('Substantial discrepancy: retaining evidence and stopping.', flush=True)
            break
    dual_unitary_comparison = {}
    for name, unitary, r, s in gates():
        if name not in ('SWAP', 'phaseSWAP_pi_over_4'):
            continue
        # The single exact, fixed product input is |+>|+>. This is an algebraic
        # control, not a random-state experiment or an entangling-power average.
        output_state = unitary @ (np.ones(4)/2)
        lambdas = np.linalg.svd(output_state.reshape(2,2), compute_uv=False)**2
        nonzero = lambdas[lambdas > 1e-15]
        dual_unitary_comparison[name] = dict(
            operator_schmidt_weights=operator_schmidt_weights(unitary,2,2).tolist(),
            output_schmidt_probabilities_for_plus_plus=lambdas.tolist(),
            output_von_neumann_entropy_nats=float(-np.sum(nonzero*np.log(nonzero))))
    output = dict(status='passed' if len(results)==10 and all(
        x['maximum_absolute_discrepancy']<1e-8 for x in results.values()) else 'mismatch',
        scope='Deterministic leading connected complex Gaussian covariance through shifted Chebyshev degree four for eight fixed boundary unitaries, plus degree three for SWAP and phaseSWAP; no Haar sampling and no nonpolynomial extension.',
        convention='Balanced spectator limit; active block dimensions r and s may differ. Operator Schmidt weights are singular values squared of realigned U divided by r*s.',
        formula='Cov(Tr Gamma_j,Tr Gamma_k) = delta_jk * k * sum_l eta_l**k',
        floating_point='complex128', results=results,
        dual_unitary_comparison=dual_unitary_comparison,
        total_elapsed_seconds=perf_counter()-start)
    (ROOT/'general_gate_wick.json').write_text(json.dumps(output,indent=2)+'\n')
    print('status:', output['status'], flush=True)


if __name__ == '__main__':
    main()
