# -*- coding: utf-8 -*-
HEAD = dict(long="20 October 2026", window="20 October 2026 (full day)", n=19, excl=58,
            bands=8, eff=2, tierA=5, meta=6)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Four identical PM monitors breathing the same air disagree by up to a
factor of three day to day --- and averaging does not fix it.}\\[1.4mm]
\footnotesize
Four prototype electrostatic (corona-charging, impaction, Faraday-cup) PM$_{10}$/PM$_{2.5}$/PM$_{1.0}$ monitors ran
at one Thai combined-cycle power plant for four months with 92--100\,\% daily recovery. Fixed station differences
explained only \textbf{0.7\,\%} of log 24-h PM$_{10}$ variance; the day$\times$station interaction explained
\textbf{57.1\,\%}. Pairwise 95\,\% limits of agreement spanned ratios \textbf{0.35--3.26} (PM$_{10}$) and
0.33--2.83 (PM$_{2.5}$); single-unit ICC 0.42, rising to 0.75 only for the four-unit mean.
\textbf{Where it is weak:} preprint, no reference instrument, and no side-by-side co-location before deployment ---
unit drift and real micro-gradients are separated by inference, not measurement.
\textbf{Why it matters here:} the failure mode is generic to distributed networks. Station-to-station contrasts
from any low-cost array need scheduled co-location checks, or they support only pooled, time-averaged statements."""

CHANGED = [
r"""\textbf{Fire smoke and the kidney.} 12.5 million renal admissions, 1020 locations, six countries: per
10\,$\mu$g\,m$^{-3}$ fire-sourced PM$_{2.5}$ (lag 0--5) RR \textbf{1.011} (1.007--1.015), strongest for acute
kidney injury and larger than for non-fire PM$_{2.5}$.""",
r"""\textbf{An LCS protocol for pregnancy cohorts.} PRECISE (Gambia, Kenya, Mozambique): 343 women, 3,190
person-days of wearable PM$_{2.5}$, Deming-harmonised sensors with inter-sensor R$^2>$0.75 in country --- precision
reported, accuracy against reference not in the abstract.""",
r"""\textbf{AI inside the CTM, not after it.} ProNet embeds neural correctors in the transport equations; across
338 Chinese cities it beats forecaster-adjusted operational PM$_{2.5}$ guidance by 6.1\,\% and attributes errors to
processes.""",
r"""\textbf{Same emissions, more PM.} CAMS reanalysis: the Indo-Gangetic Plain emits 40\,\% less than the North
China Plain yet averages 123.6 vs 113.2\,$\mu$g\,m$^{-3}$, with winter `pollution-forming efficiency' nearly double
under a $<$300\,m boundary layer.""",
r"""\textbf{Held record released.} \emph{Foehn} (arXiv 2610.25941), the generative km-scale global PM$_{2.5}$
forecaster held from 19 October, now resolves at doi.org and enters this issue.""",
]

CONT = r"""The 19 October issue closed with \texttt{last\_entry\_date} at 19 October. This issue collects
\textbf{20 October in full}, continuous with it. Built on the run that started 23:0x CDT on 20 October (04:0x UTC
21 October), after the 22:00 cut-off, so the day is complete. 21 October is due on the next run at or after
22:00 CDT; the W43 weekly (18--24 October) on Saturday 24 October."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 19 in-scope records across eight bands. Exposure assessment (6) and
sensing/forecasting (5) lead --- a measurement-heavy day; cardiovascular and occupational hold two each;
neuro/mental health and mechanistic toxicology are empty.""",
"f2_design_endpoint": r"""Left --- architecture: modelling/inventory 5, measurement campaigns 3, two acute
(case-crossover, multi-location time-series), one ecological, one cross-sectional, one non-randomised intervention;
\textbf{metadata-only 6 (32\,\%)}, again day-0 Elsevier records. Right --- endpoints: renal admissions, coronary
dilatation, MACE, COPD prevalence, placental sncRNA, livestock productivity.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only records dominate (12); two size-resolved, two
optical-property (brown carbon, aerosol typing). Right --- geography: China 6, Southeast Asia 4 (Thailand,
Singapore), Europe 3, then sub-Saharan Africa, South Asia, Korea and the US border.""",
"f6_lifecourse": r"""Life-course windows: working age leads (two occupational campaigns plus the adult renal and
COPD records); two in utero (PRECISE, BiSC placenta), one childhood (Kawasaki); no adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment spreads across modelling and
metadata-only cells; sensing concentrates in modelling (forecasters) and measurement (electrostatic monitors).""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, two estimates on different contrasts: fire-sourced PM$_{2.5}$ and renal admissions per
10\,$\mu$g\,m$^{-3}$ over lag 0--5 (six countries), and PM$_{2.5}$ and coronary artery dilatation in Kawasaki disease
at lag 3, whose increment the abstract does not state. Not poolable.}\end{minipage}"""

PROV = r"""Entry window \textbf{20 October 2026}, single day (Tuesday). Harvester legs: \textbf{PubMed} health
\textbf{20}, sensing \textbf{4}; \textbf{Europe PMC} \textbf{3} (index lag; 0 AGRICOLA); \textbf{Crossref by ISSN}
\textbf{52} (2 ES\&T front-matter dropped); \textbf{arXiv} no entry dated 20 October; \textbf{OpenAlex} HTTP 429.
76 unique, 5 already carried, 71 fresh. \textbf{PubMed connector} (EDAT 20 Oct) 18 PMIDs, 5 appended ---
\textbf{76} candidates screened, \textbf{18 admitted}, \textbf{58 rejected} with logged reasons, plus \textbf{1 held}
record released (arXiv 2610.25941), giving \textbf{19}. \textbf{Consensus} calibration sweep: 10 hits, 0 new.
\textbf{DOI gate} 0 fail / 1 warn (arXiv DataCite DOI live at doi.org, not in Crossref). \textbf{Trial watch}:
0 registrations updated 20--21 October. Abstract retry (PubMed, Europe PMC, Semantic Scholar) left
\textbf{6 carried on metadata alone}. \textbf{Scholar Gateway} not called. Abstracts remain the copyright of their
publishers."""
