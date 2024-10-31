import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import csv

m_Ent=[]
Ent=[]
with open('Ent.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_Ent.append(int(row[0]))
         Ent.append(float(row[1]))

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
         
m_Ent_zoom=[]
Ent_zoom=[]
with open('Ent_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_Ent_zoom.append(int(row[0]))
         Ent_zoom.append(float(row[1]))

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
         
fig, ax1 = plt.subplots(figsize=(4.5, 4))

# Main plot (global)
ax1.plot(m_Ent, Ent, '-', color='blueviolet', label=r'$E_{N,M}$')
ax1.plot(m_diagonal, diagonal, ':', color='forestgreen', label=r'$D_{N,M}$')
ax1.plot(m_MPD, MPD, '--', color='gray', label=r'$T_{N,M}$')
ax1.set_xlabel('M')
ax1.set_xlim(0, 2**14)
ax1.set_ylim(0, 7)
ax1.set_yticks([0, 1, 2, 3, 4, 5, 6, 7])
ax1.set_ylabel('entropy')
ax1.set_xticks([0, 2500, 5000, 7500, 10000, 12500, 15000])
ax1.set_title('global with zoom inset')
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

# Inset plot (zoomed view inside ax1)
ax2 = inset_axes(ax1, width="35%", height="35%", loc='upper right', borderpad=1)
ax2.plot(m_Ent_zoom, Ent_zoom, '-', color='blueviolet')
ax2.plot(m_diagonal_zoom, diagonal_zoom, ':', color='forestgreen')
ax2.plot(m_MPD_zoom, MPD_zoom, '--', color='gray')
ax2.set_ylim(4, 7)
ax2.set_xlim(0, 1600)
ax2.set_xticks([0, 500, 1000, 1500])
ax2.set_yticks([4, 5, 6, 7])
ax2.set_xlabel('M')
ax2.set_ylabel('entropy')

# Adjust layout
fig.tight_layout()
fig.savefig('Approximation.pdf')

