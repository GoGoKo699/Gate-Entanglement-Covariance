'''
FIG 5
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

data=[]
with open('Spectral.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         data.append(float(row[0]))
         
fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,8))

x=np.linspace(0.000001,0.007,1000)
ax1.plot(x,-x*np.log2(x),'-',color='skyblue',label=''r'$-x\log_2 x$')
ax1.plot(data[0],-data[0]*np.log2(data[0]),'+',color='blueviolet',markersize=5,label=''r'$-\lambda\log_2 \lambda$')
for i in range(1,len(data)):
    ax1.plot(data[i],-data[i]*np.log2(data[i]),'+',color='blueviolet',markersize=5)
ax1.set_xlabel(''r'$\lambda$')
ax1.set_ylabel('values')
ax1.set_xlim(0,0.0065)
ax1.set_ylim(0,0.05)
ax1.set_xticks([0.000,0.001,0.002,0.003,0.004,0.005,0.006])
ax1.set_yticks([0.00,0.01,0.02,0.03,0.04,0.05])
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
ax1.set_title('contribution to the entropy')

del data[-1]

ax2.hist(data,bins=np.arange(0, data[-1], data[-1]/500),align='mid',label=''r'$\lambda$',color='blueviolet')
ax2.set_xlabel(''r'$\lambda$')
ax2.set_ylabel('probability density')
ax2.set_xlim(0,0.00105)
ax2.set_ylim(0,250)
ax2.set_xticks([0.0000,0.0002,0.0004,0.0006,0.0008,0.0010])
ax2.set_yticks([0,50,100,150,200,250])

ax2.set_ylabel('number of occurrences')
ax2.set_title(''r'histogram without $\lambda_0$')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

fig.tight_layout() 
fig.savefig('Spectral.pdf')
