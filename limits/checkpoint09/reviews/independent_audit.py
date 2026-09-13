"""Independent audit of frozen checkpoint 09; imports no production functions.

Rebuilds the full Floquet matrix by sparse Kronecker gate embeddings; checks
all saved eigenvectors against that matrix. Entropy anchors instead diagonalize
Hermitian reduced density matrices. No new state or gate samples are generated.
"""
import os
for variable in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']:
    os.environ[variable] = '1'
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import numpy as np
from scipy import sparse
from scipy.linalg import qr

ROOT = Path(__file__).resolve().parents[1]
GATES = ['identity', 'SWAP', 'phaseSWAP']
ALPHAS = [.5, 1., 2.]


def embed(gate, bond, n):
    return sparse.kron(sparse.eye(2**bond, format='csr'),
        sparse.kron(sparse.csr_matrix(gate), sparse.eye(2**(n-bond-2), format='csr'),
                    format='csr'), format='csr')


def reduced_spectrum_entropy(vector, d):
    coefficient = vector.reshape(d, d)
    rho = coefficient @ coefficient.conj().T
    probabilities = np.linalg.eigvalsh(rho)
    assert probabilities.min() > 0, 'Frozen anchors have full-rank positive spectra.'
    return (np.array([2*math.log(np.sqrt(probabilities).sum()),
                      -np.sum(probabilities*np.log(probabilities)),
                      -math.log(np.dot(probabilities, probabilities))]),
            np.dot(probabilities, probabilities), probabilities)


def haar_benchmarks(n):
    d = 2**(n//2); D = d*d
    harmonic = lambda m, p: math.fsum(1/j**p for j in range(1, m+1))
    trigamma_integer = lambda m: math.pi**2/6-harmonic(m-1, 2)
    mean = harmonic(D, 1)-harmonic(d, 1)-(d-1)/(2*d)
    variance = (-trigamma_integer(D+1)+2*d/(D+1)*trigamma_integer(d)
                -(d+1)*(3*d+1)/(4*d*d*(D+1)))
    purity_mean = Fraction(2*d, D+1)
    purity_variance = Fraction(2*(D-1)**2, (D+1)**2*(D+2)*(D+3))
    correlation = [Fraction(1), Fraction(D*D+D+16, 4*(D-1)**2),
                   Fraction(D*D-7*D+8, 4*(D-1)**2)]
    finite = dict(d=d, purity_mean=float(purity_mean), purity_variance=float(purity_variance),
                  von_neumann_mean=mean, von_neumann_variance=variance, gates={})
    for name, rho in zip(GATES, correlation):
        finite['gates'][name] = dict(correlation=float(rho),
            covariance=float(purity_variance*rho), msd=float(2*purity_variance*(1-rho)))
    entropy = {}
    for name in GATES:
        rows = []
        for alpha in ALPHAS:
            if alpha == .5:
                coefficient_squared = lambda k: (1.5/(k*k-.25))**2
            elif alpha == 1:
                coefficient_squared = lambda k: (4/(k*(k*k-1)))**2
            else:
                coefficient_squared = lambda k: float(k == 2)
            # Both nonidentity probes have four OS weights 1/4. The 64-term
            # tail is negligible (<1e-38 even under a loose coefficient bound).
            var = alpha/4
            cov = var if name == 'identity' else math.fsum(
                .25*k*coefficient_squared(k)*4.**(1-k) for k in range(2, 65))
            rows.append(dict(order=alpha, scaled_variance=var, scaled_covariance=cov,
                             correlation=cov/var, scaled_msd=2*(var-cov)))
        entropy[name] = rows
    return finite, entropy


def statistics(x, y):
    means = np.array([x.mean(), y.mean()])
    cov = np.cov(np.stack([x, y]), bias=True)
    return dict(mean_before=float(means[0]), mean_after=float(means[1]),
        mean_shift=float(means[1]-means[0]), variance_before=float(cov[0, 0]),
        variance_after=float(cov[1, 1]), covariance=float(cov[0, 1]),
        correlation=float(cov[0, 1]/np.sqrt(cov[0, 0]*cov[1, 1])),
        msd=float(np.linalg.norm(y-x)**2/x.size),
        mean_shift_in_input_sd=float((means[1]-means[0])/np.sqrt(cov[0, 0])))


def compare_tree(actual, expected, prefix=''):
    errors = []
    if isinstance(expected, dict):
        for key, value in expected.items():
            assert key in actual, prefix+'/'+key
            errors.extend(compare_tree(actual[key], value, prefix+'/'+key))
    elif isinstance(expected, list):
        assert len(actual) == len(expected)
        for index, value in enumerate(expected):
            errors.extend(compare_tree(actual[index], value, prefix+f'/{index}'))
    elif isinstance(expected, (bool, np.bool_)) or expected is None:
        assert actual == expected, (prefix, actual, expected)
    elif isinstance(expected, (float, int, np.number)):
        delta = abs(actual-expected)
        assert delta < 2e-10*max(1, abs(expected)), (prefix, actual, expected)
        errors.append((float(delta), prefix))
    else:
        assert actual == expected, prefix
    return errors


def audit_size(n, predictions):
    source = ROOT/f'results/cohort_N{n}.npz'
    data = np.load(source)
    saved = json.loads((ROOT/f'results/summary_N{n}.json').read_text())
    D = 2**n; d = 2**(n//2)
    unitary = np.eye(D, dtype=complex)
    coordinates = data['bond_coordinates']
    expected_coordinates = np.arange(-n//2, n//2-1)
    assert np.array_equal(coordinates, expected_coordinates)
    gate_seed_errors = []
    for x, gate in zip(coordinates, data['bond_gates']):
        rng = np.random.default_rng(np.random.SeedSequence([2026091209, int(x)+100]))
        z = rng.standard_normal((4, 4))+1j*rng.standard_normal((4, 4))
        q, r = qr(z)
        regenerated = q @ np.diag(np.diag(r)/np.abs(np.diag(r)))
        gate_seed_errors.append(float(np.max(abs(gate-regenerated))))
    assert max(gate_seed_errors) < 1e-13
    for parity in [1, 0]:
        for x, gate in zip(coordinates, data['bond_gates']):
            if x % 2 == parity:
                unitary = embed(gate, int(x)+n//2, n) @ unitary
    vectors, values = data['eigenvectors'], data['eigenvalues']
    residual = np.linalg.norm(unitary@vectors-vectors@np.diag(values), axis=0)
    orth_error = float(np.max(abs(vectors.conj().T@vectors-np.eye(D))))
    unitarity = float(np.linalg.norm(unitary.conj().T@unitary-np.eye(D))/math.sqrt(D))
    assert residual.max() < 1e-10 and orth_error < 1e-10 and unitarity < 1e-12
    phases = np.angle(values)
    assert np.all(np.diff(phases) >= 0)
    gaps = np.diff(np.append(phases, phases[0]+2*math.pi))
    ratios = np.array([min(gaps[j], gaps[(j+1)%D])/max(gaps[j], gaps[(j+1)%D]) for j in range(D)])
    assert np.max(abs(ratios-data['gap_ratios'])) < 1e-13
    diagonal = dict(eigen_residual_max=float(residual.max()), orthogonality_max_entry=orth_error,
        unitarity_frobenius_relative=unitarity,
        minimum_eigenphase_gap=float(gaps.min()), mean_circular_gap_ratio=float(ratios.mean()),
        scaled_computational_ipr=float(D*np.mean(np.sum(abs(vectors)**4, axis=0))))
    diag_errors = compare_tree(saved['diagnostics'], diagonal)
    # Independently define the three physical probes, including the order of
    # SWAP and diagonal phase (they commute, but no saved gate is blindly used).
    swap = np.zeros((4, 4), complex)
    for left in range(2):
        for right in range(2):
            swap[2*right+left, 2*left+right] = 1
    zz = np.kron(np.diag([1, -1]), np.diag([1, -1]))
    pulse = math.cos(math.pi/4)*np.eye(4)-1j*math.sin(math.pi/4)*zz
    probes = [np.eye(4), swap, swap@pulse]
    assert np.max(abs(data['probe_gates']-np.array(probes))) < 1e-14
    indices = np.linspace(0, D-1, 16, dtype=int)
    errors, p_errors, tail_errors = [], [], []
    spectra_before = []
    for gi, gate in enumerate(probes):
        transformed = embed(gate, n//2-1, n) @ vectors[:, indices]
        for ai, index in enumerate(indices):
            e, p, spectrum = reduced_spectrum_entropy(transformed[:, ai], d)
            errors.append(float(np.max(abs(e-data['entropies'][gi, index]))))
            p_errors.append(float(abs(p-data['purities'][gi, index])))
            tail_errors.append(float(abs(spectrum[0]-data['minimum_schmidt_probabilities'][gi, index])))
            if gi == 0:
                spectra_before.append(spectrum)
    assert max(errors) < 1e-10 and max(p_errors) < 1e-12
    crossing = data['bond_gates'][np.flatnonzero(coordinates == -1)[0]]
    transformed = embed(crossing, n//2-1, n) @ vectors[:, indices]
    anchor_spectrum_error, anchor_entropy_error = [], []
    for ai, index in enumerate(indices):
        e, p, spectrum = reduced_spectrum_entropy(transformed[:, ai], d)
        anchor_spectrum_error.append(float(np.max(abs(spectrum-spectra_before[ai]))))
        anchor_entropy_error.append(float(np.max(abs(e-data['entropies'][0, index]))))
    assert max(anchor_entropy_error) < 1e-10 and max(anchor_spectrum_error) < 1e-12
    finite, entropy_benchmarks = haar_benchmarks(n)
    benchmark_errors = compare_tree(predictions['finite'][str(n)], finite)
    for name in GATES:
        benchmark_errors.extend(compare_tree(predictions['gates'][name]['entropy'], entropy_benchmarks[name]))
    recomputed = {'entropy': {}, 'purity': {}}
    for gi, name in enumerate(GATES):
        rows = []
        for ai, alpha in enumerate(ALPHAS):
            row = statistics(data['entropies'][0, :, ai], data['entropies'][gi, :, ai])
            reference = entropy_benchmarks[name][ai]
            row.update(order=alpha, scaled_covariance=D*row['covariance'],
                variance_before_ratio=D*row['variance_before']/reference['scaled_variance'],
                variance_after_ratio=D*row['variance_after']/reference['scaled_variance'],
                correlation_residual=row['correlation']-reference['correlation'],
                msd_ratio=D*row['msd']/reference['scaled_msd'] if gi else None)
            row['criteria'] = dict(input_scale=.75 <= row['variance_before_ratio'] <= 1.25,
                output_scale=.75 <= row['variance_after_ratio'] <= 1.25,
                correlation=abs(row['correlation_residual']) <= .10,
                increment=True if not gi else .75 <= row['msd_ratio'] <= 1.25,
                mean_shift=abs(row['mean_shift_in_input_sd']) <= .25)
            row['within_declared_band'] = all(row['criteria'].values()) if gi else None
            if alpha == 1:
                row.update(exact_haar_variance_before_ratio=row['variance_before']/finite['von_neumann_variance'],
                           exact_haar_mean_difference=row['mean_before']-finite['von_neumann_mean'])
            rows.append(row)
        recomputed['entropy'][name] = rows
        row = statistics(data['purities'][0], data['purities'][gi])
        row.update(exact_haar_variance_before_ratio=row['variance_before']/finite['purity_variance'],
            exact_haar_variance_after_ratio=row['variance_after']/finite['purity_variance'],
            exact_haar_correlation_residual=row['correlation']-finite['gates'][name]['correlation'])
        recomputed['purity'][name] = row
    recomputed['probe_pair_correlation_difference'] = [
        recomputed['entropy']['SWAP'][ai]['correlation']-
        recomputed['entropy']['phaseSWAP'][ai]['correlation'] for ai in range(3)]
    summary_errors = compare_tree(saved, recomputed)
    assert np.all(np.isfinite(data['entropies']))
    assert np.all(data['minimum_schmidt_probabilities'] > 0)
    assert saved['minimum_schmidt_probability'] == float(data['minimum_schmidt_probabilities'].min())
    assert saved['protocol_sha256'] == hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest()
    assert saved['predictions_sha256'] == hashlib.sha256((ROOT/'results/predictions.json').read_bytes()).hexdigest()
    assert saved['source_sha256'] == hashlib.sha256((ROOT/'floquet_test.py').read_bytes()).hexdigest()
    return dict(N=n, state_count=D, eigenvectors_checked=D, entropy_anchor_count=16*3,
        own_gate_anchor_count=16, diagnostics=diagonal,
        max_gate_seed_error=max(gate_seed_errors), max_entropy_anchor_error=max(errors),
        max_purity_anchor_error=max(p_errors), max_smallest_probability_anchor_error=max(tail_errors),
        max_own_gate_spectrum_change=max(anchor_spectrum_error),
        max_own_gate_entropy_change=max(anchor_entropy_error),
        max_summary_error=max(summary_errors), max_benchmark_error=max(benchmark_errors),
        max_diagnostics_difference=max(diag_errors),
        full_saved_summary_recomputed=recomputed,
        cohort_sha256=hashlib.sha256(source.read_bytes()).hexdigest())


def main():
    freeze = json.loads((ROOT/'FREEZE.json').read_text())
    for relative in ['PROTOCOL.md', 'results/predictions.json']:
        assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest() == freeze['files'][relative]
    original = (ROOT/'history/floquet_test_initial.py').read_text()
    current = (ROOT/'floquet_test.py').read_text()
    assert hashlib.sha256(original.encode()).hexdigest() == freeze['files']['floquet_test.py']
    assert current == original.replace('json.dumps(out,indent=2)',
                'json.dumps(out,indent=2,default=lambda value:value.item())')
    predictions = json.loads((ROOT/'results/predictions.json').read_text())
    results = dict(status='passed', no_production_imports=True, new_eigendecompositions=0,
        numerical_source_amendment='Only NumPy scalar JSON serialization conversion', sizes=[])
    for n in [8, 10]:
        results['sizes'].append(audit_size(n, predictions))
        print(json.dumps({k:v for k,v in results['sizes'][-1].items()
                          if k != 'full_saved_summary_recomputed'}, indent=2), flush=True)
    results['audit_source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'reviews/independent_audit.json').write_text(json.dumps(results, indent=2)+'\n')


if __name__ == '__main__':
    main()
