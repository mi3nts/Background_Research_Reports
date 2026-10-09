# -*- coding: utf-8 -*-
HEAD = dict(long="5 October 2026", window="5 October 2026 (full day)", n=13, excl=39,
            bands=7, eff=3, tierA=2, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}2.1 million adults, 19 million person-years, and the
exposure that carries the dementia signal is the one no low-cost node measures.}\\[1.4mm]
\footnotesize
Batisse and colleagues (\textit{Epidemiology}, tier A) linked high-resolution residential \textbf{ultrafine
particle number} and \textbf{UFP size} to cause-of-death records for 2.1\,million adults in Montreal and
Toronto, 2001--2019: \textbf{20,560} neurodegenerative deaths, and per \textbf{10,000 particles\,cm$^{-3}$}
a dementia-mortality \textbf{HR of 1.22} (1.17--1.27) --- stronger after adjusting for particle size,
positive across every dementia subtype, largest for vascular dementia. \textbf{Caveat:} UFP number and
NO$_2$ share the same traffic gradient, so co-pollutant adjustment cannot cleanly separate them, and
dementia is under-ascribed on death certificates.
\textbf{Why it matters for sensing:} UFP is unregulated, and an optical low-cost sensor is blind to it ---
it reports a scattering proxy for mass, and sub-100\,nm particles scatter almost nothing. A network built
to track PM$_{2.5}$ mass reports approximately zero information about the exposure this cohort implicates.
The same day, a tethered-balloon synthesis over Houston shows the other blind spot: profiles that vary
severely with boundary-layer depth above a surface node that cannot see any of it."""

CHANGED = [
r"""\textbf{Gene--environment interaction in 313,534 people.} UK Biobank: PM$_{2.5}$ \textbf{HR 1.22 per
5\,$\mu$g\,m$^{-3}$} (1.19--1.26) across five chronic-disease groups, with additive interaction between
high polygenic risk and high PM$_{2.5}$ for neurodegenerative disease (RERI 0.14) and diabetes (0.21).
A healthy-volunteer cohort over a narrow exposure range, five outcomes, four pollutants, and no
multiplicity correction on the interaction terms.""",
r"""\textbf{The 1.5\,m reading is not the 20\,m reading.} A three-level mast inside a Shenyang urban forest
through the heating season found PM$_{2.5}$ and PM$_{10}$ \textit{higher} at 10 and 20\,m than at pedestrian
level, O$_3$ and CO higher at 1.5\,m, NO$_2$ and SO$_2$ peaking mid-canopy. One site, one winter --- but
network siting guidance assumes a well-mixed sub-canopy layer, and this is direct evidence against it.""",
r"""\textbf{Triangulation that is not independent.} Pretoria: hazard quotients above unity in all age
groups, case-crossover \textbf{OR 1.027} (1.006--1.049) per 10\,$\mu$g\,m$^{-3}$, and 158--748 admissions
avertable depending on the counterfactual. The three methods re-use one exposure series, and summing
element-specific attributable cases double-counts the mass those elements are part of.""",
r"""\textbf{Respirable dust is the wrong metric for a silica hazard.} Personal sampling across five
stone-working tasks in Thailand: all means below the Thai OEL and TLV, highest in carving
(0.051\,mg\,m$^{-3}$), modelled ILCR $3.3\times10^{-7}$. No crystalline silica fraction is reported, and an
EPA inhalation-unit-risk framework applied to mixed mineral dust yields a number with no
exposure--response behind it.""",
]

CONT = r"""The 4 October issue closed with \texttt{last\_entry\_date} at 4 October. This issue collects
\textbf{5 October in full}, continuous with it. Harvest and screening were completed on the 6 October run
and cached; this run authored from that cache without re-querying. Dailies for 6--8 October and the W40
weekly (27 September--3 October) remain owed and follow in this backfill."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 13 in-scope records. \textbf{Seven of ten bands populated};
\textit{Exposure assessment} leads with \textbf{four} (three of them metadata-only), \textit{Sensing} has
three, \textit{Occupational \& indoor} two, and one each for \textit{Neuro}, \textit{Other clinical},
\textit{Respiratory} and \textit{Burden}. The clinical side is thin but carries both tier-A records.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{five} records carry no abstract and assert no
design; \textbf{four} are measurement campaigns (the canopy mast, the tethered balloon, the Nagpur
monitoring year and the Xinxiang mercury sampling); two are cohorts (CanCHEC, UK Biobank), one acute
(the case-crossover) and one cross-sectional (the stone carvers). Right --- the majority of records report
no health endpoint; the four that do are split between neurodegenerative mortality, multi-system chronic
disease, respiratory admissions and a modelled cancer risk.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM and PM$_{2.5}$ + PM$_{10}$ jointly and
PM$_{2.5}$ only take three each, with one record each for size-resolved number distribution (the Houston
profiles), optical properties, settleable/respirable dust (the personal sampling) and bioaerosol. The UFP
cohort is the only record whose exposure is a \textit{number} concentration. Right --- geography: China
\textbf{five}, North America two, and one each for Europe, Sub-Saharan Africa, South Asia, Southeast Asia,
the Middle East \& North Africa and global / multi-region.""",
"f6_lifecourse": r"""Life-course windows: older adults one (the UFP dementia-mortality cohort), working age
one (stone carvers under personal sampling), childhood one (the paediatric-ward bioaerosol model, metadata
only). In utero and adolescence have no record. The UK Biobank cohort spans adulthood and is not assigned
to a single window.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 13 records. The metadata-only block spans
exposure assessment, sensing and occupational; measurement campaigns occupy sensing, exposure and burden;
the three epidemiological architectures each sit alone in their clinical band.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Three estimates with 95\,\% CIs, log scale, from three different cohorts and three different
exposure contrasts --- per 10,000\,particles\,cm$^{-3}$ of UFP number (dementia mortality), per
5\,$\mu$g\,m$^{-3}$ of annual PM$_{2.5}$ (chronic-disease incidence) and per 10\,$\mu$g\,m$^{-3}$ of daily
PM$_{2.5}$ (respiratory admissions). The first two agree at 1.22 by coincidence of scaling, not of effect:
one is a chronic number-concentration contrast and the other an annual-mass contrast, and they are not
poolable. The third is an acute estimate and belongs to a different estimand entirely.}"""

PROV = r"""Entry window \textbf{5 October 2026}, single day, continuous with the 4 October issue. Harvest
and screening for this day were completed on the \textbf{6 October} run and cached
(\texttt{cache/2026-10-05/\_fresh.json}); this run authored from that cache without re-querying.
\textbf{52} fresh candidates after cross-day deduplication, \textbf{13 admitted}, \textbf{39 rejected} with
logged reasons (\textit{ACP} cloud microphysics and radiation, ozone-only and NO$_2$-only analyses, water
and soil chemistry, life-cycle assessment, and the usual PubMed broad-axis noise). \textbf{Five records
carried on metadata alone} (38\,\%, a series high) --- Elsevier's 5 October deposit is abstract-free across
four journals, and the retry leg recovered none. \textbf{Consensus} returned 10 calibration hits,
\textbf{0 new}. \textbf{Scholar Gateway} fails with \texttt{ACCESS\_DENIED}; it has now been unavailable
for the whole of this backfill. \textbf{ClinicalTrials.gov}: no new PM or air-pollution registration in the
window. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain the copyright of their respective
publishers."""
