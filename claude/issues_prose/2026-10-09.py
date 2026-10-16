# -*- coding: utf-8 -*-
HEAD = dict(long="9 October 2026", window="9 October 2026 (full day)", n=19, excl=52,
            bands=6, eff=5, tierA=3, meta=7)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Two records say the quantity being measured is the wrong
one: the toxicity of PM$_{2.5}$ organics is carried by reduced nitrogen compounds, and the fastest-growing
traffic particle source is tyre and road wear, not exhaust.}\\[1.4mm]
\footnotesize
Nontargeted high-resolution mass spectrometry plus serum-albumin adductomics restricts attention to the
organic fraction that actually reaches the circulation, then scores it: \textbf{reduced organic nitrogen}
compounds carry \textbf{39\,\%} of predicted multi-organ toxicity against \textbf{23\,\%} for the
oxygenated organics the field normally targets. Separately, a road-segment-resolved national inventory
puts China's tyre and road wear particles at \textbf{425\,kt} of PM$_{2.5}$ in 2023, roughly
\textbf{80\,\%} of it modelled resuspension, with the TRWP share of traffic PM$_{2.5}$ projected to rise
\textbf{34-fold} from 2011 to 2050 and reach \textbf{67\,\%} of traffic emissions.
\textbf{Why it matters for sensing:} both quantities are invisible to an optical mass node. Nitrogenous
organics are a composition signal --- and, per a third record the same day, the ones that absorb at
365\,nm, so a multi-wavelength absorption channel sees them. Non-exhaust PM is coarse-skewed and
mineral-rich, the aerosol class on which Plantower-type sensors misreport mass worst; a rising non-exhaust
share therefore drifts a network's calibration without any hardware changing."""

CHANGED = [
r"""\textbf{Source-resolved PM$_{2.5}$ and dementia.} 5,648 incident cases over a median 11.9 years, Cox
models with time-varying source-specific exposure: per IQR, road transport \textbf{HR 1.12} (1.04--1.21),
other transport 1.12 (1.06--1.19), industry 1.07 (1.03--1.11), domestic 1.05 (1.01--1.08). Per-IQR scaling
differs by source, so this is not a per-$\mu$g ranking, and the source fields are spatially collinear
outputs of one dispersion model.""",
r"""\textbf{A 1\,\% effect on six million admissions.} Time-stratified case-crossover over 6,098,836
Medicare ADRD index admissions: an IQR (7.2\,$\mu$g\,m$^{-3}$) rise in lag 0--2 PM$_{2.5}$ gave
\textbf{OR 1.010} (1.006--1.015) for 30-day all-cause readmission. Green and blue space did not
conclusively modify it --- unsurprising when exposure is ZIP-code modelled air for a largely homebound
population.""",
r"""\textbf{Persistence is still the baseline.} Five-station VAR models in Navi Mumbai bound six of seven
lagged co-pollutant effects within \textbf{$\pm$5\,\%} per SD; rain and boundary-layer height move same-day
PM$_{2.5}$ by \textbf{10--24\,\%} per SD, and shared date effects explain \textbf{78\,\%} of variance,
three-quarters of it weather. A stagnation index plus persistence warned as skilfully as XGBoost --- which
did not beat persistence. The same day carries two forecasting papers that report no persistence baseline
at all, one of them an implausible 0.73\,$\mu$g\,m$^{-3}$ next-day RMSE for Tehran.""",
r"""\textbf{Residential burning, measured two ways.} PMF on PM$_{10}$ with 34 species at an urban
background site in Belgrade puts \textbf{biomass burning first at 21\,\%}, ahead of ammonium sulphate
(18\,\%) and mineral dust (17\,\%), with traffic and industry unresolved from each other at 15\,\%. In the
North China Plain, water-soluble brown carbon absorption at a rural site ran \textbf{1.1--3.5$\times$} the
urban values while urban Abs$_{365}$ fell \textbf{$\sim$45\,\%} since 2018.""",
]

CONT = r"""The 8 October issue closed with \texttt{last\_entry\_date} at 8 October. This issue collects
\textbf{9 October in full}, continuous with it; 10 and 11 October follow as their own issues on this run,
and the \textbf{W41 weekly} (4--10 October) follows under 10 October. Three records admitted to this day
are \textbf{held, not rejected} --- authoring was interrupted mid-file --- and are logged as held in
\texttt{rejected.jsonl}, absent from this issue and from the W41 pool: the EHP green-space/biological-aging
cohort, the \textit{Nat.\ Commun.} congenital-heart-defect proteomics case-control, and the alveolar-organoid
toxicology record. They should enter a later issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 19 in-scope records. \textbf{Six of ten bands populated};
\textit{Exposure assessment} leads with \textbf{six} and \textit{Sensing} follows with \textbf{five} ---
the measurement side is 58\,\% of the day, the highest share since 3 October. \textit{Occupational \&
indoor} three, \textit{Burden} and \textit{Neuro} two each, \textit{Mechanistic toxicology} one.
\textit{Cardiovascular}, \textit{Respiratory}, \textit{Reproductive} and \textit{Other clinical} are empty
--- two of those four are empty because the records that would have filled them are among the three held.""",
"f2_design_endpoint": r"""Left --- architecture, in the grouped categories the figure uses:
\textbf{seven} metadata-only records (37\,\%, the highest share since 29 September, every one a publisher
deposit without an abstract), \textbf{six} measurement campaigns, three modelling / inventory records, and
one each of cohort, acute-design epidemiology and chamber study. Right --- only \textbf{three} records
carry a health endpoint (incident dementia, 30-day readmission, estimated worker inhalation dose); the rest
report concentrations, optical properties, emissions or forecast skill.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{seven}, unspeciated PM or
emissions \textbf{five}, size-resolved number two (the fast-scan MPSS calibration and the dormitory
Stokes-number record), PM$_{2.5}$ + PM$_{10}$ jointly two, and one each of PM$_{10}$ only, bioaerosol /
coarse, and optical properties. Right --- geography: global / multi-region \textbf{six} --- inflated,
because three records state no location and two more are method papers with no site --- then China
\textbf{four}, Europe three (Belgrade, Central European rural background, the UK nowcasting series), South
Asia two, Latin America two, and one each for North America and the Middle East \& North Africa.""",
"f6_lifecourse": r"""Life-course windows: older adults \textbf{two} (the source-specific dementia cohort
and the Medicare ADRD readmission study) and working age \textbf{one} (wastewater and landfill
bioaerosol exposure). In utero, childhood and adolescence have no record --- the periconception record
that would have occupied the first column is one of the three held.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 19 records. The metadata-only column is
the densest in the matrix and spreads across exposure assessment, burden, sensing and indoor --- a
deposit-pattern artefact, not a research pattern. No other cell holds more than two records.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Five estimates with 95\,\% CIs, log scale, from two studies. The four dementia hazard ratios come
from one cohort and one exposure model and differ only in which emission source is entered; they are
nested, not independent, and each is scaled per source-specific IQR, so the apparent ordering of transport
above domestic is not a comparison at equal mass. The Medicare readmission odds ratio is a different
quantity entirely --- a short-term, within-person contrast per 7.2\,$\mu$g\,m$^{-3}$ of daily PM$_{2.5}$
against long-term annual exposure for the dementia estimates --- and the two are not poolable. Its
interval is narrow because the denominator is six million admissions, not because the effect is precisely
characterised at the individual level.}"""

PROV = r"""Entry window \textbf{9 October 2026}, single day, continuous with the 8 October issue.
Harvester legs: \textbf{PubMed} health \textbf{14}, sensing \textbf{6}; \textbf{Europe PMC} \textbf{33}
(23 after the retro-index gate dropped 10); \textbf{Crossref by ISSN} \textbf{37}; \textbf{arXiv}
answered (148\,kB) with \textbf{one} entry dated 9 October; \textbf{OpenAlex} HTTP 429 --- the leg has
returned 429 on every run since 26 September and is treated as dead. 81 raw records deduplicated to
\textbf{75}, 5 already carried, \textbf{70} fresh. The \textbf{PubMed connector} (\texttt{[EDAT]}
9--11 October, health and instrumentation axes as separate queries) returned 9 PMIDs dated 9 October, of
which \textbf{1} was appended --- \textbf{71} candidates screened, \textbf{22 admitted}, \textbf{3 held},
\textbf{49 rejected} with logged reasons. \textbf{Seven records carried on metadata alone} (37\,\%); the
abstract-retry chain (PubMed efetch $\to$ Europe PMC $\to$ Semantic Scholar) recovered \textbf{10 of 19}
attempted and none of the nine Elsevier or Springer deposits. \textbf{Consensus} returned 10 calibration
hits, \textbf{0 new}. \textbf{Scholar Gateway} fails with \texttt{ACCESS\_DENIED} and has done for the
whole backfill --- it is the designated route for the calibration R$^2$/RMSE figures the MPSS record
omits, and it needs reconnecting. \textbf{ClinicalTrials.gov}: one new registration in the 4--11 October
window, surfaced in the W41 weekly. Abstracts remain the copyright of their respective publishers."""
