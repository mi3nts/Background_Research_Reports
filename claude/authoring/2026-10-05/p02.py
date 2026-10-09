# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.5194/acp-26-13885-2026", journal="Atmos Chem Phys",
  short="Mei et al. 2026",
  title="Synthesis of the tethered balloon system and other TRACER campaign measurements elucidates aerosol property profiles",
  sub=corpus.SENS, design="Long-term field measurement campaign",
  pm="Vertical profiles of aerosol number concentration and size distribution; CCN inferred by kappa-Koehler",
  geo="USA (Houston, Texas)", endpoint="None (aerosol profile)", tier="B",
  n=("149 tethered-balloon flights over greater Houston in summer during the DOE ARM TRACER campaign, with "
     "back-trajectory k-means clustering into marine, mixed and urban/long-range air masses. Profiles vary "
     "strongly with cluster, modulated by boundary-layer depth and coastal circulation; the marine cluster "
     "had CCN at 0.8% supersaturation below 1,000 cm-3, urban and mixed clusters higher. Limitation: one "
     "coastal city, one summer, and CCN is inferred from size distribution under an assumed kappa rather "
     "than measured, so composition heterogeneity propagates straight into the activated fraction; "
     "tethered-balloon sampling is intermittent and fair-weather-biased. Relevance: high - this is the "
     "measurement that exposes the central fiction of a surface network, namely that a 2 m reading "
     "represents the column a satellite retrieval sees.")),

 dict(pmid="42832517", doi="10.1371/journal.pone.0359706", journal="PLoS One",
  short="Ketsakorn and Chaiyadej 2026",
  title="Probabilistic health risk assessment of respirable dust exposure among stone carvers in Thailand using average daily dose and Monte Carlo simulation",
  sub=corpus.OCC, design="Observational - cross-sectional",
  pm="Personal respirable dust, NIOSH 7601, 8-h TWA across five task groups",
  geo="Thailand", endpoint="Incremental lifetime cancer risk (modelled)", tier="C",
  n=("Personal sampling across mining, cutting, splitting, knocking and carving, with a 10,000-iteration "
     "Monte Carlo ILCR using US EPA exposure parameters. Mean respirable dust was below both the Thai OEL "
     "and the TLV everywhere, highest in carving at 0.051 mg/m3; ILCR stayed under 1e-6, highest in carving "
     "at 3.3e-7. Limitation: respirable dust mass is the wrong metric for a silica hazard - no crystalline "
     "silica fraction is reported, and an EPA inhalation-unit-risk framework applied to a mixed mineral "
     "dust produces a number with no established exposure-response behind it; small sample, one season. "
     "Relevance: low-moderate - the task-level contrast is exactly what a wearable logging monitor "
     "resolves and a single shift-average sample does not.")),

 dict(pmid="42832150", doi="10.1007/s11356-026-38275-w", journal="Environ Sci Pollut Res Int",
  short="Chavan and Lataye 2026",
  title="Application of Openair package in R programming and PCA: unveiling air quality dynamics and meteorological influences",
  sub=corpus.EXPO, design="Monitoring-record analysis",
  pm="2023 CAAQMS records: PM10, PM2.5 with six co-pollutants and four meteorological variables",
  geo="India (Nagpur)", endpoint="None (air quality baseline)", tier="C",
  n=("A full year of regulatory monitoring data for a tier-2 Indian city analysed with openair and PCA. "
     "Winter AQI reached 492 (severe) in February with monsoon improvement; varimax PCA gave two components "
     "explaining 73.1% of variance, read as anthropogenic combustion (PM, NO2) and photochemistry "
     "(O3, temperature); PM2.5 and PM10 exceeded CPCB standards on 27-29 days per winter month. "
     "Limitation: descriptive reanalysis of one station-year with no source apportionment, no receptor "
     "model and no validation - PCA components here are correlation structure, not sources, and the policy "
     "recommendations do not follow from the analysis. Relevance: low as method, moderate as a reminder "
     "that tier-2 cities have one regulatory station and no spatial information at all.")),

 dict(pmid="", doi="10.3390/atmos17100974", journal="Atmosphere",
  short="Zhao et al. 2026b",
  title="Pollution Characteristics, Influencing Factors and Health Risk Assessments of Mercury in Atmospheric PM2.5 from Xinxiang, China",
  sub=corpus.BURD, design="Source apportionment",
  pm="PM2.5-bound mercury with OC/EC, water-soluble ions and trace elements, full-year 2015 sampling",
  geo="China (Xinxiang, Henan)", endpoint="Non-carcinogenic hazard index (modelled)", tier="C",
  n=("Year-long filter sampling gives an annual mean PM2.5-bound Hg of 0.399 ng/m3, significantly higher in "
     "winter (p<0.001) and in the heating than the non-heating period, positively correlated with SO2, CO, "
     "PM2.5, OC, EC, Cl-, Zn and Ca and negatively with temperature, O3 and V - a coal-combustion "
     "signature. Hazard index 2.06e-3 (children) and 8.46e-4 (adults), both far below 1, with ingestion "
     "the dominant modelled pathway. Limitation: the samples are from 2015 and describe an emissions "
     "regime two major control phases out of date; an ingestion-dominant pathway for an airborne metal is "
     "an artefact of the EPA soil-oriented default parameters. Relevance: low - logged as a composition "
     "time point, not as a risk estimate.")),
]
