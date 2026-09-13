# Gate Entanglement Covariance

**How much entanglement correlation survives a gate acting on a small boundary region?**

This repository develops one paper, provisionally titled **Operator Schmidt spectra and entanglement covariance under local gates**, with Quantum as the current publication target. Its central result is a derived covariance theorem for balanced complex-Haar states and deterministic gates of fixed boundary support. The proof has received internal review. The current phase is repository refurnishing: make the scientific story, theory, evidence, and reproduction path clear without requiring a manuscript. Manuscript drafting is the final phase.

For a relative gate V, let η_j be its normalized operator Schmidt probabilities. The limiting covariance of any fixed positive pair of Rényi orders is

```math
\lim_{d\to\infty}d^2\operatorname{Cov}
\bigl(S_\alpha(U_\ell\psi),S_\beta(U_m\psi)\bigr)
=\frac14\sum_{k\ge2}k c_{\alpha,k}c_{\beta,k}\sum_j\eta_j(U_\ell U_m^\dagger)^k.
```

The precise assumptions, coefficients, and proof map are in [the theorem statement](theory/THEOREM.md). The limit keeps the active boundary dimensions, entropy orders, and finite gate collection fixed while the balanced half-dimension d grows.

## What this explains

- **Fixed spatial access leaves a positive correlation.** A gate on fixed boundary factors cannot erase all limiting entropy correlation. Dual-unitary gates attain the bound when the two active dimensions are equal.
- **Purity does not contain the whole answer.** Gates with equal operator purity can have different von Neumann or logarithmic-negativity covariance.
- **The entropy hierarchy contains spectral information.** Ideal integer-order covariances determine the operator Schmidt probabilities at finite rank, with poor conditioning that prevents an automatic practical tomography claim.

The absolute fluctuations decrease as 1/d. The result concerns their covariance, and does not assert macroscopic retained entropy. The attempted Floquet-eigenstate extension failed its declared comparison; [that limitation is retained](limits/FLOQUET_REPORT_09.md).

## Read and reproduce

| Need | Start here |
|---|---|
| Current claims and exclusions | [Claim ledger](CLAIM_LEDGER.md) |
| Exact setting and proof | [Theorem](theory/THEOREM.md), [general-gate derivation](evidence/checkpoint08/foundation/GENERAL_GATE_REVIEW.md), [proof review](reviews/PROOF_ASSESSMENT.md) |
| Closest prior work | [Publication positioning](reviews/PUBLICATION_POSITIONING.md) |
| Current repository work | [Refurnishing roadmap](NEXT.md) |
| Later manuscript phase | [Reserved paper outline](PAPER_OUTLINE.md) |
| Computational checks | [Reproduction instructions](REPRODUCE.md) |
| New research workspace | [Handover](HANDOVER.md), [agent instructions](AGENTS.md) |
| Repository transition | [Provenance](provenance/REPOSITORY_TRANSITION.md) |

Install the recorded Python dependencies and run the focused reproduction:

```sh
python -m pip install -r requirements.txt
python verify_project.py
```

This checks imported-file integrity and runs the six checkpoint-08 deterministic checks in a temporary copy. It does not rerun the previous Haar sampling. Existing exact purity controls, contraction checks, and modest numerical cohorts remain in `evidence/` with their original protocols and reproduction commands.

## Relationship to the subset-state work

The GitHub URL is temporarily **Entangling-successions**. The author has confirmed that its old subset-state experiments were upgraded into [Subset-states](https://github.com/GoGoKo699/Subset-states), the home of **Support-size entanglement trajectories of random subset states**, updating [arXiv:2501.06292](https://arxiv.org/abs/2501.06292).

On 13 September 2026 the author authorized reuse of this historical repository. Its complete former main tree is preserved under [legacy/subset-development](legacy/subset-development/) and on branch `legacy/subset-development-2026-09-13`, at original commit `1154a87b699d1a17f9e40aaf16a141db62e96041`. It is historical material, not a second active paper here. The repository may be renamed later.

The active covariance paper is scientifically separate from Subset-states. Both use coefficient-matrix spectra, but the subset ensemble has a coherent mean, real amplitudes, and a fixed-support-cardinality constraint. A common entropy fluctuation law has not been proved. See [the scope decision](reviews/SUBSET_SCOPE_DECISION.md).

The previous name **Entanglement Temporal Fluctuations** refers to this same active paper. Entanglement Trajectories, Boundary-Entangling-Susceptibility, and the wider PRL exploration retain their own scopes.
