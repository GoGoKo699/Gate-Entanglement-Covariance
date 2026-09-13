'''
FIG 4
'''
import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
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

def ENM(n,m,s):
    entropy=0
    for i in range(s):
        Rho=rho(n,m)
        entropy=entropy+Svon(Rho)
    return entropy/s

def DNM(n,m,s):
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

def TNM(n,m):
    result=3*n/2-math.log2(2**n-m)-math.log2(math.e)/2
    result=result*(2**n-m)+m*(n-math.log2(m))
    result=result/2**n
    return result

def scale(n,a,b,c,s):
    X=[x for x in range(a,b,int((b-a)/c))]
    Y_ENM=[]
    Y_DNM=[]
    Y_TNM=[]
    for m in X:
        Y_ENM.append(ENM(n,m,s))
        Y_DNM.append(DNM(n,m,s))
        Y_TNM.append(TNM(n,m))
    return X,Y_ENM,Y_DNM,Y_TNM
    
start_time = time.time()

n=14
a=1
b=2**n
c=100
s=100
X,Y_ENM,Y_DNM,Y_TNM=scale(n,a,b,c,s)

with open('ENM.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_Ent))

with open('DNM.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_diagonal))
     
with open('TNM.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_MPD))


n=14
a=20
b=1600
c=100
s=500
X,Y_ENM,Y_DNM,Y_TNM=scale(n,a,b,c,s)

with open('ENM_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_Ent))

with open('DNM_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_diagonal))
 
with open('TNM_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_MPD))

print("--- %s seconds ---" % (time.time() - start_time))
