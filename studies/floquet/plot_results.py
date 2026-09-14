"""Standalone scientific figure from saved checkpoint-09 observations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'results/predictions.json').read_text())
data={N:json.loads((ROOT/f'results/summary_N{N}.json').read_text()) for N in [8,10]}
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10,4.2),layout='constrained')
ratios=[data[N]['entropy']['identity'][1]['exact_haar_variance_before_ratio'] for N in [8,10]]
axes[0].bar([0,1],ratios,width=.55,color=['#7592b7','#335f91'])
axes[0].axhline(1,color='#222222',ls='--',lw=1.3,label='Exact finite-size Haar value')
for x,y in enumerate(ratios):axes[0].text(x,y+.18,f'{y:.2f}',ha='center',va='bottom')
axes[0].set(xticks=[0,1],xticklabels=['8 spins','10 spins'],ylim=(0,9.3),
            ylabel='Variance / exact Haar variance',title='(a) Von Neumann entropy fluctuations')
axes[0].legend(frameon=False,loc='upper right',fontsize=9)
x=np.arange(3)
haar=[r['correlation'] for r in p['gates']['SWAP']['entropy']]
axes[1].plot(x,haar,'o--',color='#222222',lw=1.4,label='Haar limit, both probes')
for gate,color,marker,label in [('SWAP','#247a9b','o','SWAP'),('phaseSWAP','#c06a37','s','SWAP + ZZ phase')]:
    axes[1].plot(x,[r['correlation'] for r in data[10]['entropy'][gate]],marker+'-',color=color,lw=1.5,label=label)
axes[1].set(xticks=x,xticklabels=['1/2','1','2'],ylim=(0,1),xlabel='Rényi order',
            ylabel='Before/after Pearson correlation',title='(b) Independent probes, 10 spins')
axes[1].legend(frameon=False,fontsize=9,loc='lower right')
fig.suptitle('Floquet eigenstates fail the declared Haar comparison',fontsize=14)
(ROOT/'figures').mkdir(exist_ok=True)
for extension in ['png','svg']:
    fig.savefig(ROOT/f'figures/floquet_comparison.{extension}',dpi=200)
plt.close(fig)
print('Saved PNG and SVG from the frozen cohort results.')
