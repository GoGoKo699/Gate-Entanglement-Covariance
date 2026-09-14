"""Exact fourth Haar moment checks with no random-state sampling.

The direct contraction does not use the invariant formula. It stores a two-copy
operator, enumerates four-copy basis labels and performs the 24 permutation
traces. Thus it is independent of the earlier full four-copy dense calculation.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
from itertools import permutations
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm


def swap(d):
    return np.eye(d*d).reshape(d,d,d,d).transpose(1,0,2,3).reshape(d*d,d*d)


def op_purity(u, d):
    realigned = u.reshape(d,d,d,d).transpose(0,2,1,3).reshape(d*d,d*d)
    gram = realigned @ realigned.conj().T
    return float(np.trace(gram @ gram).real / d**4)


def closed_form(u, d):
    f = op_purity(u,d)
    fs = op_purity(u@swap(d),d)
    den = d*d*(d*d+1)*(d*d+2)*(d*d+3)
    moment = (4*d**6+16*d**4+2*d**4*(f+fs))/den
    ep = (d/(d+1))**2 * (1+1/d**2-f-fs)
    rho = d*d*((d*d+1)*(f+fs)-4)/(d*d-1)**2
    return dict(f=f, fs=fs, ep=ep, correlation=rho, product_moment=moment,
                squared_change=4*(d+1)**2*ep/((d*d+1)*(d*d+2)*(d*d+3)))


def direct_traces(u, d):
    b=d*d
    basis=np.arange(b*b).reshape(b,b)
    sw=np.zeros((b*b,b*b),complex)
    for x in range(b):
        for y in range(b):
            ax,bx=divmod(x,d); ay,by=divmod(y,d)
            sw[basis[ay*d+bx,ax*d+by],basis[x,y]]=1
    uu=np.kron(u,u)
    w=uu.conj().T@sw@uu
    ii=np.indices((b,)*4).reshape(4,-1).T
    ans=[]
    for p in permutations(range(4)):
        jj=ii[:,np.argsort(p)]
        # First two-copy swapA imposes these two label equalities.
        out0=(jj[:,1]//d)*d+jj[:,0]%d
        out1=(jj[:,0]//d)*d+jj[:,1]%d
        keep=(ii[:,0]==out0)&(ii[:,1]==out1)
        z=np.sum(w[ii[keep,2]*b+ii[keep,3],jj[keep,2]*b+jj[keep,3]])
        ans.append(dict(permutation=list(p),trace_real=float(z.real),trace_imag=float(z.imag)))
    return ans


def expected_trace(p, d, f, fs):
    p=tuple(p)
    if p in [(0,1,2,3),(0,1,3,2),(1,0,2,3),(1,0,3,2)]:
        return d**6
    if p in [(2,3,0,1),(3,2,1,0)]:
        return d**4*f
    if p in [(2,3,1,0),(3,2,0,1)]:
        return d**4*fs
    return d**4


def haar_unitary(d, seed):
    rg=np.random.default_rng(seed)
    z=rg.normal(size=(d*d,d*d))+1j*rg.normal(size=(d*d,d*d))
    q,r=np.linalg.qr(z)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def two_unitary_qutrit():
    u=np.zeros((9,9),complex)
    for i in range(3):
        for j in range(3):
            u[3*((i+j)%3)+(i+2*j)%3,3*i+j]=1
    return u


def main():
    z=np.diag([1.,-1.]); x=np.array([[0,1],[1,0]])
    y=np.array([[0,-1j],[1j,0]])
    cnot=np.eye(4)[[0,1,3,2]]
    cases=[('I2',2,np.eye(4)),('SWAP2',2,swap(2)),('CNOT2',2,cnot),
           ('ZZ2',2,expm(-.37j*np.kron(z,z))),
           ('phaseSWAP2',2,swap(2)@expm(-.25j*np.pi*np.kron(z,z))),
           ('Cartan2',2,expm(-1j*(.37*np.kron(x,x)+.23*np.kron(y,y)+.11*np.kron(z,z)))),
           ('random2',2,haar_unitary(2,8001)),
           ('I3',3,np.eye(9)),('SWAP3',3,swap(3)),
           ('two_unitary3',3,two_unitary_qutrit()),('random3',3,haar_unitary(3,8002)),
           ('I4',4,np.eye(16)),('SWAP4',4,swap(4)),('random4',4,haar_unitary(4,8003))]
    results=[]
    for name,d,u in cases:
        cf=closed_form(u,d)
        ts=direct_traces(u,d)
        err=max(abs(t['trace_real']-expected_trace(t['permutation'],d,cf['f'],cf['fs'])) for t in ts)
        mean=2*d/(d*d+1)
        variance=2*(d*d-1)**2/((d*d+1)**2*(d*d+2)*(d*d+3))
        direct_moment=sum(t['trace_real'] for t in ts)/(d*d*(d*d+1)*(d*d+2)*(d*d+3))
        direct_corr=(direct_moment-mean**2)/variance
        ep_corr=1-(d*d+1)/(d-1)**2*cf['ep']
        assert err<3e-10
        assert abs(direct_corr-cf['correlation'])<1e-11
        assert abs(ep_corr-cf['correlation'])<1e-12
        assert max(abs(t['trace_imag']) for t in ts)<1e-10
        if name.startswith(('I','SWAP')): assert abs(direct_corr-1)<1e-11
        if name=='CNOT2': assert abs(direct_corr+1/9)<1e-11
        if name=='two_unitary3': assert abs(direct_corr+1/4)<1e-11
        row=dict(name=name,d=d,**cf,max_trace_error=err,
                 direct_correlation=direct_corr,traces=ts)
        results.append(row)
        print(name,'rho=',format(direct_corr,'.12g'),'max trace error=',format(err,'.3g'))
    payload=dict(method='Direct four-copy permutation traces using a two-copy tensor and basis-label constraints; no state sampling.',
                 assertions_passed=True,gate_count=len(cases),permutation_count=24*len(cases),results=results)
    Path(__file__).with_name('exact_global_purity_results.json').write_text(json.dumps(payload,indent=2)+'\n')


if __name__=='__main__': main()
