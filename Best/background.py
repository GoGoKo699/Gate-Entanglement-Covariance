import numpy as np
import math
import cmath
import random
import time
import csv
from statistics import mean
import matplotlib.pyplot as plt
import tensorflow as tf
import argparse

def R(n,m):
    N=2**n
    state=[1]*m+[0]*int(N-m)
    random.shuffle(state)
    state=np.array(state)
    return state

def build_state(state,n):
    limit = 2**n
    norm = int(2**(n/2))
    pp = np.zeros((norm, norm))
    for i in np.nonzero(state):
        b = np.int64(i % norm)
        a = np.int64((i - b) / norm)
        pp[a, b] = 1
    return pp

def rho(state,n,m):
    Matrix=build_state(state,n)
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

def distribution(n,m,s):
    data=[]
    for l in range(s):
        data.append(Svon(rho(R(n,m),n,m)))
    return data

start_time = time.time()
data=distribution(14,716,100000)
with open('background14.csv', 'w') as f:
     writer = csv.writer(f, delimiter='\t')
     writer.writerows(zip(data))
print("--- %s seconds ---" % (time.time() - start_time))
