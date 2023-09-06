'''
FIG 3
'''
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

n=[10,12,14,16,18,20,22,24,26,28,30]
one_prime=[3.1900,4.0220,4.8993,5.7872,6.6748,7.5574,8.4428,9.3301,10.2159,11.1018,11.9876]
two_prime=[3.2805,4.0362,4.7394,5.4738,6.2088,6.9507,7.6911,8.4385, 9.1880, 9.9403,10.6951]
thr_prime=[3.5479,4.3220,5.0647,5.7927,6.5139,7.2236,7.9293,8.6368, 9.3452,10.0553,10.7669]

sum_oftwo=[2.1213,2.7553,3.3840,4.0189,4.6650,5.3166,5.9725,6.6329, 7.2969, 7.9635, 8.6325]
sum_three=[1.1528,1.5758,1.9895,2.4183,2.8470,3.2828,3.7224,4.1672, 4.6171, 5.0713, 5.5298]

def f(x,a,b):
    return a*x+b

popt1, pcov1 = curve_fit(f,n[-2:],one_prime[-2:],maxfev = 100000000)
a1,b1=popt1
print('1',round(2*a1,3),round(b1,3))
popt2, pcov2 = curve_fit(f,n[-2:],two_prime[-2:],maxfev = 100000000)
a2,b2=popt2
print('2',round(2*a2,3),round(b2,3))
popt3, pcov3 = curve_fit(f,n[-2:],thr_prime[-2:],maxfev = 100000000)
a3,b3=popt3
print('3',round(2*a3,3),round(b3,3))
popt12, pcov12 = curve_fit(f,n[-2:],sum_oftwo[-2:],maxfev = 100000000)
a12,b12=popt12
print('12',round(2*a12,3),round(b12,3))
popt123, pcov123 = curve_fit(f,n[-2:],sum_three[-2:],maxfev = 100000000)
a123,b123=popt123
print('123',round(2*a123,3),round(b123,3))

x=np.linspace(9,31)

plt.figure(1,figsize=(4.5,4.2))

plt.plot(x,a1*x+b1,'k-',linewidth=1,alpha=0.2)
plt.plot(n,one_prime,'kP',markersize=5,label=''r'$\mathbb{P}$',alpha=0.5)

plt.plot(x,a2*x+b2,'-',color='darkgreen',linewidth=1,alpha=0.2)
plt.plot(n,two_prime,'^',color='darkgreen',markersize=5,label=''r'$\mathbb{P}_2$',alpha=0.5)

plt.plot(x,a3*x+b3,'-',color='forestgreen',linewidth=1,alpha=0.2)
plt.plot(n,thr_prime,'s',color='forestgreen',markersize=5,label=''r'$\mathbb{P}_3$',alpha=0.5)

#plt.plot(x,a4*x+b4,'-',color='darkgreen',linewidth=1,alpha=0.2)
#plt.plot(n,thr_prime,'p',color='limegreen',markersize=5,label=''r'$\mathbb{P}_4$',alpha=0.5)

plt.title('k-almost Prime states')
plt.xlabel('n')
plt.xlim(9,31)
plt.ylim(0,13)
plt.xticks([10,15,20,25,30])
plt.yticks([0,2,4,6,8,10,12])
plt.ylabel('entropy')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5, fontsize= 9)
plt.tight_layout()
plt.savefig('Prime.pdf')

plt.figure(2,figsize=(4.5,4.2))

plt.plot(x,a1*x+b1,'k-',linewidth=1,alpha=0.2)
plt.plot(n,one_prime,'kP',markersize=5,label=''r'$\mathbb{U}$',alpha=0.5)

plt.plot(x,a12*x+b12,'-',color='dimgray',linewidth=1,alpha=0.2)
plt.plot(n,sum_oftwo,'^',color='dimgray',markersize=5,label=''r'$\mathbb{U}_2$',alpha=0.5)

plt.plot(x,a123*x+b123,'-',color='gray',linewidth=1,alpha=0.2)
plt.plot(n,sum_three,'s',color='gray',markersize=5,label=''r'$\mathbb{U}_3$',alpha=0.5)

#plt.plot(x,a1234*x+b1234,'-',color='silver',linewidth=1,alpha=0.2)
#plt.plot(n,sum_four,'p',color='silver',markersize=5,label=''r'$\mathbb{U}_4$',alpha=0.5)

plt.title('unions of k-almost Prime states')
plt.xlabel('n')
plt.xlim(9,31)
plt.ylim(0,13)
plt.xticks([10,15,20,25,30])
plt.yticks([0,2,4,6,8,10,12])
plt.ylabel('entropy')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=5, fontsize= 9)
plt.tight_layout()
plt.savefig('Union.pdf')
