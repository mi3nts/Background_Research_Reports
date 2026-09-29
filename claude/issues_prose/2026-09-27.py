# -*- coding: utf-8 -*-
HEAD = dict(long="27 September 2026", window="27 September 2026 (full day, Sunday)", n=4, excl=7,
            bands=3, eff=2, tierA=1, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A personal-monitor panel in older adults finds a
next-day activity deficit after higher-than-usual PM exposure --- and no association at all when
the same days are scored with area-level PM.}\\[1.4mm]
\footnotesize
Bloomberg and colleagues (\textit{medRxiv}, tier A, not peer reviewed) had \textbf{67 UK adults aged
50--85} wear personal air-quality monitors and 24-h accelerometers for five days (\textbf{304
person-days}). Within-person, a day \textbf{+1 IQR above the person's own mean} --- only
\textbf{+2.6\,$\mu$g\,m$^{-3}$} PM$_{2.5}$ --- was followed by \textbf{8 min less light activity
(95\,\% CI $-$14 to $-$2)} and \textbf{483 fewer steps ($-$855 to $-$82)}; PM$_{10}$ gave the same
LPA deficit and \textbf{8 min more sedentary time}. MVPA did not move, and \textbf{area-level PM
estimates produced no association}. \textbf{Why it is the signal:} the contrast is small enough to
sit inside the error band of an uncalibrated optical sensor, yet it is the personal series, not
the modelled area series, that carries the within-person signal --- the pattern expected if
area estimates smear the day-to-day variance that behaviour responds to. The weaknesses: monitor
model and calibration are not stated, weather and minor illness drive both indoor PM and
next-day activity, and the reverse pathway (being indoors more raises personal PM) is only
partly handled by the next-day lag. \textbf{The operational rule:} in short-term panel designs,
the personal sensor is not a noisier version of the area estimate but a different exposure; report
both, and report the sensor's co-location performance so the contrast can be judged against it."""

CHANGED = [
r"""\textbf{Sunday window, thin by construction.} PubMed returned \textbf{4} health records and
\textbf{0} on the sensing axis; Europe PMC \textbf{1}, Crossref-ISSN \textbf{2}, arXiv \textbf{1}
(off-topic engine control). Four records were admitted.""",
r"""\textbf{Bangladesh's regulatory network reports a 15\,\% decline.} Shahadat et al.\ (16 DoE
stations, 2018--2025): network PM$_{2.5}$ \textbf{91.54 $\rightarrow$ 77.64\,$\mu$g\,m$^{-3}$},
PM$_{10}$ \textbf{155.7 $\rightarrow$ 132.3}, non-monotonic after the 2020 minimum, every station
above national standards every year, winter/monsoon ratio \textbf{$\sim$4.2} for PM$_{2.5}$. Kriging
was abandoned for prediction because 16 stations cannot support it.""",
r"""\textbf{NAKO mental-health results arrived without an abstract.} The German National Cohort
longitudinal environmental-exposure paper (\textit{Environ Int}) is carried metadata-only and goes
to the top of the retry list.""",
r"""\textbf{Bioaerosol in a paediatric emergency room.} 73.47\,\% of culturable bacterial
aerosol was below 3.3\,$\mu$m, and CFD put 79.71\,\% of deposition on the desk and floor ---
a fraction optical PM sensors cannot distinguish.""",
]

CONT = r"""The 26 September issue (built earlier on this run) closed with \texttt{last\_entry\_date}
at 26 September. This issue collects \textbf{27 September in full}, continuous with it. Built on the
\textbf{29 September backfill run}; \textbf{28 September} follows as its own issue on the same run,
and \textbf{29 September is not opened} under the 22:00 rule. Sunday is not a weekly trigger under
the Saturday rule: the W39 weekly closed on 26 September."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the four in-scope records: \textit{Exposure assessment
\& modelling} \textbf{two} (UK personal-monitor panel, Bangladesh network), \textit{Neuro / mental
health} and \textit{Occupational \& indoor} \textbf{one} each. Seven bands are empty.""",
"f2_design_endpoint": r"""Left --- architecture: two measurement campaigns (Bangladesh network,
hospital bioaerosol), one acute observational panel, one metadata-only deposit. Right --- endpoint:
\textit{no health endpoint} \textbf{two} (the behaviour panel and the metadata-only record),
\textit{infection} one, and \textit{oncologic} one (the Bangladesh ELCR screen).""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ + PM$_{10}$ \textbf{two}, size-resolved
bioaerosol \textbf{one}, unspeciated \textbf{one}. Right --- geography: UK, Bangladesh, China, and one
metadata-only record binned as not recoverable.""",
"f6_lifecourse": r"""Life-course windows: the UK panel spans working age and older adults (50--85)
and is counted in both; the paediatric ED study counts in childhood.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the four records; four occupied
cells, each a singleton; \textit{Exposure} splits between measurement campaign and acute observational.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{\textbf{Two difference-scale estimates from one preprint.} Next-day light physical
activity, minutes, per +1 IQR within-person deviation in personal PM$_{2.5}$ (\textbf{$-$8, $-$14
to $-$2}) and PM$_{10}$ (\textbf{$-$8, $-$13 to $-$3}). Same 67 participants and days; not
independent. Step-count estimates are on a different scale and are given in the digest text.}"""

PROV = r"""Entry window \textbf{27 September 2026} (Sunday), single day, continuous with the 26 September
issue. Harvester legs run leg-by-leg: \textbf{PubMed} health \textbf{4}, sensing \textbf{0};
\textbf{Europe PMC} \textbf{1}; \textbf{Crossref by ISSN} \textbf{2}; \textbf{arXiv} \textbf{1} entry
dated 27 September (off-topic); \textbf{OpenAlex} 0. The \textbf{PubMed connector} (\texttt{[EDAT]}
26--28 September, three axes, bucketed by entrez date) placed \textbf{6} PMIDs on this day, \textbf{5}
appended. \textbf{11} candidates screened, \textbf{4 admitted}, \textbf{7 rejected} with logged reasons
(one had already been rejected on 26 September). \textbf{Consensus} and \textbf{ClinicalTrials.gov}
were swept once for the whole 26--28 September backfill and are reported in the 26 September issue
(0 new records; one trial update). \textbf{Scholar Gateway} returned an identity error
(\texttt{Could not resolve user identity}) and contributed nothing this run. One record carried on
metadata alone. DOI gate: \textbf{0 fail, 0 warn}. Abstracts remain the copyright of their
respective publishers."""
