"""Descriptive summaries and scientific figure. No exponent fits or exclusions."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import gamma
from run_experiment import ORDERS, SIZES, entropy

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'

def bulk_constant(alpha,c):
    if c==1:
        if alpha<=.25: return None
        if alpha==1: return 2*(np.pi**2/3-11/4)
        moment=lambda p:4**p*gamma(p+.5)/(np.sqrt(np.pi)*gamma(p+2))
        return float(2*(alpha/(1-alpha))**2*(moment(2*alpha-1)/moment(alpha)**2-1))
    lo=(1-np.sqrt(c))**2; hi=(1+np.sqrt(c))**2
    rho=lambda x:np.sqrt(max(0,(hi-x)*(x-lo)))/(2*np.pi*c*x)
    moment=lambda p:quad(lambda x:rho(x)*x**p,lo,hi,epsabs=1e-12)[0]
    if alpha==1:
        mean=quad(lambda x:x*rho(x)*np.log(x),lo,hi,epsabs=1e-12)[0]
        return 2*quad(lambda x:x*rho(x)*(np.log(x)-mean)**2,lo,hi,epsabs=1e-12)[0]
    return float(2*(alpha/(1-alpha))**2*(moment(2*alpha-1)/moment(alpha)**2-1))

rows=[]
for d in SIZES:
    for cut in ['balanced','shifted']:
        x=np.load(OUT/f'haar_d{d}_{cut}.npz')
        vv=d*d*np.diagonal(x['covariance'],axis1=1,axis2=2)
        rates=x['rates'][:64]; times=x['durations']; change=x['changes']
        secant=(change[:,:,0,:]-change[:,:,1,:])/(2*times[None,:,None])
        denom=np.median(np.abs(rates),axis=0)
        err=np.median(np.abs(secant-rates[:,None,:]),axis=0)/denom[None,:]
        entropies=np.array([entropy(lam) for lam in x['spectra']])
        row=dict(d=d,global_dimension=d*d,total_qubits=int(np.log2(d*d)),
             cut=cut,a=int(x['a']),b=int(x['b']),states=len(x['spectra']),
             scaled_conditional_variance_quantiles=np.quantile(vv,[.25,.5,.75],axis=0).tolist(),
             smallest_probability=float(x['spectra'].min()),
             max_normalization_error=float(np.max(np.abs(x['spectra'].sum(axis=1)-1))),
             max_trace_derivative_error=float(np.max(np.abs(x['trace_errors']))),
             D_times_sample_static_entropy_variance=(d*d*entropies.var(axis=0,ddof=1)).tolist(),
             finite_pulse=dict(states=64,durations=times.tolist(),
                symmetric_rate_error_ratio=err.tolist(),
                definition='median(abs((S(t)-S(-t))/(2t)-rate))/median(abs(rate))',
                absolute_derivative_median=denom.tolist(),
                D_times_mean_squared_changes=(d*d*np.mean(change**2,axis=0)).tolist(),
                mean_changes=np.mean(change,axis=0).tolist(),
                change_standard_error=(np.std(change,axis=0,ddof=1)/8).tolist(),
                median_abs_forward_rate_ratio=(np.median(np.abs(change[:,:,0,:]),axis=0)/times[:,None]/denom[None,:]).tolist()))
        rows.append(row)
summary=dict(orders=ORDERS.tolist(),states_total=1280,cut_observations=2560,
    pulse_global_states=320,pulse_cut_observations=640,finite_pulse_entropy_evaluations=5120,
    exclusions=0,rows=rows,
    bulk_limits={cut:[bulk_constant(float(alpha),c) for alpha in ORDERS]
                 for cut,c in [('balanced',1),('shifted',.25)]},
    critical_log_coefficient=float(4/(9*np.pi*(4**.25*gamma(.75)/(np.sqrt(np.pi)*gamma(2.25)))**2)),
    validation=json.loads((OUT/'validation.json').read_text()),
    interpretation='Finite-size descriptive check. No fitted exponent, population fourth-moment error bars for low-order rates, or finite-time scaling theorem.')
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                    'figure.dpi':160,'savefig.dpi':180})
fig,axs=plt.subplots(1,3,figsize=(13.4,4.2),layout='constrained')
colors={'balanced':'#225f91','shifted':'#d27b20'}
for cut in ['balanced','shifted']:
    rr=[r for r in rows if r['cut']==cut]
    quant=np.array([r['scaled_conditional_variance_quantiles'] for r in rr])
    axs[0].plot(SIZES,quant[:,1,0],'o-',color=colors[cut],label=cut.capitalize())
    axs[0].fill_between(SIZES,quant[:,0,0],quant[:,2,0],alpha=.16,color=colors[cut])
axs[0].set(xscale='log',yscale='log',xlabel='Balanced-cut dimension d',ylabel=r'$D\,V_{1/8}(\lambda)$',
           title='A  Low-order response differs by cut')
axs[0].legend(frameon=False)
rr=[r for r in rows if r['cut']=='balanced']
quant=np.array([r['scaled_conditional_variance_quantiles'] for r in rr])
for j,col in [(1,'#a74765'),(2,'#207c73'),(3,'#424242')]:
    axs[1].plot(SIZES,quant[:,1,j],'o-',color=col,label=f'α = {ORDERS[j]:g}')
    axs[1].fill_between(SIZES,quant[:,0,j],quant[:,2,j],color=col,alpha=.12)
    limit=summary['bulk_limits']['balanced'][j]
    if limit is not None: axs[1].axhline(limit,color=col,lw=.8,ls=':')
axs[1].set(xscale='log',xlabel='Balanced-cut dimension d',ylabel=r'$D\,V_\alpha(\lambda)$',
           title='B  Quarter-order growth; ordinary plateaus')
axs[1].legend(frameon=False)
for cut,j,col,label in [('balanced',0,'#225f91','Balanced, α = 1/8'),
                         ('shifted',0,'#d27b20','Shifted, α = 1/8'),
                         ('balanced',3,'#424242','Balanced, α = 1')]:
    rr=[r for r in rows if r['cut']==cut]
    err=np.array([r['finite_pulse']['symmetric_rate_error_ratio'] for r in rr])
    axs[2].plot(SIZES,err[:,1,j],'o-',color=col,label=label)
rr=[r for r in rows if r['cut']=='balanced']
err=np.array([r['finite_pulse']['symmetric_rate_error_ratio'] for r in rr])
axs[2].plot(SIZES,err[:,2,0],'o--',color='#225f91',label=r'Balanced, α = 1/8; $\tau=0.1/\sqrt{d}$')
axs[2].set(xscale='log',yscale='log',xlabel='Balanced-cut dimension d',ylabel='Symmetric rate error / rate scale',
           title='C  Fixed-pulse error grows at low orders')
axs[2].legend(frameon=False,fontsize=8,loc='upper left')
for ax in axs:
    ax.set_xticks(SIZES,labels=[str(d) for d in SIZES]);ax.grid(alpha=.15)
fig.suptitle('A bounded local ZZ probe on Haar states: finite-size diagnostics',fontsize=13)
figure_dir=ROOT/'figures';figure_dir.mkdir(exist_ok=True)
fig.savefig(figure_dir/'response_and_resolution.png')
fig.savefig(figure_dir/'response_and_resolution.pdf')
print(json.dumps({'bulk_limits':summary['bulk_limits'],
 'critical_log_coefficient':summary['critical_log_coefficient'],
 'maximum_normalization_error':max(r['max_normalization_error'] for r in rows),
 'smallest_probability':min(r['smallest_probability'] for r in rows)},indent=2))
