# -*- coding: utf-8 -*-
HEAD = dict(long="17 October 2026", window="17 October 2026 (full day)", n=15, excl=44,
            bands=9, eff=4, tierA=4, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}The gravimetric reference itself carries a +3 to +18\,\% water bias in PM$_1$
and PM$_{2.5}$ that survives standard conditioning --- and every low-cost sensor calibrated against filters inherits
it.}\\[1.4mm]
\footnotesize
Karl Fischer coulometry on 30 conditioned 47\,mm glass-fibre filters (PM$_1$, PM$_{2.5}$, PM$_{10}$) from a Krak\'ow
steelworks site and a Zdzieszowice coal-combustion site, plus five blanks, with stepwise thermal water release at
50--250\,$^\circ$C. Strongly bound water (180--250\,$^\circ$C) was \textbf{51--60\,\%} of filter water and adds a
systematic \textbf{+3\,\% to +18\,\%} positive mass bias, largest for PM$_1$ at the steelworks; between-filter CV
reached \textbf{53\,\%} for PM$_1$ and was minimal near 1330--1360\,$\mu$g loading.
\textbf{Where it is weak:} 35 filters at two industrial sites, preprint, and the bias is not yet resolved by
composition or humidity history.
\textbf{Why it matters here:} co-location slopes are fitted to the reference; a composition-dependent positive
bias in the reference is folded silently into every regional correction equation."""

CHANGED = [
r"""\textbf{A five-year mortality tail for wildfire smoke.} Deconvolving US county-month panels puts the excess-death
peak $\sim$3\,y after a smoke pulse and gives \textbf{1.7 million} smoke deaths 2011--2023 (1.1--2.3\,M), about ten
times long-term-RR estimates --- a large claim from an ecological lag structure (medRxiv).""",
r"""\textbf{A country-panel PM$_{2.5}$ paradox dissolves under trend control.} Two-way FE gives \textbf{+0.41}\,y life
expectancy per 10\,$\mu$g\,m$^{-3}$ (0.14--0.67); economy-specific trends take it to $-$0.02 ($-$0.18 to 0.13).""",
r"""\textbf{China's Action Plan and infant neurodevelopment.} Wuhan cohort, $n$=3,575: target-trial emulation puts
later-policy-period children \textbf{7.3} (MDI) and \textbf{6.4} (PDI) Bayley points higher; first postnatal year
the most sensitive window.""",
r"""\textbf{Cataract: NO$_2$, not PM$_{2.5}$.} Pooled HR 1.041 (1.013--1.070) per 10\,$\mu$g\,m$^{-3}$ NO$_2$; PM$_{2.5}$
1.036 (0.988--1.086) per 1\,$\mu$g\,m$^{-3}$ with I$^2$ = 99.7\,\%.""",
]

CONT = r"""The 16 October issue closed with \texttt{last\_entry\_date} at 16 October. This issue collects
\textbf{17 October in full}, continuous with it. The 17 October run did not fire at or after 22:00 CDT, so this
issue, the \textbf{W42 weekly} (11--17 October) and the 18 October daily were all built on the 19 October run
(18:47 CDT). 19 October is not opened (before 22:00)."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 15 in-scope records across nine bands --- the widest spread this week.
Sensing (3: gravimetric metrology, East African passive network, graph forecasting) leads; burden, exposure,
mechanism and other-clinical have two each. Neuro is the only empty health band.""",
"f2_design_endpoint": r"""Left --- architecture: modelling (3), ecological panels (2: smoke deconvolution, country
specification), one RCT (LPG) and one meta-analysis; metadata-only 1 (7\,\%). Right --- endpoints span mortality,
cataract, Bayley scores, acute symptoms and metabolic syndrome.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ dominates; size-resolved gravimetry and PUF
composition sampling appear on the measurement side. Right --- geography: global/multi-region and not-applicable
records (6) lead; China 3; Poland, Thailand, Chile, East Africa and the US one each.""",
"f6_lifecourse": r"""Life-course windows: the Wuhan cohort fills both preconception/in utero and childhood; working
age carries the LPG cooks and Thai adults; older adults only through the wildfire-smoke burden. No adolescent
record.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Sensing splits across laboratory metrology, a field network
and a forecasting model; burden is entirely ecological.""",
}

FOREST = r"""\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{Ratio scale: pooled cataract HRs from one meta-analysis --- PM$_{2.5}$ per 1\,$\mu$g\,m$^{-3}$ (I$^2$ 99.7\,\%,
not a common effect) and black carbon per study-specific IQR (I$^2$ 33\,\%). Both cross the null.}\end{minipage}

\vspace{2mm}
\noindent\begin{minipage}{\linewidth}\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{Difference scale: change in national life expectancy (years) per 10\,$\mu$g\,m$^{-3}$ PM$_{2.5}$ in 186
economies, conventional two-way FE vs the same model with economy-specific linear trends. The sign flip is the
finding: the paradoxical positive coefficient is a trend artefact.}\end{minipage}"""

PROV = r"""Entry window \textbf{17 October 2026}, single day. Harvester legs: \textbf{PubMed} health \textbf{6},
sensing \textbf{1}; \textbf{Europe PMC} \textbf{24} (0 AGRICOLA); \textbf{Crossref by ISSN} \textbf{36};
\textbf{arXiv} no entry dated 17 October; \textbf{OpenAlex} HTTP 429. 66 unique, 11 already carried, 55 fresh.
\textbf{PubMed connector} (EDAT 17--18 Oct) 21 PMIDs, 4 appended to this day --- \textbf{59} candidates screened,
\textbf{15 admitted}, \textbf{44 rejected} with logged reasons. \textbf{DOI gate} 0 fail / 0 warn. \textbf{Consensus}
calibration sweep (run once for 17--18 Oct): 10 hits, 1 new, filed in the 18 October issue. \textbf{Trial watch}: 0
registrations updated 16--19 October. Abstracts recovered via PubMed, Europe PMC and Semantic Scholar for 14 of 15;
\textbf{1 record carried on metadata alone}. \textbf{Scholar Gateway} not called (\texttt{ACCESS\_DENIED} on previous
runs). Abstracts remain the copyright of their publishers."""
