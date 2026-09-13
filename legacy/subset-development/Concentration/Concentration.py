'''
FIG 1
'''

import numpy as np
import math
import cmath
import random
import time
from statistics import mean
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def R(n,m):
    N=2**n
    state=[0]*int(N-m)+[1]*m
    random.shuffle(state)
    state=np.array(state)
    state=state/np.sqrt(m)
    return state

def build_state(state,n):
    limit = 2**n
    norm = int(2**(n/2))
    pp = np.zeros((norm, norm))
    for i in range(limit):
        b = np.int64(i % norm)
        a = np.int64((i - b) / norm)
        pp[a, b] = state[i]
    return pp

def rho(state,n):
    Hmatrix=build_state(state,n)
    return np.dot(Hmatrix.T,Hmatrix)
    
def partition(state,n):
    N=2**n
    b=[0]*int(n/2)+[1]*int(n/2)
    random.shuffle(b)
    c=[0]*N
    for i in range(N):
        a=[]
        m=[int(x) for x in str(bin(i))[2:]]
        m=[0]*(n-len(m))+m
        for j in range(n):
            if b[j]==1: a.append(m[j])
        for j in range(n):
            if b[j]==0: a.append(m[j])
        l=int(''.join(map(str, a)), 2)
        c[l]=state[i]
    return np.array(c)
    
def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S

def Ent(n,m,s):
    entropy=[]
    for i in range(s):
        Rho=rho(R(n,m),n)
        entropy.append(Svon(Rho))
    return mean(entropy),entropy
    
def Part(n,m,s):
    entropy=[]
    state=R(n,m)
    for j in range(s):
        state=partition(state,n)
        Rho=rho(state,n)
        entropy.append(Svon(Rho))
    return mean(entropy),entropy
    
def scale(n,a,b,c,s):
    X=[x for x in range(a,b,int((b-a)/c))]
    Y_Ent=[]
    X_Ent_data=[]
    Y_Ent_data=[]
    Y_Part=[]
    X_Part_data=[]
    Y_Part_data=[]
    for m in X:
        ent,ent_data=Ent(n,m,s)
        part,part_data=Part(n,m,s)
        Y_Ent.append(ent)
        X_Ent_data.extend([m]*len(ent_data))
        Y_Ent_data.extend(ent_data)
        Y_Part.append(part)
        X_Part_data.extend([m]*len(part_data))
        Y_Part_data.extend(part_data)
    return X,Y_Ent,X_Ent_data,Y_Ent_data,Y_Part,X_Part_data,Y_Part_data
    
start_time = time.time()

n=14
a=1
b=2**n
c=50
s=100

X,Y_Ent,X_Ent_data,Y_Ent_data,Y_Part,X_Part_data,Y_Part_data=scale(n,a,b,c,s)

n=14
a=20
b=1600
c=30
s=500

X_zoom,Y_Ent_zoom,X_Ent_data_zoom,Y_Ent_data_zoom,Y_Part_zoom,X_Part_data_zoom,Y_Part_data_zoom=scale(n,a,b,c,s)

fig, ax1 = plt.subplots(figsize=(4.5, 4))

# Main plot (ax1)
ax1.plot(X_Part_data, Y_Part_data, '.', color='skyblue', markersize=1, alpha=0.1)
ax1.plot(X_Ent_data, Y_Ent_data, '.', color='blueviolet', markersize=1, alpha=0.1)
ax1.plot(X, Y_Part, '-', color='skyblue', label='multiple partitions')
ax1.plot(X, Y_Ent, '--', color='blueviolet', label='multiple states')
ax1.set_xlabel('M')
ax1.set_xlim(0, 2**14)
ax1.set_ylim(0, 7)
ax1.set_yticks([0, 1, 2, 3, 4, 5, 6, 7])
ax1.set_ylabel('entropy')
ax1.set_xticks([0, 2500, 5000, 7500, 10000, 12500, 15000])
ax1.set_title('global with zoom inset')
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

# Inset plot (ax2 inside ax1)
ax2 = inset_axes(ax1, width="35%", height="35%", loc='upper right', borderpad=1)  # Adjust the size and location

ax2.plot(X_Part_data_zoom, Y_Part_data_zoom, '.', color='skyblue', markersize=0.5, alpha=0.5)
ax2.plot(X_Ent_data_zoom, Y_Ent_data_zoom, '.', color='blueviolet', markersize=0.5, alpha=0.5)
ax2.plot(X_zoom, Y_Part_zoom, '-', color='skyblue')
ax2.plot(X_zoom, Y_Ent_zoom, '--', color='blueviolet')
ax2.set_xlim(0, 1600)
ax2.set_ylim(4, 7)
ax2.set_xticks([0, 500, 1000, 1500])
ax2.set_yticks([4, 5, 6, 7])
ax2.set_xlabel('M')
ax2.set_ylabel('entropy')

# Adjust layout
fig.tight_layout()
plt.savefig('Concentration.pdf')

print("--- %s seconds ---" % (time.time() - start_time))

