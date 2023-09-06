import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
import matplotlib.pyplot as plt

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

def scale(n,c,s):
    X=[int(2**x) for x in list(np.arange(1,n,(n-1)/c))]
    Y_diagonal=[]
    Y_MPD=[]
    for m in X:
        Y_diagonal.append(diagonal(n,m,s))
        Y_MPD.append(MPD(n,m))
    return X,Y_diagonal,Y_MPD


start_time = time.time()
n=30
c=50
s=1
X,Y_diagonal,Y_MPD=scale(n,c,s)

with open('MPD.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_MPD))

with open('diagonal.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(X,Y_diagonal))

print("--- %s seconds ---" % (time.time() - start_time))
