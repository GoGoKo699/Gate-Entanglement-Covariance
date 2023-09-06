'''
FIG 10
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

m14=[]
ent14=[]
with open('Ent_14.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m14.append(int(row[0]))
         ent14.append(float(row[1]))
m14=np.array(m14)
ent14=np.array(ent14)

m18=[]
ent18=[]
with open('Ent_18.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m18.append(int(row[0]))
         ent18.append(float(row[1]))
m18=np.array(m18)
ent18=np.array(ent18)

m22=[]
ent22=[]
with open('Ent_22.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m22.append(int(row[0]))
         ent22.append(float(row[1]))
m22=np.array(m22)
ent22=np.array(ent22)

fig=plt.figure(1,figsize=(4.5,5))
ax = fig.add_subplot()

plt.plot(np.log2(m14)/14,ent14/(6.278),':',color='blueviolet',label=''r'$n=14$')
plt.plot(np.log2(m18)/18,ent18/(8.278),'--',color='blueviolet',label=''r'$n=18$')
plt.plot(np.log2(m22)/22,ent22/(10.278),'-',color='blueviolet',label=''r'$n=22$')
plt.xlabel('m')
plt.ylabel(''r'$\mathbf{E}_{n,m} \; /(\frac{n}{2}-cst_0)$')
plt.xlim(0,1)
plt.xticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.ylim(0,1)
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
ax.set_box_aspect(1)
plt.tight_layout() 
plt.savefig('Scalelog.pdf')
