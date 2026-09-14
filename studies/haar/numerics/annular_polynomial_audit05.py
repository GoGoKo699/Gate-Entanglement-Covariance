"""Post-protocol exact leading Gaussian Wick enumeration, trace degrees 1--4.

Independent of a claimed annular transfer-matrix theorem: enumerate every
permutation, retain connected order-d^0 terms, and average its phase exactly
over the Pauli signs attached to free row and column indices.
"""
from pathlib import Path
from itertools import permutations
from math import comb
import json
import numpy as np

ROOT=Path(__file__).resolve().parent

def cycle_labels(perm):
    labels=[-1]*len(perm); count=0
    for k in range(len(perm)):
        if labels[k]>=0: continue
        j=k
        while labels[j]<0:
            labels[j]=count; j=perm[j]
        count+=1
    return labels,count

def phase_histogram(row, col, gamma, p, q, nr, nc):
    # Every choice of the free row/column index has an equally likely Pauli
    # sign, independently. Repeated indices are allowed in exact Wick sums.
    choices=1-2*((np.arange(2**(nr+nc))[:,None] >> np.arange(nr+nc))&1)
    phase=np.zeros(len(choices),dtype=int)
    for l in range(p,p+q):
        phase += (choices[:,row[l]]-choices[:,row[gamma[l]]])*choices[:,nr+col[l]]
    return np.bincount(phase+8,minlength=17)

def power_covariance_hist(p,q):
    n=p+q
    gamma=list(range(1,p))+[0]+list(range(p+1,n))+[p]
    histogram=np.zeros(17,dtype=np.int64)
    leading=0; connected=0
    for perm in permutations(range(n)):
        if all(perm[i]<p for i in range(p)): continue
        connected+=1
        col,nc=cycle_labels(perm)
        row,nr=cycle_labels([gamma[perm[i]] for i in range(n)])
        if nr+nc!=n: continue
        leading+=1
        histogram+=phase_histogram(row,col,gamma,p,q,nr,nc)
    # Uniform denominator 2^8 for every p,q<=4.
    scaled=histogram*(2**(8-n))
    return scaled,dict(p=p,q=q,connected_pairings=connected,
        leading_pairings=leading,phase_fourier_numerators=scaled.tolist(),
        phase_fourier_denominator=256)

def main():
    power=np.zeros((4,4,17),dtype=np.int64); counts=[]
    for p in range(1,5):
        for q in range(1,5):
            power[p-1,q-1],info=power_covariance_hist(p,q)
            counts.append(info)
    # Twice the nonconstant coefficients of T_k((x-2)/2), columns x,...,x^4.
    cc=np.array([[1,0,0,0],[-4,1,0,0],[9,-6,1,0],[-16,20,-8,1]],dtype=np.int64)
    cheb=np.einsum('ip,pqz,jq->ijz',cc,power,cc)
    predicted=np.zeros_like(cheb)
    for k in range(1,5):
        for j in range(2*k+1):
            phase=2*k-2*j
            numerator=k*comb(2*k,j)*(1+(-1)**(k+j))
            predicted[k-1,k-1,phase+8]+=numerator*(2**(8-2*k))
    difference=cheb-predicted
    result=dict(status='exact agreement' if not difference.any() else 'mismatch',
        scope='Post-protocol leading-order complex-Gaussian Wick algebra only, polynomial trace degrees one through four. Not a nonanalytic-Renyi theorem.',
        common_fourier_denominator=1024,
        fourier_frequencies=list(range(-8,9)),
        exact_chebyshev_covariance_fourier_numerators=cheb.tolist(),
        predicted_fourier_numerators=predicted.tolist(),
        maximum_integer_discrepancy=int(abs(difference).max()),
        enumeration=counts,
        convention='Cov[Tr T_j((W(0)-2I)/2), Tr T_k((W(t)-2I)/2)] leading d^0; W=GG†/d, G complex standard Gaussian, G(t)_ij=exp(-it a_i b_j)G_ij, balanced Pauli signs.')
    (ROOT/'annular_polynomial_audit05.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],maximum_integer_discrepancy=result['maximum_integer_discrepancy'],
        leading_pairing_counts=[[x['leading_pairings'] for x in counts[4*i:4*i+4]] for i in range(4)]),indent=2))

if __name__=='__main__': main()
