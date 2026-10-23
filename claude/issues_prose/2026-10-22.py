# -*- coding: utf-8 -*-
HEAD = dict(long="22 October 2026", window="22 October 2026 (full day)", n=17, excl=38,
            bands=8, eff=6, tierA=4, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Denmark, 53,901 people: the ADHD signal sits in the second year of
life, it follows elemental carbon rather than PM$_{2.5}$ mass, and it is larger in girls.}\\[1.4mm]
\footnotesize
A national case-cohort (21,860 diagnosed cases, 32,041 subcohort; births 1981--2008) with daily address-level PM$_{2.5}$
and EC from pre-conception to age 12 (DEHM/UBM/AirGIS). Each period was adjusted for the others. Second year of life,
EC $>$1.13 vs $<$0.49\,$\mu$g\,m$^{-3}$: HR \textbf{1.24} (1.12--1.36), unchanged after PM$_{2.5}$ adjustment;
girls \textbf{1.44} (1.21--1.72), boys 1.18 (1.00--1.40). Models adjust for ADHD polygenic scores.
\textbf{Where it is weak:} exposures at one address in consecutive years are close to collinear, so a ``window''
found by mutual adjustment is sensitive to differential error between periods. ADHD diagnosis in girls carries
referral bias that tracks urbanicity.
\textbf{Why it matters here:} the combustion tracer, not total mass, carries the effect. A mass-only optical network
cannot see this contrast; an absorption (BC) channel can."""

CHANGED = [
r"""\textbf{HAPIN null extends to age 5.} LPG stove plus fuel cut infant PM$_{2.5}$ from 113 to 37\,$\mu$g\,m$^{-3}$,
but HAZ $\beta$ $-$0.06 ($-$0.16 to 0.03) across 2,169 children and no stunting effect; post-trial exposures
converged ($\approx$99\,$\mu$g\,m$^{-3}$ both arms). Preprint.""",
r"""\textbf{Blocked cross-validation as interpolation.} GEOS-CF PM$_{2.5}$ emulator, Arabian Peninsula: a Random
Forest on latitude/longitude alone (R$^2$ 0.91) beat the 13-predictor model (0.82--0.84). Skill vanished with a
300\,km buffer and on an unseen sector ($r$ 0.11).""",
r"""\textbf{CO$_2$-normalised traffic emission factors.} Helsinki street canyon: PM and NO$_x$ fleet factors well
above post-2014 Euro limits; traffic is a \emph{sink} for O$_3$ and sub-2\,nm ions (negative ``impact factors'').""",
r"""\textbf{Intermittent point source.} Gas-fired peaker plant, Massachusetts: respiratory ED/UC visits OR 1.044
(1.001--1.090) per unit of a unitless trajectory index; no cardiovascular signal.""",
r"""\textbf{Implausible per-microgram hazard.} Beijing elderly cohort ($n$\,=\,3,472): all-cause HR 1.053 per
1\,$\mu$g\,m$^{-3}$, an order of magnitude above pooled long-term estimates --- read as urban/rural confounding.""",
r"""\textbf{Europe PMC lag.} Europe PMC returned a single 22 October record (a medRxiv preprint); PubMed (21) and the
Crossref ISSN sweep (37) carried the issue.""",
]

CONT = r"""The 21 October issue closed with \texttt{last\_entry\_date} at 21 October. This issue collects
\textbf{22 October in full}, continuous with it. The scheduled 04:04 UTC run fired at 16:06 UTC on 23 October
(11:06 CDT), before the 22:00 cut-off, so 23 October is \emph{not} opened and is left to the next run at or after
22:00 CDT. The W43 weekly (18--24 October) is due Saturday 24 October."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 17 in-scope records across eight bands. Exposure assessment leads with
five (emission factors, emulation, soluble PM$_{10}$, a rainfall event, a microbiome method); respiratory three;
occupational/indoor and other clinical endpoints are empty.""",
"f2_design_endpoint": r"""Left --- architecture: four reviews, three measurement campaigns, two cohorts, two
modelling, two toxicology, one trial, one case-crossover, one ecological; \textbf{metadata-only 1 (6\,\%)}, a series
low. Right --- endpoints run from ADHD and child growth to mortality, ED visits, CRS, ILD and in-vitro cytotoxicity.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 9, unspeciated/emissions 4, joint
PM$_{2.5}$+PM$_{10}$ 2, PM$_{10}$ 1, nanoscale 1. Right --- geography: Europe 3 (Denmark, Finland, Spain) ties
China 3; global/multi-region 5 (mostly reviews); North America 2; one each for MENA, South Asia and Latin America.""",
"f6_lifecourse": r"""Life-course windows: childhood carries two records (ADHD second-year window; HAPIN growth to age
5), with HAPIN also in utero; three working-age records; one older-adult cohort (Beijing); no adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment is spread over measurement, modelling and
methods cells; the health bands sit in cohorts, the trial and reviews. Sensing has only the metadata-only
fluorescence record today.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, five estimates from three studies: second-year EC and ADHD (all, female) in the Danish
case-cohort; PM$_{2.5}$ per 1\,$\mu$g\,m$^{-3}$ and all-cause/CVD death in the Beijing elderly cohort; peaker-plant
index and respiratory ED/UC visits (OR per unitless index unit). Exposure contrasts differ completely. Not poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: HAPIN intention-to-treat effect of the LPG intervention on repeated height-for-age Z
score, ages 2--5 (n\,=\,2,169). The null is an ITT contrast for a partial exposure reduction.}\end{minipage}"""

PROV = r"""Entry window \textbf{22 October 2026}, single day (Thursday). Harvester legs: \textbf{PubMed} health
\textbf{21}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{1} (index lag); \textbf{Crossref by ISSN} \textbf{37};
\textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. 58 unique, 8 already carried, 50 fresh;
PubMed connector (EDAT 22 Oct) 25 PMIDs, 5 appended, \textbf{55 screened}. Abstracts for 9 PubMed records recovered
by efetch and for 6 more via Crossref/Semantic Scholar. \textbf{Consensus} calibration sweep: 10 hits, 0 new.
\textbf{17 admitted}, \textbf{38 rejected} with logged reasons. \textbf{DOI gate} 0 fail / 1 warn (CMA DOI live at
doi.org, not in Crossref). \textbf{Trial watch} 22--23 October: 2 registrations updated (APCIQ-BP HEPA purifier RCT
NCT05903950, AIRWEIGHS NCT02763917), both already tracked. \textbf{1 carried on metadata alone}. \textbf{Scholar
Gateway} not called. Abstracts remain the copyright of their publishers."""
