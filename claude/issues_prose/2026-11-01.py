# -*- coding: utf-8 -*-
HEAD = dict(long="1 November 2026", window="1 November 2026 (full day)", n=7, excl=10,
            bands=6, eff=6, tierA=1, meta=2)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}China, 466,543 kidney deaths: coarse PM$_{2.5\text{--}10}$ per IQR (OR 1.024,
1.016--1.032) is comparable to PM$_{2.5}$ (OR 1.020, 1.012--1.027), with renal failure the most affected subtype.}\\[1.4mm]
\footnotesize
Nationwide time-stratified case-crossover, 2013--2019, modelled daily concentrations at the residential address. NO$_2$ was the
strongest of the four pollutants per IQR (+3.62\,\%, 2.47--4.78); renal-failure and glomerular deaths responded to all four,
tubulointerstitial to O$_3$ only, urolithiasis to none.
\textbf{Where it is weak:} the abstract gives no IQR widths, so the pollutant ranking is not per unit mass; lags differ by pollutant;
renal failure on a death certificate is often a proximate cause.
\textbf{Why it matters here:} a coarse-mode association this size sits in the size range where low-cost optical nodes are least reliable."""

CHANGED = [
r"""\textbf{Accra schoolchildren: no pro-hypertensive signal.} 919 children, home PM$_{2.5}$ SBP $-$0.70\,mmHg ($-$3.34 to 1.94) per 10 units, in a
city at 5--8 times the WHO annual guideline. Inverse point estimates suggest confounding. LUR built on a 146-site campaign. \textsc{backfill}, entry 4 June.""",
r"""\textbf{Low-level mortality gradient shrinks under geography.} Native American Medicare beneficiaries OR 1.12 (1.06--1.18) per $\mu$g\,m$^{-3}$ vs
1.01 (1.001--1.02); most attenuation came from state-level clustering. \textsc{backfill}, entry 4 May.""",
r"""\textbf{SPIROMICS proteomics.} 860 plasma proteins at FDR$<$0.05 for prior-year PM$_{2.5}$, none for NO$_2$ (n$\approx$1,620, congress abstract, no effect
sizes). \textsc{backfill}, Crossref deposit 29 October.""",
r"""\textbf{Ferrimagnetic nanoparticles in children's brains.} Mexico City autopsy tissue, 12 children and 16 adults; presence and field-driven motion shown,
no comparison group, no effect size.""",
r"""\textbf{Sunday floor.} PubMed entered 5 candidate records; the day's Crossref yield was Elsevier deposits without abstracts. Two records ride on metadata
alone (German sick-leave claims, personal air purifier); retry the \textit{Environ Int} abstract first.""",
r"""\textbf{Exposure basis (x1).} Of the four health records with a recoverable basis, three are modelled (national grid, LUR, prior-year surface) and one is a laboratory tissue assay: nothing measured on a person and no low-cost-sensor record today."""
,
]

CONT = r"""The 31 October issue closed with \texttt{last\_entry\_date} at 31 October. This issue was built on the \textbf{2 November 05:0x UTC (1 November 23:0x CST)
run}; the 22:00 rule is satisfied, so 1 November is complete. It covers \textbf{1 November in full} (Sunday, first day of standard time). One record (Calder\'on-Garcidue\~nas,
EDAT 31 October) surfaced only on Europe PMC's 1 November leg and was not screened on 31 October, so it is assigned here. Three \textsc{backfill} records are carried, the working
cap, all marked with their entry dates. No rollup is owed: W45 (1--7 November) falls on Saturday 7 November."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 7 records across six bands: burden and policy two (sick leave, Medicare mortality); respiratory,
cardiovascular, neuro, occupational \& indoor and other clinical one each. Mechanistic, reproductive, exposure and sensing bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: observational cross-sectional three (Accra, Medicare case-control, SPIROMICS baseline), metadata-only two, and one each
acute case-crossover and laboratory (autopsy tissue). Right --- endpoints from kidney mortality and blood pressure to the plasma proteome and sick leave.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 4, unspeciated 3. Right --- geography: North America 2, then one each Sub-Saharan Africa, Europe, Latin
America and China; the personal-purifier record states no site and is drawn under global/multi-region.""",
"f6_lifecourse": r"""Life-course windows: two childhood records (Accra blood pressure, Mexico City brain tissue), one working-age (sick leave, metadata only) and one
older-adult (Medicare mortality). No in-utero or separate adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Seven records occupy seven cells; no cell has a replicate today, so this is a map of what arrived, not a
pattern.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, five estimates from three studies. Increments differ (per IQR with undisclosed widths in China; per 1\,$\mu$g\,m$^{-3}$ in Medicare; per 10
units in Accra) and the Medicare slope is a low-decile contrast: nothing here is comparable across studies or poolable.}\end{minipage}

\vspace{2mm}
\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale, one estimate: systolic blood pressure per 10 units of home PM$_{2.5}$, Accra schoolchildren (n=919), an inverse point estimate with a CI spanning zero.}\end{minipage}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{1 November 2026}, single day (Sunday). Harvester legs: \textbf{PubMed} health \textbf{0}, sensing \textbf{1}; \textbf{Europe PMC}
\textbf{9} after dropping 2 AGRICOLA retro-index records; \textbf{Crossref by ISSN} \textbf{6}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429 (the OpenAlex connector
is not on this session). 14 unique, 6 already carried, 8 fresh; PubMed connector (EDAT 1 Nov, three axes) 5 PMIDs, 1 seen, 4 appended (\textbf{12 screened}). Abstracts: 4 recovered by efetch; Elsevier
day-0 deposits remain empty. \textbf{Amass} BiomedCore (ingest date filter) surfaced \textbf{3 backfill} records admitted and 2 rejected; others held. \textbf{Consensus} calibration sweep: 10 hits, 0 new (Fang 2026 already shipped; Feng 2026 review already rejected).
\textbf{medRxiv} toolbox leg: no keyword filter, no PM record. bioRxiv/medRxiv and alphaXiv connectors are not on this session. \textbf{Scite} retraction check unavailable (connector requires a paid plan); Amass reports no retraction on PMID-bearing backfills. \textbf{Wiley Scholar Gateway} not called (needs re-authorisation).
\textbf{7 admitted} (4 window, 3 backfill), \textbf{10 rejected} with logged reasons. \textbf{Trial watch} 1--2 November: ClinicalTrials.gov 0; Amass TrialCore 10 returned, one relevant (NCT07311967, UIC cooking UFP chamber, not previously logged). \textbf{2 carried on metadata alone}.
Abstracts remain the copyright of their publishers."""
