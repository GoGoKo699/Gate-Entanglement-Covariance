'''
FIG 4
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

m_ent_14=[]
ent_14=[]
with open('Ent.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ent_14.append(int(row[0]))
         ent_14.append(float(row[1]))
         
m_prime_14=[]
prime_14=[]
with open('prime.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_prime_14.append(int(row[0]))
         prime_14.append(float(row[1]))
         
m_union_14=[]
union_14=[]
with open('union.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_union_14.append(int(row[0]))
         union_14.append(float(row[1]))
         
m_ent_26=[]
ent_26=[]
with open('Ent_26.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ent_26.append(int(row[0]))
         ent_26.append(float(row[1]))
         
m_prime_26=[]
prime_26=[]
with open('prime_26.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_prime_26.append(int(row[0]))
         prime_26.append(float(row[1]))
         
m_union_26=[]
union_26=[]
with open('union_26.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_union_26.append(int(row[0]))
         union_26.append(float(row[1]))

plt.figure(1,figsize=(4.5,4.2))

plt.plot(m_ent_14,ent_14,'--',color='blueviolet',label=''r'$E_{N,M}$')
plt.plot(m_prime_14,prime_14,'-',alpha=0.6,color='forestgreen')
plt.plot(m_prime_14,prime_14,'x',alpha=0.6,color='forestgreen',label=''r'$\mathbb{P}_k$')
plt.plot(m_union_14,union_14,'-',alpha=0.6,color='gray')
plt.plot(m_union_14,union_14,'*',alpha=0.6,color='gray',label=''r'$\mathbb{U}_k$')
plt.plot(m_union_14[0],union_14[0],'+',color='black',markersize=10)

plt.title('n=14')
plt.xlabel('M')
plt.ylabel('entropy')
plt.xlim(0,2**14)
plt.ylim(0,7)
plt.yticks([0,1,2,3,4,5,6,7])
plt.xticks([0,2500,5000,7500,10000,12500,15000])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('Scale_14.pdf')

plt.figure(2,figsize=(4.5,4.2))

plt.plot(m_ent_26,ent_26,'--',color='blueviolet',label=''r'$E_{N,M}$')
plt.plot(m_prime_26,prime_26,'-',alpha=0.6,color='forestgreen')
plt.plot(m_prime_26,prime_26,'x',alpha=0.6,color='forestgreen',label=''r'$\mathbb{P}_k$')
plt.plot(m_union_26,union_26,'-',alpha=0.6,color='gray')
plt.plot(m_union_26,union_26,'*',alpha=0.6,color='gray',label=''r'$\mathbb{U}_k$')
plt.plot(m_union_26[0],union_26[0],'+',color='black',markersize=10)

plt.title('n=26')
plt.xlabel('M')
plt.ylabel('entropy')
plt.xlim(0,2**26)
plt.ylim(0,13)
plt.yticks([0,1,3,5,7,9,11,13])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('Scale_26.pdf')
