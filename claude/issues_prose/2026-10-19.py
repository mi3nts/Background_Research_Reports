# -*- coding: utf-8 -*-
HEAD = dict(long="19 October 2026", window="19 October 2026 (full day)", n=18, excl=70,
            bands=9, eff=5, tierA=1, meta=6)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}In 131,346 Guangdong schoolchildren, mass-normalised oxidative potential
explains allergy-related symptoms more consistently than PM$_{2.5}$ mass --- and carries up to 36\,\% of a
constituent's association.}\\[1.4mm]
\footnotesize
Six cities, ages 6--18; DTT oxidative potential as volume- (DTTv) and mass-normalised (DTTm) metrics alongside
PM$_{2.5}$ mass, metals, carbonaceous fractions and ions. Mass and OP were both positively associated with rhinitis,
rhinoconjunctivitis and eczema symptoms; DTTm gave lower AIC/BIC and survived two-pollutant models best. Mixture
and mediation analyses put the largest indirect share at \textbf{36.2\,\%} (OC $\to$ DTTm $\to$ rhinoconjunctivitis),
with Co, Cu and Hg also partly routed through OP.
\textbf{Where it is weak:} cross-sectional symptom questionnaires, no effect sizes in the abstract, and OP assigned
from a sparse filter network --- a better fit may reflect smoother exposure error as much as biology.
\textbf{Why it matters here:} optical low-cost sensors report mass only; if OP is the health-relevant axis, mass
networks need a co-located speciation or OP tier to be interpretable for allergic endpoints."""

CHANGED = [
r"""\textbf{A PM null built on interpolation.} Korean stroke registry, $n$=27,340: post-discharge district PM$_{10}$
and PM$_{2.5}$ (IDW) unrelated to recurrence; only SO$_2$ showed a graded association (Q4 vs Q1 HR \textbf{1.19},
0.94--1.50), concentrated in harbour cities.""",
r"""\textbf{Secondary inorganic components and cognition.} CLHLS: per 10\,$\mu$g\,m$^{-3}$ HR 1.005 for PM$_{2.5}$
but 1.030 (sulphate) and 1.033 (ammonium); a favourable lifestyle halved risk and mediated $\sim$9\,\% of the
pollutant association.""",
r"""\textbf{Traffic counts do not substitute for monitors.} Bosphorus bridges, 17,520\,h: a traffic-only proxy gave
negative R$^2$ for every pollutant; ML with meteorology and autoregressive terms reached R$^2\approx$0.77 ---
mostly persistence.""",
r"""\textbf{Component-resolved assimilation.} CALIOP--MODIS species extinction assimilated by LETKF in WRF-Chem
recovers elevated free-tropospheric BC plumes over South Asia that the free model misses.""",
r"""\textbf{One record held.} \emph{Foehn}, a generative km-scale global PM$_{2.5}$ forecaster (arXiv 2610.25941,
tier A), was admitted but its DataCite DOI does not yet resolve; it is authored and held for the next issue.""",
]

CONT = r"""The 18 October issue closed with \texttt{last\_entry\_date} at 18 October. This issue collects
\textbf{19 October in full}, continuous with it. Built on the run that started 23:0x CDT on 19 October (04:0x UTC
20 October), i.e.\ after the 22:00 cut-off, so the day is complete. 20 October is due on the next run at or after
22:00 CDT."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 18 in-scope records across nine bands. Exposure assessment (5) and
burden/mitigation (4) lead; every health band holds a single record; other clinical endpoints is empty.""",
"f2_design_endpoint": r"""Left --- architecture: two cohorts, two cross-sectional, three modelling/inventory, four
measurement, one laboratory; \textbf{metadata-only 6 (33\,\%)}, all Elsevier/T\&F titles without an indexed abstract
on day 0. Right --- endpoints: cognition, stroke recurrence, allergy symptoms, lung cancer proteome, urinary metals.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM/emissions and PM$_{2.5}$-only records dominate;
one composition, one optical-property and one size-resolved record. Right --- geography: China 4, not-stated or
global 6, then Korea, East Asia, Iran, Turkiye, Thailand, Italy and the USA.""",
"f6_lifecourse": r"""Life-course windows: every window populated by a single study except older adults (CLHLS
cognition, CPS-II smokers). The childhood and adolescent counts are the same Guangdong survey.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. The only cell above one is exposure assessment $\times$
measurement campaign; the metadata-only column spreads across sensing, burden and indoor bands.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale: four HRs for incident cognitive disorder per 10\,$\mu$g\,m$^{-3}$ from one Chinese cohort
(PM$_{2.5}$, sulphate, nitrate, ammonium; single-pollutant models of collinear secondary components), and the
quartile HR for post-discharge SO$_2$ and stroke recurrence from a Korean registry, whose CI crosses 1. No PM
estimate from the stroke study is plotted because none was reported.}\end{minipage}"""

PROV = r"""Entry window \textbf{19 October 2026}, single day (Monday). Harvester legs: \textbf{PubMed} health
\textbf{4}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{96} (16 AGRICOLA retro-index dropped); \textbf{Crossref by
ISSN} \textbf{55}; \textbf{arXiv} 1 entry dated 19 October; \textbf{OpenAlex} HTTP 429. 137 unique, 50 already
carried, 87 fresh. \textbf{PubMed connector} (EDAT 19 Oct) 6 PMIDs, 2 appended --- \textbf{89} candidates screened,
\textbf{19 admitted}, \textbf{70 rejected} with logged reasons; 1 admitted record \textbf{held} (arXiv DOI not yet
registered), leaving \textbf{18}. \textbf{Consensus} calibration sweep: 10 hits, 0 new. \textbf{DOI gate} 0 fail /
0 warn after the hold. \textbf{Trial watch}: 0 registrations updated 19--20 October. Abstract retry (PubMed, Europe
PMC, Crossref, Semantic Scholar) recovered none of the six day-0 Elsevier and T\&F records; \textbf{6 carried on
metadata alone}. \textbf{Scholar Gateway} not called. Abstracts remain the copyright of their publishers."""
