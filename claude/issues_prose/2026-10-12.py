# -*- coding: utf-8 -*-
HEAD = dict(long="12 October 2026", window="12 October 2026 (full day)", n=24, excl=40,
            bands=9, eff=8, tierA=2, meta=6)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}346.5 million admissions across six countries: short-term
PM$_{2.5}$ raises cancer, mental-disorder and nervous-system admissions more than respiratory ones, with lags
out to 21 days.}\\[1.4mm]
\footnotesize
949 communities in Australia, Brazil, Canada, Chile, New Zealand and Taiwan, 2000--2019, quasi-Poisson time
series pooled by meta-analysis. Per 10\,$\mu$g\,m$^{-3}$, all-cause admissions \textbf{RR 1.080} (1.074--1.086);
malignant neoplasms \textbf{1.108} (1.094--1.123), mental disorders \textbf{1.100}, nervous system \textbf{1.085}
--- all above respiratory, \textbf{1.067} (1.060--1.074). The attributable fraction against the WHO daily
guideline fell from 8.9\,\% (2000--09) to 3.9\,\% (2010--19).
\textbf{Where it is weak:} a 21-day distributed lag on cancer admissions is long enough to absorb scheduling
and elective-admission structure that has nothing to do with acute exposure, and the pooled RR is reported
alongside ``substantial heterogeneity'' that the abstract does not quantify. The non-respiratory ranking is
the result worth testing, not the headline 8\,\%."""

CHANGED = [
r"""\textbf{Composition beats mass, twice.} A 39.7-million-person Medicare preprint puts the wildfire-smoke
\textit{carbonaceous} fraction at HR 1.090 (1.077--1.103) per $\mu$g\,m$^{-3}$ for incident ADRD against 1.029
for smoke PM$_{2.5}$ mass; in Lanzhou, PAHs and Tl/Pb/Mn drive cardiovascular mortality in the traffic district
and nitrate/chloride/sulfate in the industrial one. Neither exposure is measurable by an optical node.""",
r"""\textbf{Sensor-built exposure reaches African epidemiology.} The Kinshasa case-crossover (13,049
admissions) builds its PM$_{2.5}$ series from PurpleAir and QuantAQ nodes fused with bias-corrected GEOS-CF ---
OR 1.01 (1.00--1.03) per 10\,$\mu$g\,m$^{-3}$, with no reported local validation of the fused series.""",
r"""\textbf{Two instrumentation results worth keeping.} A fixed distance graph beat learned, wind-informed and
hybrid graphs for 12-city PM$_{2.5}$ forecasting in Bangladesh; and LP-DOAS in Fairbanks shows inversion
layers only 20--40\,m deep persisting for days --- a rooftop and a breathing-height node sample different air.""",
r"""\textbf{A personal-monitor null that should not be read as a null.} Gambian children in solid-fuel homes
logged a geometric-mean personal PM$_{2.5}$ of 12.6\,$\mu$g\,m$^{-3}$, and colonisation showed no association;
an exposure that low in wood-smoke households points at the monitor, not at the biology.""",
r"""\textbf{Three held records enter.} The EHP biological-aging cohort, the Nat Commun congenital-heart-defect
proteomics study and the alveolar-organoid toxicology paper, held from the 9 October issue when authoring was
interrupted, are carried here.""",
]

CONT = r"""The 11 October issue closed with \texttt{last\_entry\_date} at 11 October. This issue collects
\textbf{12 October in full}, continuous with it. This run began at 19:46 CDT on 15 October and backfills
12, 13 and 14 October as three separate issues; 15 October is not opened under the 22:00 rule. The 9--11
October issues and the W41 weekly, built on 12 October but never committed, were proofed and pushed at the
start of this run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 24 in-scope records across nine of ten bands. Exposure
assessment leads (6) and sensing is second (4), carried by a graph forecaster, a respirable-dust
real-time-vs-gravimetric comparison, a dust-storm PM$_{10}$ forecaster and the Fairbanks inversion profiles.""",
"f2_design_endpoint": r"""Left --- architecture, including six metadata-only records (25\,\%), all Elsevier
deposits without abstracts at harvest. Right --- health endpoints: admissions dominate, with dementia,
congenital heart defects and biological aging as single records.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ dominates; composition-resolved records
(smoke carbon, components, metals, WSON) are a quarter of the issue. Right --- geography: China leads, with
records from the DR Congo, Gambia, Bangladesh, Kazakhstan and Saudi Arabia.""",
"f6_lifecourse": r"""Life-course windows: all five occupied for the first time since early October --- the
CHD periconception study, Gambian children 5--14, a 20--65 aging cohort and Medicare beneficiaries.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Sensing records are machine-learning or field
measurement; the health side is spread across time series, cohorts and one nested case-control.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Eight ratio estimates with 95\,\% CIs. Scales differ and the panel is not a meta-analysis: three are per
10\,$\mu$g\,m$^{-3}$ short-term (multicountry admissions), two are per 1\,$\mu$g\,m$^{-3}$ long-term (Medicare
smoke), one is a mixture-index odds ratio. The smoke-carbon HR is the largest per unit mass on the page; the
Kinshasa OR is the only estimate built on low-cost sensor exposure, and its lower bound touches the null.}"""

PROV = r"""Entry window \textbf{12 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{8},
sensing \textbf{0}; \textbf{Europe PMC} \textbf{7} (4 AGRICOLA retro-index records dropped, 3 kept);
\textbf{Crossref by ISSN} \textbf{47}; \textbf{arXiv} no entry dated 12 October; \textbf{OpenAlex} HTTP 429.
58 unique, 0 already carried. \textbf{PubMed connector} (\texttt{[EDAT]} 12--14 October) returned 34 PMIDs,
8 dated 12 October, 3 appended --- \textbf{61} candidates screened, \textbf{21 admitted}, \textbf{40 rejected}
with logged reasons; plus \textbf{3 held records} from 9 October. Abstract retry (PubMed $\to$ Europe PMC $\to$
Semantic Scholar) recovered 6 of 13; \textbf{6 records carried on metadata alone}. \textbf{Consensus}
calibration sweep: 10 + 10 hits, 0 new.
\textbf{Scholar Gateway} still \texttt{ACCESS\_DENIED}. Abstracts remain the copyright of their publishers."""
