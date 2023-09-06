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

def rho(eta,n):
    N=2**n
    m=int(2**(eta*n))
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

def Ent(n,eta,s):
    b=[]
    for i in range(s):
        b.append(Svon(rho(eta,n)))
    return mean(b)

start_time = time.time()
L=[20,22,24,26,28,30]

data=[]
eta=0.6
data.append(Ent(10,eta,10000))
data.append(Ent(12,eta,1000))
data.append(Ent(14,eta,500))
data.append(Ent(16,eta,100))
data.append(Ent(18,eta,10))
for i in L:
    data.append(Svon(rho(eta,i)))
with open('m6.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

data=[]
eta=0.7
data.append(Ent(10,eta,10000))
data.append(Ent(12,eta,1000))
data.append(Ent(14,eta,500))
data.append(Ent(16,eta,100))
data.append(Ent(18,eta,10))
for i in L:
    data.append(Svon(rho(eta,i)))
with open('m7.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

data=[]
eta=0.8
data.append(Ent(10,eta,10000))
data.append(Ent(12,eta,1000))
data.append(Ent(14,eta,500))
data.append(Ent(16,eta,100))
data.append(Ent(18,eta,10))
for i in L:
    data.append(Svon(rho(eta,i)))
with open('m8.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))

print("--- %s seconds ---" % (time.time() - start_time))
