# -*- coding: utf-8 -*-
HEAD = dict(long="10 October 2026", window="10 October 2026 (full day)", n=9, excl=35,
            bands=4, eff=0, tierA=1, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Sixty-six studies, ten years: low-cost PM sensors reach a
median calibrated R$^2$ of 0.92 on the bench and 0.72 in the field, and median RMSE rises from
2.6 to 12.3\,$\mu$g\,m$^{-3}$ on the same crossing.}\\[1.4mm]
\footnotesize
A critical review of 66 peer-reviewed studies published 2015--2025 --- 32 laboratory evaluations and 34
field deployments --- puts numbers on the gap this watch keeps circling. Median calibrated R$^2$ was
\textbf{0.92} ($n$ = 31) in the laboratory against \textbf{0.72} ($n$ = 29) in the field; median RMSE
\textbf{2.6\,$\mu$g\,m$^{-3}$} ($n$ = 7) against \textbf{12.3\,$\mu$g\,m$^{-3}$} ($n$ = 9). The authors
are careful that these summarise a heterogeneous literature rather than estimate a pooled effect: aerosol
mixture, reference instrument, concentration range, averaging interval and validation design all differ
between studies, and only 7 and 9 of the 66 reported RMSE at all.
\textbf{Why it matters:} the review's conclusion is the operative one --- calibration is not a correction
applied once and carried unchanged into a new deployment. Machine-learning and hybrid models appear more
often in field work and sometimes lower error, but independent validation across \textit{time, place and
sensor unit} is uneven, which is precisely the validation that a network, as opposed to a study, requires."""

CHANGED = [
r"""\textbf{The error figures rest on a thin subset.} Of 66 studies, \textbf{31} reported a calibrated
R$^2$ and only \textbf{7} (laboratory) and \textbf{9} (field) reported RMSE. A median over nine field
RMSEs is a weak estimate of what a network should expect, and the studies that report error at all are
plausibly the ones that found it acceptable.""",
r"""\textbf{Microplastics travel with the resuspended mixture.} Two seasonal campaigns in central Los
Angeles found airborne microplastics in every sample (2.2--4.0\,MP\,m$^{-3}$ cool season,
2.2--3.4 warm), fibre-dominated and concentrated in the 5--50 and 50--100\,$\mu$m fractions, correlating
at $\rho \ge 0.79$ with crustal, traffic and carbonaceous tracers while showing no consistent relationship
with short-term meteorology. The inhalable fraction below 5\,$\mu$m is not resolved.""",
r"""\textbf{A policy reform with emissions down and ambient flat.} Kazakhstan's 2021 Environmental Code cut
reported stationary-source emissions by \textbf{5--6\,\%} between 2021 and 2024, yet no statistically
significant improvement in ambient indicators appeared through 2025 and episodic exceedances persisted.
With no control region, the null is as much a property of the design --- and of a network too sparse to
detect a 5\,\% change --- as of the policy.""",
r"""\textbf{Trends that are mostly weather.} Eight years of Indian in-situ data give falling PM at several
Indo-Gangetic sites (Sen's slope $-0.893$ to $-0.097\,\mu$g\,m$^{-3}$ per month for PM$_{2.5}$), rising
ozone (0.041 to 0.529), and rising Punjab. The paper's own finding --- declining boundary-layer height and
wind speed modulate all of it --- is the reason those slopes are not emission trends.""",
]

CONT = r"""The 9 October issue closed with \texttt{last\_entry\_date} at 9 October. This issue collects
\textbf{10 October in full}, continuous with it; the 11 October issue follows on this run, and the
\textbf{W41 weekly} (4--10 October) is filed under this date. Two PubMed-connector records dated 10 October
by entry date also surfaced in the 11 October PubMed query and were rejected there as duplicates of this
issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 9 in-scope records --- a thin Saturday, the smallest issue
since 4 October. \textbf{Four of ten bands populated}: \textit{Exposure assessment} and \textit{Burden}
three each, \textit{Sensing} two, \textit{Reproductive} one. The six empty bands include every clinical
band except reproductive, which is what a day with one health-endpoint record looks like.""",
"f2_design_endpoint": r"""Left --- architecture: three measurement campaigns, \textbf{three}
metadata-only records (33\,\%), two modelling / inventory records and one review / synthesis (the sensor
calibration review, the day's only tier-A record). Right --- a single record reports a health endpoint
(lung cancer burden, modelled rather than observed); one more asserts one by title only. Everything else
reports concentrations, composition, model skill or measurement performance.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated PM or emissions \textbf{three},
PM$_{2.5}$ only three, and one each of PM$_{10}$ only, PM$_{2.5}$ + PM$_{10}$ jointly, and optical
properties. Right --- geography: North America \textbf{two} (the Los Angeles microplastics campaign and
the China--US burden comparison), Europe two, and one each for China, South Asia, Central Asia,
sub-Saharan Africa and global --- the widest geographic spread per record of the backfill, on the fewest
records.""",
"f6_lifecourse": r"""Life-course windows: one record only, in preconception / in utero (the nationwide
maternal PM$_{2.5}$ and macrosomia study, carried on metadata alone). Childhood, adolescence, working age
and older adults have no age-specific record this issue --- the lung-cancer burden projection spans all
ages and is not assigned to a window.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 9 records. With nine records across four
subtopics and five architectures, no cell holds more than two; the matrix is nearly diagonal, which is
what a thin and heterogeneous day looks like rather than any structure in the field.""",
}

FOREST = r"""{\fontsize{7.4}{9}\selectfont\color{Slate}\textbf{No forest plot this issue.} No admitted
record reports a PM effect estimate with a confidence interval. The calibration review's headline
quantities are measurement-performance statistics (median R$^2$ and RMSE across studies), not effect
estimates, and pooling them would misrepresent a literature its own authors decline to pool; the lung
cancer projection reports burden rather than an exposure-response estimate. The f5 panel is absent by
design, not by build failure.\par}"""

PROV = r"""Entry window \textbf{10 October 2026}, single day, continuous with the 9 October issue.
Harvester legs: \textbf{PubMed} health \textbf{1}, sensing \textbf{0} --- the thinnest PubMed day of the
series, a Saturday entry date; \textbf{Europe PMC} \textbf{20} (8 after the retro-index gate dropped 12);
\textbf{Crossref by ISSN} \textbf{32}; \textbf{arXiv} returned no entry dated 10 October;
\textbf{OpenAlex} HTTP 429. 41 raw records, no cross-source duplicates, \textbf{41} fresh. The
\textbf{PubMed connector} (\texttt{[EDAT]} 9--11 October) returned 9 PMIDs dated 10 October, 5 already
carried and \textbf{3} appended --- \textbf{44} candidates screened, \textbf{9 admitted}, \textbf{35
rejected} with logged reasons. \textbf{Three records carried on metadata alone} (33\,\%); the
abstract-retry chain recovered \textbf{3 of 7} attempted, all three via PubMed, and none of the Elsevier
or Springer deposits. \textbf{Consensus} returned 10 calibration hits, \textbf{0 new} --- all pre-date the
window and several are cited by the calibration review admitted here. \textbf{Scholar Gateway} fails with
\texttt{ACCESS\_DENIED}. \textbf{ClinicalTrials.gov}: one new registration in the 4--11 October window
(EPIC-AIR, NCT07500948), reported in the W41 weekly. Abstracts remain the copyright of their respective
publishers."""
