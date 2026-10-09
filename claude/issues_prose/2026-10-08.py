# -*- coding: utf-8 -*-
HEAD = dict(long="8 October 2026", window="8 October 2026 (full day)", n=16, excl=63,
            bands=6, eff=6, tierA=5, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}The same day: a preregistered test of whether exposure-map
uncertainty intervals actually cover --- and a deposition model showing the same ambient concentration
delivers a threefold different dose depending on the source.}\\[1.4mm]
\footnotesize
Two records attack the two halves of the exposure problem. The first preregisters an external validation
of spatially valid conformal prediction on province-level population-weighted PM$_{2.5}$ across China
(1998--2024, $n$ = 837), with an acceptance band of [0.85, 0.95] declared in advance. Under spatial
hold-out it reached \textbf{0.873} coverage at nominal 90\,\% --- gradient boosting reached \textbf{0.486}
--- with interval widths identical to equal-weight conformal prediction, so the coverage was not bought
with wider intervals. Under \textit{temporal} hold-out coverage fell to \textbf{0.794} and the
preregistered joint hypothesis \textbf{failed}, traced to the post-2017 PM$_{2.5}$ decline.
The second takes source-apportioned particle number (6--1000\,nm) at an urban background site in Budapest
into a lung deposition model: deposition fraction ranges from \textbf{76\,\%} for new particle formation to
\textbf{27\,\%} for solid fuel combustion, maximum deposition at airway generations \textbf{17--21}, and
exercise shifts the deposit from extra-thoracic to alveolar.
\textbf{Why it matters for sensing:} one says the map's number needs an honest interval and the usual
method does not provide one; the other says the number is not the dose. Together they bracket what a
network actually owes a health study."""

CHANGED = [
r"""\textbf{Indoor constituents, modelled rather than measured.} 12,607 Chinese adults aged 86.8 on
average, 8,643 deaths: per 1\,$\mu$g\,m$^{-3}$, indoor black carbon \textbf{HR 1.072} (1.035--1.111)
against PM$_{2.5}$ mass \textbf{1.003} (1.001--1.005), with sulfate 1.010 and organic matter 1.009.
``Indoor'' here is an ambient field times a modelled infiltration factor --- the one quantity a cheap
indoor node measures directly.""",
r"""\textbf{540,000 deaths, and a 45\,\% forcing error.} A localized Chinese black-carbon inventory with a
revised risk function more than doubles the 2015 attributable mortality, while CMIP6 is found to
\textit{overestimate} BC radiative forcing by 45\,\%. The doubled burden rests entirely on that revised
risk function, and BC concentration--response is confounded with co-emitted species in every source study
it derives from.""",
r"""\textbf{Ageing changes the toxicity, not just the mass.} A GPF-equipped Euro 6 plug-in hybrid aged in a
secondary aerosol reactor, delivered to lung cells at the air--liquid interface, shifts composition and
toxicity from primary to secondary. Separately, parking-garage aerosol aged in an oxidation flow reactor
gained up to \textbf{6.9$\times$} SOA mass, O:C from \textbf{0.26 to 0.79}, higher oxidative potential and
greater DNA-damage response --- while acellular DCF activity \textit{fell}.""",
r"""\textbf{Kidneys in Beijing, and the tell.} 15,580 adults, 664 incident CKD: PM$_{10}$ \textbf{HR 1.18}
(1.06--1.31) per 10\,$\mu$g\,m$^{-3}$, PM$_{2.5}$ 1.22 (0.99--1.50), composite score 1.51 (1.07--2.12) per
IQR --- and ozone \textit{inverse} at 0.77 (0.68--0.87). Ozone rose as PM fell over the same six years in
the same city; the inverse estimate is the sign that single-pollutant models here are not separating
anything.""",
]

CONT = r"""The 7 October issue closed with \texttt{last\_entry\_date} at 7 October. This issue collects
\textbf{8 October in full}, continuous with it, and \textbf{closes the six-day backlog} that opened when
the 3 October issue failed to author on four consecutive runs. Harvest and screening for this day were run
fresh on this run. The \textbf{W40 weekly} (27 September--3 October) is the remaining outstanding item and
follows under 3 October."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 16 in-scope records --- the largest issue of the backfill.
\textbf{Six of ten bands populated}; \textit{Exposure assessment} leads with \textbf{five}, then
\textit{Burden} and \textit{Other clinical} three each, \textit{Mechanistic toxicology} and
\textit{Respiratory} two each, \textit{Occupational} one. \textit{Cardiovascular}, \textit{Neuro},
\textit{Reproductive} and \textit{Sensing} are empty --- the instrument-side work this day is filed under
exposure assessment because every record of it is a model rather than a device.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{five} modelling / inventory records (the conformal
validation, the deposition model, the GOES-R surface, the national BC burden and the productivity
analysis), \textbf{three} cohorts, two chamber studies (both aerosol-ageing toxicology), two measurement
campaigns, one cross-sectional and three metadata-only. Right --- half the records report a health
endpoint, which is the highest share of the backfill: all-cause mortality, incident CKD, two paediatric
respiratory outcomes and two in-vitro endpoints.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM or emissions \textbf{five},
PM$_{2.5}$ only four, composition / speciation three (the indoor constituents, the iron isotopes and the
aged-particle chemistry), PM$_{2.5}$ + PM$_{10}$ jointly three, and size-resolved number distribution one
--- the Budapest deposition record, which is also the only one whose exposure metric is a dose. Right ---
geography: China \textbf{six}, global / not stated three, Europe two, and one each for North America,
East Asia excluding China, Latin America, the Middle East \& North Africa and South Asia.""",
"f6_lifecourse": r"""Life-course windows: childhood \textbf{three} (the Ko-CHENS 36-month cohort, the
S\~ao Paulo paediatric admissions and the neonatal air-cleaner study) --- the most of any issue in this
backfill --- working age one (the Beijing CKD cohort) and older adults one (the indoor-constituent
mortality cohort). In utero and adolescence have no record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 16 records. Modelling fills exposure
assessment and burden; the two chamber studies sit together in mechanistic toxicology; the three cohorts
spread across other clinical and respiratory. No cell holds more than three records, which is what a
broad day looks like.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Six hazard ratios with 95\,\% CIs, log scale, from two cohorts. The four indoor-exposure estimates
share one cohort and one exposure surface and differ only in which constituent is entered, so they are
nested, not independent --- black carbon's per-$\mu$g\,m$^{-3}$ estimate is an order of magnitude above
PM$_{2.5}$ mass, which is biologically plausible and is also what regressing on a small-magnitude
collinear constituent produces. The two Beijing CKD estimates are per 10\,$\mu$g\,m$^{-3}$ of annual
exposure in a city where all pollutants fell together; the PM$_{2.5}$ interval crosses unity. The two
cohorts are not poolable: one is per 1\,$\mu$g\,m$^{-3}$ of a modelled indoor concentration, the other per
10\,$\mu$g\,m$^{-3}$ of ambient.}"""

PROV = r"""Entry window \textbf{8 October 2026}, single day, continuous with the 7 October issue. Harvester
legs run leg-by-leg on this run: \textbf{PubMed} health \textbf{14}, sensing \textbf{3}; \textbf{Europe
PMC} \textbf{26} (14 after the AGRICOLA retro-index gate dropped 12); \textbf{Crossref by ISSN}
\textbf{45}; \textbf{arXiv} answered with no entry dated 8 October; \textbf{OpenAlex} HTTP 429. 76 raw
deduplicated to \textbf{70}, 1 already carried, \textbf{69} fresh. The \textbf{PubMed connector}
(\texttt{[EDAT]} 7--8 October, both axes as separate queries) returned 24 PMIDs dated 8 October, 3 merging
a PMID onto an existing DOI-only record and \textbf{10} appended --- \textbf{79} candidates screened,
\textbf{16 admitted}, \textbf{63 rejected} with logged reasons. \textbf{Three records carried on metadata
alone} (19\,\%, the lowest share since 4 October). The DOI gate earned its place this run: it caught
\textbf{three} wrong DOIs on metadata-only records before the build and they were corrected against the
harvest cache --- \textbf{0 fail, 0 warn} on the re-run. The abstract-retry leg recovered \textbf{9 of
10} attempted. \textbf{Consensus} returned 10 calibration hits, \textbf{0 new}. \textbf{Scholar Gateway}
fails with \texttt{ACCESS\_DENIED}. \textbf{ClinicalTrials.gov}: no new PM or air-pollution registration
in the window. Abstracts remain the copyright of their respective publishers."""
