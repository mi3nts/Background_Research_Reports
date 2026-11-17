# -*- coding: utf-8 -*-
HEAD = dict(long="15 November 2026", window="15 November 2026 (full day)", n=4, excl=15,
            bands=3, eff=0, tierA=0, meta=2)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}China's 2026 PM$_{2.5}$ standard (GB 3095-2026, 35 to 25\,$\mu$g/m$^3$ annual) would, at full compliance in 2024, avert 4.3 times the deaths that compliance with the old limit would, lifting PM$_{2.5}$-specific progress toward the WHO 2040 halving target from 66.2\,\% to 83.4\,\%.}\\[1.4mm]
\footnotesize
Peking University, \textit{Environmental Science and Ecotechnology}; comparative risk assessment on gridded PM$_{2.5}$ and population, 2013--2024, cause-specific exposure--response functions. Gains concentrate in COPD, stroke, lung cancer, lower respiratory infection and IHD; dementia and type 2 diabetes barely move.
\textbf{Where it is weak:} a counterfactual, not an observed mortality change --- the 4.3$\times$ ratio is set by the shape of the exposure--response functions between 25 and 35\,$\mu$g/m$^3$, and the abstract gives neither absolute deaths nor uncertainty intervals.
\textbf{Why it matters here:} enforcement at 25\,$\mu$g/m$^3$ moves the regulatory margin into the range where uncorrected low-cost sensor bias (humidity, composition) is a large fraction of the exceedance being judged."""

CHANGED = [
r"""\textbf{Sunday floor.} Four records from 19 screened; 15 off topic (ozone climatology, heat, building physics, aquatic virology). Two of the four are Crossref deposits with no abstract.""",
r"""\textbf{Household fuel in East Africa.} GBD 2023 secondary analysis: stroke attributable to all risks 110,013 deaths in Eastern Sub-Saharan Africa in 2023; environmental risks 4,146 DALYs per 100,000 (2,621--5,668), household air pollution third among single risks, no significant decline since 1990. All model output; household and ambient PM are not separated in the abstract.""",
r"""\textbf{Particles mass sensors do not see.} Metadata-only deposits on airborne microplastics during northwest-China winter haze and on ultrafine particles in subway station offices under different ventilation modes --- both particle classes outside what Plantower-class optical mass sensors report.""",
r"""\textbf{Exposure basis (x1).} Both health-side records (the NAAQS risk assessment and the GBD stroke analysis) rest on modelled exposure; nothing today is measured and no record uses a low-cost sensor. No effect estimate with a CI was reported, so there is no forest plot.""",
]

CONT = r"""The 14 November issue closed the day before. This issue was built on the \textbf{16 November 05:40 UTC (23:40 CST 15 November) run}. After 22:00 CST the newest buildable day is today, so this run owes \textbf{12, 13, 14 and 15 November as four issues} plus the \textbf{W46 weekly (8--14 November, filed under Saturday 14 November)}; \textbf{15 November is covered in full}. Sunday: no rollup falls today; \textbf{W47 (15--21 November) is due on Saturday 21 November}. A cross-day pass assigned 12 records that resurfaced today to earlier issues. No \textsc{backfill} records today. OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session, and Scite was not run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the four records across three bands: burden, policy \& mitigation 2 (China NAAQS risk assessment, East African stroke burden), exposure assessment 1 (microplastics in haze, metadata only), occupational \& indoor 1 (subway-office ultrafines, metadata only).""",
"f2_design_endpoint": r"""Left --- architecture: two modelling records (the NAAQS comparative risk assessment and the GBD stroke analysis) and two metadata-only records. Right --- endpoints: the two metadata-only records, and one each for cause-specific attributable mortality and attributable stroke deaths and DALYs.""",
"f3_metric_geography": r"""Left --- particle metric as classified from the record fields: unspeciated PM 3 (the two metadata-only records and the GBD stroke analysis), PM$_{2.5}$ only 1 (the NAAQS assessment). Right --- geography: China 3 (one by author inference), sub-Saharan Africa 1.""",
"f6_lifecourse": r"""Life-course windows: working age carries the two burden analyses; older adults the stroke burden (55+ emphasis). No preconception, childhood or adolescent record today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture: burden, policy \& mitigation holds both modelling records; the exposure and occupational \& indoor rows are one metadata-only record each. No cohort, trial or measurement campaign today.""",
}

FOREST = ""

X1NOTE = ""

PROV = r"""Entry window \textbf{15 November 2026}, single day (Sunday). Harvester legs: \textbf{PubMed} health \textbf{7}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{16}; \textbf{Crossref by ISSN} \textbf{13}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 429 on the harvester leg. 37 raw, 31 unique, 1 already carried, 30 fresh. PubMed connector (EDAT 12--15 November, three axes) 53 PMIDs (\texttt{\_conn\_1116.py}), 2 bucketed to 15 November, 1 appended (31); cross-day dedupe moved 12 records to earlier issues --- \textbf{19 screened}. Abstracts: efetch filled 2 of 2 PMID records; Crossref/Semantic Scholar recovered none of the Crossref records tried.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run. No Amass or Consensus backfill this run.
\textbf{4 admitted}, \textbf{15 rejected} with logged reasons. \textbf{2 carried on metadata alone}. Affiliations from PubMed XML and Crossref (OpenAlex unavailable); blank where neither carries one. Trial watch: see W46 weekly.
Abstracts remain the copyright of their publishers."""
