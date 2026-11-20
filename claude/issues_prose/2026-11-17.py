# -*- coding: utf-8 -*-
HEAD = dict(long="17 November 2026", window="17 November 2026 (full day)", n=26, excl=49,
            bands=7, eff=2, tierA=2, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Against 249 CPCB monitors, CAMS reanalysis overstates Indian PM$_{2.5}$ by +56\,$\mu$g\,m$^{-3}$ (monthly RMSE 79) and flags 60\,$\mu$g\,m$^{-3}$ exceedances on 64.6\,\% of cell-days against 27.0\,\% observed; the satellite-derived SatPM$_{2.5}$ product is nearly unbiased (MB $-$2.1, RMSE 25.3, r 0.71).}\\[1.4mm]
\footnotesize
NARL Gadanki and IIST, \textit{Environmental Monitoring and Assessment}; CAMS EAC4, MERRA-2 and SatPM$_{2.5}$ V6.GL.02.04 on a common 0.75$^\circ$ grid (101 cells), 2022--2023. A spatiotemporal holdout multiplicative correction cut CAMS daily RMSE from 84.5 to 33.2\,$\mu$g\,m$^{-3}$ (IOA 0.58 to 0.78); MERRA-2 underestimates (MB $-$6.8) and under-calls exceedances (20.0\,\%).
\textbf{Where it is weak:} validation is at 0.75$^\circ$ against a monitor network concentrated in cities, so rural and sub-grid error --- where these products are actually used for exposure --- is not characterised, and SatPM$_{2.5}$ is evaluated only monthly.
\textbf{Why it matters here:} any satellite--sensor fusion in India inherits one of these surfaces as its prior; a raw CAMS prior more than doubles the apparent exceedance burden, and the correction needs ground truth with far denser coverage than CPCB provides."""

CHANGED = [
r"""\textbf{Dementia in a low-pollution cohort.} Generation Scotland, 22\,071 adults, 18 y, EMEP4UK CTM exposure: above-average annual PM$_{2.5}$, HR 1.48 (1.15--1.90) for all-cause dementia; PM$_{10}$ in one-allele APOE\,$\varepsilon$4 carriers, HR 2.38 (1.36--4.16). Both are dichotomies at the cohort mean, not per-increment slopes, from eight pollutants $\times$ five outcomes.""",
r"""\textbf{Km-scale probabilistic PM$_{2.5}$ forecasting.} Foehn (LUT, preprint), a generative model trained on global kilometre-scale PM$_{2.5}$ estimates, beat the operational forecast at three stations in four and detected local extremes four days ahead as well as the operational system does one day ahead --- but it needs real-time km-scale input that does not yet exist. Dense sensor networks are the obvious candidate.""",
r"""\textbf{An LCS node as forecast target, Kampala.} 696 hourly AirQo observations on Jinja Road: congestion indicators from Google Routes made gradient-boosting forecasts worse (R$^2$ 0.575 to 0.475); lagged PM$_{2.5}$ gave the best fit (R$^2$ 0.625). One corridor, 29 days, calibration status unstated.""",
r"""\textbf{Behaviour change, no exposure measurement.} Ibadan AirHealth pre--post study (607 adults): SBP fell 4.58\,mmHg (1.43--7.74) with no control group and no PM measurement, so nothing links the BP change to dose.""",
r"""\textbf{Exposure basis (x1).} Of 26 records one rests on a low-cost network (Kampala) and five on regulatory monitors. On the health side the recoverable bases are mostly measured, but the only two PM effect estimates today (Generation Scotland) come from a CTM at postcode scale; \emph{no health estimate today rests on sensor-measured exposure.}""",
]

CONT = r"""The 16 November issue closed the day before. This issue was built on the \textbf{20 November 01:04 UTC (19:04 CST 19 November) run}. Before 22:00 CST the newest buildable day is yesterday, so this run owes \textbf{17 and 18 November as two issues} (Tuesday and Wednesday; no rollup); \textbf{17 November is covered in full}. Five PubMed records with entry date 16 November (entered after that day's harvest closed) were unassigned; all five surfaced in today's harvest and were screened here (three admitted: India product evaluation, Himalaya PM$_{2.5}$ elements, Israel AMI time-series; two rejected: NO$_2$ hotspots, radon). No \textsc{backfill} records today."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 26 records across seven of ten bands: exposure assessment 9, sensing 4, cardiovascular/metabolic 4, occupational \& indoor 4, burden 3, neuro/mental health 1, respiratory 1. Mechanistic, reproductive and other clinical are empty today.""",
"f2_design_endpoint": r"""Left --- architecture: measurement campaigns dominate (10), then modelling/inventory work (5) and five metadata-only records; one cohort, one non-randomised intervention, one acute time-series, one ecological study, one review and one software tool. Right --- endpoints are singletons apart from the metadata-only bar.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only 7, unspeciated PM or emissions 7, PM$_{2.5}$ and PM$_{10}$ jointly 5, optical properties 3, PM$_{10}$ only 2, composition 1, size-resolved 1. Right --- geography: Europe 6, China 4, South Asia 3, sub-Saharan Africa 3, global / multi-region 3, Middle East \& North Africa 2, East Asia ex-China 2, and one each from North America, Latin America and the remote Indian Ocean.""",
"f6_lifecourse": r"""Life-course windows. Working age: the Ibadan AirHealth adults, the landfill-mining and microplastic inhalation work and care-home staff; older adults: Generation Scotland dementia, CHARLS (45+) and the Belgian nursing homes. No record addresses pregnancy, childhood or adolescence today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment is mostly measurement campaigns (5) with two modelling/inventory papers, one tool and one metadata-only record; sensing is three modelling/forecasting papers and one campaign; cardiovascular is spread across trial, acute, ecological and metadata-only cells; the single cohort is the neuro record.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, two estimates, both Generation Scotland (EMEP4UK annual residential exposure, 18 y Cox models): all-cause dementia for above- vs below-average PM$_{2.5}$, HR 1.48 (1.15--1.90), and for above-average PM$_{10}$ in carriers of one APOE\,$\varepsilon$4 allele, HR 2.38 (1.36--4.16). Both are categorical contrasts at the cohort mean, not per-increment slopes. Israel AMI (PM$_{2.5}$ ``small but significant'') and Madrid STEMI (truncated abstract) gave no extractable estimate.}\end{minipage}

\vspace{2mm}
"""

X1NOTE = ""

PROV = r"""Entry window \textbf{17 November 2026}, single day (Tuesday). Harvester legs: \textbf{PubMed} health \textbf{17}, sensing \textbf{0}; \textbf{Europe PMC} \textbf{14}; \textbf{Crossref by ISSN} \textbf{47}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 403 on the harvester leg. 78 raw, 75 unique, 7 already carried, 68 fresh. PubMed connector (EDAT 17--18 November, health, instrumentation and MeSH axes) 42 PMIDs (\texttt{\_conn\_1120.py}): 22 bucketed to 17 November (4 seen, 1 merged, 9 appended) plus 5 entered 16 November after that harvest closed, screened here --- 77, of which 2 were already rejected/seen, \textbf{75 screened}. Abstracts: efetch filled 18 of 18 PMID records; Crossref/Semantic Scholar recovered none of the 7 Elsevier/ACS records tried.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run. No Amass or Consensus backfill this run.
\textbf{26 admitted}, \textbf{49 rejected} with logged reasons (\texttt{\_rej\_1120\_17.py}). \textbf{5 carried on metadata alone} (one with a two-sentence Crossref fragment). Affiliations from PubMed XML and Crossref; "not stated" where the record carries none. Trial watch: see W47 weekly.
Abstracts remain the copyright of their publishers."""
