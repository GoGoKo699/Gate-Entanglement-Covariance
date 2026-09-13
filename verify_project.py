"""Verify immutable inputs and reproduce only the six checkpoint-08 checks.

The imported checkpoints are never modified. No Haar sampling is rerun.
"""
from pathlib import Path
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    imports = json.loads((ROOT / 'provenance/IMPORTS.json').read_text())
    files = imports['imported_files']
    failures = [name for name, digest in files.items()
                if not (ROOT / name).is_file() or sha256(ROOT / name) != digest]
    if failures:
        raise SystemExit('Imported file mismatch: ' + ', '.join(failures))
    print(f'Imported files verified: {len(files)}', flush=True)
    output = ROOT / 'validation'
    output.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='entropy_quantum_verify_') as tmp:
        work = Path(tmp) / 'checkpoint08'
        shutil.copytree(ROOT / 'evidence/checkpoint08', work)
        process = subprocess.run([sys.executable, 'reproduce.py'], cwd=work, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True)
        (output / 'deterministic_reproduction.log').write_text(process.stdout)
        print(process.stdout, end='', flush=True)
        reproduction = work / 'REPRODUCTION.json'
        if reproduction.exists():
            shutil.copy2(reproduction, output / 'CHECKPOINT08_REPRODUCTION.json')
        if process.returncode:
            raise SystemExit(process.returncode)
        result = json.loads(reproduction.read_text())
        if result['status'] != 'passed':
            raise SystemExit('Deterministic reproduction did not pass')
    # Check that the reproduction really left every imported reference untouched.
    assert all(sha256(ROOT / name) == digest for name, digest in files.items())
    report = dict(status='passed', imported_files_verified=len(files),
                  python=platform.python_version(),
                  deterministic_checks=len(result['checks']),
                  new_random_states=0,
                  original_inputs_unchanged=True,
                  scope='Input integrity and six checkpoint-08 deterministic checks only; '
                        'earlier sampling and proof audits are inherited evidence.')
    (output / 'PROJECT_VERIFICATION.json').write_text(json.dumps(report, indent=2)+'\n')
    print('Project migration verification passed.', flush=True)


if __name__ == '__main__':
    main()
