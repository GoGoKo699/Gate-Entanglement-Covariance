'''
FIG 12
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

n10=10
m10=107
seed10=163765

n14=14
m14=716
seed14=541

background10=[]
with open(f'background{n10}.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         background10.append(float(row[0]))

background14=[]
with open(f'background{n14}.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         background14.append(float(row[0]))

state10=R(n10,m10,seed10)
L10=all_partition_set(n10)
data10=distribution(state10,n10,m10,L10)

state14=R(n14,m14,seed14)
L14=all_partition_set(n14)
data14=distribution(state14,n14,m14,L14)

Min10=min(min(background10),min(data10))
Max10=max(max(background10),max(data10))
Mean10=mean(background10)

Min14=min(min(background14),min(data14))
Max14=max(max(background14),max(data14))
Mean14=mean(background14)

fig,ax = plt.subplots(2,figsize=(5,7.5))
#ax[0].hist(background10,density=False,bins=np.arange(Min10, Max10, (Max10-Min10)/500),align='mid',color='blueviolet',label='Best')
ax[0].hist(background10,density=False,bins=np.arange(Min10, Max10, (Max10-Min10)/500),align='mid',color='skyblue',label='average')
ax[0].set_title(''r'$n=10, M=107$')
ax[0].set_xlabel('entropy')
ax[0].set_ylabel('number of occurrences',color='skyblue')
ax[0].set_xlim(Mean10-0.3,Mean10+0.3)
ax2=ax[0].twinx()
ax2.hist(data10,density=False,bins=np.arange(Min10, Max10, (Max10-Min10)/500),align='mid',color='blueviolet',label='best')
ax2.set_ylabel('number of occurrences',color='blueviolet')
ax[0].legend(loc='upper left')
ax2.legend(loc='upper right')

#ax[1].hist(background14,density=False,bins=np.arange(Min14, Max14, (Max14-Min14)/500),align='mid',color='m',label='Best')
ax[1].hist(background14,density=False,bins=np.arange(Min14, Max14, (Max14-Min14)/500),align='mid',color='skyblue',label='average')
ax[1].set_title(''r'$n=14, M=716$')
ax[1].set_xlabel('entropy')
ax[1].set_ylabel('number of occurrences',color='skyblue')
ax[1].set_xlim(Mean14-0.09,Mean14+0.09)
ax2=ax[1].twinx()
ax2.hist(data14,density=False,bins=np.arange(Min14, Max14, (Max14-Min14)/500),align='mid',color='blueviolet',label='best')
ax2.set_ylabel('number of occurrences',color='blueviolet')
ax[1].legend(loc='upper left')
ax2.legend(loc='upper right')

fig.tight_layout() 
plt.savefig('Best.pdf') 
