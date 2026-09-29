# -*- coding: utf-8 -*-
HEAD = dict(long="26 September 2026", window="26 September 2026 (full day)", n=23, excl=109,
            bands=9, eff=4, tierA=0, meta=2)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}The exposure metric that carried the signal in a
cystic-fibrosis pilot was time above 35\,$\mu$g\,m$^{-3}$ indoors --- a quantity only a continuous
sensor can produce --- while the period mean was null.}\\[1.4mm]
\footnotesize
Zhang and colleagues (\textit{Respir Med}) put real-time PM$_{2.5}$ sensors in the homes of adults
with cystic fibrosis for \textbf{4--11 days} and drew one multiplex cytokine panel per person. The
\textbf{mean} PM$_{2.5}$ over the monitoring period was unrelated to any cytokine; the
\textbf{percentage of monitoring time above 35\,$\mu$g\,m$^{-3}$} correlated moderately and
significantly with \textbf{PDGF-AA/BB}, with non-significant positive trends for IL-7 and IL-8.
\textbf{Why it is the signal:} indoor PM$_{2.5}$ is dominated by short cooking and cleaning
episodes, and a filter-integrated mean folds those peaks into a number that can sit well below
any threshold; the exceedance metric preserves them. The weaknesses are real --- sample size and
sensor model are not in the abstract, correlations are Spearman across a cytokine panel with no
multiplicity control, and one blood draw cannot fix timing --- so this is a hypothesis, not a
result. The Durban MACE paper in the same issue shows the opposite failure: categorical ETS and
biomass-fuel proxies carried large ORs while the \emph{measured} indoor PM$_{2.5}$ is not reported
at all. \textbf{The operational rule:} when a panel study deploys continuous sensors, pre-specify
an exceedance or peak metric alongside the mean, and report the measured-PM model even when it
is null."""

CHANGED = [
r"""\textbf{Non-exhaust iron behaved as a brake, not an accelerator, on cellular superoxide.} Shen
et al.\ (\textit{ES\&T}) find brake-wear particles induce slight superoxide below
\textbf{10\,$\mu$g\,mL$^{-1}$} and suppress it dose-dependently above; Fe$^{2+}$ and Fe$^{3+}$
suppress organic-induced superoxide via the labile iron pool and direct quenching. Ghio et al.\
(\textit{Pathogens}) argue the reverse direction for TB --- particles sequester host iron. Both
are mechanistic; neither measures hydroxyl radical, the Fe-driven species.""",
r"""\textbf{A cell-based oxidative-activity assay was characterised on filter substrates.}
Tzagkaroulaki et al.\ (\textit{Toxics}) report PTFE-vs-quartz zero-intercept slopes of
\textbf{0.90} (mass-normalised) and \textbf{0.99} (volume-normalised), R$^2$\,$\approx$\,0.99, over
\textbf{eight} matched pairs, and a monotonic SRM\,2584 response only at the 60-min readout.
Fluorescence did not track PM mass in field samples.""",
r"""\textbf{Two pooled or cohort estimates, both with unstated increments.} CHARLS (8,792 adults,
2011--2020): incident CVD \textbf{HR 1.09 (1.03--1.16)} for PM$_{2.5}$ and \textbf{1.07
(1.04--1.10)} for PM$_{10}$. An osteoporosis meta-analysis of \textbf{48 studies}: PM$_{2.5}$
\textbf{OR 1.24 (1.02--1.51)}, PM$_{10}$ \textbf{1.17 (0.96--1.42)}, with extreme heterogeneity.
Neither abstract states the contrast, so the forest panel is a display, not a synthesis.""",
r"""\textbf{Composition records from under-sampled places.} 116 daily speciated PM$_{10}$ samples
from \textbf{Luanda} tie aqueous-extract toxicity to a Zn/Pb/Cd metallurgy and scrap-burning PMF
factor ($\rho$\,=\,0.63--0.78); \textbf{Temuco} wood-smoke season averaged \textbf{75.0}
PM$_{2.5}$ / \textbf{87.7} PM$_{10}$\,$\mu$g\,m$^{-3}$; \textbf{Nanchang} WSIIs show the control
problem shifting since 2019 from sulfate to wintertime nitrate.""",
r"""\textbf{Harvest state.} Europe PMC is back (\textbf{45} records after the 25 September
HTTP\,503); arXiv now answers (148\,kB) but carried no entry dated 26 September. The PubMed
connector's broad axis bucketed \textbf{77} PMIDs to this day by entrez date; most were
`aerosolised'/`carbon black' noise, and \textbf{5} of the admissions came only from the connector.
\textbf{No tier-A record} this issue and \textbf{two} Elsevier deposits carried on metadata alone.""",
]

CONT = r"""The 25 September issue closed with \texttt{last\_entry\_date} at 25 September. This issue
collects \textbf{26 September in full}, continuous with it. The scheduled runs for 26, 27 and 28
September did not fire; this issue was built on the \textbf{29 September backfill run at about
17:40 CDT}, which also builds 27 and 28 September as separate issues. Under the standing 22:00
rule \textbf{29 September is not opened}. The \textbf{W39 weekly} (20--26 September) is built on
the same run and filed under 26 September."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 23 in-scope records. \textbf{Nine of ten bands are
populated; \textit{Burden, policy \& mitigation} is empty.} \textit{Exposure assessment \&
modelling} and \textit{Mechanistic toxicology} lead with \textbf{six} each; \textit{Sensing}
holds a single metadata-only deposit.""",
"f2_design_endpoint": r"""Left --- study architecture across seven groups: measurement
campaigns and experimental toxicology \textbf{five} each, reviews \textbf{four}, cross-sectional
\textbf{three}, cohort, modelling and metadata only \textbf{two} each. Right --- health endpoint:
the non-health categories (bioaerosol, aerosol chemistry, missing abstracts) and a long tail of
clinical endpoints with one or two records each.""",
"f3_metric_geography": r"""Left --- particle metric: \textit{PM$_{2.5}$ only} \textbf{9},
\textit{PM$_{2.5}$ + PM$_{10}$} \textbf{6}, unspeciated \textbf{6}, PM$_{10}$ only and optical
\textbf{one} each. Right --- geography: \textbf{Global / multi-region holds eleven}, of which only
reviews are truly multi-region; the rest are laboratory studies, metadata-only deposits and one
abstract naming no country. China \textbf{four}, Europe \textbf{three}, Sub-Saharan Africa
\textbf{two} (Luanda, Durban), and one each for Latin America, Central Asia and Southeast Asia.""",
"f6_lifecourse": r"""Life-course windows addressed; counts are non-exclusive. In utero two (GDM
case-control, Durban prenatal PM$_{2.5}$), childhood one (Durban), adolescence none, working age
four (coal miners, CF adults, cyclists, MetS adults), older adults two (CHARLS $\geq$45, dementia
review).""",
"f4_heatmap": r"""Subtopic $\times$ study-architecture cross-tabulation for the 23 records. The
densest cells are \textit{Mechanistic toxicology} $\times$ experimental (\textbf{five}) and
\textit{Exposure} $\times$ measurement campaign (\textbf{three}); most other occupied cells are
singletons.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{\textbf{Four ratio-scale estimates from two studies, on unstated contrasts --- not a
synthesis.} The CHARLS incident-CVD HRs (PM$_{2.5}$ \textbf{1.09}, PM$_{10}$ \textbf{1.07}) are
single-pollutant and the increment is not given in the abstract; the osteoporosis ORs
(PM$_{2.5}$ \textbf{1.24}, PM$_{10}$ \textbf{1.17}, CI crossing 1) pool incommensurate
contrasts under extreme heterogeneity. Read magnitudes as indicative only.}"""

PROV = r"""Entry window \textbf{26 September 2026}, single day, continuous with the previous issue.
Harvester legs, run leg-by-leg in the foreground: \textbf{PubMed} E-utilities on the health and
instrumentation axes as separate queries (\textbf{12} health, \textbf{2} sensing);
\textbf{Europe PMC} \texttt{CREATION\_DATE} (\textbf{45}); \textbf{Crossref by ISSN}
(\textbf{26}); \textbf{OpenAlex} 0 (date filter still paywalled); \textbf{arXiv} relevance query
answered (148\,kB) but no entry was dated 26 September after the window gate. Connector sweeps:
the \textbf{PubMed connector} over \texttt{[EDAT]} 26--28 September on three axes --- health (40
PMIDs), sensing (2), broad aerosol/air-quality (97) --- bucketed by entrez date, \textbf{77} to
this day, \textbf{63} appended after dedup. \textbf{Consensus} on low-cost PM$_{2.5}$ calibration,
humidity correction and co-location: 10 hits, all archived, previously rejected or outside the
window (\textbf{0 new}). \textbf{ClinicalTrials.gov}, updates posted 26--29 September: one hit,
the completed HAPIN LPG trial (NCT02944682), recorded for the weekly trial watch.
The \textbf{85} harvester records deduplicated to \textbf{82}, \textbf{13} already carried,
leaving \textbf{69}; with 63 connector records, \textbf{132} candidates were screened,
\textbf{23 admitted} and \textbf{109 rejected}, every rejection logged with a reason (most are
connector noise: inhaled-drug formulations, carbon-black materials, food science). Two records
previously rejected on 25 September resurfaced through Europe PMC and were rejected again under the
same reasons. \textbf{Two records are carried on metadata alone}; recovery was attempted through
PubMed \texttt{efetch}, Crossref, Europe PMC and publisher landing pages. DOI gate:
\textbf{0 fail, 2 warn} (two MDPI \textit{Toxics} DOIs not yet deposited but matching PubMed).
Geography needles added for Angola, Chile and Kazakhstan. Labels are single-assignment
judgements, not a controlled vocabulary; where an abstract names no country, geography is recorded
as not stated. Abstracts remain the copyright of their respective publishers."""
