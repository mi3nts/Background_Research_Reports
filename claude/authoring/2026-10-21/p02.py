# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.3389/fpubh.2026.1950282", journal="Front Public Health",
  short="Sun long-term air pollution lipid profiles Shanxi repeated measures 2026",
  title="Long-term exposure to ambient air pollution and lipid profiles: a longitudinal study in a heavily industrialized region of northern China",
  sub=corpus.CVM, design="Prospective cohort", pm="3-y mean PM2.5, PM10 (ChinaHighAirPollutants, geocoded residence)",
  geo="China (Shanxi Province)", endpoint="TG, TC, LDL-C, HDL-C; dyslipidaemia", tier="B",
  n=("Repeated-measures study of 9,040 adults with 19,113 lipid measurements from a health-screening programme, 2019-2023. "
     "Per 10 ug/m3 PM2.5: TG +1.85%, TC +1.70%, LDL-C +1.81%, HDL-C -1.55% (linear mixed models); PM10, NO2, SO2 and O3 "
     "in the same direction, CO weaker; age modified the HDL-C association after FDR correction. Limitation: a "
     "health-screening population self-selects; CHAP is itself trained on the sparse Shanxi monitor network that "
     "underrepresents coal-industry hotspots, and with five correlated pollutants the 'PM2.5 most pronounced' ranking "
     "is not identified from single-pollutant models. Lipids are sensitive to fasting status, not mentioned. "
     "Relevance: moderate - industrial-region exposure surfaces are where LCS densification would most change CHAP errors.")),
 dict(pmid="", doi="10.21203/rs.3.rs-10964316/v1", journal="Research Square (preprint)",
  short="Mai population-weighted PM2.5 O3 China 2015-2024 preprint 2026",
  title="Population Weighted Ambient PM2.5 and O3 Concentrations in China from 2015 to 2024",
  sub=corpus.EXPO, design="Exposure model (secondary data)", pm="Annual ~1 km CHAP PM2.5 and O3 weighted by WorldPop",
  geo="China (national)", endpoint="Population-weighted vs geographic-mean concentration trends", tier="C",
  n=("Ecological geospatial analysis of annual ~1 km CHAP PM2.5/O3 rasters matched to WorldPop counts, 2015-2024. "
     "Population-weighted PM2.5 fell from 53.06 to 31.25 ug/m3 (-41.1%) while population-weighted O3 rose from 77.06 to "
     "96.75 ug/m3 (+25.6%); the population-weighted minus geographic gap narrowed for PM2.5 (5.77 to 2.43) and widened for O3 "
     "(1.01 to 2.72). 97.4% of 0.2-degree blocks show falling PM2.5 with rising O3 at a 0.5 ug/m3/y threshold. Limitation: "
     "purely descriptive and inherits CHAP's ML smoothing; no uncertainty on the weighted means; preprint, not peer reviewed. "
     "Relevance: moderate - the narrowing urban-rural PM2.5 gap shifts LCS value toward peri-urban and rural siting.")),
 dict(pmid="42903623", doi="10.1021/envhealth.6c00080", journal="Environ Health (ACS)",
  short="Liu PM2.5 IL-17 microglia neuroinflammation 2026",
  title="IL-17 Signaling Pathway: A Potential Signaling Pathway Mediating Neuroinflammation Induced by PM2.5",
  sub=corpus.MECH, design="Animal + in vitro", pm="Collected PM2.5 suspension (dose not stated in abstract)",
  geo="Laboratory", endpoint="Microglial viability, IL-17/NF-kB/MAPK activation, neurobehaviour", tier="C",
  n=("BV2 microglia exposed to PM2.5 lost viability and raised inflammatory cytokines; microarray DEGs enriched for "
     "inflammatory GO terms and the KEGG IL-17 pathway with downstream NF-kB and MAPK. An anti-IL-17A antibody reversed "
     "cytokine release, microglial activation and behavioural deficits (implying an in vivo arm). Limitation: the abstract "
     "gives no PM2.5 source, composition or dose, so environmental relevance cannot be judged; BV2 is an immortalised "
     "murine line with an exaggerated inflammatory phenotype, and IL-17 is usually T-cell/gamma-delta derived, so "
     "microglial IL-17 signalling needs cell-type attribution. Relevance: low - mechanistic only.")),
 dict(pmid="42903402", doi="10.1021/envhealth.5c00779", journal="Environ Health (ACS)",
  short="Ge preconception folic acid air pollution birthweight 2026",
  title="Preconception Folic Acid Supplementation Associated with Attenuated Effects of Air Pollution on Birthweight Outcomes",
  sub=corpus.REPR, design="Metadata only (no abstract)", pm="Ambient air pollution (metrics not stated in record)",
  geo="China (inferred from author group; not stated in record)", endpoint="Birthweight outcomes", tier="C",
  n=("Title and authors only (Ge, Zhang, Liao ... Berhane, Bai et al.); no abstract retrievable from PubMed, Europe PMC, "
     "Crossref or Semantic Scholar at harvest. The title claims effect modification of the air pollution-birthweight "
     "association by preconception folic acid use. Pollutants, cohort, n and effect sizes cannot be stated. Limitation: "
     "unverifiable beyond the title; supplement use is self-reported and strongly socially patterned, so 'attenuation' by "
     "folate is exposed to confounding by SES and antenatal-care quality unless handled explicitly. Relevance: low - "
     "no sensing content evident.")),
]
