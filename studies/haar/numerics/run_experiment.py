"""Standalone bounded Haar entropy-response experiment. See PROTOCOL.md."""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(name, "1")
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import scipy.linalg as la

ORDERS = np.array([0.125, 0.25, 0.5, 1.0, 2.0])
SIZES = [8, 16, 32, 64, 128]
ROOT = Path(__file__).resolve().parent

def haar_state(d, sample):
    rng = np.random.default_rng(np.random.SeedSequence([90512026, d, sample]))
    psi = rng.normal(size=d*d) + 1j*rng.normal(size=d*d)
    return psi / la.norm(psi)

def zz(a, b):
    za = 1 - 2*(np.arange(a) % 2)
    zb = 1 - 2*(np.arange(b) // (b//2))
    return za[:, None]*zb[None, :]

def entropy(lam):
    return np.array([-np.dot(lam, np.log(lam)) if x == 1 else
                     np.log(np.sum(lam**x))/(1-x) for x in ORDERS])

def weights(lam):
    w = np.array([-np.log(lam) if x == 1 else
                  x/(1-x)*lam**(x-1)/np.sum(lam**x) for x in ORDERS])
    return w - (w@lam)[:, None]

def conditional_covariance(lam, a, b):
    w = weights(lam)
    return 2*a*b/((a*a-1)*(b*b-1)) * (w*lam)@w.T

def observe(psi, a, b):
    mat = psi.reshape(a,b)
    u,s,vh = la.svd(mat, full_matrices=False, lapack_driver="gesdd")
    lam = s*s
    dmat = -1j*zz(a,b)*mat
    ds = np.einsum('ik,ij,kj->k', u.conj(), dmat, vh.conj(), optimize=True).real
    dl = 2*s*ds
    return lam, weights(lam)@dl, conditional_covariance(lam,a,b), float(dl.sum())

def pulsed_entropy(psi, a, b, t):
    mat = psi.reshape(a,b)
    changed = np.cos(t)*mat - 1j*np.sin(t)*zz(a,b)*mat
    s = la.svdvals(changed)
    return entropy(s*s)

def run_main(out):
    for d in SIZES:
        for cut, a,b in [('balanced',d,d), ('shifted',d//2,2*d)]:
            spectra, rates, covs, trace_errors, changes = [],[],[],[],[]
            durations = np.array([.02,.1,.1/np.sqrt(d),.5/np.sqrt(d)])
            for j in range(256):
                psi = haar_state(d,j)
                lam,rate,cov,err = observe(psi,a,b)
                spectra.append(lam); rates.append(rate); covs.append(cov); trace_errors.append(err)
                if j < 64:
                    e = entropy(lam)
                    changes.append([[pulsed_entropy(psi,a,b,t)-e,
                                     pulsed_entropy(psi,a,b,-t)-e] for t in durations])
            np.savez_compressed(out/f'haar_d{d}_{cut}.npz', d=d,a=a,b=b,
                orders=ORDERS, spectra=spectra, rates=rates, covariance=covs,
                trace_errors=trace_errors, durations=durations, changes=changes)
            print(f'completed d={d} {cut}', flush=True)
        np.savez_compressed(out/f'anchor_d{d}.npz', psi=haar_state(d,0))

def random_unitary(rng, d):
    q,r = la.qr(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))
    ph = np.diag(r); ph = ph/np.abs(ph)
    return q*ph[None,:]

def validate(out):
    rng = np.random.default_rng(90512999)
    results = []
    for a,b in [(8,8),(4,16)]:
        mat = rng.normal(size=(a,b))+1j*rng.normal(size=(a,b))
        s=la.svdvals(mat); s=s/la.norm(s); lam=s*s
        w=weights(lam); pred=conditional_covariance(lam,a,b)
        samples=[]; direct_errors=[]
        for j in range(4000):
            u=random_unitary(rng,a); v=random_unitary(rng,b)
            za=1-2*(np.arange(a)%2); zb=1-2*(np.arange(b)//(b//2))
            aa=u.conj().T@(za[:,None]*u)
            bb=v.conj().T@(zb[:,None]*v)
            # Independent Schmidt-basis response, no SVD of the new state.
            dl=2*s*np.imag((aa[:a,:a]*bb[:a,:a])@s)
            rr=w@dl; samples.append(rr)
            if j < 16:
                psi=((u*s[None,:])@v[:,:a].T).ravel()
                direct_errors.append(float(np.max(np.abs(observe(psi,a,b)[1]-rr))))
        samples=np.asarray(samples)
        products=samples[:,:,None]*samples[:,None,:]
        empirical=products.mean(axis=0)
        se=products.std(axis=0,ddof=1)/np.sqrt(len(samples))
        z=(empirical-pred)/se
        result=dict(a=a,b=b,draws=len(samples),max_absolute_z=float(np.abs(z).max()),
                    max_direct_rate_error=max(direct_errors))
        results.append(result)
        np.savez_compressed(out/f'orientation_a{a}_b{b}.npz', spectrum=lam,
                            rates=samples,predicted=pred,empirical=empirical,se=se,z=z)
    fd=[]
    for d in SIZES:
        psi=haar_state(d,0)
        for a,b in [(d,d),(d//2,2*d)]:
            lam,r,c,e=observe(psi,a,b)
            for dt in [1e-4,1e-5,1e-6]:
                estimate=(pulsed_entropy(psi,a,b,dt)-pulsed_entropy(psi,a,b,-dt))/(2*dt)
                fd.append(dict(d=d,a=a,b=b,dt=dt,min_schmidt_probability=float(lam.min()),
                    rates=r.tolist(),finite_difference=estimate.tolist(),
                    max_absolute_error=float(np.max(np.abs(estimate-r)))))
    report=dict(orientation=results,finite_differences=fd)
    (out/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(orientation=results,finite_difference_max_error={
        str(dt):max(row['max_absolute_error'] for row in fd if row['dt']==dt)
        for dt in [1e-4,1e-5,1e-6]})),flush=True)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=ROOT/'results')
    parser.add_argument('--validation-only',action='store_true')
    args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    versions={'numpy':np.__version__,'scipy':__import__('scipy').__version__,
      'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
      'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (args.output/'provenance.json').write_text(json.dumps(versions,indent=2)+'\n')
    if not args.validation_only: run_main(args.output)
    validate(args.output)
