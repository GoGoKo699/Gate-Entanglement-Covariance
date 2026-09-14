"""Post-protocol exact Wick check for the two four-by-four phase arrays.

No random-state simulation. Enumerates every leading connected Gaussian
pairing through degree three and all four-valued boundary-label assignments.
The comparison is an exact integer Fourier-polynomial comparison.
"""
from pathlib import Path
from itertools import permutations
from math import comb
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
HA = np.outer([1,-1,1,-1],[1,1,-1,-1])
HB = np.array([[1,1,-1,-1],[1,-1,-1,1],[-1,-1,1,1],[-1,1,1,-1]])

def components(p):
    labels = [-1]*len(p)
    count = 0
    for i in range(len(p)):
        if labels[i] >= 0:
            continue
        j = i
        while labels[j] < 0:
            labels[j] = count
            j = p[j]
        count += 1
    return labels,count

def covariance(h,p,q):
    n = p+q
    gamma = list(range(1,p))+[0]+list(range(p+1,n))+[p]
    hist = np.zeros(13,dtype=np.int64)
    count = 0
    # For leading pairings there are exactly n free row/column vertices.
    labels = (np.arange(4**n)[:,None]//(4**np.arange(n)))%4
    for sigma in permutations(range(n)):
        if all(sigma[i] < p for i in range(p)):
            continue
        cols,nc = components(sigma)
        rows,nr = components([gamma[sigma[i]] for i in range(n)])
        if nr+nc != n:
            continue
        count += 1
        phase = np.zeros(len(labels),dtype=np.int64)
        for i in range(p,n):
            phase += h[labels[:,rows[i]],labels[:,nr+cols[i]]]
            phase -= h[labels[:,rows[gamma[i]]],labels[:,nr+cols[i]]]
        hist += np.bincount(phase+6,minlength=13)
    return hist*4**(6-n),count

def main():
    results = {}
    cc = np.array([[1,0,0],[-4,1,0],[9,-6,1]],dtype=np.int64)
    for name,h in [('A',HA),('B',HB)]:
        power = np.zeros((3,3,13),dtype=np.int64)
        counts = np.zeros((3,3),dtype=np.int64)
        for p in range(1,4):
            for q in range(1,4):
                power[p-1,q-1],counts[p-1,q-1] = covariance(h,p,q)
        got = np.einsum('ip,pqz,jq->ijz',cc,power,cc)
        expected = np.zeros_like(got)
        for k in range(1,4):
            for j in range(2*k+1):
                f = 2*k-2*j
                if name == 'A':
                    coefficient = k*comb(2*k,j)*(1+(-1)**(k+j))
                    scale = 2**(12-2*k)
                else:
                    coefficient = k*comb(2*k,j)*(2**(k-1)+(-1)**(k+j))
                    scale = 2**(12-(3*k-1))
                expected[k-1,k-1,f+6] += coefficient*scale
        err = int(np.abs(got-expected).max())
        results[name] = dict(maximum_integer_discrepancy=err,
            leading_pairing_counts=counts.tolist(),
            chebyshev_fourier_numerators=got.tolist(),
            predicted_fourier_numerators=expected.tolist())
    output = dict(status='exact agreement' if all(x['maximum_integer_discrepancy']==0 for x in results.values()) else 'mismatch',
        scope='Leading connected complex Gaussian covariance of Gamma_1 through Gamma_3 for the two fixed four-by-four arrays. No random-state simulation and no independent proof of nonpolynomial entropy extension.',
        fourier_denominator=4096,frequencies=list(range(-6,7)),results=results)
    (ROOT/'generalized_wick_check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({name:x['maximum_integer_discrepancy'] for name,x in results.items()}))

if __name__ == '__main__':
    main()
