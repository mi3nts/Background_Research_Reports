# -*- coding: utf-8 -*-
HEAD = dict(long="29 October 2026", window="29 October 2026 (full day)", n=22, excl=85,
            bands=9, eff=3, tierA=3, meta=7)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Accra, 146 gravimetric sites: in a decade, household biomass burning
lost $\sim$16\,\% of its share of PM$_{2.5}$ elemental mass and solid/e-waste burning gained 23 points.}\\[1.4mm]
\footnotesize
A citywide campaign (April 2019--June 2020, $>$600 weekly filters, ED-XRF, PMF) against four legacy sites sampled in
2007--2008. Harmattan dust was 52--68\,\% of elemental mass. Outside Harmattan: biomass burning 11--32\,\%, traffic and
road dust 9--36\,\%, solid and e-waste combustion 0--35\,\%. Biomass share $-$16\,\% (5.2--25.8); waste burning
$+$23 points (15.9--30.0).
\textbf{Where it is weak:} ED-XRF misses the carbonaceous fraction, so these are shares of \emph{elemental} mass, not of
PM$_{2.5}$; the decadal contrast rests on four sites.
\textbf{Why it matters here:} a 146-site gravimetric network is the speciation reference a West African low-cost
network needs, and open waste burning is a source an optical mass sensor cannot tell apart from wood smoke."""

CHANGED = [
r"""\textbf{Ultrafine particles and the kidney.} New York State, 269,945 ED visits: excess risk 0.74\,\% (0.28--1.20)
per IQR of CTM-modelled UFP at lag 0--3. The exposure is modelled, and co-pollutant control is not reported.""",
r"""\textbf{Surface vs 230\,m.} Czech rural tower, ToF-ACSM at 4\,m and ToF-AMS at 230\,m: every submicron component
higher at the surface (ratio 0.55--0.82); 2--3$\times$ under inversions with mixing height $<$230\,m.""",
r"""\textbf{Children's respirators.} Chiang Mai, 82 children: a KN95-equivalent passed fit testing in 3.7\,\%
(median fit factor 9.5); adding positive-pressure HEPA air raised the pass rate to 23.2\,\%.""",
r"""\textbf{Biomass fuel tops the stillbirth PAF.} ICMR-SPIC, 227,821 pregnancies: household biomass aIRR 1.37
(1.21--1.57), PAF 13.95\,\% --- the largest of any factor, and an upper bound given its tie to rural poverty.""",
r"""\textbf{Seven metadata-only records (32\,\%)}, including the most sensing-relevant title of the day: multicopter
vibration and OPC accuracy (\emph{Aerosol Sci.\ Technol.}). Retry first.""",
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. The scheduled runs for 23--29 October
did not complete (one 30 October 00:21 UTC firing harvested 23--28 October and stopped before screening). This issue
was built on the \textbf{30 October 14:20 UTC (09:20 CDT) recovery run}, which backfills 23--29 October day by day,
each with its own window; this issue covers \textbf{29 October in full}. By the 22:00 rule 30 October is \emph{not}
opened. The W44 weekly (25--31 October) and the October monthly are due on the Saturday 31 October run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 22 in-scope records across nine bands; cardiovascular \& metabolic is
empty. Exposure assessment leads with six (Accra PMF, vertical speciation, WRF-Chem NH$_3$ uptake, trend change-points,
Warsaw, nucleation mode); burden/mitigation four; sensing three (all metadata-only).""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{metadata-only 7 (32\,\%)}, three cross-sectional, three
measurement campaigns, two cohorts, two modelling, and one each acute (case-crossover), ecological, toxicology,
laboratory (respirator fit) and review. Right --- endpoints run from kidney ED visits to stillbirth, behaviour, COPD,
TB and respirator fit.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated/emissions 10 (biomass-fuel proxies, metadata-only
records), PM$_{2.5}$-only 6, size-resolved/number 2, and one each joint PM$_{2.5}$+PM$_{10}$, UFP, bioaerosol, optical.
Right --- geography: global/not stated 8, China 3, Europe 3; two each North America, Southeast Asia (Thailand) and the
Middle East (Iran, T\"urkiye); one each Sub-Saharan Africa (Ghana) and South Asia.""",
"f6_lifecourse": r"""Life-course windows: two in-utero records (stillbirth, CHAPS prenatal window), three childhood, one
reaching adolescence (CHAPS), two working-age (COPD, coal dust) and one older-adult signal (UFP kidney effect stronger
above 65).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Sensing is entirely metadata-only today; the exposure band spans
measurement, modelling and metadata cells; the health bands sit in cohort, cross-sectional, case-crossover and
ecological cells.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, two estimates from two studies: combined biomass + cigarette vs cigarette-only COPD and severe
exacerbation (OR, T\"urkiye, $n$\,=\,319); household biomass fuel and stillbirth (IRR, ICMR-SPIC). Neither is a measured
particle exposure. Not poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: \% excess risk of kidney-disease ED visits per IQR of CTM-modelled UFP, cumulative lag 0--3
(New York State, 269,945 visits).}\end{minipage}"""

PROV = r"""Entry window \textbf{29 October 2026}, single day (Thursday). Harvester legs: \textbf{PubMed} health
\textbf{13}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{19}; \textbf{Crossref by ISSN} \textbf{66}; \textbf{arXiv}
150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. 97 unique, 0 already carried, 97 fresh; PubMed connector
(EDAT 29 Oct) 21 PMIDs (20 bucketed to 29 Oct), 1 merged, 10 appended, \textbf{107 screened}. Abstracts for 24
PubMed records recovered by efetch; Crossref/Semantic Scholar recovered the Accra (EHP) abstract and a one-line
fragment for one more. \textbf{Consensus} calibration sweep (once for the 23--29 October backfill): 10 hits, 0 new (Ginsburg 2026, Kumpika 2026 and Fang 2026 already archived). \textbf{22 admitted}, \textbf{85 rejected} with logged reasons (6 of them already shipped in the 28 October issue). \textbf{DOI
gate} 0 fail / 0 warn. \textbf{Trial watch} 23--30 October: 4 registrations updated, \textbf{1 new} --- NCT07536178 (UBC \emph{Lungs on Fire}, $n$\,=\,24 controlled woodsmoke vs filtered-air exposure; co-primary FeNO and CANTAB cognition, with rs-fMRI, $^{129}$Xe MRI and neuroinflammation panels); \texttt{trials.json} 20 NCT / 36 windows. \textbf{7 carried on metadata alone}. \textbf{Scholar Gateway} not called.
Abstracts remain the copyright of their publishers."""
