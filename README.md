# Gate Entanglement Covariance

**How much of a state's entanglement fluctuation survives a gate acting across a small boundary?**

Take a random pure state of two large quantum systems. Apply a fixed gate to a small part of each system, then compare the entanglement before and after the gate. Averaging over Haar-random input states gives the same mean entropy at both times. The question is whether a state that starts above the mean tends to remain above it.

The central result relates that correlation to the gate's **operator Schmidt spectrum**. For balanced growing systems and fixed boundary access, this spectrum determines the limiting covariance of every fixed positive-order Rényi entropy, including von Neumann entropy and pure-state logarithmic negativity.

Three consequences make the relation useful:

- A gate with fixed spatial access leaves a positive limiting same-order entropy correlation. For a boundary qubit pair, the minimum Rényi-2 correlation is **1/4**.
- Gates with the same operator purity can retain different correlations at other entropy orders.
- An ideal hierarchy of integer-order entropy covariances identifies the operator Schmidt probabilities, although its poor conditioning limits practical reconstruction.

The absolute entropy fluctuations shrink as the half-dimension grows. The theorem concerns their rescaled covariance. Its input ensemble is complex Haar; the tested Floquet-eigenstate extension did not follow the same law.

![Predicted entropy correlation under a fixed boundary ZZ gate](figures/entropy_memory.png)

The curves are analytical large-d predictions for a boundary ZZ gate. Horizontal lines give the minima attained by an active-qubit SWAP. [Understand this example](docs/WORKED_EXAMPLE.md), or [regenerate the figure](REPRODUCE.md). The figure adds no random-state samples.

## Read the story

**One background tutorial:** James A. Mingo and Roland Speicher,
*Free Probability and Random Matrices* (2017). The [selected passages and reading
map](docs/START_HERE.md#selected-reading) use the verified author PDF, not
published-book page numbers. The repository supplies the quantum-information
dictionary and the gate-dependent argument. Primary research sources remain
credited proof inputs, not additional prerequisite tutorials.

| Route | Where to go |
|---|---|
| **LEARN** | [Physical setup and selected reading](docs/START_HERE.md) → [book-to-project bridge](docs/TUTORIAL_BRIDGE.md) → [complete gate calculation](docs/WORKED_EXAMPLE.md) → [results and evidence](docs/RESULTS.md) |
| **CHECK** | Go directly to [the theorem](theory/THEOREM.md), [derivation and hypotheses](theory/PROOF.md), [claim ledger](CLAIM_LEDGER.md), [primary attribution](docs/REFERENCES.md), and [evidence](docs/RESULTS.md). No educational detour is required. |
| **REPRODUCE** | Run the [focused commands](REPRODUCE.md) to check maintained calculations and frozen evidence and regenerate the analytical figure. |

For a specific question:

| Question | Read |
|---|---|
| What is being compared, and why is it interesting? | [Start here](docs/START_HERE.md) |
| How does Wishart fluctuation theory become a quantum entropy prediction? | [Tutorial bridge](docs/TUTORIAL_BRIDGE.md) |
| What happens for an actual two-qubit gate? | [Worked example](docs/WORKED_EXAMPLE.md) |
| What exactly is the theorem? | [Setting and result](theory/THEOREM.md) |
| How do product gates, SWAP, local basis changes, and different times fit? | [Gate controls and limiting cases](theory/CONTROLS.md) |
| Why does the operator Schmidt spectrum appear? | [Technical derivation and proof dependencies](theory/PROOF.md) |
| What supports each claim, and where does the theory fail? | [Results and evidence](docs/RESULTS.md), [claim ledger](CLAIM_LEDGER.md) |
| Which parts build on prior work? | [References and attribution](docs/REFERENCES.md) |

This is a standalone research repository. The explanatory route does not require a manuscript or earlier conversations. The theorem and its supporting arguments have received internal review; the numerical checks illustrate and calibrate the result within their recorded limits.

## Run the focused reproduction

Use Python 3.12:

```sh
python -m pip install -r requirements.txt
python scripts/reproduce.py
```

The command checks the maintained calculations against saved exact results, verifies the imported evidence, runs the six existing deterministic checks, and generates the reader figure and table under `build/reproduction/`. The frozen research records stay unchanged. [Reproduction details](REPRODUCE.md) distinguish this default calculation from optional sampling and figure scripts.

## Work with the repository

| Location | Role |
|---|---|
| `docs/`, `theory/` | Maintained explanation, theorem, derivation, and evidence map |
| `gate_covariance/`, `scripts/` | Maintained calculations and reproduction entry points |
| `figures/`, `results/` | Small reference outputs for the reader example |
| `evidence/`, `limits/` | Frozen supporting research and the unsuccessful extension |
| `provenance/`, `reviews/`, `legacy/` | Source records, internal assessments, and preserved repository history |

See the [repository map](docs/REPOSITORY_MAP.md) for exact responsibilities and the [handover](HANDOVER.md) for future work. [The roadmap](NEXT.md) puts repository refurnishing before manuscript preparation; [the paper outline](PAPER_OUTLINE.md) is reserved for the final phase.

The current GitHub name is **Entangling-successions**. Its former subset-state work was upgraded into [Subset-states](https://github.com/GoGoKo699/Subset-states), and this repository now hosts one active covariance project. The former contents are preserved, with the transition documented in [provenance](provenance/REPOSITORY_TRANSITION.md). A subset-ensemble extension of the covariance theorem remains unproved.
