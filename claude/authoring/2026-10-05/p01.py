# -*- coding: utf-8 -*-
P = [
 dict(pmid="42832702", doi="10.1097/ede.0000000000002054", journal="Epidemiology",
  short="Batisse et al. 2026",
  title="Long-term exposure to ultrafine particles and mortality from neurodegenerative diseases: a population-based cohort study",
  sub=corpus.NEU, design="Retrospective cohort",
  pm="High-resolution UFP number concentration and UFP size at residential postal code, 3-year moving average",
  geo="Canada (Montreal and Toronto)", endpoint="Dementia, Parkinson's disease, ALS mortality", tier="A",
  n=("2.1 million adults in the Canadian Census Health and Environment Cohorts, 2001-2019, 19 million "
     "person-years and 20,560 neurodegenerative deaths. Per 10,000 particles/cm3 of UFP number, dementia "
     "mortality HR 1.22 (95% CI 1.17-1.27), strengthened after adjustment for UFP size; positive for every "
     "dementia subtype, largest for vascular dementia. Models were run with and without inverse-probability "
     "censoring weights for competing events and adjusted for co-pollutants. Limitation: postal-code "
     "exposure from a land-use-regression UFP surface, no mobility or indoor time, and cause of death on "
     "the death certificate under-ascribes dementia; UFP number and NO2 share the traffic gradient, so "
     "co-pollutant adjustment cannot fully separate them. Relevance: high - UFP is unregulated and "
     "unmeasured by every optical low-cost node, which sees mass, not number; this is the strongest "
     "current argument for CPC-class instruments in dense networks.")),

 dict(pmid="42831997", doi="10.1007/s00439-026-02875-w", journal="Hum Genet",
  short="Tian et al. 2026",
  title="Annual average exposure to ambient air pollution, polygenic risk, and incidence of major chronic diseases: a large-scale prospective cohort study",
  sub=corpus.OTHR, design="Prospective cohort",
  pm="Annual PM2.5, PM10, NO2, NOx at residence from land-use regression",
  geo="United Kingdom (UK Biobank)", endpoint="Cardiovascular, respiratory, neurodegenerative, hypertension, diabetes incidence", tier="A",
  n=("313,534 UK Biobank participants with LUR annual pollutant estimates and weighted polygenic risk "
     "scores for each of five disease groups; Cox models with RERI and AP for additive interaction. PM2.5 "
     "carried the strongest association, HR 1.22 per 5 ug/m3 (95% CI 1.19-1.26); high genetic risk acted "
     "independently (diabetes HR 1.77 per SD of PRS), with significant additive interaction between high "
     "PRS and high PM2.5 for neurodegenerative disease (RERI 0.14) and diabetes (RERI 0.21). Limitation: "
     "UK Biobank is a healthy-volunteer cohort with a narrow PM2.5 range, the LUR surface is a single "
     "baseline-era estimate carried forward, and five outcomes with four pollutants invites selective "
     "emphasis - the interaction terms are modest and not corrected for multiplicity. Relevance: moderate - "
     "gene-environment interaction raises the value of resolving exposure well at the individual level, "
     "which is the case for personal rather than ambient monitoring.")),

 dict(pmid="42832616", doi="10.1080/09603123.2026.2733112", journal="Int J Environ Health Res",
  short="Howlett-Downing and Wichmann 2026",
  title="Triangulating health risks of PM2.5 and trace elements in Pretoria: evidence from health risk assessment, case-crossover, and concentration-response function analyses",
  sub=corpus.RESP, design="Time-stratified case-crossover",
  pm="Sampled PM2.5 mass and PM2.5-bound trace elements, Apr 2017 - Feb 2020",
  geo="South Africa (Pretoria)", endpoint="Respiratory hospital admissions (ICD-10 J00-J99)", tier="B",
  n=("Three methods applied to the same secondary dataset: hazard quotients, a case-crossover analysis and "
     "concentration-response functions. Hazard quotients exceeded unity in adults, children and infants; "
     "the case-crossover OR was 1.027 (95% CI 1.006-1.049) per 10 ug/m3 PM2.5. Meeting the South African "
     "standard would avert 158 admissions annually, rising to 342 and 748 under the WHO daily and annual "
     "guidelines; element-specific functions give 110-608. Limitation: the three methods are not "
     "independent evidence - they re-use one exposure series from a small number of sampling days, and "
     "summing element-specific attributable cases double-counts the mass they are part of; hazard "
     "quotients are screening-level and not comparable to epidemiological risk. Relevance: moderate - "
     "Southern African monitoring is thin, and a saturation low-cost network would resolve the "
     "within-city contrast this design cannot.")),

 dict(pmid="42833334", doi="10.1016/j.envpol.2026.129270", journal="Environ Pollut",
  short="Chang et al. 2026",
  title="Wintertime vertical stratification of air pollutants and meteorological associations within an urban forest canopy in Shenyang, China",
  sub=corpus.SENS, design="Long-term field measurement campaign",
  pm="PM2.5, PM10 with O3, NO2, SO2, CO and meteorology at 1.5, 10 and 20 m",
  geo="China (Shenyang)", endpoint="None (vertical profile)", tier="B",
  n=("A three-level monitoring mast inside an urban forest in a cold-climate northern Chinese city through "
     "the winter heating season. PM2.5 and PM10 were generally higher at 10 and 20 m than at pedestrian "
     "level, O3 and CO higher at 1.5 m, and NO2 and SO2 peaked mid-canopy; relative humidity and wind speed "
     "dominated the statistical and machine-learning associations, but height-dependently. Limitation: one "
     "site, one winter, no replication mast and no flux measurement, so the inversion of the usual "
     "near-ground maximum is described rather than explained - and at wintertime humidity, uncorrected "
     "optical PM readings are themselves height-correlated through the humidity profile. Relevance: high - "
     "siting guidance for low-cost networks assumes a well-mixed layer below canopy height; this is direct "
     "evidence that the 1.5 m reading is not the 20 m reading.")),
]
