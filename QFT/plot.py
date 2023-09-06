'''
FIG 13
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

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

plt.figure(figsize=(4.5,4.2))

plt.plot(m,ent,'-',color='blueviolet',label=''r'$E_{N,M}$')
plt.plot(m_QFT,ent_QFT,'--',color='skyblue',label='QFT')
plt.xlabel('M')
plt.ylabel('entropy')
plt.xlim(0,2**14)
plt.ylim(0,7)
plt.yticks([0,1,2,3,4,5,6,7])
plt.xticks([0,2500,5000,7500,10000,12500,15000])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('QFT.pdf')
