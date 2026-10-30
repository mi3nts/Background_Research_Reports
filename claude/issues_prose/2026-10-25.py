# -*- coding: utf-8 -*-
HEAD = dict(long="25 October 2026", window="25 October 2026 (full day)", n=3, excl=52,
            bands=3, eff=0, tierA=0, meta=1)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}A Sunday floor issue: three records, and the most watch-relevant
point is that 3-D printing emits almost entirely below the optical cut of consumer PM sensors.}\\[1.4mm]
\footnotesize
Recycled plastic-bag HDPE extruded to filament and then 3-D printed (NIOSH chamber work): extrusion emits mostly
1.2--5.2\,nm particles, printing mostly 5.6--560\,nm, with number yields per gram \textbf{2--3 orders of magnitude}
higher during printing; formaldehyde 9.9--16.1\,$\mu$g\,g$^{-1}$ printed.
\textbf{Where it is weak:} yields are per mass processed in an enclosure, not breathing-zone concentrations, and
no uncertainty is attached to the contrast.
\textbf{Why it matters here:} a PMS-class optical node registers almost none of this number emission; maker-space
and indoor-occupational monitoring needs a condensation or diffusion-charging counter."""

CHANGED = [
r"""\textbf{Thin day, heavy overlap.} Ten of the 13 records that passed the topic screen had already been issued on
23, 24 or 26 October (Europe PMC re-surfacing PubMed entries one to two days late) and are logged as duplicates.""",
r"""\textbf{Single-monitor ceiling.} Cubat\~ao schoolchildren ($n$\,=\,77): HRV and spirometry associations are for
SO$_2$, O$_3$ and NO$_2$ assigned from one regulatory station; no PM association is reported.""",
r"""\textbf{Street-scale morphology thresholds} for PM$_{2.5}$/PM$_{10}$ (Atmos.\ Pollut.\ Res.) arrived as a
metadata-only Crossref deposit.""",
]

CONT = r"""The 22 October issue closed with \texttt{last\_entry\_date} at 22 October. The scheduled runs for 23--29
October did not complete (a 30 October 00:21 UTC run harvested 23--28 October but stopped before screening). This
issue was built on the \textbf{30 October 14:20 UTC (09:20 CDT) recovery run}, which backfills 23--29 October day by
day; it collects \textbf{25 October in full} (Sunday), continuous with the 24 October issue."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 3 in-scope records: respiratory (Cubat\~ao schoolchildren), occupational
\& indoor (3-D printing emissions) and exposure assessment (street-scale morphology, metadata-only).""",
"f2_design_endpoint": r"""Left --- architecture: one school-based cross-sectional study, one chamber emission
characterisation, one metadata-only record (1 of 3). Right --- endpoints: HRV/spirometry, emission yields, and
street-level concentration.""",
"f3_metric_geography": r"""Left --- particle metric: regulatory-monitor pollutants, nanoscale number emissions, and
PM$_{2.5}$+PM$_{10}$. Right --- geography: Brazil, United States (laboratory), and one not stated.""",
"f6_lifecourse": r"""Life-course windows: one childhood record (Cubat\~ao) and one working-age occupational record;
no in-utero, adolescent or older-adult record today.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture. Three singleton cells; no cohort, trial or effect estimate
with a confidence interval today, so no forest plot is drawn.""",
}

FOREST = ""

PROV = r"""Entry window \textbf{25 October 2026}, single day (Sunday). Harvester legs (run 30 October 00:21 UTC):
\textbf{PubMed} health \textbf{12}, sensing \textbf{1}; \textbf{Europe PMC} \textbf{68}; \textbf{Crossref by ISSN}
\textbf{7}; \textbf{arXiv} 150 kB, no in-window entry; \textbf{OpenAlex} HTTP 429. PubMed connector (EDAT 23--28 Oct,
one backfill query bucketed by entry date) appended 1. \textbf{55 screened}. \textbf{3 admitted}, \textbf{52
rejected} with logged reasons, 10 of them cross-day duplicates of the 23, 24 and 26 October issues. \textbf{DOI gate}
0 fail / 0 warn. \textbf{0 effect estimates with a CI} --- no forest plot. \textbf{1 carried on metadata alone}.
Consensus sweep and trial watch were run once for the 23--29 October backfill and are reported in the 29 October
issue. Abstracts remain the copyright of their publishers."""
