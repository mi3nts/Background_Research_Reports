# -*- coding: utf-8 -*-
HEAD = dict(long="12 November 2026", window="12 November 2026 (full day)", n=30, excl=76,
            bands=10, eff=4, tierA=3, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Two Sensirion modules, calibrated where they are used, held to $\le$22\,\% error against gravimetry indoors and out and $\le$15\,\% expanded uncertainty outdoors --- and stayed stable through repeated kitchen-smoke events above 1000\,$\mu$g/m$^3$, the manufacturer's ceiling.}\\[1.4mm]
\footnotesize
Arba Minch University and Lund University, \textit{Atmospheric Measurement Techniques}; SPS30 and SEN55 co-located indoors and outdoors in Arba Minch (Ethiopia) against gravimetry, plus a Swedish outdoor set against a Palas FIDAS for humidity. SEN55 read 6--10\,\% above SPS30; with that offset removed the two were interchangeable (CV $\le$7.7\,\%, between-sampler uncertainty $\le$1.7\,$\mu$g/m$^3$). SEN55 truncates digitally at 6553.4\,$\mu$g/m$^3$; readings between 1000 and that limit still carried mass information. The RH effect was small for both.
\textbf{Where it is weak:} the abstract gives neither the number of gravimetric samples nor the RH range, and ``calibrated under circumstances of use'' means the accuracy figures are post-calibration, not out of the box.
\textbf{Why it matters here:} the 11 November issue carried 923 Ethiopian kitchens measured on uncorrected PurpleAir units. This is the missing local calibration evidence for the same setting --- with a different sensor family."""

CHANGED = [
r"""\textbf{Network QA for smoke.} University of Washington: an entropy-based rule and a gradient-boosted classifier flag faulty PM$_{2.5}$ sensors across mixed-vendor North American networks during 11 smoke events (2024--2025), when real swings mimic faults. Faults were simulated, and the abstract gives no detection rates.""",
r"""\textbf{Ghana at 1\,km, validated on sensors.} Lamont--Doherty/Columbia: daily PM$_{2.5}$ 2005--2025 from XGBoost on monitors, satellite and reanalysis, evaluated against reference monitors and a calibrated low-cost network; the north--south gap widens by about 0.15\,$\mu$g/m$^3$ per year. A companion all-hour 5\,km AOD product for China falls from R\,=\,0.95 in cross-validation to 0.61 against MODIS.""",
r"""\textbf{A new short-term endpoint.} Beijing, 39,015 endometriosis outpatient visits: PM$_{2.5}$ lag 0--7 RR 1.109 (1.044--1.177), PM$_{10}$ lag 0--6 RR 1.070 (1.014--1.128), increments unstated; the additive interaction with heat ran through ozone, not PM. Indoor PM$_{10}$ and adolescent asthma in REPRO\_PL: OR 2.22 (0.88--5.57) on one 24-h sample in 172 homes.""",
r"""\textbf{Exhaust is no longer the truck problem.} Southern California: brake and tyre wear has dominated heavy-truck PM$_{2.5}$ emissions since 2022 and reaches 92\,\% by 2045 under the zero-emission rules. Separately, mice inhaling PM$_{2.5}$ at 5 or 35\,$\mu$g/m$^3$ for 180 days developed arterial stiffening and calcification --- an ambient-level dose, unusual in this literature.""",
]

X1NOTE = r"""\textbf{Exposure basis (x1).} XXX"""

CONT = r"""The 11 November issue closed the day before. This issue was built on the \textbf{16 November 05:40 UTC (23:40 CST 15 November) run}. After 22:00 CST the newest buildable day is today, so this run owes \textbf{12, 13, 14 and 15 November as four issues plus the W46 weekly (8--14 November)}; \textbf{12 November is covered in full}. Thursday: no rollup is filed under this date. A cross-day pass assigned records resurfacing on 13--15 November to their earliest day. No \textsc{backfill} records today. OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session, and Scite was not run."""

CAPS = {
"f1_subtopics": r"""XXX""",
"f2_design_endpoint": r"""XXX""",
"f3_metric_geography": r"""XXX""",
"f6_lifecourse": r"""Life-course windows. Preconception/in utero is the Chinese provincial perinatal panel; childhood the KN95 donning study (6--13 years); adolescence the REPRO\_PL indoor-PM cohort; working age the Beijing endometriosis series, Frankfurt runners, Colombo office workers and the exercise network meta-analysis; older adults the Aberdeen cognition cohort and the brain-MRI review (65+).""",
"f4_heatmap": r"""XXX""",
}

FOREST = r"""XXX"""

PROV = r"""Entry window \textbf{12 November 2026}, single day (Thursday). Harvester legs: \textbf{PubMed} health \textbf{12}, sensing \textbf{4}; \textbf{Europe PMC} \textbf{45}; \textbf{Crossref by ISSN} \textbf{64}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 429 on the harvester leg. 125 raw, 118 unique, 16 already carried, 102 fresh. PubMed connector (EDAT 12--15 November, three axes) 53 PMIDs (\texttt{\_conn\_1116.py}), 16 bucketed to 12 November, 0 seen, 11 appended (113); the cross-day pass removed 7 previously rejected or seen records --- \textbf{106 screened}. Abstracts: efetch filled 21 of 22 PMID records; Crossref/Semantic Scholar recovered none of the remaining Crossref records.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run. No Amass or Consensus backfill this run.
\textbf{30 admitted}, \textbf{76 rejected} with logged reasons. \textbf{3 carried on metadata alone}. Affiliations from PubMed XML and Crossref (OpenAlex unavailable); blank where neither carries one. Trial watch: see W46 weekly.
Abstracts remain the copyright of their publishers."""
