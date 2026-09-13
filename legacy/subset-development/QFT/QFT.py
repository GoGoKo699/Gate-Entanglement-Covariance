import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve
import tensorflow as tf


def H(m,n):
    N=2**n
    Matrix=[0]*int(N-m)+[1]*m
    random.shuffle(Matrix)
    Matrix=np.array(Matrix)
    Matrix_QFT=np.fft.fft(Matrix)
    Matrix=Matrix.reshape((2**int(n/2),2**int(n/2)))
    Matrix_QFT=Matrix_QFT.reshape((2**int(n/2),2**int(n/2)))
    return Matrix,Matrix_QFT

def rho(m,n):
    M,M_QFT=H(m,n)
    M=tf.linalg.matmul(tf.transpose(M), M)/m
    M_QFT=tf.linalg.matmul(tf.transpose(M_QFT,conjugate=True), M_QFT)/(m*2**n)
    return M,M_QFT

def Svon(rho):
    S=0
    w = tf.linalg.eigvalsh(rho)
    w=tf.math.real(w)
    wf = tf.gather(w, tf.where(w > 1e-15))
    vp=np.array(wf)
    vp=list(vp)
    for x in vp:
        S=S+(float(x))*math.log2(float(x))
    return -S

def Ent(k,m,s):
    a=[]
    b=[]
    for i in range(s):
        A,B=rho(m,k)
        a.append(Svon(A))
        b.append(Svon(B))
    return mean(a),mean(b)

def scale(n,a,b,c,s):
    Z=[x for x in range(a,b,int((b-a)/c))]
    a=[]
    b=[]
    for l in Z:
        A,B=Ent(n,l,s)
        a.append(A)
        b.append(B)
    return Z,a,b


start_time = time.time()
n=14
a=1
b=2**n
c=100
s=100
m,ent,ent_QFT=scale(n,a,b,c,s)

with open('Ent.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(m,ent))

with open('Ent_QFT.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(m,ent_QFT))

print("--- %s seconds ---" % (time.time() - start_time))
