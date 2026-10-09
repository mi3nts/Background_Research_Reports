# -*- coding: utf-8 -*-
HEAD = dict(long="4 October 2026", window="4 October 2026 (full day)", n=5, excl=8,
            bands=4, eff=0, tierA=1, meta=0)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A Saturday of five records, and the two strongest are both
about air-cleaning controls --- one measured properly, one not measured at all.}\\[1.4mm]
\footnotesize
Blackley and colleagues (\textit{Ann.\ Work Expo.\ Health}, tier A) evaluated five high-volume suction
systems during \textbf{51} real dental procedures, with direct-reading number and mass instruments (PM$_4$
respirable, PM$_{10}$ thoracic) beside the dentist and in the hallway. The estimand is the one that matters
and is almost never used: a system counts as effective only when the \textbf{95\,\% lower confidence limit
of the procedure-to-background ratio is $\le$1} --- that is, when the control returns the air to background
\textit{against the instrument's own noise}, not when it produces a quotable percentage reduction.
Against that, Rees and colleagues report the qualitative arm of \textbf{AFRI-c}, the care-home HEPA cluster
RCT that found \textbf{no reduction in respiratory infections}: units were accepted, maintenance was light,
cost was judged prohibitive sector-wide --- and \textbf{runtime, filter loading and achieved air-change
rate were never measured}. \textbf{Why it matters for sensing:} a filtration null without exposure
verification cannot distinguish ``filtration does not work'' from ``the filters were off''. One logging
low-cost node per room is the cheap repair to a trial design that otherwise cannot fail informatively."""

CHANGED = [
r"""\textbf{Road dust is a live microbial reservoir.} 16S metabarcoding of dust from nine sites in three
Philippine metros: alpha diversity does not differ between cities (Kruskal--Wallis $p>0.05$) but composition
does (PERMANOVA \textbf{R$^2$ = 0.466}, $p$ = 0.004), with \textit{Paracoccus} rising toward the most
metal-laden site and correlating with cobalt and nickel. Dust is a reservoir, not an exposure --- nothing
here measures what resuspends.""",
r"""\textbf{The atmospheric mycobiome by aircraft.} Seasonal flights joined to vegetation-productivity and
meteorological data find fungal diversity declining with altitude and with productivity, decomposers and
pathogens dominant, and \textbf{over 40\,\%} of taxa putative plant or animal pathogens. Amplicon relative
abundance is not concentration and viability is untested.""",
r"""\textbf{Review, not evidence.} A \textit{Carcinogenesis} narrative review maps early-onset lung-cancer
mechanisms --- mutational signatures, telomere and mitochondrial dysfunction, CXCL13/IL-1$\beta$
inflammation, PD-L1 and CD47--SIRP$\alpha$ immune evasion, microbiome disruption --- and calls single-study
biomarkers validated. Useful as a list of mediators a cohort with \textit{measured} personal exposure
could test.""",
]

CONT = r"""The 3 October issue closed with \texttt{last\_entry\_date} at 3 October. This issue collects
\textbf{4 October in full}, continuous with it. It is a Saturday, and the volume is a series low: 13 fresh
candidates, \textbf{5 admitted}. Harvest and screening were completed on the 6 October run and cached;
this run authored from that cache without re-querying. Dailies for 5--8 October and the W40 weekly
(27 September--3 October) remain owed and follow in this backfill."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 5 in-scope records. \textbf{Four of ten bands populated}:
\textit{Occupational \& indoor} two (both air-cleaning controls), and one each for \textit{Exposure
assessment}, \textit{Sensing} and \textit{Mechanistic toxicology}. No clinical-endpoint band is populated
--- the one cancer record is a mechanistic review, not a study of people.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{three} measurement campaigns (the dental
operatories, the road-dust survey and the aircraft bioaerosol flights) and \textbf{two} filed as review /
synthesis (the narrative review and the qualitative arm nested in the AFRI-c trial). Right --- \textbf{all
five} records report no measured health endpoint, including the HEPA record, whose trial endpoint lives in
the parent RCT and not in this paper.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM in the two intervention records,
PM$_{10}$ only in the dust survey (reported as a reservoir), bioaerosol in the aircraft campaign, and
PM$_{2.5}$ + PM$_{10}$ in the review. The dental study is the only record reporting a respirable (PM$_4$)
cut. Right --- geography: Europe two, and one each for North America, Southeast Asia and
global / multi-region.""",
"f6_lifecourse": r"""Life-course windows: working age two (dental providers, care-home staff) and older
adults one (care-home residents under HEPA filtration). No record addresses in utero, childhood or
adolescence --- a consequence of a day dominated by occupational and environmental-survey work.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 5 records. Measurement campaigns spread
across occupational, exposure and sensing; the two review-type records sit in occupational and mechanistic
toxicology. Every occupied cell holds a single record except occupational measurement.""",
}

FOREST = r"""{\fontsize{7.4}{9}\selectfont\color{Slate}\textbf{No forest plot this issue.} No admitted
abstract reports a PM effect estimate with a confidence interval. The dental study's estimand is a
procedure-to-background concentration ratio with a 95\,\% lower confidence limit, reported per system in
the full text rather than in the abstract; the AFRI-c qualitative arm reports no effect measure, and the
remaining three records report none. The f5 panel is absent by design, not by build failure.\par}"""

PROV = r"""Entry window \textbf{4 October 2026}, single day, continuous with the 3 October issue. Harvest
and screening for this day were completed on the \textbf{6 October} run and cached
(\texttt{cache/2026-10-04/\_fresh.json}); this run authored from that cache without re-querying.
\textbf{13} fresh candidates after cross-day deduplication --- a Saturday, and the lowest daily volume of
the series. \textbf{5 admitted}, \textbf{8 rejected} with logged reasons. \textbf{No record carried on
metadata alone}, the first such issue since 27 September: the Crossref-ISSN leg returned nothing dated
4 October, and Elsevier does not deposit at weekends. \textbf{Consensus} returned 10 calibration hits,
\textbf{0 new}. \textbf{Scholar Gateway} fails with \texttt{ACCESS\_DENIED}. \textbf{ClinicalTrials.gov}:
no PM or air-pollution registration updated in the window beyond EPIC-AIR (\texttt{NCT07500948}), carried
from the 3 October issue. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain the copyright of their
respective publishers."""
