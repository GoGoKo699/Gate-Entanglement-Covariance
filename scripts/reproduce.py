#!/usr/bin/env python3
"""Run focused validation and regenerate the analytical reader examples.

All new outputs go below --output-dir (default: build/reproduction in the
repository). Committed reference data and example artifacts stay untouched.
No Haar or Floquet sample generation is rerun.
"""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
# Set before importing numerical libraries. Single-thread execution also
# avoids starting large thread pools for these small deterministic checks.
for variable in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[variable] = "1"

from gate_covariance.examples import reader_examples
from gate_covariance.plotting import plot_entropy_memory
from verify_project import safe_output_directory


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT/"build/reproduction")
    args = parser.parse_args()
    output = safe_output_directory(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(ROOT/"verify_project.py"),
                    "--output-dir", str(output/"validation")], check=True)
    subprocess.run([sys.executable, str(ROOT/"scripts/check_calculations.py"),
                    "--output", str(output/"validation/maintained_calculations.json")], check=True)
    data = reader_examples()
    (output/"results").mkdir(exist_ok=True)
    (output/"results/reader_examples.json").write_text(json.dumps(data, indent=2)+"\n")
    plot_entropy_memory(output/"figures", cutoff=data["cutoff"])
    print(f"Focused reproduction passed. Outputs: {output}")


if __name__ == "__main__":
    main()
