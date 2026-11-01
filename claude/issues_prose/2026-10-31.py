# -*- coding: utf-8 -*-
HEAD = dict(long="31 October 2026", window="31 October 2026 (full day)", n=10, excl=36,
            bands=6, eff=2, tierA=2, meta=2)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Idaho, 32 AQS sites over 20 years: winter wood smoke and the clean
background fell, fire-season PM$_{2.5}$ rose 2.54\,$\mu$g\,m$^{-3}$ per decade, and the annual mean stayed flat.}\\[1.4mm]
\footnotesize
4,260 site-months (2005--2024), Theil--Sen trends, PCA and IDW. Regional mean 7.53\,$\mu$g\,m$^{-3}$ (sites 3.16--12.08);
an August--September wildfire peak and a November--February inversion/wood-smoke peak, with July--September carrying
36.6\,\% of annual mass. 32.7\,\% of site-years exceed the 9.0\,$\mu$g\,m$^{-3}$ annual standard.
\textbf{Where it is weak:} an unreviewed preprint; IDW across 32 sites in mountain terrain is not an exposure surface,
and the two ``regimes'' are PCA loadings, not apportioned sources.
\textbf{Why it matters here:} a flat annual mean hiding two diverging seasonal sources is the case for season-specific
sensor correction --- smoke and wood-smoke aerosol need different optical calibrations."""

CHANGED = [
r"""\textbf{Stroke in a clean karst city.} Guiyang 2016--2021, 11,517 strokes: PM$_{2.5}$ RR 1.026 (1.005--1.048) and
PM$_{10}$ 1.015 (1.001--1.030) per 10\,$\mu$g\,m$^{-3}$ at the maximal lag; single-pollutant models only.""",
r"""\textbf{Informal workplaces.} Agra footwear cluster, 378 worker-sessions: no session met the WHO PM$_{2.5}$
guideline, and air velocity (0.80 to 0.16\,m\,s$^{-1}$ from factory to cottage) explained 79\,\% of between-tier variance.""",
r"""\textbf{Antibiotics in PM$_{2.5}$.} A 74-compound UPLC-MS/MS method (LOQ to 0.37\,pg\,m$^{-3}$) found 22 antibiotics
in 29 Beijing samples; roxithromycin in all of them.""",
r"""\textbf{Particulate matter leads T2DM attributable burden across Asia} (GBD 2023) --- a modelled attribution, not
new evidence of causality.""",
r"""\textbf{A thin Saturday.} 46 candidates after 18 cross-day duplicates went to the 30 October issue; 10 admitted, two on
metadata alone (Guanzhong humidity--PM, kitchen purifiers in 338 cities). Retry those abstracts first.""",
]

CONT = r"""The 29 October issue closed with \texttt{last\_entry\_date} at 29 October. This issue was built on the
\textbf{1 November 05:2x UTC (00:2x CDT) run}; by the 22:00 rule 31 October is complete and 1 November is \emph{not}
opened. The run backfills 30 and 31 October as separate issues; candidates surfacing on both days (18) were screened
once and assigned to 30 October. This issue covers \textbf{31 October in full} (Saturday). The W44 weekly (25--31
October) and the October monthly are filed under this date."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 10 in-scope records across six bands. Respiratory, exposure, occupational
\& indoor and burden carry two each; cardiovascular (Guiyang stroke) and sensing (antibiotics in PM$_{2.5}$) one each.
Neuro, reproductive, mechanistic and other-clinical bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: three modelling (Bayesian influenza, causal-ML asthma, GBD), two
experimental (analytical method, filtration membrane), two metadata-only, and one each acute time-series,
cross-sectional (occupational) and measurement record analysis. Right --- endpoints from stroke and influenza to
asthma, T2DM burden, workplace IAQ and filtration efficiency.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 6, unspeciated 3, joint PM$_{2.5}$+PM$_{10}$ 1
(Guiyang). Right --- geography: China 4, global/multi-country or laboratory 3, North America 2 (Idaho, Colorado), South
Asia 1 (Agra).""",
"f6_lifecourse": r"""Life-course windows: one childhood-inclusive record (county asthma, all ages), one working-age
(footwear workers) and one older-adult signal (stroke risk stronger at $\geq$65). No in-utero or adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. The health bands sit in acute and modelling cells; sensing is a
single analytical-method cell; exposure splits between record analysis and metadata-only.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, two estimates from one study: stroke incidence per 10\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ and PM$_{10}$ at
the maximal lag (Guiyang, 11,517 strokes, single-pollutant GAM). Same population, same outcome --- not independent and
not poolable.}\end{minipage}"""

PROV = r"""Entry window \textbf{31 October 2026}, single day (Saturday). Harvester legs: \textbf{PubMed} health
\textbf{6}, sensing \textbf{0}; \textbf{Europe PMC} \textbf{35} (5 AGRICOLA retro-index records dropped);
\textbf{Crossref by ISSN} \textbf{22}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. 62 unique,
2 already carried, 60 fresh; PubMed connector (EDAT 30--31 Oct, health and sensing axes) 9 PMIDs bucketed to 31 Oct,
1 merged, 4 appended (64); \textbf{18 cross-day duplicates assigned to 30 October}, \textbf{46 screened}. Abstracts for
10 PubMed records recovered by efetch; Crossref recovered none for the Elsevier day-0 deposits. \textbf{Consensus}
calibration sweep: 10 hits, 0 new (Yan 2026 and Guo 2026 matched by DOI to earlier issues/rejections).
\textbf{10 admitted}, \textbf{36 rejected} with logged reasons. \textbf{Trial watch} 30 October--1 November: 0
registrations updated. \textbf{2 carried on metadata alone}. \textbf{Scholar Gateway} not called.
Abstracts remain the copyright of their publishers."""
