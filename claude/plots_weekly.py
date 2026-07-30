# -*- coding: utf-8 -*-
"""Rollup-only figures. Daily runs do not touch this file.

  PMRW_START / PMRW_END  inclusive period bounds (required)
  PMRW_FIGDIR            output dir (required)

Produces w1_subtopic_trend.png: per-issue subtopic counts across the period,
read from state/metrics.csv. Never queries an API.
"""
import os, csv, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from plots import SUBCOL, PAPER, INK, SLATE, GRID, DEEP, save  # shared design system

HERE  = os.path.dirname(os.path.abspath(__file__))
START = os.environ["PMRW_START"]
END   = os.environ["PMRW_END"]

rows = []
with open(os.path.join(HERE, "state", "metrics.csv")) as f:
    for r in csv.DictReader(f):          # quoted: subtopics may contain commas
        if START <= r["date"] <= END:
            rows.append((r["date"], r["subtopic"], int(r["n"])))

dates = sorted({d for d, _, _ in rows})
subs  = [s for s, _ in collections.Counter(
            {s: sum(n for _, ss, n in rows if ss == s) for s in {x[1] for x in rows}}
         ).most_common()]
subs  = sorted({s for _, s, _ in rows},
               key=lambda s: -sum(n for _, ss, n in rows if ss == s))
M = {(d, s): 0 for d in dates for s in subs}
for d, s, n in rows:
    M[(d, s)] = n

fig, ax = plt.subplots(figsize=(9.4, 4.2))
x = np.arange(len(dates))
bottom = np.zeros(len(dates))
for s in subs:
    v = np.array([M[(d, s)] for d in dates], dtype=float)
    ax.bar(x, v, bottom=bottom, color=SUBCOL.get(s, SLATE), width=0.62,
           edgecolor=PAPER, linewidth=1.0, zorder=3, label=s)
    bottom += v
for i, t in enumerate(bottom):
    ax.text(i, t + 0.35, "%d" % t, ha="center", fontsize=8.6,
            fontweight="bold", color=INK)
ax.set_xticks(x)
ax.set_xticklabels([d[5:] for d in dates], fontsize=8.4)
ax.set_ylabel("Records in issue")
ax.set_xlabel("Issue date (mm-dd)")
ax.set_ylim(0, max(bottom.max() + 2, 4))
ax.set_title("Subtopic composition by issue, %s to %s" % (START, END), pad=10)
ax.yaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
for sp in ("top", "right", "left"):
    ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), fontsize=7.2, ncol=3,
          handlelength=1.0, handletextpad=0.5, columnspacing=1.4, frameon=False)
save(fig, "w1_subtopic_trend.png")
print("weekly figure written for %s..%s over %d issues" % (START, END, len(dates)))
