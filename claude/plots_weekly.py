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

# Two regimes, because one panel cannot serve both.
#
# WEEKLY (<= 10 issues, no backfill batch in range): the question is how each subtopic
# moved day to day, so plot a per-issue line series with the daily total on a twin axis.
# A jump from 2 to 6 means nothing without its denominator, and the denominator is the
# issue size - so the figure carries it.
#
# MONTHLY (a 164-record backfill batch sits in range next to 11-33-record days): a
# stacked per-issue bar collapses to stripes and is unreadable. The question there is
# "what did the daily cadence miss", so plot caught-vs-missed per subtopic instead.
BATCH_CUTOFF = "2026-07-27"          # first day of the daily cadence
DAILY = [d for d in dates if d >= BATCH_CUTOFF]
BATCH = [d for d in dates if d < BATCH_CUTOFF]

if not BATCH and len(dates) <= 10:
    tot = {d: sum(M[(d, s)] for s in subs) for d in dates}
    top = subs[:6]                    # a line per subtopic past six is unreadable
    fig, ax = plt.subplots(figsize=(11.0, 6.4))
    x = np.arange(len(dates))
    ax2 = ax.twinx()
    ax2.bar(x, [tot[d] for d in dates], width=0.62, color=GRID, zorder=0,
            label="records in issue (right axis)")
    ax2.set_ylabel("Records in issue", fontsize=11.0, color=SLATE)
    ax2.tick_params(axis="y", labelcolor=SLATE, labelsize=10)
    ax2.set_ylim(0, max(tot.values()) * 1.9)
    for sp in ("top", "left"):
        ax2.spines[sp].set_visible(False)
    for s in top:
        ax.plot(x, [M[(d, s)] for d in dates], marker="o", ms=5.5, lw=2.0,
                color=SUBCOL.get(s, DEEP), label=s, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels([d[5:] for d in dates], fontsize=11)
    ax.set_ylabel("Records in subtopic", fontsize=11.5)
    ax.set_xlabel("Issue date (2026)", fontsize=11.5)
    ax.set_ylim(0, max(max(M[(d, s)] for d in dates for s in top), 4) * 1.25)
    ax.set_title("Subtopic movement across the week (%s to %s)" % (START, END), pad=12)
    ax.yaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper center", bbox_to_anchor=(0.5, -0.13),
              ncol=3, fontsize=9.8, frameon=False)
    fig.tight_layout()
    save(fig, "w1_subtopic_trend.png")
    print("weekly trend figure written for %s..%s over %d issues" % (START, END, len(dates)))
    raise SystemExit

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
