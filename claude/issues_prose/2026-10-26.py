# -*- coding: utf-8 -*-
HEAD = dict(long="26 October 2026", window="26 October 2026 (full day)", n=24, excl=56,
            bands=9, eff=8, tierA=4, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}US Medicaid, 893,212 mother--child pairs: prenatal wildfire-smoke
PM$_{2.5}$ tracks autism, not ADHD, and the window is mid-to-late gestation.}\\[1.4mm]
\footnotesize
Weekly smoke-attributable PM$_{2.5}$ at 1\,km, aggregated to the residential ZIP code across pregnancy; Cox models with
distributed-lag nonlinear terms; 8,357 ASD and 22,302 ADHD diagnoses (claims algorithms). Per IQR (0.75\,$\mu$g\,m$^{-3}$)
of cumulative smoke PM$_{2.5}$: ASD HR \textbf{1.30} (1.07--1.59); ADHD HR \textbf{1.03} (0.91--1.17).
\textbf{Where it is weak:} a 30\,\% hazard increase per 0.75\,$\mu$g\,m$^{-3}$ is very steep for a ZIP-level smoke
fraction; smoke years and regions coincide with secular and regional shifts in ASD coding, and claims-based diagnosis in
Medicaid depends on access to services.
\textbf{Why it matters here:} the contrast is sub-microgram and source-specific. Smoke fractions at that resolution are
where dense sensor networks, not 1\,km model fields, decide the exposure ranking."""

CHANGED = [
r"""\textbf{Low-contrast lung deficit.} COPSAC (Denmark, $n$\,=\,846): per 2.2\,$\mu$g\,m$^{-3}$ postnatal PM$_{2.5}$,
FEV$_1$ at age 6 $-$2.70\,\% ($-$4.27 to $-$1.10) and sRaw +7.30\,\% (1.87--13.07), persisting through age 18 in an
asthma-enriched cohort.""",
r"""\textbf{Chamber crossover on cognition.} 90 adults, candle PM$_{2.5}$ 31.2 vs 1.7\,$\mu$g\,m$^{-3}$ (sham vs real
purifier filter): lower HRV, worse attention and memory; HRV partly mediates. Candle smoke is not PM alone.""",
r"""\textbf{Non-monotone haematology signal.} REDIAL ($n$\,=\,2,125): induction PM$_{2.5}$ and positive MRD in B-ALL,
Q2 aOR 1.56, Q3 1.51, Q4 null --- not a dose--response.""",
r"""\textbf{Background vs increment.} Wavelet-based PM$_{2.5}$ background for India from MERRA-2; agreement with GMM-HMM
backgrounds MAD 2.2--10.8\,$\mu$g\,m$^{-3}$, RMSE 29.5 across the Delhi network.""",
r"""\textbf{Siting by expert weights.} Pythagorean-fuzzy MCDM ranks five PM$_{2.5}$ station sites in Trabzon --- no
coverage or representativeness objective is tested.""",
r"""\textbf{Mass is not hazard.} Chiang Mai haze: the lowest-mass rural site had a higher metal hazard index (2.10) than
the urban site (1.34); Cr dominates every risk estimate.""",
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. Scheduled runs for 23--29 October did
not complete: a run at 00:21 UTC on 30 October harvested 23--28 October but stopped before screening. This issue was
built on the \textbf{30 October 2026 14:20 UTC (09:20 CDT) recovery run}, which backfills 23--29 October day by day; it collects
\textbf{26 October in full} (Monday), continuous with the 25 October issue. The W43 weekly (18--24 October) is filed
under 24 October on the same run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 24 in-scope records across nine bands. Exposure assessment leads with eight
(two PMF source apportionments, two composition/metal-risk campaigns, background estimation, fog-haze deep learning, a
plume screening model, a dust event); burden \& policy is the only empty band.""",
"f2_design_endpoint": r"""Left --- architecture: cohorts lead (Medicaid wildfire, COPSAC, REDIAL, IVF, lung surgery),
then composition and source-apportionment campaigns, modelling, reviews and mechanistic work, with one randomised
crossover; \textbf{metadata-only 3 (13\,\%)}. Right --- endpoints run from ASD, lung function and MRD to IVF outcomes,
hypertension classification and respirator protection factors.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ dominates; PM-bound metals, respirable grain dust and
dust-event coarse mass add the speciated and coarse tail. Right --- geography: China and the USA lead; Europe (Denmark,
Poland, multi-country), South Korea, Thailand, India, Turkiye and Australia each contribute; two global reviews/panels.""",
"f6_lifecourse": r"""Life-course windows: in utero (wildfire ASD, IVF folliculogenesis), childhood (COPSAC, ALL, a
neurodevelopment review), adolescence (COPSAC to 18), working age (chamber crossover, farm respirators, AusDiab) and
older adults (AusDiab, lung-cancer surgery).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Health bands sit in cohorts and the crossover; exposure assessment
spreads across composition campaigns, source apportionment and modelling; sensing has a single siting record.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, five estimates from three studies: prenatal wildfire PM$_{2.5}$ per IQR (0.75\,$\mu$g\,m$^{-3}$) and
ASD/ADHD (US Medicaid); induction PM$_{2.5}$ quartiles Q2 and Q3 vs Q1 and positive MRD in B-ALL (REDIAL); PM$_{2.5}$ per
10\,$\mu$g\,m$^{-3}$ before oocyte retrieval and live birth after IVF (Chengdu). Contrasts and endpoints differ. Not
poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale (\% change): COPSAC FEV$_1$ and sRaw at age 6 per IQR (2.2\,$\mu$g\,m$^{-3}$) postnatal
PM$_{2.5}$; ecological gastric-cancer incidence per 1\,$\mu$g\,m$^{-3}$ national PM$_{2.5}$ (GBD, 204 countries).
The ecological estimate is population-level and not comparable with the cohort estimates.}\end{minipage}"""

PROV = r"""Entry window \textbf{26 October 2026}, single day (Monday). Harvester legs (run 00:21 UTC 30 Oct): \textbf{PubMed}
health \textbf{19}, sensing \textbf{2}; \textbf{Europe PMC} \textbf{10}; \textbf{Crossref by ISSN} \textbf{45};
\textbf{arXiv} 1 in-window entry (off-topic); \textbf{OpenAlex} 0 (HTTP 429). 74 fresh after cross-source dedupe; PubMed
connector (EDAT 23--28 Oct, bucketed by entrez date) 23 records for 26 October, 6 appended, \textbf{80 screened}.
Abstract retry (efetch, Crossref, Semantic Scholar) left 3 records without abstracts. \textbf{24 admitted},
\textbf{56 rejected} with logged reasons. \textbf{DOI gate} 0 fail / 1 warn (Int J Fertil Steril DOI live at doi.org, not
in Crossref). \textbf{3 carried on metadata alone}. Consensus sweep and trial watch for 23--29 October are reported in
the 29 October issue. \textbf{Scholar Gateway} not called. Abstracts remain the copyright of their publishers."""
