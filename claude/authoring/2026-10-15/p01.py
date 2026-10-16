# -*- coding: utf-8 -*-
P = [
 dict(pmid="42880579", doi="10.1016/j.envpol.2026.129345", journal="Environ Pollut",
  short="Guangdong CHD PM2.5 constituents 2026",
  title="Differential Impacts of Fine Particulate Matter Constituents on Congenital Heart Disease across Critical Periconceptional Windows",
  sub=corpus.REPR, design="Case-control study", pm="Residential PM2.5 mass and constituents (sulfate, nitrate, ammonium, BC, OM) by periconceptional window",
  geo="China (Guangdong)", endpoint="Congenital heart disease (incl. conotruncal defects)", tier="A",
  n=("Guangdong CHD Registry 2004-2022: 12,680 cases, 10,266 controls, multilevel logistic regression by exposure window. "
     "Per-IQR increments of PM2.5 mass and constituents raised CHD odds 9-16%, strongest in the preconception window and "
     "attenuating later; BC and nitrate stayed associated during pregnancy. Conotruncal defects carried the largest ORs "
     "(1.14-1.36 per IQR). Mixture models put sulfate and BC first preconception, BC and nitrate thereafter. Limitation: "
     "constituents are modelled and mutually collinear, so 'dominant constituent' rankings are mixture-model artefacts as "
     "much as biology; registry controls and the higher-SES amplification hint at ascertainment differences. CIs absent "
     "from the abstract. Relevance: moderate - constituent-resolved windows need speciation, which optical LCS cannot "
     "supply; BC from multi-wavelength nodes is the tractable piece.")),
 dict(pmid="42880149", doi="10.1016/j.ecoenv.2026.120919", journal="Ecotoxicol Environ Saf",
  short="UKB arrhythmia NMR metabolome mediation 2026",
  title="Large-scale plasma metabolic profiling identifies signatures and biomarkers associated with air pollution and arrhythmias: A prospective cohort study from UK Biobank",
  sub=corpus.CVM, design="Prospective cohort", pm="LUR PM2.5, PM10, NO2, NOx at baseline residence",
  geo="United Kingdom (UK Biobank)", endpoint="Incident arrhythmia (AF, SVT, intraventricular block)", tier="A",
  n=("449,068 UK Biobank participants free of arrhythmia, median follow-up 16.3 y, 47,381 incident cases. All four "
     "pollutants were associated with arrhythmia, HR 1.015-1.257 per 10 ug/m3 (range across pollutants; CIs not in the "
     "abstract). An elastic-net signature from 170 NMR metabolites mediated 11.2% of the PM2.5 association (PM10 5.2%, "
     "NO2 7.4%, NOx 9.8%); lipid, ketone-body and amino-acid pathways recurred, ketone bodies most for intraventricular "
     "block. Limitation: single-baseline 2010 LUR exposure and single-time metabolomics make mediation cross-sectional in "
     "disguise; ketone bodies track fasting and diabetes status. Relevance: low-moderate for sensing - another UKB "
     "LUR result whose exposure contrast is too smooth to need dense monitoring.")),
 dict(pmid="42879685", doi="10.1093/annweh/wxag088", journal="Ann Work Expo Health",
  short="Creosote railroad switch PAH workers 2026",
  title="Assessing PAH exposure during construction work of railroad switches using creosote-impregnated ties",
  sub=corpus.OCC, design="Field measurement", pm="Full-shift breathing-zone PAH (16 EPA priority; particle + vapour), dermal tape strips, urinary 1-HP",
  geo="Sweden", endpoint="Urinary 1-hydroxypyrene (biomarker)", tier="C",
  n=("Workers assembling railroad switches from creosote ties: breathing-zone sum of 16 PAHs 120,000-280,000 ng/m3 on a "
     "single sampled shift; skin pyrene 0.31-140 ng/cm2, highest on palms and calves; urinary 1-HP rose across the week "
     "(1.9-17 umol/mol creatinine), most above the UK guidance value by day 4. A PBTK model attributed uptake mainly to the "
     "dermal route, and pyrene under protective clothing implies fabric penetration. Limitation: one air-sampling shift, "
     "small crew, and the particle/vapour split is not reported, so the inhalation share rests on the model. Relevance: "
     "low for ambient sensing - a reminder that biomarker-based particulate PAH exposure is not reducible to air "
     "concentration.")),
 dict(pmid="42877688", doi="10.1021/acsestair.6c00125", journal="ACS EST Air",
  short="Pu Lima hybrid transfer-learning PM2.5 2026",
  title="A Hybrid Transfer Learning Approach for Ambient PM2.5 Exposure Modeling in LMIC Contexts: A Case Study from Lima, Peru",
  sub=corpus.EXPO, design="Machine-learning model", pm="Daily 1 km PM2.5 from reference + low-cost monitors, MAIAC AOD, WRF-Chem and covariates",
  geo="Peru (Lima)", endpoint="No health endpoint", tier="A",
  n=("Lima 2010-2023 daily PM2.5 surface from an instance-weighted random forest that fuses reference and low-cost "
     "monitor data, satellite AOD and WRF-Chem. Sampling bias toward monitored districts is handled by geo-environmental "
     "similarity transfer learning that borrows weighted training instances from the US. Cross-validated R2 0.76; "
     "predicted mean PM2.5 in mountainous districts fell from 34.19 to 29.23 ug/m3 versus the unweighted model. "
     "Limitation: CV R2 is computed on the same biased monitor locations the method claims to correct, so the "
     "mountain-region gain is unverified by held-out sites there; how low-cost data were calibrated is not stated. "
     "Relevance: high - a template for using sparse LCS networks plus transfer learning in data-poor cities.")),
]
