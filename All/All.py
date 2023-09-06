'''
FIG 6
'''
import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
from numpy.linalg import matrix_rank
import matplotlib.pyplot as plt
import tensorflow as tf

def H(n,m):
    N=2**n
    Matrix=[0]*int(N-m)+[1]*m
    random.shuffle(Matrix)
    Matrix=np.array(Matrix)
    Matrix=Matrix.reshape((2**int(n/2),2**int(n/2)))
    return Matrix

def rho(n,m):
    Hmatrix=H(n,m)
    matrix=tf.linalg.matmul(Hmatrix, tf.transpose(Hmatrix))/m            
    matrix=np.matmul(Hmatrix.T,Hmatrix)/m
    rank=matrix_rank(matrix)
    return matrix ,rank

def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S

def Ent(n,m,s):
    entropy=0
    rank=0
    for i in range(s):
        Rho=rho(n,m) #Rho,Rank=rho(n,m)
        entropy=entropy+Svon(Rho)
        rank=rank+Rank
    return entropy/s ,rank/s
    
def ZOA(n,m):
    l0=m/2**n
    l1=(1/2**(n/2))+(1/2**n)-(m/2**(3*n/2))
    result=-l0*math.log2(l0)-(2**(n/2)-1)*l1*math.log2(l1)
    return result

def diagonal(n,m,s):
    data=[]
    for j in range(s):
        A=np.zeros(2**int(n/2))
        for i in range(m):
            a=random.randrange(2**int(n/2))
            A[a]=A[a]+1./m
        S=0
        for i in range(2**int(n/2)):
            if A[i]!=0:
               S=S-A[i]*math.log2(A[i])
        data.append(S)
    return mean(data)

def MPD(n,m):
    result=3*n/2-math.log2(2**n-m)-math.log2(math.e)/2
    result=result*(2**n-m)+m*(n-math.log2(m))
    result=result/2**n
    return result
    
def rankMPD(n,m,r):
    if m>2**(0.75*n):
       r=2**(n/2)
    if r==1:
       return 0
    else:
       result=3*math.log2(r)-math.log2(r**2-m)-math.log2(math.e)/2
       result=(r**2-m)*result+m*(2*math.log2(r)-math.log2(m))
       result=result/r**2
       return result

def scale(n,a,b,c,s):
    X=[x for x in range(a,b,int((b-a)/c))]
    Y_Ent=[]
    Y_ZOA=[]
    Y_diagonal=[]
    Y_MPD=[]
    Y_rankMPD=[]
    for m in X:
        entropy,rank=Ent(n,m,s)
        Y_Ent.append(entropy)
        Y_ZOA.append(ZOA(n,m))
        Y_diagonal.append(diagonal(n,m,s))
        Y_MPD.append(MPD(n,m))
        Y_rankMPD.append(rankMPD(n,m,rank))
    return X,Y_Ent,Y_ZOA,Y_diagonal,Y_MPD,Y_rankMPD
    
start_time = time.time()

n=14
a=1
b=2**n
c=100
s=100
X,Y_Ent,Y_ZOA,Y_diagonal,Y_MPD,Y_rankMPD=scale(n,a,b,c,s)

with open('Ent.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_Ent))

with open('ZOA.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_ZOA))

with open('diagonal.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_diagonal))
     
with open('MPD.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_MPD))
     
with open('rankMPD.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_rankMPD))

n=14
a=20
b=1600
c=100
s=500
X,Y_Ent,Y_ZOA,Y_diagonal,Y_MPD,Y_rankMPD=scale(n,a,b,c,s)

with open('Ent_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_Ent))

with open('ZOA_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_ZOA))

with open('diagonal_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_diagonal))
     
with open('MPD_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_MPD))
     
with open('rankMPD_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_rankMPD))

print("--- %s seconds ---" % (time.time() - start_time))
