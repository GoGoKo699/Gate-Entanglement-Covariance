"""Two frozen Floquet eigenstate cohorts and independently fixed probe gates."""
import os
for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']:
    os.environ[key] = '1'
from pathlib import Path
import hashlib
import json
import time
import numpy as np
from scipy.linalg import schur
from scipy.special import digamma, polygamma

ROOT = Path(__file__).resolve().parent
ORDERS = [.5, 1., 2.]
GATE_NAMES = ['identity', 'SWAP', 'phaseSWAP']
SEED = 2026091209


def haar_gate(x):
    rng = np.random.default_rng(np.random.SeedSequence([SEED, x+100]))
    z = rng.normal(size=(4, 4)) + 1j*rng.normal(size=(4, 4))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r)/np.abs(np.diag(r)))[None, :]


def apply_gate(v, g, site, N):
    """Columns are states, sites are MSB-first; only adjacent sites used."""
    shape = v.shape
    a = v.reshape(2**site, 4, 2**(N-site-2), -1)
    return np.einsum('ij,ajbk->aibk', g, a, optimize=True).reshape(shape)


def operator_weights(g):
    r = g.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    return np.linalg.svd(r, compute_uv=False)**2/4


def probes():
    swap = np.eye(4)[[0, 2, 1, 3]].astype(complex)
    return [np.eye(4, dtype=complex), swap,
            swap @ np.diag(np.exp(-1j*np.pi/4*np.array([1., -1., -1., 1.])))]


def entropy_columns(v, d):
    out = np.zeros((v.shape[1], 3))
    purity = np.zeros(v.shape[1])
    pmin = np.zeros(v.shape[1])
    for j in range(v.shape[1]):
        s = np.linalg.svd(v[:, j].reshape(d, d), compute_uv=False)
        p = s*s
        # The eigensolver supplies normalized columns; no tail truncation.
        assert abs(p.sum()-1) < 2e-11
        purity[j] = np.dot(p, p)
        pmin[j] = p[-1]
        positive = p > 0
        out[j] = [2*np.log(s.sum()), -np.dot(p[positive], np.log(p[positive])), -np.log(purity[j])]
    return out, purity, pmin


def predictions():
    result = {'scope': 'Entropy covariance is limiting; purity and von Neumann marginal anchors are exact finite d.',
              'orders': ORDERS, 'gates': {}}
    k = np.arange(2, 65537, dtype=float)
    for name, gate in zip(GATE_NAMES, probes()):
        eta = operator_weights(gate)
        rows = []
        for alpha in ORDERS:
            if alpha == 1:
                c = 4*(-1.)**(k-1)/(k*(k*k-1))
            else:
                c = np.empty(len(k)); c[0] = -2*alpha/(alpha+2)
                c[1:] = c[0]*np.cumprod((alpha-k[:-1])/(alpha+k[:-1]+1))
            var = alpha/4  # Exact for the three selected orders.
            cov = float(.25*np.sum(k*c*c*np.sum(eta[:, None]**k[None, :], axis=0)))
            if name == 'identity':
                cov = var
            rows.append(dict(order=alpha, scaled_variance=var, scaled_covariance=cov,
                             correlation=cov/var, scaled_msd=2*(var-cov)))
        result['gates'][name] = dict(operator_weights=eta.tolist(), entropy=rows)
    result['finite'] = {}
    for N in [8, 10]:
        d = 2**(N//2); D = d*d
        varp = 2*(D-1)**2/((D+1)**2*(D+2)*(D+3))
        rows = {}
        swap = probes()[1]
        for name, g in zip(GATE_NAMES, probes()):
            f = np.sum(operator_weights(g)**2)
            h = np.sum(operator_weights(g@swap)**2)
            rho = ((D+1)*(D*f+4*h)-4*D)/(D-1)**2
            rows[name] = dict(correlation=float(rho), covariance=float(varp*rho), msd=float(2*varp*(1-rho)))
        result['finite'][str(N)] = dict(d=d, purity_mean=2*d/(D+1), purity_variance=varp,
              von_neumann_mean=float(digamma(D+1)-digamma(d+1)-(d-1)/(2*d)),
              von_neumann_variance=float(-polygamma(1,D+1)+2*d/(D+1)*polygamma(1,d)-(d+1)*(3*d+1)/(4*d*d*(D+1))),
              gates=rows)
    return result


def pair_stats(a, b):
    am, bm = float(a.mean()), float(b.mean())
    va, vb = float(np.mean((a-am)**2)), float(np.mean((b-bm)**2))
    cov = float(np.mean((a-am)*(b-bm)))
    return dict(mean_before=am, mean_after=bm, mean_shift=bm-am,
                variance_before=va, variance_after=vb, covariance=cov,
                correlation=cov/np.sqrt(va*vb), msd=float(np.mean((b-a)**2)),
                mean_shift_in_input_sd=(bm-am)/np.sqrt(va))


def summarize(N, entropy, purity, pred):
    d = 2**(N//2); result = {'entropy': {}, 'purity': {}}
    for gi, name in enumerate(GATE_NAMES):
        result['entropy'][name] = []
        for ai, alpha in enumerate(ORDERS):
            row = pair_stats(entropy[0, :, ai], entropy[gi, :, ai])
            p = pred['gates'][name]['entropy'][ai]
            row.update(order=alpha, scaled_covariance=d*d*row['covariance'],
                       variance_before_ratio=d*d*row['variance_before']/p['scaled_variance'],
                       variance_after_ratio=d*d*row['variance_after']/p['scaled_variance'],
                       correlation_residual=row['correlation']-p['correlation'])
            row['msd_ratio'] = d*d*row['msd']/p['scaled_msd'] if gi else None
            row['criteria'] = dict(input_scale=.75<=row['variance_before_ratio']<=1.25,
                 output_scale=.75<=row['variance_after_ratio']<=1.25,
                 correlation=abs(row['correlation_residual'])<=.10,
                 increment=True if gi==0 else .75<=row['msd_ratio']<=1.25,
                 mean_shift=abs(row['mean_shift_in_input_sd'])<=.25)
            row['within_declared_band'] = all(row['criteria'].values()) if gi else None
            if alpha == 1:
                row['exact_haar_variance_before_ratio'] = row['variance_before']/pred['finite'][str(N)]['von_neumann_variance']
                row['exact_haar_mean_difference'] = row['mean_before']-pred['finite'][str(N)]['von_neumann_mean']
            result['entropy'][name].append(row)
        row = pair_stats(purity[0], purity[gi])
        p = pred['finite'][str(N)]
        row.update(exact_haar_variance_before_ratio=row['variance_before']/p['purity_variance'],
                   exact_haar_variance_after_ratio=row['variance_after']/p['purity_variance'],
                   exact_haar_correlation_residual=row['correlation']-p['gates'][name]['correlation'])
        result['purity'][name] = row
    result['probe_pair_correlation_difference'] = [result['entropy']['SWAP'][a]['correlation']-result['entropy']['phaseSWAP'][a]['correlation'] for a in range(3)]
    return result


def run_size(N, pred):
    D = 2**N; d = 2**(N//2); start = time.monotonic()
    xs = list(range(-N//2, N//2-1))
    gates = {x:haar_gate(x) for x in xs}
    F = np.eye(D, dtype=complex)
    for parity in [1, 0]:
        for x in xs:
            if x % 2 == parity:
                F = apply_gate(F, gates[x], x+N//2, N)
    unitary_error = float(np.linalg.norm(F.conj().T@F-np.eye(D), 'fro')/np.sqrt(D))
    T, v = schur(F, output='complex', check_finite=False)
    eigenvalues = np.diag(T)
    idx = np.argsort(np.angle(eigenvalues)); eigenvalues=eigenvalues[idx]; v=v[:,idx]
    phase = np.angle(eigenvalues)
    diag = dict(unitarity_frobenius_relative=unitary_error,
                eigen_residual_max=float(np.max(np.linalg.norm(F@v-v*eigenvalues[None,:], axis=0))),
                orthogonality_max_entry=float(np.max(abs(v.conj().T@v-np.eye(D)))),
                eigenvalue_modulus_max_error=float(np.max(abs(abs(eigenvalues)-1))),
                schur_off_diagonal_frobenius=float(np.linalg.norm(T-np.diag(np.diag(T)))))
    gaps = np.diff(np.r_[phase, phase[0]+2*np.pi])
    ratios = np.minimum(gaps,np.roll(gaps,-1))/np.maximum(gaps,np.roll(gaps,-1))
    diag.update(minimum_eigenphase_gap=float(gaps.min()),mean_circular_gap_ratio=float(ratios.mean()),
                scaled_computational_ipr=float(D*np.mean(np.sum(abs(v)**4,axis=0))))
    states = np.arange(D)
    signs = np.array([[1-2*((j>>(N-1-s))&1) for j in states] for s in range(N)])
    charge = signs.sum(axis=0); parity = signs.prod(axis=0)
    reverse = np.array([int(format(j,f'0{N}b')[::-1],2) for j in states])
    diag['symmetry_commutator_relative'] = dict(
       total_Z=float(np.linalg.norm((charge[:,None]-charge[None,:])*F)/np.linalg.norm(charge)),
       Z_parity=float(np.linalg.norm((parity[:,None]-parity[None,:])*F)/np.sqrt(D)),
       X_flip=float(np.linalg.norm(F[::-1,:]-F[:,::-1])/np.sqrt(D)),
       reflection=float(np.linalg.norm(F[reverse,:]-F[:,reverse])/np.sqrt(D)))
    assert diag['eigen_residual_max']<1e-10 and diag['orthogonality_max_entry']<1e-10
    assert diag['minimum_eigenphase_gap']>1e-10
    entropy=[]; purity=[]; pmin=[]
    for name, g in zip(GATE_NAMES,probes()):
        after=v if name=='identity' else apply_gate(v,g,N//2-1,N)
        e,p,m=entropy_columns(after,d);entropy.append(e);purity.append(p);pmin.append(m)
    entropy=np.array(entropy);purity=np.array(purity);pmin=np.array(pmin)
    anchor_idx=np.linspace(0,D-1,16,dtype=int)
    eg,pg,_=entropy_columns(apply_gate(v[:,anchor_idx],gates[-1],N//2-1,N),d)
    diag['own_crossing_gate_anchor'] = dict(indices=anchor_idx.tolist(),
            maximum_entropy_change=float(np.max(abs(eg-entropy[0,anchor_idx]))),
            maximum_purity_change=float(np.max(abs(pg-purity[0,anchor_idx]))))
    for x in xs:
        eta=operator_weights(gates[x])
        diag.setdefault('bond_operator_purities',{})[str(x)] = float(np.sum(eta**2))
    out=summarize(N,entropy,purity,pred)
    out.update(N=N,half_dimension=d,cohort_count=D,diagnostics=diag,
               minimum_schmidt_probability=float(pmin.min()),elapsed_seconds=time.monotonic()-start,
               protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
               predictions_sha256=hashlib.sha256((ROOT/'results/predictions.json').read_bytes()).hexdigest(),
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    np.savez_compressed(ROOT/f'results/cohort_N{N}.npz', eigenvectors=v,eigenvalues=eigenvalues,
         bond_coordinates=np.array(xs),bond_gates=np.array([gates[x] for x in xs]),
         probe_gates=np.array(probes()),entropies=entropy,purities=purity,minimum_schmidt_probabilities=pmin,
         gap_ratios=ratios)
    (ROOT/f'results/summary_N{N}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'N':N,'seconds':out['elapsed_seconds'],'gap_ratio':diag['mean_circular_gap_ratio'],
       'central_gate_operator_purity':diag['bond_operator_purities']['-1'],
       'S1_variance_ratio_exact':out['entropy']['identity'][1]['exact_haar_variance_before_ratio'],
       'S1_mean_Page_difference':out['entropy']['identity'][1]['exact_haar_mean_difference'],
       'correlations':{name:[x['correlation'] for x in out['entropy'][name]] for name in GATE_NAMES},
       'own_crossing_gate_anchor':diag['own_crossing_gate_anchor']},indent=2),flush=True)
    return out


def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--predict-only',action='store_true')
    args=parser.parse_args()
    (ROOT/'results').mkdir(exist_ok=True)
    pred=predictions();path=ROOT/'results/predictions.json'
    serialized=json.dumps(pred,indent=2)+'\n'
    if path.exists():
        assert json.loads(path.read_text())==pred, 'Frozen prediction differs. Retain original and investigate.'
    else:
        path.write_text(serialized)
    if args.predict_only:
        print(serialized);return
    for N in [8,10]:run_size(N,pred)


if __name__=='__main__':main()
