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

def rho(m,n):
    N=2**n
    Matrix=[0]*int(N-m)+[1]*m
    random.shuffle(Matrix)
    Matrix=np.array(Matrix)
    Matrix=Matrix.reshape((2**int(n/2),2**int(n/2)))
    return tf.linalg.matmul(tf.transpose(Matrix), Matrix)/m

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

def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S

def Ent(k,m,s):
    b=[]
    for i in range(s):
        b.append(Svon(rho(m,k)))
    return mean(b)

def scalelog(n,c,s):
    Z=[int(2**x) for x in list(np.arange(1,n,(n-1)/c))]
    a=[]
    for l in Z:
        a.append(Ent(n,l,s))
    return Z,a


start_time = time.time()

m14,ent14=scalelog(14,100,200)
with open('Ent_14.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(m14,ent14))

m18,ent18=scalelog(18,100,20)
with open('Ent_18.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(m18,ent18))

m22,ent22=scalelog(22,100,6)
with open('Ent_22.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(m22,ent22))

print("--- %s seconds ---" % (time.time() - start_time))
