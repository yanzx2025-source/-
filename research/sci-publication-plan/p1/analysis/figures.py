"""Figures 1-2 for the manuscript (static, print). Usage: python figures.py <p1 folder>"""
import sys, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
P = sys.argv[1]; D = ["D1", "D2", "D3", "D4", "D5", "D6"]
key = pd.read_csv(f"{P}/data/sheet_key.csv"); key["img"] = key.sheet + "-" + key.rep.astype(str)
c = pd.read_csv(f"{P}/data/consensus_codes.csv")[["img"] + D].merge(key, on="img")
L = c.melt(id_vars=["img", "model", "strategy", "role"], value_vars=D, var_name="dim", value_name="v")
L = L[L.v != 9]; L["y"] = L.v.astype(int)
COL = {"P1": "#2a78d6", "P2": "#eb6834"}; HATCH = {"P1": "", "P2": "///"}
INK, MUTED, GRID = "#1f1f1e", "#6b6a64", "#e4e3df"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": MUTED})

def bars(groups, labels, rates, fname, xlabel, width=6.3):
    fig, ax = plt.subplots(figsize=(width, 3.2), dpi=300)
    w = 0.36
    for i, s in enumerate(["P1", "P2"]):
        xs = [g + (i - 0.5) * (w + 0.02) for g in range(len(groups))]
        vals = [rates[(g, s)] * 100 for g in groups]
        ax.bar(xs, vals, w, color=COL[s], hatch=HATCH[s], edgecolor="white", linewidth=0.6,
               label={"P1": "P1: role name only", "P2": "P2: dress code stated"}[s], zorder=3)
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.2, f"{v:.1f}", ha="center", va="bottom", fontsize=7.5, color=INK)
    ax.set_xticks(range(len(groups))); ax.set_xticklabels(labels)
    ax.set_ylabel("Violation rate (% of codable items)"); ax.set_xlabel(xlabel)
    ax.set_ylim(0, 100); ax.yaxis.grid(True, color=GRID, linewidth=0.6, zorder=0)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    fig.tight_layout(); fig.savefig(f"{P}/figures/{fname}.png"); fig.savefig(f"{P}/figures/{fname}.tiff", pil_kwargs={"compression": "tiff_lzw"})
    plt.close(fig)

r = L.groupby(["model", "strategy"]).y.mean().to_dict()
bars(["deepseek", "doubao", "muse"], ["Hunyuan Image Alpha\n(WorkBuddy)", "Doubao", "Meta AI"], r,
     "fig1_channel_by_strategy", "Generation channel")
r = L.groupby(["dim", "strategy"]).y.mean().to_dict()
bars(D, ["D1\nGarment\ntype", "D2\nColour", "D3\nMotif", "D4\nHeadwear", "D5\nMarkers and\naccessories", "D6\nCross-cultural\nsubstitution"],
     r, "fig2_dimension_by_strategy", "Dress-code dimension", width=7.2)
print("ok")
