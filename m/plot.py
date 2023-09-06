'''
FIG 8
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

xdata=np.array([10,12,14,16,18,20,22,24,26,28,30])

data6=[]
with open('m6.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         data6.append(float(row[0]))
data6=np.array(data6)

data7=[]
with open('m7.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         data7.append(float(row[0]))
data7=np.array(data7)

data8=[]
with open('m8.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         data8.append(float(row[0]))
data8=np.array(data8)

x=np.linspace(9,31,100)

fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,8))

ax1.plot(x,x/2-1+0.278,'-',color='skyblue')
ax1.plot(xdata,data7,'*',color='gray',markersize=5)
ax1.plot(xdata,data6,'x',color='forestgreen',markersize=6)
ax1.plot(xdata,data8,'+',color='blueviolet',markersize=7)
ax1.set_xlim([9, 31])
ax1.set_xticks([10,15,20,25,30])
ax1.set_xlabel('n')
ax1.set_ylabel('entropy')
ax1.set_title('compare')

ax2.axhline(y=0,color='skyblue')
ax2.plot(xdata,data6-(xdata/2-1+0.278),'x',color='forestgreen',markersize=6,label='m=0.6')
ax2.plot(xdata,data7-(xdata/2-1+0.278),'*',color='gray',markersize=5,label='m=0.7')
ax2.plot(xdata,data8-(xdata/2-1+0.278),'+',color='blueviolet',markersize=7,label='m=0.8')
ax2.set_xlim([9, 31])
ax2.set_xticks([10,15,20,25,30])
ax2.set_xlabel('n')
ax2.set_ylabel('entropy')
ax2.set_title('converge')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

fig.tight_layout() 
fig.savefig('m.pdf')
