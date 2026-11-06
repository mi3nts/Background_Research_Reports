# -*- coding: utf-8 -*-
"""Insight figures added 2026-11-01 (x1-x4). Run after plots.py with the same env
(PMRW_DATE, or PMRW_START+PMRW_END; PMRW_FIGDIR). Writes PNGs plus
<FIGDIR>/extra_figs.tex: figure blocks with data-derived captions, so a daily issue or a
rollup can \\input it without hand-writing counts.

x1_exposure_basis   how the exposure / PM quantity was obtained (low-cost sensor, reference
                    monitor, lab instrument, satellite-fused, model, proxy) by corpus side;
                    right panel: measured vs modelled vs proxy share per health subtopic.
x4_evidence_grade   tier A/B/C mix per subtopic (where the strong evidence sits).
x2_effect_funnel    ratio-scale estimates: ln(estimate) vs SE from the CI, coloured by the
                    exposure increment the authors used; Egger asymmetry test when n>=10.
                    Rollups always; a daily only when it has >=6 ratio estimates.
x3_series           rollups only: every Sun-Sat week in the archive up to PMRW_END
                    (health vs measurement records, tier-A %, metadata-only %), period shaded.
"""
import os, re, json, glob, math, collections, datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import corpus
from corpus import PAPERS, EFFECTS

S, E = os.environ.get("PMRW_START"), os.environ.get("PMRW_END")
ROLL = bool(S and E)
OUT = os.environ.get("PMRW_FIGDIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig")
os.makedirs(OUT, exist_ok=True)
K = 1.3 if ROLL else 1.0
INK, SLATE, PAPER, GRID = "#14262E", "#4A6572", "#FBF9F5", "#D9D3C9"
DEEP, TEAL, SKY, SAGE, AMBER, CLAY, CORAL, VIOLET, MUSK = ("#0F4C5C", "#1F7A8C", "#4FA3C4",
    "#6FA287", "#E3A008", "#B5643C", "#D1495B", "#6A5B9E", "#8A7E72")
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9 * K, "axes.edgecolor": SLATE,
    "axes.labelcolor": INK, "text.color": INK, "xtick.color": SLATE, "ytick.color": SLATE,
    "axes.titlesize": 10.5 * K, "axes.titleweight": "bold", "figure.facecolor": PAPER,
    "axes.facecolor": PAPER, "savefig.facecolor": PAPER, "legend.frameon": False})
MEAS_SIDE = {corpus.SENS, corpus.EXPO}
HEALTH = [s for s in corpus.SUBTOPICS if s not in MEAS_SIDE]
BLOCKS = []

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=300, bbox_inches="tight", pad_inches=0.14); plt.close(fig)

def despine(ax):
    for s in ("top", "right"): ax.spines[s].set_visible(False)

def block(fn, cap):
    BLOCKS.append("\\noindent\\begin{minipage}{\\linewidth}\\includegraphics[width=\\linewidth]{\\FIGDIR/%s}\n"
                  "\\figcap{%s}\\end{minipage}\n\n\\vspace{2mm}\n" % (fn, cap))

def pct(a, b): return "%d\\,\\%%" % round(100.0 * a / b) if b else "--"

# ------------------------------------------------------------------ x1 exposure basis
RULES = [
 ("Low-cost sensor / network", r"low[- ]cost|purpleair|plantower|pms ?5003|pms ?7003|sps30|opc-n|alphasense|"
                               r"sensor network|\blcs\b|micro-?sensor|consumer[- ]grade|clarity node|airbeam|atmotube"),
 ("Personal / wearable", r"personal (exposure|monitor|sampl)|wearable|backpack|mobile monitor|breathing[- ]zone"),
 ("Satellite-fused", r"chinahighairpollutants|\bchap\b|van donkelaar|\bacag\b|satellite|\baod\b|maiac|modis|viirs|tropomi|himawari|geostationary|remote[- ]sens"),
 ("Model (CTM / LUR / ML)", r"\bctm\b|chemical transport|cmaq|geos-?chem|wrf|camx|dispersion|land[- ]use regression|"
                           r"\blur\b|machine[- ]learning|random forest|xgboost|reanalysis|merra|\bcams\b|model|"
                           r"ensemble|emulat|forecast|gridded|kriging|interpolat|inventory|emission factor"),
 ("Genetic / biomarker proxy", r"genetic|mendelian|gwas|methylation|protein signature|risk score|biomarker"),
 ("Lab / research instrument", r"sampled|sampling|direct-reading|niosh|campaign|tower|vertical profile|single-particle|"
                               r"fluorescence|deposition|road dust|size distribution|gravimetric|filter|speciat|icp-?ms|xrf|\bams\b|acsm|aethalometer|\bcpc\b|smps|"
                               r"\baps\b|nephelometer|lidar|tof|mass spectrom|chamber|in vitro|in vivo|instill|"
                               r"mice|\brats?\b|cell line|organoid|dose"),
 ("Reference / regulatory monitor", r"monitor|station|\bfem\b|\bfrm\b|\bbam\b|teom|regulatory|\baqs\b|airnow|network"),
 ("Proxy / questionnaire", r"proxy|distance|proximity|near (major )?road|fuel|biomass|cookstove|self-?report|"
                           r"questionnaire|occupation|job[- ]exposure|smok|wildfire (day|season|event)|residen"),
]
MEASURED = {"Low-cost sensor / network", "Personal / wearable", "Lab / research instrument", "Reference / regulatory monitor"}
MODELLED = {"Satellite-fused", "Model (CTM / LUR / ML)"}
PROXY = {"Proxy / questionnaire", "Genetic / biomarker proxy"}
BCOL = {"Low-cost sensor / network": AMBER, "Personal / wearable": CLAY, "Lab / research instrument": VIOLET,
        "Reference / regulatory monitor": TEAL, "Satellite-fused": SKY, "Model (CTM / LUR / ML)": MUSK,
        "Proxy / questionnaire": SAGE, "Genetic / biomarker proxy": CORAL, "Review / no primary exposure": "#C9BFAF",
        "Not stated / metadata only": GRID}

def basis(p):
    if p.get("basis") in BCOL: return p["basis"]          # author-declared (optional field)
    if p.get("basis") == "Not stated": return "Not stated / metadata only"  # 2026-11-06: an explicit declaration beats the regex
    if p["design"].lower().startswith("metadata only"): return "Not stated / metadata only"
    s = (p.get("pm") or "").lower()
    for lab, rx in RULES:
        if re.search(rx, s): return lab
    if re.search(r"review|meta-analys|synthesis|commentary|editorial|guideline", (p.get("design") or "").lower()):
        return "Review / no primary exposure"
    # methods part of the summary only: the limitation and relevance sentences routinely
    # mention low-cost sensing and would bias the class (2026-11-01)
    t = re.split(r"limitation|relevance", (p.get("n") or "").lower())[0] + " " + (p.get("design") or "").lower()
    for lab, rx in RULES:
        if re.search(rx, t): return lab
    return "Not stated / metadata only"

def kind(b):
    return "measured" if b in MEASURED else "modelled" if b in MODELLED else "proxy" if b in PROXY else "none"

if PAPERS:
    B = [(p, basis(p)) for p in PAPERS]
    order = [r[0] for r in RULES] + ["Review / no primary exposure", "Not stated / metadata only"]
    cm = collections.Counter(b for p, b in B if p["sub"] in MEAS_SIDE)
    ch = collections.Counter(b for p, b in B if p["sub"] not in MEAS_SIDE)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.6 * (1.15 if ROLL else 1), 3.9 * (1.3 if ROLL else 1)),
                                 gridspec_kw=dict(width_ratios=[1.15, 1], wspace=0.85))
    y = np.arange(len(order))[::-1]
    vm = np.array([cm[o] for o in order]); vh = np.array([ch[o] for o in order])
    a1.barh(y, vm, color=AMBER, height=0.62, label="Measurement side (sensing + exposure)", zorder=3)
    a1.barh(y, vh, left=vm, color=TEAL, height=0.62, label="Health side", zorder=3)
    for yi, m, h in zip(y, vm, vh):
        if m + h: a1.text(m + h + 0.15 * K, yi, str(m + h), va="center", fontsize=8.6 * K, fontweight="bold")
    a1.set_yticks(y); a1.set_yticklabels(order, fontsize=8.2 * K)
    a1.set_xlabel("Records"); a1.grid(axis="x", color=GRID, zorder=0); despine(a1)
    a1.set_title("How the PM quantity was obtained", pad=8)
    a1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=7.6 * K)
    subs = [s for s in HEALTH if any(p["sub"] == s and kind(b) != "none" for p, b in B)]
    rows = []
    for s in subs:
        c = collections.Counter(kind(b) for p, b in B if p["sub"] == s and kind(b) != "none")
        n = sum(c.values()); rows.append((s, n, c["measured"] / n, c["modelled"] / n, c["proxy"] / n))
    rows.sort(key=lambda r: r[3])
    yy = np.arange(len(rows))
    if rows:
        me = np.array([r[2] for r in rows]); mo = np.array([r[3] for r in rows]); pr = np.array([r[4] for r in rows])
        a2.barh(yy, me, color=TEAL, height=0.62, label="Measured", zorder=3)
        a2.barh(yy, mo, left=me, color=MUSK, height=0.62, label="Modelled / satellite", zorder=3)
        a2.barh(yy, pr, left=me + mo, color=SAGE, height=0.62, label="Proxy", zorder=3)
        a2.set_yticks(yy); a2.set_yticklabels(["%s (n=%d)" % (r[0], r[1]) for r in rows], fontsize=8.0 * K)
        a2.set_xlim(0, 1); a2.set_xticks([0, .25, .5, .75, 1]); a2.set_xticklabels(["0", "25", "50", "75", "100%"])
        a2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, fontsize=7.6 * K)
    a2.set_title("Health side: exposure basis", pad=8); despine(a2)
    save(fig, "x1_exposure_basis.png")
    hk = collections.Counter(kind(b) for p, b in B if p["sub"] not in MEAS_SIDE and kind(b) != "none")
    nh = sum(hk.values()); lcs = cm["Low-cost sensor / network"] + ch["Low-cost sensor / network"]
    block("x1_exposure_basis.png",
          "How each record obtained its PM quantity, classified from the exposure field. %d of %d records "
          "rest on a low-cost sensor or sensor network; %d on reference or regulatory monitors. Health side, "
          "where an exposure basis is recoverable (n=%d): measured %s, modelled or satellite-fused %s, proxy %s. "
          "Right panel sorted by modelled share: the subtopics at the bottom are where a measured low-cost "
          "network exposure would add most." % (lcs, len(PAPERS), cm["Reference / regulatory monitor"] +
          ch["Reference / regulatory monitor"], nh, pct(hk["measured"], nh), pct(hk["modelled"], nh), pct(hk["proxy"], nh)))

# ------------------------------------------------------------------ x4 evidence grade
if PAPERS:
    subs = [s for s in corpus.SUBTOPICS if any(p["sub"] == s for p in PAPERS)]
    T = {s: collections.Counter(p["tier"] for p in PAPERS if p["sub"] == s) for s in subs}
    subs.sort(key=lambda s: T[s]["A"] / max(1, sum(T[s].values())))
    fig, ax = plt.subplots(figsize=(7.6 * (1.3 if ROLL else 1), 0.36 * len(subs) * K + 1.2))
    left = np.zeros(len(subs))
    for t, c in (("A", DEEP), ("B", SKY), ("C", GRID)):
        v = np.array([T[s][t] for s in subs], float)
        ax.barh(range(len(subs)), v, left=left, color=c, height=0.64, label="Tier " + t, zorder=3)
        for i, (l, x) in enumerate(zip(left, v)):
            if x: ax.text(l + x / 2, i, int(x), ha="center", va="center", fontsize=7.8 * K,
                          color=PAPER if t != "C" else INK, fontweight="bold")
        left += v
    ax.set_yticks(range(len(subs))); ax.set_yticklabels(subs, fontsize=8.2 * K)
    ax.set_xlabel("Records"); despine(ax); ax.grid(axis="x", color=GRID, zorder=0)
    ax.legend(loc="lower right", fontsize=7.8 * K); ax.set_title("Evidence grade by subtopic (sorted by tier-A share)", pad=8)
    save(fig, "x4_evidence_grade.png")
    tA = sum(T[s]["A"] for s in subs); top = subs[-1]
    block("x4_evidence_grade.png",
          "Tier mix per subtopic. %d of %d records are tier A (%s). Highest tier-A share: \\textit{%s} "
          "(%d of %d)." % (tA, len(PAPERS), pct(tA, len(PAPERS)), top.replace("&", "\\&"), T[top]["A"], sum(T[top].values())))

# ------------------------------------------------------------------ x2 effect funnel
RATIO = {"HR", "RR", "OR", "IRR", "RR-equiv", "aHR", "aOR", "aRR", "SHR", "sHR", "MRR", "RRR", "PR", "GMR", "TR", "Ratio", "ratio"}  # PR etc. added 2026-11-04
def incr(e):
    if e.get("inc") in ICOL: return e["inc"]              # author-declared (optional field)
    s = (e.get("exposure") or "").lower()
    if re.search(r"per ?10 ?(µ|u|ug|μ)", s) or "per 10 " in s: return "per 10 µg/m³"
    if "iqr" in s or re.search(r"per [^,]*\bsd\b", s): return "per IQR / SD"
    if re.search(r"per ?(1|one) ?(µ|u|ug|μ)|per unit|per 1 ", s): return "per 1 µg/m³ / unit"
    if re.search(r"->| to \d| vs |versus|highest|quartile|quintile|tertile|high |exposed|any |categor", s): return "categorical contrast"
    return "increment not recorded"
ICOL = {"per 10 µg/m³": TEAL, "per IQR / SD": AMBER, "per 1 µg/m³ / unit": CORAL,
        "categorical contrast": VIOLET, "increment not recorded": MUSK}
R = [e for e in EFFECTS if e.get("metric") in RATIO and e.get("lo") and e.get("hi") and e["lo"] > 0 and e["hi"] > e["lo"] and e["est"] > 0]
if (ROLL and len(R) >= 4) or len(R) >= 6:
    x = np.array([math.log(e["est"]) for e in R]); se = np.array([(math.log(e["hi"]) - math.log(e["lo"])) / 3.92 for e in R])
    se = np.where(se <= 0, 1e-4, se); c0 = float(np.median(x))
    fig, ax = plt.subplots(figsize=(7.4 * (1.25 if ROLL else 1), 4.6 * (1.25 if ROLL else 1)))
    smax = float(se.max()) * 1.08; ss = np.linspace(0, smax, 50)
    ax.fill_betweenx(ss, c0 - 1.96 * ss, c0 + 1.96 * ss, color="#E9E4DA", zorder=0, label="95% pseudo-CI about median")
    ax.plot(-1.96 * ss, ss, color=SLATE, lw=0.7, ls=":", zorder=1); ax.plot(1.96 * ss, ss, color=SLATE, lw=0.7, ls=":", zorder=1)
    ax.axvline(0, color=INK, lw=0.9); ax.axvline(c0, color=DEEP, lw=0.9, ls="--")
    for k, c in ICOL.items():
        m = [i for i, e in enumerate(R) if incr(e) == k]
        if m: ax.scatter(x[m], se[m], s=34 * K, color=c, edgecolor=INK, lw=0.4, zorder=3, label="%s (%d)" % (k, len(m)))
    ax.set_ylim(smax, 0); ax.set_xlabel("ln(ratio estimate)   [dotted: p = 0.05 boundary about the null]")
    ax.set_ylabel("Standard error of ln estimate (from 95% CI)"); despine(ax); ax.grid(color=GRID, lw=0.5, zorder=0)
    ax.legend(fontsize=7.4 * K, loc="lower left" if c0 > 0 else "lower right")
    ax.set_title("Ratio-scale estimates: precision vs magnitude", pad=8)
    eg = ""
    nsrc = len({(e.get("src") or "?") for e in R})   # 2026-11-06: estimates from one cohort are not independent studies
    if len(R) >= 10 and nsrc < 10:
        eg = " Egger regression not computed: the %d estimates come from %d sources and are not independent." % (len(R), nsrc)
    elif len(R) >= 10:
        z = x / se; pr = 1 / se; A = np.vstack([np.ones_like(pr), pr]).T
        coef, res, *_ = np.linalg.lstsq(A, z, rcond=None); n = len(z)
        resid = z - A @ coef; s2 = resid @ resid / (n - 2); cov = s2 * np.linalg.inv(A.T @ A)
        tb = coef[0] / math.sqrt(cov[0, 0]); p = math.erfc(abs(tb) / math.sqrt(2))
        eg = (" Egger regression intercept %.2f (SE %.2f, normal-approx.\\ p=%.3f, n=%d)%s." %
              (coef[0], math.sqrt(cov[0, 0]), p, n, " --- asymmetry: small imprecise estimates sit on the harmful side"
               if (p < 0.1 and coef[0] > 0) else ""))
    save(fig, "x2_effect_funnel.png")
    ic = collections.Counter(incr(e) for e in R)
    sig = sum(1 for e in R if e["lo"] > 1 or e["hi"] < 1)
    block("x2_effect_funnel.png",
          "Every ratio-scale estimate (n=%d) plotted as ln(estimate) against its standard error, coloured by the "
          "exposure increment the authors reported. %d of %d exclude the null. Increments: %s. Because "
          "increments differ (per 1 unit, per 10\\,$\\mu$g/m$^3$, per IQR, categorical), the spread is not "
          "a heterogeneity estimate and the median line is not a pooled effect; the plot shows whether "
          "precision and magnitude co-vary.%s" % (len(R), sig, len(R), ", ".join("%s %d" % (k.replace("\u00b5g/m\u00b3", "$\\mu$g/m$^3$"), v) for k, v in ic.most_common()), eg))

# ------------------------------------------------------------------ x3 archive series (rollups)
if ROLL:
    end = dt.date.fromisoformat(E); weeks = collections.OrderedDict()
    for f in sorted(glob.glob(os.path.join(corpus.STORE, "*.json"))):
        j = json.load(open(f)); d = dt.date.fromisoformat(j["date"])
        if d > end: continue
        wk = d - dt.timedelta(days=(d.weekday() + 1) % 7)
        w = weeks.setdefault(wk, collections.Counter())
        for p in j["PAPERS"]:
            w["n"] += 1; w["meas" if p["sub"] in MEAS_SIDE else "health"] += 1
            w["A"] += p["tier"] == "A"; w["meta"] += p["design"].lower().startswith("metadata only")
            w["lcs"] += basis(p) == "Low-cost sensor / network"
        w["eff"] += len(j["EFFECTS"])
    if len(weeks) >= 3:
        ks = list(weeks); X = np.arange(len(ks)); W = [weeks[k] for k in ks]
        fig, ax = plt.subplots(figsize=(11.5, 4.6))
        hm = np.array([w["health"] for w in W]); ms = np.array([w["meas"] for w in W])
        ax.bar(X, ms, color=AMBER, width=0.72, label="Measurement side", zorder=3)
        ax.bar(X, hm, bottom=ms, color=TEAL, width=0.72, label="Health side", zorder=3)
        ax.plot(X, [w["lcs"] for w in W], color=INK, marker="o", ms=3.5, lw=1.1, label="Low-cost-sensor records", zorder=4)
        s0 = dt.date.fromisoformat(S)
        inper = [i for i, k in enumerate(ks) if k + dt.timedelta(days=6) >= s0]
        if inper: ax.axvspan(inper[0] - 0.5, X[-1] + 0.5, color="#EFE7D6", zorder=0, label="This period")
        ax.set_ylabel("Records per Sun-Sat week"); despine(ax); ax.grid(axis="y", color=GRID, zorder=0)
        ax2 = ax.twinx()
        ax2.plot(X, [100 * w["A"] / max(1, w["n"]) for w in W], color=CORAL, lw=1.6, label="Tier A (%)")
        ax2.plot(X, [100 * w["meta"] / max(1, w["n"]) for w in W], color=VIOLET, lw=1.6, ls="--", label="Metadata only (%)")
        ax2.set_ylim(0, 60); ax2.set_ylabel("% of week's records"); ax2.spines["top"].set_visible(False)
        step = max(1, len(ks) // 14)
        ax.set_xticks(X[::step]); ax.set_xticklabels([k.strftime("%d %b") for k in ks][::step], rotation=0, fontsize=8)
        h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
        ax.legend(h1 + h2, l1 + l2, loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=6, fontsize=7.6)
        ax.set_title("The archive so far: weekly volume, measurement share and evidence quality", pad=8)
        save(fig, "x3_series.png")
        tot = sum(w["n"] for w in W); pn = len(PAPERS); pm = sum(1 for p in PAPERS if p["sub"] in MEAS_SIDE)
        block("x3_series.png",
              "All %d Sunday--Saturday weeks in the archive up to %s (%d records). This period (shaded): "
              "measurement side %s of %d records, versus %s across the archive. Tier-A and metadata-only shares "
              "on the right axis; partial first and last weeks are drawn as recorded." %
              (len(ks), E, tot, pct(pm, pn), pn, pct(sum(w["meas"] for w in W), tot)))

open(os.path.join(OUT, "extra_figs.tex"), "w").write("".join(BLOCKS))
print("plots_extra:", OUT, len(BLOCKS), "figures")
