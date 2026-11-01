# -*- coding: utf-8 -*-
HEAD = dict(long="30 October 2026", window="30 October 2026 (full day)", n=24, excl=67,
            bands=9, eff=3, tierA=1, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}All of Us, 179,218 adults, preregistered: heat anomaly and social
vulnerability predict incident depression; 30-day wildfire-smoke PM$_{2.5}$ does not --- at 3-digit-ZIP resolution.}\\[1.4mm]
\footnotesize
Cox models on 5,484 first EHR-recorded depression diagnoses (mean follow-up 371 days). Heat anomaly HR 1.06 (1.03--1.10)
and 1.08 (1.04--1.11) per SD; social-material vulnerability HR 1.36 (1.33--1.40) per SD. Mean smoke PM$_{2.5}$ (Stanford
ECHO): no association in the primary model; secondary smoke metrics heterogeneous by metric and follow-up window.
\textbf{Where it is weak:} exposure is a ZIP3 average frozen at baseline --- smoke episodes are short and spatially
patchy, so this is the textbook setting for attenuation to the null. A preregistered null is still a null on a
heavily smoothed exposure, not evidence of no effect.
\textbf{Why it matters here:} the contrast between a clean heat signal and a flat smoke signal is what residence-scale,
humidity-corrected sensor PM$_{2.5}$ would test directly."""

CHANGED = [
r"""\textbf{Low-cost sensors as the reference.} A MethodsX protocol measures air-cleaner CADR from PM$_{2.5}$ decay on
low-cost sensors in a real home: $\sim$26\,\% below lab values from research-grade instruments --- conservative, and
quantified. A four-filter Corsi--Rosenthal box led the DIY builds.""",
r"""\textbf{Hygroscopicity is source-dependent.} Eastern China, humidified nephelometry: $\kappa_{\rm OA}$ 0--0.49
(mean 0.11), tracking biomass-burning influence rather than O:C. A fixed-$\kappa$ humidity correction is wrong during
smoke. Separately, Kelvin-suppressed growth of 15--36\,nm particles changes modelled lung deposition by up to 25\,\%.""",
r"""\textbf{Policy co-benefit, modelled.} China's 2017 climate-adaptive city pilot: PM$_{2.5}$ $-$3.87\,$\mu$g\,m$^{-3}$
($-$6.49 to $-$1.25) by difference-in-differences, $\sim$8\,\% lower GEMM burden --- shrinking in the matched sample.""",
r"""\textbf{Prenatal exposure, small signals.} TTN in Taiwan: PM$_{2.5}$ aOR 1.001 (1.000--1.002) per unit, dominated by
CO; ECHO cord-blood methylation classifies high PM$_{2.5}$ exposure with AUC only 0.64--0.68.""",
r"""\textbf{Five metadata-only records (21\,\%)}, two of them squarely in scope for sensing: PN-PTI counters on gasoline
exhaust (\emph{J.\ Aerosol Sci.}) and e-cigarette aerosol decay. Retry first.""",
]

CONT = r"""The 29 October issue closed with \texttt{last\_entry\_date} at 29 October. A 31 October 05:33 UTC firing harvested
the PubMed and Europe PMC legs for 30 October and stopped. This issue was built on the \textbf{1 November 05:25 UTC
(00:25 CDT) run}; by the 22:00 rule the newest buildable day is 31 October, so the run backfills \textbf{30 October in
full} here and 31 October as its own issue, with the W44 weekly (25--31 October) and the October monthly. Candidates
were screened sequentially across the two days (cross-day DOI and title set built before authoring) to avoid the
double admissions of the 23--29 October backfill."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 24 in-scope records across nine bands; other clinical endpoints is empty.
Sensing and exposure assessment lead with five each, mechanistic toxicology four; reproductive, respiratory, burden and
occupational/indoor two each; neuro and cardiovascular one each.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{metadata-only 5 (21\,\%)}, four measurement campaigns, four
toxicology, three modelling, three cross-sectional, two cohort-type (All of Us, TTN case-cohort), two ecological and one
laboratory (HTDMA). Right --- endpoints span depression, TTN, cord-blood methylation, air-cleaner CADR,
hygroscopicity and new particle formation.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 10, unspeciated/emissions 6, size-resolved/number
3, optical 3, and one each joint PM$_{2.5}$+PM$_{10}$ and composition. Right --- geography: global/not stated 5, North
America 4, China 4, Europe 4, South Asia 3, and one each East Asia (Taiwan), Sub-Saharan Africa (Tanzania), Latin
America (Brazil) and Central Asia (Kazakhstan).""",
"f6_lifecourse": r"""Life-course windows: three in-utero/early-life records (TTN, ECHO cord blood, CHAMACOS prenatal
exposure), one childhood (Dar es Salaam school BP), one adolescent/young-adult (nasal EWAS), one working-age (All of Us
depression); no older-adult record today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Sensing splits between measurement, modelling and metadata
cells; mechanistic toxicology is all experimental; the health bands sit in cohort, cross-sectional and ecological
cells.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, one estimate: prenatal PM$_{2.5}$ and transient tachypnea of the newborn (aOR per unit
concentration, Taiwan, 3,091 cases). The CI touches 1; CO, not PM$_{2.5}$, carries the study.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale, one study (China, 264 cities): the climate-adaptive city pilot's PM$_{2.5}$ change
($\mu$g\,m$^{-3}$) and the GEMM-modelled burden change (\%). Different units; the second is derived from the first and
is not an independent estimate.}\end{minipage}"""

PROV = r"""Entry window \textbf{30 October 2026}, single day (Friday). Harvester legs: \textbf{PubMed} health
\textbf{16}, sensing \textbf{4}; \textbf{Europe PMC} \textbf{40} (9 AGRICOLA retro-index records dropped);
\textbf{Crossref by ISSN} \textbf{43}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. 95 unique,
10 already seen, 85 fresh; PubMed connector (EDAT 30--31 Oct, health and sensing axes separately) 27 PMIDs, 18 bucketed
to 30 Oct, 1 merged, \textbf{6 appended}, \textbf{91 screened}. Abstracts for 22 PubMed records recovered by efetch;
Crossref/Semantic Scholar recovered further abstracts, leaving 19 candidates abstract-free. \textbf{Consensus}
calibration sweep (once for 30--31 October): 10 hits, none new for this day. \textbf{24 admitted}, \textbf{67 rejected}
with logged reasons (5 were EPMC re-surfacings of 29 October rejections; 1 duplicate MethodsX record). \textbf{Trial
watch} 30 October--1 November: 0 registrations updated. \textbf{5 carried on metadata alone}. \textbf{Scholar Gateway}
not called. Abstracts remain the copyright of their publishers."""
