# -*- coding: utf-8 -*-
HEAD = dict(long="18 October 2026", window="18 October 2026 (full day)", n=13, excl=15,
            bands=8, eff=5, tierA=2, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Sham-controlled HEPA filtration moves IL-1$\beta$ only in people with excess
visceral fat --- a 22.8\,\% reduction in 12 of 116 participants, and nothing on average.}\\[1.4mm]
\footnotesize
Pragmatic randomised crossover: 30 days HEPA vs 30 days sham with a 30-day washout, 116 adults (mean age 41.5),
ultra-sensitive cytokine assays. No overall difference in IL-1$\beta$; visceral adiposity (ABSI $z \geq +0.229$)
moderated the effect (interaction $p$=0.001), with IL-1$\beta$ \textbf{0.138 vs 0.179}\,pg\,mL$^{-1}$ under HEPA vs sham
in the excess-VAT group. IL-6 followed the same direction without significance; hsCRP barely moved; BMI was a weaker
moderator than ABSI.
\textbf{Where it is weak:} $n$=12 in the responsive stratum, chosen among several adiposity indices, and the indoor
PM$_{2.5}$ reduction actually achieved is not reported in the abstract.
\textbf{Why it matters here:} in filtration trials the dose is the measured indoor PM difference; calibrated
low-cost monitors in both arms are what turn a null-on-average trial into an exposure--response analysis."""

CHANGED = [
r"""\textbf{Secondary inorganic PM$_{2.5}$ and the cardiorenal trajectory.} Cohort $n$=307,639: per-IQR HRs for
eGFR category 2$\to$3 of \textbf{1.27} (sulfate), \textbf{1.30} (nitrate), \textbf{1.28} (ammonium), all with CIs
$\pm$0.02 --- precision that points to spatial confounding as much as toxicity.""",
r"""\textbf{An equatorial Plantower co-location.} Jambi, Indonesia, two months against a BAM-1020: PMS7003 R$^2$
0.59, MBE \textbf{+10.5}\,$\mu$g\,m$^{-3}$, RMSE 18.0; PMS5003 R$^2$ 0.60, MBE +11.8 (Consensus sweep).""",
r"""\textbf{Wood smoke sits below optical detection.} Phase-resolved stove emissions peak at \textbf{$\sim$0.1\,$\mu$m}
with PM$_1$ 70--89\,\% of mass; spruce gives an HMW-PAH burst at ignition.""",
r"""\textbf{UFP from mass inventories.} A mass- and number-conserving conversion reproduces total particle number
over Greater Paris at background and traffic sites; non-exhaust traffic is about a third of traffic PN.""",
]

CONT = r"""The 17 October issue (built on the same run) closed with \texttt{last\_entry\_date} at 17 October. This
issue collects \textbf{18 October in full}, continuous with it. Built on the 19 October run at 18:5x CDT; 19 October
is not opened (before 22:00) and is due on the next run at or after 22:00 CDT."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 13 in-scope records across eight bands, none with more than two
records. Cardiovascular holds both tier-A records (HEPA trial, cardiorenal components); reproductive and
mechanism bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: one RCT, one cohort, two reviews, two cross-sectional, one sensor
co-location; metadata-only 1 (8\,\%). Right --- endpoints: cytokines, kidney-function transitions, asthma morbidity,
sinonasal scores, brain immune influx, small airway function, antibiotic resistance.""",
"f3_metric_geography": r"""Left --- particle metric: size-resolved records (Paris PN, stove impactor) join PM$_{2.5}$
mass. Right --- geography: global, not-applicable and not-stated records (6) lead; Europe and North America 2 each;
Indonesia, China and the Asian SDS review one each.""",
"f6_lifecourse": r"""Life-course windows: childhood only through the metadata-only school-microenvironment record;
working age carries the HEPA adults, cement workers and CF adults. Preconception, adolescent and older-adult
windows are empty.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. No cell exceeds one record: the issue is broad and
shallow.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale: three per-IQR HRs for the eGFR category 2$\to$3 transition from one cohort (sulfate, nitrate,
ammonium; collinear, single-component models), and two prevalence-rate ratios for genotypic antibiotic resistance
against country-level PM$_{2.5}$ from an ecological analysis of 397,103 isolates. The ecological RRs carry no
causal weight.}\end{minipage}"""

PROV = r"""Entry window \textbf{18 October 2026}, single day (Sunday). Harvester legs: \textbf{PubMed} health
\textbf{10}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{0} (weekend index lag); \textbf{Crossref by ISSN}
\textbf{10}; \textbf{arXiv} no entry dated 18 October; \textbf{OpenAlex} HTTP 429. 20 unique, 0 already carried.
\textbf{PubMed connector} (EDAT 17--18 Oct) 7 appended --- \textbf{27} candidates screened, \textbf{12 admitted},
\textbf{15 rejected} (one an exact duplicate of a 17 October admission) with logged reasons. \textbf{Consensus}
calibration sweep: 10 hits, \textbf{1 new} (Jambi co-location, DOI by Crossref title match) added here, for
\textbf{13} records. \textbf{DOI gate} 0 fail / 0 warn. \textbf{Trial watch}: 0 registrations updated 16--19
October. Abstracts recovered via PubMed and Europe PMC for 12 of 13; \textbf{1 record carried on metadata alone}.
\textbf{Scholar Gateway} not called. Abstracts remain the copyright of their publishers."""
