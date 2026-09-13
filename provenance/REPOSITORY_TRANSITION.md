# Repository reuse, 13 September 2026

The user confirmed that Entangling-successions was upgraded into Subset-states, described the former as a historical redundancy, and authorized its reuse for this project, with a possible later rename.

Verified starting points:

| Repository | Branch | Commit |
|---|---|---|
| GoGoKo699/Entangling-successions | main | 1154a87b699d1a17f9e40aaf16a141db62e96041 |
| GoGoKo699/Subset-states | main | 4cb99f109194124f500d75dd065ff43581a2682d |

Subset-states explicitly identifies the manuscript **Support-size entanglement trajectories of random subset states**, updating arXiv:2501.06292. Its provenance and exploratory code retain revised versions of earlier subset-state experiments. The user's statement supplies the project-lineage decision; this migration does not claim that every old result has been independently audited or mapped into the newer manuscript.

The complete old Entangling-successions root tree, `ffb13b5f01c8c8ad18c80b521feefd3383a34e34`, is preserved as the subtree `legacy/subset-development/`. Branch `legacy/subset-development-2026-09-13` preserves the original main commit. The new main commit descends from that commit normally, without a force update or rewritten history.

The new active content is the previously verified checkpoint-16 covariance paper project, with root scope and handover documents adapted to this repository. Checkpoint 07 and 08 evidence is imported unchanged. The checkpoint 09 source and summary package is imported unchanged except for omission of two large regenerable cohort NPZ files, listed separately with original hashes. All actual imported files are covered by the new import manifest.

This is a repository migration and scope decision. No new entropy theorem or physical generalization is claimed. Subset-states, Entanglement Trajectories, and Boundary-Entangling-Susceptibility are not editing targets. The covariance paper remains separate because the existing Haar theorem does not establish the corresponding subset-ensemble fluctuations.

No new external repository or repository rename is part of this transition. No software reuse license was selected by this migration; inherited notices and attribution remain with their files.
