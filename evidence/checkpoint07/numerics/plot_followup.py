"""Compare the separately frozen finite-time series to fresh state data."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from finite_time_followup import prediction, ORDERS

ROOT=Path(__file__).resolve().parent
summary=json.loads((ROOT/'followup_results/summary.json').read_text())
times=np.array(summary['frozen']['times'])
grid=np.linspace(.03,.43,150)
model=prediction(grid,K=65536)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160})
fig,axes=plt.subplots(1,3,figsize=(11.8,3.9),layout='constrained')
for ax,j in zip(axes,[0,1,3]):
    ax.plot(grid,model[:,j],color='#333333',label='Predicted large-d limit')
    for row,col,mark in zip(summary['rows'],['#d27b20','#225f91'],['s','o']):
        mean=np.array(row['mean']);se=np.array(row['standard_error'])
        ax.errorbar(times,mean[:,j],yerr=se[:,j],fmt=mark,ms=5,capsize=3,color=col,
                    label=f"d = {row['d']}; 128 fresh states")
    ax.set(xlabel=r'Pulse duration $\tau$',ylabel=r'$D\,\langle(\Delta S_\alpha)^2\rangle$',
           title=f'α = {ORDERS[j]:g}',xlim=(.02,.45))
    ax.grid(alpha=.15)
axes[0].legend(frameon=False,fontsize=8)
fig.suptitle('Finite-pulse prediction tested on an independent cohort',fontsize=13)
fig.savefig(ROOT/'figures/finite_time_fresh_check.png',dpi=180)
fig.savefig(ROOT/'figures/finite_time_fresh_check.pdf')
