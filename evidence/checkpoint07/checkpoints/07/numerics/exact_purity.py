"""Independent finite-d Haar calculation using the exact four-copy moment.

No Gaussian Wick contractions and no random-state sampling are used here.
The 24 permutation terms factor between fixed active factors and spectators.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
from itertools import permutations
import json
import numpy as np
import scipy.linalg as la
from decimal import Decimal, getcontext

ROOT=Path(__file__).resolve().parents[1]

def cycles(p):
    seen=set(); n=0
    for i in range(len(p)):
        if i in seen: continue
        n+=1
        while i not in seen: seen.add(i); i=p[i]
    return n

def gates():
    X=np.array([[0,1],[1,0]],complex)
    Y=np.array([[0,-1j],[1j,0]],complex)
    Z=np.diag([1.,-1.])
    swap=np.eye(4)[[0,2,1,3]]
    return {'identity':np.eye(4), 'ZZ':la.expm(-.37j*np.kron(Z,Z)),
            'phaseSWAP':swap@la.expm(-.25j*np.pi*np.kron(Z,Z)),
            'SWAP':swap, 'Cartan':la.expm(-1j*(.37*np.kron(X,X)+.23*np.kron(Y,Y)+.11*np.kron(Z,Z)))}

def operator_weights(U,r=2,s=2):
    return la.svdvals(U.reshape(r,s,r,s).transpose(0,2,1,3).reshape(r*r,s*s))**2/(r*s)

def active_terms(U,r=2,s=2):
    b=r*s
    # Swap active A between two copies, leaving each active B in place.
    pair=np.arange(b*b).reshape(b,b)
    sw=np.zeros((b*b,b*b),complex)
    for x in range(b):
        for y in range(b):
            a,bb=divmod(x,s); c,dd=divmod(y,s)
            sw[pair[c*s+bb,a*s+dd],pair[x,y]]=1
    uu=np.kron(U,U)
    K=np.kron(sw,uu.conj().T@sw@uu)
    digits=np.indices((b,)*4).reshape(4,-1).T
    rows=np.arange(b**4)
    tau=[1,0,3,2]
    terms=[]
    for p in permutations(range(4)):
        inv=np.argsort(p)
        cols=np.ravel_multi_index(digits[:,inv].T,(b,)*4)
        z=np.sum(K[rows,cols])
        nr=cycles([tau[p[i]] for i in range(4)])
        nc=cycles(p)
        terms.append(dict(permutation=p,nr=nr,nc=nc,active_real=float(z.real),active_imag=float(z.imag)))
    return terms

def exact_covariance(terms,d,r=2,s=2):
    getcontext().prec=60
    D=Decimal(d)**2
    num=sum(Decimal(str(t['active_real']))*(Decimal(d)/r)**t['nr']*(Decimal(d)/s)**t['nc'] for t in terms)
    moment=num/(D*(D+1)*(D+2)*(D+3))
    mean=2*Decimal(d)/(D+1)
    cov=moment-mean**2
    var=2*(D-1)**2/((D+1)**2*(D+2)*(D+3))
    return dict(d=d,purity_product_moment=float(moment),purity_covariance=float(cov),
                purity_correlation=float(cov/var),renyi2_delta_method_scaled_covariance=float(d**4*cov/4))

def main():
    out={}
    for name,U in gates().items():
        ts=active_terms(U)
        eta=operator_weights(U)
        rows=[exact_covariance(ts,d) for d in [2,4,8,16,32,64,128,256,1024]]
        out[name]=dict(operator_weights=eta.tolist(),predicted_limiting_purity_correlation=float(np.sum(eta**2)),
                       terms=ts,rows=rows)
    assert max(abs(x['purity_correlation']-1) for x in out['identity']['rows'])<1e-12
    assert abs(out['SWAP']['rows'][0]['purity_correlation']-1)<1e-12
    assert max(abs(x['purity_correlation']-(x['d']**4+x['d']**2+16)/(4*(x['d']**2-1)**2)) for x in out['SWAP']['rows'])<1e-12
    assert abs(out['SWAP']['rows'][-1]['purity_correlation']-.25)<1e-5
    assert max(abs(x['active_imag']) for v in out.values() for x in v['terms'])<1e-12
    payload=dict(method='Exact complex-Haar four-copy moment, 24 permutations; active traces in floating point and scalar sums at 60 decimal digits.',
                 limitation='The purity covariance is exact up to floating-point active traces. The Renyi-2 delta-method column is an asymptotic transformation, not the exact finite-d logarithmic entropy covariance.',results=out)
    (ROOT/'results').mkdir(exist_ok=True)
    (ROOT/'results'/'exact_purity.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:[(x['d'],x['purity_correlation']) for x in v['rows']] for k,v in out.items()},indent=2))

if __name__=='__main__': main()
