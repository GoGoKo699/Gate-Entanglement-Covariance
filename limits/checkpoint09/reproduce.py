"""Reproduce checkpoint09 without extending its scientific sample."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import sys
import time
import numpy as np
import scipy

ROOT=Path(__file__).resolve().parent


def close_tree(a,b):
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(close_tree(a[k],b[k]) for k in a if k!='elapsed_seconds')
    if isinstance(a,list):
        return len(a)==len(b) and all(close_tree(x,y) for x,y in zip(a,b))
    if isinstance(a,bool) or a is None:
        return a==b
    if isinstance(a,(int,float)):
        return bool(np.isclose(a,b,rtol=1e-9,atol=1e-11))
    return a==b


def main():
    original={N:json.loads((ROOT/f'results/summary_N{N}.json').read_text()) for N in [8,10]}
    reference={N:{k:v.copy() for k,v in np.load(ROOT/f'results/cohort_N{N}.npz').items()}
               for N in [8,10]}
    (ROOT/'reproduction_logs').mkdir(exist_ok=True)
    checks=[]
    for source in ['theory/haar_predictions.py','floquet_test.py','reviews/independent_audit.py','plot_results.py']:
        start=time.monotonic()
        proc=subprocess.run([sys.executable,source],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (ROOT/'reproduction_logs'/f'{Path(source).stem}.log').write_text(proc.stdout)
        checks.append(dict(source=source,exit_code=proc.returncode,seconds=round(time.monotonic()-start,3)))
        print(source,'PASS' if proc.returncode==0 else 'FAIL',flush=True)
        if proc.returncode!=0:
            print(proc.stdout)
            raise RuntimeError('Reproduction check failed; retain the result.')
    arrays=[]
    for N in [8,10]:
        current=dict(np.load(ROOT/f'results/cohort_N{N}.npz'))
        row={'N':N,'arrays':{}}
        for k,v in reference[N].items():
            delta=float(np.max(abs(current[k]-v)))
            # Eigenvectors have an arbitrary phase. Compare all scalar/physical
            # arrays directly; separately compare eigenvectors phase-insensitively.
            if k=='eigenvectors':
                overlap=np.sum(v.conj()*current[k],axis=0)
                aligned=current[k]*np.exp(-1j*np.angle(overlap))[None,:]
                error=float(np.max(np.linalg.norm(v-aligned,axis=0)))
                passed=error<1e-8
                row['arrays'][k]=dict(maximum_phase_aligned_column_error=error,identical_bytes=v.tobytes()==current[k].tobytes(),passed=passed)
            else:
                passed=bool(np.allclose(v,current[k],rtol=1e-9,atol=1e-11))
                row['arrays'][k]=dict(maximum_absolute_difference=delta,identical_bytes=v.tobytes()==current[k].tobytes(),passed=passed)
            assert passed,(N,k)
        summary=json.loads((ROOT/f'results/summary_N{N}.json').read_text())
        row['summary_matches_excluding_wall_time']=close_tree(original[N],summary)
        assert row['summary_matches_excluding_wall_time']
        arrays.append(row)
    result=dict(status='passed',environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                checks=checks,cohort_comparisons=arrays,
                protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
                predictions_sha256=hashlib.sha256((ROOT/'results/predictions.json').read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256((ROOT/'floquet_test.py').read_bytes()).hexdigest(),
                scope='Same frozen two sizes and gates. No new circuit realizations, state samples, or comparison criteria.')
    (ROOT/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All physical arrays and summaries match the saved reference.',flush=True)


if __name__=='__main__':main()
