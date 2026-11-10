# -*- coding: utf-8 -*-
HEAD = dict(long="6 November 2026", window="6 November 2026 (full day)", n=26, excl=62,
            bands=9, eff=8, tierA=2, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}In 75,602 asthma emergency visits in Lima, PM$_{2.5}$ rising from 5 to 15\,$\mu$g/m$^3$ gave OR 1.09 (1.01--1.16) at lag 0, the exposure--response was steepest at low concentrations, and the cumulative 0--15-day association was larger within 400\,m of a major road (OR 4.02, 1.97--8.19) than beyond it (1.66, 0.81--3.38; interaction p=0.04).}\\[1.4mm]
\footnotesize
Time-stratified case-crossover with DLNM, 10 public hospitals, 2017--2023, mean patient age 16; daily PM$_{2.5}$ from a 1$\times$1\,km multi-source model at the geocoded residence (Johns Hopkins / Cayetano Heredia).
\textbf{Where it is weak:} the contrast behind the cumulative ORs is not stated in the abstract and their size is hard to reconcile with a 2\,\% per-lag effect; the road modifier almost certainly carries traffic NO$_2$ and ultrafine particles that a 1-km PM$_{2.5}$ surface does not resolve.
\textbf{Why it matters here:} a road-proximity gradient finer than the exposure grid is the measurable question for curbside low-cost nodes, and a supra-linear curve at 5--15\,$\mu$g/m$^3$ puts the burden where sensor precision is worst."""

CHANGED = [
r"""\textbf{Deep phenotyping meets long-term PM.} German Diabetes Study, 1,120 recent-onset patients with clamp measurements: per IQR of 5-year PM$_{2.5}$, albuminuria geometric-mean ratio 1.72 (1.34--2.20) in type 1 and 1.71 (1.41--2.08) in type 2, HbA$_{1c}$ 1.07 and 1.04, DSPN OR 1.53 (1.02--2.32). Cross-sectional and many outcomes; exposure modelled.""",
r"""\textbf{Model-only smoke exposure misses the days that matter.} CMAQ against 187,051 California fire-season site-days: r 0.50, RMSE 9.96\,$\mu$g/m$^3$, and 1,273 of 2,151 observed $>$35\,$\mu$g/m$^3$ site-days missed through spatial--temporal mismatch. A random forest with fire-only CMAQ as a predictor reached R$^2$ 0.71 on held-out site-years.""",
r"""\textbf{Indoor endpoints fitted to outdoor monitors.} Shandong ICU, 6,196 cardiac-surgery patients: PM$_{2.5}$ 30 vs 10\,$\mu$g/m$^3$ gave 14.2\,\% (2.6--27) higher odds of hospital-acquired pneumonia at lag 1 --- an exposure assigned from city monitors to patients in filtered ICU air.""",
r"""\textbf{Sensors reported as compliance.} A single unnamed ``automatic sensor'' in Jhansi supports a whole-year NAAQS assessment (annual PM$_{2.5}$ 37.5 vs standard 40) with no co-location; a Bhopal indoor survey uses uncorrected DustTrak photometry in humid biomass-smoke homes.""",
r"""\textbf{Exposure basis (x1).} Of 26 records, 1 rests on a low-cost sensor (Jhansi, sensing side) and none on a personal monitor. Health-side exposure is mostly modelled or monitor-assigned: the Lima, Diabetologia and UK Biobank records use residential models, the ICU, Kashi and Thai records city monitors, and the miner cohort self-report. \emph{None of the 8 effect estimates rests on a measured personal or sensor exposure.}""",
]

CONT = r"""The 5 November issue closed with \texttt{last\_entry\_date} at 5 November. No run fired successfully on 7, 8 or 9 November. This issue was built on the \textbf{10 November 22:16 UTC (16:16 CST) run}, the 05:00 UTC slot firing 17 hours late. Before 22:00 the newest buildable day is 9 November, so this run backfills \textbf{6, 7, 8 and 9 November as four issues} and builds the \textbf{W45 weekly (1--7 November)} owed since Saturday. A cross-day candidate set was built first and each record assigned to its earliest day (Europe PMC re-surfaced 33 records on later days). Friday: no rollup of its own. No \textsc{backfill} from Amass this run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 26 records across nine bands: exposure assessment, occupational and indoor, mechanistic and burden 4 each; respiratory 3; neuro, cardiovascular and sensing 2 each; other clinical 1. Reproductive is empty.""",
"f2_design_endpoint": r"""Left --- architecture: a wide spread of designs with no dominant class; three cohorts, three metadata-only records, two systematic reviews, two field measurements and one case-crossover among them. Right --- endpoints are almost all singletons, and three are unrecoverable (metadata only).""",
"f3_metric_geography": r"""Left --- particle metric, dominated by PM$_{2.5}$ alone. Right --- geography by region: Europe 5 (Germany, Spain, Poland, UK, Alpine region), global or multi-region 5 (three reviews, the GBD record and the MR study), China 5, South Asia 3, and 2 each for sub-Saharan Africa (Somalia, Malawi), North America and East Asia ex-China; one each Southeast Asia and Latin America (Lima).""",
"f6_lifecourse": r"""Life-course windows. Children: Lima asthma (mean age 16) and Somalia under-five mortality; adolescence: Lima; working age adds miners, metro workers, the diabetes cohort, ICU patients and the AML review; older adults add the neuro review, the CKD dementia cohort and the CarVasCLiMa protocol. No preconception or in-utero record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Burden spreads across ecological, GBD and hazard-quotient designs; mechanistic splits into animal, organoid, MR and metadata-only; the two cohorts sit in respiratory/occupational and neuro, and the one acute design is the Lima case-crossover.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, 8 estimates from 4 sources: Singh German Diabetes Study (5, per IQR; geometric-mean ratios for continuous outcomes and one OR), Espinoza-Guillen Lima asthma (1, per 10\,$\mu$g/m$^3$), Li Shandong ICU pneumonia (1, 30 vs 10\,$\mu$g/m$^3$) and Kim coal miners (1, high vs low self-reported dust). The five Singh estimates share one sample and exposure and are not independent; no two sources share metric, endpoint family and increment, so no pooling and no I$^2$.}\end{minipage}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{6 November 2026}, single day (Friday). Harvester legs: \textbf{PubMed} health \textbf{16}, sensing \textbf{0}; \textbf{Europe PMC} \textbf{43}; \textbf{Crossref by ISSN} \textbf{44}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 429 on the harvester leg. 99 unique after cross-source dedupe, 14 already carried, \textbf{85 fresh}; PubMed connector (EDAT 6--9 Nov, three axes) 69 PMIDs, 22 bucketed to 6 Nov, 9 appended; 6 removed as previously carried or rejected --- \textbf{88 screened}. Abstracts: efetch filled 21 of 23 PubMed gaps; Elsevier and ACS day-0 deposits stayed empty.
\textbf{Consensus} calibration sweep and \textbf{Amass} were not used for backfill on this four-day run. OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run. Affiliations from PubMed XML.
\textbf{26 admitted}, \textbf{62 rejected} with logged reasons. \textbf{Trial watch}: see the W45 weekly. \textbf{3 carried on metadata alone}.
Abstracts remain the copyright of their publishers."""
