# -*- coding: utf-8 -*-
HEAD = dict(long="21 October 2026", window="21 October 2026 (full day)", n=18, excl=86,
            bands=9, eff=5, tierA=3, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}26 million Medicare beneficiaries: atrial fibrillation tracks sulfate and
combustion PM$_{2.5}$, not biomass smoke or secondary organics.}\\[1.4mm]
\footnotesize
Source-apportioned PM$_{2.5}$ (Multilinear Engine on speciation-network data, inverse-distance weighted to ZIP code)
against 4.44 million incident AF cases over 171.6 million person-years, 2000--2019. Per IQR: secondary sulfate HR
\textbf{1.056} (1.053--1.058), heavy oil/coal combustion \textbf{1.048}, secondary nitrate 1.032, vehicle 1.029;
biomass burning and dust modest; SOA null nationally but positive in the West.
\textbf{Where it is weak:} source fields are interpolated from sparse speciation monitors over 100\,km, so source
contrasts are largely regional contrasts, and per-IQR scaling differs by source --- this is not a per-microgram
toxicity ranking. Claims-based AF misses paroxysmal disease.
\textbf{Why it matters here:} optical low-cost networks report mass. If composition carries the cardiac signal,
a dense mass network needs a sparse speciation backbone to be epidemiologically useful."""

CHANGED = [
r"""\textbf{Particle size matters for spirometry.} China Pulmonary Health Study, 50,991 adults: per IQR PM$_1$
FEV$_1$ \textbf{$-$36.8\,mL} ($-$45.9 to $-$27.8); large-airway decrements grow as size falls, while the coarse
fraction PM$_{2.5\text{--}10}$ gives the largest small-airway (FEF$_{25\text{--}75}$) decrements.""",
r"""\textbf{An outcome-weighted air index.} 1.21 million AMI cases, 325 cities: a composite Air Health Index
(PM$_{2.5}$, NO$_2$, O$_3$, temperature) gives +5.97\,\% per IQR vs +3.33\,\% for AQHI and +2.04\,\% for AQI ---
in-sample advantage expected, but externally validated.""",
r"""\textbf{Implausibly large cancer-prognosis HRs.} Cervical cancer, 3,758 women: PM$_{2.5}$ recurrence SHR
1.93, death HR 2.55 per IQR on 113 deaths --- read as confounding by referral geography until replicated.""",
r"""\textbf{Magnetite inventory.} Respirable magnetite from Chinese coal power: 2,829\,t\,y$^{-1}$; two provinces
with 4\,\% of output could cut $>$31\,\% of emissions by tightening standards.""",
r"""\textbf{PubMed was nearly silent.} Only 2 records carried a 21 October entry date in PubMed; Europe PMC and
the Crossref ISSN sweep carried the issue, and five ACS \emph{Environment \& Health} papers arrived via Europe PMC
with PMIDs assigned the next day.""",
]

CONT = r"""The 20 October issue closed with \texttt{last\_entry\_date} at 20 October. This issue collects
\textbf{21 October in full}, continuous with it. The scheduled run for 21 October (04:0x UTC 22 October) did not
fire; this run started 18:02 CDT on 22 October, before the 22:00 cut-off, so 22 October is \emph{not} opened and
is left to the next run at or after 22:00 CDT. The W43 weekly (18--24 October) is due Saturday 24 October."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 18 in-scope records across nine bands. Cardiovascular, other
clinical endpoints, exposure assessment and burden/mitigation hold three each; sensing two; neuro/mental health is
the only empty band.""",
"f2_design_endpoint": r"""Left --- architecture: four cohorts, four modelling/inventory records, one acute
time-series, one cross-sectional, one toxicology, one laboratory, one review; \textbf{metadata-only 5 (28\,\%)},
day-0 Elsevier and one ACS record. Right --- endpoints span AF, AMI, lipids, spirometry, frailty, cervical cancer
prognosis, HFMD and birthweight.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$-only 6, joint PM$_{2.5}$+PM$_{10}$ 4,
unspeciated/emissions 5, one composition record (sulfate), one optical (dust optical depth), one respirable dust.
Right --- geography: China 9 dominates; MENA 2; one each for the US, Southeast Asia, South Asia, Nigeria.""",
"f6_lifecourse": r"""Life-course windows: working age leads (spirometry, lipids, cervical cancer, silica, AMI);
three older-adult records (Medicare AF, CHARLS frailty, AMI); one in utero (folic acid, metadata only), one childhood
(HFMD); no adolescent record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Cardiovascular sits in cohorts and health-impact
modelling; exposure assessment and sensing fall mostly in metadata-only cells today, which limits what the
measurement side of this issue can assert.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale, four estimates from two studies: source-specific PM$_{2.5}$ (secondary sulfate, vehicle) and
incident AF per IQR in Medicare; PM$_{2.5}$ per IQR and cervical cancer recurrence (Fine--Gray SHR) and death in a
single-centre cohort. Per-IQR contrasts differ by source and study. Not poolable.}\end{minipage}

\vspace{3mm}

\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: FEV$_1$ change (mL) per IQR long-term PM$_1$, China Pulmonary Health Study
(n\,=\,50,991). Single estimate shown for scale; the coarse-fraction small-airway estimates are not given with
CIs in the abstract.}\end{minipage}"""

PROV = r"""Entry window \textbf{21 October 2026}, single day (Wednesday). Harvester legs: \textbf{PubMed} health
\textbf{2}, sensing \textbf{0} (connector EDAT query confirms 2 total --- indexing lull); \textbf{Europe PMC}
\textbf{53} (2 AGRICOLA dropped); \textbf{Crossref by ISSN} \textbf{61}; \textbf{arXiv} HTTP 429;
\textbf{OpenAlex} HTTP 429. 113 unique, 10 already carried, \textbf{103 fresh}; PubMed connector (EDAT 21 Oct)
2 PMIDs, 0 appended. Europe PMC records lacking DOI were resolved by Crossref title match (five returned
supplementary-file \texttt{.s001} DOIs, stripped and verified) and their abstracts recovered from PubMed by DOI.
\textbf{Consensus} calibration sweep: 10 hits, 1 candidate (Ginsburg 2026, PurpleAir global calibration) ---
\textbf{rejected by the DOI gate as already shipped 29 July}. \textbf{104} candidates screened, \textbf{18
admitted}, \textbf{86 rejected} with logged reasons. \textbf{DOI gate} 0 fail / 0 warn after the duplicate was
removed. \textbf{Trial watch} 21--22 October: 2 registrations updated (AIRWEIGHS purifier RCT NCT02763917, primary
completion passed; Taif COPD survey). \textbf{5 carried on metadata alone}. \textbf{Scholar Gateway} not called.
Abstracts remain the copyright of their publishers."""
