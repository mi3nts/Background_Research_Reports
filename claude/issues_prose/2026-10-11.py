# -*- coding: utf-8 -*-
HEAD = dict(long="11 October 2026", window="11 October 2026 (full day)", n=1, excl=11,
            bands=1, eff=2, tierA=0, meta=0)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A one-record Sunday. The single admitted paper puts
PM$_{2.5}$ against incident fatty liver disease at HR 1.19 (1.10--1.30) and claims a 700-protein signature
mediates 15\,\% of it --- with a confidence interval from 2.7\,\% to 37.7\,\%.}\\[1.4mm]
\footnotesize
52,190 participants free of metabolic dysfunction-associated steatotic liver disease at baseline, 624
incident cases over a median 11.8 years. Annual average PM$_{2.5}$ gave \textbf{HR 1.19} (1.10--1.30); an
elastic-net signature of \textbf{700} PM$_{2.5}$-associated proteins gave the same \textbf{1.19}
(1.08--1.31), enriched in NF-$\kappa$B signalling and cytokine--receptor interaction. Mendelian
randomisation supported CD28, CSF3 and HAVCR2 as causally associated with MASLD, and structural equation
modelling put the mediated fraction at \textbf{15\,\%} (2.7--37.7\,\%).
\textbf{Where it is weak:} a 700-protein signature trained and tested in one cohort absorbs variance from
everything PM$_{2.5}$ co-varies with, so 15\,\% is an upper bound on mediation rather than an estimate of
it, and the interval spans more than an order of magnitude. The MR arm establishes protein-to-disease
causality, not exposure-to-protein. Exposure itself is an annual mean read off an interpolated surface ---
the weakest link in the chain, and the one a measurement network addresses directly."""

CHANGED = [
r"""\textbf{A single-record day, and that is the finding.} Eleven candidates were screened, one admitted.
The rejected eleven are heatwave mortality, pesticide exposure, indoor radon, two records already carried
in the 10 October issue and six journal-sweep records with no PM content --- a Sunday entry date with one
PubMed health hit and no instrumentation deposits at all.""",
r"""\textbf{Two estimates, one cohort, one exposure.} The exposure HR and the protein-signature HR are not
independent findings: the signature is derived \textit{from} PM$_{2.5}$ in the same participants, so its
agreement with the exposure estimate is close to arithmetic rather than confirmatory.""",
r"""\textbf{Mediation reported as a point estimate, read as a range.} 15\,\% with a 2.7--37.7\,\%
interval is compatible with a trivially small mechanism and with a dominant one. The abstract's framing
--- that the signature ``mediated 15\,\%'' --- is the kind of precision this digest records but does not
repeat as a finding.""",
]

CONT = r"""The 10 October issue closed with \texttt{last\_entry\_date} at 10 October. This issue collects
\textbf{11 October in full}, continuous with it, and brings the watch current: the backlog that opened on
9 October is closed. The \textbf{W41 weekly} (4--10 October) is filed under 10 October. 12 October is not
opened --- under the 22:00 rule a run must not harvest the day it executes on before 22:00 local, and this
run began at 17:17 local."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the single in-scope record: \textit{Other clinical endpoints},
one of ten bands populated. This is the smallest issue in the history of the watch, below the previous
floor of four records (27 September, also a Sunday). A one-bar bar chart carries no distributional
information and is retained only so the issue's figure set is complete and comparable in the rollups.""",
"f2_design_endpoint": r"""Left --- architecture: one prospective cohort. Right --- one health endpoint,
incident metabolic dysfunction-associated steatotic liver disease. No metadata-only record this issue,
the first zero since 4 October.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only, as an annual mean from an
interpolated surface. Right --- geography: the cohort's country is not stated in the abstract, so the
record is assigned to global / multi-region rather than guessed at from cohort size or follow-up.""",
"f6_lifecourse": r"""Life-course windows: one record, working-age adulthood (mid-life enrolment, 11.8-year
follow-up to incident liver disease). Every other window is empty.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture: a single occupied cell. Shown for continuity with
the rest of the series and for the pooled rollups, where this issue contributes one cell of the week.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Two hazard ratios with 95\,\% CIs from one cohort, one exposure model and one set of 624 events.
They are not independent estimates: the protein signature is fitted to PM$_{2.5}$ in these same
participants, so its near-identical hazard ratio reflects how well the signature reproduces the exposure
variable, not a second line of evidence for the association. Reading the pair as mutual confirmation
would be a mistake; the panel is shown because the issue's only quantitative content is here.}"""

PROV = r"""Entry window \textbf{11 October 2026}, single day, continuous with the 10 October issue.
Harvester legs: \textbf{PubMed} health \textbf{9}, sensing \textbf{3}; \textbf{Europe PMC} \textbf{0} ---
no record created in the window, the first zero EPMC day since 25 September; \textbf{Crossref by ISSN}
\textbf{6}; \textbf{arXiv} no entry dated 11 October; \textbf{OpenAlex} HTTP 429. 18 raw records
deduplicated to \textbf{15}, 4 already carried, \textbf{11} fresh. The \textbf{PubMed connector}
(\texttt{[EDAT]} 9--11 October) returned 3 PMIDs dated 11 October, 1 appended --- \textbf{12} candidates
screened, \textbf{1 admitted}, \textbf{11 rejected} with logged reasons, two of them duplicates of records
already carried in the 10 October issue. \textbf{No record carried on metadata alone.} \textbf{Consensus}
returned 10 calibration hits, \textbf{0 new}. \textbf{Scholar Gateway} fails with \texttt{ACCESS\_DENIED}
and has done for the whole backfill; it is the designated route for recovering numbers that abstracts
omit, and it needs reconnecting at the user's end. \textbf{ClinicalTrials.gov}: the 4--11 October window
is reported in the W41 weekly. Abstracts remain the copyright of their respective publishers."""
