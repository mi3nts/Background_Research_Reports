# -*- coding: utf-8 -*-
import os, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from corpus import PAPERS, EFFECTS
try:
    from corpus import LIFECOURSE
except ImportError:
    LIFECOURSE = None

OUT = os.environ.get("PMRW_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette
INK    = "#14262E"
SLATE  = "#4A6572"
PAPER  = "#FBF9F5"
GRID   = "#D9D3C9"
TEAL   = "#1F7A8C"
DEEP   = "#0F4C5C"
AMBER  = "#E3A008"
CORAL  = "#D1495B"
VIOLET = "#6A5B9E"
SAGE   = "#6FA287"
CLAY   = "#B5643C"
SKY    = "#4FA3C4"
MUSK   = "#8A7E72"

SEQ = [DEEP, TEAL, SKY, SAGE, AMBER, CLAY, CORAL, VIOLET, MUSK, SLATE]

# fixed subtopic -> colour map, identical to BANDCOL in mktable.py so a given
# subtopic keeps its colour across every issue
SUBCOL = {
    "Neuro / mental health": DEEP,
    "Cardiovascular & metabolic": TEAL,
    "Reproductive & developmental": SKY,
    "Respiratory & allergic": SAGE,
    "Mechanistic toxicology": VIOLET,
    "Occupational & indoor": CLAY,
    "Sensing, forecasting & instrumentation": AMBER,
    "Exposure assessment & modelling": MUSK,
    "Burden, policy & mitigation": CORAL,
    "Other clinical endpoints": SLATE,
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": SLATE,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.linewidth": 0.8,
    "xtick.color": SLATE,
    "ytick.color": SLATE,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "legend.frameon": False,
})

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)

def despine(ax, keep=("left", "bottom")):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)

# ---------------------------------------------------------------- 1. subtopics
counts = collections.Counter(p["sub"] for p in PAPERS)
items = counts.most_common()
labels = [k for k, _ in items][::-1]
vals   = [v for _, v in items][::-1]
cols   = [SUBCOL.get(k, SLATE) for k in labels]

fig, ax = plt.subplots(figsize=(7.4, 3.5))
y = np.arange(len(labels))
ax.barh(y, vals, color=cols, height=0.66, zorder=3)
for yi, v in zip(y, vals):
    ax.text(v + 0.13, yi, str(v), va="center", ha="left", fontsize=9,
            fontweight="bold", color=INK)
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8.6)
ax.set_xlim(0, max(vals) + 1.1)
ax.set_xlabel("Number of records")
ax.set_title("Subtopic distribution of today's corpus")
ax.xaxis.grid(True, color=GRID, lw=0.7, zorder=0)
ax.set_axisbelow(True)
despine(ax, keep=("bottom",))
ax.tick_params(axis="y", length=0)
save(fig, "f1_subtopics.png")

# ---------------------------------------------------------------- 2. design donut + tier bar
design_group = {
    "Case-crossover": "Observational - acute",
    "Panel study": "Observational - acute",
    "Prospective cohort": "Observational - cohort",
    "Prospective cohort (mixtures)": "Observational - cohort",
    "Nationwide cohort": "Observational - cohort",
    "Registry cohort + geospatial": "Observational - cohort",
    "Cross-sectional (multistage)": "Observational - cross-sectional",
    "Ecological panel": "Ecological",
    "GBD secondary analysis": "Ecological",
    "Emission inventory": "Modelling / inventory",
    "Deep-learning model": "Modelling / inventory",
    "CTM + mobility integration": "Modelling / inventory",
    "Narrative review": "Review / synthesis",
    "Critical review": "Review / synthesis",
    "Review + risk economics": "Review / synthesis",
    "Umbrella review / meta-analysis": "Review / synthesis",
    "In vitro + organoid + murine": "Experimental / toxicology",
    "Real-ambient murine + co-culture": "Experimental / toxicology",
    "Controlled exposure (ecotox)": "Experimental / toxicology",
    "Bench / device experiment": "Experimental / toxicology",
    "RCT process evaluation": "Trial / intervention",
    "Field measurement": "Measurement campaign",
    "Real-time sensor campaign": "Measurement campaign",
    "Observational exposure study": "Measurement campaign",
    "Repeated-measures biomarker": "Measurement campaign",
    "Scoping review": "Review / synthesis",
    "Commentary / methods letter": "Review / synthesis",
    "Retrospective clinical series": "Observational - cross-sectional",
    "Retrospective cohort": "Observational - cohort",
    "In vitro (cell lines)": "Experimental / toxicology",
    "Murine inhalation exposure": "Experimental / toxicology",
    "Supersite observation": "Measurement campaign",
    "Environmental surveillance campaign": "Measurement campaign",
    "Dispersion model + soil sampling": "Modelling / inventory",
    "Spatial econometric model": "Modelling / inventory",
    "Bayesian + geospatial regression": "Modelling / inventory",
    "Cross-sectional imaging": "Observational - cross-sectional",
    "Time-series": "Observational - acute",
    "Physical exposure model": "Modelling / inventory",
    "Machine-learning model": "Modelling / inventory",
    "Source apportionment": "Measurement campaign",
    "Sensor co-location": "Measurement campaign",
    "Chamber sensor evaluation": "Measurement campaign",
    "Proxy validation vs personal exposure": "Measurement campaign",
    "Exposome-wide association": "Observational - cross-sectional",
    "Case-control": "Observational - cross-sectional",
    "Ex vivo perfused organ": "Experimental / toxicology",
}
def dgrp(d):
    return design_group.get(d, "Other / mixed")
dg = collections.Counter(dgrp(p["design"]) for p in PAPERS)
dg_items = dg.most_common()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.3),
                               gridspec_kw={"width_ratios": [1.0, 1.0], "wspace": 0.42})
w = [v for _, v in dg_items]
lab = [k for k, _ in dg_items]
wedges, _ = ax1.pie(w, colors=SEQ[:len(w)], startangle=90, radius=0.86,
                    wedgeprops=dict(width=0.36, edgecolor=PAPER, linewidth=1.6))
ax1.text(0, 0.08, str(sum(w)), ha="center", va="center", fontsize=20,
         fontweight="bold", color=DEEP)
ax1.text(0, -0.14, "records", ha="center", va="center", fontsize=8.0, color=SLATE)
ax1.legend(wedges, [f"{l}  ({v})" for l, v in zip(lab, w)],
           loc="upper center", bbox_to_anchor=(0.5, -0.02), fontsize=7.0, ncol=2,
           handlelength=1.0, handletextpad=0.5, columnspacing=1.2)
ax1.set_title("Study architecture", pad=2)

ep = collections.Counter(p["endpoint"] for p in PAPERS)
ep_items = sorted(ep.items(), key=lambda kv: kv[1])
ax2.barh([k for k, _ in ep_items], [v for _, v in ep_items],
         color=[SEQ[i % len(SEQ)] for i in range(len(ep_items))][::-1],
         height=0.62, zorder=3)
for i, (_, v) in enumerate(ep_items):
    ax2.text(v + 0.1, i, str(v), va="center", fontsize=8.4, fontweight="bold", color=INK)
ax2.set_xlim(0, max(ep.values()) + 1)
ax2.set_xlabel("Records")
ax2.set_title("Health endpoint / organ system", pad=2)
ax2.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax2.set_axisbelow(True)
despine(ax2, keep=("bottom",)); ax2.tick_params(axis="y", length=0)
ax2.tick_params(axis="y", labelsize=8.2)
save(fig, "f2_design_endpoint.png")

# ---------------------------------------------------------------- 3. PM metric + geography
def pmclass(s):
    s = s.lower()
    if "ultrafine" in s: return "Ultrafine / nanoscale"
    if "bioaerosol" in s or "seed" in s: return "Bioaerosol / coarse"
    if "settleable" in s or "respirable dust" in s: return "Settleable / respirable dust"
    if "pm2.5" in s and "pm10" in s: return "PM2.5 + PM10 jointly"
    if "pm2.5" in s: return "PM2.5 only"
    if "pm10" in s: return "PM10 only"
    return "PM (unspeciated) / emissions"

pmc = collections.Counter(pmclass(p["pm"]) for p in PAPERS)
geo_group = {
    "China": "China", "China / India": "China", "USA": "North America",
    "Canada": "North America", "Germany": "Europe", "Spain": "Europe",
    "UK": "Europe", "EU-27": "Europe", "Global": "Global / multi-region",
    "MENA": "Middle East & N. Africa", "South Korea": "East Asia (ex-China)",
    "Japan": "East Asia (ex-China)", "Colombia": "Latin America",
    "Brazil": "Latin America", "Australia": "Oceania",
    "Thailand": "Southeast Asia", "Vietnam": "Southeast Asia",
    "Ghana": "Sub-Saharan Africa", "Uganda": "Sub-Saharan Africa",
    "Nigeria": "Sub-Saharan Africa", "Kenya": "Sub-Saharan Africa",
    "Poland": "Europe", "Romania": "Europe", "Netherlands": "Europe",
    "Turkiye": "Middle East & N. Africa", "India": "South Asia",
    "South Africa": "Sub-Saharan Africa", "Mexico": "Latin America",
    "Lebanon": "Middle East & N. Africa", "Bangladesh": "South Asia",
    "Kazakhstan": "Central Asia", "Greece": "Europe", "Bulgaria": "Europe",
    "Norway": "Europe", "Taiwan": "East Asia (ex-China)",
    "Czech Republic": "Europe", "The Gambia / Kenya / Mozambique": "Sub-Saharan Africa",
}
geo = collections.Counter(geo_group.get(p["geo"], "Global / multi-region") for p in PAPERS)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.3),
                               gridspec_kw={"wspace": 0.46})
pi = sorted(pmc.items(), key=lambda kv: kv[1])
ax1.barh([k for k, _ in pi], [v for _, v in pi],
         color=[TEAL, SKY, SAGE, AMBER, CLAY, VIOLET, DEEP][:len(pi)][::-1],
         height=0.6, zorder=3)
for i, (_, v) in enumerate(pi):
    ax1.text(v + 0.12, i, str(v), va="center", fontsize=8.4, fontweight="bold")
ax1.set_xlim(0, max(pmc.values()) + 1.2)
ax1.set_title("Particle metric under study", pad=8)
ax1.set_xlabel("Records")
ax1.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax1.set_axisbelow(True)
despine(ax1, keep=("bottom",)); ax1.tick_params(axis="y", length=0, labelsize=8.2)

gi = sorted(geo.items(), key=lambda kv: kv[1])
ax2.barh([k for k, _ in gi], [v for _, v in gi],
         color=[DEEP, TEAL, SKY, SAGE, AMBER, CLAY, CORAL, VIOLET][:len(gi)][::-1],
         height=0.6, zorder=3)
for i, (_, v) in enumerate(gi):
    ax2.text(v + 0.12, i, str(v), va="center", fontsize=8.4, fontweight="bold")
ax2.set_xlim(0, max(geo.values()) + 1.2)
ax2.set_title("Geographic provenance of evidence", pad=8)
ax2.set_xlabel("Records")
ax2.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax2.set_axisbelow(True)
despine(ax2, keep=("bottom",)); ax2.tick_params(axis="y", length=0, labelsize=8.2)
save(fig, "f3_metric_geography.png")

# ---------------------------------------------------------------- 4. subtopic x design heatmap
subs = [k for k, _ in counts.most_common()]
dgs  = [k for k, _ in dg.most_common()]
M = np.zeros((len(subs), len(dgs)))
for p in PAPERS:
    M[subs.index(p["sub"]), dgs.index(dgrp(p["design"]))] += 1

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("pm", [PAPER, "#BFD8DD", SKY, TEAL, DEEP])

fig, ax = plt.subplots(figsize=(7.8, 4.2))
im = ax.imshow(M, cmap=cmap, aspect="auto", vmin=0, vmax=max(3, M.max()))
ax.set_xticks(range(len(dgs))); ax.set_xticklabels(dgs, rotation=32, ha="right", fontsize=7.8)
ax.set_yticks(range(len(subs))); ax.set_yticklabels(subs, fontsize=8.2)
for i in range(len(subs)):
    for j in range(len(dgs)):
        if M[i, j] > 0:
            ax.text(j, i, int(M[i, j]), ha="center", va="center", fontsize=8.6,
                    fontweight="bold", color=PAPER if M[i, j] >= 2 else INK)
ax.set_xticks(np.arange(-.5, len(dgs), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(subs), 1), minor=True)
ax.grid(which="minor", color=PAPER, lw=2.0)
ax.tick_params(which="minor", length=0); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title("Where the work is happening: subtopic x study architecture", pad=10)
cb = fig.colorbar(im, ax=ax, fraction=0.024, pad=0.02)
cb.outline.set_visible(False); cb.ax.tick_params(length=0, labelsize=7.5)
save(fig, "f4_heatmap.png")

# ---------------------------------------------------------------- 5. forest plot
E = sorted(EFFECTS, key=lambda d: d["est"])
fig, ax = plt.subplots(figsize=(8.0, 4.6))
y = np.arange(len(E))
colmap = collections.defaultdict(lambda: SLATE, {"HR": TEAL, "OR": CLAY, "IRR": VIOLET,
          "RR-equiv": SAGE, "RR": SAGE, "beta": SKY, "%": AMBER, "r": DEEP})
def _hasci(e):
    return e.get("lo") is not None and e.get("hi") is not None and e["hi"] > e["lo"]

for i, e in enumerate(E):
    c = colmap[e["metric"]]
    if _hasci(e):
        ax.plot([e["lo"], e["hi"]], [i, i], color=c, lw=2.0, solid_capstyle="round", zorder=3)
        ax.plot([e["lo"], e["lo"]], [i - .16, i + .16], color=c, lw=1.4, zorder=3)
        ax.plot([e["hi"], e["hi"]], [i - .16, i + .16], color=c, lw=1.4, zorder=3)
    ax.scatter([e["est"]], [i], s=46, color=c, zorder=4,
               edgecolor=PAPER, linewidth=1.0)
    _lbl = (f"{e['est']:.4g} ({e['lo']:.4g}–{e['hi']:.4g})" if _hasci(e)
            else f"{e['est']:.4g} (no CI reported)")
    ax.text(1.025, i, _lbl,
            transform=ax.get_yaxis_transform(which="grid"),
            fontsize=7.6, va="center", ha="left", color=SLATE, family="monospace")
ax.axvline(1.0, color=CORAL, lw=1.1, ls="--", zorder=2)
ax.set_xscale("log")
_lo = min([e["lo"] for e in E if e.get("lo") is not None]
          + [e["est"] for e in E] + [1.0])
_hi = max([e["hi"] for e in E if e.get("hi") is not None]
          + [e["est"] for e in E] + [1.0])
_pad = (_hi / _lo) ** 0.10
ax.set_xlim(_lo / _pad, _hi * _pad)
_cand = [0.5, 0.8, 0.9, 0.95, 1.0, 1.02, 1.04, 1.05, 1.06, 1.08, 1.1, 1.15,
         1.25, 1.5, 2, 3, 5, 9]
_tk = [t for t in _cand if _lo / _pad <= t <= _hi * _pad]
if len(_tk) > 9:
    _tk = [t for t in _tk if t in (1.0, 1.05, 1.1, 1.25, 1.5, 2, 3, 5, 9)]
ax.set_xticks(_tk)
ax.set_xticklabels([("%g" % t) for t in _tk])
ax.get_xaxis().set_minor_formatter(plt.NullFormatter())
ax.set_yticks(y)
ax.set_yticklabels([f"{e['label']}\n{e['exposure']} - {e['src']}" for e in E], fontsize=7.4)
ax.set_xlabel("Effect estimate (log scale); dashed line = null")
ax.set_ylim(-0.7, len(E) - 0.3)
ax.set_title("Quantitative associations reported in today's corpus", pad=10)
ax.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
despine(ax, keep=("bottom",)); ax.tick_params(axis="y", length=0)
_used = [m for m in dict.fromkeys(e["metric"] for e in E)]
handles = [plt.Line2D([], [], color=colmap[m], lw=2.4, label=m) for m in _used]
ax.legend(handles=handles, loc="lower right", fontsize=7.6, ncol=max(1, len(handles)),
          bbox_to_anchor=(1.0, -0.22))
save(fig, "f5_forest.png")

# ---------------------------------------------------------------- 6. life-course window strip
stages = ["Preconception /\nin utero", "Infancy &\nearly childhood", "Puberty &\nadolescence",
          "Working-age\nadulthood", "Older adults\n(65+)"]
stage_hits = [5, 3, 2, 3, 4]
stage_note = ["fetal growth, brain\nstructure, IQ",
              "asthma admissions,\ndyslipidaemia",
              "pubertal timing,\nPAH endocrine axis",
              "occupational RCS,\nfirefighter biomarkers",
              "AF events, cognition,\ncare-home filtration"]
if LIFECOURSE:
    stage_hits = [d["n"] for d in LIFECOURSE]
    stage_note = [d["note"] for d in LIFECOURSE]
fig, ax = plt.subplots(figsize=(8.4, 2.55))
xs = np.arange(len(stages))
ax.plot(xs, [0] * len(xs), color=GRID, lw=3, zorder=1, solid_capstyle="round")
for i, (s, n, note) in enumerate(zip(stages, stage_hits, stage_note)):
    c = SEQ[i]
    ax.scatter([i], [0], s=120 + 95 * n, color=c, zorder=3,
               edgecolor=PAPER, linewidth=2.0, alpha=0.92)
    ax.text(i, 0, str(n), ha="center", va="center", color=PAPER,
            fontsize=10, fontweight="bold", zorder=4)
    ax.text(i, 0.62, s, ha="center", va="bottom", fontsize=8.4, fontweight="bold", color=INK)
    ax.text(i, -0.62, note, ha="center", va="top", fontsize=7.2, color=SLATE)
ax.set_xlim(-0.55, len(stages) - 0.45); ax.set_ylim(-1.5, 1.35)
ax.axis("off")
ax.set_title("Life-course windows addressed today (records may span several stages)",
             pad=6, fontsize=10)
save(fig, "f6_lifecourse.png")

print("figures:", sorted(os.listdir(OUT)))
print("n_papers:", len(PAPERS))
print("subtopics:", dict(counts))
print("designs:", dict(dg))
print("geo:", dict(geo))
print("pm:", dict(pmc))
