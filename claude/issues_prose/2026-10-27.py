# -*- coding: utf-8 -*-
HEAD = dict(long="27 October 2026", window="27 October 2026 (full day)", n=30, excl=169,
            bands=9, eff=5, tierA=4, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}PurpleAir dries its own sample: internal heating in the housing lowers
detection-zone RH and removes aerosol water before the PMS5003 counts it.}\\[1.4mm]
\footnotesize
Laboratory and field work (Santa Rosa, CA; Winston-Salem, NC, against a Teledyne T640x) measured air temperature in the
particle detection zone of the Plantower PMS5003, standalone and inside a PurpleAir. The housing warms the zone more than
a bare sensor; a wraparound USB heater pushed sample RH down to regulatory-monitor conditions and lowered reported
PM$_{2.5}$ at high ambient RH. Even unheated, the PurpleAir read below a standalone PMS5003, consistent with partial
removal of hygroscopic water. CFD resolved airflow, residence time and temperature inside the unit.
\textbf{Where it is weak:} two field sites, no fitted growth factor or quantified bias reduction in the abstract;
preprint.
\textbf{Why it matters here:} humidity corrections are fitted on ambient RH, but the optical engine sees a warmed, drier
sample whose RH depends on housing and airflow. Corrections fitted on bare-PMS data need not transfer to housed units."""

CHANGED = [
r"""\textbf{Trajectory source maps fail a negative control.} Riyadh, 10 years of METAR dust codes: PSCF/CWT run on
\emph{locally lifted} dust (no distant source needed) was \emph{more} enriched over candidate source regions than
suspended dust (permutation $p\le0.007$); wind matching erased most structure in both.""",
r"""\textbf{Paris plume optics change within hours.} Airborne plus ground: refractive index moved from
$\sim$1.35--1.40\,+\,0.03--0.08$i$ near source to $\sim$1.45--1.50\,+\,0.015--0.02$i$ 2--6\,h downwind; SSA and AAE
rose. A single assumed refractive index in OPC mass conversion is wrong for one of the two.""",
r"""\textbf{Prenatal PM$_{2.5}$ and infant antibiotics, Scotland.} 498,123 births; observed vs 5\,$\mu$g\,m$^{-3}$
counterfactual: controlled direct effect OR 1.12 (1.10--1.14), indirect via birthweight 0.99. The exposure IQR is only
6--8\,$\mu$g\,m$^{-3}$; read as residual area confounding until replicated.""",
r"""\textbf{Coal heating drives Polish respiratory admissions.} 779k emergency COPD/asthma admissions: associations
only in the heating season (adult asthma RR 1.100 per IQR PM$_{2.5}$); NO$_2$ null throughout.""",
r"""\textbf{ERF choice dominates burden.} BEST-COST, five countries: disease-specific ERFs gave 2--4$\times$ lower
YLL than WHO all-cause ERFs (median ratio 0.42 for PM$_{2.5}$), with stable rankings.""",
r"""\textbf{Power shutoffs compound wildfire smoke.} California 2013--2019: severe PSPS plus +10\,$\mu$g\,m$^{-3}$
wildfire PM$_{2.5}$ vs neither, respiratory encounters OR 1.16 (1.10--1.22), multiplicative interaction --- the window
in which mains-powered sensors and purifiers go dark.""",
r"""\textbf{Low-cost PM$_{2.5}$ calibration holds through winter; gases do not.} London, 10 months, two sites: linear
T/RH calibration matched ML for PM$_{2.5}$, transferred at R$^2\ge$0.56; gas calibrations transferred at R$^2\le$0.28.""",
r"""\textbf{Cross-day collisions.} 15 of this day's in-scope records were already issued in the 26 October issue and
are logged here as duplicates."""
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. A 30 October 00:21 UTC run harvested
23--28 October but stopped before screening; this issue was built on the 30 October 14:20 UTC (09:20 CDT) recovery run, which
backfills 23--29 October day by day. This issue collects \textbf{27 October in full}, continuous with the 26 October
issue. Consensus, Scholar Gateway and the trial watch for the backfill window are reported in the 29 October issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 30 in-scope records across nine bands. Exposure assessment leads with
six (plume back-trajectories, trajectory negative control, Paris plume optics, Nepal on-road BC, Faisalabad PMF, Khulna);
respiratory five; sensing and occupational/indoor four each; cardiovascular is the only empty band.""",
"f2_design_endpoint": r"""Left --- architecture: time-series, case-crossover, cohorts and burden models alongside
calibration, mobile, laboratory and monitoring analyses, two animal studies and one review; \textbf{metadata-only 1
(3\,\%)}. Nine records are \emph{European Journal of Public Health} conference abstracts recovered by Crossref title
match. Right --- endpoints run from emergency admissions, spirometry and sensitisation to infant antibiotic use,
absenteeism, cortisol and burden metrics.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ dominates; PM$_{10}$ (UK fire plume, Faisalabad,
Croatia), eBC (Nepal), PM$_1$ (Paris) and dust codes (Riyadh) also appear. Right --- geography: Europe carries the issue
(UK, Poland, Spain, Greece, Ireland, Slovakia, France, Sweden, Croatia and a five-country burden study); the USA is
second (California, Oklahoma, national infant life expectancy, PurpleAir heating), then South Asia and East Asia.""",
"f6_lifecourse": r"""Life-course windows: one prenatal record (Scotland); three childhood records (Head Start smoke,
Patras classrooms, Croatian ragweed sensitisation); three working-age records (cortisol at 24, PSPS, La Palma); no
adolescent or older-adult record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment sits in campaign, monitoring and
source-apportionment cells; sensing spans calibration comparison, laboratory instrumentation and ML; respiratory sits in
time-series and case-crossover; mechanistic toxicology in two animal studies and one review.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, four estimates from four studies: PSPS plus wildfire PM$_{2.5}$ and respiratory encounters
(California); regional fire detections and sick absence (OK-AIR Head Start); observed prenatal PM$_{2.5}$ vs a
5\,$\mu$g\,m$^{-3}$ counterfactual and infant amoxicillin (Scotland, controlled direct effect); rural residence and
ragweed sensitisation (Croatia, area-level PM$_{10}$/pollen contrast). Exposure contrasts differ completely. Not
poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: cancer years of life lost per 10\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ at lag 0--1, Pudong, Shanghai
(2013--2021).}\end{minipage}"""

PROV = r"""Entry window \textbf{27 October 2026}, single day (Tuesday). Harvester legs (run 30 Oct 00:21 UTC): \textbf{PubMed}
health \textbf{27}, sensing \textbf{6}; \textbf{Europe PMC} \textbf{159} raw (25 AGRICOLA retro-index dropped);
\textbf{Crossref by ISSN} \textbf{49}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. PubMed
connector (EDAT 23--28 Oct, bucketed) 32 for this day. \textbf{199 screened}. DOIs and abstracts for 15 \emph{Eur J
Public Health} conference abstracts recovered by Crossref title match. \textbf{30 admitted}, \textbf{169 rejected}
with logged reasons, of which 15 are cross-day duplicates of the 26 October issue and 3 within-window copies.
\textbf{DOI gate} 0 fail / 0 warn. \textbf{1 carried on metadata alone}. Abstracts remain the copyright of their
publishers."""
