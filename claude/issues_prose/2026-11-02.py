# -*- coding: utf-8 -*-
HEAD = dict(long="2 November 2026", window="2 November 2026 (full day)", n=19, excl=57,
            bands=8, eff=4, tierA=2, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Toronto: the published four-station community AQHI missed other city sites by more than 2 AQHI units in both directions, across eight continuous sites in six weeks.}\\[1.4mm]
\footnotesize
SWAPIT, January--March 2024. NO$_2$ dominated short-term AQHI risk and rose under calm winds; O$_3$ rose with wind speed; PM$_{2.5}$ carried both local and regional features. Against the NAPS record from 1997, median AQHI has fallen almost twice as fast in summer as in winter, leaving winter higher since 2013.
\textbf{Where it is weak:} one six-week winter at eight sites, no CI, and the abstract gives neither instrument class nor site typology, so the deviation cannot be split into siting and method.
\textbf{Why it matters here:} it puts a number on the gap between a sparse index and the intra-urban field. NO$_2$ rather than PM$_{2.5}$ drives the index here, so the sensor case rests on the multi-pollutant node, not on an optical PM node alone."""

CHANGED = [
r"""\textbf{Aged smoke is not fresh smoke.} Chamber aging raised ROS and oxidative DNA damage in BEAS-2B cells, most for smoldering emissions, while attenuating inflammatory signalling; cytotoxicity barely moved. No fold-changes in the abstract, and extracts on a submerged line, so dose relevance is open.""",
r"""\textbf{Low-cost optical sensors meeting vape aerosol, twice.} AirBeam3 in a bar: PM$_{2.5}$ mean 28.8, peak 84.7\,$\mu$g\,m$^{-3}$ (pilot, no reference). Vendor-led school deployment, 37 sites, 18 months: over 300 incidents, no confusion matrix, alert fatigue and a smoke false positive reported. \textsc{backfill} for the second, entry 4 May.""",
r"""\textbf{Inductive ferrous-aerosol sensing.} Micro-3D-printed impactor with liquid-metal coils: cut-offs 5.28 and 0.99\,$\mu$m, nRMSE 6.72--8.95\,\%. Laboratory aerosol only; no humidity, drift or unit-to-unit data.""",
r"""\textbf{Hygroscopicity shifts with chemistry.} CMAQ, US summers 2013--2022: isoprene organosulfates move $\kappa$ by $-$5.6\,\% net. A spatially structured term that a single humidity correction cannot carry.""",
r"""\textbf{Joint burden accounting.} 825 European cities: 213,889 deaths (89,224--344,223) jointly attributable to PM$_{2.5}$ and NO$_2$ in 2018, about a quarter below the sum of the single-pollutant figures. Abstract states a 76,833 gap; its printed numbers give 75,504. \textsc{backfill}, Crossref 26 October.""",
r"""\textbf{Reproductive signals on thin exposure.} PMOS PR 1.22 (1.09--1.35) per SD PM$_{2.5}$, IDW from three stations; offspring hernia or hydrocele OR 1.07 (1.01--1.14) per $\mu$g\,m$^{-3}$, 53 events (\textsc{backfill}, entry 4 May); a pregnancy-loss classifier with AUC 0.935 on internal validation only. All three are hypothesis-grade.""",
r"""\textbf{Exposure basis (x1).} Of 19 records, 2 rest on low-cost sensors (AirBeam3 bar pilot; school vape nodes), neither with a reference co-location in the abstract, and 4 on reference monitors. Health side with a recoverable basis (n=8): 50\,\% measured, 25\,\% modelled, 25\,\% proxy, but the measured share includes two station-interpolated residential estimates (three-station IDW; kriging), not personal measurement.""",
]

CONT = r"""The 1 November issue closed with \texttt{last\_entry\_date} at 1 November. This issue was built on the \textbf{4 November 00:2x UTC (3 November 18:2x CST) run}; the run fired 19 hours after its 2 November 23:04 CST slot, and before 22:00 local, so 3 November is not opened and is left to the next run. It covers \textbf{2 November in full}. Three \textsc{backfill} records are carried, the working cap, all marked with entry or deposit date. No rollup is owed: W45 (1--7 November) falls on Saturday 7 November."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 19 records across eight bands: exposure assessment seven, reproductive three, occupational and indoor three, sensing two, and one each mechanistic, neuro, burden and other clinical. Cardiovascular and respiratory are empty today.""",
"f2_design_endpoint": r"""Left --- architecture: measurement campaign five, metadata-only three, then two each cohort, cross-sectional, modelling and review, one each experimental, chamber or laboratory and ecological. Right --- endpoints are near-singletons, as expected on a day led by exposure records.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 7, unspeciated 6, PM$_{2.5}$+PM$_{10}$ jointly 3, and one each PM$_{10}$-only, composition and size-resolved. Right --- geography: Europe 4, global/multi-region 4 (two reviews, two with no site stated), East Asia ex-China 3, then China, North America and Southeast Asia 2 each, Oceania and Middle East 1 each.""",
"f6_lifecourse": r"""Life-course windows: two in utero or preconception (hernia cohort, pregnancy-loss model), one adolescent (school vaping sensors), three working-age (welders, occupational review, PMOS). No childhood or older-adult record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment spreads across measurement, modelling and metadata-only; three of its seven records are metadata-only or discussion. Sensing sits in measurement and laboratory cells only, with no co-location design today.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, four estimates from three studies. Increments differ (per SD with undisclosed width in Arak; per 1\,$\mu$g\,m$^{-3}$ in Korea; a job-role contrast for welders), and the two Arak estimates come from the same 301 women: nothing here is comparable across studies or poolable. The Korean carcinogen-emission RR is not a PM estimate and is not drawn.}\end{minipage}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{2 November 2026}, single day (Monday). Harvester legs: \textbf{PubMed} health \textbf{9}, sensing \textbf{2}; \textbf{Europe PMC} \textbf{9}, no AGRICOLA records; \textbf{Crossref by ISSN} \textbf{54}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} 0 returned (the OpenAlex connector is not on this session). 69 unique, 1 already carried, 68 fresh; PubMed connector (EDAT 2 Nov, three axes) 16 PMIDs plus one Amass check, 4 appended (\textbf{72 screened}). Abstracts: 10 recovered by efetch; Elsevier day-0 deposits remain empty. \textbf{Amass} BiomedCore (ingest date filter) surfaced \textbf{3 backfill} records admitted (two from Amass, one already held from 1 November), 1 rejected and 1 held. \textbf{Consensus} calibration sweep: 10 hits, 0 new.
bioRxiv/medRxiv and alphaXiv connectors are not on this session. \textbf{Scite} retraction check unavailable (connector requires a paid plan); Amass reports no retraction on the PMID-bearing backfills. \textbf{Wiley Scholar Gateway} not on this session.
\textbf{19 admitted} (16 window, 3 backfill), \textbf{57 rejected} with logged reasons. \textbf{Trial watch} 2--4 November: ClinicalTrials.gov 1, NCT07914010 (REACT, UC Berkeley: PurpleAir indoor monitors with the indicator light randomised on or off, 100 households, co-primary indoor PM$_{2.5}$ and BCSS/ACT); Amass TrialCore 20 returned, 2 relevant (ACTRN12626001238369, Melbourne HEPA RCT in COPD, n=200; ChiCTR2600134305). \textbf{3 carried on metadata alone}.
Abstracts remain the copyright of their publishers."""
