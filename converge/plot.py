'''
FIG 7
'''
import matplotlib.pyplot as plt
import numpy as np

xdata=np.array([10,12,14,16,18,20,22,24,26,28,30])
ydata=np.array([4.072,5.108,6.143,7.176,8.196,9.215,10.231,11.242,12.251,13.258,14.263])
x=np.linspace(9,31,100)

fig, (ax1, ax2) = plt.subplots(2,figsize=(4.5,8))

ax1.plot(x,x/2-1+0.278,'-',color='skyblue')
ax1.plot(xdata,ydata,'+',color='blueviolet',markersize=7)
ax1.set_xlim([9, 31])
ax1.set_xticks([10,15,20,25,30])
ax1.set_xlabel('n')
ax1.set_ylabel('entropy')
ax1.set_title('compare')

ax2.axhline(y=0,color='skyblue',label=''r'$\frac{n}{2}-cst_0$')
ax2.plot(xdata,ydata-(xdata/2-1+0.278),'+',color='blueviolet',markersize=7,label=''r'$E_n$')
ax2.set_xlim([9, 31])
ax2.set_xticks([10,15,20,25,30])
ax2.set_xlabel('n')
ax2.set_ylabel('entropy')
ax2.set_title('converge')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5)

fig.tight_layout() 
fig.savefig('Converge.pdf')
