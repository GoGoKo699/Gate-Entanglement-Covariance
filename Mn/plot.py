'''
FIG 2
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

xdata=np.array([10,12,14,16,18,20,22,24,26,28,30])
ydata=np.array([107,276,716,1873,4934,13091,34771,93018,250660,672556,1836685])
x=np.linspace(9,31,100)

def f(x,a,b):
    return a*x+b

popt, pcov = curve_fit(f,xdata,np.log2(ydata),maxfev = 100000000)
a,b=popt
print(a,b)

plt.figure(figsize=(4.5,4.2))

x=np.linspace(9,31,100)

plt.plot(x,f(x,a,b),'-',color='gray',markersize=2,label='Linear fit',alpha=0.5)
plt.plot(xdata,np.log2(ydata),'+',color='blueviolet',markersize=7,label=''r'$\log_2 M_n$')

plt.xlim([9, 31])
plt.xticks([10,15,20,25,30])
plt.ylim([6, 22])
plt.yticks([6,8,10,12,14,16,18,20,22])

plt.xlabel('n')
plt.ylabel('values')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('M_n.pdf')
