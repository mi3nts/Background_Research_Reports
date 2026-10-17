# -*- coding: utf-8 -*-
HEAD = dict(long="16 October 2026", window="16 October 2026 (full day)", n=18, excl=107,
            bands=7, eff=3, tierA=2, meta=2)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Gating lidar's extinction-to-PM$_{2.5}$ conversion on aerosol
type cuts surface RMSE by 38\,\% and bias by about 83\,\% --- the coarse-dust error that also breaks optical
low-cost sensors is separable by depolarisation plus fluorescence.}\\[1.4mm]
\footnotesize
A Beijing fluorescence--Raman--Mie polarisation lidar classifies anthropogenic pollution aerosol, desert dust and
mineral dust by particle depolarisation ratio and fluorescence capacity, then applies the extinction--PM$_{2.5}$
regression only to the anthropogenic fraction. Date-separated validation (411 hourly samples, 69 days): RMSE
\textbf{17.32}, MAE \textbf{13.54}, bias \textbf{3.30}\,$\mu$g\,m$^{-3}$, against an unconstrained model that was
38\,\%, 45\,\% and $\sim$83\,\% worse.
\textbf{Where it is weak:} validation is at the surface only, so the vertical structure --- the point of a lidar
--- is unverified, and the scatter of the empirical extinction--mass relation, not the classification, dominates the
remaining uncertainty.
\textbf{Why it matters here:} optical LCS overestimate mass in dust and under-read it in hygroscopic haze for the
same reason; a type flag from a co-located ceilometer or depolarisation lidar is a practical gate for network QC."""

CHANGED = [
r"""\textbf{MESA, the cohort built to cut exposure error, still leans null on PM$_{2.5}$ for AF.} 6,618 participants,
16.5\,y, 1,055 AF events, time-varying 2-y exposures from the MESA Air spatiotemporal model: NO$_2$ HR
\textbf{1.29} (1.00--1.67) per 13.5\,ppb; PM$_{2.5}$ weaker and unreported in the abstract.""",
r"""\textbf{Platform error in UAV sensing.} Rotor-wash bias of 3--10\,\% in hover and 6--15\,\% at 5\,m/s across
PM$_{2.5}$, PM$_{10}$ and gases; correlation with a fixed reference fell to \textbf{r = 0.44} in forward flight.""",
r"""\textbf{Per-mass toxicity is set by organic composition.} Mass-normalised ROS yield tracked the
oxidised/unsaturated organic ratio across Chinese, German and boreal aerosol, independent of loading --- a
variation mass-only networks cannot see.""",
r"""\textbf{An occupational dose--response.} Brazilian street vendors ($n$=238, four campaigns): micronucleus IRR
\textbf{1.024} (1.013--1.034) and \textbf{1.026} (1.019--1.034) per 1\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ in rainy and dry
seasons, but exposure is collinear with working outdoors.""",
]

CONT = r"""The 15 October issue closed with \texttt{last\_entry\_date} at 15 October. This issue collects
\textbf{16 October in full}, continuous with it. 17 October is not opened: this run began at 11:40 CDT on
17 October, before 22:00. The \textbf{17 October daily and the W42 weekly} (11--17 October) are due on the next
run at or after 22:00 CDT."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 18 in-scope records across seven bands. Sensing leads (5) with the
lidar tier-A record; mechanistic toxicology (4, three of them reviews) and exposure assessment (2) follow.
Neuro, respiratory and reproductive bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: reviews and method/algorithm papers make up a third of the
issue; metadata-only 2 (11\,\%). Right --- health endpoints: incident AF, CVD admissions, buccal micronuclei,
nasopharyngeal-carcinoma survival, and mechanistic endpoints from the reviews.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ mass dominates; optical (lidar extinction, MISR
AOD) and organic-composition (ROS) records appear on the measurement side. Right --- geography: global/multi-region (7: reviews, MISR, the
ROS synthesis) leads; North America and China 4 each; Brazil, Thailand and Spain/Ireland complete it.""",
"f6_lifecourse": r"""Life-course windows: one working-age sample (street vendors) and two older-adult samples
(MESA, Florida $\geq$65). No preconception, child or adolescent record --- the first issue since 4 October with
the early-life windows empty.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. The sensing row splits across retrieval, UAV deployment
and algorithm records; mechanism is almost entirely review.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale: two micronucleus IRRs per 1\,$\mu$g\,m$^{-3}$ of work-area PM$_{2.5}$ from one Brazilian
panel (rainy and dry campaigns, same men), and one RR per interquartile contrast of daily PM$_{2.5}$ for stroke
admissions among Black patients in West Florida. Units differ; the panel IRRs per 1\,$\mu$g\,m$^{-3}$ imply
$\sim$27\,\% per 10\,$\mu$g\,m$^{-3}$ if log-linear.}\end{minipage}"""

PROV = r"""Entry window \textbf{16 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{15},
sensing \textbf{3}; \textbf{Europe PMC} \textbf{123} raw (57 AGRICOLA retro-index dropped); \textbf{Crossref by ISSN}
\textbf{48}; \textbf{arXiv} no entry dated 16 October; \textbf{OpenAlex} HTTP 429. 129 unique, 8 already carried,
121 fresh. \textbf{PubMed connector} (EDAT 16 Oct) 15 PMIDs, 4 appended --- \textbf{125} candidates screened,
\textbf{18 admitted}, \textbf{107 rejected} (one admitted record failed the DOI gate as already shipped on 14 October) with logged reasons. \textbf{Consensus} calibration sweep: 10 hits,
\textbf{0 new}. \textbf{Trial watch}: 0 registrations updated 16--17 October. Abstracts recovered via PubMed,
Europe PMC and Crossref for 16 of 18; \textbf{2 records carried on metadata alone}. \textbf{Scholar Gateway} not
called (still \texttt{ACCESS\_DENIED} on previous runs). Abstracts remain the copyright of their publishers."""
