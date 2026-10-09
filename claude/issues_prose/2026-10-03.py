# -*- coding: utf-8 -*-
HEAD = dict(long="3 October 2026", window="3 October 2026 (full day)", n=14, excl=45,
            bands=7, eff=5, tierA=1, meta=4)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Constituent-specific lung-cancer risk in a quarter-million
never-smokers --- and the constituent it fingers is the one low-cost sensors measure worst.}\\[1.4mm]
\footnotesize
Xia and colleagues (\textit{J.\ Hazard.\ Mater.}, tier A) followed \textbf{262,785} never-smokers in the
China Kadoorie Biobank to \textbf{2,646} incident lung cancers and assigned annual PM$_{2.5}$ constituents
from a satellite/ML reanalysis, 2004--2018. Per IQR: nitrate \textbf{HR 1.35} (1.23--1.48), ammonium
\textbf{1.22} (1.13--1.31), chloride \textbf{1.20} (1.12--1.28); the quantile g-computation mixture gives
\textbf{1.13} (1.07--1.19), with NO$_3^-$ and NH$_4^+$ the dominant contributors and an additive and
multiplicative NO$_3^-\times$PRS interaction. \textbf{Caveat:} nitrate and ammonium are strongly collinear
in any reanalysis product and are partly inherited from the total-mass predictors, so ``nitrate drives the
risk'' may be ``the best-resolved component wins''.
\textbf{Why it matters for sensing:} ammonium nitrate is semi-volatile. It evaporates in a heated inlet and
in the warm optical cavity of a low-cost node, which is why nephelometric sensors under-read exactly the
fraction this cohort implicates --- and why a composition-blind network cannot stratify the exposure that
carries the effect."""

CHANGED = [
r"""\textbf{Marine PM$_{2.5}$ by extrapolation.} XGBoost on AOD, meteorology and NO$_2$/CO/O$_3$/SO$_2$ gives
2019--2024 PM$_{2.5}$ fields over the eastern China seas, falling west-to-east with Bohai Bay maxima and a
visible 2020 drop; SHAP puts AOD first in spring--autumn, meteorology in winter. There are almost no marine
ground monitors, so training and held-out validation both lean on coastal land sites --- open-water skill is
unverified, and no shipping-emission predictor enters the model.""",
r"""\textbf{Waterpipe caf\'es as occupational environments.} Five operating venues in Al-Madinah:
weekday PM$_{2.5}$ \textbf{285.5\,$\pm$\,149}\,$\mu$g\,m$^{-3}$, PM$_{10}$ \textbf{301.6\,$\pm$\,156},
weekend TVOC 0.50\,mg\,m$^{-3}$, formaldehyde below reference. A PM$_{2.5}$/PM$_{10}$ ratio near 0.95 is the
signature of pure combustion with no coarse fraction. Instrument and humidity correction unstated --- but a
factor-of-two optical bias still leaves these an order of magnitude above guideline.""",
r"""\textbf{A properly bounded null.} Two-sample MR of six pollutants against otitis media with effusion
(12,397 cases / 464,237 controls) finds nothing surviving FDR; the nominal PM$_{10}$ OR \textbf{1.56}
(0.95--2.55) reverses with the 88-SNP set. The authors report minimum detectable ORs of \textbf{1.69--32.1},
so moderate effects are not excluded --- and ambient-PM genetic instruments index residence and behaviour,
not exposure.""",
r"""\textbf{Cold-start particle number.} A 1.6\,L GDI engine with an electrically heated catalyst plus
secondary air over the first 80\,s of the cold WLTC cut THC 69.1\,\%, CO 65.7\,\% and NO$_x$ 80.6\,\% for
26.7\,Wh; PN rose sharply at $-7\,^\circ$C coolant but fell $>$30\,\% under coordinated control. PN is
reported only as a relative change --- no absolute count, size distribution or sub-23\,nm fraction, which is
where cold-start GDI particles sit and where optical nodes are blind."""
]

CONT = r"""The 2 October issue closed with \texttt{last\_entry\_date} at 2 October. This issue collects
\textbf{3 October in full}, continuous with it. \textbf{Five scheduled runs (4--8 October) harvested and
screened but did not author}, so dailies for 4--8 October and the W40 weekly (27 September--3 October) are
still owed and follow in this backfill. One admitted record (an \textit{ES\&T} in-vitro immunotoxicology
paper, \texttt{10.1021/acs.est.6c07515}) could not be written in this run and is held, not rejected; it
enters a later issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 14 in-scope records. \textbf{Seven of ten bands populated};
\textit{Other clinical}, \textit{Burden} and \textit{Sensing} carry \textbf{three} each, \textit{Mechanistic
toxicology} two, and one each for \textit{Reproductive}, \textit{Exposure assessment} and
\textit{Occupational \& indoor}. \textit{Cardiovascular}, \textit{Neuro} and \textit{Respiratory} are empty
--- the day's only respiratory-adjacent record is a never-smoker lung-cancer cohort, filed under other
clinical endpoints.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{four} records carry no abstract and assert no
design; \textit{modelling / inventory} and \textit{experimental / toxicology} hold \textbf{three} each (the
machine-learning marine surface, the aviation health-impact model and the Mendelian-randomisation analysis;
the mouse model and two in-vitro studies), with one each for the prospective cohort, the review, the indoor
measurement campaign and the engine bench. Right --- \textbf{eight} records report no health endpoint.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM or emissions \textbf{six} (the four
metadata-only deposits, the engine bench and the aviation burden), PM$_{2.5}$ only \textbf{five},
PM$_{2.5}$ + PM$_{10}$ jointly two (the waterpipe caf\'es and the MR analysis), PM$_{10}$ only one. The
constituent cohort is filed under PM$_{2.5}$; no record reports particle number or composition as its
primary metric. Right --- geography: China \textbf{five}, global / not stated \textbf{three}, East Asia
excluding China \textbf{three} (both Korean laboratory studies and the engine bench), and one each for
Europe, South Asia and the Middle East \& North Africa.""",
"f6_lifecourse": r"""Life-course windows: in utero one (the gestational mouse preeclampsia model), working
age one (the CKB never-smoker cohort, adult at baseline); childhood, adolescence and older adults have no
age-specific record. The in-utero entry is experimental, not a human birth cohort.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 14 records. The metadata-only block sits
across sensing and burden; toxicology concentrates in mechanistic and reproductive; the measurement and
modelling cells are each occupied once.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Five ratio estimates with 95\,\% CIs, log scale. The four hazard ratios are per-IQR constituent and
mixture effects from one cohort (China Kadoorie Biobank never-smokers) and share cases, so they are not
poolable with each other. The fifth is the two-sample MR odds ratio for PM$_{10}$ and otitis media with
effusion --- a different estimand on a genetic instrument, plotted for scale, and it crosses unity. The
aviation burden estimate is a death count, not a ratio, and does not enter the panel.}"""

PROV = r"""Entry window \textbf{3 October 2026}, single day, continuous with the 2 October issue. Harvest and
screening for this day were completed on the \textbf{6 October} run and cached
(\texttt{cache/2026-10-03/\_fresh.json}); this run authored from that cache without re-querying, so the
per-source counts are as logged then: \textbf{PubMed}, \textbf{Europe PMC}, \textbf{Crossref by ISSN} and
the \textbf{PubMed connector} (\texttt{[EDAT]} 3--5 October, 17 PMIDs merged across three days) contributing
\textbf{60} fresh candidates after cross-day deduplication; \textbf{OpenAlex} HTTP 429; \textbf{arXiv} no
entry dated 3 October. \textbf{14 admitted}, \textbf{45 rejected} with logged reasons, \textbf{1 held} to a
later issue. \textbf{Four records carried on metadata alone} (29\,\%, a series high) --- all four are
Elsevier or Wiley deposits with no abstract, and the abstract-retry leg recovered none of them.
\textbf{Consensus} returned 10 calibration hits, \textbf{0 new}. \textbf{Scholar Gateway} fails with
\texttt{ACCESS\_DENIED} and has now been unavailable for eleven days. \textbf{ClinicalTrials.gov}:
EPIC-AIR (\texttt{NCT07500948}, Leicester, $n$=80, real-time PM$_{2.5}$/PM$_{10}$/NO$_2$ guidance in cardiac
and pulmonary rehabilitation) is new in the window and enters the trial watch. DOI gate: \textbf{0 fail,
0 warn}. Abstracts remain the copyright of their respective publishers."""
