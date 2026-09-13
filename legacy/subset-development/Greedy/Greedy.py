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

def R(n,m,seed):
    random.seed(seed)
    N=2**n
    state=[1]*m+[0]*int(N-m)
    random.shuffle(state)
    state=np.array(state)
    return state

def all_partition_set(n):
    a=int(n/2)
    L=[]
    for i in range(2**n):
        m=[int(x) for x in str(bin(i))[2:]]
        m=[0]*(n-len(m))+m
        if m.count(0)==a:
           L.append(m)
    return L

def partition(state,n,l):
    N=2**n
    c=[0]*N
    for i in np.nonzero(state)[0]:
        a=[]
        m=[int(x) for x in str(bin(i))[2:]]
        m=[0]*(n-len(m))+m
        for j in range(n):
            if l[j]==1: a.append(m[j])
        for j in range(n):
            if l[j]==0: a.append(m[j])
        x=int(''.join(map(str, a)), 2)
        c[x]=1
    return c

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

def distribution(state,n,m,L):
    data=[Svon(rho(state,n,m))]
    for l in L:
        new_state=partition(state,n,l)
        data.append(Svon(rho(new_state,n,m)))
    return data

def greedy(n,m,a,b):
    L=all_partition_set(n)
    seed=a
    state0=R(n,m,seed)
    result0=mean(distribution(state0,n,m,L))
    for i in range(a+1,b):
        state1=R(n,m,i)
        result1=mean(distribution(state1,n,m,L))
        if result1>result0:
           seed=i
           result0=result1
    return seed,result0

def main(n,m,a,b):
    start_time = time.time()
    seed,result=greedy(n,m,a,b)
    print('seed',seed)
    print('mean entropy',result)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", default=10, type=int)
    parser.add_argument("--m", default=107, type=int)
    parser.add_argument("--a", default=0, type=int)
    parser.add_argument("--b", default=100, type=int)
    args = vars(parser.parse_args())
    main(**args)
