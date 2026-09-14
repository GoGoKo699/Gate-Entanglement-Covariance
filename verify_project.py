"""Verify reference integrity and reproduce six deterministic calculations.

Calculations run in a temporary copy. Committed inputs are checked before and
after execution. No state sampling is rerun.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'reference_integrity.json'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_output_directory(path):
    """Resolve an output directory without allowing writes into reference data."""
    output = Path(path).resolve()
    if output == ROOT or ROOT in output.parents:
        build = ROOT / 'build'
        if output != build and build not in output.parents:
            raise SystemExit('Within the repository, outputs must be under build/.')
    return output


def verify_references(files):
    failures = []
    for name, digest in files.items():
        relative = Path(name)
        path = (ROOT / relative).resolve()
        if relative.is_absolute() or '..' in relative.parts or ROOT not in path.parents:
            raise SystemExit(f'Invalid reference path: {name}')
        if not path.is_file() or sha256(path) != digest:
            failures.append(name)
    if failures:
        raise SystemExit('Reference file mismatch: ' + ', '.join(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'build/validation',
                        help='Directory for new validation reports (default: build/validation).')
    args = parser.parse_args()
    output = safe_output_directory(args.output_dir)
    manifest_digest = sha256(MANIFEST)
    files = json.loads(MANIFEST.read_text())['files']
    if not isinstance(files, dict) or not files:
        raise SystemExit('Reference integrity manifest must contain a nonempty files mapping.')
    verify_references(files)
    print(f'Reference files verified: {len(files)}', flush=True)
    output.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    try:
        with tempfile.TemporaryDirectory(prefix='entropy_covariance_verify_') as tmp:
            work = Path(tmp) / 'checks'
            shutil.copytree(ROOT / 'checks', work)
            # The original numerical implementation includes the protocol's
            # byte hash in its result and expects this local filename.
            shutil.copy2(work / 'protocol.txt', work / 'PROTOCOL.md')
            process = subprocess.run([sys.executable, 'reproduce.py'], cwd=work, env=env,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                     text=True)
            (output / 'deterministic_reproduction.log').write_text(process.stdout)
            print(process.stdout, end='', flush=True)
            reproduction = work / 'REPRODUCTION.json'
            if reproduction.exists():
                shutil.copy2(reproduction, output / 'DETERMINISTIC_REPRODUCTION.json')
            if process.returncode:
                raise SystemExit(process.returncode)
            result = json.loads(reproduction.read_text())
            if result['status'] != 'passed' or len(result['checks']) != 6:
                raise SystemExit('Six deterministic calculations did not pass')
    finally:
        verify_references(files)
        if sha256(MANIFEST) != manifest_digest:
            raise SystemExit('Reference integrity manifest changed during reproduction.')
    report = dict(status='passed', reference_files_verified=len(files),
                  reference_manifest_sha256=manifest_digest,
                  python=platform.python_version(),
                  deterministic_checks=len(result['checks']),
                  new_random_states=0,
                  reference_inputs_unchanged=True,
                  scope='Reference integrity and six deterministic calculations. '
                        'Saved sampling results are checked for integrity; '
                        'their sampling campaigns and the proof review are not rerun.')
    (output / 'PROJECT_VERIFICATION.json').write_text(json.dumps(report, indent=2)+'\n')
    print('Reference integrity and deterministic reproduction passed.', flush=True)


if __name__ == '__main__':
    main()
