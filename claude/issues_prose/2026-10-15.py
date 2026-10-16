# -*- coding: utf-8 -*-
HEAD = dict(long="15 October 2026", window="15 October 2026 (full day)", n=25, excl=85,
            bands=8, eff=4, tierA=5, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}AERONET's night-time lunar AOD now matches its daytime solar
AOD to within $\pm$0.01 at 440\,nm across 492 sites --- the column reference for AOD--PM$_{2.5}$ fusion no
longer stops at sunset.}\\[1.4mm]
\footnotesize
Model-T CIMEL radiometers have recorded direct-beam lunar irradiance at six wavelengths (440--1640\,nm) since
2014. With an updated empirical correction to the ROLO lunar irradiance model, day--night AOD differences at
every long-record site are typically \textbf{within $\pm$0.01} at 440\,nm and as good or better at longer
wavelengths; in 3\,h dusk/dawn transition windows under low, stable AOD, AOD, \AA ngstr\"om exponent, column water
vapour and SDA fine/coarse AOD differ negligibly.
\textbf{Where it is weak:} consistency is demonstrated only where AOD is low and stable --- smoke and dust nights,
the case that matters for exposure, are not tested, and lunar phase leaves recurring multi-day gaps.
\textbf{Why it matters here:} satellite AOD is daytime-only, so AOD-driven PM$_{2.5}$ surfaces interpolate the
night; a validated night column is a direct check on how ground LCS networks and models handle the nocturnal
boundary layer."""

CHANGED = [
r"""\textbf{Low-cost monitors in a transfer-learning exposure model.} Lima 2010--2023: reference and low-cost
monitors, MAIAC AOD and WRF-Chem fused by an instance-weighted random forest that borrows US training data by
geo-environmental similarity. CV R$^2$ \textbf{0.76}; mountain-district mean PM$_{2.5}$ fell from 34.2 to
29.2\,$\mu$g\,m$^{-3}$ --- a correction that the reported CV, run on the same biased sites, cannot verify.""",
r"""\textbf{Datacenter power as a PM$_{2.5}$ exposure.} Memphis preprint (Dominici group): on-site turbines
concentrate attributable deaths within 50\,km (82\,\%), grid supply scatters them $>$250\,km (94\,\%); at
real/permitted capacity, \textbf{11.35} (6.48--17.29) vs \textbf{8.10} (4.60--12.38) deaths/yr. A near-source
burden that a local network could test directly.""",
r"""\textbf{Two well-powered nulls.} MESA ($n$=5,072): no pollutant associated with suPAR, PM$_{2.5}$ CI
excluding $\geq$2\,\% per 5\,$\mu$g\,m$^{-3}$. UK Biobank women ($n$=231,525): the PM$_{2.5}$--NO$_2$
association with fatty-liver index vanishes after area deprivation (OR \textbf{0.999}, 0.993--1.004) --- with
the caveat that deprivation may sit on the pathway.""",
r"""\textbf{Constituents and windows.} Guangdong CHD registry (12,680 cases): per-IQR constituent increments
raised odds 9--16\,\%, strongest preconception; conotruncal ORs 1.14--1.36; sulfate and BC lead early, BC and
nitrate later. CIs absent from the abstract.""",
r"""\textbf{Non-exhaust metrology with explicit drift.} DLR tire-wear rig: chamber temperature raised CPC
response 3.6-fold (1.8--7.2), inflation pressure cut OPS number 18\,\% (12--24\,\%), and the reference-condition
CPC signal doubled over the campaign --- drift monitoring and randomised blocks are prerequisites.""",
]

CONT = r"""The 14 October issue closed with \texttt{last\_entry\_date} at 14 October. This issue collects
\textbf{15 October in full}, continuous with it. 16 October is not opened: this run began at 11:23 CDT on
16 October, before 22:00. The \textbf{W42 weekly} (11--17 October) is due with the Saturday 17 October issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 25 in-scope records across eight bands. Exposure assessment and
modelling leads (7), burden and policy follows (5); sensing (4) carries the AERONET lunar-AOD tier-A record.
Neuro and other-clinical bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: modelling/inventory and review each 5, metadata-only 5
(20\,\%, all Elsevier or Springer Nature deposits without abstracts at harvest). Right --- health endpoints:
CHD, arrhythmia, chronic respiratory disease, stroke burden, fatty liver, a biomarker null (suPAR).""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ dominates; optical (AOD) and size-resolved
number (tire-wear CPC/OPS) metrics appear on the sensing side. Right --- geography: China (5) and North America
(4) lead; Peru, Indonesia/Malaysia and Taiwan enter.""",
"f6_lifecourse": r"""Life-course windows: preconception/in utero (Guangdong CHD), school-age children
(inhaled dose), working age (creosote workers), and three older-adult samples (Guangdong $\geq$40, MESA, UK
Biobank women). No adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Review/synthesis spreads across burden, respiratory,
sensing and mechanism; the exposure row mixes modelling, laboratory and metadata-only records.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale: one estimate --- the UK Biobank fatty-liver OR per unit of a 2010 PM$_{2.5}$--NO$_2$ score
after area-deprivation adjustment, a null by construction of the adjustment set, not per unit concentration.}\end{minipage}

\vspace{2mm}
\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: population-attributable fractions (\%) of chronic respiratory disease for PM$_1$,
PM$_{2.5}$ and PM$_{10}$ from one cross-sectional Guangdong sample. All three come from the same 1\,km
satellite-ML product and are near-collinear --- one estimate drawn three times, causal only by assumption.}\end{minipage}"""

PROV = r"""Entry window \textbf{15 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{6},
sensing \textbf{3}; \textbf{Europe PMC} \textbf{46} (0 AGRICOLA retro-index); \textbf{Crossref by ISSN}
\textbf{78}; \textbf{arXiv} no entry dated 15 October; \textbf{OpenAlex} HTTP 429. 129 unique, 22 already
carried, 107 fresh. \textbf{PubMed connector} (EDAT 15 Oct) 7 PMIDs, 3 appended --- \textbf{110} candidates
screened, \textbf{25 admitted}, \textbf{85 rejected} with logged reasons. \textbf{Consensus} calibration sweep:
10 hits, \textbf{0 new} (Ginsburg 2026 and Kumpika 2026 already archived). \textbf{Trial watch}: 0 registrations
updated 15--16 October. Abstract retry recovered 7 of 12; \textbf{5 records carried on metadata alone}.
DOI gate 0 fail, 2 advisory warnings (Epidemiologia e Prevenzione DOIs resolve at doi.org but are absent from
Crossref). \textbf{Scholar Gateway} still \texttt{ACCESS\_DENIED}. Abstracts remain the copyright of their
publishers."""
