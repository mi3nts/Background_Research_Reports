# -*- coding: utf-8 -*-
HEAD = dict(long="7 October 2026", window="7 October 2026 (full day)", n=14, excl=61,
            bands=7, eff=2, tierA=4, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Congestion pricing cut PM$_{2.5}$ by
1.44\,$\mu$g\,m$^{-3}$ inside the zone --- and the same day, a national analysis shows that averaging
that kind of contrast away is how disparities disappear.}\\[1.4mm]
\footnotesize
New York's Central Business District Tolling Program began in January 2025. Against 2022--2024, a
difference-in-differences on NYCCAS real-time monitors attributes a \textbf{1.44\,$\mu$g\,m$^{-3}$}
PM$_{2.5}$ reduction inside the congestion relief zone ($p<0.001$; \textbf{1.33} allowing for spillover),
while nearby non-zone sites rose a non-significant 0.50. Tropospheric NO$_2$ fell over 20\,\% across metro
New York, but only \textbf{1.23\,\%} of that is attributable to the programme ($p$ = 0.096).
Alongside it, block-level US emission intensities: medium- and heavy-duty trucks are under \textbf{11\,\%}
of vehicle kilometres but \textbf{46\,\%} of NO$_x$ and \textbf{50\,\%} of PM$_{2.5}$ emission burden;
people of colour face burdens \textbf{40\,\%} above the national mean, and significant disparities appear
in \textbf{85--89\,\%} of counties, rural as much as urban. The finding that matters most is methodological:
\textbf{spatial aggregation substantially attenuates the measured disparity}.
\textbf{Why it matters for sensing:} both results are about resolution. A 1.4\,$\mu$g\,m$^{-3}$ step across
a few square kilometres, and an equity gap that shrinks as you coarsen the grid, are the two clearest
arguments yet in this series that network density is not a refinement --- it decides what is visible."""

CHANGED = [
r"""\textbf{Black carbon, at lag0, across 212 million outpatient records.} 274 Chinese cities, 2013--2017:
BC carried the strongest independent constituent associations, per IQR (1.8\,$\mu$g\,m$^{-3}$) ranging from
\textbf{+1.33\,\%} (0.93--1.74) for chronic kidney disease to \textbf{+3.89\,\%} (3.30--4.49) for COPD, and
at \textit{lag0} rather than the lag0--1 typical of admissions. Outpatient visits are supply-sensitive, so
a same-day signal may partly be care-seeking on visibly bad days.""",
r"""\textbf{Rural exposure misclassification, visible in the estimate.} 592 rural Californian children: an
IQR (38 days) increase in prior-year days above 50\,$\mu$g\,m$^{-3}$ PM$_{10}$ gave \textbf{+1.1\,mmHg} DBP
(0.8--1.5) and +0.9 SBP (0.3--1.5), with 5.8--5.9 percentage points higher risk of elevated SBP in the top
short-term quartile. Exposure came from regulatory monitors that can be tens of kilometres away in a
region whose sources are agricultural and local.""",
r"""\textbf{A network paper with no calibration.} A ZigBee mesh of low-cost CO and PM$_{2.5}$ nodes in
Calabar reports mean PM$_{2.5}$ of 40\,$\mu$g\,m$^{-3}$, AQI 112.5 and a self-defined
``performance index'' of 76.5\,\% --- with no co-location, no reference comparison and no humidity
correction reported. West Africa's data gap is real; this does not close it.""",
r"""\textbf{A null worth having.} PRISm in 2,275 Kazakh adults: prevalence \textbf{12\,\%} (10.7--13.3),
higher in women, and \textit{no} association with lifetime occupational vapour, gas, dust and fume exposure
by job-exposure matrix --- in a heavily industrial country. A European-derived JEM applied to Kazakh work
histories is exactly the instrument that would null out a real effect.""",
]

CONT = r"""The 6 October issue closed with \texttt{last\_entry\_date} at 6 October. This issue collects
\textbf{7 October in full}, continuous with it. Unlike the 3--6 October issues, this day was
\textbf{harvested and screened fresh on this run} --- the cached backfill ended at 6 October. The 8 October
daily and the W40 weekly (27 September--3 October) remain owed and follow."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 14 in-scope records. \textbf{Seven of ten bands populated};
\textit{Mechanistic toxicology} leads with \textbf{four} (three of them metadata-only or review),
\textit{Burden} three --- and those three carry three of the day's four tier-A records --- then two each
for \textit{Neuro} and \textit{Exposure assessment}, and one each for \textit{Cardiovascular},
\textit{Occupational} and \textit{Sensing}.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{five} metadata-only deposits, two cohorts (the
children's blood-pressure study and the ABCD imaging analysis), and one each for the ecological
policy evaluation, the national inventory, the acute case-crossover, the cross-sectional spirometry
survey, the chamber work, the toxicology experiment and the review. Right --- the health endpoints are
unusually spread: blood pressure, brain structure, outpatient visits, spirometry and the in-vitro
endpoints each appear once.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{eight}, unspeciated PM or
emissions three, composition/speciation two (the black-carbon constituent analysis and the manganese
biomarker deposit) and PM$_{2.5}$ + PM$_{10}$ jointly one. Right --- geography: North America
\textbf{five}, the most of any issue in this backfill, global / not stated four, Sub-Saharan Africa two
(Calabar and the Ethiopian eruption), and one each for China, Central Asia and East Asia excluding
China.""",
"f6_lifecourse": r"""Life-course windows: childhood one (rural Californian blood pressure), adolescence one
(the ABCD imaging cohort --- the first adolescence-specific record since 26 September), working age one
(the PRISm survey). In utero and older adults have no record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 14 records. The metadata-only block spans
mechanistic toxicology, neuro and exposure assessment; burden holds three different architectures
(ecological, inventory, acute) and no two records in it share a design --- which is why the three agree
only in direction.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Two relative risks with 95\,\% CIs, log scale, both per interquartile range (1.8\,$\mu$g\,m$^{-3}$)
of daily black carbon at lag0, from the same 274-city case-crossover --- COPD and chronic kidney disease,
the extremes of the twelve disease groups reported. They share an exposure series and are not independent.
The day's other quantitative results do not belong on a ratio scale: the New York policy effect is a
concentration difference ($-$1.44\,$\mu$g\,m$^{-3}$), the children's blood-pressure results are mean
differences in mmHg and percentage-point risk differences, and the emission-burden disparities are ratios
of emission intensity, not of risk.}"""

PROV = r"""Entry window \textbf{7 October 2026}, single day, continuous with the 6 October issue, and the
first day in this backfill harvested on the run that published it. Harvester legs run leg-by-leg:
\textbf{PubMed} health \textbf{9}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{20} (11 after the
AGRICOLA retro-index gate dropped 9); \textbf{Crossref by ISSN} \textbf{43}; \textbf{arXiv} answered
(148\,kB) with no entry dated 7 October; \textbf{OpenAlex} HTTP 429 --- the leg has now failed on every run
since 26 September and should be considered dead rather than degraded. 64 raw deduplicated to \textbf{62},
all fresh. The \textbf{PubMed connector} (\texttt{[EDAT]} 7--8 October, both axes as separate queries)
returned 23 PMIDs dated 7 October, of which 2 merged a PMID onto an existing DOI-only record and
\textbf{13} were appended --- \textbf{75} candidates screened, \textbf{14 admitted}, \textbf{61 rejected}
with logged reasons (water and soil chemistry, microplastics, wastewater, measurement-science and
remote-sensing engineering, and the usual broad-axis noise). \textbf{Five records carried on metadata
alone} (36\,\%), including the day's highest-relevance record (\textit{Part.\ Fibre Toxicol.}, measured
lung black-carbon deposition). The abstract-retry leg recovered \textbf{6 of 11} attempted.
\textbf{Consensus} returned 10 calibration hits, \textbf{0 new}. \textbf{Scholar Gateway} fails with
\texttt{ACCESS\_DENIED}. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain the copyright of their
respective publishers."""
