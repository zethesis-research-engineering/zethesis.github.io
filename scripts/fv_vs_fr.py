"""
Didactic figure for the flux-reconstruction note.

Shows how finite volume and flux reconstruction represent the *same* smooth-but-wiggly
function, and how FR sharpens as the polynomial degree p increases:

  FV       : one cell average per cell  -> a piecewise-constant staircase.
  FR (p=1) : a line   per element, discontinuous at interfaces -> large jumps.
  FR (p=2) : a parabola per element                             -> smaller jumps.
  FR (p=3) : a cubic   per element                              -> jumps almost gone.

The element count (6) is fixed across the FR panels, so the only thing changing is p:
that is "p-refinement", FR's way of buying accuracy without touching the mesh.

Run from the repository root:
    python scripts/fv_vs_fr.py
Writes: assets/images/fv-vs-fr.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import legendre as Lg

# np.trapz was renamed to np.trapezoid in NumPy 2.0; support both.
_trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))

FV_COLOR = "#c0392b"
FR_COLOR = "#2471a3"


def f(x):
    """The 'true' smooth-but-wiggly function (a windowed cosine wave packet)."""
    return np.exp(-((x - 0.5) ** 2) / (2 * 0.18 ** 2)) * np.cos(7 * np.pi * x)


def cell_average(a, b, n=400):
    """Exact-ish average of f over [a, b] by fine-grid quadrature."""
    xs = np.linspace(a, b, n)
    return _trapz(f(xs), xs) / (b - a)


def lagrange_interp(xs, ys, xq):
    """Evaluate the degree-(len(xs)-1) Lagrange interpolant of (xs, ys) at points xq."""
    yq = np.zeros_like(xq)
    for j in range(len(xs)):
        Lj = np.ones_like(xq)
        for m in range(len(xs)):
            if m != j:
                Lj *= (xq - xs[m]) / (xs[j] - xs[m])
        yq += ys[j] * Lj
    return yq


def draw_true(ax, xx):
    ax.plot(xx, f(xx), color="0.72", lw=1.6, label="true function", zorder=1)


def draw_fv(ax, xx, N=24):
    edges = np.linspace(0, 1, N + 1)
    avg = np.array([cell_average(edges[i], edges[i + 1]) for i in range(N)])
    draw_true(ax, xx)
    for i in range(N):
        ax.plot([edges[i], edges[i + 1]], [avg[i], avg[i]],
                color=FV_COLOR, lw=2.4, zorder=3)
        if i < N - 1:
            ax.plot([edges[i + 1], edges[i + 1]], [avg[i], avg[i + 1]],
                    color=FV_COLOR, lw=0.8, alpha=0.45, zorder=2)
    for e in edges:
        ax.axvline(e, color="0.92", lw=0.6, zorder=0)
    ax.set_title(f"Finite volume — one average per cell, {N} cells (a staircase)",
                 fontsize=11, loc="left")


def draw_fr(ax, xx, K=6, p=3):
    el = np.linspace(0, 1, K + 1)
    gp, _ = Lg.leggauss(p + 1)  # p+1 reference Gauss solution points in [-1, 1]
    draw_true(ax, xx)
    for k in range(K):
        a, b = el[k], el[k + 1]
        xs = a + (b - a) * (gp + 1) / 2
        ys = f(xs)
        xloc = np.linspace(a, b, 250)
        ax.plot(xloc, lagrange_interp(xs, ys, xloc),
                color=FR_COLOR, lw=2.5, zorder=3)
        ax.plot(xs, ys, "o", color=FR_COLOR, ms=4.5, zorder=4)
    for e in el:
        ax.axvline(e, color="0.82", lw=0.9, ls="--", zorder=0)
    ax.set_title(f"Flux reconstruction — degree-{p} polynomial per element, "
                 f"{K} elements", fontsize=11, loc="left")


def main():
    xx = np.linspace(0, 1, 2000)
    degrees = [1, 2, 3]
    nrows = 1 + len(degrees)
    fig, axes = plt.subplots(nrows, 1, figsize=(8, 2.05 * nrows + 0.4), sharex=True)

    draw_fv(axes[0], xx)
    for ax, p in zip(axes[1:], degrees):
        draw_fr(ax, xx, K=6, p=p)

    for ax in axes:
        ax.set_ylim(-1.3, 1.3)
        ax.set_yticks([])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[-1].set_xlabel("x")
    axes[0].legend(loc="upper right", fontsize=9, frameon=False)
    fig.suptitle("Same function, different representations: FV averages vs. FR "
                 "at increasing polynomial degree", fontsize=12.5)
    fig.tight_layout(rect=[0, 0, 1, 0.975])

    os.makedirs("assets/images", exist_ok=True)
    out = "assets/images/fv-vs-fr.png"
    fig.savefig(out, dpi=150)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
