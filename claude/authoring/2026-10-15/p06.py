# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.3390/atmos17101016", journal="Atmosphere",
  short="Shandong integrated air-pollutant GHG inventory 2026",
  title="Strategies for Co-Control of Air Pollutants and Greenhouse Gases: Insights from an Integrated Emission Inventory in Shandong Province",
  sub=corpus.BURD, design="Emission inventory", pm="Primary PM, SO2, NOx, VOCs, NH3, CO plus CO2, CH4, N2O by source and city",
  geo="China (Shandong)", endpoint="No health endpoint", tier="C",
  n=("2024 integrated inventory for 16 Shandong prefectures, 10 air pollutants and 4 GHGs over 8 source categories. "
     "Power/heat and industry gave 86.84% of CO2; industry dominated SO2, CO and VOCs; mobile sources NOx; agriculture "
     "NH3, CH4 and N2O; fugitive dust dominated primary PM. Interspecies correlations show partial synergy, so co-control "
     "cannot be assumed from shared sources. Limitation: inventory only, no uncertainty bounds in the abstract, and "
     "fugitive-dust PM is the least constrained category in any inventory. Relevance: low-moderate - fugitive dust "
     "dominance is a coarse-mode signal that PM10/PM2.5 ratios from LCS can check locally.")),
 dict(pmid="", doi="10.3390/atmos17101011", journal="Atmosphere",
  short="Epple DLR tire-wear particle chassis dynamometer 2026",
  title="Temperature and Inflation Pressure Effects on Airborne Tire Wear Particle Measurements on a Chassis Dynamometer",
  sub=corpus.SENS, design="Laboratory measurement", pm="Airborne TRWP number (MCPC 7 nm-2 um; OPS 0.3-10 um) and OPS mass proxy",
  geo="Germany (DLR)", endpoint="No health endpoint", tier="B",
  n=("Two-level factorial (inflation 1.8/3.8 bar x chamber 11/35 C) on the DLR TRWP system, in two blocks of toe "
     "setting. Higher temperature raised cumulative MCPC response 3.6-fold (95% CI 1.8-7.2); higher pressure cut OPS "
     "number 18% (12-24%); OPS mass proxy fell ~17% with temperature. Toe >48 arcmin produced rising signals and "
     "irregular wear. Reference-condition MCPC response doubled over the campaign, so drift monitoring and randomised "
     "blocked run order are prerequisites. Limitation: one tire, one rig; the OPS mass proxy assumes density and "
     "refractive index; the ultrafine mode may be volatile, not wear. Relevance: moderate - non-exhaust PM metrology "
     "with explicit instrument drift; the same discipline applies to LCS.")),
 dict(pmid="", doi="10.3390/atmos17101010", journal="Atmosphere",
  short="Cheng BTH multi-source satellite PM2.5 stacking 2026",
  title="Machine Learning-Based Retrieval of PM2.5 Concentrations Using Multi-Source Satellite Data in the Beijing-Tianjin-Hebei Region of China",
  sub=corpus.EXPO, design="Machine-learning model", pm="Satellite AOD + LST, NDVI, tropospheric NO2 + meteorology -> surface PM2.5",
  geo="China (Beijing-Tianjin-Hebei)", endpoint="No health endpoint", tier="B",
  n=("BTH 2019-2021: RF, SVR, XGBoost and linear stacking on four predictor sets with an 80:10:10 split. Test R2 rose from "
     "0.51-0.54 with AOD alone to 0.83-0.84 with all eight predictors; stacking best at R2 0.84, RMSE 12.4, MAE 9.7 "
     "ug/m3. Southern/southwestern Hebei highest; winter > summer. Missing AOD limited spatial completeness. "
     "Limitation: a random split leaks spatial and temporal autocorrelation, so the test R2 overstates out-of-site skill; "
     "no spatial-block CV, and gap filling - the real problem - is left to future work. Relevance: moderate - AOD alone "
     "explains half the variance; ground nodes and meteorology carry the rest.")),
 dict(pmid="", doi="10.1038/s41370-026-00989-x", journal="J Expo Sci Environ Epidemiol",
  short="Walter neighbourhood air exchange inhaled dose children 2026",
  title="Neighborhood-scale disparities in air exchange rates and inhaled pollution dose among school-aged children",
  sub=corpus.OCC, design="Metadata only (no abstract)", pm="Residential air exchange rate and infiltrated PM / inhaled dose",
  geo="United States", endpoint="Inhaled pollution dose (children)", tier="C",
  n=("No abstract at harvest. Title indicates neighbourhood-scale modelling of housing air exchange rates and the "
     "resulting inhaled pollutant dose among school-aged children, framed as a disparity analysis (Northeastern "
     "University group). Recorded for coverage; no estimate inferred. Relevance: high if infiltration is parameterised "
     "from data - indoor/outdoor LCS pairs measure exactly this ratio.")),
]
