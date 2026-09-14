"""Independent direct Haar moments for two-cut purity memory.

This script contracts the sum/difference observables directly. It does not
import checkpoint-07 code or use a sum of precomputed one-cut correlations.
The entangling power comparator uses the product-input second moment directly.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from itertools import permutations
from decimal import Decimal, getcontext
import json,hashlib
import numpy as np
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parents[1]

def cycles(p):
    seen=set();count=0
    for i in range(len(p)):
        if i in seen: continue
        count+=1
        while i not in seen: seen.add(i);i=p[i]
    return count

def swaps(q):
    b=q*q
    sa=np.zeros((b*b,b*b),complex);sb=sa.copy()
    for x in range(b):
      for y in range(b):
        a,bb=divmod(x,q);c,e=divmod(y,q)
        sa[(c*q+bb)*b+(a*q+e),x*b+y]=1
        sb[(a*q+e)*b+(c*q+bb),x*b+y]=1
    return sa,sb

def product_entangling_power(U,q):
    sa,sb=swaps(q);b=q*q
    moment=(np.eye(b*b)+sa)@(np.eye(b*b)+sb)/(q*q*(q+1)**2)
    uu=np.kron(U,U)
    return float((1-np.trace(uu@moment@uu.conj().T@sa)).real)

def realignment_purity(U,q):
    z=U.reshape(q,q,q,q).transpose(0,2,1,3).reshape(q*q,q*q)
    return float(np.trace((z@z.conj().T)@(z@z.conj().T)).real/q**4)

def exact_terms(U,q,sign=1):
    b=q*q;sa,sb=swaps(q);left=sa+sign*sb
    uu=np.kron(U,U);right=uu.conj().T@left@uu
    digits=np.indices((b,)*4).reshape(4,-1).T
    i0=digits[:,0]*b+digits[:,1];i1=digits[:,2]*b+digits[:,3]
    tau=[1,0,3,2];terms=[]
    for p in permutations(range(4)):
        cols=digits[:,np.argsort(p)]
        z=np.sum(left[i0,cols[:,0]*b+cols[:,1]]*right[i1,cols[:,2]*b+cols[:,3]])
        terms.append(dict(permutation=list(p),nr=cycles([tau[p[i]] for i in range(4)]),
                          nc=cycles(p),active_real=float(z.real),active_imag=float(z.imag)))
    return terms

def centered_moment(terms,d,q,sign=1):
    getcontext().prec=60;D=Decimal(d*d);n=Decimal(d)/q
    raw=sum(Decimal(str(t['active_real']))*n**(t['nr']+t['nc']) for t in terms)/(D*(D+1)*(D+2)*(D+3))
    mean=Decimal((1+sign)*2*d)/(D+1)
    return raw-mean*mean

def coefficient(q,d):
    D=d*d
    return (q+1)**2*(D+1)*(D+q*q)/((q*q+1)*D*D+(q**4+1-6*q*q)*D+q*q+q**4)

def gate_examples(q):
    b=q*q;S=np.eye(b).reshape(q,q,q,q).transpose(1,0,2,3).reshape(b,b)
    phase=np.exp(-1j*.37*np.outer(np.arange(q),np.arange(q))).ravel()
    rng=np.random.default_rng(908001+q)
    z=rng.normal(size=(b,b))+1j*rng.normal(size=(b,b));u,_=np.linalg.qr(z)
    yield 'identity',np.eye(b)
    yield 'SWAP',S
    yield 'phaseSWAP',S@np.diag(phase)
    yield 'generic_QR',u
    if q==2:
        Z=np.diag([1.,-1.]);X=np.array([[0,1],[1,0.]])
        yield 'phaseSWAP_pi8',S@expm(-1j*np.pi/8*np.kron(Z,Z))
        yield 'phaseSWAP_pi4',S@expm(-1j*np.pi/4*np.kron(Z,Z))
        yield 'XX_0.29',expm(-.29j*np.kron(X,X))

def explicit_cut_identity():
    q=2;n=3;d=q*n
    # A single deterministic complex vector; no random-state ensemble.
    idx=np.arange(d*d)
    state=(np.sin(.17+idx*.23)+1j*np.cos(.41+idx*.19)).reshape(q,n,q,n)
    state/=np.linalg.norm(state)
    errors=[]
    S=dict(gate_examples(2))['SWAP']
    for name,U in gate_examples(2):
        after=np.einsum('acbd,bidj->aicj',U.reshape(2,2,2,2),state)
        transformed=np.einsum('acbd,bidj->aicj',(S@U).reshape(2,2,2,2),state)
        crossed=after.transpose(2,1,0,3).reshape(d,d)
        lam1=np.linalg.svd(crossed,compute_uv=False)**2
        lam2=np.linalg.svd(transformed.reshape(d,d),compute_uv=False)**2
        errors.append(float(np.max(abs(lam1-lam2))))
    swapped=np.einsum('acbd,bidj->aicj',S.reshape(2,2,2,2),state)
    def entropy2_sum(v):
        a=v.reshape(d,d);c=v.transpose(2,1,0,3).reshape(d,d)
        return -np.log(np.sum(np.linalg.svd(a,compute_uv=False)**4))-np.log(np.sum(np.linalg.svd(c,compute_uv=False)**4))
    return dict(maximum_crossed_cut_spectrum_error=max(errors),swap_entropy_sum_error=float(abs(entropy2_sum(state)-entropy2_sum(swapped))))

def main():
    payload={'method':'Direct four-copy Haar contraction of purity sum and direct second-moment product-input entangling power. No fitted or sampled Haar moments.',
       'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'results':[]}
    for q in [2,3,4]:
      baseterms=exact_terms(np.eye(q*q),q)
      S=dict(gate_examples(q))['SWAP']
      for name,U in gate_examples(q):
        terms=exact_terms(U,q);ep=product_entangling_power(U,q)
        a=realignment_purity(U,q);b=realignment_purity(S@U,q)
        ep_invariants=q*q/(q+1)**2*(1+1/(q*q)-a-b)
        rows=[]
        for n in [1,2,4,8,16]:
            d=q*n
            var=centered_moment(baseterms,d,q);cov=centered_moment(terms,d,q)
            rho=float(cov/var);pred=1-coefficient(q,d)*ep
            rows.append(dict(d=d,spectator_dimension=n,correlation_direct=rho,correlation_prediction=pred,error=abs(rho-pred)))
        payload['results'].append(dict(q=q,gate=name,entangling_power_direct=ep,operator_purity=a,crossed_operator_purity=b,
              ep_invariant_error=abs(ep-ep_invariants),terms=terms,rows=rows))
    payload['cut_identity']=explicit_cut_identity()
    payload['maximum_correlation_error']=max(row['error'] for x in payload['results'] for row in x['rows'])
    payload['maximum_ep_invariant_error']=max(x['ep_invariant_error'] for x in payload['results'])
    payload['status']='passed' if payload['maximum_correlation_error']<1e-9 and payload['maximum_ep_invariant_error']<1e-12 and payload['cut_identity']['maximum_crossed_cut_spectrum_error']<1e-12 else 'failed'
    (ROOT/'results').mkdir(exist_ok=True)
    (ROOT/'results/two_cut_check.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k!='results'},indent=2))
    if payload['status']!='passed':raise RuntimeError('Retained mismatch; do not promote claim.')

if __name__=='__main__': main()
