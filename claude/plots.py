# -*- coding: utf-8 -*-
import os, collections
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from corpus import PAPERS, EFFECTS
_S, _E = os.environ.get("PMRW_START"), os.environ.get("PMRW_END")
PERIODWORD = ("this period" if (_S and _E) else "today")
PERIODWORD_OF = ("the period" if (_S and _E) else "today")
# Rollups pool an order of magnitude more records than a daily issue. Figures sized for
# 11-18 records collapse into unreadable label soup at 270, so every canvas and every
# font scales up when a date range is set.
BIG = bool(_S and _E)
FS  = (lambda x: round(x * 1.35, 1)) if BIG else (lambda x: x)
SZ  = (lambda w, h: (w * 1.30, h * 1.55)) if BIG else (lambda w, h: (w, h))


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
    "font.size": 9 * (1.3 if BIG else 1.0),
    "axes.edgecolor": SLATE,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "axes.titlesize": 10.5 * (1.3 if BIG else 1.0),
    "axes.titleweight": "bold",
    "axes.linewidth": 0.8,
    "xtick.color": SLATE,
    "ytick.color": SLATE,
    "text.color": INK,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "savefig.dpi": 240 if BIG else 200,
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

fig, ax = plt.subplots(figsize=SZ(7.4, 3.5))
y = np.arange(len(labels))
ax.barh(y, vals, color=cols, height=0.66, zorder=3)
for yi, v in zip(y, vals):
    ax.text(v + 0.13, yi, str(v), va="center", ha="left", fontsize=FS(9),
            fontweight="bold", color=INK)
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=FS(8.6))
ax.set_xlim(0, max(vals) + 1.1)
ax.set_xlabel("Number of records")
ax.set_title("Subtopic distribution of %s corpus" % ("the period's" if (_S and _E) else "today's"))
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
    # added 2026-08-05: the diagnostic fired again, this time because canonical GROUP
    # names were being written straight onto records. Identity self-maps make a group
    # name a legal design label, so the map is closed under its own output.
    "Modelling / inventory": "Modelling / inventory",
    "Measurement campaign": "Measurement campaign",
    "Review / synthesis": "Review / synthesis",
    "Experimental / toxicology": "Experimental / toxicology",
    "Observational - acute": "Observational - acute",
    "Observational - cohort": "Observational - cohort",
    "Observational - cross-sectional": "Observational - cross-sectional",
    "Ecological": "Ecological",
    "Trial / intervention": "Trial / intervention",
    "Spatial analysis / GIS": "Modelling / inventory",
    "Time-series / case-crossover": "Observational - acute",
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
    "Satellite retrieval evaluation": "Modelling / inventory",
    "Chemical transport model": "Modelling / inventory",
    # added 2026-08-01 with the Crossref by-journal leg: instrumentation designs
    # were all falling through to "Other / mixed", which collapsed the architecture
    # donut to a single slice on an issue that had four distinct architectures.
    "Field co-location + chamber": "Measurement campaign",
    "Chamber co-location, AutoML calibration": "Measurement campaign",
    "Multi-instrument field evaluation": "Measurement campaign",
    "Network deployment + field evaluation": "Measurement campaign",
    "Proof-of-concept deployment": "Measurement campaign",
    "Chamber emission characterisation": "Experimental / toxicology",
    "Simulation (system-level)": "Modelling / inventory",
    "LUR model comparison": "Modelling / inventory",
    "Design resampling + cohort analysis": "Modelling / inventory",
    "CTM simulation + source attribution": "Modelling / inventory",
    "Kinetic model + field validation": "Modelling / inventory",
    "Systematic review (PRISMA)": "Review / synthesis",
    "Mapping review": "Review / synthesis",
    "Cross-sectional (cohort baseline)": "Observational - cross-sectional",
    "Cross-sectional (multistage)": "Observational - cross-sectional",
    "Registry cohort, FE models": "Observational - cohort",
    "Registry cohort + geospatial": "Observational - cohort",
    "Prospective birth cohort": "Observational - cohort",
    "Ecological panel, fixed effects": "Observational - ecological",
    "Ecological panel": "Observational - ecological",
    # added 2026-08-03: the 1 Aug fix covered the instrumentation designs that existed
    # then, but an issue whose corpus is 41% instrumentation exposed eleven more that
    # still fell through. Proofing caught it because the donut AND the f4 heatmap both
    # collapsed to a single "Other / mixed" column, which made two figures worthless.
    "Software / tool description": "Tool / software",
    "Methods / near-road field data": "Measurement campaign",
    "Laboratory metrology": "Chamber / laboratory",
    "Controlled chamber factorial": "Chamber / laboratory",
    "Chamber co-location, AutoML calibration": "Chamber / laboratory",
    "Release-recapture field experiment": "Measurement campaign",
    "Multi-site co-location evaluation": "Measurement campaign",
    "Calibration model comparison": "Measurement campaign",
    "Spatial cross-validation, operational network": "Measurement campaign",
    "Mechanistic correction framework": "Modelling / inventory",
    "Model intercomparison": "Modelling / inventory",
    "Exposure assessment + in vitro": "Experimental / toxicology",
    # honest fall-through for records surfaced without an abstract: they get their
    # own slice rather than being silently pooled with characterised designs
    "Metadata only (no abstract)": "Metadata only",
    # added 2026-08-05: ALL 13 records fell through to "Other / mixed" on this run,
    # the third recurrence of this failure class (01, 02, 03 Aug). The root cause is
    # that an unmapped design was SILENT - only a rendered figure revealed it. The
    # print below makes it loud, exactly as GEO already does.
    "Field campaign / remote sensing": "Measurement campaign",
    "Field campaign / shipborne": "Measurement campaign",
    "Method / algorithm": "Modelling / inventory",
    "Review / synthesis": "Review / synthesis",
    "Theory / simulation": "Modelling / inventory",
    "Emission inventory / decomposition": "Modelling / inventory",
    "Vehicle emission experiment": "Chamber / laboratory",
    "Animal experiment": "Experimental / toxicology",
    "Animal + in vitro": "Experimental / toxicology",
    "Cohort": "Observational - cohort",
    "Cohort (secondary trial analysis)": "Observational - cohort",
}
_design_unmapped = set()
def dgrp(d):
    if d not in design_group:
        _design_unmapped.add(d)
    return design_group.get(d, "Other / mixed")
dg = collections.Counter(dgrp(p["design"]) for p in PAPERS)
dg_items = dg.most_common()

# Endpoint labels drifted across issues (Cognitive / Neurological / Neuro-cognitive were
# all in use). Canonicalise before counting, otherwise a rollup splits one endpoint across
# three bars and the tail becomes unreadable. This is label normalisation only - no record
# changes subtopic.
ENDPOINT_CANON = {
    "Cognitive": "Neuro / cognitive", "Neurological": "Neuro / cognitive",
    "Mental health": "Neuro / mental health", "Neuro / behaviour": "Neuro / mental health",
    "Respiratory / allergic": "Respiratory", "Respiratory infection": "Respiratory",
    "Allergy": "Respiratory",
    "Oncological": "Oncologic", "Carcinogenic risk": "Oncologic",
    "None (monitoring)": "No health endpoint", "Not applicable": "No health endpoint",
    "Monitoring capacity": "No health endpoint", "Aerosol chemistry": "No health endpoint",
    "Source / policy": "No health endpoint", "Emissions / policy": "No health endpoint",
    "Hepatic / metabolic": "Metabolic",
    "Renal": "Other clinical", "Gastrointestinal": "Other clinical",
    "Ocular": "Other clinical", "Auditory": "Other clinical", "Sleep": "Other clinical",
    "Oral health": "Other clinical", "Surgical / mortality": "Other clinical",
    "Developmental / oxidative": "Reproductive", "Placental": "Reproductive",
    "Endocrine / puberty": "Reproductive",
    "Infectious surveillance": "Other clinical",
    # added 2026-08-03
    "None (monitoring)": "No health endpoint",
    "Epigenetic ageing": "Epigenetic ageing",
    "Toxicological (in vitro)": "Toxicological (in vitro)",
}
def canon_ep(e):
    return ENDPOINT_CANON.get(e, e)

ep = collections.Counter(canon_ep(p["endpoint"]) for p in PAPERS)

# The right panel's y-tick labels grow leftwards out of its own axes. With a fixed
# wspace they run over ax1's legend once an endpoint label is long ("Oxidative stress
# (in vitro proxy)"), which is what happened in the first weekly build. Scale the gap
# with the longest label instead of pinning it.
_eplab = max((len(k) for k in ep), default=10)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=SZ(9.0, max(4.3, 0.30 * len(ep) + 1.6)),
                               gridspec_kw={"width_ratios": [1.0, 1.0],
                                            "wspace": min(1.05, 0.42 + 0.021 * max(0, _eplab - 16))})
w = [v for _, v in dg_items]
lab = [k for k, _ in dg_items]
wedges, _ = ax1.pie(w, colors=SEQ[:len(w)], startangle=90, radius=0.86,
                    wedgeprops=dict(width=0.36, edgecolor=PAPER, linewidth=1.6))
ax1.text(0, 0.08, str(sum(w)), ha="center", va="center", fontsize=FS(20),
         fontweight="bold", color=DEEP)
ax1.text(0, -0.14, "records", ha="center", va="center", fontsize=FS(8.0), color=SLATE)
ax1.legend(wedges, [f"{l}  ({v})" for l, v in zip(lab, w)],
           loc="upper center", bbox_to_anchor=(0.5, -0.02), fontsize=FS(7.0), ncol=2,
           handlelength=1.0, handletextpad=0.5, columnspacing=1.2)
ax1.set_title("Study architecture", pad=2)


ep_items = sorted(ep.items(), key=lambda kv: kv[1])
ax2.barh([k for k, _ in ep_items], [v for _, v in ep_items],
         color=[SEQ[i % len(SEQ)] for i in range(len(ep_items))][::-1],
         height=0.62, zorder=3)
for i, (_, v) in enumerate(ep_items):
    ax2.text(v + max(ep.values()) * 0.018, i, str(v), va="center", fontsize=FS(8.4),
             fontweight="bold", color=INK)
ax2.set_xlim(0, max(ep.values()) + 1)
ax2.set_xlabel("Records")
ax2.set_title("Health endpoint / organ system", pad=2)
ax2.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax2.set_axisbelow(True)
despine(ax2, keep=("bottom",)); ax2.tick_params(axis="y", length=0)
ax2.tick_params(axis="y", labelsize=FS(8.2))
save(fig, "f2_design_endpoint.png")

# Split versions of the same two panels. The combined figure is the right shape for a
# daily, where both panels are small; in a rollup the architecture donut is squeezed to a
# quarter of the text width while the endpoint bar list runs to 18 rows, so the page ends
# up with a wide band of whitespace beside the donut. Emitting the panels separately lets
# a rollup template place each one where it actually fits. Same data, same colours.
# Wide-and-short so the panel fits in the whitespace under a trend figure rather than
# forcing its own page: donut left, legend as a single column to its right.
_fa, _axa = plt.subplots(figsize=SZ(8.6, 3.5))
_w, _ = _axa.pie(w, colors=SEQ[:len(w)], startangle=90, radius=1.0,
                 wedgeprops=dict(width=0.40, edgecolor=PAPER, linewidth=1.8))
_axa.text(0, 0.09, str(sum(w)), ha="center", va="center", fontsize=FS(22),
          fontweight="bold", color=DEEP)
_axa.text(0, -0.17, "records", ha="center", va="center", fontsize=FS(9.5), color=SLATE)
_axa.legend(_w, [f"{l}  ({v})" for l, v in zip(lab, w)],
            loc="center left", bbox_to_anchor=(0.92, 0.5), fontsize=FS(8.0),
            ncol=2 if len(lab) > 6 else 1,
            handlelength=1.0, handletextpad=0.5, labelspacing=0.48, columnspacing=1.1,
            frameon=False)
_axa.set_title("Study architecture", pad=6)
save(_fa, "f2a_architecture.png")

_fb, _axb = plt.subplots(figsize=SZ(9.0, max(3.4, 0.30 * len(ep) + 1.1)))
_axb.barh([k for k, _ in ep_items], [v for _, v in ep_items],
          color=[SEQ[i % len(SEQ)] for i in range(len(ep_items))][::-1],
          height=0.66, zorder=3)
for i, (_, v) in enumerate(ep_items):
    _axb.text(v + max(ep.values()) * 0.015, i, str(v), va="center", fontsize=FS(9.0),
              fontweight="bold", color=INK)
_axb.set_xlim(0, max(ep.values()) + 1)
_axb.set_xlabel("Records")
_axb.set_title("Health endpoint / organ system", pad=6)
_axb.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); _axb.set_axisbelow(True)
despine(_axb, keep=("bottom",)); _axb.tick_params(axis="y", length=0)
_axb.tick_params(axis="y", labelsize=FS(9.0))
save(_fb, "f2b_endpoint.png")

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
    "Iran": "Middle East & N. Africa", "France": "Europe", "Italy": "Europe",
    "Denmark": "Europe", "Europe": "Europe", "Kenya": "Sub-Saharan Africa",
    # added 2026-08-05 from the printed-unmapped list
    "Philippines": "Southeast Asia", "Indonesia": "Southeast Asia",
    "Malaysia": "Southeast Asia", "Singapore": "Southeast Asia",
    "Arctic Ocean": "Polar / remote marine", "Antarctica": "Polar / remote marine",
    "Southern Ocean": "Polar / remote marine",
    # added 2026-08-05: continental group names used directly as a record's geo
    "East Asia": "East Asia (ex-China)", "South Asia": "South Asia",
    "North America": "North America", "Multi-country": "Global / multi-region",
}
# Aliases and sub-national place names. `geo` is written as free text on the record
# ("Chiang Mai, Thailand", "Bogota, Colombia", "Ile-Ife, Nigeria"), so an exact-key
# lookup silently dumps everything into the fallback. On 2026-08-03 that put 20 of 25
# records into "Global / multi-region" and made the f3 right panel worthless - the same
# failure class as the design-map fall-through fixed on 01/02 Aug. Resolution is now
# exact -> alias -> substring, and anything still unresolved is PRINTED, so a new
# unmapped place is visible in the run log instead of being absorbed silently.
GEO_ALIAS = {
    "United States": "USA", "US": "USA", "U.S.": "USA",
    "United Kingdom": "UK", "Korea": "South Korea",
}
GEO_SUBSTR = [
    ("united states", "USA"), ("u.s.", "USA"), (" usa", "USA"), ("america", "USA"),
    ("united kingdom", "UK"), ("england", "UK"), ("london", "UK"), ("scotland", "UK"),
    ("china", "China"), ("shanghai", "China"), ("beijing", "China"),
    ("south korea", "South Korea"), ("seoul", "South Korea"), ("korea", "South Korea"),
    ("taiwan", "Taiwan"), ("japan", "Japan"),
    ("thailand", "Thailand"), ("chiang mai", "Thailand"), ("vietnam", "Vietnam"),
    ("india", "India"), ("bangladesh", "Bangladesh"),
    ("nigeria", "Nigeria"), ("ile-ife", "Nigeria"), ("south africa", "South Africa"),
    ("southern africa", "South Africa"), ("kenya", "Kenya"), ("ghana", "Ghana"),
    ("colombia", "Colombia"), ("bogota", "Colombia"), ("brazil", "Brazil"),
    ("mexico", "Mexico"), ("medellin", "Colombia"),
    ("germany", "Germany"), ("spain", "Spain"), ("cartagena", "Spain"),
    ("france", "France"), ("italy", "Italy"), ("poland", "Poland"),
    ("netherlands", "Netherlands"), ("denmark", "Denmark"), ("norway", "Norway"),
    ("greece", "Greece"), ("europe", "Europe"),
    ("canada", "Canada"), ("iran", "Iran"), ("turkiye", "Turkiye"),
    ("australia", "Australia"),
    ("global", "Global"), ("multi-region", "Global"), ("worldwide", "Global"),
    # surfaced by the unmapped diagnostic when it was first run over 31 Jul - 2 Aug;
    # these matter for the weekly/monthly rollups, not just for today's issue
    ("hong kong", "China"), ("finland", "Norway"), ("northern ireland", "UK"),
    ("ireland", "Europe"), ("bulgaria", "Bulgaria"), ("sofia", "Bulgaria"),
    ("antwerp", "Europe"), ("oslo", "Norway"), ("zagreb", "Europe"),
    ("siberia", "Global"), ("multi-country", "Global"), ("czech", "Czech Republic"),
    ("pakistan", "India"), ("indonesia", "Vietnam"), ("malaysia", "Vietnam"),
    ("singapore", "Vietnam"), ("egypt", "Turkiye"), ("saudi", "Turkiye"),
    ("new zealand", "Australia"), ("switzerland", "Europe"), ("sweden", "Norway"),
    ("belgium", "Europe"), ("austria", "Europe"), ("portugal", "Europe"),
    # added 2026-08-05
    ("philippines", "Philippines"), ("quezon city", "Philippines"), ("manila", "Philippines"),
    ("arctic", "Arctic Ocean"), ("svalbard", "Arctic Ocean"), ("antarctic", "Antarctica"),
    ("benevento", "Italy"), ("salt lake city", "USA"),
]
# Labels that are honestly not geographic. They belong in the fallback bucket by
# intent, not by accident, so they must not trip the unmapped warning.
GEO_NONGEO = ("chamber", "laboratory", "lab ", "n/a", "not stated", "not applicable",
              "method", "synthetic", "simulation", "in vitro", "in silico", "deposit",
              "computational", "no site", "theoretical", "modelled only")
_geo_unmapped = set()
def geo_of(g):
    g = (g or "").strip()
    if g in geo_group:
        return geo_group[g]
    if GEO_ALIAS.get(g) in geo_group:
        return geo_group[GEO_ALIAS[g]]
    low = g.lower()
    for needle, key in GEO_SUBSTR:
        if needle in low:
            return geo_group[key]
    # A chamber/methods paper with no field site is genuinely not geographic.
    if any(w in low for w in GEO_NONGEO) or not low:
        return "Global / multi-region"
    _geo_unmapped.add(g)
    return "Global / multi-region"

geo = collections.Counter(geo_of(p["geo"]) for p in PAPERS)
if _geo_unmapped:
    print("!! geo unmapped (add to geo_group/GEO_SUBSTR):", sorted(_geo_unmapped))
if _design_unmapped:
    print("!! design unmapped (add to design_group):", sorted(_design_unmapped))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=SZ(9.4, 3.9),
                               gridspec_kw={"wspace": 0.46})
pi = sorted(pmc.items(), key=lambda kv: kv[1])
ax1.barh([k for k, _ in pi], [v for _, v in pi],
         color=[TEAL, SKY, SAGE, AMBER, CLAY, VIOLET, DEEP][:len(pi)][::-1],
         height=0.6, zorder=3)
for i, (_, v) in enumerate(pi):
    ax1.text(v + max(pmc.values()) * 0.018, i, str(v), va="center", fontsize=FS(8.4), fontweight="bold")
ax1.set_xlim(0, max(pmc.values()) + 1.2)
ax1.set_title("Particle metric under study", pad=8)
ax1.set_xlabel("Records")
ax1.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax1.set_axisbelow(True)
despine(ax1, keep=("bottom",)); ax1.tick_params(axis="y", length=0, labelsize=FS(8.2))

gi = sorted(geo.items(), key=lambda kv: kv[1])
ax2.barh([k for k, _ in gi], [v for _, v in gi],
         color=[DEEP, TEAL, SKY, SAGE, AMBER, CLAY, CORAL, VIOLET][:len(gi)][::-1],
         height=0.6, zorder=3)
for i, (_, v) in enumerate(gi):
    ax2.text(v + max(geo.values()) * 0.018, i, str(v), va="center", fontsize=FS(8.4), fontweight="bold")
ax2.set_xlim(0, max(geo.values()) + 1.2)
ax2.set_title("Geographic provenance of evidence", pad=8)
ax2.set_xlabel("Records")
ax2.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax2.set_axisbelow(True)
despine(ax2, keep=("bottom",)); ax2.tick_params(axis="y", length=0, labelsize=FS(8.2))
save(fig, "f3_metric_geography.png")

# ---------------------------------------------------------------- 4. subtopic x design heatmap
subs = [k for k, _ in counts.most_common()]
dgs  = [k for k, _ in dg.most_common()]
M = np.zeros((len(subs), len(dgs)))
for p in PAPERS:
    M[subs.index(p["sub"]), dgs.index(dgrp(p["design"]))] += 1

from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("pm", [PAPER, "#BFD8DD", SKY, TEAL, DEEP])

fig, ax = plt.subplots(figsize=SZ(7.8, 4.6))
im = ax.imshow(M, cmap=cmap, aspect="auto", vmin=0, vmax=max(3, M.max()))
ax.set_xticks(range(len(dgs))); ax.set_xticklabels(dgs, rotation=32, ha="right", fontsize=FS(7.8))
ax.set_yticks(range(len(subs))); ax.set_yticklabels(subs, fontsize=FS(8.2))
for i in range(len(subs)):
    for j in range(len(dgs)):
        if M[i, j] > 0:
            ax.text(j, i, int(M[i, j]), ha="center", va="center", fontsize=FS(8.6),
                    fontweight="bold", color=PAPER if M[i, j] >= 2 else INK)
ax.set_xticks(np.arange(-.5, len(dgs), 1), minor=True)
ax.set_yticks(np.arange(-.5, len(subs), 1), minor=True)
ax.grid(which="minor", color=PAPER, lw=2.0)
ax.tick_params(which="minor", length=0); ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title("Where the work is happening: subtopic x study architecture", pad=10)
cb = fig.colorbar(im, ax=ax, fraction=0.024, pad=0.02)
cb.outline.set_visible(False); cb.ax.tick_params(length=0, labelsize=FS(7.5))
save(fig, "f4_heatmap.png")

# ---------------------------------------------------------------- 5. forest plot
# At 62 pooled estimates a single panel is unreadable however tall it gets, because the
# page caps its height. Split into equal panels of <=32 rows, each rendered on its own
# page by the document. Daily issues (few estimates) still get exactly one panel.
_ALL = sorted(EFFECTS, key=lambda d: d["est"])
_MAXROWS = 32 if (_S and _E) else 999
_CHUNKS = [_ALL[i:i + _MAXROWS] for i in range(0, len(_ALL), _MAXROWS)] or [[]]

colmap = collections.defaultdict(lambda: SLATE, {"HR": TEAL, "OR": CLAY, "IRR": VIOLET,
          "RR-equiv": SAGE, "RR": SAGE, "beta": SKY, "%": AMBER, "r": DEEP})
def _hasci(e):
    return e.get("lo") is not None and e.get("hi") is not None and e["hi"] > e["lo"]

# a common x-range across panels so the eye can compare them
_glo = min([e["lo"] for e in _ALL if e.get("lo") is not None] + [e["est"] for e in _ALL] + [1.0])
_ghi = max([e["hi"] for e in _ALL if e.get("hi") is not None] + [e["est"] for e in _ALL] + [1.0])

for _ci, E in enumerate(_CHUNKS):
    if not E:
        continue
    _fs = (8.6 if (_S and _E) else (7.4 if len(E) <= 20 else 6.6))
    # Row pitch has to beat the label height AFTER the page scales the panel to
    # \linewidth. 0.30in/row rendered at ~11pt of page space for an 8.6pt two-line
    # label; 0.55 gives ~17pt and is legible.
    _fh = max(4.6, (0.55 if (_S and _E) else 0.30) * len(E) + 1.9)
    fig, ax = plt.subplots(figsize=((10.2 if (_S and _E) else 8.0), _fh))
    y = np.arange(len(E))
    for i, e in enumerate(E):
        c = colmap[e["metric"]]
        if _hasci(e):
            ax.plot([e["lo"], e["hi"]], [i, i], color=c, lw=2.2, solid_capstyle="round", zorder=3)
            ax.plot([e["lo"], e["lo"]], [i - .16, i + .16], color=c, lw=1.5, zorder=3)
            ax.plot([e["hi"], e["hi"]], [i - .16, i + .16], color=c, lw=1.5, zorder=3)
        ax.scatter([e["est"]], [i], s=52, color=c, zorder=4, edgecolor=PAPER, linewidth=1.0)
        _lbl = (f"{e['est']:.4g} ({e['lo']:.4g}-{e['hi']:.4g})" if _hasci(e)
                else f"{e['est']:.4g} (no CI reported)")
        ax.text(1.025, i, _lbl, transform=ax.get_yaxis_transform(which="grid"),
                fontsize=_fs, va="center", ha="left", color=SLATE, family="monospace")
    ax.axvline(1.0, color=CORAL, lw=1.1, ls="--", zorder=2)
    ax.set_xscale("log")
    _pad = (_ghi / _glo) ** 0.10
    ax.set_xlim(_glo / _pad, _ghi * _pad)
    _cand = [0.5, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5, 2, 3, 5, 9]
    _tk = [t for t in _cand if _glo / _pad <= t <= _ghi * _pad]
    ax.set_xticks(_tk); ax.set_xticklabels([("%g" % t) for t in _tk])
    ax.get_xaxis().set_minor_formatter(plt.NullFormatter())
    ax.set_yticks(y)
    def _clip(x, n):
        x = str(x)
        return x if len(x) <= n else x[:n - 1].rstrip(" ,;-") + "\u2026"
    # Long y-labels blow up the figure width under bbox_inches="tight", which then forces
    # the whole panel to be scaled down to \linewidth and undoes the extra height.
    ax.set_yticklabels([f"{_clip(e['label'], 46)}\n{_clip(e['exposure'], 26)}  |  "
                        f"{_clip(e['src'].split(' (')[0], 24)}" for e in E], fontsize=_fs)
    ax.set_xlabel("Effect estimate (log scale); dashed line = null")
    ax.set_ylim(-0.7, len(E) - 0.3)
    _ttl = "Quantitative associations reported in %s corpus" % ("the period's" if (_S and _E) else "today's")
    if len(_CHUNKS) > 1:
        _ttl += "  (%d of %d)" % (_ci + 1, len(_CHUNKS))
    ax.set_title(_ttl, pad=10)
    ax.xaxis.grid(True, color=GRID, lw=0.7, zorder=0); ax.set_axisbelow(True)
    despine(ax, keep=("bottom",)); ax.tick_params(axis="y", length=0)
    _used = [m for m in dict.fromkeys(e["metric"] for e in E)]
    handles = [plt.Line2D([], [], color=colmap[m], lw=2.4, label=m) for m in _used]
    ax.legend(handles=handles, loc="lower right", fontsize=_fs, ncol=max(1, len(handles)),
              bbox_to_anchor=(1.0, -0.22 * (4.6 / _fh)))
    save(fig, "f5_forest.png" if _ci == 0 else "f5_forest_%d.png" % (_ci + 1))

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
fig, ax = plt.subplots(figsize=SZ(8.4, 2.75))
xs = np.arange(len(stages))
ax.plot(xs, [0] * len(xs), color=GRID, lw=3, zorder=1, solid_capstyle="round")
for i, (s, n, note) in enumerate(zip(stages, stage_hits, stage_note)):
    c = SEQ[i]
    ax.scatter([i], [0], s=120 + 95 * n, color=c, zorder=3,
               edgecolor=PAPER, linewidth=2.0, alpha=0.92)
    ax.text(i, 0, str(n), ha="center", va="center", color=PAPER,
            fontsize=FS(10), fontweight="bold", zorder=4)
    ax.text(i, 0.62, s, ha="center", va="bottom", fontsize=FS(8.4), fontweight="bold", color=INK)
    ax.text(i, -0.62, note, ha="center", va="top", fontsize=FS(7.2), color=SLATE)
ax.set_xlim(-0.55, len(stages) - 0.45); ax.set_ylim(-1.5, 1.35)
ax.axis("off")
ax.set_title("Life-course windows addressed %s (records may span several stages)" % PERIODWORD,
             pad=6, fontsize=FS(10))
save(fig, "f6_lifecourse.png")

print("figures:", sorted(os.listdir(OUT)))
print("n_papers:", len(PAPERS))
print("subtopics:", dict(counts))
print("designs:", dict(dg))
print("geo:", dict(geo))
print("pm:", dict(pmc))
