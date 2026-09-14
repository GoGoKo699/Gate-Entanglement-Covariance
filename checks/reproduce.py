"""Run the six declared deterministic checks and compare saved JSON results."""
from pathlib import Path
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
CHECKS = [
    ('inverse/inverse_moments.py', 'inverse/inverse_results.json'),
    ('finite_purity/check_exact_global_purity.py', 'finite_purity/exact_global_purity_results.json'),
    ('finite_purity/check_two_cut_modes.py', 'finite_purity/two_cut_modes_results.json'),
    ('symbolic/two_cut_symbolic_audit.py', 'symbolic/two_cut_symbolic_audit.json'),
    ('numerics/two_cut_check.py', 'results/two_cut_check.json'),
    ('numerics/design_pair.py', 'results/design_pair.json'),
]


def equivalent(a, b):
    """Allow platform roundoff; require identical structure and labels."""
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is type(b) and a == b
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        return math.isclose(a, b, rel_tol=1e-10, abs_tol=5e-11)
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(equivalent(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(equivalent(x, y) for x, y in zip(a, b))
    return a == b


def main():
    import numpy
    import scipy
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    logs = ROOT / 'reproduction_logs'
    logs.mkdir(exist_ok=True)
    rows = []
    for script, result in CHECKS:
        reference = (ROOT / result).read_bytes()
        start = time.monotonic()
        process = subprocess.run([sys.executable, script], cwd=ROOT, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        (logs / (Path(script).stem + '.log')).write_text(process.stdout)
        current = (ROOT / result).read_bytes()
        row = dict(script=script, result=result, exit_code=process.returncode,
                   elapsed_seconds=round(time.monotonic()-start, 3),
                   identical_bytes=reference == current,
                   matches_reference=equivalent(json.loads(reference), json.loads(current)),
                   output_sha256=hashlib.sha256(current).hexdigest())
        rows.append(row)
        print(script, 'PASS' if process.returncode == 0 and row['matches_reference'] else 'FAIL',
              'identical JSON bytes:', row['identical_bytes'], flush=True)
        if process.returncode != 0:
            print(process.stdout, flush=True)
    passed = all(x['exit_code'] == 0 and x['matches_reference'] for x in rows)
    report = dict(status='passed' if passed else 'failed', python=platform.python_version(),
                  numpy=numpy.__version__, scipy=scipy.__version__, checks=rows,
                  comparison='JSON values: rel_tol=1e-10, abs_tol=5e-11; exact structure and text. Each check also has its own stricter internal assertions. Byte identity is reported separately.',
                  scope='Six deterministic calculations only. No state-sampling campaign is rerun.')
    (ROOT / 'REPRODUCTION.json').write_text(json.dumps(report, indent=2)+'\n')
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
