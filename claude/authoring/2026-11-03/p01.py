# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.21203/rs.3.rs-11388680/v1", journal="Research Square (preprint)",
  short="Yadav CUPI-G low-cost sensor assimilation WRF-Chem Delhi stubble burning 2026",
  title="Can Low-Cost Sensor Networks Improve Analysis of Extreme Pollution Episodes in Delhi During Stubble Burning?",
  sub=corpus.SENS, design="Data assimilation experiment", pm="Twice-daily PM2.5 from 33 CUPI-G low-cost sensors assimilated into WRF-Chem by 3D-Var",
  geo="India (Punjab, Haryana, Delhi)", endpoint="Forecast mean fractional bias and AQI category hit rate", tier="A",
  basis="Low-cost sensor / network", affil="Indian Institute of Tropical Meteorology, India; Indian Institute of Tropical Meteorology, India",
  n=("November 2024 post-monsoon burning season. Assimilating 33 rural source-region low-cost PM2.5 nodes cut the mean fractional bias over Haryana from "
     "-116.7% to -56.8%, and the Severe AQI category was recovered in about 95% of Delhi cases and 100% of Punjab and Haryana cases, where the control run "
     "predicted no Severe case at all. A second experiment using a 1.5 ug/m3 observation error, the reference-monitor value, improved further, so the "
     "assumed observation error, not the sensor count, sets the gain. Limitation: one month, one burning season, a preprint, and no co-location statistics "
     "for the CUPI-G nodes, so the 10% error is asserted rather than demonstrated. Relevance: direct - the strongest case to date that uncalibrated-grade "
     "source-region nodes carry forecast-relevant information.")),
 dict(pmid="", doi="10.21203/rs.3.rs-11579816/v1", journal="Research Square (preprint)",
  short="Zhang source-resolved PM2.5 metals Bayesian inversion California hazard index 2026",
  title="Source-Resolved PM2.5 Metals Emissions, Exposure, and Health Risks in California Using an Observation-Constrained Hybrid Model",
  sub=corpus.EXPO, design="Chemical-transport modelling with Bayesian inversion", pm="23 PM2.5-bound metals across 11 source sectors, source-oriented CTM constrained by monitor data",
  geo="North America (California)", endpoint="Population-weighted exposure, hazard index, excess lifetime cancer risk", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Lawrence Berkeley National Laboratory, USA; Lawrence Berkeley National Laboratory, USA",
  n=("Source-oriented CTM output was reconciled with observations by Bayesian inversion, lowering the mean fractional error from 0.835 to 0.511. "
     "Miscellaneous sources supplied 9.1% of emissions but 24.1% of population-weighted exposure and 57.7% of the non-carcinogenic hazard index, driven by "
     "cadmium; industrial and miscellaneous sectors each carried roughly 35% of excess lifetime cancer risk across six carcinogenic metals. Census-tract "
     "clusters with joint contributions from both sectors were concentrated in metropolitan Los Angeles. No CI on any figure. Limitation: a preprint, and the "
     "inversion is only as good as the sparse speciation network that constrains it, which is the same sparsity the paper is trying to overcome. "
     "Relevance: moderate - mass-only sensing is blind to exactly the composition that drives these risk gradients.")),
 dict(pmid="42973650", doi="10.1007/s40201-026-01010-1", journal="J Environ Health Sci Eng",
  short="Sotiropoulou smart bench low-cost sensors Attica exposure AirQ+ FAIRCITY 2026",
  title="Smart city developments: Pilot case study of smart benches usage for impact assessment due to exposure to air pollution in the urban environment.",
  sub=corpus.SENS, design="Pilot field measurement with health-impact modelling", pm="PM2.5, PM10, NO2 and O3 from an IoT low-cost smart-bench station",
  geo="Europe (Attica, Greece)", endpoint="Population exposure, received dose, attributable respiratory admissions", tier="C",
  basis="Low-cost sensor / network", affil="National Observatory of Athens, Greece; National Observatory of Athens, Greece",
  n=("A single IoT smart-bench node in a dense Attica district fed exposure and dose estimates for two population groups, with short-term respiratory "
     "admissions quantified in WHO AirQ+. O3 exceeded PM2.5, PM10 and NO2 by more than a factor of two; NO2 doubled in the cold season; PM10 breached the EU "
     "limit value in both seasons. Adolescents carried roughly double the general-population exposure through longer time in the district, while attributable "
     "admissions were an order of magnitude higher for the working-age group on population size alone. No CI, and no reference co-location is reported for the "
     "bench. Limitation: one node standing for a district, and AirQ+ coefficients imported wholesale. Relevance: direct, as a worked example of how far a "
     "single low-cost node is pushed in municipal practice.")),
 dict(pmid="42975724", doi="10.1007/s10661-026-16103-5", journal="Environ Monit Assess",
  short="Andino intra-urban PM2.5 PM10 meteorological GAM arid San Juan Argentina 2026",
  title="Intra-urban variability and meteorological drivers of PM(2.5) and PM(10) concentrations in an arid Argentine city.",
  sub=corpus.EXPO, design="Multi-site monitoring campaign", pm="PM2.5 and PM10 with co-located meteorology across residential, industrial and commercial zones",
  geo="South America (San Juan, Argentina)", endpoint="Land-use-zone contrasts and meteorological predictors of PM", tier="B",
  basis="Reference / regulatory monitor", affil="Universidad Nacional de San Juan, Argentina; Universidad Nacional de San Juan, Argentina",
  n=("Cold-season campaign across three land-use zones in an arid metropolitan area, with generalized additive models over temperature, humidity, pressure, "
     "wind speed and direction, and radiation. Industrial and commercial zones ran highest and residential lowest, with morning and evening peaks. Pressure "
     "and wind speed were the dominant predictors; PM2.5 responded to atmospheric stability and low wind, PM10 to wind-driven resuspension. No effect sizes, "
     "CIs or deviance explained in the abstract, and the campaign is short-term, so the zone contrast confounds season with siting. Relevance: moderate - the "
     "PM2.5/PM10 split in meteorological response is the physical reason a single correction factor fitted on one fraction transfers badly to the other in "
     "dust-dominated cities.")),
]
