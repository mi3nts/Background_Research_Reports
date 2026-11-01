# -*- coding: utf-8 -*-
"""Author build/weekly.tex for W44 (25-31 Oct 2026) from the W43 source (2026-11-01 run).
Middle sections rewritten whole; masthead, digest and register scaffolding kept."""
s = open("issues/weekly_2026-10-24.tex").read()
def rep(old, new):
    global s
    assert old in s, old[:70]; s = s.replace(old, new)
rep(r"\newcommand{\DIGESTDATE}{24 October 2026}", r"\newcommand{\DIGESTDATE}{31 October 2026}")
rep(r"\newcommand{\PERIODSTART}{18 October 2026}", r"\newcommand{\PERIODSTART}{25 October 2026}")
rep(r"\newcommand{\PERIODEND}{24 October 2026}", r"\newcommand{\PERIODEND}{31 October 2026}")
rep(r"\mbox{119 records pooled from 7 daily issues}", r"\mbox{135 records pooled from 7 daily issues}")
i = s.index(r"\begin{minipage}[t]{0.190\linewidth}\metric{119}"); j = s.index(r"\vspace{6mm}", i)
s = s[:i] + r"""\begin{minipage}[t]{0.190\linewidth}\metric{135}{RECORDS POOLED\\(135 UNIQUE DOIs)}{Deep}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{37\%}{MEASUREMENT SIDE\\(50 RECORDS)}{Teal}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{10}{SUBTOPICS\\ACTIVE}{Sky}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{29}{POOLED EFFECT\\ESTIMATES (29 WITH A CI)}{Amber}\end{minipage}\hfill
\begin{minipage}[t]{0.190\linewidth}\metric{23}{ABSTRACT-FREE\\(17\% OF WEEK)}{Clay}\end{minipage}

""" + s[j:]
i = s.index("% -------------------------------------------------------------- week in one box")
j = s.index("% -------------------------------------------------------------- digest")
SEC = lambda t, r=r"\vspace{2.5mm}": "\\section*{\\sffamily\\bfseries\\color{Deep}%s}\n\\vspace{-1.5mm}{\\color{Teal}\\rule{\\linewidth}{1.1pt}}%s\n\n" % (t, r)
body = "% -------------------------------------------------------------- week in one box\n" + SEC("The week in one paragraph") + r"""\begin{keybox}
{\sffamily\bfseries\small\color{Deep}Volume up to 135, the health side swung from cardiorenal components to the
airway and the developing brain, and fire smoke became the week's common exposure --- prenatal smoke and autism
in 893,212 Medicaid pairs, smoke plus power shutoffs in California, smoke days in Head Start classrooms, a lead-laden
urban firestorm, and a preregistered null for smoke and depression. On the measurement side, humidity came back to
the sensor: a heated PurpleAir sample path, Kelvin-suppressed growth of ultrafine particles, and organic-aerosol
hygroscopicity by source.}\\[1.4mm]
\footnotesize
\textbf{Scale.} \textbf{135 records} over seven issues on daily totals of \textbf{3}, 24, \textbf{30}, 22, 22,
24 and 10. Against recent rollups: 135 after 119, 123, 87, 125, 162 and 148. \textbf{All ten subtopics are
populated} for the sixth week running.

\textbf{The measurement side slipped to 37\,\%} (50 records): \textit{Exposure assessment \& modelling}
31 $\rightarrow$ \textbf{34}, \textit{Sensing} 15 $\rightarrow$ \textbf{16}; the share fell only because the health side
grew faster. Share series 33, 42, 44, 39, 39, \textbf{37\,\%}.

\textbf{Respiratory led the health side's growth}: 11 $\rightarrow$ \textbf{17}; \textit{Neuro / mental health}
doubled 4 $\rightarrow$ \textbf{8}; \textit{Mechanistic toxicology} 10 $\rightarrow$ 14 and \textit{Occupational
\& indoor} 11 $\rightarrow$ 14. \textit{Cardiovascular \& metabolic} halved, 12 $\rightarrow$ \textbf{6}.

\textbf{Estimates: 29, every one with an interval} (sixth complete week at 100\,\%), one per 4.7 records. 21 on
ratio scales (OR 12, HR 5, RR 3, IRR 1) and 8 on difference or percentage scales.

\textbf{Abstract gap 23 of 135 (17\,\%)}, down from 21\,\%. \textbf{Tier mix 16 A, 54 B, 65 C} --- tier A at
\textbf{12\,\%}, back from last week's 18\,\% high; ten EUPHA conference abstracts inflate tier C.
\end{keybox}

\clearpage

% -------------------------------------------------------------- trend
""" + SEC("Subtopic trend and inflection") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/w1_subtopic_trend.png}
\figcap{Per-issue subtopic counts across the week from \texttt{state/metrics.csv}, seven issues. Daily totals 3,
24, 30, 22, 22, 24 and 10. The scheduled runs for 23--29 October did not complete; 25--29 October were built on
the \textbf{30 October recovery run}, and 30 and 31 October with this rollup on the \textbf{1 November run}. The
3-record Sunday (25 October) is the week's floor, as Sundays usually are.}

\footnotesize
\textbf{Expanding.} \textit{Respiratory} 11 $\rightarrow$ \textbf{17} is the largest gain and is cohort- and
event-driven: COPSAC lung-function trajectories to age 18 (FEV$_1$ $-$2.70\,\%, sRaw $+$7.30\,\% per IQR at age 6),
the California PSPS--smoke interaction (joint OR 1.16), Louisiana paediatric asthma admissions (OR 1.079), a
biomass-plus-tobacco COPD series, and a cluster of EUPHA abstracts (Polish DLNM admissions, Dublin spores, La Palma
volcanic ash). \textit{Neuro} 4 $\rightarrow$ \textbf{8} brings two tier-A records (Medicaid prenatal smoke and ASD;
the All of Us depression null) and a purifier-controlled crossover on cognition.

\vspace{1.2mm}
\textbf{Contracting.} \textit{Cardiovascular \& metabolic} 12 $\rightarrow$ \textbf{6} --- the stroke time series
from Guiyang and the 123-city heart-disease cohort are what is left. \textit{Burden} 14 $\rightarrow$ 11.

\vspace{1.2mm}
\textbf{The inflection worth naming.} \textbf{Last week the effect was carried by PM$_{2.5}$ components; this week
it is carried by the source --- fire.} Nine records put a fire-derived exposure on a health or exposure endpoint:
prenatal smoke PM$_{2.5}$ and ASD (HR \textbf{1.30}, 1.07--1.59, per 0.75\,$\mu$g\,m$^{-3}$) but not ADHD (1.03,
0.91--1.17); PSPS outages compounding smoke for respiratory encounters; FIRMS fire counts and Head Start sick absence
(OR 1.106); fire PM$_{2.5}$ and eGFR ($-$0.83\,mL\,min$^{-1}$\,1.73\,m$^{-2}$); a Brazilian fire-density null for
circulatory admissions; the Eaton firestorm plume enriched $>$50-fold in lead over wildland smoke; Idaho's fire-season
PM$_{2.5}$ rising 2.54\,$\mu$g\,m$^{-3}$ per decade while the winter wood-smoke mode declines; and the preregistered
All of Us analysis in which smoke PM$_{2.5}$ showed \textbf{no} association with incident depression. Every one of
these exposures is a model or a satellite product (ECHO smoke, FIRMS, CTM, kriged AQS); the composition contrast the
Eaton record measured is the exception, and it is the one that matters most for toxicity. \textbf{The test for next
week}: a smoke-specific estimate built on measured network data, or a smoke-vs-non-smoke PM$_{2.5}$ contrast with
composition attached.

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f2a_architecture.png}
\figcap{Study architecture over the pooled week. \textit{Measurement campaign} 24 and \textit{Metadata only} 23
lead, then \textit{Modelling / inventory} 19, cross-sectional and cohort designs 16 each and experimental /
toxicology 13. \textbf{Interventional evidence}: a purifier vs sham-filter randomised crossover (cognition, HRV),
the OK-AIR cluster-randomised HEPA/UVGI classroom trial (secondary analysis), and a difference-in-differences
evaluation of China's climate-adaptive city pilot; only OK-AIR carries the \textit{Trial / intervention} label.}

\clearpage
% -------------------------------------------------------------- pooled analytics
""" + SEC("Pooled analytics", r"\vspace{3mm}") + r"""\noindent\includegraphics[width=\linewidth]{\FIGDIR/f1_subtopics.png}
\figcap{Pooled subtopic distribution, all ten bands populated: \textit{Exposure} 34 and \textit{Sensing} 16 put
the measurement side at \textbf{50 of 135 (37\,\%)}. On the health side \textit{Respiratory} 17 leads, then
\textit{Mechanistic toxicology} and \textit{Occupational \& indoor} 14 each and \textit{Burden} 11;
\textit{Cardiovascular} is smallest at 6. The canonicalised endpoint chart (f2b) is omitted: at this volume it
resolves into $>$60 single-record categories and is unreadable; respiratory and neurodevelopmental endpoints lead,
and end-of-induction MRD in childhood leukaemia, transient tachypnoea of the newborn and infant antibiotic
prescribing are new endpoint classes for the watch.}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f3_metric_geography.png}
\figcap{Left --- particle metric; PM$_{2.5}$ alone dominates, with BC/eBC (Oakland inversion, Nepal on-road) and
number-concentration work (ironing, UFP kidney, hygroscopic deposition) the secondary metrics. Right --- geography;
Europe and \textit{Global / multi-region} tie at 28 (the EUPHA abstracts lift Europe), then China 26 and North
America 21; South Asia 10 is a series high.}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f6_lifecourse.png}
\figcap{Life-course windows across the pooled week; counts non-exclusive. \textbf{Childhood leads} for the first
time (COPSAC, REDIAL, Head Start, Louisiana asthma, infant antibiotics), ahead of working age;
preconception / in utero is carried by Medicaid smoke, Taiwan TTN, Chengdu IVF and Indian stillbirth.}

\clearpage

\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest.png}
\figcap{FOREST1}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f5_forest_2.png}
\figcap{FOREST2}

\vspace{2mm}
\noindent\includegraphics[width=\linewidth]{\FIGDIR/f4_heatmap.png}
\figcap{Subtopic $\times$ architecture, pooled. The densest cells are \textit{Exposure} $\times$
\textit{Measurement campaign} and \textit{Mechanistic toxicology} $\times$ experimental; respiratory work spreads
across cohort, acute and cross-sectional designs; sensing is split between instrument evaluation, method papers and
ML prediction.}

\vspace{4mm}

% -------------------------------------------------------------- venues + trials
\par\vskip 0pt plus 14\baselineskip\penalty-200\vskip 0pt plus -14\baselineskip
""" + SEC("Venues, trial watch, and what the pipeline did") + r"""\footnotesize
\textbf{Venues.} \textit{Eur J Public Health} leads at \textbf{10} --- all conference abstracts from the EUPHA 2026
supplement, a batch deposit rather than a trend --- then \textit{Toxics} 6, and \textit{Atmos Chem Phys},
\textit{Atmosphere}, \textit{Front Public Health} and Research Square at 5. \textbf{Preprints supplied 7} (Research
Square 5, medRxiv 1, Preprints.org 1). \textit{Atmos Chem Phys} at 5 is the PubMed-invisible instrumentation
literature arriving through the Crossref-ISSN leg, as designed.

\vspace{1.5mm}
\textbf{Recurring groups and most-cited work.} One genuine repeat-group cluster: the \textbf{K-HEALTHinAIR}
consortium supplied two records (four-country low-cost-sensor monitoring of homes and schools; a Spanish indoor
PM$_{2.5}$--COPD burden estimate). Otherwise surname frequency is a naming artefact. Citation counts for records
days old are uninformative; the largest datasets --- 893,212 Medicaid mother--child pairs, 498,123 Scottish births,
269,945 kidney ED visits, 227,821 Indian pregnancies, 179,218 All of Us adults --- each supplied one record.

\vspace{1.5mm}
\textbf{Trial watch.} ClinicalTrials.gov \texttt{LastUpdatePostDate} 23--30 October: 4 hits, \textbf{1 new}
--- \textbf{NCT07536178} (UBC, \emph{Lungs on Fire}), a controlled woodsmoke-exposure chamber study with FeNO and a
CANTAB cognitive battery as co-primary endpoints; MARKOPOLO NCT07111208, APCIQ-BP NCT05903950 and the Taif COPD
survey NCT07886346 were record updates. 30 October--1 November: \textbf{0 hits} (the weekend days are a structural
registry zero). \texttt{trials.json} holds \textbf{20 trials}. The chamber study is the registry's answer to this
week's smoke literature: it is the only design in the set that can separate smoke from co-exposures. The week's
other interventional evidence came from the literature (purifier crossover, OK-AIR).

\vspace{1.5mm}
\textbf{What the harvesting legs did.} \textbf{Europe PMC} re-surfaced PubMed records on later days throughout
--- 18 of the 31 October candidates were 30 October records and went to that issue; the recovery run caught $\sim$40
cross-day duplicates for 23--29 October. \textbf{Crossref-by-ISSN} 22--66/day. \textbf{PubMed connector} appended
4--10 records/day. \textbf{OpenAlex} HTTP 429 throughout. \textbf{arXiv} no in-window entry. \textbf{Consensus}
10 hits, \textbf{0 new} (both unmatched titles resolved by DOI to shipped records). \textbf{Scholar Gateway} not called.

\vspace{2mm}
% -------------------------------------------------------------- gaps
""" + SEC("Open gaps") + r"""\footnotesize
\begin{itemize}
\item \textbf{Smoke health effects are estimated on modelled smoke.} ECHO, FIRMS and CTM fields carry every smoke
estimate this week; the one record using a PurpleAir exposure (Kinshasa low birthweight, n=355, OR 1.18,
0.59--2.36) is too small to inform. A corrected low-cost network is the obvious smoke-exposure instrument and is
not yet being used as one.

\item \textbf{Humidity is being fixed in hardware and still ignored in exposure.} Heating the PMS5003 sample path
moved readings toward regulatory conditions, and Kelvin-suppressed growth changes UFP deposition by up to 25\,\%;
no health record propagates RH-correction uncertainty into its estimate.

\item \textbf{Ultrafine particles: modelled in the epidemiology, measured only indoors.} The New York kidney signal
(0.74\,\% per IQR) rests on CTM number concentration; the only measured PNC in the week is from ironing.

\item \textbf{Composition faded as fast as it rose.} Last week's ion-resolved cohorts had no successor; measured
speciation (Accra 146-site ED-XRF, Czech dual-height ACSM) stayed on the exposure side and did not reach an outcome.

\item \textbf{The abstract gap eased to 17\,\%}, still concentrated in day-0 Elsevier and Taylor \& Francis deposits.

\item \textbf{Pipeline defects carried forward}: scheduled runs for 23--29 October did not complete (recovered on
30 October); late Europe PMC re-surfacing makes per-day dedup order-dependent; OpenAlex dead; \texttt{.git} lock
debris on the delete-restricted mount.
\end{itemize}

\vspace{1.5mm}
\textbf{Research direction.} The field is moving from \emph{how much} PM$_{2.5}$ to \emph{which} PM$_{2.5}$, and is
answering the question first by source (fire, waste burning, freight) rather than by measured chemistry. That favours
networks that can label source in real time --- absorption/BC channels, size ratios, co-located gas signatures ---
over networks that only report mass.

\clearpage

"""
s = s[:i] + body + s[j:]
i = s.index(r"Period \textbf{18 -- 24 October 2026}"); j = s.index(r"\end{keybox}", i)
s = s[:i] + r"""Period \textbf{25 -- 31 October 2026}, Sunday to Saturday, \textbf{seven daily issues},
\textbf{135 records}, \textbf{135 unique DOIs}, no record without a DOI. This rollup is
\textbf{aggregation only}: it re-reads \texttt{state/corpus/*.json}, \texttt{state/metrics.csv} and
\texttt{state/trials.json} over the period and \textbf{queries no literature API}; every record was gated by
\texttt{check\_dois.py} at daily-issue time. Tier mix \textbf{16 A, 54 B, 65 C}. The 25--29 October dailies were
built on the \textbf{30 October recovery run}; the 30 and 31 October dailies and this rollup on the \textbf{1 November
run}; no record is held. Effect estimates are transcribed verbatim from the daily issues on heterogeneous contrasts
and are \textbf{not} meta-analysed. Abstracts remain the copyright of their respective publishers.\par}
""" + s[j:]
import sys
F1 = open("_wk_1101_f1.txt").read().strip() if len(sys.argv) > 1 else "Ratio-scale estimates (caption pending proof)."
F2 = open("_wk_1101_f2.txt").read().strip() if len(sys.argv) > 1 else "Difference-scale estimates (caption pending proof)."
s = s.replace(r"\figcap{FOREST1}", r"\figcap{" + F1 + "}").replace(r"\figcap{FOREST2}", r"\figcap{" + F2 + "}")
open("build/weekly.tex", "w").write(s); print("ok", len(s))
