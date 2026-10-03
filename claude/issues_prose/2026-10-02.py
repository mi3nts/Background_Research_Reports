# -*- coding: utf-8 -*-
HEAD = dict(long="2 October 2026", window="2 October 2026 (full day)", n=15, excl=56,
            bands=8, eff=3, tierA=2, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A 25-year, 100\,m daily PM$_{2.5}$ surface for the contiguous US
--- and, the same day, a rural low-cost network showing where interpolation stops working.}\\[1.4mm]
\footnotesize
Sheidaei and colleagues (\textit{ES\&T}, tier A) fill missing satellite AOD with a reanalysis-informed U-Net,
refine it with a bidirectional LSTM, downscale it on terrain to 100\,m and predict daily PM$_{2.5}$ over
$>$766 million cells for 2000--2024. Site-held-out validation: \textbf{R$^2$ = 0.82}, \textbf{RMSE = 2.85}\,$\mu$g\,m$^{-3}$;
spatial R$^2$ 0.94, temporal \textbf{0.78}. \textbf{Caveat:} the 100\,m detail is inherited from downscaled AOD
and land use, and regulatory monitors cannot validate sub-kilometre gradients; smoke-day skill is not
reported. Mielnik and colleagues (Research Square, tier A) ran low-cost sensors at \textbf{46} sites in the
Everglades Agricultural Area for 18 months: day-by-day leave-one-out R$^2$ ranged \textbf{0 to 0.99},
IDW beat kriging on most days, and smoke added \textbf{1.65}\,$\mu$g\,m$^{-3}$ (SE 0.13) inland.
\textbf{Why it matters for sensing:} the national product is smooth where the agricultural plume is
patchy; the honest use of a dense LCS network is as the residual on such a surface, and the 0--0.99 range is
the size of the day-to-day failure that a single-model exposure surface hides."""

CHANGED = [
r"""\textbf{Periconceptional PM$_{10}$ and congenital heart disease, Delhi NCR} (1,115 cases / 441 controls):
post-conception PM$_{10}$ AOR \textbf{3.36} (2.05--5.52) for all CHD and \textbf{4.35} (2.41--7.83) for VSD;
preconception PM$_{10}$ \textbf{2.82} (1.69--4.71) for simple CHD. ORs of 3--4 are far above the
literature; the exposure contrast is not stated and controls are outnumbered 2.5:1.""",
r"""\textbf{Conflict as an emissions experiment.} Across nine Middle Eastern countries during the 39-day
2026 conflict, column anomalies ordered by lifetime --- SO$_2$ \textbf{$-$45.6\,\%}, AOD \textbf{$-$19.6\,\%},
NO$_2$ $-$15.1\,\%, CO $-$8.6\,\%, CH$_4$ flat --- point to reduced hydrocarbon-sector emissions. The authors
decline a PM$_{2.5}$ burden: dust and anthropogenic aerosol are inseparable at CAMS resolution.""",
r"""\textbf{Condensables carry the metals.} Stack sampling in Chinese coking plants puts \textbf{44.5--57.4\,\%}
of flue-gas trace elements in the condensable fraction, with As and Cd enriched in PM$_{2.5}$; a 307-plant
inventory gives \textbf{159.8}\,kt PM in 2022, falling to 15.5\,kt by 2050 under BACT.""",
r"""\textbf{Instrument metadata.} For the SwisensPoleno Jupiter, the choice of baseline material (H$_2$O, NaCl,
SiO$_2$) changes the share of fluorescence-positive particles --- NaCl thresholds are up to 15$\times$ higher.
Bioaerosol counts are not comparable across networks unless baseline and threshold rule are reported.""",
r"""\textbf{Thin Friday.} PubMed entered only \textbf{7} PM records under \texttt{[EDAT]} 2 October; Crossref by
ISSN (40) was mostly off-topic \textit{AMT/ACP}, \textit{MST} and \textit{ES\&T} water chemistry. One
metadata-only record (\textbf{7\,\%}, the series low): an Aveiro-group indoor/outdoor school PM$_{10}$
toxicology paper in \textit{APR}, on the retry list.""",
]

CONT = r"""The 1 October issue closed with \texttt{last\_entry\_date} at 1 October. This issue collects
\textbf{2 October in full}, continuous with it. The run started at 14:50 CDT on 3 October, before the 22:00
cut, so the newest buildable date is 2 October; \textbf{3 October and the W40 weekly (27 September--3 October)
are left to the next run}."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 15 in-scope records. \textbf{Eight of ten bands populated};
\textit{Exposure assessment} leads with \textbf{five} (two tier A), then two each for \textit{Sensing},
\textit{Mechanistic toxicology} and \textit{Occupational \& indoor}. \textit{Neuro / mental health} and
\textit{Other clinical} are empty; the one neuro-relevant record is an astrocyte study filed under toxicology.""",
"f2_design_endpoint": r"""Left --- architecture: modelling / inventory \textbf{six} (two deep-learning
models, the CTM, the satellite analysis, the inventory, the interpolation study), cross-sectional three,
and one each for the field campaign, laboratory validation, in-vitro exposure, review, cohort and the
metadata-only record. Right --- \textbf{nine} records carry no health endpoint.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{five}, unspeciated / emissions
three, PM$_{2.5}$ + PM$_{10}$ two, and one each for PM$_{10}$, size-resolved (PM$_{0.2}$), bioaerosol, optical
(BC) and composition. Right --- geography: North America and China \textbf{three} each, global / not stated
three (laboratory, review, metadata-only), Europe and South Asia two each, Middle East and Sub-Saharan
Africa one each.""",
"f6_lifecourse": r"""Life-course windows: in utero one (Delhi CHD), childhood one (school PM$_{10}$,
metadata only), working age one (traffic police), adolescence and older adults none.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 15 records. Modelling sits in exposure,
sensing and burden; the three cross-sectional records are spread across respiratory, occupational and
reproductive (the case-control study).""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Three adjusted odds ratios with 95\,\% CIs, all from the Delhi NCR CHD case-control study, log
scale. The PM$_{10}$ contrast (per unit or category) is not given in the abstract, and the three share
cases and controls, so they are not poolable. The MESA heart-failure preprint reports biomarker HRs only
(PM$_{2.5}$ is a co-adjustment), and the Ouagadougou OR (1.70) has no CI; neither enters the panel.}"""

PROV = r"""Entry window \textbf{2 October 2026}, single day, continuous with the 1 October issue. Harvester
legs run leg-by-leg: \textbf{PubMed} health \textbf{6}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{31};
\textbf{Crossref by ISSN} \textbf{40}; \textbf{arXiv} no entry dated 2 October; \textbf{OpenAlex} HTTP 429.
78 raw deduplicated to \textbf{76}, \textbf{9} already carried, \textbf{67} fresh. The \textbf{PubMed
connector} (\texttt{[EDAT]} 2 October) returned 7 health and 0 sensing PMIDs; 4 appended. \textbf{71}
candidates screened, \textbf{15 admitted}, \textbf{56 rejected} with logged reasons (\textit{AMT/ACP}
cloud, ozone and radiation work, \textit{MST} engineering, \textit{ES\&T} water and soil chemistry, LCA
records, a benzene-only cohort, NO$_2$-only trends, an editorial and a commentary). \textbf{Consensus}
returned 10 calibration hits, \textbf{0 new} (all archived or previously rejected).
\textbf{ClinicalTrials.gov}: no PM/air-pollution registration updated 2--3 October. \textbf{Scholar
Gateway} still fails with an identity error. \textbf{One record carried on metadata alone}. DOI gate:
\textbf{0 fail, 0 warn}. Abstracts remain the copyright of their respective publishers."""
