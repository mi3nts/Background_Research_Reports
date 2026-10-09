# -*- coding: utf-8 -*-
HEAD = dict(long="6 October 2026", window="6 October 2026 (full day)", n=11, excl=61,
            bands=6, eff=0, tierA=2, meta=4)

SIGNAL = r"""{\sffamily\bfseries\small\color{Deep}An emission-control policy moved mean particle diameter by
27\,\% --- which is a calibration drift no sensor firmware will ever report.}\\[1.4mm]
\footnotesize
Dai and colleagues (\textit{ACP}) ran single-particle aerosol mass spectrometry through winter and summer
emission-control periods in Yangzhou against matched normal periods, defining sulfur-to-nitrogen ratios in
the gas phase, the particle phase and by particle number. Cutting NO$_x$ while SO$_2$ stayed flat raised
the gas-phase ratio, lifted the particle-phase ratio by \textbf{$\sim$57\,\%} across particle classes, and
expanded mean vacuum aerodynamic diameter by \textbf{27\,\%}. Enrichment was largest in particles carrying
both black and organic carbon, least in BC-free inorganic particles.
\textbf{Caveat:} control periods are confounded with season and meteorology, and ``causal inference'' is a
strong label for an observational series with co-varying controls.
\textbf{Why it matters for sensing:} a nephelometric node's mass estimate is a fixed assumption about size
distribution and refractive index wrapped around a scattering measurement. A 27\,\% shift in mean diameter
changes the scattering cross-section per unit mass directly --- so a network calibrated before an emission
control reads differently after it, with no hardware change and nothing in the diagnostics to show for it.
Co-location drift studies attribute this to the sensor. It is not the sensor."""

CHANGED = [
r"""\textbf{Infiltration above 0.6 in naturally ventilated classrooms.} Ten Klang Valley primary schools
across five land-use classes: indoor 24\,h PM$_{2.5}$ peaked at mixed industrial/port schools
(\textbf{35.33\,$\pm$\,9.25}\,$\mu$g\,m$^{-3}$), outdoor at high-traffic schools (34.50\,$\pm$\,20.64), with
mean \textbf{F$_{\textrm{inf}}$ $>$ 0.6}. Two buildings per class confounds land use with building, and
F$_{\textrm{inf}}$ from indoor--outdoor ratios absorbs any indoor source --- but if it holds, outdoor
network data is a usable proxy for children's exposure in this climate.""",
r"""\textbf{Brain structure, without numbers.} 4,276 adults with repeated MRI: higher long-term PM$_{2.5}$
and PM$_{10}$ associated with accelerated grey-matter loss and greater white-matter-hyperintensity
progression. The abstract reports \textit{no} effect size, interval, exposure contrast, cohort name or
country, so the record is logged and cannot be entered as an estimate.""",
r"""\textbf{Italy's national attributable-burden platform.} PM$_{2.5}$ and NO$_2$ modelled at 1\,km by
random forest for 2016--2024, population-weighted to municipality level against the 2021 census, and run
through HRAPIE-2 functions to the WHO 5\,$\mu$g\,m$^{-3}$ counterfactual. The surface is validated against
the monitors that train it, and municipality-scale population weighting erases the within-city contrast ---
which is precisely the gap a dense network fills.""",
r"""\textbf{Port outflow at 4--10\,$\mu$g\,m$^{-3}$.} Four seasons of HR-ToF-AMS at a coastal receptor
downwind of Busan: five PMF organic factors, frequent ultrafine growth events, and oxidised primary organic
aerosol reaching \textbf{36\,\%} in autumn under north-easterly port transport. Growth events at that mass
loading are invisible to a mass-reporting network.""",
]

CONT = r"""The 5 October issue closed with \texttt{last\_entry\_date} at 5 October. This issue collects
\textbf{6 October in full}, continuous with it, and is the last day covered by the cached harvest. Harvest
and screening were completed on the 6 October run; this run authored from that cache without re-querying.
\textbf{Dailies for 7 and 8 October have not yet been harvested} and the W40 weekly (27 September--3
October) is still owed; both follow."""

CAPS = {
"f1_subtopics": r"""Subtopic assignment of the 11 in-scope records. \textbf{Six of ten bands populated};
\textit{Sensing} leads with three, \textit{Burden}, \textit{Exposure assessment} and \textit{Mechanistic
toxicology} two each, and one each for \textit{Neuro} and \textit{Occupational \& indoor}. The measurement
side holds 8 of 11 records --- the highest share of the backfill.""",
"f2_design_endpoint": r"""Left --- architecture: \textbf{four} measurement campaigns (the AMS receptor
site, the single-particle series, the school indoor--outdoor survey and the Kazakh elemental sampling),
\textbf{four} metadata-only deposits, and one each for the imaging cohort, the national health-impact
model and the coal-fire laboratory rig. Right --- only two records report a health endpoint, and one of
those (the brain-imaging cohort) reports it without a number.""",
"f3_metric_geography": r"""Left --- particle metric: PM$_{2.5}$ only \textbf{four}, unspeciated PM or
emissions three, PM$_{2.5}$ + PM$_{10}$ jointly two, and one each for size-resolved number distribution
(the submicron AMS record) and optical properties (the HULIS deposit). Right --- geography: China and
global / not stated \textbf{three} each, and one each for Europe, Southeast Asia, Central Asia, East Asia
excluding China, and South Asia --- Kazakhstan is the first Central Asian record since 29 September.""",
"f6_lifecourse": r"""Life-course windows: childhood one (the Klang Valley school measurement) and older
adults one (the repeated-MRI cohort). In utero, adolescence and working age have no record --- a day
dominated by atmospheric measurement rather than by population studies.""",
"f4_heatmap": r"""Subtopic $\times$ study architecture for the 11 records. Measurement campaigns occupy
sensing, exposure and occupational; the metadata-only block spans sensing, exposure and mechanistic
toxicology; burden holds the only two modelling-type records, one national and one at bench scale.""",
}

FOREST = r"""{\fontsize{7.4}{9}\selectfont\color{Slate}\textbf{No forest plot this issue.} No admitted
abstract reports a PM effect estimate with a confidence interval. The brain-imaging cohort is the only
record with an epidemiological estimand, and its abstract reports direction without magnitude, interval or
exposure contrast; the Kazakh hazard quotients and the Italian attributable fractions are risk-assessment
outputs, not estimated associations, and are excluded from the panel by the same rule that has excluded
them all series. The f5 panel is absent by design, not by build failure.\par}"""

PROV = r"""Entry window \textbf{6 October 2026}, single day, continuous with the 5 October issue. Harvest
and screening were completed on the \textbf{6 October} run and cached
(\texttt{cache/2026-10-06/\_fresh.json}); this run authored from that cache without re-querying.
\textbf{72} fresh candidates after cross-day deduplication, including \textbf{7} appended from the PubMed
connector; \textbf{OpenAlex} HTTP 429 again; \textbf{arXiv} answered (148\,kB) with no entry dated
6 October passing the recency gate. \textbf{11 admitted}, \textbf{61 rejected} with logged reasons.
\textbf{Four records carried on metadata alone} (36\,\%) --- the fourth consecutive issue above 25\,\%,
and one of them (\textit{Atmos.\ Environ.}, satellite-constrained inductive kriging) is the
highest-relevance record of the day despite having no abstract. \textbf{Consensus} returned 10 calibration
hits, \textbf{0 new}. \textbf{Scholar Gateway} fails with \texttt{ACCESS\_DENIED}.
\textbf{ClinicalTrials.gov} (LastUpdatePostDate 3--6 October): EPIC-AIR \texttt{NCT07500948} and a
CAN-EXACT update, both already in the trial watch. An \textit{Atmos.\ Environ.} retraction notice
(drought and PM$_{2.5}$ in Texas) appeared in the window and concerns no record in this corpus. DOI gate:
\textbf{0 fail, 1 warn} --- the \textit{Epidemiologia \& Prevenzione} supplement DOI resolves but is not in
Crossref, which is normal for that publisher and was confirmed by eye. Abstracts remain the copyright of
their respective publishers."""
