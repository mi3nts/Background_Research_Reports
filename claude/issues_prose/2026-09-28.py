# -*- coding: utf-8 -*-
HEAD = dict(long="28 September 2026", window="28 September 2026 (full day)", n=15, excl=120,
            bands=7, eff=0, tierA=1, meta=5)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A year after the Maui wildland--urban interface
fire, 1,400 adults carry urinary metal burdens far above US reference levels, and the mixture
index tracks abnormal spirometry --- a hazard that PM$_{2.5}$ mass monitoring would not have
registered.}\\[1.4mm]
\footnotesize
Maunakea and colleagues (\textit{PNAS}, tier A) enrolled \textbf{1,400 adults 6--18 months} after the
August 2023 Maui fires and measured \textbf{24 urinary metals} and spirometry at the same visit.
Relative to US reference values, antimony was \textbf{40-fold}, manganese \textbf{3.8-fold}, barium
\textbf{2.3-fold} and arsenic \textbf{2.2-fold} higher, clustering in the most affected areas. Per
quantile of the WQS positive-mixture index (driven by As, Cd, Cu), the odds of FVC, FEV$_1$,
FEV$_1$/FVC and FEF$_{25-75}$ below the lower limit of normal were \textbf{1.71, 1.53, 1.83 and 1.84}.
\textbf{Why it is the signal:} a WUI fire burns buildings, vehicles and treated materials, and what
it leaves behind is a metal-rich ash that resuspends for months; mass-based PM$_{2.5}$ sensors
record smoke days, not this. The inference has real gaps --- cross-sectional, no pre-fire baseline,
no CIs in the abstract, arsenic partly dietary and cadmium partly from smoking, and \textbf{no air
or dust measurement} ties the burden to the fire. \textbf{The operational rule:} after structure
fires, add filter-based metal speciation (or XRF on sensor-co-located filters) and resuspension
monitoring for months, rather than standing down when the optical PM$_{2.5}$ series returns to
baseline."""

CHANGED = [
r"""\textbf{Indoor and occupational records dominated: six of fifteen.} Coal-mine dust and NO$_2$ led
a BKMR/Qgcomp mixture associated with metabolic syndrome in Chinese miners; Benin City classrooms
ran \textbf{11.2--81.4\,$\mu$g\,m$^{-3}$} PM$_{2.5}$ with cough in \textbf{58.2\,\%} of pupils while
every HQ stayed below 1; a Beijing Metro study used CFD to place measurement points before sampling;
a scoping review inventoried questionnaires paired with low-cost IAQ sensors.""",
r"""\textbf{A controlled wood-smoke exposure model for calves.} 24 pre-weaned Holsteins, 6\,h at
\textbf{238\,$\mu$g\,m$^{-3}$} vs \textbf{9.9}: lower respiratory rate, higher tidal volume, more BALF
granulocytes, macrophages and NK cells. A rare controlled dose in agricultural smoke work.""",
r"""\textbf{No PM association survived in a microtia case-only study} (589 patients): only an
inverse SO$_2$ association in males passed FDR, with address at registration standing in for
gestational weeks 5--9.""",
r"""\textbf{Five of fifteen are metadata-only}, including the \textit{JAMA Netw Open} Singapore
PM$_{2.5}$--asthma/COPD ED study (PubMed carries only a one-line summary), an \textit{AS\&T}
differential mobility analyser geometry paper, and a \textit{QJM} decomposition of the PM$_{2.5}$
NCD burden into ageing versus epidemiological change. All go on the retry list.""",
r"""\textbf{Harvest state.} Europe PMC \textbf{75} (mostly MDPI noise), Crossref-ISSN \textbf{49},
PubMed health \textbf{10} / sensing \textbf{1}. Seven Europe PMC records had already been screened
out on 26 September and were rejected again under the same reasons; the Bangladesh network paper
reappeared via Europe PMC and was dropped as already in the 27 September issue. \textbf{Scholar
Gateway failed} with an identity error, so the JAMA numbers could not be recovered from full text.""",
]

CONT = r"""The 27 September issue (built earlier on this run) closed with \texttt{last\_entry\_date}
at 27 September. This issue collects \textbf{28 September in full}, continuous with it, and closes
the three-day backfill of 26--28 September. The run started at about 17:40 CDT on 29 September,
so under the 22:00 rule \textbf{29 September is not opened}; it and the \textbf{September monthly}
(30 September) fall to the next runs."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 15 in-scope records. \textbf{Seven of ten bands
populated}; \textit{Occupational \& indoor} leads with \textbf{six}. \textit{Cardiovascular},
\textit{Neuro} and \textit{Other clinical} are empty.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{metadata only five}, measurement
campaigns, cross-sectional observational and reviews \textbf{three} each, one experimental. Right ---
endpoint: \textit{no health endpoint} takes \textbf{eight} (five missing abstracts, three non-health
records); \textit{respiratory} \textbf{three} (Maui, calves, the IL-20 review); occupational,
irritant symptoms, metabolic and congenital anomaly one each.""",
"f3_metric_geography": r"""Left --- particle metric: unspeciated / emissions \textbf{seven} (metal
biomonitoring, dusts, smoke and metadata-only records), PM$_{2.5}$ only \textbf{four}, PM$_{2.5}$ +
PM$_{10}$ \textbf{three}, size-resolved one (the DMA). Right --- geography: North America
\textbf{four} (Maui, the calf study, OR nurses, Greenland fjords binned geographically), China
\textbf{three}, and one each for Singapore, South Korea, France and Nigeria; four not recoverable or
multi-region.""",
"f6_lifecourse": r"""Life-course windows: in utero one (microtia, weeks 5--9), childhood and
adolescence one each (Benin City primary and secondary schools), working age three (coal miners,
OR nurses, Maui adults), older adults none.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 15 records.
\textit{Occupational \& indoor} spreads across four architectures; metadata-only records sit in
four different bands.""",
}

FOREST = r"""{\fontsize{7.4}{9}\selectfont\color{Slate}\textbf{No forest plot this issue.} No admitted
abstract reports a PM effect estimate with a confidence interval: the Maui ORs are per quantile of a
urinary metal mixture index and carry no CI in the abstract; the Benin City classroom OR is crude and
without CI; the microtia study reports p- and q-values only. The f5 panel is absent by design, not by
build failure.\par}"""

PROV = r"""Entry window \textbf{28 September 2026}, single day, continuous with the 27 September issue.
Harvester legs run leg-by-leg: \textbf{PubMed} health \textbf{10}, sensing \textbf{1}; \textbf{Europe
PMC} \textbf{75}; \textbf{Crossref by ISSN} \textbf{49}; \textbf{arXiv} no entry dated 28 September;
\textbf{OpenAlex} 0. 135 raw deduplicated to \textbf{133}, \textbf{12} already carried, \textbf{121}
fresh; the \textbf{PubMed connector} (\texttt{[EDAT]} 26--28 September, three axes, bucketed by entrez
date) placed \textbf{25} PMIDs on this day: 14 appended, 1 PMID merged onto an existing DOI record.
\textbf{135} candidates screened, \textbf{15 admitted}, \textbf{120 rejected} with logged reasons
(dominated by MDPI pharmaceutics, food and materials papers from Europe PMC, \textit{Measurement
Science and Technology} engineering, and gas-phase or ozone-only records under standing precedent).
Consensus and ClinicalTrials.gov were swept once for the backfill (see the 26 September issue).
\textbf{Scholar Gateway} returned an identity error and contributed nothing. \textbf{Five records are
carried on metadata alone}. DOI gate: \textbf{0 fail, 0 warn} after one PMID mis-keyed at authoring
was caught by the gate and corrected (the \textit{QJM} record). Greenland geography needle added
(binned with North America geographically). Abstracts remain the copyright of their respective
publishers."""
