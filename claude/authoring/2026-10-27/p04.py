# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1093/eurpub/ckag169.807", journal="Eur J Public Health (conference abstract)",
  short="Poland air pollution COPD asthma emergency admissions DLNM heating season 2026",
  title="Air pollution and respiratory admissions in Poland: a nationwide DLNM analysis of COPD and asthma",
  sub=corpus.RESP, design="Distributed-lag time-series", pm="PM10, PM2.5, NO2, SO2, PAHs and metals in PM10 (national monitoring)",
  geo="Poland (nationwide, 2012-2019)", endpoint="Emergency hospitalisations for COPD and asthma", tier="B",
  n=("National registry: 625,597 COPD and 153,563 asthma emergency admissions (32,893 paediatric), DLNM lag 0-10, "
     "stratified by heating season. Associations appeared only in the heating season: COPD RR per IQR PM2.5 1.044, PM10 "
     "1.039, SO2 1.055; lead 1.072, benzo[a]anthracene 1.057. Adult asthma stronger (PM2.5 1.100). In children, PM was "
     "not significant; arsenic (1.124) and ozone (1.115) were. NO2 null throughout. No CIs in the abstract. Limitation: "
     "component and pollutant RRs come from single-pollutant models on collinear coal-combustion tracers, so 'lead' and "
     "'PAH' effects cannot be separated from PM2.5; conference abstract. Relevance: moderate - heating-season coal "
     "signatures are where speciation-capable nodes add value over mass.")),
 dict(pmid="", doi="10.1093/eurpub/ckag169.1053", journal="Eur J Public Health (conference abstract)",
  short="K-HEALTHinAIR indoor PM2.5 COPD attributable burden Spanish households 2026",
  title="Attributable Burden of COPD from Indoor PM2.5 Exposure in Spanish Households, 2025",
  sub=corpus.BURD, design="Burden estimation", pm="Measured indoor PM2.5 in Spanish homes (K-HEALTHinAIR)",
  geo="Spain", endpoint="COPD DALYs attributable to indoor PM2.5", tier="C",
  n=("Comparative risk assessment combining measured household PM2.5 (K-HEALTHinAIR), GBD 2023 Spanish rates and published "
     "exposure-response functions. Mean attributable COPD burden ~116 thousand DALYs; by household type, homes with "
     "smokers 327 thousand, air-conditioning for heating 183 thousand, no climate control 192 thousand, gas cooking 119 "
     "thousand. Limitation: applying ambient-derived ERFs to indoor PM2.5 of different composition (tobacco, cooking) and "
     "scaling household-type estimates to national totals as if every home were that type; the subgroup figures are not "
     "additive and no uncertainty is given. Conference abstract. Relevance: moderate - burden estimates driven by "
     "low-cost indoor measurements.")),
 dict(pmid="", doi="10.1093/eurpub/ckag169.955", journal="Eur J Public Health (conference abstract)",
  short="Scotland prenatal PM2.5 infant amoxicillin birthweight mediation 2026",
  title="Prenatal PM2.5 and Infant Antibiotics: Birth-Weight Mediation via Causal Analysis",
  sub=corpus.REPR, design="Prospective cohort (registry linkage)", pm="Annual postcode PM2.5, pregnancy-month weighted (mean 7 ug/m3)",
  geo="United Kingdom (Scotland, 2009-2018)", endpoint=">=1 amoxicillin prescription in first year (respiratory infection proxy)", tier="B",
  n=("All Scottish singleton births 2009-2018, n=498,123, linked registries; g-computation mediation comparing observed "
     "PM2.5 with a counterfactual of 5 ug/m3. Controlled direct effect OR 1.12 (1.10-1.14); interventional direct OR 1.12 "
     "(1.11-1.14); indirect via birthweight 0.99 (0.99-1.01). Limitation: exposure IQR is only 6-8 ug/m3, so a 12% excess "
     "over a ~2 ug/m3 counterfactual shift is implausibly large and points to residual area-level confounding "
     "(deprivation, prescribing culture); amoxicillin dispensing is a weak infection proxy. Preliminary conference "
     "abstract. Relevance: low-moderate - fine-scale exposure contrast is too narrow for postcode annual means.")),
 dict(pmid="", doi="10.1093/eurpub/ckag169.809", journal="Eur J Public Health (conference abstract)",
  short="UK Air Quality Cell PM10 plume back trajectory tyre fire Mexborough vulnerability 2026",
  title="Back trajectory modelled PM10 plumes: population vulnerability profile from an uncontrolled fire",
  sub=corpus.EXPO, design="Event-based monitoring", pm="Incident PM10 monitoring + ADMS-STAR back-trajectory plume (22 hourly plumes)",
  geo="United Kingdom (Mexborough, England)", endpoint="Population exposed by AQI band; socioeconomic profile", tier="B",
  n=("The UK Air Quality Cell monitored PM10 during an uncontrolled tyre fire; 22 hourly ADMS-STAR back-trajectory plumes "
     "were spatially averaged and overlaid on Output Areas. 24,952 residents fell in 'Unhealthy for Sensitive Groups' or "
     "worse; 7,856 (31.5%) in 'Hazardous' or beyond. Exposed areas had above-median deprivation, prior ill health and "
     "lower education. The modelling suggested field monitoring under-captured peaks. Limitation: AQI bands from a "
     "24 h index were applied to hourly plume concentrations, and exposure is residential, ignoring sheltering and "
     "evacuation; no health outcomes. Conference abstract. Relevance: high - rapid-deploy sensor arrays around industrial "
     "fires would close the peak-capture gap the authors identify.")),
]
