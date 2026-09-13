'''
FIG 2
'''
import matplotlib.pyplot as plt
import numpy as np

Xdata=np.array([10,12,14,16,18,20,22,24,26,28,30])
Mdata=np.array([107,276,716,1873,4934,13091,34771,93018,250660,672556,1836685])
Edata=np.array([4.072,5.108,6.143,7.176,8.196,9.215,10.231,11.242,12.251,13.258,14.263])
x=np.linspace(9,31,100)

plt.figure(figsize=(4.5,4))

x=np.linspace(9,31,100)

plt.plot(x,0.703*x-0.357,'--',color='blueviolet',markersize=2,alpha=0.7)
plt.plot(Xdata,np.log2(Mdata),'+',color='blueviolet',markersize=8,label=''r'$\log_2 M_n$')

plt.plot(x,0.509*x-0.990,'--',color='forestgreen',markersize=2,alpha=0.7)
plt.plot(Xdata,Edata,'*',color='forestgreen',markersize=8,label=''r'$E_n$')

plt.xlim([9, 31])
plt.xticks([10,15,20,25,30])
plt.ylim([0, 22])
plt.yticks([0,5,10,15,20])
plt.title('linear regressions')

plt.xlabel('n')
plt.ylabel('values')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

plt.tight_layout() 
plt.savefig('Linear.pdf')
