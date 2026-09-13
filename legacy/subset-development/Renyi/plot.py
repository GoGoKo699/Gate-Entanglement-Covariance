import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import csv

m_1=[]
d_1=[]
with open('d_1.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_1.append(int(row[0]))
         d_1.append(float(row[1]))

m_2=[]
d_2=[]
with open('d_2.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_2.append(int(row[0]))
         d_2.append(float(row[1]))

m_inf=[]
d_inf=[]
with open('d_inf.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_inf.append(int(row[0]))
         d_inf.append(float(row[1]))

m_1_zoom=[]
d_1_zoom=[]
with open('d_1_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_1_zoom.append(int(row[0]))
         d_1_zoom.append(float(row[1]))
         
m_2_zoom=[]
d_2_zoom=[]
with open('d_2_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_2_zoom.append(int(row[0]))
         d_2_zoom.append(float(row[1]))

m_inf_zoom=[]
d_inf_zoom=[]
with open('d_inf_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_inf_zoom.append(int(row[0]))
         d_inf_zoom.append(float(row[1]))


fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,7.5))

ax1.plot(m_1,d_1,'-',color='blueviolet')
ax1.plot(m_2,d_2,'--',color='blueviolet')
ax1.plot(m_inf,d_inf,':',color='blueviolet')
ax1.set_xlabel('M')
ax1.set_xlim(0,2**14)
ax1.set_ylim(0,7)
ax1.set_yticks([0,1,2,3,4,5,6,7])
ax1.set_ylabel('entropy')
ax1.set_xticks([0,2500,5000,7500,10000,12500,15000])
ax1.set_title('global')


ax2.axhline(y=max(d_1_zoom),color='silver',linestyle='solid')
ax2.plot([m_1_zoom[np.argmax(d_1_zoom)],m_1_zoom[np.argmax(d_1_zoom)]],[0,max(d_1_zoom)],color='silver',linestyle='solid',alpha=0.5)
ax2.plot(m_1_zoom,d_1_zoom,'-',color='blueviolet',label=''r'$d\rightarrow 1$')
ax2.axhline(y=max(d_2_zoom),color='silver',linestyle='dashed')
ax2.plot([m_2_zoom[np.argmax(d_2_zoom)],m_2_zoom[np.argmax(d_2_zoom)]],[0,max(d_2_zoom)],color='silver',linestyle='dashed',alpha=0.5)
ax2.plot(m_2_zoom,d_2_zoom,'--',color='blueviolet',label=''r'$d= 2$')
ax2.axhline(y=max(d_inf_zoom),color='silver',linestyle='dotted')
ax2.plot([m_inf_zoom[np.argmax(d_inf_zoom)],m_inf_zoom[np.argmax(d_inf_zoom)]],[0,max(d_inf_zoom)],color='silver',linestyle='dotted',alpha=0.5)
ax2.plot(m_inf_zoom,d_inf_zoom,':',color='blueviolet',label=''r'$d\rightarrow \infty$')
ax2.set_ylim(4,7)
ax2.set_xlim(0,1600)
ax2.set_xticks([0,250,500,750,1000,1250,1500])
ax2.set_yticks([4,5,6,7])
ax2.set_xlabel('M')
ax2.set_ylabel('entropy')
ax2.set_title('zoom')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

fig.tight_layout() 
fig.savefig('Renyi.pdf')
