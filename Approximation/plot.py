import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import csv

m_ENM=[]
ENM=[]
with open('ENM.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ENM.append(int(row[0]))
         ENM.append(float(row[1]))

m_DNM=[]
DNM=[]
with open('DNM.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_DNM.append(int(row[0]))
         DNM.append(float(row[1]))
         
m_TNM=[]
TNM=[]
with open('TNM.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_TNM.append(int(row[0]))
         TNM.append(float(row[1]))
         
m_ENM_zoom=[]
ENM_zoom=[]
with open('ENM_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_ENM_zoom.append(int(row[0]))
         ENM_zoom.append(float(row[1]))

m_DNM_zoom=[]
DNM_zoom=[]
with open('DNM_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_DNM_zoom.append(int(row[0]))
         DNM_zoom.append(float(row[1]))
         
m_TNM_zoom=[]
TNM_zoom=[]
with open('TNM_zoom.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         m_TNM_zoom.append(int(row[0]))
         TNM_zoom.append(float(row[1]))
         
fig, ax1 = plt.subplots(figsize=(4.5, 4))

# Main plot (global)
ax1.plot(m_ENM, ENM, '-', color='blueviolet', label=r'$E_{N,M}$')
ax1.plot(m_DNM, DNM, ':', color='forestgreen', label=r'$D_{N,M}$')
ax1.plot(m_TNM, TNM, '--', color='gray', label=r'$T_{N,M}$')
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
ax2.plot(m_ENM_zoom, ENM_zoom, '-', color='blueviolet')
ax2.plot(m_DNM_zoom, DNM_zoom, ':', color='forestgreen')
ax2.plot(m_TNM_zoom, TNM_zoom, '--', color='gray')
ax2.set_ylim(4, 7)
ax2.set_xlim(0, 1600)
ax2.set_xticks([0, 500, 1000, 1500])
ax2.set_yticks([4, 5, 6, 7])
ax2.set_xlabel('M')
ax2.set_ylabel('entropy')

# Adjust layout
fig.tight_layout()
fig.savefig('Approximation.pdf')

