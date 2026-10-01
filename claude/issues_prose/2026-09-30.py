# -*- coding: utf-8 -*-
HEAD = dict(long="30 September 2026", window="30 September 2026 (full day)", n=25, excl=85,
            bands=9, eff=9, tierA=6, meta=8)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Per microgram, wildfire-smoke carbon is the most
lethal fraction of PM$_{2.5}$ in 77.5 million Medicare beneficiaries --- and a mass-only
network cannot see it.}\\[1.4mm]
\footnotesize
Jin and colleagues (\textit{ES\&T}, tier A) linked annual high-resolution smoke and non-smoke
PM$_{2.5}$, split into mass and carbonaceous matter, to Medicare enrolees 2002--2019. Per
1\,$\mu$g\,m$^{-3}$, all-cause mortality HR was \textbf{1.032} (1.027--1.037) for smoke PM$_{2.5}$ and
\textbf{1.087} (1.076--1.098) for smoke carbon --- both above their non-smoke counterparts. On the IQR scale
the mass ranking \textbf{reverses}, because chronic smoke exposure varies little between places; the
carbon fraction stays the stronger predictor either way. The authors attribute \textbf{22,420 deaths a
year} to smoke PM$_{2.5}$, most of it to its carbon, with larger effects in Black and dual-eligible
beneficiaries. \textbf{Caveats:} annual means flatten episodic smoke into a chronic metric, and the
smoke/non-smoke split is itself modelled. \textbf{Why it matters for sensing:} optical LCS report
mass, and their response to smoke differs from their response to urban aerosol. In fire regions a
network that adds an absorption or BC channel measures the fraction that drives the mortality
estimate, not just its mass."""

CHANGED = [
r"""\textbf{Half of global tuberculosis attributed to PM$_{2.5}$} (\textit{Ann Am Thorac Soc}, 140
studies, tier A): household solid fuel RR \textbf{1.82} (1.52--2.17), outdoor short-term PM$_{2.5}$ RR
\textbf{1.03} (1.00--1.05) per 10\,$\mu$g\,m$^{-3}$, giving \textbf{4.15 million} cases and $\sim$\textbf{535,000}
deaths in 2023 (49.9\,\%). The fraction rests on poverty-confounded fuel contrasts; read it as an
upper bound.""",
r"""\textbf{Acute PM$_{2.5}$ and cancer deaths, Japan} (47 prefectures, 2013--2022): \textbf{+0.88\,\%}
(0.57--1.18) per 10\,$\mu$g\,m$^{-3}$ at lag 0--2, gone after NO$_2$ or SO$_2$ adjustment. \textbf{MS
relapses, Paris} (1,152 patients, self-controlled): PM$_{10}$ IRR \textbf{1.28} and PM$_{2.5}$ \textbf{1.20} at a
two-week lag; the 11--12-week hits are likely multiplicity.""",
r"""\textbf{Meteorological adjustment.} A preprint covering ten French cities finds boundary-layer height carries
\textbf{nine times} the unique variance of wind speed for PM (four times for NO$_2$ and O$_3$), despite r\,$\approx$\,0.7 between them ---
trend normalisation and short-term models that adjust for wind alone are misspecified. A mobile-monitoring BC
model for a Beijing pregnancy cohort reaches CV R$^2$ \textbf{0.69} but is not validated at the homes it is
used for.""",
r"""\textbf{Policy modelling.} A Bayesian inversion shows emission cuts of similar tonnage range from full
compliance to almost none with the 9\,$\mu$g\,m$^{-3}$ NAAQS, depending on where and what is cut; maximal
afforestation in China adds only \textbf{0.39}\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ in summer, and two-thirds less under
carbon-neutral emissions.""",
r"""\textbf{Eight of 25 records are metadata-only (32\,\%)}, seven of them Elsevier deposits, including an
extreme-condition \textbf{sensor test chamber} (\textit{Atmos Environ}) and \textbf{satellite PM$_{2.5}$
composition} for Seoul, both first on the retry list. Scholar Gateway, the full-text route for these,
is still disconnected.""",
]

CONT = r"""The 29 September issue closed with \texttt{last\_entry\_date} at 29 September. This issue
collects \textbf{30 September in full}, continuous with it. The run started at 17:36 CDT on 1 October,
before the 22:00 cut, so the newest buildable date is 30 September and \textbf{1 October is left to the
next run}. The \textbf{September monthly} is built on this run, after this issue, so it includes it."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 25 in-scope records. \textbf{Nine of ten bands
populated}; \textit{Exposure assessment} leads with \textbf{eight} (five of them metadata-only),
\textit{Sensing} has six and \textit{Burden \& policy} four. \textit{Reproductive \& developmental} is empty;
the one prenatal record is a mouse study filed under mechanistic toxicology.""",
"f2_design_endpoint": r"""Left --- architecture: metadata-only \textbf{eight}, modelling four, cohort
three, and two each for measurement campaigns, chamber/laboratory, reviews and acute designs (the
case-crossover and the self-controlled MS series); one animal and one cross-sectional study. Right ---
\textbf{17} records carry no health endpoint; the eight that do are spread one each across neurological,
respiratory, cardiovascular, cancer mortality, all-cause mortality, multi-outcome proteomics,
haematological and animal neurodevelopment.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{eight}, unspeciated / emissions
six, PM$_{2.5}$ + PM$_{10}$ five, composition two, one each for PM$_{10}$ only, bioaerosol, size-resolved and
ultrafine. Right --- geography: global / not stated \textbf{seven} (the metadata-only records dominate),
Europe six, China five, East Asia ex-China and North America two each, and one each for South Asia,
Sub-Saharan Africa (C\^ote d'Ivoire) and Turkiye.""",
"f6_lifecourse": r"""Life-course windows: in utero one (mouse only), childhood one (the TB under-15 RR),
adolescence none, working age two (MS relapse, grill workers), older adults two (Medicare smoke,
solid fuel $\geq$60).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 25 records. The metadata-only column sits
almost entirely in \textit{Exposure assessment}; health designs are one-per-band, with no subtopic holding
more than one epidemiological study today.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Nine ratio estimates with 95\,\% CIs from six records, log scale. \textbf{Increments and
contrasts differ} (per 1, per 10, per year of fuel use, fuel-type and occupational contrasts, and an
unstated increment for the two MS rows), so the panel shows direction and precision, not a poolable
effect. The cancer-mortality and smoke-mass rows are tight because of their size, not because the
effect is large; the grill-worker dacrocyte row is the widest, from 25 workers per arm.}"""

PROV = r"""Entry window \textbf{30 September 2026}, single day, continuous with the 29 September issue.
Harvester legs run leg-by-leg: \textbf{PubMed} health \textbf{9}, sensing \textbf{2}; \textbf{Europe PMC}
\textbf{39} (36 after the retro-index gate); \textbf{Crossref by ISSN} \textbf{78}; \textbf{arXiv} no entry
dated 30 September; \textbf{OpenAlex} HTTP 429. 125 raw deduplicated to \textbf{123}, \textbf{13} already
carried, \textbf{110} fresh. The \textbf{PubMed connector} (\texttt{[EDAT]} 30 September) returned 6 health
and 0 sensing PMIDs, all already in the harvester set. \textbf{110} candidates screened, \textbf{25 admitted},
\textbf{85 rejected} with logged reasons (water chemistry and wastewater from \textit{ES\&T},
\textit{Measurement Science and Technology} engineering, meteorology and carbon-cycle work from
\textit{Atmosphere}, gas-phase-only records, and a record with no DOI). \textbf{Consensus} returned 10
calibration hits, \textbf{0 new}. \textbf{ClinicalTrials.gov}: one registry update (CAN-EXACT,
NCT07850648, observational COPD-exacerbation cohort with environmental factors only as a secondary
measure) screened, not added. \textbf{Scholar Gateway} still fails with an identity error.
\textbf{Eight records carried on metadata alone}. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain
the copyright of their respective publishers."""
