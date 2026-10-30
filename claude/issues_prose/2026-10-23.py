# -*- coding: utf-8 -*-
HEAD = dict(long="23 October 2026", window="23 October 2026 (full day)", n=24, excl=124,
            bands=8, eff=5, tierA=5, meta=3)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}96 paired comparisons: optical dust monitors read 36\,\% above
gravimetry, and site-specific calibration cuts that to 13\,\%.}\\[1.4mm]
\footnotesize
A PRISMA meta-analysis of 112 occupational studies pooled 96 real-time-monitor vs gravimetric pairs (DustTrak, SidePak,
pDR) in a three-level random-effects model. Pooled log response ratio \textbf{0.31} (0.25--0.37), $I^2$ 78\,\%, prediction
interval 0.11--0.63. Factory-calibrated units read 43\,\% high, site-calibrated units 13\,\%. Site calibration was the
strongest moderator ($\beta$ $-$0.24), then the log GSD of the size distribution ($\beta$ 0.15) and RH.
\textbf{Where it is weak:} geometric-mean ratios pooled over very different aerosols and campaign lengths; the
prediction interval says a single uncalibrated deployment can be off by 12--88\,\%.
\textbf{Why it matters here:} no eligible study tested sub-\$500 sensors against gravimetry. The moderators found for
professional photometers --- size distribution and humidity --- are the terms low-cost calibration models already
carry, and this gives them a pooled prior."""

CHANGED = [
r"""\textbf{Electret filters fail on soot, not clogging.} Residential HVAC electret filters lose efficiency through
soot-driven charge neutralisation at loadings far below any pressure-drop rise; modelled effective life during
wildfire smoke falls from months to days.""",
r"""\textbf{Cooking leads primary PM$_1$ emission in London and Beijing.} Eddy-covariance AMS fluxes: cooking up to 87\,\%
of early-evening primary PM$_1$ emission in London, 76\,\% in Beijing; traffic and combustion still lead in Delhi.
Cooking is absent from national and global inventories.""",
r"""\textbf{Size-resolved number carries the summer signal.} Beijing oxylipin panel ($n$\,=\,123): UFP associated with
+12.9 to +97.7\,\% oxylipin change per IQR in summer, $-$7.7 to +18.8\,\% in winter.""",
r"""\textbf{Randomised roadside crossover.} 51 young adults: per 10\,$\mu$g\,m$^{-3}$ PM$_{10}$, FEF$_{75}$
$-$0.215\,L\,s$^{-1}$; noise co-exposure appeared to amplify PM$_1$/PM$_{2.5}$ small-airway decrements (exploratory).""",
r"""\textbf{Cross-day resurfacing.} Three records indexed on 23 October reappeared in the 24 October Europe PMC and PubMed
legs; they are carried here, the first issue to see them.""",
r"""\textbf{Held record released.} \texttt{10.1021/acs.est.6c07515} (NK-cell dysfunction from respirable mining dust),
held unauthored from the 3 October issue, is now indexed in PubMed and carried here.""",
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. This issue collects
\textbf{23 October in full}, continuous with it. The scheduled runs for 23--29 October did not complete: a 30 October
00:21 UTC run harvested 23--28 October but stopped before screening. This issue was screened, authored and built on
the 30 October 2026 14:20 UTC (09:20 CDT) recovery run, which backfills 23--29 October day by day; the W43 weekly (18--24 October)
is built on the same run."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 24 in-scope records across eight bands. Exposure assessment leads with
seven (flux source attribution, receptor modelling, brown carbon, NPF simulation and three metadata-only records);
occupational/indoor four; sensing three. Cardiovascular and other clinical endpoints are empty.""",
"f2_design_endpoint": r"""Left --- architecture: two reviews, two field studies, one randomised crossover, one panel, one
case-control, one meta-analysis, modelling, in-vitro and burden records; \textbf{metadata-only 3 (13\,\%)}. Right ---
endpoints run from SGA and depression to lung function, oxylipins, cytokines and instrument bias.""",
"f3_metric_geography": r"""Left --- particle metric: mass (PM$_{2.5}$/PM$_{10}$) dominates; number-based UFP metrics appear
in four records (oxylipin panel, wood stoves, NPF field and model). Right --- geography: China leads; Europe (Spain,
Norway, UK) next; multi-region records are the meta-analysis, the three-megacity flux study, MR and GBD.""",
"f6_lifecourse": r"""Life-course windows: two in-utero/pregnancy records (IVF SGA; heat and air-quality review), one
childhood dose scenario (wood-stove UFP), five working-age records; no adolescent or older-adult record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Exposure assessment spreads across measurement, modelling and
metadata-only cells; sensing holds the meta-analysis, a long-term field campaign and a metadata-only estimator; the
health bands sit in the crossover, panel, case-control and MR cells.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, four estimates from two studies: PM$_{2.5}$ and small for gestational age in IVF pregnancies
(whole pregnancy, second and third trimester; Guangzhou matched case-control, increment not stated), and genetically
predicted PM$_{2.5}$ and major depression (two-sample MR preprint, unit not stated). Not poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: pooled log response ratio of optical real-time dust monitors vs gravimetric sampling
(96 pairs, three-level random effects; $I^2$ 78\,\%). A value of 0.31 corresponds to a 36\,\% positive bias.}\end{minipage}"""

PROV = r"""Entry window \textbf{23 October 2026}, single day (Friday). Harvester legs: \textbf{PubMed} health
\textbf{67}, sensing \textbf{10}; \textbf{Europe PMC} \textbf{40}; \textbf{Crossref by ISSN} \textbf{70};
\textbf{arXiv} 150 kB, 1 in-window entry (rejected); \textbf{OpenAlex} HTTP 429. 50 cross-source duplicates removed;
128 fresh; PubMed connector (EDAT 23 Oct) 64 PMIDs, 20 appended, \textbf{148 screened}. Abstract retry recovered none
of the three Elsevier metadata-only records. \textbf{24 admitted}, \textbf{124 rejected} with logged reasons.
\textbf{DOI gate} 1 warn (nursing review title overlap). \textbf{Consensus} sweep and \textbf{trial watch}: run once for
the 23--29 October backfill --- see the 29 October issue and the W43 weekly. \textbf{3 carried on metadata alone}.
\textbf{Scholar Gateway} not called. Abstracts remain the copyright of their publishers."""
