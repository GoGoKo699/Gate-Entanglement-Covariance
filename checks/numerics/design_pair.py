"""Two exact two-design local orbits with distinct entropy memory.

Directly checks the full two-copy twirling superoperator, not only ep/gt.
No sampled gates, Haar input states, or fitted coefficients are used.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parents[1]

def coeff(alpha,K=65536):
    k=np.arange(2,K+1,dtype=float)
    if alpha==1: c=4*(-1.)**(k-1)/(k*(k*k-1))
    else:
        c=np.empty(len(k));c[0]=-2*alpha/(alpha+2)
        c[1:]=c[0]*np.cumprod((alpha-k[:-1])/(alpha+k[:-1]+1))
    return k,c

def weights(U):
    R=U.reshape(2,2,2,2).transpose(0,2,1,3).reshape(4,4)
    return np.linalg.svd(R,compute_uv=False)**2/4

def channel_projectors():
    sa=np.zeros((16,16));sb=np.zeros((16,16))
    for a in range(2):
     for b in range(2):
      for c in range(2):
       for e in range(2):
        inp=((a*2+b)*2+c)*2+e
        sa[((c*2+b)*2+a)*2+e,inp]=1
        sb[((a*2+e)*2+c)*2+b,inp]=1
    basis=[np.eye(16),sa,sb,sa@sb]
    V=np.array([v.reshape(-1,order='F') for v in basis]).T
    W=V[:,[0,3]]
    return V@np.linalg.inv(V.T@V)@V.T,W@np.linalg.inv(W.T@W)@W.T

def main():
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1.,-1.])
    S=np.eye(4)[[0,2,1,3]]
    us={'A':np.array([.5+np.sqrt(3/20),.5,.5-np.sqrt(3/20)]),
        'B':np.array([.5+np.sqrt(1/20),.5+np.sqrt(1/20),.5-2*np.sqrt(1/20)])}
    Plocal,Phaar=channel_projectors();results={}
    for name,u in us.items():
        c=.5*np.arccos(np.sqrt(u))
        U=expm(-1j*sum(t*np.kron(p,p) for t,p in zip(c,[X,Y,Z])))
        eta=weights(U);cross=weights(S@U)
        uu=np.kron(U,U)
        channel=np.kron(uu.conj(),uu)
        dressed=Plocal@channel@Plocal
        memories={}
        for alpha in [.5,1,2,3]:
            k,cs=coeff(alpha)
            power=eta[:,None]**k[None,:]
            cov=.25*np.sum(k*cs**2*np.sum(power,axis=0))
            var=.25*np.sum(k*cs**2)
            memories[str(alpha)]=dict(covariance=float(cov),variance=float(var),correlation=float(cov/var))
        results[name]=dict(cos_squared_double_angles=u.tolist(),cartan_angles=c.tolist(),
            operator_weights=eta.tolist(),crossed_operator_weights=cross.tolist(),
            F2=float(np.sum(eta**2)),F3=float(np.sum(eta**3)),crossed_F2=float(np.sum(cross**2)),
            twirled_channel_frobenius_error=float(np.linalg.norm(dressed-Phaar)),
            twirled_channel_maximum_entry_error=float(np.max(abs(dressed-Phaar))),memory=memories)
    diff=results['A']['memory']['3']['correlation']-results['B']['memory']['3']['correlation']
    exact=3*np.sqrt(5)/20000
    ordinary={a:results['A']['memory'][a]['correlation']-results['B']['memory'][a]['correlation'] for a in ['0.5','1','2','3']}
    out=dict(status='passed',scope='Fixed two-qubit gates with independent local Haar input/output dressing, each orbit is an exact unitary 2-design. Memory comparisons use inherited large-spectator Haar entropy theorem. No state-design or efficient estimation claim.',results=results,
         differences_A_minus_B=ordinary,renyi3_difference_exact_expression='3 sqrt(5) / 20000',renyi3_difference_error=abs(diff-exact),
         series_limit='Ordinary orders only. K=65536; alpha=1/2 static tail below 7e-11. No significance inferred from numerical decimal evaluation.')
    assert max(x['twirled_channel_frobenius_error'] for x in results.values())<1e-12
    assert max(abs(x['F2']-.4) for x in results.values())<1e-13
    assert max(abs(x['crossed_F2']-.4) for x in results.values())<1e-13
    assert abs(diff-exact)<1e-13
    (ROOT/'results/design_pair.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
