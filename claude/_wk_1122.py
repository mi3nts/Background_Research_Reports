# -*- coding: utf-8 -*-
"""Author build/weekly.tex for W47 (15-21 Nov 2026) from the W46 source (2026-11-22 run).
Numbers from _wkstats_1122.py; trial watch read from state/trials.json at write time."""
import json
s = open("issues/weekly_2026-11-14.tex").read()
def rep(old, new):
    global s
    assert old in s, old[:70]; s = s.replace(old, new)
rep(r"\newcommand{\DIGESTDATE}{14 November 2026}", r"\newcommand{\DIGESTDATE}{21 November 2026}")
rep(r"\newcommand{\PERIODSTART}{8 November 2026}", r"\newcommand{\PERIODSTART}{15 November 2026}")
rep(r"\newcommand{\PERIODEND}{14 November 2026}", r"\newcommand{\PERIODEND}{21 November 2026}")
rep(r"\mbox{157 records pooled from 7 daily issues}", r"\mbox{145 records pooled from 7 daily issues}")
i = s.index(r"\begin{minipage}[t]{0.190\linewidth}\metric{157}"); j = s.index(r"\vspace{6mm}", i)
s = s[:i] + r"""\begin{minipage}[t]{0.190\linewidth}\metric{145}{RECORDS POOLED\\(145 UNIQUE DOIs)}{Deep}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{38\%}{MEASUREMENT SIDE\\(55 RECORDS)}{Teal}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{9}{LOW-COST SENSOR\\RECORDS (6\%)}{Sky}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{25}{POOLED EFFECT\\ESTIMATES (25 WITH A CI)}{Amber}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{40}{ABSTRACT-FREE\\(28\% OF WEEK)}{Clay}\end{minipage}

""" + s[j:]

# ---- trial watch from state/trials.json
T = json.load(open("state/trials.json"))
W = [w for w in T.get("windows", []) if w.get("window", "")[-10:] >= "2026-11-17"]
ntr = len(T.get("trials", {})) if isinstance(T.get("trials"), (dict, list)) else T.get("trials")
nwin = len(T.get("windows", []))
newest = W[-1] if W else {}
extra = ""
if newest and newest.get("window", "")[-10:] >= "2026-11-21":
    extra = (r" The window queried on this run (\texttt{%s}) returned %s hits, %s kept." %
             (newest["window"].replace("->", "to"), newest.get("hits", "?"), newest.get("kept", "?")))
TRIALS = (r"""\textbf{Trial watch.} ClinicalTrials.gov \texttt{LastUpdatePostDate} windows 17--19 and 19--20 November
(Amass TrialCore on the second): \textbf{1 added} to the register --- \textbf{NCT07539987} AIRWISE (University of
Montana), real-time air-quality monitoring plus portable air cleaning in older adults, the third registered trial in
the set whose intervention starts from \emph{a monitor reading} (after REACT, NCT07914010, now recruiting, and the
Boston University monitor-plus-messaging trial NCT07931820). INTERLUNG (NCT07540000) and REACT were carried as updates;
Amass returned 20 new registrations on 19--20 November, none on topic.""" + extra +
 r""" \texttt{trials.json} holds \textbf{%s trials} over %s query windows. \texttt{analyze\_endpoints} was not run.""" % (ntr, nwin))

i = s.index("% -------------------------------------------------------------- week in one box")
j = s.index("% -------------------------------------------------------------- digest")
SEC = lambda t, r=r"\vspace{2.5mm}": "\\section*{\\sffamily\\bfseries\\color{Deep}%s}\n\\vspace{-1.5mm}{\\color{Teal}\\rule{\\linewidth}{1.1pt}}%s\n\n" % (t, r)
BRK = "\\par\\vskip 0pt plus 14\\baselineskip\\penalty-200\\vskip 0pt plus -14\\baselineskip\n"
CAP = dict(F2A="F2A", F1="F1", F3="F3", F6="F6", F4="F4", FO1="FO1", FO2="FO2", FO3="")
try:
    exec(open("_wk_1122_caps.py").read(), {"CAP": CAP})
except FileNotFoundError:
    pass
body = "% -------------------------------------------------------------- week in one box\n" + SEC("The week in one paragraph") + r"""\begin{keybox}
{\sffamily\bfseries\small\color{Deep}The week moved indoors and underground. \textit{Occupational \& indoor} rose
from 15 to 22 records --- subway platforms, classrooms in wildfire smoke, nursing homes, ski-wax benches, milling
markets, improved stoves --- and the strongest of them measured what the ambient network cannot: wildfire-day
indoor PM$_{2.5}$ 2.72-fold higher in five New York schools (10.09 vs 3.71\,$\mu$g/m$^3$, infiltration factor
0.69--0.95), and Philadelphia subway platforms at 5.1$\times$ street-level PM$_{2.5}$ and 16.5$\times$ black carbon.
Sensing contracted (22 $\rightarrow$ 17) and turned to how evaluations are judged rather than to new failure modes.
On the health side the week's largest analyses are model-exposure cohorts with small per-increment slopes; none of
the 25 estimates rests on a low-cost sensor, for the second week running.}\\[1.4mm]
\footnotesize
\textbf{Scale.} \textbf{145 records} over seven issues on daily totals of \textbf{4}, 15, 26, 22, \textbf{34}, 33
and 11. Against recent rollups: 145 after 157, 151, 135, 119, 123 and 87. \textbf{All ten subtopics populated}
for the ninth week running.

\textbf{The measurement side held at 38\,\%} (55 records): \textit{Exposure assessment \& modelling} 40
$\rightarrow$ \textbf{38}, \textit{Sensing} 22 $\rightarrow$ \textbf{17}. Share series 39, 39, 37, 40, 39,
\textbf{38\,\%}.

\textbf{Indoor grew; burden, mechanistic and sensing fell back.} \textit{Occupational \& indoor} 15 $\rightarrow$
\textbf{22}, \textit{Other clinical} 8 $\rightarrow$ 10, \textit{Cardiovascular} 12 $\rightarrow$ 12, \textit{Neuro}
7 $\rightarrow$ 7; \textit{Burden, policy \& mitigation} 18 $\rightarrow$ \textbf{13}, \textit{Mechanistic} 16
$\rightarrow$ \textbf{11}, \textit{Respiratory} 12 $\rightarrow$ 9, \textit{Reproductive} 7 $\rightarrow$ 6.

\textbf{Estimates: 25, every one with an interval} (ninth complete week at 100\,\%), one per 5.8 records against
one per 4.5 last week. 20 on ratio scales (HR 11, OR 4, RR 3, aOR 2) and 5 on difference scales (all \% change).

\textbf{Abstract gap 40 of 145 (28\,\%)}, up from 16\,\% --- mostly Elsevier deposits on the Crossref-ISSN leg
with no abstract. \textbf{Tier mix 12 A, 38 B, 95 C} --- tier A at \textbf{8\,\%}, from 11\,\%.
\end{keybox}

\clearpage

% -------------------------------------------------------------- trend
""" + SEC("Subtopic trend and inflection") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/w1_subtopic_trend.png}
\figcap{Per-issue subtopic counts across the week from \texttt{state/metrics.csv}, seven issues, daily totals 4,
15, 26, 22, 34, 33 and 11. Sunday 15 November's 4 is the week's minimum and
Thursday 19 November's 34 its maximum. 15--16 November were built on the 17 November run (15 November recovered
from the interrupted 16 November run), 17--18 November on the 20 November 01Z run, 19 November on the 20 November
15Z run, and \textbf{20--21 November and this rollup on the 22 November run}.}

\footnotesize
\textbf{Expanding.} \textit{Occupational \& indoor} 15 $\rightarrow$ \textbf{22} is the only large gain (below).
\textit{Other clinical} 8 $\rightarrow$ 10 carries the Chongqing post-resection colorectal-cancer cohort (HR 1.079,
1.045--1.115, per 5\,$\mu$g/m$^3$ PM$_{2.5}$; organic matter HR 1.088, 1.028--1.152, per IQR) and the India NFHS-5
under-five mortality preprint (aOR 1.07, 1.04--1.10, per 10\,$\mu$g/m$^3$).

\vspace{1.2mm}
\textbf{Contracting.} \textit{Burden} 18 $\rightarrow$ 13 (four GBD secondary analyses remain the bulk);
\textit{Mechanistic toxicology} 16 $\rightarrow$ 11; \textit{Sensing} 22 $\rightarrow$ 17, with sensing tier A down
from eight to two.

\vspace{1.2mm}
\textbf{The inflection worth naming.} \textbf{Microenvironments displaced the ambient network as the measured
quantity.} Five New York K-12 schools with paired calibrated indoor/outdoor sensors (\textit{npj Clean Air}, tier A):
wildfire-day indoor PM$_{2.5}$ 10.09 vs 3.71\,$\mu$g/m$^3$, infiltration factor 0.69--0.95, rising with outdoor
temperature to a plateau near 20--25\,$^\circ$C and higher during instructional hours. Villanova, three Philadelphia
subway stations: belowground PM$_{2.5}$ 5.1$\times$, black carbon 16.5$\times$ and UFP lung-deposited surface area
1.9$\times$ street level (15th Street PM$_{2.5}$ 156.8\,$\pm$\,25.3\,$\mu$g/m$^3$). Utah ski-waxing on a low-cost
optical sensor: application-stage PM$_{2.5}$ 456--771\,$\mu$g/m$^3$, with 8\,\% of 50 workers reporting dedicated
exhaust. Cape Coast milling markets, ten months of IQAir monitors: PM$_{2.5}$ 27.0 and 28.9\,$\mu$g/m$^3$, WHO
24-h guideline exceeded on 61\,\% and 92\,\% of days. Xuanwei gasifier stoves: PM$_{2.5}$-bound PAHs 31.5 to
21.2\,ng/m$^3$. \textbf{The weakness is shared}: in each, an optical sensor calibrated on ambient aerosol meets an
aerosol it was not calibrated for --- wax fume, organic mill dust, iron-rich subway particles --- and only the New York
study reports a correction. And half of the band's 22 records (11) are metadata-only deposits: part of the
gain is volume without content.

\vspace{1.2mm}
\textbf{Last week's test} (a health or exposure-contrast estimate on a corrected low-cost network, or a wildfire
PM$_{2.5}$ split validated against one) \textbf{was met on the exposure side only.} The New York schools contrast
uses calibrated sensors with satellite smoke classification --- an exposure contrast, not a health estimate.
No health estimate this week used a sensor exposure, and no wildfire split was validated.

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f2a_architecture.png}
\figcap{""" + CAP["F2A"] + r"""}

\clearpage
% -------------------------------------------------------------- pooled analytics
""" + SEC("Pooled analytics", r"\vspace{3mm}") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f1_subtopics.png}
\figcap{""" + CAP["F1"] + r"""}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f3_metric_geography.png}
\figcap{""" + CAP["F3"] + r"""}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f6_lifecourse.png}
\figcap{""" + CAP["F6"] + r"""}

\clearpage

\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{""" + CAP["FO1"] + r"""}

\vspace{2mm}
\IfFileExists{\FIGDIR/f5_forest_2.png}{\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{""" + CAP["FO2"] + r"""}}{}

\vspace{2mm}
\IfFileExists{\FIGDIR/f5_forest_3.png}{\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_3.png}
\figcap{""" + CAP["FO3"] + r"""}}{}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f4_heatmap.png}
\figcap{""" + CAP["F4"] + r"""}

\vspace{4mm}

% -------------------------------------------------------------- exposure basis and funnel
""" + BRK + SEC("Exposure basis and the effect funnel") + r"""\footnotesize
\textbf{Exposure basis (x1).} 9 of 145 records rest on a low-cost sensor or network (6\,\%), against 12 (8\,\%)
last week and 15 of 523 (3\,\%) in October; 3 on a personal or wearable monitor. On the health side, where a basis is
recoverable (n=59), \textbf{59\,\% measured, 36\,\% modelled or satellite-fused, 5\,\% proxy}, against 52/43/5 last
week and the October baseline of 36/42/22. The measured share rose because indoor and occupational campaigns moved
into the health-side bands, and because chamber and toxicology work counts as laboratory measurement; it is not a
shift in how cohorts assign exposure. \emph{None of the 25 effect estimates rests on a low-cost sensor exposure}: the
cohorts use chemical-transport (EMEP4UK, CHAP/TAP), satellite-ML, EXPANSE or dispersion surfaces, and the only
monitor-based estimate is the Bangkok AQHI series on regulatory stations.

\vspace{1.5mm}
\textbf{Increments and precision (x2).} Of the 20 ratio estimates, 8 are per IQR or SD, 4 per 10\,$\mu$g/m$^3$,
4 categorical contrasts, 2 per 1\,$\mu$g/m$^3$ or unit, and \textbf{2 are classed ``increment not recorded''} ---
10\,\%, against 40\,\% last week. Both are the Chongqing estimates, which \emph{are} reported per 5\,$\mu$g/m$^3$, a
class the classifier does not have; in substance every ratio estimate this week carries an increment. The Egger
intercept is \textbf{3.57 (SE 1.18, n=20)}, against 2.59 (SE 0.92, n=30) last week: imprecise estimates still sit
on the harmful side. The 20 come from 10 sources with nested sets (California Teachers Study immune markers 4,
Shenzhen CKM 3, Chongqing 3), so the intercept is descriptive. The funnel is \textbf{not} a pooled estimate:
increments differ and many estimates share a sample.

\vspace{1.5mm}
\textbf{Within-family heterogeneity.} \textbf{No family qualifies this week, and no I$^2$ is reported.} The nearest
pair --- dementia in Generation Scotland (above- vs below-mean PM$_{2.5}$, HR 1.48, 1.15--1.90) and FINRISK
(source-specific PM$_{2.5}$ per 0.1\,$\mu$g/m$^3$: traffic exhaust HR 0.95, 0.85--1.05; wood combustion 1.23,
0.79--1.92) --- differs in contrast, increment and exposure source. Shenzhen's three CKM-progression estimates (per
IQR 5.0\,$\mu$g/m$^3$: overall 1.054, 1.030--1.078; early 1.073, 1.030--1.118; advanced 1.055, 1.027--1.085) share
one cohort and are not independent.

\vspace{4mm}

% -------------------------------------------------------------- venues + trials
""" + BRK + SEC("Venues, groups, trial watch, and what the pipeline did") + r"""\footnotesize
\textbf{Venues.} Research Square leads at \textbf{10}, then \textit{Atmospheric Pollution Research} \textbf{9},
\textit{Atmos Chem Phys} 7, \textit{Environ Res} 6, \textit{Environ Monit Assess} and \textit{Atmos Environ} 5
each, \textit{Environ Pollut} and \textit{Environ Int} 4 each. Research Square again supplied the sensing-relevant
preprints: the Ghana IQAir deployments, the Kampala AirQo forecasting test and the two Kolkata--Howrah network papers.

\vspace{1.5mm}
\textbf{Recurring groups.} The \texttt{affil} field is empty or ``not stated'' for 48 of 145 records (33\,\%), most of
them metadata-only Crossref deposits; no institution reaches three mentions. \textbf{Four pairs are coherent.}
\textbf{University of Cape Coast}: two IQAir deployments in Ghana (milling markets; a mining community vs background),
both uncorrected optical sensors in coarse dust. \textbf{Bule Hora University}: two GBD 2023 secondary analyses
(Ethiopian air-pollution deaths; East African stroke burden). \textbf{Nankai University}: size-resolved oxidative
potential (fine OP tracking EC and 9,10-phenanthrenequinone) and WRF-GC/E-AIM winter aerosol pH 2.54--4.32 across
six eastern Chinese regions. And one author's \textbf{Kolkata--Howrah} pair on the same 13 regulatory stations: random
10-fold CV R$^2$ 0.84 vs 0.58 under spatial-block or leave-one-station-out validation (inflation 1.45$\times$), and
persistent-homology network geometry with spatial correlation reaching random by about 7\,km (semivariogram range
5.29\,km). Scite counts were not retrieved; for records days old they would be uninformative.

\vspace{1.5mm}
""" + TRIALS + r"""

\vspace{1.5mm}
\textbf{What the harvesting legs did.} \textbf{Crossref-by-ISSN} supplied 34--61 records/day (16--21 November) and most of the
abstract gap; \textbf{Europe PMC} 4--47/day (16--21 November), with 17 of 21 November's records already in the 20 November set and
removed by the cross-day candidate set; \textbf{PubMed E-utilities} health 2--18/day, sensing axis zero on most days;
\textbf{PubMed connector} (EDAT) appended 1--9/day on 17--21 November and twice recovered records entered after their day's harvest.
\textbf{OpenAlex}: HTTP leg 403 all week, connector absent. \textbf{arXiv} no in-window record. \textbf{Consensus},
\textbf{Amass} literature backfill and \textbf{Scite} were not run. The 22 November run lost the device connection
once mid-harvest and resumed from the cached legs.

\vspace{2mm}
% -------------------------------------------------------------- gaps
""" + SEC("Open gaps") + r"""\footnotesize
\begin{itemize}
\item \textbf{Optical sensors in non-ambient aerosol.} Wax fume, organic mill dust and iron-rich subway PM all violate
the ambient calibration that consumer optical sensors carry; of this week's microenvironment campaigns only the New York
schools report a correction. Concentrations of 456--771\,$\mu$g/m$^3$ on an uncorrected sensor are an order-of-magnitude
statement, not an exposure.

\item \textbf{Validation that flatters.} Random cross-validation inflated a 13-station LUR R$^2$ by 1.45$\times$
(Kolkata--Howrah); the India gridded-product evaluation validated against 249 monitors clustered in cities, leaving
rural error uncharacterised; the Malings framework asks evaluators to separate missing from uncertain information.
Network-based exposure surfaces need station-held-out validation as the default.

\item \textbf{Mass is the wrong currency, again.} The 26-laboratory ascorbic-acid OP comparison found significant
between-lab discrepancies (just over half satisfactory); Fudan put non-exhaust PM$_{2.5}$ at 5--11$\times$ the
oxidative and cytotoxic potency of exhaust per unit mass; Chongqing's survival signal sat on organic matter. None of
these is resolvable by an optical mass sensor.

\item \textbf{Abstract gap 28\,\%} (40 of 145); 8 of 11 records on
21 November are metadata only. The two low-cost-sensor records of 20 November (NIST wildland--urban-interface aerosol
test, \textit{AS\&T}; northern Thailand microsensor smoke haze, \textit{AAQR}) are among them and need full text.

\item \textbf{Pipeline defects carried forward}: per-5\,$\mu$g/m$^3$ increments fall to ``not recorded'' in x2;
\texttt{AOR} (upper case) is not in the ratio-metric set and was silently dropped until rewritten as \texttt{aOR};
OpenAlex unavailable on both legs; \texttt{.git} lock debris on the delete-restricted mount.
\end{itemize}

\vspace{1.5mm}
\textbf{Research direction.} Last week the sensing literature characterised its own failure envelope; this week
the measured literature moved into the places people spend their exposure --- classrooms, platforms, workbenches ---
and carried the ambient calibration problem with it. The cohorts meanwhile grew larger and their slopes smaller
(HR 1.05--1.08 per IQR or 5\,$\mu$g/m$^3$, +1.4\,\% per quartile in 29 million Europeans), exactly where exposure
error, not sample size, limits inference. \textbf{Test for W48}: a microenvironment or health study that reports a
reference or gravimetric co-location for its low-cost sensor in the aerosol actually measured, or a cohort estimate
whose exposure surface is validated station-held-out.

\clearpage

"""
s = s[:i] + body + s[j:]
i = s.index(r"Period \textbf{8 -- 14 November 2026}"); j = s.index(r"\end{keybox}", i)
s = s[:i] + r"""Period \textbf{15 -- 21 November 2026}, Sunday to Saturday, \textbf{seven daily issues},
\textbf{145 records}, \textbf{145 unique DOIs}, no record without a DOI. This rollup is
\textbf{aggregation only}: it re-reads \texttt{state/corpus/*.json}, \texttt{state/metrics.csv} and
\texttt{state/trials.json} over the period and \textbf{queries no literature API}; every record was gated by
\texttt{check\_dois.py} at daily-issue time. Tier mix \textbf{12 A, 38 B, 95 C}. The 15--16 November dailies were
built on the 17 November run, 17--18 November on the 20 November 01Z run, 19 November on the 20 November 15Z run,
and 20--21 November and this rollup on the \textbf{22 November run}. Effect estimates are transcribed verbatim from
the daily issues on heterogeneous contrasts and are \textbf{not} meta-analysed; no within-family I$^2$ qualified this
week. Abstracts remain the copyright of their respective publishers.\par}
""" + s[j:]
open("build/weekly.tex", "w").write(s); print("ok", len(s))
