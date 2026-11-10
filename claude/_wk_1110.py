# -*- coding: utf-8 -*-
"""Author build/weekly.tex for W45 (1-7 Nov 2026) from the W44 source (2026-11-10 run)."""
s = open("issues/weekly_2026-10-31.tex").read()
def rep(old, new):
    global s
    assert old in s, old[:70]; s = s.replace(old, new)
rep(r"\newcommand{\DIGESTDATE}{31 October 2026}", r"\newcommand{\DIGESTDATE}{7 November 2026}")
rep(r"\newcommand{\PERIODSTART}{25 October 2026}", r"\newcommand{\PERIODSTART}{1 November 2026}")
rep(r"\newcommand{\PERIODEND}{31 October 2026}", r"\newcommand{\PERIODEND}{7 November 2026}")
rep(r"\mbox{135 records pooled from 7 daily issues}", r"\mbox{151 records pooled from 7 daily issues}")
i = s.index(r"\begin{minipage}[t]{0.190\linewidth}\metric{135}"); j = s.index(r"\vspace{6mm}", i)
s = s[:i] + r"""\begin{minipage}[t]{0.190\linewidth}\metric{151}{RECORDS POOLED\\(151 UNIQUE DOIs)}{Deep}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{40\%}{MEASUREMENT SIDE\\(61 RECORDS)}{Teal}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{11}{LOW-COST SENSOR\\RECORDS (7\%)}{Sky}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{53}{POOLED EFFECT\\ESTIMATES (53 WITH A CI)}{Amber}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{24}{ABSTRACT-FREE\\(16\% OF WEEK)}{Clay}\end{minipage}

""" + s[j:]
i = s.index("% -------------------------------------------------------------- week in one box")
j = s.index("% -------------------------------------------------------------- digest")
SEC = lambda t, r=r"\vspace{2.5mm}": "\\section*{\\sffamily\\bfseries\\color{Deep}%s}\n\\vspace{-1.5mm}{\\color{Teal}\\rule{\\linewidth}{1.1pt}}%s\n\n" % (t, r)
body = "% -------------------------------------------------------------- week in one box\n" + SEC("The week in one paragraph") + r"""\begin{keybox}
{\sffamily\bfseries\small\color{Deep}Volume rose to 151, the measurement side recovered to 40\,\%, and the low-cost
sensor stopped being the object of study and became an input: 33 rural nodes assimilated into WRF-Chem for Delhi's
stubble-burning season, a statewide Bihar network carried to attributable mortality, a metrology-chain network
calibration that worked for temperature and humidity and failed first on PM. Eleven records rest on a low-cost
sensor, against 15 in the whole of October. On the health side, the week's strongest designs were a three-day
controlled human exposure, a life-course constituent analysis in UK Biobank and a deeply phenotyped diabetes cohort
--- and none of their exposures came from a sensor.}\\[1.4mm]
\footnotesize
\textbf{Scale.} \textbf{151 records} over seven issues on daily totals of \textbf{7}, 19, \textbf{28}, 18, 25,
26 and \textbf{28}. Against recent rollups: 151 after 135, 119, 123, 87, 125 and 162. \textbf{All ten subtopics
populated} for the seventh week running.

\textbf{The measurement side rose to 40\,\%} (61 records): \textit{Exposure assessment \& modelling} 34
$\rightarrow$ \textbf{40}, \textit{Sensing} 16 $\rightarrow$ \textbf{21}. Share series 42, 44, 39, 39, 37,
\textbf{40\,\%}.

\textbf{Occupational \& indoor led the health side's growth}: 14 $\rightarrow$ \textbf{20} (coal-miner PMF and CWP,
metro track maintenance, welding, cannabis grow rooms, facility-wide personal monitoring). \textit{Cardiovascular}
recovered 6 $\rightarrow$ 9; \textit{Respiratory} 17 $\rightarrow$ 16, \textit{Neuro} 8 $\rightarrow$ 7,
\textit{Other clinical} 8 $\rightarrow$ 6, \textit{Reproductive} 7 $\rightarrow$ 6.

\textbf{Estimates: 53, every one with an interval} (seventh complete week at 100\,\%), one per 2.8 records, the
densest week of the watch. 48 on ratio scales (OR 13, HR 10, PR 8, RR 7, aOR 6, GMR 4) and 5 on difference scales
(3 mmHg, 2 \% FEV$_1$).

\textbf{Abstract gap 24 of 151 (16\,\%)}, from 17\,\%. \textbf{Tier mix 20 A, 52 B, 79 C} --- tier A at
\textbf{13\,\%}, from 12\,\%.
\end{keybox}

\clearpage

% -------------------------------------------------------------- trend
""" + SEC("Subtopic trend and inflection") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/w1_subtopic_trend.png}
\figcap{Per-issue subtopic counts across the week from \texttt{state/metrics.csv}, seven issues, daily totals 7,
19, 28, 18, 25, 26 and 28. Exposure assessment swings between 3 and 10 per issue; the Sunday (1 November) floor of
7 is the week's minimum. The 1 November daily was built on the 2 November run; 2--5 November on three late runs
between 4 and 6 November; \textbf{6 and 7 November and this rollup on the 10 November recovery run}, after no
scheduled run completed on 7--9 November.}

\footnotesize
\textbf{Expanding.} \textit{Occupational \& indoor} 14 $\rightarrow$ \textbf{20} is the largest gain and carries
the week's largest ratios: in 30,319 US coal miners, progressive massive fibrosis prevalence ran 10 (5.7--17.5)
times higher in Central Appalachia than elsewhere and 3 (2.3--4) times higher in continuous-miner operators. \textit{Sensing}
16 $\rightarrow$ 21 is the other gain, and the composition of that band changed more than its size.

\vspace{1.2mm}
\textbf{Contracting.} Nothing fell by more than two records; \textit{Other clinical} 8 $\rightarrow$ 6 is the
largest fall.

\vspace{1.2mm}
\textbf{The inflection worth naming.} \textbf{Last week the low-cost sensor was an instrument to be corrected;
this week it is a data stream to be used.} The 3 November CUPI-G preprint assimilated 33 rural nodes into WRF-Chem
and cut Haryana mean fractional bias from $-$116.7\,\% to $-$56.8\,\%, recovering the Severe AQI category in about
95\,\% of Delhi cases where the control run called none. The 5 November \textit{Nature Communications} paper
carried a dense Bihar network through ML gap-filling to district attributable mortality (3.2-fold spread). The
4 November SensEURCity/SMEAR III network calibration found PM the hardest quantity to transfer node-to-node, because
PM signals are localised and weakly correlated. Kinshasa (PurpleAir and asthma), Attica (smart benches), a
37-location school vape-detection network and a $\kappa$-K\"ohler humidity correction for the PA-II fill out the
band. \textbf{The weakness is uniform}: none of these abstracts reports the propagated sensor uncertainty in the
downstream quantity --- assimilated fields, attributable deaths or exposure contrasts.

\vspace{1.2mm}
\textbf{Last week's test} (a smoke-specific estimate on measured network data, or a smoke-vs-non-smoke contrast
with composition) \textbf{was not met}. The week's smoke evidence --- All of Us smoke and adult asthma (OR 1.38,
1.32--1.44, at the highest lag), California smoke disparities, wildfire PM$_{0.1}$ in mice, the CMAQ evaluation
showing 1,273 of 2,151 observed $>$35\,$\mu$g/m$^3$ smoke site-days missed --- rests on models and regulatory monitors.

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f2a_architecture.png}
\figcap{Study architecture over the pooled week. \textit{Measurement campaign} 31 and \textit{Metadata only} 24
lead, then \textit{Review / synthesis} 18, \textit{Modelling / inventory} 16, cross-sectional 15, cohort and
experimental 13 each, acute 8, chamber 6, ecological 4. \textbf{Trial / intervention 3}: the EPA three-day
controlled exposure (FEV$_1$ $-$1.9\,\% on day 2, $-$1.8\,\% on day 3), the Beijing clean-heating
difference-in-differences and a paired intervention pilot.}

\clearpage
% -------------------------------------------------------------- pooled analytics
""" + SEC("Pooled analytics", r"\vspace{3mm}") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f1_subtopics.png}
\figcap{Pooled subtopic distribution, all ten bands populated: \textit{Exposure} 40 and \textit{Sensing} 21 put
the measurement side at \textbf{61 of 151 (40\,\%)}. On the health side \textit{Occupational \& indoor} 20 leads,
then \textit{Respiratory} 16, \textit{Mechanistic toxicology} 14 and \textit{Burden} 12; \textit{Cardiovascular} 9,
\textit{Neuro} 7, \textit{Reproductive} and \textit{Other clinical} 6 each. The endpoint chart (f2b) is omitted at
rollup volume; pneumoconiosis prevalence, sinonasal malignancy, hospital-acquired pneumonia and ovarian
hyperandrogenism are new endpoint classes for the watch.}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f3_metric_geography.png}
\figcap{Left --- particle metric: PM$_{2.5}$ alone 60, unspeciated PM or emissions 48, PM$_{2.5}$ and PM$_{10}$
jointly 27; size-resolved, composition, optical and ultrafine metrics together 12. Right --- geography: China and
North America tie at 31, \textit{Global / multi-region} 30, Europe 19, East Asia ex-China 11, South Asia 10,
sub-Saharan Africa 7, Southeast Asia 5.}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f6_lifecourse.png}
\figcap{Life-course windows across the pooled week; counts non-exclusive. Working age leads, carried by the
occupational cluster, the controlled exposure and the diabetes and NIH-AARP cohorts; preconception and in utero are
carried by animal reproductive work, follicular-fluid metals, Korean offspring hernia/hydrocele and the
Generation R epigenetic-age analysis.}

\clearpage

\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{FOREST1}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{FOREST2}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_3.png}
\figcap{FOREST3}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f4_heatmap.png}
\figcap{Subtopic $\times$ architecture, pooled. The densest cell is \textit{Exposure} $\times$ \textit{Measurement
campaign}; occupational work is mostly measurement campaigns and cross-sectional prevalence; mechanistic toxicology
is all experimental or chamber; sensing splits between instrument and calibration work, modelling and metadata-only
deposits.}

\vspace{4mm}

% -------------------------------------------------------------- exposure basis and funnel
\par\vskip 0pt plus 14\baselineskip\penalty-200\vskip 0pt plus -14\baselineskip
""" + SEC("Exposure basis and the effect funnel") + r"""\footnotesize
\textbf{Exposure basis (x1).} 11 of 151 records rest on a low-cost sensor or network (7\,\%), against 15 of 523 in
October (3\,\%); 3 on a personal or wearable monitor. On the health side, where a basis is recoverable (n=60),
\textbf{58\,\% measured, 30\,\% modelled or satellite-fused, 12\,\% proxy}, against the October baseline of 36/42/22.
The shift is real but narrow: ``measured'' here is mostly regulatory monitors assigned at city scale and occupational
filter campaigns. \emph{Not one of the 53 effect estimates rests on a low-cost sensor exposure}; the only sensor-based
health record (Kinshasa PurpleAir and asthma) reports no estimate with an interval in the pooled set.

\vspace{1.5mm}
\textbf{Increments and precision (x2).} Of the 48 ratio estimates, 21 are per IQR or SD, 10 categorical
contrasts, 6 per 1\,$\mu$g/m$^3$, 5 per 10\,$\mu$g/m$^3$ and \textbf{6 carry no recorded increment} --- 12\,\%,
against 49 of 97 (51\,\%) in October, the clearest improvement in the record set. 42 of 48 exclude the null. The
funnel is \textbf{not} a pooled estimate: increments differ and many estimates share a sample. The Egger intercept,
4.38 (SE 0.66), is close to October's 4.6 --- the small-study asymmetry is a property of what gets published and
indexed, not of one week.

\vspace{1.5mm}
\textbf{Within-family heterogeneity.} No two independent sources this week share metric, endpoint family and
increment: the two influenza series (Shanxi RR per 10\,$\mu$g/m$^3$ PM$_{2.5}$; Shanghai OR per 10\,$\mu$g/m$^3$
PM$_{10}$) differ in pollutant and design, and the asthma estimates (All of Us smoke case-crossover; Lima PM$_{2.5}$
5$\rightarrow$15) differ in contrast. \textbf{No I$^2$ is reported.}

\vspace{4mm}

% -------------------------------------------------------------- venues + trials
\par\vskip 0pt plus 14\baselineskip\penalty-200\vskip 0pt plus -14\baselineskip
""" + SEC("Venues, groups, trial watch, and what the pipeline did") + r"""\footnotesize
\textbf{Venues.} \textit{Environ Res} and Research Square lead at \textbf{7} each, then \textit{Atmos Environ} 6,
\textit{Environ Sci Technol} and \textit{Environ Health Perspect} 5, and \textit{Atmosphere}, \textit{Atmos Pollut
Res}, \textit{J Hazard Mater}, \textit{Environ Pollut} and \textit{Front Public Health} 4. Research Square supplied
the CUPI-G assimilation, the California metals analysis and the CMAQ smoke evaluation --- the sensing-relevant
preprint stream is coming through Europe PMC, not arXiv.

\vspace{1.5mm}
\textbf{Recurring groups.} From the \texttt{affil} field (first- and last-author institutions, counted per mention):
Sun Yat-sen University 6, Peking University 5 (plus 3 for its Shenzhen graduate school), and Environment and Climate
Change Canada, Johns Hopkins, Colorado State and USC 4 each; IIT Bombay, Yonsei, AGH Krakow and CU Boulder 3. The
Peking/Sun Yat-sen counts are spread over unrelated health records; the only coherent cluster is \textbf{ECCC}:
the SWAPIT Toronto AQHI-representativeness campaign and a calibrated ventilation index for Lagrangian dispersion, both
measurement-side and both from the federal air-quality research group. Scite citation counts were
not retrieved (paid-plan refusal); for records days old they would be uninformative.

\vspace{1.5mm}
\textbf{Trial watch.} ClinicalTrials.gov \texttt{LastUpdatePostDate} windows 1--10 November: \textbf{3 new}
registrations. \textbf{NCT07914010} REACT (UC Berkeley; air cleaners plus a PurpleAir indoor monitor with a visual
indicator, asthma and COPD, n=100) on 4 November --- the first registered trial in the set whose primary outcome is a
\emph{low-cost-sensor-measured} indoor PM$_{2.5}$ change. On 10 November: \textbf{NCT07925229} PINE (UBC;
lodgepole-pine woodsmoke versus filtered air crossed with ibuprofen, phase 4, n=20) and \textbf{NCT07924839}
(Michigan State; sham-filtration PM$_{2.5}$ $\times$ obesity $\times$ dietary antioxidant, n=20). Amass TrialCore
(WHO ICTRP) carried ACTRN12626001238369 (HEPA RCT) and ChiCTR2600134305 (pollutant exposure and reproductive
outcomes) from 4 November and nothing PM-related on 10 November. \texttt{trials.json} holds \textbf{26 trials}
over 43 query windows. UBC now has two controlled woodsmoke chamber registrations (\emph{Lungs on Fire} last week,
PINE this week): the smoke question is being moved into the chamber, where composition is known.

\vspace{1.5mm}
\textbf{What the harvesting legs did.} \textbf{Europe PMC} re-surfaced records across days again: the 6--9 November
backfill caught 33 cross-day duplicates before authoring, and returned zero records on 5 and 9 November (indexing
lag). \textbf{Crossref-by-ISSN} 28--67/day (3 on Sunday 8 November). \textbf{PubMed connector} appended 2--18
records/day. \textbf{OpenAlex}: the connector's date filter worked once (3 November, 2 records admitted) and the
connector was absent on every later session; the harvester's HTTP leg returned 429 throughout. \textbf{arXiv} no
in-window entry. \textbf{Consensus} 10 hits/run, 1 new record (ARMIE). \textbf{Scite} refused (paid plan).

\vspace{2mm}
% -------------------------------------------------------------- gaps
""" + SEC("Open gaps") + r"""\footnotesize
\begin{itemize}
\item \textbf{Sensor-derived quantities ship without propagated uncertainty.} Assimilated WRF-Chem fields, Bihar
attributable deaths and the Jhansi compliance assessment all inherit sensor error that their abstracts do not
quantify. The field now needs uncertainty propagation more than it needs another co-location.

\item \textbf{Node-to-node PM calibration transfer is the weak link.} The SensEURCity result is the first in the
watch to say directly that PM transfers worse than meteorology; any network that calibrates by chaining nodes to a
single reference should expect it.

\item \textbf{Smoke exposure is still modelled.} CMAQ missed most observed smoke-exceedance site-days; every smoke
health estimate this week used a model or a monitor. The two UBC chamber registrations will supply composition-known
dose--response, not population exposure.

\item \textbf{Indoor endpoints on outdoor monitors.} ICU hospital-acquired pneumonia in filtered post-surgical air was
fitted to city-wide ambient PM$_{2.5}$; an indoor sensor is the obvious test of the pathway.

\item \textbf{The abstract gap is 16\,\%}, concentrated in day-0 Elsevier and ACS deposits.

\item \textbf{Pipeline defects carried forward}: scheduled runs for 7--9 November did not complete (recovered
10 November); Europe PMC re-surfacing makes per-day dedup order-dependent; the OpenAlex connector is present only
intermittently; \texttt{.git} lock debris on the delete-restricted mount.
\end{itemize}

\vspace{1.5mm}
\textbf{Research direction.} The sensing literature is moving from \emph{is the sensor right} to \emph{what does the
sensor change downstream} --- forecasts, burden estimates, inequity maps. The epidemiology has not followed: its
best designs this week (controlled exposure, deep phenotyping, life-course constituents) still use monitors or
models. The next step that matters is a health estimate whose exposure comes from a calibrated network with its
uncertainty carried through.

\clearpage

"""
s = s[:i] + body + s[j:]
i = s.index(r"Period \textbf{25 -- 31 October 2026}"); j = s.index(r"\end{keybox}", i)
s = s[:i] + r"""Period \textbf{1 -- 7 November 2026}, Sunday to Saturday, \textbf{seven daily issues},
\textbf{151 records}, \textbf{151 unique DOIs}, no record without a DOI. This rollup is
\textbf{aggregation only}: it re-reads \texttt{state/corpus/*.json}, \texttt{state/metrics.csv} and
\texttt{state/trials.json} over the period and \textbf{queries no literature API}; every record was gated by
\texttt{check\_dois.py} at daily-issue time. Tier mix \textbf{20 A, 52 B, 79 C}. The 1--5 November dailies were
built on runs of 2--6 November; the 6 and 7 November dailies and this rollup on the \textbf{10 November recovery
run}. Effect estimates are transcribed verbatim from the daily issues on heterogeneous contrasts and are
\textbf{not} meta-analysed. Abstracts remain the copyright of their respective publishers.\par}
""" + s[j:]
F1 = r"""Ratio scale, part 1: the 32 estimates up to 1.38, from 0.42 (Kim coal-miner seroconversion, high vs low self-reported dust) to 1.38 (All of Us wildfire-smoke asthma exacerbation, highest lag). Nested sets share samples and are not independent: Yang sinonasal (3 averaging windows), Yang UK Biobank (4 endpoints), Singh diabetes (5 across both panels), China kidney deaths (2 pollutants), Tsogtbayar Ulaanbaatar (3 lags). Increments differ across sources; no pooling."""
F2 = r"""Ratio scale, part 2: the 16 estimates from 1.39 to 10. Myers' US coal-miner prevalence ratios supply 6 (PMF 10.0, 5.7--17.5, Central Appalachia vs rest of US; job-category contrasts for continuous-miner operators and roof bolters), Shi CFPS 3 (PM$_{2.5}$ with dry-hot extremes and CVD), Singh diabetes 3, NIH-AARP endometrial and ovarian cancer 2 (per 5\,$\mu$g/m$^3$), Italian welders 1 and the TRAP allergic-rhinitis meta-analysis 1. Regional and occupational contrasts, not per-unit PM effects."""
F3 = r"""Difference scale, 5 estimates: Pulczinski EPA controlled exposure (35\,$\mu$g/m$^3$ PM$_{2.5}$ vs clean air, n=17), FEV$_1$ $-$1.9\,\% (day 2) and $-$1.8\,\% (day 3); Sternbach Beijing clean-heating policy, brachial SBP $-$1.4 and DBP $-$1.6\,mmHg; Accra children, SBP $-$0.7\,mmHg per 10 units home PM$_{2.5}$ with an interval spanning zero."""
s = s.replace(r"\figcap{FOREST1}", r"\figcap{" + F1 + "}").replace(r"\figcap{FOREST2}", r"\figcap{" + F2 + "}").replace(r"\figcap{FOREST3}", r"\figcap{" + F3 + "}")
open("build/weekly.tex", "w").write(s); print("ok", len(s))
