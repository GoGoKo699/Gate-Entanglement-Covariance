"""Protocol-fixed, small non-diagonal-gate entropy illustration."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
import json,hashlib
import numpy as np
import scipy.linalg as la
from exact_purity import gates,operator_weights

ROOT=Path(__file__).resolve().parents[1]
ORDERS=np.array([.5,1.,2.])
SIZES=[32,64]
NSTATES=96
SEED=90712026

def coefficients(alpha,K=65536):
    k=np.arange(2,K+1,dtype=float)
    if alpha==1: return k,4*(-1.)**(k-1)/(k*(k*k-1))
    # Gamma-free recurrence, also valid at the positive integers.
    c=np.empty(len(k));c[0]=-2*alpha/(alpha+2)
    c[1:]=c[0]*np.cumprod((alpha-k[:-1])/(alpha+k[:-1]+1))
    return k,c

def prediction(eta):
    cov=[];var=[];increment=[]
    for a in ORDERS:
        k,c=coefficients(a)
        f=np.sum(eta[:,None]**k[None,:],axis=0)
        C=.25*np.sum(k*c*c*f);V=.25*np.sum(k*c*c)
        cov.append(C);var.append(V);increment.append(2*(V-C))
    return dict(covariance=cov,static_variance=var,increments=increment)

def entropy(lam):
    lam=np.maximum(lam,0)
    pos=lam[lam>0]
    return np.array([2*np.log(np.sum(np.sqrt(pos))),-np.dot(pos,np.log(pos)),-np.log(np.sum(pos**2))])

def apply(U,M):
    d=len(M);m=d//2
    return np.einsum('acbd,bidj->aicj',U.reshape(2,2,2,2),M.reshape(2,m,2,m)).reshape(d,d)

def dense_full(U,d):
    m=d//2
    # Independent explicit embedding in |a,i,b,j> order.
    full=np.zeros((d*d,d*d),complex)
    for a in range(2):
      for b in range(2):
       for c in range(2):
        for e in range(2):
         for i in range(m):
          for j in range(m):
           full[(a*m+i)*d+b*m+j,(c*m+i)*d+e*m+j]=U[2*a+b,2*c+e]
    return full

def main():
    out=ROOT/'results';out.mkdir(exist_ok=True)
    gs={k:v for k,v in gates().items() if k in ['SWAP','Cartan']}
    eta={k:operator_weights(v) for k,v in gs.items()}
    frozen=dict(sizes=SIZES,states_per_size=NSTATES,seed=SEED,orders=ORDERS.tolist(),gates=list(gs),
                weights={k:v.tolist() for k,v in eta.items()},predictions={k:prediction(v) for k,v in eta.items()},
                protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'pilot_frozen.json').write_text(json.dumps(frozen,indent=2)+'\n')
    print('Predictions saved before sampling.',flush=True)
    summaries=[]
    for d in SIZES:
        base=[];deltas=[];purities=[];anchors=[]
        for j in range(NSTATES):
            rng=np.random.default_rng(np.random.SeedSequence([SEED,d,j]))
            M=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));M/=la.norm(M)
            l0=la.svdvals(M)**2;e0=entropy(l0)
            es=[];ps=[]
            for name,U in gs.items():
                Mt=apply(U,M);lam=la.svdvals(Mt)**2
                es.append(entropy(lam)-e0);ps.append(float(np.sum(lam**2)))
                if j==0:
                    dense=dense_full(U,d)@M.ravel()
                    anchors.append(dict(gate=name,state_error=float(la.norm(dense-Mt.ravel())),
                           spectrum_error=float(np.max(np.abs(np.sort(la.eigvalsh(Mt@Mt.conj().T))-np.sort(lam))))))
            base.append(e0);deltas.append(es);purities.append([float(np.sum(l0**2)),*ps])
        base=np.array(base);deltas=np.array(deltas);purities=np.array(purities)
        np.savez_compressed(out/f'pilot_d{d}.npz',orders=ORDERS,base=base,deltas=deltas,purities=purities)
        values=d*d*deltas**2
        summaries.append(dict(d=d,states=NSTATES,mean=values.mean(axis=0).tolist(),
                         sample_standard_error=(values.std(axis=0,ddof=1)/np.sqrt(NSTATES)).tolist(),
                         anchors=anchors))
        print(json.dumps(summaries[-1]),flush=True)
    assert max(a['state_error'] for row in summaries for a in row['anchors'])<1e-12
    result=dict(frozen=frozen,rows=summaries,
      limitations='Small illustration, not a fitted convergence study. Same states are reused across orders and gates. Sample SEs exclude finite-d bias; standardized differences are not calibrated tests. No samples are added based on agreement.')
    (out/'pilot_summary.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
