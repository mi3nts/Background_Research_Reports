# -*- coding: utf-8 -*-
HEAD = dict(long="24 October 2026", window="24 October 2026 (full day)", n=10, excl=67,
            bands=4, eff=2, tierA=1, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}65.2 million Medicare beneficiaries: the long-term PM$_{2.5}$--CVD
slope is halved in ZIP-years that had wildfire smoke waves.}\\[1.4mm]
\footnotesize
A national ZIP-year cohort (2017--2022) with 1\,km total PM$_{2.5}$ and 10\,km smoke PM$_{2.5}$ from machine-learning
models; a smoke wave is $\geq$2 consecutive days with smoke PM$_{2.5}$ $>$10\,$\mu$g\,m$^{-3}$. Raising the two-year mean
from 5 to 9\,$\mu$g\,m$^{-3}$: overall CVD first hospitalisation RR \textbf{1.09} (1.09--1.10) without smoke waves,
\textbf{1.04} (1.03--1.04) with them; ratio of RRs 1.05 (1.04--1.06). The gap persists below 9\,$\mu$g\,m$^{-3}$ and is
largest in men, urban and western residents.
\textbf{Where it is weak:} episodic spikes inflate a two-year mean without a proportional rise in risk, so the
attenuation is partly a property of the exposure metric, not of smoke toxicity; ZIP assignment and a 10\,km smoke grid
blur the contrast further.
\textbf{Why it matters here:} the long-term mean cannot represent a peaked exposure distribution. Peak-resolved,
high-frequency network data are the input this kind of model lacks."""

CHANGED = [
r"""\textbf{Wildfire PM toxicology is mostly not wildfire PM.} Systematic review of 46 studies (2005--2025): only 42\,\%
of in-vitro and 27\,\% of in-vivo studies used particles collected during real fires; no chronic or toxicokinetic work
and no mixtures with urban PM.""",
r"""\textbf{Brown carbon toxicity tracks lipophilicity.} 350\,$^\circ$C wood-pyrolysis BrC, 776--1,132 molecular
features per extract: A549 cytotoxicity rose water $<$ methanol $<$ acetone; methoxyphenols, quinols and
coniferylaldehyde named as contributors.""",
r"""\textbf{Cordwood stove trade-off (metadata only).} Automated forced-air injection lowers PM$_{2.5}$ mass but shifts
emissions to smaller particles --- the regime where optical mass sensors overstate the gain.""",
r"""\textbf{Five cross-day duplicates moved to 23 October.} Records harvested again in the 24 October window (EPMC
re-surfacings of 23 October PubMed entries) were assigned to the earlier issue; one smoke--dementia preprint had
already shipped on 12 October and was blocked by the DOI gate.""",
r"""\textbf{Saturday floor.} PubMed returned 2 records; Europe PMC (40) and the Crossref ISSN sweep (33) carried a thin
window, and 3 of 10 admitted records have no abstract anywhere.""",
]

CONT = r"""The 23 October issue closes the window through 23 October. This issue collects \textbf{24 October in full},
continuous with it. It was built on the \textbf{30 October 2026 recovery run} (14:20 UTC (09:20 CDT)), which backfilled
23--29 October day by day after the scheduled runs of 24--29 October did not complete; a 30 October 00:21 UTC run had
harvested 23--28 October but stopped before screening. 24 October is a Saturday: the \textbf{W43 weekly (18--24
October)} is filed under this date as a separate report."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 10 in-scope records across four bands. Mechanistic toxicology leads with
four (wildfire-PM review, brown-carbon cytotoxicity, gut microbiota, rat lung); exposure assessment three (all
metadata-only); cardiovascular two; respiratory one. Sensing is empty today.""",
"f2_design_endpoint": r"""Left --- architecture: two animal studies, one in-vitro, one systematic review, one
narrative review, one nationwide cohort, one ecological analysis; \textbf{metadata-only 3 (30\,\%)}. Right ---
endpoints: CVD hospitalisation, heart failure, subglottic stenosis prevalence and in-vitro/in-vivo toxicity markers.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only dominates; dust/smoke aerosol and stove emissions
are unspeciated. Right --- geography: North America 2 (Medicare; iSGS), global 2 (reviews), East Asia, Argentina and
China one each; the rest are laboratory or not stated.""",
"f6_lifecourse": r"""Life-course windows: two older-adult records (smoke-wave CVD; heart-failure exposome) and one
working-age ecological record (iSGS in women). No in-utero, childhood or adolescent record today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Toxicology sits in animal, in-vitro and review cells; the two
cardiovascular records split between a cohort and a narrative review; the exposure band is entirely metadata-only.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, two estimates from one study: overall CVD first-hospitalisation RR for a two-year PM$_{2.5}$
increase from 5 to 9\,$\mu$g\,m$^{-3}$ in Medicare ZIP-years without and with wildfire smoke waves. Same cohort,
stratified --- the contrast, not either estimate, is the finding.}\end{minipage}"""

PROV = r"""Entry window \textbf{24 October 2026}, single day (Saturday). Harvester legs: \textbf{PubMed} health
\textbf{2}, sensing \textbf{0}; \textbf{Europe PMC} \textbf{40} (4 AGRICOLA retro-index dropped); \textbf{Crossref by
ISSN} \textbf{33}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. PubMed connector (EDAT
24 Oct) 11 PMIDs, 8 appended; \textbf{77 screened}. Abstracts for 4 records recovered via Crossref/Semantic Scholar
title match. \textbf{10 admitted}, \textbf{67 rejected} with logged reasons, including 5 cross-day duplicates assigned
to 23 October and 1 DUPLICATE-DOI (shipped 12 October). \textbf{DOI gate} 0 fail / 0 warn after removal.
\textbf{3 carried on metadata alone}. Consensus sweep and trial watch for the 23--29 October backfill are reported in
the 29 October issue and the W43 weekly. \textbf{Scholar Gateway} not called. Abstracts remain the copyright of their
publishers."""
