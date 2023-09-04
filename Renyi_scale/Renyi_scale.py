'''
FIG 1 b
'''
import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
import matplotlib.pyplot as plt

def H(n,m):
    N=2**n
    Matrix=[0]*int(N-m)+[1]*m
    random.shuffle(Matrix)
    Matrix=np.array(Matrix)
    Matrix=Matrix.reshape((2**int(n/2),2**int(n/2)))
    return Matrix

def rho(n,m):
    Hmatrix=H(n,m)
    matrix=np.dot(Hmatrix.T,Hmatrix)/m
    return matrix

def Renyi(rho):
    y_1=0
    y_2=0
    y_inf=0
    vp=np.linalg.eigvals(rho)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           y_1=y_1
        else: 
           y_1=y_1+(abs(x))*math.log2(abs(x))
    y_1=-y_1
    for x in vp:
        y_2=y_2+x**2
    y_2=math.log2(y_2)
    y_2=y_2/(1-2)
    y_inf=-math.log2(max(vp))
    return y_1,y_2,y_inf

def Ent(n,m,s):
    Y_1=0
    Y_2=0
    Y_inf=0
    for i in range(s):
        Rho=rho(n,m)
        y_1,y_2,y_inf=Renyi(Rho)
        Y_1=Y_1+y_1
        Y_2=Y_2+y_2
        Y_inf=Y_inf+y_inf
    return Y_1/s,Y_2/s,Y_inf/s


def scale(n,a,b,c,s):
    X=[x for x in range(a,b,int((b-a)/c))]
    Y_1=[]
    Y_2=[]
    Y_inf=[]
    for m in X:
        y_1,y_2,y_inf=Ent(n,m,s)
        Y_1.append(y_1)
        Y_2.append(y_2)
        Y_inf.append(y_inf)
    return X,Y_1,Y_2,Y_inf
    
start_time = time.time()
n=14
a=1
b=2**n
c=100
s=200
X,Y_1,Y_2,Y_inf=scale(n,a,b,c,s)

with open('d_1.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_1))

with open('d_2.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_2))

with open('d_inf.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_inf))

n=14
a=20
b=1600
c=100
s=1000
X,Y_1,Y_2,Y_inf=scale(n,a,b,c,s)

with open('d_1_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_1))

with open('d_2_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_2))

with open('d_inf_zoom.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_inf))

print("--- %s seconds ---" % (time.time() - start_time))
