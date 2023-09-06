'''
FIG 9
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

m_MPD=[]
MPD=[]
with open('MPD.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_MPD.append(int(row[0]))
         MPD.append(float(row[1]))
m_MPD=np.array(m_MPD)
MPD=np.array(MPD)

m_diagonal=[]
diagonal=[]
with open('diagonal.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_diagonal.append(int(row[0]))
         diagonal.append(float(row[1]))
m_diagonal=np.array(m_diagonal)
diagonal=np.array(diagonal)

fig=plt.figure(1,figsize=(4.5,5))
ax = fig.add_subplot()

plt.plot([0,0.5],[0,15],'-',color='skyblue')
plt.plot([0.5,1],[15,15],'-',color='skyblue')
plt.plot(np.log2(m_MPD)/30,MPD,'-.',color='gray',label=''r'$\mathbf{T}_{n,m}$')
plt.plot(np.log2(m_diagonal)/30,diagonal,':',color='forestgreen',label=''r'$\mathbf{D}_{n,m}$')
plt.xlabel('m')
plt.ylabel('entropy')

plt.xlim(0,1)
plt.xticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.ylim(0,15)
plt.yticks([0,3,6,9,12,15])

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
ax.set_box_aspect(1)
plt.tight_layout() 
plt.savefig('Intersection.pdf')
