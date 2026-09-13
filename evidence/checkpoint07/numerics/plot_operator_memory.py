"""Analytical gate comparison and the retained finite-state pilot; no new states."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from finite_time_followup import coefficients
from operator_memory import increment_prediction

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'figures'
OUT.mkdir(exist_ok=True)
ORDERS=np.array([.125,.25,.5,1.,2.])
blue='#214e78';teal='#177f83';gray='#606b75'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,
    'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold'})

p=(1+np.sqrt(np.sqrt(2)-1))/2
etas={'A':[.5,.5],'C':[p*p,p*(1-p),p*(1-p),(1-p)**2]}
cov={}
for name,eta in etas.items():
    values=[]
    for alpha in ORDERS:
        k,c,_=coefficients(float(alpha),32768)
        F=np.sum(np.asarray(eta)[:,None]**k[None,:],axis=0)
        values.append(float(.25*np.sum(k*c*c*F)))
    cov[name]=values
analytic=dict(p=float(p),operator_weights=etas,orders=ORDERS.tolist(),
    covariance=cov,meaning='Large-d covariance d² Cov(S_alpha(U psi),S_alpha(psi)); analytical series only.',
    comparison='Equal F2; strict higher power-sum ordering is proved in DIAGONAL_GATE_THEORY.md.')
(ROOT/'operator_results/equal_purity_analytic.json').write_text(json.dumps(analytic,indent=2)+'\n')

summary=json.loads((ROOT/'operator_results/summary.json').read_text())
fig,ax=plt.subplots(1,3,figsize=(13.8,4.5),layout='constrained')
x=np.arange(5);w=.34
ax[0].bar(x-w/2,cov['A'],width=w,color=blue,label='Gate A: two weights')
ax[0].bar(x+w/2,cov['C'],width=w,color=teal,label='Gate C: four weights')
ax[0].set(xticks=x,xticklabels=['1/8','1/4','1/2','1','2'],xlabel=r'Rényi order $\alpha$',
    ylabel=r'$\lim d^2\,\mathrm{Cov}(S_\alpha(U\psi),S_\alpha(\psi))$',
    title='Same operator purity, different memory')
ax[0].legend(frameon=False,fontsize=8,loc='upper left')
ax[0].text(.03,.67,'Both operator purities = 1/2\nAnalytical predictions',
    transform=ax[0].transAxes,fontsize=8,color=gray)

t=np.linspace(0,np.pi/2,401)
ax[1].plot(t,1-np.cos(t)**4-np.sin(t)**4,color=blue,label='A: product gate at π/2')
ax[1].plot(t,1-np.cos(t)**4-.5*np.sin(t)**4,color=teal,label='B: entangling gate at π/2')
row=next(r for r in summary['rows'] if r['d']==128)
means=np.array(row['mean']);se=np.array(row['standard_error'])
for j,color in enumerate([blue,teal]):
    ax[1].errorbar([np.pi/4,np.pi/2],means[j,:,4],yerr=se[j,:,4],fmt='o',
        color=color,capsize=3,ms=4)
ax[1].set(xticks=[0,np.pi/4,np.pi/2],xticklabels=['0','π/4','π/2'],
    xlabel='Pulse time',ylabel=r'$d^2\,\mathbb{E}(\Delta S_2)^2$',
    title='Matched energies: recurrence contrast')
ax[1].legend(frameon=False,fontsize=8,loc='upper left')
ax[1].text(.02,.48,'Curves: dimension limit\nPoints: d = 128, 64 states\nBars: one sample SE',
    transform=ax[1].transAxes,fontsize=8,color=gray,bbox=dict(facecolor='white',edgecolor='none',alpha=.9))

target=np.array(summary['frozen']['predictions']['B'])[0]
for j,(row,color) in enumerate(zip(summary['rows'],[blue,teal])):
    y=np.array(row['mean'])[1,0]/target
    e=np.array(row['standard_error'])[1,0]/target
    ax[2].errorbar(x+(j-.5)*.14,y,yerr=e,fmt='o',capsize=3,ms=4,color=color,label=f"d = {row['d']}")
ax[2].axhline(1,color=gray,lw=1,ls='--')
ax[2].set(xticks=x,xticklabels=['1/8','1/4','1/2','1','2'],xlabel=r'Rényi order $\alpha$',
    ylabel='Measured increment / limiting prediction',title='Finite-size deviations retained',ylim=(0.25,1.9))
ax[2].legend(frameon=False,fontsize=8,loc='upper left')
ax[2].text(.97,.94,'Gate B at π/4\n64 states per size',transform=ax[2].transAxes,
    fontsize=8,color=gray,va='top',ha='right')
for a in ax:
    a.grid(axis='y',alpha=.15);a.set_axisbelow(True)
fig.savefig(OUT/'operator_memory_comparison.png',dpi=180)
fig.savefig(OUT/'operator_memory_comparison.pdf')
print(json.dumps(analytic,indent=2))
