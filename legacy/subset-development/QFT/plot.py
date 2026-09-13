'''
FIG 5
'''
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

m=[]
ent=[]
with open('Ent.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m.append(int(row[0]))
         ent.append(float(row[1]))

m_QFT=[]
ent_QFT=[]
with open('Ent_QFT.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_QFT.append(int(row[0]))
         ent_QFT.append(float(row[1]))
         
def classify(N):
    List=np.ones(N)
    List=List.astype(int)
    List[0]=0
    List[1]=0
    b=int(math.sqrt(N))+1
    for i in range(2,b):
        c=int(N/i)+1
        for j in range(i,c):
             d=i*j
             if d<N: List[d]=0
    for k in range(2,1+int(math.log2(N))):
        for i in np.where(List==1)[0]:
            x=List[i:int(N/i)+1]
            l=np.where(x==k-1)[0]
            for j in l:
                d=i*(j+i)
                if d<N: List[d]=k
    LIST=[]
    for k in range(1,int(math.log2(N))):
        LIST.append(list(np.where(List==k)[0]))
    return LIST
    
def State(n,List):
    a=np.zeros(2**n)
    m=len(List)
    for i in List:
        a[i]=1/math.sqrt(m)
    a_QFT=np.fft.fft(a)
    a_QFT=a_QFT/np.linalg.norm(a_QFT)
    return a,a_QFT
    
def build_state(state,n):
    limit = 2**n
    norm = int(2**(n/2))
    pp = (0+0j)*np.ones((norm,norm))
    for i in np.nonzero(state)[0]:
        b = np.int64(i % norm)
        a = np.int64((i - b) / norm)
        pp[a, b] =state[i]
    return pp

def rho(state,n):
    M=build_state(state,n)
    M=np.matmul(M, M.conj().T)
    return M

def Svon(rho):
    S=0
    vp=np.linalg.eigvals(rho)
    vp=np.sort(vp)
    for x in vp:
        if 1e-15> x.real > -1e-15: 
           S=S
        else: 
           S=S+(abs(x))*math.log2(abs(x))
    return -S
    
n=14
LIST=classify(2**n)

M_union=[]
Ent_union=[]
Ent_union_QFT=[]
List=[]
for i in range(len(LIST)):
    List=List+LIST[i]
    M=len(List)
    state,state_QFT=State(n,List)
    ent_union=Svon(rho(state,n))
    ent_union_QFT=Svon(rho(state_QFT,n))
    M_union.append(M)
    Ent_union.append(ent_union)
    Ent_union_QFT.append(ent_union_QFT)

plt.figure(figsize=(4.5,4))

plt.plot(m_QFT,ent_QFT,'-',color='skyblue',label='QFT')
plt.plot(m,ent,'--',color='blueviolet',label=''r'$E_{N,M}$')
plt.plot(M_union,Ent_union_QFT,'+',markersize=10,color='skyblue',label='QFT')
plt.plot(M_union,Ent_union,'+',markersize=6,color='forestgreen',label=''r'$U_{N,k}$')
plt.xlabel('M')
plt.ylabel('entropy')
plt.xlim(0,2**14)
plt.ylim(0,7)
plt.yticks([0,1,2,3,4,5,6,7])
plt.xticks([0,2500,5000,7500,10000,12500,15000])
plt.title('position and momentum space')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('QFT.pdf')
