"""Independent numerical audit; does not import the production implementation."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
from pathlib import Path
import hashlib
import json
import numpy as np
import scipy.linalg as sla

ROOT = Path(__file__).resolve().parent
ORDERS = np.array([.125, .25, .5, 1., 2.])

def state(d, index):
    rng = np.random.default_rng(np.random.SeedSequence([90512026, d, index]))
    z = rng.standard_normal(d*d) + 1j*rng.standard_normal(d*d)
    return z / np.sqrt(np.vdot(z, z).real)

def h(lam):
    lam = np.asarray(lam, dtype=np.longdouble)
    return np.array([-np.log(lam) if alpha == 1 else
                     alpha*lam**(alpha-1)/((1-alpha)*sum(lam**alpha))
                     for alpha in ORDERS], dtype=np.longdouble)

def pair_cov(lam, a, b):
    """Uncentered unordered-pair expression, independently of production centering."""
    lam = np.asarray(lam, dtype=np.longdouble)
    hp = h(lam)
    i, j = np.triu_indices(a, 1)
    dh = hp[:, i] - hp[:, j]
    return np.asarray((dh*(lam[i]*lam[j]))@dh.T *
                      (np.longdouble(2*a*b)/((a*a-1)*(b*b-1))), dtype=float)

def commutator_rates(psi, a, b):
    mat = psi.reshape(a,b)
    # The signs are produced directly from global basis bit positions.
    bit_a, bit_b = int(np.log2(b)), int(np.log2(b))-1
    idx = np.arange(a*b)
    signs = (1-2*((idx >> bit_a)&1))*(1-2*((idx >> bit_b)&1))
    hm = (signs*psi).reshape(a,b)
    drho = -1j*(hm@mat.conj().T - mat@hm.conj().T)
    # QR-iteration SVD driver differs from production divide-and-conquer driver.
    u, s, vh = sla.svd(mat, full_matrices=False, lapack_driver='gesvd')
    lam = s*s
    dl = np.einsum('ij,ji->i', u.conj().T@drho, u).real
    rates = np.asarray(h(lam), float)@dl
    return lam, rates, float(np.trace(drho).real), signs

def entropy_from_eigenvalues(lam):
    lam = np.asarray(lam, dtype=np.longdouble)
    return np.asarray([-sum(lam*np.log(lam)) if x == 1 else
                       np.log(sum(lam**x))/(1-x) for x in ORDERS], float)

def audit():
    output = {'method': 'Independent unordered-pair covariance, reduced-density commutator, and direct matrix exponential; no production import.'}
    checks = []
    rate_checks = []
    max_saved_cov = 0.
    max_norm_error = 0.
    min_sv_resolution_ratio = float('inf')
    min_probability = float('inf')
    observation_count = 0
    for path in sorted((ROOT/'results').glob('haar_d*.npz')):
        z = np.load(path)
        d, a, b = int(z['d']), int(z['a']), int(z['b'])
        spectra = z['spectra']
        observation_count += len(spectra)
        covariance_errors = []
        for k, lam in enumerate(spectra):
            cov = pair_cov(lam, a, b)
            scale = np.sqrt(np.outer(np.diag(cov), np.diag(cov)))
            covariance_errors.append(float(np.max(np.abs(cov-z['covariance'][k])/scale)))
        max_saved_cov = max(max_saved_cov, max(covariance_errors))
        max_norm_error = max(max_norm_error, float(np.max(np.abs(spectra.sum(axis=1)-1))))
        min_probability = min(min_probability, float(spectra.min()))
        ratio = np.sqrt(spectra[:,-1]/spectra[:,0])/np.finfo(float).eps
        min_sv_resolution_ratio = min(min_sv_resolution_ratio, float(ratio.min()))
        # Anchor plus worst small-eigenvalue observation, chosen for numerical risk.
        indices = sorted(set([0, int(np.argmin(spectra[:,-1]))]))
        for k in indices:
            psi = state(d,k)
            lam, rates, trace_error, signs = commutator_rates(psi,a,b)
            delta = rates-z['rates'][k]
            rms = np.sqrt(np.diag(z['covariance'][k]))
            rate_checks.append(dict(file=path.name,index=k,
                max_absolute_rate_error=float(np.max(abs(delta))),
                max_error_in_conditional_rms=float(np.max(abs(delta)/rms)),
                max_spectrum_absolute_error=float(np.max(abs(lam-spectra[k]))),
                derivative_trace_error=trace_error))
        checks.append(dict(file=path.name,samples=len(spectra),
                           max_covariance_error_in_rms_product=max(covariance_errors)))
    output['production_arrays'] = dict(observations=observation_count,files=checks,
        min_probability=min_probability,max_normalization_error=max_norm_error,
        minimum_smallest_sv_over_machine_epsilon_times_largest_sv=min_sv_resolution_ratio,
        max_covariance_error_in_rms_product=max_saved_cov)
    output['commutator_checks'] = rate_checks

    # A deterministic spherical two-design for each rotated Pauli. All 36
    # orientation pairs integrate the relevant second moment exactly for a=b=2.
    lam = np.array([.73,.27]); hp=np.asarray(h(lam),float)
    directions = np.concatenate([np.eye(3),-np.eye(3)])
    samples=[]
    for n in directions:
        for m in directions:
            imag=((n[0]-1j*n[1])*(m[0]-1j*m[1])).imag
            samples.append(2*np.sqrt(np.prod(lam))*(hp[:,0]-hp[:,1])*imag)
    samples=np.asarray(samples)
    empirical=samples.T@samples/len(samples)
    expected=pair_cov(lam,2,2)
    output['deterministic_pauli_orientation_design'] = dict(points=36,
        max_absolute_covariance_error=float(np.max(abs(empirical-expected))))

    orientation=[]
    for path in sorted((ROOT/'results').glob('orientation_*.npz')):
        z=np.load(path)
        import re
        a,b=map(int,re.search(r'a(\d+)_b(\d+)',path.name).groups())
        expected=pair_cov(z['spectrum'],a,b)
        rr=z['rates']; products=rr[:,:,None]*rr[:,None,:]
        empirical=products.mean(0)
        se=products.std(0,ddof=1)/np.sqrt(len(rr))
        orientation.append(dict(file=path.name,draws=len(rr),
            max_absolute_z=float(np.max(abs(empirical-expected)/se)),
            max_absolute_mean_in_standard_errors=float(np.max(abs(rr.mean(0))/(rr.std(0,ddof=1)/np.sqrt(len(rr))))),
            max_stored_covariance_difference=float(np.max(abs(expected-z['predicted'])))))
    output['saved_orientation_recheck']=orientation

    # Direct 64x64 matrix exponentials plus rho eigenvalues provide an
    # independent implementation of the finite pulse and entropy calculation.
    pulse=[]
    psi=state(8,0)
    for a,b,cut in [(8,8,'balanced'),(4,16,'shifted')]:
        lam,rates,_,signs=commutator_rates(psi,a,b)
        z=np.load(ROOT/'results'/f'haar_d8_{cut}.npz')
        hh=np.diag(signs.astype(float))
        base=entropy_from_eigenvalues(sla.eigvalsh(psi.reshape(a,b)@psi.reshape(a,b).conj().T))
        for index,t in enumerate(z['durations']):
            for sign_index,direction in enumerate([1,-1]):
                evolved=sla.expm(-1j*direction*t*hh)@psi
                mm=evolved.reshape(a,b)
                eig=sla.eigvalsh(mm@mm.conj().T)
                change=entropy_from_eigenvalues(eig)-base
                pulse.append(dict(a=a,b=b,duration=float(direction*t),
                    max_saved_entropy_change_error=float(np.max(abs(change-z['changes'][0,index,sign_index])))))
    output['direct_matrix_finite_pulses']=pulse
    output['interpretation'] = [
        'The conditional mean rate is exactly zero; empirical second moments are appropriate without subtracting estimated sample means.',
        'Fixed-spectrum orientation products have finite moments, so their reported conditional Monte Carlo standard errors are legitimate.',
        'Across random balanced spectra, fourth rate moments can fail for alpha<=1/4; ordinary unconditional sample-variance error bars would be unjustified.',
        'Finite-pulse entropy changes require no eigenvalue cutoffs. Dividing them by duration tests differentiability on the tested states and durations, not a uniform expansion over Haar states.',
        'Changing the cut also changes the physical ZZ bond. An aspect-ratio comparison is valid; a locality or statewise protection claim would not follow.',
        'The smallest sampled singular value is far above backward-error resolution; observed low-order statistics are not caused by clipped or numerically zero Schmidt probabilities.'
    ]
    output['provenance']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [ROOT/'run_experiment.py',ROOT/'PROTOCOL.md',Path(__file__)]}
    (ROOT/'audit05.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({
        'observations':observation_count,
        'max_covariance_error_in_rms_product':max_saved_cov,
        'max_commutator_rate_error':max(x['max_absolute_rate_error'] for x in rate_checks),
        'max_commutator_error_in_conditional_rms':max(x['max_error_in_conditional_rms'] for x in rate_checks),
        'minimum_sv_resolution_ratio':min_sv_resolution_ratio,
        'max_direct_pulse_entropy_change_error':max(x['max_saved_entropy_change_error'] for x in pulse),
        'orientation':orientation,
    },indent=2))

if __name__ == '__main__':
    audit()
