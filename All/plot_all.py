import matplotlib.pyplot as plt
import numpy as np
import csv

m_Ent=[]
Ent=[]
with open('Ent.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_Ent.append(int(row[0]))
         Ent.append(float(row[1]))

m_ZOA=[]
ZOA=[]
with open('ZOA.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ZOA.append(int(row[0]))
         ZOA.append(float(row[1]))

m_diagonal=[]
diagonal=[]
with open('diagonal.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_diagonal.append(int(row[0]))
         diagonal.append(float(row[1]))
         
m_MPD=[]
MPD=[]
with open('MPD.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_MPD.append(int(row[0]))
         MPD.append(float(row[1]))

m_rankMPD=[]
rankMPD=[]
with open('rankMPD.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_rankMPD.append(int(row[0]))
         rankMPD.append(float(row[1]))
         
m_Ent_zoom=[]
Ent_zoom=[]
with open('Ent_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_Ent_zoom.append(int(row[0]))
         Ent_zoom.append(float(row[1]))

m_ZOA_zoom=[]
ZOA_zoom=[]
with open('ZOA_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ZOA_zoom.append(int(row[0]))
         ZOA_zoom.append(float(row[1]))

m_diagonal_zoom=[]
diagonal_zoom=[]
with open('diagonal_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_diagonal_zoom.append(int(row[0]))
         diagonal_zoom.append(float(row[1]))
         
m_MPD_zoom=[]
MPD_zoom=[]
with open('MPD_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_MPD_zoom.append(int(row[0]))
         MPD_zoom.append(float(row[1]))

m_rankMPD_zoom=[]
rankMPD_zoom=[]
with open('rankMPD_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_rankMPD_zoom.append(int(row[0]))
         rankMPD_zoom.append(float(row[1]))


fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,8))

ax1.plot(m_ZOA,ZOA,'-',color='skyblue',label=''r'$Z_{N,M}$')
ax1.plot(m_diagonal,diagonal,':',color='forestgreen')
ax1.plot(m_MPD,MPD,'-.',color='gray')
ax1.plot(m_Ent,Ent,'--',color='blueviolet')
ax1.plot(m_rankMPD,rankMPD,'k-',label=''r'$R_{N,M}$')
ax1.set_xlabel('M')
ax1.set_xlim(0,2**14)
ax1.set_ylim(0,7)
ax1.set_yticks([0,1,2,3,4,5,6,7])
ax1.set_ylabel('entropy')
ax1.set_xticks([0,2500,5000,7500,10000,12500,15000])
ax1.set_title('global')

ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

ax2.plot(m_ZOA_zoom,ZOA_zoom,'-',color='skyblue')
ax2.plot(m_diagonal_zoom,diagonal_zoom,':',color='forestgreen',label=''r'$D_{N,M}$')
ax2.plot(m_MPD_zoom,MPD_zoom,'-.',color='gray',label=''r'$T_{N,M}$')
ax2.plot(m_Ent_zoom,Ent_zoom,'--',color='blueviolet',label=''r'$E_{N,M}$')
ax2.plot(m_rankMPD_zoom,rankMPD_zoom,'k-')
ax2.set_ylim(4,7)
ax2.set_xlim(0,1600)
ax2.set_xticks([0,250,500,750,1000,1250,1500])
ax2.set_yticks([4,5,6,7])
ax2.set_xlabel('M')
ax2.set_ylabel('entropy')
ax2.set_title('zoom')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

fig.tight_layout() 
fig.savefig('All.pdf')
