# -*- coding: utf-8 -*-
HEAD = dict(long="1 October 2026", window="1 October 2026 (full day)", n=30, excl=65,
            bands=9, eff=2, tierA=2, meta=6)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Bulk PM$_{2.5}$ oxidative potential understates the oxidative
burden of its own size fractions --- metal--organic complexation makes PM$_1$ and PM$_{1-2.5}$ antagonistic
when mixed.}\\[1.4mm]
\footnotesize
Liu and colleagues (\textit{ES\&T}, tier A) tested roadside PM$_1$ and PM$_{1-2.5}$ separately and mixed. Every
endpoint was sub-additive: interaction factor \textbf{0.65--0.81} for ascorbate OP, \textbf{0.80--0.93} for DTT
OP, \textbf{0.10--0.88} for cellular ROS and \textbf{0.43--0.78} for mitochondrial superoxide. Metal-free
biomass-burning PM was strictly additive; Cu$^{2+}$--humic-acid mixtures reproduced the antagonism (IF
0.22--0.95), and EPR showed complexed Cu forming non-linearly with the HA:Cu ratio --- which explains why
earlier studies disagree on whether size fractions add. \textbf{Caveats:} one roadside site, extract assays,
one model complex; whether lung lining fluid reproduces the complexation is untested. \textbf{Why it matters
for sensing:} OP is being proposed as the toxicity-weighted complement to mass. If bulk PM$_{2.5}$ OP is
not the sum of its parts, OP measured on a PM$_{2.5}$ filter cannot be read as dose; a size cut at 1\,$\mu$m
is the cheaper fix, and an optical counter's size bins are already there to stratify by."""

CHANGED = [
r"""\textbf{Coal retirements delayed, deaths priced} (medRxiv, tier A): 20 of 50 US coal plants due to retire
before 2035 now retire later or not at all; plant-attributable PM$_{2.5}$ over 2026--2035 adds
\textbf{1,256} Medicare deaths (1,136--1,376), \textbf{3.1$\times$} the original burden. Eighteen of the
20 sit in balancing authorities with hyperscale data-centre demand. The interval carries
concentration--response uncertainty only.""",
r"""\textbf{Metastatic prostate cancer} (33,384 men, 11 US registries): cardiovascular mortality HR
\textbf{1.04} (1.02--1.07) per IQR PM$_{2.5}$; \textbf{1.19} (1.05--1.34) high vs low PM$_{2.5}$ in
ADT-treated men. \textbf{ELSA} (12,235 adults 50+): PM$_{2.5}$ and PM$_{10}$ exceedance-day counts
\textbf{null} for 14-year cognitive decline once the annual mean is adjusted; NO$_2$ exceedance days were not.
\textbf{Crime, China} (483,718 events): every one of six pollutants positive on the day --- the pattern
shared confounding produces.""",
r"""\textbf{Urban greening is a weak PM sink.} Direct leaf sampling in Delhi puts urban-forest removal at
\textbf{527} t PM$_{2.5}$ a year, \textbf{1.08\,\%} of emissions, and at \textbf{$\sim$24\,\%} of what the
deposition-velocity method predicts ($\sim$4.6\,\% for PM$_{10}$), with leaf loading saturating in winter.""",
r"""\textbf{Hazard decoupled from mass.} PM$_{2.5}$-bound PFASs in Jinan (163 filters) were numerically
higher on clean than on slightly polluted days in summer and autumn; in Beijing, haze, firework and dust
events rank differently by hazard index, carcinogenic risk and OP. Neither ordering is recoverable from a
mass sensor.""",
r"""\textbf{Six of 30 records are metadata-only (20\,\%)}, down from 32\,\% on 30 Sep: three Elsevier, two
RSC (\textit{Environ Sci: Atmos}, teaser only) and one \textit{KRCP}. The most watch-relevant is an
\textbf{indoor air study in low-income Indianapolis housing}. Retry list grows by six.""",
]

CONT = r"""The 30 September issue closed with \texttt{last\_entry\_date} at 30 September. This issue
collects \textbf{1 October in full}, continuous with it. The run started at 09:32 CDT on 2 October, before
the 22:00 cut, so the newest buildable date is 1 October and \textbf{2 October is left to the next run}.
\textbf{Month-boundary fix:} the Europe PMC retro-index gate dropped preprints first published before the
issue month; on the 1st that would have discarded five medRxiv / Research Square preprints posted 29--30
September and deposited on 1 October (all five are admitted here). The gate now floors at $D-7$ days."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 30 in-scope records. \textbf{Nine of ten bands
populated}; \textit{Exposure assessment} leads with \textbf{ten} (three metadata-only), \textit{Mechanistic
toxicology} has five, \textit{Sensing} four and \textit{Burden \& policy} three. \textit{Respiratory \&
allergic} is empty; the one airway record is a mouse mechanism study filed under toxicology.""",
"f2_design_endpoint": r"""Left --- architecture: measurement campaigns \textbf{eight}, metadata-only six,
modelling/inventory five, experimental toxicology four, cohorts three, chamber/laboratory two, and one each
for the case-crossover and the cross-sectional epigenetic study. Right --- \textbf{19} records carry no
health endpoint; the eleven that do are spread one each, from attributable mortality to an in-vitro
ocular barrier.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{nine}, unspeciated / emissions
nine, PM$_{2.5}$ + PM$_{10}$ six, composition four, optical properties two. Right --- geography: China
\textbf{eleven}, global / not stated eight (six metadata-only plus two laboratory or computational), North
America four, Europe and East Asia ex-China three each (Japan, South Korea, Taiwan), South Asia one.""",
"f6_lifecourse": r"""Life-course windows: in utero three (ECHO autism traits; mouse carbon-black and kidney
records), childhood, adolescence and working age none, older adults two (ELSA 50+, metastatic prostate
cancer).""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 30 records. Measurement campaigns sit in
exposure, sensing, burden and indoor bands; all four experimental-toxicology records are mechanistic; the
three cohorts are one each in neuro, reproductive and cardiovascular.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Two hazard ratios with 95\,\% CIs, both from the metastatic-prostate-cancer cohort, log scale. One
is per IQR (IQR not stated in the abstract), the other a high-vs-low contrast within ADT-treated men, so
they are not poolable. The crime study reports percentages without CIs, and the ELSA and ECHO estimates
that carry CIs are for NO$_2$ and O$_3$; none enters the panel.}"""

PROV = r"""Entry window \textbf{1 October 2026}, single day, continuous with the 30 September issue.
Harvester legs run leg-by-leg: \textbf{PubMed} health \textbf{34}, sensing \textbf{3}; \textbf{Europe PMC}
\textbf{17} (all kept after the $D-7$ floor on the retro-index gate); \textbf{Crossref by ISSN} \textbf{55};
\textbf{arXiv} no entry dated 1 October; \textbf{OpenAlex} HTTP 429. 109 raw deduplicated to \textbf{104},
\textbf{11} already carried, \textbf{93} fresh. The \textbf{PubMed connector} (\texttt{[EDAT]} 1 October)
returned 13 health and 3 sensing PMIDs (15 unique); 2 appended, 4 already seen, the rest in the
harvester set. \textbf{95} candidates screened, \textbf{30 admitted}, \textbf{65 rejected} with logged
reasons (\textit{J Environ Sci} gas-phase, catalysis and soil records, \textit{ES\&T} water chemistry,
\textit{Measurement Science and Technology} engineering, NO$_2$- or CO$_2$-only records, and climate
aerosol--cloud work). \textbf{Consensus} returned 10 calibration hits, \textbf{0 new} (all archived or
previously rejected). \textbf{ClinicalTrials.gov}: no PM/air-pollution registration updated 1--2 October.
\textbf{Scholar Gateway} still fails with an identity error. \textbf{Six records carried on metadata
alone}. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain the copyright of their respective
publishers."""
