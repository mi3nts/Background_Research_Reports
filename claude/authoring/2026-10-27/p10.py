# -*- coding: utf-8 -*-
P = [
 dict(pmid="42946835", doi="10.1038/s41370-026-00993-1", journal="J Expo Sci Environ Epidemiol",
  short="Fan wildfire smoke indoor PM2.5 absenteeism Oklahoma Head Start OK-AIR 2026",
  title="Wildfire smoke, indoor and outdoor PM2.5, and sick-related absenteeism in Oklahoma Head Start early care and education centers",
  sub=corpus.OCC, design="Cohort (secondary trial analysis)", pm="Continuous classroom PM2.5 paired with hourly EPA outdoor PM2.5; HMS smoke days; FIRMS fire detections",
  geo="USA (Oklahoma)", endpoint="Indoor PM2.5 on smoke days; sick-related absence", tier="A",
  n=("Cohort 1 of the OK-AIR cluster-randomised 2x2 factorial trial (HEPA, upper-room UVGI): 5 centres, 20 classrooms, "
     "204 children aged 0-5, 2023-2024. On smoke-impacted days, the intervention period (pooled arms) was associated "
     "with 29.0% lower indoor PM2.5 (22.8-34.7%) after adjustment for outdoor PM2.5. Each +100 in the 7-day mean of "
     "regional FIRMS fire detections: sick-related absence OR 1.106 (1.018-1.201). Limitation: the period contrast pools "
     "all arms, so it is not a HEPA effect, and smoke days cluster in Feb-Mar, confounded by respiratory-virus season; "
     "fire counts are a regional proxy, not exposure. Relevance: high - classroom sensor plus EPA outdoor pairing is a "
     "deployable I/O design for childcare networks.")),
 dict(pmid="42945340", doi="10.1371/journal.pone.0360049", journal="PLoS One",
  short="Zhong air pollution years of life lost cancer Pudong Shanghai time series 2026",
  title="The short-term impact of ambient air pollution on years of life lost from cancer in Pudong New Area, Shanghai: A time series study",
  sub=corpus.OTHR, design="Distributed-lag time-series", pm="Daily PM2.5, PM10, SO2, NO2, O3 (monitoring network)",
  geo="China (Shanghai, Pudong New Area, 2013-2021)", endpoint="Cancer years of life lost and cancer mortality", tier="B",
  n=("Daily time series of cancer deaths and YLL in Pudong, 2013-2021, with DLNM (linear for YLL, quasi-Poisson for "
     "deaths). Per 10 ug/m3 at lag 0-1: PM2.5 +2.22 YLL (0.71-3.74), PM10 +1.04 (0.17-1.91); SO2, NO2 and O3 also "
     "positive. Effects were marginally larger in men, younger and more educated people. Limitation: short-term "
     "harvesting of cancer deaths is mostly mortality displacement in terminally ill patients, and single-pollutant "
     "models leave the PM2.5 estimate inseparable from co-pollutants; YLL per day is driven by a few young deaths, so "
     "the scale is unstable. Relevance: low - single-district monitor-average exposure.")),
 dict(pmid="", doi="10.1038/s41370-026-00995-z", journal="J Expo Sci Environ Epidemiol",
  short="Santoso air pollution noise greenness salivary cortisol BAMSE 2026",
  title="Air pollution, road traffic noise, and greenness in relation to salivary cortisol in young adults",
  sub=corpus.NEU, design="Cross-sectional (birth cohort)", pm="Address-level PM2.5, PM10, black carbon, NOx (dispersion models), prior year",
  geo="Sweden (Stockholm, BAMSE)", endpoint="Morning and evening salivary cortisol at age 24", tier="B",
  n=("BAMSE birth cohort, n=1,148 at age 24; linear regression of salivary cortisol on prior-year modelled pollutants, "
     "noise and NDVI. No overall associations. In post hoc male subgroups, PM10 was associated with higher morning "
     "cortisol (beta 0.058, 0.003-0.112) as were NOx and noise, with greenness inverse; females showed opposite trends. "
     "Limitation: the only signals are exploratory sex-by-season subgroup contrasts after a null main analysis, with "
     "lower CIs at ~0; single-day cortisol is highly variable. Treat as null. Relevance: low - low-contrast Stockholm "
     "exposures modelled at the address.")),
 dict(pmid="42944341", doi="10.3390/s26206478", journal="Sensors (Basel)",
  short="Ruwali Lary US infant life expectancy environmental determinants machine learning 2026",
  title="Estimating Life Expectancy in the U.S.: Identifying Environmental Determinants and Disparities (2003 to 2019)",
  sub=corpus.BURD, design="Machine-learning model", pm="33 ECMWF reanalysis environmental variables incl. PM, sulphate and dust aerosol, O3, CO, HCHO",
  geo="USA (contiguous, county level)", endpoint="Life expectancy, age <1 year (IHME)", tier="B",
  n=("County-level IHME life expectancy for the under-1 age group, contiguous US 2003-2019, regressed on 33 ECMWF "
     "environmental variables with ML. Marked north-south disparity, southern counties lowest. With only five variables "
     "the model reached R2 0.81 and RMSE 1.06 years on an independent test set. Beyond PM, O3 and CO, lower formaldehyde, "
     "sulphate and dust aerosol, more vegetation and lower wet-bulb temperature ranked as predictors of higher life "
     "expectancy. Limitation: no socioeconomic, race or healthcare covariates, so the south-north environmental gradient "
     "absorbs deprivation; feature importance is predictive, not causal, and IHME county estimates are themselves "
     "smoothed models. Relevance: moderate - a reanalysis-driven baseline that dense LCS data could sharpen.")),
]
