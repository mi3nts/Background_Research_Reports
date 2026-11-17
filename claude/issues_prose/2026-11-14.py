# -*- coding: utf-8 -*-
HEAD = dict(long="14 November 2026", window="14 November 2026 (full day)", n=27, excl=30,
            bands=7, eff=4, tierA=5, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Run PurpleAir offline in the cold and the winter record goes missing: with SD-card logging and no WiFi, pilot co-locations recovered 100\,\% of data in Arizona but 57\,\% in Oklahoma and 10\,\% in South Dakota, with logging failing at mean (SD) ambient temperatures of 4.4 (3.2) and 7.7 (2.0)\,$^\circ$C.}\\[1.4mm]
\footnotesize
Columbia University, \textit{Sensors}; Strong Heart Air Study, ten PurpleAir monitors co-located per site in three American Indian communities before a cardiovascular cohort deployment. SD logging was chosen to keep data under community control rather than in the vendor cloud. Outdoor tests suggested a WiFi connection protects logging at low temperature; 4\,$^\circ$C cold-room runs reproduced the failure without WiFi.
\textbf{Where it is weak:} a pilot completeness finding, not an accuracy evaluation; firmware and card models are not in the abstract, and the mechanism (power, card or firmware) is not isolated.
\textbf{Why it matters here:} the missingness is not at random --- it concentrates in cold, stagnant, wood-smoke weeks, so any exposure--response analysis built on offline PurpleAir data in cold climates is biased toward the clean season unless the gap is modelled."""

CHANGED = [
r"""\textbf{Sensirion over 19 months.} Two SEN54 and two SPS30 against a Fidas 200S (Czech Hydrometeorological Institute): raw PM$_{2.5}$ R$^2$ 0.87 (RMSE 5.53\,$\mu$g/m$^3$), PM$_{10}$ only 0.50 (13.70); a MARS correction on dew point deficit lifted them to 0.92 (3.29) and 0.68 (8.25). Mineral-dust PM$_{10}$ episodes stayed invisible.""",
r"""\textbf{Calibrate one, deploy many --- fails for PM$_{10}$.} TU Delft, five multi-modal devices in Brussels: tree ensembles win on the source unit but lose their advantage over the \emph{uncalibrated} sensor for PM$_{10}$ once transferred; a cross-sensor residual monitor catches injected drift in reconstructable channels. Separately, an Upper Silesia SDS011 study emulates a heated inlet in software (R$^2$ 94\,\%, RMSE 3.69--3.79\,$\mu$g/m$^3$ against the heated twin) --- a low-cost target, not a reference.""",
r"""\textbf{Telomeres: significant until clustered.} Northern Thailand, 179 rural adults: relative LTL +0.050 T/S (0.012--0.089) per IQR of 0--30-day PM$_{2.5}$ and +0.079 (0.035--0.123) at 0--60 days --- but the authors' wild cluster bootstrap over eight site--date groups leaves all five windows non-significant (p 0.25--0.79).""",
r"""\textbf{Randomised stove, no PM$_{2.5}$ gradient.} HAPIN Peru follow-up, 101 children aged 3--5: oscillometry did not differ between LPG and biomass arms; no association with prenatal or postnatal personal PM$_{2.5}$; postnatal CO tracked worse reactance (AX7 +0.041 z per ppm, 0.003--0.078).""",
r"""\textbf{Exposure basis (x1).} Five of today's 27 records rest on low-cost sensors, all on the measurement side, none producing a health estimate. Of the four forest estimates, only the HAPIN contrast rests on measured (personal) exposure; the Geneva interaction uses a modelled residential surface and the Thai telomere paper does not state its PM$_{2.5}$ source. \emph{No effect estimate today comes from sensor-measured exposure.}""",
]

CONT = r"""The 13 November issue closed the day before. This issue was built on the \textbf{16 November 05:40 UTC (23:40 CST 15 November) run}. After 22:00 CST the newest buildable day is today, so this run owes \textbf{12, 13, 14 and 15 November as four issues} plus the \textbf{W46 weekly (8--14 November)}, which is filed under this Saturday alongside this daily; \textbf{14 November is covered in full}. A cross-day pass assigned 11 records that resurfaced today to earlier issues. No \textsc{backfill} records today. OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session, and Scite was not run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 27 records across seven of ten bands: sensing 7, mechanistic 6, exposure assessment 4, occupational \& indoor 3, respiratory 3, cardiovascular/metabolic 2, burden 2. Neuro/mental health, reproductive and other clinical are empty today.""",
"f2_design_endpoint": r"""Left --- architecture: animal and in-vitro work, reviews, calibration and field sensor studies, two randomised trials (vitamin D in people living with HIV; the HAPIN stove follow-up), three metadata-only records, two time series and two cross-sectional studies. Right --- endpoints are almost all singletons; the three metadata-only records form the only shared bar.""",
"f3_metric_geography": r"""Left --- particle metric as classified from the record fields. Right --- geography by record: China, the United States and Europe dominate, with single records from Thailand, Viet Nam, Taiwan, Peru, Colombia, India and Korea.""",
"f6_lifecourse": r"""Life-course windows. In utero and childhood are the HAPIN Peru follow-up (prenatal stove randomisation, oscillometry at 3--5 years) and the Geneva children; adolescence the Geneva adolescents (null); working age the Wuhan vitamin D trial, the Thai telomere study and the Ahmedabad slum households; older adults the Madrid heat--pollution mortality series (all ages).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Sensing is the widest row (calibration comparisons, field campaigns, an instrument build, a simulation and a metadata-only comment); mechanistic is animal, in-vitro and review work; the two randomised trials sit in mechanistic and respiratory.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, one estimate: the Geneva financial-situation $\times$ PM$_{2.5}$ interaction for child excess weight, aOR 1.59 (0.98--2.59), increment not stated in the abstract. Null at 95\,\%.}\end{minipage}

\vspace{2mm}
\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale, three estimates on two different units. Two are telomere length (T/S units) per window-specific IQR of PM$_{2.5}$ in northern Thailand, whose own cluster bootstrap renders them non-significant; one is the randomised LPG-versus-biomass contrast in post-bronchodilator resonance frequency z-score (HAPIN Peru), not a PM increment. Different endpoints and units: no pooling and no I$^2$.}\end{minipage}"""

X1NOTE = ""

PROV = r"""Entry window \textbf{14 November 2026}, single day (Saturday). Harvester legs: \textbf{PubMed} health \textbf{23}, sensing \textbf{6}; \textbf{Europe PMC} \textbf{17}; \textbf{Crossref by ISSN} \textbf{23}; \textbf{arXiv} no in-window entry; \textbf{OpenAlex} HTTP 429 on the harvester leg. 69 raw, 58 unique, 1 already carried, 57 fresh. PubMed connector (EDAT 12--15 November, three axes) 53 PMIDs (\texttt{\_conn\_1116.py}), 18 bucketed to 14 November, 1 seen, 11 appended (68); the cross-day pass found 11 already in earlier days' sets --- \textbf{57 screened}. Abstracts: efetch filled 27 of 27 PMID records; Crossref/Semantic Scholar recovered none of the Crossref records tried.
OpenAlex, alphaXiv, bioRxiv/medRxiv and Wiley Scholar Gateway connectors were not available on this session; \textbf{Scite} retraction check not run, so no record carries a Scite check. No Amass or Consensus backfill this run.
\textbf{27 admitted}, \textbf{30 rejected} with logged reasons. \textbf{3 carried on metadata alone}. Affiliations from PubMed XML and Crossref (OpenAlex unavailable); blank where neither carries one. Trial watch: see W46 weekly.
Abstracts remain the copyright of their publishers."""
