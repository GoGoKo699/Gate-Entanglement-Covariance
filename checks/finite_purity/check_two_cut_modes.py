"""Check two-cut purity modes via direct fourth-Haar-moment contractions."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from check_exact_global_purity import direct_traces, op_purity, swap, haar_unitary, two_unitary_qutrit


def embed(u,q,n):
    eye=np.eye(n)
    return np.einsum('abcd,ij,kl->aibkcjdl',u.reshape(q,q,q,q),eye,eye).reshape((q*n)**2,(q*n)**2)


def direct_rho(u,d):
    traces=direct_traces(u,d)
    moment=sum(t['trace_real'] for t in traces)/(d*d*(d*d+1)*(d*d+2)*(d*d+3))
    mean=2*d/(d*d+1)
    var=2*(d*d-1)**2/((d*d+1)**2*(d*d+2)*(d*d+3))
    return (moment-mean**2)/var


def main():
    z=np.diag([1.,-1.])
    gates=[('I2',2,np.eye(4)),('SWAP2',2,swap(2)),
           ('CNOT2',2,np.eye(4)[[0,1,3,2]]),
           ('phaseSWAP2',2,swap(2)@expm(-.25j*np.pi*np.kron(z,z))),
           ('random2',2,haar_unitary(2,8101)),
           ('two_unitary3',3,two_unitary_qutrit()),('random3',3,haar_unitary(3,8102))]
    results=[]
    for name,q,u in gates:
        for n in [1,2]:
            d=q*n; D=d*d
            eu=embed(u,q,n); es=embed(swap(q),q,n)
            same=direct_rho(eu,d)
            cross=direct_rho(es@eu,d)
            baseline=direct_rho(es,d)
            a=op_purity(u,q); b=op_purity(u@swap(q),q)
            ep=q*q/(q+1)**2*(1+1/q**2-a-b)
            gt=.5*(1-(a-b)/(1-1/q**2))
            K=(q+1)**2*(D+1)*(D+q*q)/((q*q+1)*D*D+(q**4+1-6*q*q)*D+q*q+q**4)
            plus=(same+cross)/(1+baseline)
            assert abs(plus-(1-K*ep))<1e-10
            minus=(same-cross)/(1-baseline) if n>1 else None
            if minus is not None: assert abs(minus-(1-2*gt))<1e-10
            row=dict(gate=name,q=q,n=n,d=d,a=a,b=b,ep=ep,gt=gt,
                     direct_same=same,direct_cross=cross,direct_baseline=baseline,
                     direct_plus=plus,predicted_plus=1-K*ep,
                     direct_minus=minus,predicted_minus=1-2*gt if n>1 else None)
            results.append(row)
            print(name,n,'plus',format(plus,'.12g'),'minus',minus)
    Path(__file__).with_name('two_cut_modes_results.json').write_text(json.dumps(dict(
        method='Direct full-Hilbert-space fourth-Haar-moment traces, independent of active-factor and closed-form simplifications.',
        assertions_passed=True,case_count=len(results),results=results),indent=2)+'\n')


if __name__=='__main__': main()
