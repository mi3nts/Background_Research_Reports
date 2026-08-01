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
from plots import SUBCOL, PAPER, INK, SLATE, GRID, DEEP, AMBER, save  # shared design system

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

# A stacked bar per issue is unreadable once one "issue" is a 164-record backfill batch
# and the others are 11-33-record days: every segment collapses to a stripe. The question
# the panel actually has to answer is "what did the daily cadence miss", so plot that
# directly - per subtopic, records the dailies caught against records only the month-wide
# harvest found.
DAILY = [d for d in dates if d >= "2026-07-27"]
BATCH = [d for d in dates if d < "2026-07-27"]
caught = np.array([sum(M[(d, s)] for d in DAILY) for s in subs], dtype=float)
missed = np.array([sum(M[(d, s)] for d in BATCH) for s in subs], dtype=float)
order = np.argsort(caught + missed)
subs_o = [subs[i] for i in order]
caught, missed = caught[order], missed[order]

fig, ax = plt.subplots(figsize=(11.0, 7.2))
y = np.arange(len(subs_o))
h = 0.38
ax.barh(y + h/2, caught, height=h, color=DEEP, zorder=3,
        label="Recovered by the five daily issues (27-31 Jul)")
ax.barh(y - h/2, missed, height=h, color=AMBER, zorder=3,
        label="Recovered only by the month-wide harvest (1-26 Jul)")
for yi, v in zip(y + h/2, caught):
    ax.text(v + 0.6, yi, "%d" % v, va="center", fontsize=11, fontweight="bold", color=DEEP)
for yi, v in zip(y - h/2, missed):
    ax.text(v + 0.6, yi, "%d" % v, va="center", fontsize=11, fontweight="bold", color=AMBER)
ax.set_yticks(y); ax.set_yticklabels(subs_o, fontsize=11.5)
ax.set_xlabel("Records", fontsize=11.5)
ax.set_xlim(0, max((caught + missed).max(), 4) * 1.12)
ax.set_title("What the daily cadence missed, by subtopic (%s to %s)" % (START, END), pad=12)
ax.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
for sp in ("top", "right", "left"):
    ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(loc="lower right", fontsize=10.5, frameon=False)
fig.tight_layout()
save(fig, "w1_subtopic_trend.png")
print("weekly figure written for %s..%s over %d issues" % (START, END, len(dates)))
