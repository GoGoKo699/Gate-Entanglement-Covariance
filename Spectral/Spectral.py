import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import variance
import matplotlib.pyplot as plt

def H(M,n):
    N=2**n
    p=M/N
    Matrix=[0]*int(N-M)+[1]*M
    random.shuffle(Matrix)
    Matrix=np.array(Matrix)
    Matrix=Matrix.reshape((2**int(n/2),2**int(n/2)))
    return Matrix

def rho(M,n):
    Hmatrix=H(M,n)
    return np.dot(Hmatrix.T,Hmatrix)/M


start_time = time.time()

n=24
M_list=[107,276,716,1873,4934,13091,34771,93018,250660,672556,1836685]
M=M_list[int(n/2-5)]

rho=rho(M,n)
vp=np.linalg.eigvals(rho)
vp=np.real(vp)
vp=np.sort(vp)
data=list(vp)

with open('Spectral.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

print("--- %s seconds ---" % (time.time() - start_time))
