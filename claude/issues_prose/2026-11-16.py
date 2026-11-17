# -*- coding: utf-8 -*-
HEAD = dict(long="16 November 2026", window="16 November 2026 (full day)", n=15, excl=46,
            bands=7, eff=0, tierA=0, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Ethiopia's air-pollution burden is 139 deaths per 100\,000 (95\,\% UI 106--177) in GBD 2023, with Addis Ababa carrying the highest ambient-PM mortality (64 per 100\,000, 43--88) --- numbers that rest almost entirely on a modelled exposure surface.}\\[1.4mm]
\footnotesize
Adigrat and Bule Hora universities, \textit{Environmental Health Insights}; GBD 2023 national and subnational re-analysis, 1990--2023. DALYs 4557 per 100\,000 (3685--5397); YLDs dominated by household solid fuel (247 per 100\,000); Afar has the highest total mortality (185 per 100\,000). Mortality rates were flat over 33 years while DALY rates fell.
\textbf{Where it is weak:} no new data --- every subnational contrast is an output of GBD's exposure model, which in Ethiopia is constrained by very few ground monitors, so the uncertainty intervals understate exposure-surface error.
\textbf{Why it matters here:} this is the clearest case in today's set for what a distributed low-cost network buys: the ambient half of the burden is only as good as the PM$_{2.5}$ surface under it, and that surface is largely unobserved outside Addis Ababa."""

CHANGED = [
r"""\textbf{Growth-factor calibration of a low-cost PM sensor.} \textit{Aerosol and Air Quality Research} (Kiss, Kiss, Veres) calibrates an optical LCS through the hygroscopic growth factor --- the physics-based alternative to empirical RH terms. Metadata only: no sensor model, R$^2$ or RMSE retrievable today.""",
r"""\textbf{The same humidity problem, upstream.} A large-aperture scintillometer retrieves path-averaged aerosol mass flux over open water in eastern China (\textit{AMT}); the optical-to-mass factor $R_{MN}$ had to be refit as a function of RH against PM$_{10}$ and visibility, falling consistently with humidity. Campaign-median flux magnitudes 0.091--0.399\,$\mu$g\,m$^{-2}$\,s$^{-1}$.""",
r"""\textbf{Pregnancy PM$_{2.5}$ and postpartum mood: null, then a BMI interaction.} ECHO, 6407 women at 18 US sites, satellite-hybrid PM$_{2.5}$: no main effect on EPDS; a thin-plate PM$_{2.5}\times$BMI interaction for anhedonia at p=0.06, strongest for first-trimester exposure. Hypothesis-generating.""",
r"""\textbf{County AQI and child bone density.} New Mexico, 597 paediatric decedents on postmortem CT: poorer gestational AQI in trimesters 2--3 associated with lower BMD; no effect sizes in the abstract, and AQI is a composite at county scale.""",
r"""\textbf{Exposure basis (x1).} No admitted record reports a PM effect estimate with a CI today, so there is no forest. The three health records with an exposure are a satellite-fused residential surface (ECHO), a regulatory-monitor composite (county AQI) and a burden model (GBD); the two low-cost-relevant records (growth-factor calibration, the COPD/IPF home-IAQ framework) are on the measurement and guidance side. \emph{No health estimate today rests on sensor-measured exposure.}""",
]

CONT = r"""The 15 November issue closed the day before. This issue was built on the \textbf{17 November 05:06 UTC (23:06 CST 16 November) run}, which also completed the interrupted 16 November 05:40 UTC run: 12 and 14 November had been authored but not built (an unmapped design label stopped \texttt{plots.py}), 13 and 15 November were built but unshipped, and nothing had been pushed. After 22:00 CST the newest buildable day is today, so this run owes \textbf{12--16 November as five issues} plus the \textbf{W46 weekly (8--14 November)}; \textbf{16 November is covered in full}. Two PubMed records with entry date 15 November were found unassigned (the 15 November harvest had already closed) and screened here; one was admitted (New Mexico BMD), one rejected (ozone only). No \textsc{backfill} records today."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 15 records across seven of ten bands: occupational \& indoor 4, exposure assessment 3, sensing 2, respiratory 2, burden 2, neuro/mental health 1, reproductive 1. Mechanistic, cardiovascular/metabolic and other clinical are empty today.""",
"f2_design_endpoint": r"""Left --- architecture: reviews dominate (systematic, narrative and one bibliometric), three metadata-only records, one cohort, one cross-sectional and one case-control study, two modelling papers, a GBD burden analysis and one measurement campaign. Right --- endpoints are singletons apart from the metadata-only bar.""",
"f3_metric_geography": r"""Left --- particle metric as classified from the record fields. Right --- geography by record: single records from the United States, Ethiopia, China, India, France and Korea, with reviews filed as global / multi-region and three records with no stated geography.""",
"f6_lifecourse": r"""Life-course windows. In utero: the ECHO pregnancy cohort and the New Mexico gestational-AQI study; childhood: the New Mexico BMD outcome (ages 0.5--21); working age: the COPD/IPF indoor-air guidance, the occupational arrhythmia review and the upper-airway review; older adults: the Ethiopia GBD analysis, where older adults carry the heaviest burden. Adolescence has no dedicated record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Occupational \& indoor is all review or metadata-only work; exposure assessment splits between modelling and a metadata-only AOD record; sensing is one measurement campaign and one metadata-only calibration paper.""",
}

FOREST = r"""{\fontsize{7.4}{9}\selectfont\color{Slate}\textbf{No forest plot this issue.} No admitted record reports a PM effect estimate with a confidence interval. The ECHO analysis gives only an interaction p-value, the New Mexico BMD study no effect size, and the Ethiopia GBD figures are attributable burdens, not exposure--response estimates; the only ratio estimate harvested today (ozone and AMD in Korea) was rejected as gas-phase only.}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{16 November 2026}, single day (Monday). Harvester legs: \textbf{PubMed} health \textbf{6}, sensing \textbf{0}; \textbf{Europe PMC} \textbf{4}; \textbf{Crossref by ISSN} \textbf{47}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 403 on the harvester leg. 57 raw, 55 unique, 0 already carried, 55 fresh. PubMed connector (EDAT 16 November, health and instrumentation axes) 13 PMIDs (\texttt{\_conn\_1117.py}): 11 bucketed to 16 November and 2 to 15 November (unassigned, screened here), 6 appended --- \textbf{61 screened}. Abstracts: efetch/Europe PMC filled 10; Crossref recovered none of the three metadata-only records tried.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run. No Amass or Consensus backfill this run.
\textbf{15 admitted}, \textbf{46 rejected} with logged reasons (\texttt{\_rej\_1117\_16.py}). \textbf{3 carried on metadata alone}. Affiliations from PubMed XML; blank or "not stated" where the record carries none. Trial watch: see W46 weekly.
Abstracts remain the copyright of their publishers."""
