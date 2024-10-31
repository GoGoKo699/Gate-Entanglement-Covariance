'''
FIG 3
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

data=[]
with open('Spectral.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter='\t')
     for row in plots:
         data.append(float(row[0]))
         
del data[-1]
        
plt.figure(figsize=(4.5,4))

plt.hist(data,bins=np.arange(0, data[-1], data[-1]/500),align='mid',label=''r'$\lambda$',color='blueviolet')
plt.xlabel(''r'$\lambda$')
plt.ylabel('probability density')
plt.xlim(0,0.00105)
plt.ylim(0,100)
plt.xticks([0.0000,0.0002,0.0004,0.0006,0.0008,0.0010])
plt.yticks([0,25,50,75,100])
plt.xlabel('eigenvalues')
plt.ylabel('number of occurrences')
plt.title(''r'histogram without $\lambda_0$')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.tight_layout() 
plt.savefig('Spectral.pdf')
