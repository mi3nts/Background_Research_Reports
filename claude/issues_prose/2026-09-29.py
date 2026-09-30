# -*- coding: utf-8 -*-
HEAD = dict(long="29 September 2026", window="29 September 2026 (full day)", n=22, excl=70,
            bands=8, eff=9, tierA=3, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Machine-learning calibration of low-cost particle
counters looks excellent under a random train/test split and near-useless under a chronological
one --- validation design, not algorithm, decides the reported R$^2$.}\\[1.4mm]
\footnotesize
Sahin and colleagues (\textit{Atmosphere}, tier A) co-located three low-cost OPCs with reference
nephelometers over \textbf{seven indoor runs} and fitted six calibrators, from MLR to LightGBM. Under a
conventional random 80/20 hold-out the tree ensembles reached \textbf{R$^2$ = 0.86--0.89}; under day-blocked
and run-blocked splits R$^2$ fell steeply, and under forward chaining and chronological hold-out it sat
\textbf{near or below zero}. Validation design explained \textbf{63--91\,\%} of the spread in R$^2$; algorithm
choice \textbf{3.6--10.6\,\%}. Calibration was still worth doing --- prospective RMSE fell \textbf{22--48\,\%} ---
but the calibrated slope was only \textbf{0.18--0.44}, so real variation was compressed.
\textbf{Why it is the signal:} random splits of autocorrelated 1-min series leak neighbouring
minutes into the test set, and much of the LCS calibration literature reports exactly that number.
The study is small (three sensors, $\sim$200\,h, PM$_1$ 8--9\,$\mu$g\,m$^{-3}$), so the magnitudes
will not transfer, but the ranking of error sources should. \textbf{The operational rule:} accept
no calibration skill figure that is not from a temporally blocked or prospective hold-out, and report
slope alongside RMSE."""

CHANGED = [
r"""\textbf{Prenatal PM$_{2.5}$ and autism in 1.55 million Medicaid pairs} (\textit{ES\&T}, tier A): HR
\textbf{1.17} (1.00--1.37) per 10\,$\mu$g\,m$^{-3}$ cumulative prenatal exposure, with a window at
gestational weeks \textbf{23--31} (HR 1.09, 1.02--1.17). The lower bound sits on the null and exposure is
ZIP-code level.""",
r"""\textbf{Two UK Biobank papers disagree on stroke.} Jin et al.\ report HR \textbf{1.29} (1.15--1.45) per
5\,$\mu$g\,m$^{-3}$ for incident ischaemic stroke; Wang et al., in 149,410 participants of the same
cohort, find no pollutant associated with stroke but heart-failure HR \textbf{1.045} (1.005--1.086) per
IQR, with a 20-year absolute risk difference of $\sim$\textbf{0.2 per 100}.""",
r"""\textbf{Greenness bends the OHCA slope} (62,915 cases, tier A): per 0.1 NDVI the PM$_{2.5}$ effect on
out-of-hospital cardiac arrest odds falls by \textbf{1.62} percentage points per 10\,$\mu$g\,m$^{-3}$.
An instrumental-variable study using thermal inversions puts PM$_{2.5}$--suicide at \textbf{0.66 deaths
per million} per $\mu$g\,m$^{-3}$ in South Korea --- the inversion also traps other pollutants.""",
r"""\textbf{Composition over mass.} Open waste burning emits \textit{p}-phenylenediamine antioxidants at
a median \textbf{11.5\,$\mu$g\,g$^{-1}$ PM$_{2.5}$} and carries $>$99.7\,\% of China's estimated waste-burning
PPD emissions --- a quinone hazard no mass sensor sees. A coarse-particle classifier for a bioaerosol
spectrometer shows where fluorescence alone mislabels smoke and dust.""",
r"""\textbf{Three metadata-only records}, led by an \textit{Atmos Environ} test of a \textbf{virtual
ultrafine-particle limit value} on German network data --- the paper most relevant to UFP counting
sensors this week, first on the retry list. An \textit{expression of concern} on an earlier
\textit{Reprod Toxicol} PM$_{2.5}$--pregnancy cohort was logged, not admitted.""",
]

CONT = r"""The 28 September issue (built on the 29 September backfill run) closed with
\texttt{last\_entry\_date} at 28 September. This issue collects \textbf{29 September in full},
continuous with it. The run started at 23:06 CDT on 29 September, after the 22:00 cut, so the day
is complete. \textbf{30 September} and the \textbf{September monthly} fall to the next run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 22 in-scope records. \textbf{Eight of ten bands
populated}; \textit{Exposure assessment} and \textit{Cardiovascular \& metabolic} lead with
\textbf{five} each. \textit{Mechanistic toxicology} and \textit{Other clinical} are empty.""",
"f2_design_endpoint": r"""Left --- architecture: observational cohort \textbf{seven}, measurement
campaigns, modelling and metadata-only \textbf{three} each, reviews and ecological two each, one
acute (case-crossover) and one laboratory. Right --- endpoint distribution for the same 22 records;
\textbf{ten} carry no health endpoint (instrument, exposure, emissions and missing-abstract records); reproductive and cardiovascular take three each.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{eight}, PM$_{2.5}$ +
PM$_{10}$ \textbf{six}, unspeciated / emissions five, and one each for PM$_{10}$ only, coarse bioaerosol
and optical absorption. Right --- geography: China \textbf{seven}, Europe \textbf{five} (UK, Belgium,
Germany, Svalbard, and the CHARLS--UK Biobank pair), global / not stated five, South Asia and North
America two each, South Korea one.""",
"f6_lifecourse": r"""Life-course windows: in utero four (pregnancy loss, pulmonary-hypertension
pregnancies, twins, the ASD window), childhood and adolescence one each, working age none, older
adults two (OHCA $\geq$65 subgroup, elderly suicide).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 22 records. Cohorts concentrate in
\textit{Cardiovascular} and \textit{Reproductive}; the measurement side is split across campaigns,
laboratory work and a review.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Nine ratio estimates with 95\,\% CIs from six records, on a log scale. \textbf{Increments
differ} (per 5, per 10, per IQR, and unstated for the two pregnancy-loss and the CHARLS estimates), so
the panel shows direction and precision, not a poolable effect. The adolescent-asthma row is a fuel
contrast with no PM measurement. The widest interval is the pregnancy-loss PM$_{2.5}$ OR, driven by
106 events.}"""

PROV = r"""Entry window \textbf{29 September 2026}, single day, continuous with the 28 September issue.
Harvester legs run leg-by-leg: \textbf{PubMed} health \textbf{17}, sensing \textbf{4}; \textbf{Europe PMC}
\textbf{3} (low; creation-date indexing for the day may still be filling); \textbf{Crossref by ISSN}
\textbf{71}; \textbf{arXiv} no entry dated 29 September; \textbf{OpenAlex} HTTP 429. 95 raw deduplicated to
\textbf{91}, \textbf{2} already carried, \textbf{89} fresh; the \textbf{PubMed connector} (\texttt{[EDAT]}
29 September, health and sensing axes) returned 15 PMIDs, 14 dated to this day, \textbf{3 appended}.
\textbf{92} candidates screened, \textbf{22 admitted}, \textbf{70 rejected} with logged reasons (PFAS and
water chemistry from \textit{ES\&T}, \textit{Measurement Science and Technology} engineering,
meteorology from \textit{Atmosphere}, and gas-phase-only records under standing precedent).
\textbf{Consensus} returned 10 calibration hits, \textbf{0 new} (the one 2026 paper, Kumpika et al., was
screened out earlier). \textbf{ClinicalTrials.gov}: one update (HAPIN, NCT02944682), already tracked.
\textbf{Three records carried on metadata alone}. DOI gate: \textbf{0 fail, 1 warn} (the
\textit{Neonatology} DOI resolves at doi.org but is not yet in Crossref). Abstracts remain the
copyright of their respective publishers."""
