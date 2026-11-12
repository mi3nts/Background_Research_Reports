# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-10/_rec.py", encoding="utf-8").read(), globals())
P = [
 R(83, "BMC Psychiatry",
  short="Liu Xi'an UK Biobank PM2.5 PM10 PMcoarse NO2 NOx greenness incident substance use disorder Cox 10.9 y",
  sub=corpus.NEU, design="Prospective cohort",
  pm="Residential PM2.5, PM2.5-10, PM10, NO2, NOx from land-use regression; 300 m greenness",
  geo="UK", endpoint="Incident substance use disorder", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Xi'an Jiaotong University, China; Xi'an Jiaotong University, China",
  n=("247,138 UK Biobank participants free of substance use disorder at baseline; 4,982 incident cases over a median 10.9 years. All five "
     "pollutants were positively associated; PM2.5 strongest (HR 1.111, 1.081-1.142), then PM10 (1.070, 1.054-1.086); the increment is not "
     "stated in the abstract, so the size of these HRs cannot be interpreted. Green space (HR 0.997, 0.996-0.998) was inversely associated and "
     "domestic garden attenuated the pollutant HRs in the high-exposure group. Effects were largest in older men and ever-smokers, the strata where "
     "residual confounding by deprivation and smoking intensity is worst; baseline LUR surfaces stand in for decade-long exposure. "
     "Relevance: low - an LUR cohort result without an increment adds a hazard ratio that cannot be pooled.")),
 R(3, "Brain Behav",
  short="Lebiedz Chitnis Brigham MS Center PM2.5 satellite zip-code PIRA EDSS 6 Cox null northeastern US 2017-2023",
  sub=corpus.NEU, design="Retrospective cohort",
  pm="Monthly zip-code PM2.5 from an open satellite-derived dataset, baseline and time-varying annual means",
  geo="USA", endpoint="Time to progression independent of relapse activity (PIRA); time to EDSS >= 6", tier="B",
  basis="Satellite-fused", affil="Brigham and Women's Hospital, USA; University of Washington, USA",
  n=("3,040 people with MS at the Brigham MS Center, mean age 49.5, median EDSS 2.7, mean baseline PM2.5 5.8 ug/m3. Adjusted HRs were null for "
     "PIRA (baseline 1.01, 0.96-1.06; time-varying 0.98, 0.93-1.04) and for EDSS >= 6 (baseline 1.03, 0.94-1.13; time-varying 1.01, 0.92-1.10). "
     "The increment behind the HRs is not stated. Exposure contrast is narrow at New England levels, zip-code assignment blurs it further, and "
     "clinic-based retrospective ascertainment of PIRA is noisy, so the null mainly bounds large effects at low concentrations. "
     "Relevance: a well-powered null at ~6 ug/m3; resolving within-zip contrast would need denser measurement than satellite surfaces give.")),
 R(67, "GeoHealth",
  short="Yan Li Sun Yat-sen national cohort PM2.5 components OM BC SO4 NO3 NH4 arthritis quantile g-computation middle-aged older China",
  sub=corpus.OTHR, design="Prospective cohort",
  pm="Short- and long-term PM2.5 mass and components (OM, BC, SO4 2-, NO3-, NH4+), modelled surfaces",
  geo="China", endpoint="Arthritis prevalence", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Sun Yat-sen University, China; Sun Yat-sen University, China",
  n=("14,935 middle-aged and older adults in a nationally representative Chinese cohort; mixed-effects logistic regression and quantile "
     "g-computation. Both short- and long-term PM2.5 mass and organic matter, black carbon, sulfate and ammonium were reported to raise arthritis "
     "risk, with men and overweight or obese participants most vulnerable. The abstract gives no effect size, CI or increment, and does not say how "
     "arthritis was ascertained, so neither magnitude nor outcome specificity can be judged from the record. "
     "Component surfaces are correlated model products. "
     "Relevance: low until numbers appear; another component study where nitrate does not lead, unlike the Pearl River respiratory result today.")),
 R(8, "BMC Public Health",
  short="Guangzhou Tianjin Guizhou urolithiasis stone composition NO2 PM10 inverse U-shaped case-crossover 128000 stones",
  sub=corpus.OTHR, design="Time-stratified case-crossover",
  pm="Six criteria pollutants incl. PM2.5 and PM10 (fixed-site monitors) with meteorology",
  geo="China", endpoint="Laboratory-confirmed urinary stones by composition", tier="C",
  basis="Reference / regulatory monitor", affil="First Affiliated Hospital of Guangzhou Medical University, China; First Affiliated Hospital of Guangzhou Medical University, China",
  n=("25,374 analysed urinary stones in Guangzhou with validation in Tianjin (99,552) and Guizhou (3,021); conditional logistic regression and GAMs "
     "over lags 0-7 and 6- to 12-month averages. The robust signal is NO2, strongest at lags 0 and 2-4 for carbonate apatite and calcium oxalate. "
     "PM10 showed mainly inverse or U-shaped associations with overall and composition-specific risk, and a PM10-carbonate apatite pattern was "
     "confirmed in Guizhou; no PM effect sizes are given in the abstract. Stones are dated at analysis, not symptom onset, so short lags are "
     "misaligned with formation. "
     "Relevance: low - a PM null-to-inverse result in a gas-driven outcome, carried for completeness.")),
]
