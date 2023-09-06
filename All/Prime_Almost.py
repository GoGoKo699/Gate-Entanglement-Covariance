import numpy as np
import math
import cmath
import random
import time
from statistics import mean
import matplotlib.pyplot as plt
import csv

start_time = time.time()

def classify(N):
    List=np.ones(N)
    List=List.astype(int)
    List[0]=0
    List[1]=0
    b=int(math.sqrt(N))+1
    for i in range(2,b):
        c=int(N/i)+1
        for j in range(i,c):
             d=i*j
             if d<N: List[d]=0
    for k in range(2,1+int(math.log2(N))):
        for i in np.where(List==1)[0]:
            x=List[i:int(N/i)+1]
            l=np.where(x==k-1)[0]
            for j in l:
                d=i*(j+i)
                if d<N: List[d]=k
    LIST=[]
    for k in range(1,int(math.log2(N))):
        LIST.append(list(np.where(List==k)[0]))
    return LIST
    
def State(n,List):
    a=np.zeros(2**n)
    m=len(List)
    for i in List:
        a[i]=1/math.sqrt(m)
    return a
    
def build_state(state,n):
    limit = 2**n
    norm = int(2**(n/2))
    pp = (0+0j)*np.ones((norm,norm))
    for i in np.nonzero(state)[0]:
        b = np.int64(i % norm)
        a = np.int64((i - b) / norm)
        pp[a, b] =state[i]
    return pp

def rho(state,n):
    M=build_state(state,n)
    M=np.matmul(M, M.conj().T)
    return M

def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    vp=np.sort(vp)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S

n=24

LIST=classify(2**n)

M_prime=[]
ent_prime=[]
for i in range(len(LIST)):
    List=LIST[-1-i]
    M=len(List)
    state=State(n,List)
    ent=Svon(rho(state,n))
    M_prime.append(M)
    ent_prime.append(ent)
    
with open('prime_24.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(M_prime,ent_prime))
    
M_union=[]
ent_union=[]
List=[]
for i in range(len(LIST)):
    List=List+LIST[i]
    M=len(List)
    state=State(n,List)
    ent=Svon(rho(state,n))
    M_union.append(M)
    ent_union.append(ent)
    
with open('union_24.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(M_union,ent_union))

print("--- %s seconds ---" % (time.time() - start_time))
