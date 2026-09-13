"""Small scientific figure generated solely from the analytical series."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from .core import spatial_correlation_bound
from .examples import DEFAULT_CUTOFF, zz_correlation_curve


def plot_entropy_memory(output_dir, *, cutoff=DEFAULT_CUTOFF):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    angles = np.linspace(0, np.pi/2, 161)
    colors = ["#0072B2", "#D55E00", "#009E73"]
    with plt.rc_context({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "svg.hashsalt": "gate-entropy-covariance"}):
        fig, ax = plt.subplots(figsize=(7.0, 4.5), layout="constrained")
        for alpha, label, color in zip([.5, 1., 2.], [r"$\alpha=1/2$", r"$\alpha=1$", r"$\alpha=2$"], colors):
            values = zz_correlation_curve(angles, alpha, cutoff)
            floor = spatial_correlation_bound(alpha, 2, 2, cutoff=cutoff)
            ax.plot(angles, values, color=color, lw=2.2, label=label)
            ax.axhline(floor, color=color, ls="--", lw=1.5)
        ax.set(xlim=(0, np.pi/2), ylim=(0, 1.04),
               xlabel=r"Pulse angle $\theta$ in $U=\exp(-i\theta Z\otimes Z)$",
               ylabel=r"Limiting entropy correlation $\rho_\alpha(U)$")
        ax.set_xticks([0, np.pi/4, np.pi/2], ["0", r"$\pi/4$", r"$\pi/2$"])
        ax.set_yticks([0, .25, .5, .75, 1])
        ax.grid(axis="y", alpha=.18)
        ax.legend(loc="upper center", frameon=False, ncol=3)
        ax.text(.5, .08, "Dashed: minimum for one active qubit pair, attained by active SWAP",
                ha="center", va="center", transform=ax.transAxes, fontsize=9)
        ax.set_title("A local gate changes entanglement memory", pad=12)
        fig.savefig(output_dir/"entropy_memory.png", dpi=180,
                    metadata={"Software": "Gate Entanglement Covariance"})
        fig.savefig(output_dir/"entropy_memory.svg", metadata={"Date": None})
        plt.close(fig)
