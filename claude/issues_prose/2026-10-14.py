# -*- coding: utf-8 -*-
HEAD = dict(long="14 October 2026", window="14 October 2026 (full day)", n=24, excl=56,
            bands=9, eff=5, tierA=2, meta=8)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A national correction beat local fitting for PurpleAir in
Philadelphia --- RMSE 1.64\,$\mu$g\,m$^{-3}$ --- and accuracy fell from R$^2$ 0.68 to 0.57 within a year in the
field.}\\[1.4mm]
\footnotesize
Co-location across summer and spring plus a one-year re-evaluation. The Barkjohn (2021) US-wide correction
applied to the mean of the two channels' \texttt{atm} outputs gave \textbf{RMSE 1.640}\,$\mu$g\,m$^{-3}$,
\textbf{MBE 0.103}, \textbf{R$^2$ 0.683} at both 1\,h and 24\,h, outperforming locally derived corrections. On-board
vs weather-station RH changed R$^2$ by only 0.04. After a year, \textbf{R$^2$ 0.567}.
\textbf{Where it is weak:} R$^2$ at low temperate concentrations is range-limited, so part of the year-one drop may
be a narrower concentration distribution rather than drift; the abstract does not separate the two. Barkjohn was
derived on \texttt{cf\_1}, so applying it to \texttt{atm} is off-label even if it works here. The operational
reading is still clear: budget a scheduled re-co-location inside the first year."""

CHANGED = [
r"""\textbf{Two tier-A records, one of them calibration.} The Consensus sweep surfaced a mechanistic
aerosol-liquid-water humidity correction (ACS ES\&T Air, January 2026); the DOI gate showed it was already carried
in the 2 August issue, so it is not repeated here --- the one-record-one-issue rule held.""",
r"""\textbf{Smoke and the upper airway, again.} SEER county DLNM: any annual wildfire PM$_{2.5}$ exposure cRR
\textbf{1.41} (1.24--1.60) for head and neck cancer over 0--10-year lags, larynx 1.13 per exceedance day --- the
second smoke--aerodigestive cancer signal in two days after the 13 October China fire-PM result.""",
r"""\textbf{Spatial information budget.} A 1\,km CMAQ for Washington, D.C. finds NO$_2$'s intra-urban
coefficient of variation more than three times PM$_{2.5}$'s, and 4$\to$1\,km refinement moves PM$_{2.5}$
population-weighted exposure by only 1.5--3\,\%: dense PM$_{2.5}$ networks buy less spatial contrast than NO$_2$
networks would.""",
r"""\textbf{Indoor secondary particles.} Ventilated outdoor O$_3$ made indoor new particle formation VOC-limited;
limonene drove growth at 20--100\,nm\,h$^{-1}$ --- particles that PM$_{2.5}$-only indoor monitors do not see until
they pass $\sim$300\,nm.""",
r"""\textbf{Burden arithmetic.} Abu Dhabi attributable deaths rose from 231 to 1,249 while air quality held
roughly steady --- driven mainly by steeper concentration--response functions, not by exposure.""",
]

CONT = r"""The 13 October issue (built earlier in this run) closed with \texttt{last\_entry\_date} at 13 October.
This issue collects \textbf{14 October in full}, continuous with it, and brings the watch current. 15 October is
not opened: this run began at 19:46 CDT on 15 October, before 22:00. The \textbf{W42 weekly} (11--17 October)
is due with the Saturday 17 October issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 24 in-scope records across nine bands. Exposure assessment and
burden lead at five each; sensing (2) is small in count but carries one of the two tier-A records.""",
"f2_design_endpoint": r"""Left --- architecture: eight metadata-only records (32\,\%), seven of them Elsevier
deposits, the series' recurring blind spot. Right --- health endpoints: cancer (head and neck, HCC), CSF
biomarkers, undernutrition, hyperemesis, antioxidant capacity.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ leads; UFP, deposited dose, Pb, dust optics and
indoor number distributions appear once each. Right --- geography: United States leads (4), with India,
Pakistan, Iran, UAE, Spain, Morocco and Turkiye.""",
"f6_lifecourse": r"""Life-course windows: pregnancy (hyperemesis), under-fives (Pakistan), adolescents
(Isfahan trial), working age (ALFA+ midlife, cathode workers). No older-adult-specific record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. The metadata-only column spans five bands; the
sensing row is entirely field measurement.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Five ratio estimates with 95\,\% CIs from two studies. The three head-and-neck cancer estimates are
cumulative RRs from one county-level DLNM on three different exposure definitions --- not independent. The two
Pakistan ORs compare polluting with clean cooking fuel, a wealth-confounded proxy with no measured PM. None of the
five is per unit concentration.}"""

PROV = r"""Entry window \textbf{14 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{26},
sensing \textbf{4}; \textbf{Europe PMC} \textbf{0} (index lag; the 14 October creation date had not populated
by harvest); \textbf{Crossref by ISSN} \textbf{48}; \textbf{arXiv} no entry dated 14 October; \textbf{OpenAlex}
HTTP 429. 75 unique, 0 already carried. \textbf{PubMed connector} 18 PMIDs dated 14 October, 1 merged, 5
appended --- \textbf{80} candidates screened, \textbf{24 admitted}, \textbf{56 rejected} with logged reasons (one,
the GeoHealth ammonia model, a PubMed copy of a 13 October Crossref record). \textbf{Consensus}
calibration sweep: 20 hits, \textbf{0 new} (one apparent new hit, ACS ES\&T Air 2026, was caught by the DOI gate as
shipped on 2 August).
Abstract retry recovered 15 of 24; the PurpleAir validation abstract came from Consensus; \textbf{8 records
carried on metadata alone}. \textbf{Scholar Gateway} still \texttt{ACCESS\_DENIED}. Abstracts remain the
copyright of their publishers."""
