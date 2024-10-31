'''
FIG 7
'''
import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import variance
import matplotlib.pyplot as plt

def G(n):
    N=2**n
    state= np.random.normal(0, 1/2**int(n/2), N)
    norm=np.linalg.norm(state)
    return state/norm

def R(n,m):
    N=2**n
    state=[0]*int(N-m)+[1]*m
    random.shuffle(state)
    state=np.array(state)
    state=state/np.sqrt(m)
    return state

def build_state(state,qubits):
    limit = 2**qubits
    norm = int(2**(qubits/2))
    pp = np.zeros((norm, norm))
    for i in range(limit):
        b = np.int64(i % norm)
        a = np.int64((i - b) / norm)
        pp[a, b] = state[i]
    return pp

def rho(state,n):
    Hmatrix=build_state(state,n)
    return np.dot(Hmatrix.T,Hmatrix)

def partition(state,n):
    N=2**n
    b=[0]*int(n/2)+[1]*int(n/2)
    random.shuffle(b)
    c=[0]*N
    for i in range(N):
        a=[]
        m=[int(x) for x in str(bin(i))[2:]]
        m=[0]*(n-len(m))+m
        for j in range(n):
            if b[j]==1: a.append(m[j])
        for j in range(n):
            if b[j]==0: a.append(m[j])
        l=int(''.join(map(str, a)), 2)
        c[l]=state[i]
    return np.array(c)

def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S

def distribution(state,n,sample):
    data=[]
    for i in range(sample):
        data.append(Svon(rho(partition(state,n),n)))
    return data

start_time = time.time()
n=20
sample=1000

M_list=[107,276,716,1873,4934,13091,34771,93018,250660,672556,1836685]
M=M_list[int(n/2-5)]
state=R(n,M)
data=distribution(state,n,sample)
with open('Partition.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

state=G(n)
data=distribution(state,n,sample)
with open('Gaussian.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

print("--- %s seconds ---" % (time.time() - start_time))
