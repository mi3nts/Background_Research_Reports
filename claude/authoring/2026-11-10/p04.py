# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-10/_rec.py", encoding="utf-8").read(), globals())
P = [
 R(66, "GeoHealth",
  short="CUHK CESM XGBoost 0.1 degree PM2.5 mortality GEMM SSP1 SSP2 SSP3 SSP5 2010 2050 emissions climate land use",
  sub=corpus.BURD, design="Integrated emission-air quality-health modelling",
  pm="Annual PM2.5 from CESM bias-corrected and downscaled to 0.1 degree by XGBoost",
  geo="Global / multi-region", endpoint="PM2.5-attributable deaths by age and cause, 2010 and 2050", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Chinese University of Hong Kong, China; Chinese University of Hong Kong, China",
  n=("CESM factorial runs separating emissions, climate and land-use change, bias-corrected and refined to 0.1 degree with XGBoost, fed to GEMM. "
     "Present-day burden about 6.13 million deaths in 2010 (UI 5.77-6.48); by 2050 SSP1 removes about 1.1 million deaths and SSP3 adds about "
     "0.5 million. Emissions dominate, climate change offsets part of the emission benefit, and the burden concentrates in people over 60 and in "
     "LMICs. The uncertainty interval covers the concentration-response function only; the ML downscaler is trained against present-day "
     "observations and is applied to 2050 states it has never seen. "
     "Relevance: the downscaler's skill rests on ground data that are thinnest in the LMICs that carry the burden.")),
 R(7, "BMC Public Health",
  short="Shandong GBD 2021 PM2.5 attributable ASMR greenspace access Gini 204 countries 2000-2020 EAPC",
  sub=corpus.BURD, design="Descriptive burden analysis, GBD 2021",
  pm="GBD 2021 ambient PM2.5-attributable age-standardised mortality; greenspace access from GLAD",
  geo="Global / multi-region", endpoint="PM2.5-attributable ASMR; greenspace access and inequality", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Shandong University, China; Shandong University, China",
  n=("204 countries, 2000-2020. Global PM2.5-attributable all-cause ASMR fell from 63.5 to 55.4 per 100,000 while greenspace access fell from "
     "37.0% to 28.6%; greenspace inequality in low-SDI countries rose (Gini 0.20 to 0.24). Higher greenspace access correlated with lower "
     "PM2.5-attributable mortality for IHD, stroke, COPD and neonatal disorders. Both sides are modelled country aggregates and the attributable "
     "burden is itself a function of GBD exposure and baseline rates, so the correlation is ecological and confounded by development. "
     "Mortality attributable to PM2.5 can fall while concentrations rise if baseline rates fall, so the trend is not an exposure trend. Relevance: low - burden bookkeeping with no measurement content.")),
 R(65, "J Expo Sci Environ Epidemiol",
  short="NIEHS PEGS GIS-ExWAS 88 geospatial exposure indicators 11 phenotypes IPTW LASSO air pollution cardiovascular",
  sub=corpus.EXPO, design="Exposome-wide association",
  pm="88 GIS-linked residential exposure indicators including air pollution",
  geo="USA", endpoint="11 common disease phenotypes", tier="C",
  basis="Model (CTM / LUR / ML)", affil="DLH LLC, USA; National Institute of Environmental Health Sciences, USA",
  n=("7,531 Personalized Environment and Genes Study participants' residential histories linked by open-source GIS to 88 exposure indicators; "
     "cross-sectional associations with 11 phenotypes by adjusted logistic regression, IPTW and LASSO. The GIS-ExWAS recovered associations "
     "complementary to the cohort's earlier questionnaire ExWAS, including air pollution with cardiovascular disease, plus new suggestive "
     "associations. No effect sizes are given; the contribution is the linkage pipeline. Cross-sectional design and many correlated indicators "
     "make every hit a hypothesis, and the abstract does not say which air-pollution surfaces were linked. "
     "Relevance: indirect - a standard linkage layer is where sensor-network surfaces would have to plug in.")),
 R(88, "JMIR Res Protoc",
  short="Luebeck Schleswig-Holstein emergency department climate air quality infectious surveillance DLNM register protocol 2014-2024",
  sub=corpus.BURD, design="Study protocol",
  pm="State environmental monitoring air-quality data linked with German Weather Service meteorology",
  geo="Germany", endpoint="Daily ED visits overall and by disease category (planned)", tier="C",
  basis="Reference / regulatory monitor", affil="University Hospital Schleswig-Holstein, Germany; University Hospital Schleswig-Holstein, Germany",
  n=("Protocol for a four-site retrospective study of emergency department presentations in the Luebeck area, January 2014-December 2024, "
     "linking ICD-coded visits to German Weather Service meteorology, state air-quality monitoring and Robert Koch Institute infectious surveillance. "
     "Distributed lag nonlinear models within GAMs, stratified by age, sex and socioeconomic status; ethics granted July 2025 and data transfer "
     "under way. No results. The analysis plan centres on temperature; the abstract names no particle metric, and a maritime region with few "
     "monitors will give little PM contrast. "
     "Relevance: low - noted as an upcoming low-concentration ED series.")),
]
