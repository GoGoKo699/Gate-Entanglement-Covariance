"""Separately frozen fresh-state test; see FOLLOWUP_PLAN.md."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import hashlib,json
import numpy as np
import scipy.linalg as la
from scipy.special import gamma,zeta
from run_experiment import ORDERS, entropy, pulsed_entropy

ROOT=Path(__file__).resolve().parent
TIMES=np.array([.1,.2,.4])

def coefficients(alpha,K):
    k=np.arange(2,K+1,dtype=float)
    if alpha==1:
        return k,4*(-1.)**(k-1)/(k*(k*k-1)),0.
    moment=4**alpha*gamma(alpha+.5)/(np.sqrt(np.pi)*gamma(alpha+2))
    first=2*gamma(2*alpha+1)/(gamma(alpha+3)*gamma(alpha-1)*(1-alpha)*moment)
    c=np.empty(len(k));c[0]=first
    c[1:]=first*np.cumprod((alpha-k[:-1])/(alpha+k[:-1]+1))
    amplitude=2*gamma(2*alpha+1)*np.sin(np.pi*alpha)/(np.pi*(1-alpha)*moment)
    tail=.5*amplitude**2*zeta(4*alpha+1,K+1)
    return k,c,tail

def prediction(times,K=32768):
    pred=np.empty((len(times),len(ORDERS)))
    for j,alpha in enumerate(ORDERS):
        k,c,tail=coefficients(float(alpha),K)
        for l,t in enumerate(times):
            pred[l,j]=.5*np.sum(k*c*c*(1-np.cos(t)**(2*k)-np.sin(t)**(2*k)))+tail
    return pred

if __name__=='__main__':
    out=ROOT/'followup_results';out.mkdir(exist_ok=True)
    pred=prediction(TIMES)
    frozen=dict(orders=ORDERS.tolist(),times=TIMES.tolist(),prediction=pred.tolist(),
        meaning='Candidate large-d limit of D E[(Delta S)^2], exact fixed-polynomial kernel; nonanalytic extension unresolved.',
        plan_sha256=hashlib.sha256((ROOT/'FOLLOWUP_PLAN.md').read_bytes()).hexdigest(),
        implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        doubled_series_cutoff_difference=float(np.max(np.abs(pred-prediction(TIMES,65536)))))
    (out/'frozen_prediction.json').write_text(json.dumps(frozen,indent=2)+'\n')
    print('Prediction frozen before generating new states.',flush=True)
    rows=[]
    for d in [128,256]:
        spectra=[];base=[];changes=[]
        for j in range(128):
            rng=np.random.default_rng(np.random.SeedSequence([90512506,d,j]))
            psi=rng.normal(size=d*d)+1j*rng.normal(size=d*d);psi/=la.norm(psi)
            lam=la.svdvals(psi.reshape(d,d))**2;e=entropy(lam)
            spectra.append(lam);base.append(e)
            changes.append([[pulsed_entropy(psi,d,d,t)-e,pulsed_entropy(psi,d,d,-t)-e] for t in TIMES])
        changes=np.array(changes)
        np.savez_compressed(out/f'fresh_d{d}.npz',d=d,orders=ORDERS,times=TIMES,
                            spectra=spectra,initial_entropies=base,changes=changes)
        perstate=d*d*np.mean(changes**2,axis=2)
        mean=perstate.mean(axis=0);se=perstate.std(axis=0,ddof=1)/np.sqrt(len(perstate))
        row=dict(d=d,states=len(perstate),mean=mean.tolist(),standard_error=se.tolist(),
                 standardized_difference=((mean-pred)/se).tolist())
        rows.append(row)
        print(json.dumps(row),flush=True)
    (out/'summary.json').write_text(json.dumps(dict(frozen=frozen,rows=rows),indent=2)+'\n')
