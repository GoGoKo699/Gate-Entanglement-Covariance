# Entangling-successions

Code and data for numerical experiments on bipartite entanglement of subset states.

This repository is intentionally organized by figure/experiment directory. Each folder stores:
- the script(s) that generate data,
- the generated CSV data,
- the final PDF plot.

## Repository layout

- `QFT/`
- `Renyi/`
- `Spectral/`
- `Partition/`
- `Concentration/`
- `Approximation/`
- `Greedy/`
- `Linear/`

## Environment

Use Python 3.10+ and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
