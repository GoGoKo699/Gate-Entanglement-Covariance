'''
FIG 11
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

partition=[]
with open('Partition.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         partition.append(float(row[0]))

gaussian=[]
with open('Gaussian.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         gaussian.append(float(row[0]))


fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,7.5))

Min=9.206
Max=9.224

ax1.hist(partition,bins=np.arange(Min, Max, (Max-Min)/500),align='mid',color='blueviolet',label=''r'$|\mathbb{A}_{N,M_n}$>')
ax1.set_xlim(Min,Max)
ax1.set_ylim(0,30)
ax1.set_yticks([0,5,10,15,20,25,30])
ax1.legend()
ax1.set_title('maximally entangling successions')
ax1.set_xlabel('entropy')
ax1.set_ylabel('number of occurrences')

Min=9.269
Max=9.287

ax2.hist(gaussian,bins=np.arange(Min, Max, (Max-Min)/500),align='mid',color='forestgreen',label=''r'$|\mathbb{R}_N$>')
ax2.set_xlim(Min,Max)
ax2.set_ylim(0,30)
ax2.set_yticks([0,5,10,15,20,25,30])
ax2.legend()
ax2.set_title('gaussian random state')
ax2.set_xlabel('entropy')
ax2.set_ylabel('number of occurrences')

fig.tight_layout() 
fig.savefig('Partition.pdf')
