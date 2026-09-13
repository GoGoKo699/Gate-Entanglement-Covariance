"""One bounded matched-interaction test; see OPERATOR_PLAN.md."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import hashlib,json
from pathlib import Path
import numpy as np
import scipy.linalg as la
from run_experiment import ORDERS,entropy
from finite_time_followup import coefficients

ROOT=Path(__file__).resolve().parent
HA=np.outer([1,-1,1,-1],[1,1,-1,-1])
HB=np.array([[1,1,-1,-1],[1,-1,-1,1],[-1,-1,1,1],[-1,1,1,-1]])
TIMES=np.array([np.pi/4,np.pi/2])
ETAS={'A':[[.5,.5],[1.]],'B':[[.5,.25,.25],[.5,.5]]}

def increment_prediction(eta,K=32768):
    """Declared finite-pulse spectra; exact identity or exponentially small tail kernel."""
    eta=np.asarray(eta,dtype=float)
    if np.any(eta<0) or not np.isclose(eta.sum(),1,rtol=0,atol=1e-14):
        raise ValueError('Expected normalized nonnegative operator Schmidt weights.')
    if len(eta)==1 and eta[0]==1: return np.zeros(len(ORDERS))
    if eta.max()**K>1e-14:
        raise ValueError('This finite-pulse tail approximation needs a larger cutoff for these weights.')
    values=[]
    for alpha in ORDERS:
        k,c,tail=coefficients(float(alpha),K)
        F=np.sum(eta[:,None]**k[None,:],axis=0)
        values.append(.5*np.sum(k*c*c*(1-F))+tail)
    return np.array(values)

def check_interactions():
    out={}
    for name,h in [('A',HA),('B',HB)]:
        centered=h-h.mean(axis=0)[None,:]-h.mean(axis=1)[:,None]+h.mean()
        errors=[]
        for j,t in enumerate(TIMES):
            eta=la.svdvals(np.exp(-1j*t*h)/4)**2
            target=np.pad(np.array(ETAS[name][j]),(0,4-len(ETAS[name][j])))
            errors.append(float(np.max(np.abs(np.sort(eta)-np.sort(target)))))
        out[name]=dict(plus=int(np.sum(h==1)),minus=int(np.sum(h==-1)),
            operator_norm=int(np.max(np.abs(h))),chi=float(np.mean(centered**2)),
            max_operator_spectrum_error=max(errors))
    assert out['A']['chi']==out['B']['chi']==1
    assert max(x['max_operator_spectrum_error'] for x in out.values())<1e-13
    return out

if __name__=='__main__':
    out=ROOT/'operator_results';out.mkdir(exist_ok=True)
    predictions={name:np.array([increment_prediction(eta) for eta in ETAS[name]]) for name in ETAS}
    frozen=dict(times=TIMES.tolist(),orders=ORDERS.tolist(),operator_weights=ETAS,
        predictions={name:v.tolist() for name,v in predictions.items()},
        interactions=check_interactions(),
        plan_sha256=hashlib.sha256((ROOT/'OPERATOR_PLAN.md').read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'frozen_prediction.json').write_text(json.dumps(frozen,indent=2)+'\n')
    print('Operator-memory predictions frozen before new states.',flush=True)
    rows=[]
    for d in [64,128]:
        spectra=[];changes=[]
        ia=np.arange(d)%4;ib=np.arange(d)//(d//4)
        patterns=[h[ia[:,None],ib[None,:]] for h in [HA,HB]]
        for j in range(64):
            rng=np.random.default_rng(np.random.SeedSequence([90612026,d,j]))
            mat=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));mat/=la.norm(mat)
            lam=la.svdvals(mat)**2;e=entropy(lam);spectra.append(lam)
            changes.append([[entropy(la.svdvals(np.exp(-1j*t*pattern)*mat)**2)-e for t in TIMES] for pattern in patterns])
        changes=np.array(changes)
        np.savez_compressed(out/f'matched_d{d}.npz',d=d,orders=ORDERS,times=TIMES,
                            spectra=spectra,changes=changes,HA=HA,HB=HB)
        yy=d*d*changes**2
        mean=yy.mean(axis=0);se=yy.std(axis=0,ddof=1)/8
        contrast=yy[:,1]-yy[:,0]
        row=dict(d=d,states=64,mean=mean.tolist(),standard_error=se.tolist(),
            paired_B_minus_A_mean=contrast.mean(axis=0).tolist(),
            paired_B_minus_A_standard_error=(contrast.std(axis=0,ddof=1)/8).tolist(),
            max_A_recurrence_entropy_error=float(np.abs(changes[:,0,1]).max()))
        rows.append(row);print(json.dumps(row),flush=True)
    (out/'summary.json').write_text(json.dumps(dict(frozen=frozen,rows=rows),indent=2)+'\n')
