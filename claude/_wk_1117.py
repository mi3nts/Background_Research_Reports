# -*- coding: utf-8 -*-
"""Author build/weekly.tex for W46 (8-14 Nov 2026) from the W45 source (2026-11-17 run)."""
import sys
s = open("issues/weekly_2026-11-07.tex").read()
def rep(old, new):
    global s
    assert old in s, old[:70]; s = s.replace(old, new)
rep(r"\newcommand{\DIGESTDATE}{7 November 2026}", r"\newcommand{\DIGESTDATE}{14 November 2026}")
rep(r"\newcommand{\PERIODSTART}{1 November 2026}", r"\newcommand{\PERIODSTART}{8 November 2026}")
rep(r"\newcommand{\PERIODEND}{7 November 2026}", r"\newcommand{\PERIODEND}{14 November 2026}")
rep(r"\mbox{151 records pooled from 7 daily issues}", r"\mbox{157 records pooled from 7 daily issues}")
i = s.index(r"\begin{minipage}[t]{0.190\linewidth}\metric{151}"); j = s.index(r"\vspace{6mm}", i)
s = s[:i] + r"""\begin{minipage}[t]{0.190\linewidth}\metric{157}{RECORDS POOLED\\(157 UNIQUE DOIs)}{Deep}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{39\%}{MEASUREMENT SIDE\\(62 RECORDS)}{Teal}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{12}{LOW-COST SENSOR\\RECORDS (8\%)}{Sky}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{35}{POOLED EFFECT\\ESTIMATES (35 WITH A CI)}{Amber}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{25}{ABSTRACT-FREE\\(16\% OF WEEK)}{Clay}\end{minipage}

""" + s[j:]
i = s.index("% -------------------------------------------------------------- week in one box")
j = s.index("% -------------------------------------------------------------- digest")
SEC = lambda t, r=r"\vspace{2.5mm}": "\\section*{\\sffamily\\bfseries\\color{Deep}%s}\n\\vspace{-1.5mm}{\\color{Teal}\\rule{\\linewidth}{1.1pt}}%s\n\n" % (t, r)
BRK = "\\par\\vskip 0pt plus 14\\baselineskip\\penalty-200\\vskip 0pt plus -14\\baselineskip\n"
CAP = dict(F2A="F2A", F1="F1", F3="F3", F6="F6", F4="F4", FO1="FO1", FO2="FO2", FO3="FO3")
try:
    exec(open("_wk_1117_caps.py").read(), {"CAP": CAP})
except FileNotFoundError:
    pass
body = "% -------------------------------------------------------------- week in one box\n" + SEC("The week in one paragraph") + r"""\begin{keybox}
{\sffamily\bfseries\small\color{Deep}Volume held at 157 and the measurement side at 39\,\%, but the sensing band
changed its question: last week the low-cost sensor was a data stream to be used; this week the strongest sensing
papers measured \emph{where it breaks} --- biomass smoke above 1000\,$\mu$g/m$^3$, sub-8\,$^\circ$C winters, mineral-dust
PM$_{10}$, calibration transfer between units, and wildfire swings that look like faults. Eight of the 22 sensing
records are tier A, the most in one week. The health side was dominated by smoke, all of it modelled: wildfire
PM$_{2.5}$ and mortality pooled at RR 1.066 per 10\,$\mu$g/m$^3$, and a plume-plus-heat contrast in dialysis
patients at RR 1.92. Increment reporting slipped back: 12 of 30 ratio estimates carry none.}\\[1.4mm]
\footnotesize
\textbf{Scale.} \textbf{157 records} over seven issues on daily totals of \textbf{5}, 17, 26, \textbf{36}, 30,
16 and 27. Against recent rollups: 157 after 151, 135, 119, 123, 87 and 125. \textbf{All ten subtopics populated}
for the eighth week running.

\textbf{The measurement side held at 39\,\%} (62 records): \textit{Exposure assessment \& modelling} 40
$\rightarrow$ \textbf{40}, \textit{Sensing} 21 $\rightarrow$ \textbf{22}. Share series 44, 39, 39, 37, 40,
\textbf{39\,\%}.

\textbf{Burden and cardiovascular grew; occupational and respiratory fell back.} \textit{Burden, policy \&
mitigation} 12 $\rightarrow$ \textbf{18}, \textit{Cardiovascular} 9 $\rightarrow$ \textbf{12}, \textit{Mechanistic}
14 $\rightarrow$ 16, \textit{Other clinical} 6 $\rightarrow$ 8, \textit{Reproductive} 6 $\rightarrow$ 7,
\textit{Neuro} 7 $\rightarrow$ 7; \textit{Occupational \& indoor} 20 $\rightarrow$ \textbf{15} and
\textit{Respiratory} 16 $\rightarrow$ \textbf{12}.

\textbf{Estimates: 35, every one with an interval} (eighth complete week at 100\,\%), one per 4.5 records against
one per 2.8 last week. 30 on ratio scales (RR 12, HR 11, OR 6, IRR 1) and 5 on difference scales (2 \% change,
2 telomere T/S, 1 z-score).

\textbf{Abstract gap 25 of 157 (16\,\%)}, unchanged. \textbf{Tier mix 18 A, 55 B, 84 C} --- tier A at
\textbf{11\,\%}, from 13\,\%.
\end{keybox}

\clearpage

% -------------------------------------------------------------- trend
""" + SEC("Subtopic trend and inflection") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/w1_subtopic_trend.png}
\figcap{Per-issue subtopic counts across the week from \texttt{state/metrics.csv}, seven issues, daily totals 5,
17, 26, 36, 30, 16 and 27. The Sunday (8 November) floor of 5 is the week's minimum and Wednesday 11 November's 36
its maximum. 8 and 9 November were built on the 10 November recovery run, 10 and 11 November on the 12 November
run, and \textbf{12--14 November and this rollup on the 17 November run}, which completed an interrupted
16 November run that had authored 12--15 November but shipped nothing.}

\footnotesize
\textbf{Expanding.} \textit{Burden, policy \& mitigation} 12 $\rightarrow$ \textbf{18} is the largest gain:
GBD secondary analyses, refinery-closure and health-impact models, and the CONUS wildfire-attribution preprint
(wildfire smoke 20\,\% of PM$_{2.5}$-attributable deaths on the west coast in 2020, 30 times 2019).
\textit{Cardiovascular} 9 $\rightarrow$ 12 carries the CHARLS stroke cohort (high vs low PM$_{2.5}$ HR 1.25,
1.04--1.51; solid fuel 1.38, 1.18--1.62).

\vspace{1.2mm}
\textbf{Contracting.} \textit{Occupational \& indoor} 20 $\rightarrow$ 15 after last week's coal-miner cluster;
\textit{Respiratory} 16 $\rightarrow$ 12.

\vspace{1.2mm}
\textbf{The inflection worth naming.} \textbf{The sensing band moved from deployment to failure modes.} Arba Minch
(\textit{AMT}): SPS30 and SEN55 stayed stable through repeated biomass-smoke events above 1000\,$\mu$g/m$^3$, with
in-use accuracy error $\le$22\,\% and outdoor expanded uncertainty $\le$15\,\% against gravimetry. Prague (CHMI,
19 months): Sensirion PM$_{2.5}$ R$^2$ 0.87 raw, PM$_{10}$ only 0.50, and dust episodes invisible after correction.
TU Delft: calibration learned on one unit lost its advantage over the \emph{uncalibrated} sensor for PM$_{10}$ when
transferred. Strong Heart Air Study: offline PurpleAir logging recovered 100\,\% of data in Arizona but 10\,\% in
South Dakota, failing at 4--8\,$^\circ$C. University of Washington: an entropy-based outlier detector for smoke
events, when true swings mimic faults. And at the regulatory end, 43,576 reference-equivalent pairs at 45 US sites
showed that 1-in-6 sampling leaves 63.8\,\% (53.0--73.8) of comparability verdicts indeterminate. \textbf{The
weakness is shared}: most of these test failure on a handful of devices or simulated faults, and none carries the
failure through to a health estimate.

\vspace{1.2mm}
\textbf{Last week's test} (a health estimate on calibrated network exposure with uncertainty carried through)
\textbf{was not met}. The nearest record is the Haramaya HDSS kitchen survey --- 923 kitchens on PurpleAir II-SD,
rural 473 vs urban 80\,$\mu$g/m$^3$ (difference 393, 370--416) --- which reports no correction or co-location and
no health outcome.

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
\textbf{Exposure basis (x1).} 12 of 157 records rest on a low-cost sensor or network (8\,\%), against 11 (7\,\%)
last week and 15 of 523 (3\,\%) in October; 4 on a personal or wearable monitor. On the health side, where a basis
is recoverable (n=60), \textbf{52\,\% measured, 43\,\% modelled or satellite-fused, 5\,\% proxy}, against 58/30/12
last week and the October baseline of 36/42/22. The modelled share rose because the week's health evidence was
dominated by wildfire smoke, which is always a model split of total PM$_{2.5}$. \emph{Not one of the 35 effect
estimates rests on a low-cost sensor exposure}; the only measured-exposure estimates are the rural Beijing panel
(TNF-$\alpha$ +1.9\,\%, 0.2--3.6, per 10\,$\mu$g/m$^3$ outdoor village monitor) and the HAPIN Peru randomised
contrast.

\vspace{1.5mm}
\textbf{Increments and precision (x2).} Of the 30 ratio estimates, 10 are per 10\,$\mu$g/m$^3$, 7 categorical
contrasts, 1 per IQR and \textbf{12 carry no recorded increment} --- 40\,\%, against 12\,\% last week and 51\,\% in
October: last week's improvement did not hold. The 12 come from five sources (UK Biobank substance use, the
Brigham MS cohort, the glaucoma surgery cohort, Beijing endometriosis and the Bangkok coarse-PM series) whose
abstracts give no unit. The funnel is \textbf{not} a pooled estimate: increments differ and many estimates share a
sample.

\vspace{1.5mm}
\textbf{Within-family heterogeneity.} One family qualifies: wildfire PM$_{2.5}$ and all-cause or dialysis mortality,
RR per 10\,$\mu$g/m$^3$ --- the Yadate meta-analysis, 1.066 (1.014--1.121), and the Fresenius western-US dialysis
cohort, 1.03 (1.02--1.06). Fixed-effect combination 1.035, Q = 1.57 on 1 df, \textbf{I$^2$ = 36\,\%}. Two
estimates, one of them already a pooled estimate and the other in a susceptible population, so this is a
consistency check, not a summary. Every other source this week stands alone on its metric, endpoint and increment.

\vspace{4mm}

% -------------------------------------------------------------- venues + trials
""" + BRK + SEC("Venues, groups, trial watch, and what the pipeline did") + r"""\footnotesize
\textbf{Venues.} \textit{Atmospheric Pollution Research} leads at \textbf{10} (indexed under two names), then
Research Square \textbf{10}, \textit{Environ Pollut} 7, \textit{Sensors} 6, \textit{Environ Sci Technol} 5, and
\textit{AMT} and \textit{J Environ Sci (China)} 4 each. \textit{AMT} carried three of the week's tier-A sensing papers
(Arba Minch, the UW outlier detector, the Ghana 1-km product); Research Square again supplied sensing-relevant
preprints (AirQo LOCATE, Haramaya kitchens, the Aurora evaluation).

\vspace{1.5mm}
\textbf{Recurring groups.} From the \texttt{affil} field (first- and last-author institutions, per mention): Sun
Yat-sen University 8, then Peking University, the University of Washington and Chiang Mai University 4 each, and the
Chinese Research Academy of Environmental Sciences 3. \textbf{Two clusters are coherent.} Sun Yat-sen produced two
PM$_{2.5}$-constituent mixture analyses with quantile g-computation (Pearl River cohort respiratory mortality, HR
1.29, 1.23--1.34, per quantile of the mixture; a national arthritis cohort) --- the same method on different
endpoints. The University of Washington produced the sensor-network outlier detector and the CONUS 1-km wildfire
PM$_{2.5}$ preprint: smoke measurement and smoke modelling from one institution. Chiang Mai's four mentions are two
unrelated records (rural telomeres, a veterinary review). Scite citation counts were not retrieved; for records days
old they would be uninformative.

\vspace{1.5mm}
\textbf{Trial watch.} ClinicalTrials.gov \texttt{LastUpdatePostDate} 11--17 November and Amass TrialCore
(\texttt{minCreateDate} 10 November): \textbf{4 added} to the register. \textbf{NCT07931820} (Boston University;
not yet recruiting, n=120 households, start February 2027) randomises households given an indoor air monitor to
monitor-only, generic reminders or personalised insights --- after REACT (NCT07914010), the second registered trial
in the set whose intervention is \emph{information from a low-cost monitor}. Three updated registrations were not
previously carried: \textbf{NCT07119333} (Norwegian Institute of Public Health, cluster-randomised classroom
purifiers vs sham, school absence, 72 classes), \textbf{NCT05230784} (NYU, purifier vs placebo filter in heart
failure, n=600) and \textbf{NCT07238608} (UPRISE, observational, ultrafine PM and micro/nanoplastics in 1,600
pregnancies). \texttt{trials.json} holds \textbf{30 trials} over 45 query windows; the 12--16 November window was
logged once by this run, the interrupted 16 November run having logged none.

\vspace{1.5mm}
\textbf{What the harvesting legs did.} \textbf{Crossref-by-ISSN} supplied 3--71 records/day (Sunday 8 November
the floor); \textbf{Europe PMC} returned zero on 9 November (indexing lag) and continued to re-surface records on
consecutive days, caught by cross-day candidate sets on 10--11 and 12--15 November before authoring.
\textbf{PubMed connector} appended 2--18/day. \textbf{OpenAlex}: the harvester's HTTP leg returned 429 all week and
403 by 16 November; the connector was absent on every session. \textbf{arXiv} one in-window record (10 November).
\textbf{Consensus}, \textbf{Amass} literature backfill and \textbf{Scite} were not run.

\vspace{2mm}
% -------------------------------------------------------------- gaps
""" + SEC("Open gaps") + r"""\footnotesize
\begin{itemize}
\item \textbf{Sensor missingness is not at random.} Cold-weather logging failure (Strong Heart) and dust-blind
PM$_{10}$ (Prague) both drop the dirtiest periods. An exposure series built on these sensors without a missingness
model is biased toward the clean season.

\item \textbf{PM$_{10}$ does not transfer.} Two independent groups (TU Delft, CHMI) found PM$_{10}$ the quantity that
calibration cannot rescue on optical sensors; any network reporting PM$_{10}$ from Plantower or Sensirion units should
say so.

\item \textbf{Uncorrected sensors at extreme concentrations.} The largest household survey of the week (Haramaya,
923 kitchens) reports no correction, while the Arba Minch evaluation shows correction is feasible at the same
concentrations. The wet-season doubling it reports lies on exactly the humidity axis that biases uncorrected
Plantower readings.

\item \textbf{Smoke health evidence is entirely modelled.} The meta-analysis, the dialysis cohort and the CONUS
attribution all split wildfire from total PM$_{2.5}$ by model; the UW group now has both the detector and the model
needed to test that split against a network.

\item \textbf{Increment reporting regressed to 40\,\% missing} among ratio estimates.

\item \textbf{Pipeline defects carried forward}: the 16 November run authored 12--15 November but stopped when
\texttt{plots.py} hard-failed on unmapped design labels, and shipped nothing for 23 h; overlapping or interrupted
runs still have no run-level lock; OpenAlex unavailable on both legs; \texttt{.git} lock debris on the
delete-restricted mount.
\end{itemize}

\vspace{1.5mm}
\textbf{Research direction.} The sensing literature is now characterising its own failure envelope ---
concentration, temperature, size fraction, unit-to-unit transfer --- which is the precondition for using networks in
epidemiology. The health literature has not met it: its most consequential estimates this week concern wildfire
smoke, the exposure most in need of dense measurement, and every one of them is modelled. \textbf{Test for W47}: a
health or exposure-contrast estimate that either uses a corrected low-cost network as its exposure, or validates a
wildfire PM$_{2.5}$ split against one.

\clearpage

"""
s = s[:i] + body + s[j:]
i = s.index(r"Period \textbf{1 -- 7 November 2026}"); j = s.index(r"\end{keybox}", i)
s = s[:i] + r"""Period \textbf{8 -- 14 November 2026}, Sunday to Saturday, \textbf{seven daily issues},
\textbf{157 records}, \textbf{157 unique DOIs}, no record without a DOI. This rollup is
\textbf{aggregation only}: it re-reads \texttt{state/corpus/*.json}, \texttt{state/metrics.csv} and
\texttt{state/trials.json} over the period and \textbf{queries no literature API}; every record was gated by
\texttt{check\_dois.py} at daily-issue time. Tier mix \textbf{18 A, 55 B, 84 C}. The 8--9 November dailies were
built on the 10 November run, 10--11 November on the 12 November run, and 12--14 November and this rollup on the
\textbf{17 November run}. Effect estimates are transcribed verbatim from the daily issues on heterogeneous contrasts
and are \textbf{not} meta-analysed; the single within-family I$^2$ above is a consistency check. Abstracts remain
the copyright of their respective publishers.\par}
""" + s[j:]
open("build/weekly.tex", "w").write(s); print("ok", len(s))
