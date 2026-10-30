# -*- coding: utf-8 -*-
HEAD = dict(long="28 October 2026", window="28 October 2026 (full day)", n=22, excl=96,
            bands=9, eff=8, tierA=2, meta=7)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}West Oakland: a dense black-carbon network plus Bayesian inversion
raises the BC inventory by a third and quadruples the exposure share of neighbourhood and port sources.}\\[1.4mm]
\footnotesize
Mobile and fixed-site BC measurements (6.7 sites\,km$^{-2}$) were assimilated into hourly 150\,m emission maps. The
posterior added $\sim$33\,\% to bottom-up BC emissions and moved the population-weighted exposure share of local and
port-related sources from 5 to 20\,\%, concentrated in low-income blocks beside freight corridors. A thinned network of
$\sim$10 fixed monitors ($\sim$1\,km$^{-2}$) plus time-averaged mobile maps gave similar answers.
\textbf{Where it is weak:} the posterior inherits the transport kernel and prior error covariance; ``unaccounted''
sources are inferred, not inspected, and this is one community.
\textbf{Why it matters here:} it is the clearest demonstration yet that a sensor network's value is in inversion, not
in concentration maps --- and it states the density needed."""

CHANGED = [
r"""\textbf{Urban firestorm smoke is a metal plume.} Eaton fire, Los Angeles: lead $>$50-fold, halogens 7-fold, arsenic
3-fold above wildfire smoke; $\sim$7 million residents above 50\,ng\,m$^{-3}$ 24-h lead. Optical sensors see the mass,
not the toxicity.""",
r"""\textbf{Low-cost sensors as the sole exposure metric.} Kinshasa LBW study used calibrated PurpleAir PA-II-SD
(0.52$\times$raw\,+\,3.2 vs BAM): area PM$_{2.5}$ $>$75\,$\mu$g\,m$^{-3}$ aOR 1.18 (0.59--2.36) --- but sensors ran
48--72\,h in 2022 for births in 2021.""",
r"""\textbf{Component scaling artefact.} China 123-city cohort: BC HR 1.381 per 1\,$\mu$g\,m$^{-3}$ vs PM$_{2.5}$ 1.027
--- a per-unit comparison across ranges that differ tenfold.""",
r"""\textbf{Paediatric asthma, Louisiana.} 28,499 hospitalisations: PM$_{2.5}$ lag 0--3 OR 1.079 (1.052--1.107),
robust to co-pollutants; no significant modification by race or Medicaid.""",
r"""\textbf{Cross-day duplicates.} 14 records in the 28 October harvest had already entered the 27 October pool via
Europe PMC/PubMed lag and were issued there; one record, one issue.""",
r"""\textbf{Metadata-only share 32\,\%.} Seven day-0 Elsevier/T\&F deposits with no abstract anywhere; abstract retry
(EPMC $\rightarrow$ Semantic Scholar) recovered none.""",
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. Scheduled runs for 23--29 October did
not complete: a run at 00:21 UTC on 30 October harvested 23--28 October but stopped before screening. This issue was
built on the \textbf{30 October 2026 14:20 UTC (09:20 CDT) recovery run}, which backfills 23--29 October day by day, each with its
own window and issue. This issue collects \textbf{28 October in full}, continuous with the 27 October issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 22 in-scope records across nine bands. Exposure assessment leads with six
(urban-fire metals, fireworks, PM--O$_3$ coupling and three metadata-only records); respiratory three; burden/policy is
empty.""",
"f2_design_endpoint": r"""Left --- architecture: cohorts, cross-sectional surveys, field measurements, one inversion
method, one case-crossover, one ecological panel; \textbf{metadata-only 7 (32\,\%)}. Right --- endpoints run from LBW,
childhood haemoglobin and eGFR to asthma admissions, OSA, heart disease and cancer recurrence.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only dominates; BC and speciated metals carry the two
tier-A records. Right --- geography: China leads; USA second (Oakland, Los Angeles, Louisiana); one each for DRC and
Brazil; several metadata-only records carry inferred locations.""",
"f6_lifecourse": r"""Life-course windows: in utero two (Fujian haemoglobin/anaemia, Kinshasa LBW); childhood three;
adolescence two; working age three; no dedicated older-adult record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment spreads over measurement and metadata-only
cells; the health bands sit in cohorts and cross-sectional surveys; sensing holds the inversion method and one
metadata-only metrology record.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, seven estimates from six studies: Louisiana paediatric asthma (PM$_{2.5}$ lag 0--3); China
123-city heart disease per 1\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ and BC; lung cancer recurrence per within-site SD;
Sichuan adolescent anxiety per IQR PM$_{10}$; Kinshasa LBW (area PM$_{2.5}$ $>$75\,$\mu$g\,m$^{-3}$); Brazil
circulatory admissions per fire-detection density. Contrasts differ completely. Not poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: eGFR (mL\,min$^{-1}$\,1.73\,m$^{-2}$) per IQR (0.505\,$\mu$g\,m$^{-3}$) of landscape-fire
PM$_{2.5}$ in 12,102 Chinese children --- a large effect for a tiny contrast; read with the confounding caveat.}\end{minipage}"""

PROV = r"""Entry window \textbf{28 October 2026}, single day (Wednesday). Harvester legs (run 30 Oct 00:21 UTC):
\textbf{PubMed} health \textbf{16}, sensing \textbf{2}; \textbf{Europe PMC} \textbf{26}; \textbf{Crossref by ISSN}
\textbf{78}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. PubMed connector (EDAT 23--28 Oct,
bucketed by entrez date) 18 PMIDs for 28 Oct; \textbf{118 screened}. Abstract retry (efetch; Europe PMC
$\rightarrow$ Semantic Scholar) recovered none of the 7 day-0 deposits. \textbf{22 admitted}, \textbf{96 rejected}
with logged reasons, of which 14 are cross-day duplicates issued under 27 October. \textbf{DOI gate} run before
build. Consensus sweep and trial watch for 23--29 October are reported in the 29 October issue. \textbf{7 carried on
metadata alone}. \textbf{Scholar Gateway} not called. Abstracts remain the copyright of their publishers."""
