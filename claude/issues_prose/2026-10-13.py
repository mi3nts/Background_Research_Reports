# -*- coding: utf-8 -*-
HEAD = dict(long="13 October 2026", window="13 October 2026 (full day)", n=16, excl=40,
            bands=9, eff=2, tierA=1, meta=4)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}Prenatal ultrafine particles, not PM$_{2.5}$, track positive
postpartum-depression screens in a 2,647-woman Shanghai cohort: OR 1.25 per IQR in the first trimester.}\\[1.4mm]
\footnotesize
Residential trimester-specific UFP and PM$_{2.5}$; EPDS $\geq$10 at 6--10 weeks postpartum (20.4\,\% positive).
First-trimester UFP \textbf{OR 1.252} (1.065--1.471) per IQR, whole-pregnancy \textbf{1.104} (1.047--1.164), both
robust to PM$_{2.5}$ adjustment; PM$_{2.5}$ itself showed no stable independent association. It follows the 5
October UFP--dementia result (HR 1.22 per 10,000\,cm$^{-3}$): two neuro endpoints in nine days carried by
particle \textit{number}, not mass.
\textbf{Where it is weak:} an EPDS screen is not a diagnosis, and the abstract does not give the UFP surface's
resolution or validation. UFP decays within a few hundred metres of roads; residential misclassification is
probably large, and it is non-differential only if road proximity is unrelated to deprivation."""

CHANGED = [
r"""\textbf{Instrumentation is a third of the issue.} A polarisation-ceilometer aerosol typing algorithm
(CONIOPOL, Vaisala CL61) validated over a year at Uccle; drone profiles showing when ground nodes represent the
mixed layer; dust-lidar asymptotics implying classifiers under-count coarse absorbing dust; and a Taiwan PM$_{10}$
forecaster in which \textit{upwind observation density}, not trajectory sophistication, delivered the skill
(RMSE 11.04\,$\mu$g\,m$^{-3}$, 13\,\% below persistence).""",
r"""\textbf{Smoke source attribution in three regimes.} Fire-sourced PM$_{2.5}$ outperforms all-source mass for
five cancer sites across China; fire-on/fire-off simulations put 17--21\,$\mu$g\,m$^{-3}$ of 2024 S\~ao Paulo
peaks on biomass burning, with every inventory short at the worst episode; PMF on 1,195 filters attributes
21--35\,\% of North Macedonian PM$_{2.5}$ to wood burning, $>$50\,\% on 83\,\% of Skopje episode days.""",
r"""\textbf{Particle counts are not microbes.} In dental ultrasonic scaling, sub-micron counts surged while
culturable bacteria sat in the 1.1--3.3\,$\mu$m stages --- an optical counter's number signal is the wrong
proxy for biological load.""",
r"""\textbf{One cross-day duplicate removed.} The Lancet Planetary Health multicountry admissions paper reached
13 October through the connector's \texttt{[EDAT]} bucket; it is carried once, in the 12 October issue.""",
]

CONT = r"""The 12 October issue (built earlier in this run) closed with \texttt{last\_entry\_date} at 12 October.
This issue collects \textbf{13 October in full}, continuous with it. 14 October follows as its own issue;
15 October is not opened under the 22:00 rule."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 16 in-scope records across nine bands. Sensing and exposure
assessment tie at four each --- the first issue since 8 October where measurement work equals the largest
health band combined.""",
"f2_design_endpoint": r"""Left --- architecture: four metadata-only records (25\,\%), all Elsevier or Dove
deposits without abstracts at harvest; one instrument development and one theoretical optics paper. Right ---
health endpoints are sparse: postpartum depression, cancer incidence, placental biomarkers, paediatric asthma.""",
"f3_metric_geography": r"""Left --- particle metric: composition, source-resolved and vertical/optical
quantities outnumber plain PM$_{2.5}$. Right --- geography spans China, Taiwan, Vietnam, Brazil, North
Macedonia, Belgium, Germany, Canada and the US.""",
"f6_lifecourse": r"""Life-course windows: in utero (prenatal UFP, placental biomarkers), childhood and
adolescence (school smoke, Taiwanese asthma), working age (postpartum mothers). No older-adult record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. The sensing row spans machine learning, instrument
development, theory and field measurement --- four architectures for four records.""",
}

FOREST = r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Two odds ratios per IQR of modelled residential UFP from the same 2,647 pregnancies; not independent.
The first-trimester estimate is larger but wider; the whole-pregnancy estimate is the more stable of the two.
No PM$_{2.5}$ estimate is shown because the abstract reports none as stable.}"""

PROV = r"""Entry window \textbf{13 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{14},
sensing \textbf{1}; \textbf{Europe PMC} \textbf{46}, all AGRICOLA retro-index records (pubYear before 2026),
\textbf{all dropped}; \textbf{Crossref by ISSN} \textbf{42} (2 ES\&T Letters front-matter items dropped);
\textbf{arXiv} no entry dated 13 October; \textbf{OpenAlex} HTTP 429. 53 unique, 0 already carried.
\textbf{PubMed connector} 8 PMIDs dated 13 October, 3 appended --- \textbf{56} candidates screened,
\textbf{16 admitted}, \textbf{40 rejected} with logged reasons (one a cross-day duplicate of the 12 October
Lancet Planetary Health record). Abstract retry recovered 11 of 15; \textbf{4 records carried on metadata
alone}. \textbf{Scholar Gateway} still \texttt{ACCESS\_DENIED}. Abstracts remain the copyright of their
publishers."""
