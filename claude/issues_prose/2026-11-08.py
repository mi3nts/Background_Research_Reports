# -*- coding: utf-8 -*-
HEAD = dict(long="8 November 2026", window="8 November 2026 (full day, Sunday)", n=5, excl=11,
            bands=3, eff=3, tierA=0, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Indoor and outdoor PM act jointly on stroke in older Chinese adults: in CHARLS (13,917 adults, 1,060 strokes) high county-level PM$_{2.5}$ carried HR 1.25 (1.04--1.51), household solid fuel HR 1.38 (1.18--1.62), with a multiplicative interaction (p=0.022).}\\[1.4mm]
\footnotesize
Ambient exposure is one pre-baseline year of the CHAP satellite-fused product averaged to county; solid fuel is a single questionnaire item. The ordinal joint-exposure score gives HR 1.10 (1.05--1.15) per step.
\textbf{Where it is weak:} the PM$_{2.5}$ contrast is categorical with no cut-point or per-$\mu$g/m$^3$ estimate in the abstract; every resident of a county shares one value; no household PM was measured, so the ``joint'' category combines an ecological and a proxy exposure.
\textbf{Why it matters here:} the interaction is the kind of claim paired indoor--outdoor low-cost nodes could test directly at the household, which neither exposure layer in this cohort can."""

CHANGED = [
r"""\textbf{A Sunday floor.} Five records from sixteen screened, three bands occupied (exposure assessment 2, sensing 2, cardiovascular 1), no tier-A record. Eighteen Europe PMC hits for 8 November had already been assigned to 6--7 November in the cross-day candidate set.""",
r"""\textbf{Personal sensors inside an intervention design.} URBANOME ran wearable and ambient monitoring, agent-based exposure modelling, spirometry, HRV and omics before and after co-created mobility, greening and traffic-calming interventions in nine European urban living labs. The abstract gives direction only (annoyance, sleep-breathing complaints down; FVC gradient attenuated) and a metabolite panel at AUROC $\approx$1.0 that the authors themselves call overoptimistic. No control arm.""",
r"""\textbf{Two sensing items for quality control and toxicity.} A labelled smart-home indoor air-quality dataset with experimentally induced contextual anomalies (Norway), useful for fault detection on unattended nodes if a PM channel is present --- the abstract does not list channels. A review of automated field-deployable cell-exposure platforms maps hardware for toxicity-weighted sensing, without performance data.""",
r"""\textbf{Exposure basis (x1).} Of 5 records, 1 rests on a low-cost sensor class (the smart-home dataset, sensing side) and 1 on personal/wearable monitoring (URBANOME). The single health-side record (stroke) is \emph{modelled} (satellite-fused, county mean); no health estimate today is tied to a measured exposure.""",
]

CONT = r"""The 5 November issue closed with \texttt{last\_entry\_date} at 5 November. This issue was built on the \textbf{10 November 22:16 UTC (16:16 CST) run}, the 05:00 UTC slot firing 17 hours late; no run executed on 7--9 November. Before 22:00 the newest buildable day is 9 November, so this run \textbf{backfills 6, 7, 8 and 9 November as four issues} and builds the \textbf{W45 weekly (1--7 November)}, owed since Saturday. Sunday 8 November opens W46. A cross-day candidate set was built before authoring and each record assigned to its earliest day. No \textsc{backfill} records this issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 5 records across three of ten bands: exposure assessment 2, sensing 2, cardiovascular and metabolic 1. Seven bands are empty, as expected on a Sunday entry day.""",
"f2_design_endpoint": r"""Left --- architecture: one each of cohort, non-randomised intervention field study, review, data descriptor and metadata-only record. Right --- every endpoint is a singleton; only incident stroke is a clinical outcome.""",
"f3_metric_geography": r"""Left --- particle metric as recorded per record; three records carry no single PM metric (review, data descriptor, metadata-only). Right --- geography: China 1 (CHARLS), Brazil 1 (S\~ao Paulo State), one multi-region review and two European records (nine-city URBANOME; Norway).""",
"f6_lifecourse": r"""Life-course windows. Working age carries CHARLS (enrolment from 45 years) and URBANOME adults; older adults the CHARLS stroke cohort (mean age 58.9). No preconception, in-utero, childhood or adolescent record today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture, five occupied cells, each with one record: the cohort sits in cardiovascular; exposure assessment holds the intervention study and the metadata-only record; sensing holds the review and the data descriptor.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, 3 hazard ratios from one source (Liu, CHARLS, n=13,917): high vs low county PM$_{2.5}$, solid fuel vs clean fuel, and the per-step trend of the ordinal joint score. All three are categorical contrasts in the same sample and are not independent; no pooling and no I$^2$.}\end{minipage}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{8 November 2026}, single day (Sunday). Harvester legs: \textbf{PubMed} health \textbf{18}, sensing \textbf{2}; \textbf{Europe PMC} \textbf{27}; \textbf{Crossref by ISSN} \textbf{3}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 429 on the harvester leg. PubMed connector (EDAT 6--9 November, health, instrumentation and broad MeSH axes) 69 PMIDs, \textbf{4 bucketed to 8 November, 2 appended}. The cross-day candidate set removed \textbf{18} records already assigned to 6--7 November (mostly Europe PMC re-surfacing), leaving \textbf{16 screened}. Abstracts: efetch filled 4 of 5 PMID records; Crossref title lookup recovered one EHP abstract; the APR deposit stayed empty.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run; no Amass backfill this run. Affiliations from PubMed XML.
\textbf{5 admitted} (all window), \textbf{11 rejected} with logged reasons. \textbf{1 carried on metadata alone}. \textbf{Trial watch}: see the W45 weekly.
Abstracts remain the copyright of their publishers."""
