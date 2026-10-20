# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.3390/atmos17101024", journal="Atmosphere",
  short="Birinci Bosphorus bridge traffic ML proxy PM2.5 NO2 2026",
  title="Machine-Learning Proxy of Air-Quality Variability Associated with Intercontinental Bridge Traffic over the Bosphorus in Istanbul",
  sub=corpus.SENS, design="Machine-learning model", pm="Hourly PM2.5, PM10, coarse fraction, NO2, NO, NOx",
  geo="Turkiye (Istanbul)", endpoint="Not applicable (hold-out R2, RMSE)", tier="B",
  n=("17,520-h panel (2022-2023) pairing six bridge traffic sensors with the nearest monitors. A Prophet traffic-only "
     "baseline gave negative R2 for every bridge x pollutant. LightGBM, XGBoost and a BiLSTM-attention model with "
     "meteorology, calendar, precipitation lags and short autoregressive terms reached mean hold-out R2 ~0.77 (0.58-0.86), "
     "RMSE down 47-63%; the three families were practically equivalent. SHAP ranked autocorrelation, season, wind "
     "direction and heavy vehicles above total traffic. Limitation: autoregressive pollutant terms make this nowcasting "
     "persistence, not a traffic proxy - the headline R2 largely reflects lagged concentrations, and 'closest monitor' "
     "distance is unstated. Relevance: moderate - shows traffic counts alone do not substitute for measurement in "
     "complex coastal flow.")),
 dict(pmid="42895578", doi="10.1007/s10653-026-03508-x", journal="Environ Geochem Health",
  short="Moradnia Isfahan pregnant urinary metals indoor dust AQI 2026",
  title="Spatial variability of heavy metals in pregnant women: linking urinary biomarkers, indoor dust contamination, and air quality in Isfahan, Iran",
  sub=corpus.REPR, design="Cross-sectional environmental survey", pm="Zone-level Air Quality Index; indoor settled dust metals (not airborne PM)",
  geo="Iran (Isfahan)", endpoint="Urinary Cr, Pb, Cd, Ni in pregnancy", tier="C",
  n=("80 pregnant women; paired urine and vacuum dust analysed by ICP-OES. Dust metals ranked Pb>Cr>Ni>Cd (Pb mean "
     "111.10 ug/g); urine Pb 10.52, Cr 8.30, Ni 4.14 ug/L. Urinary metals and AQI differed across urban zones "
     "(p<0.001); dust did not (Pb p=0.514). Building age correlated with dust Pb (rho 0.788). Dust and urinary profiles "
     "were uncorrelated. Limitation: n=80, spot urine without creatinine adjustment stated, and the only airborne "
     "metric is a zone-level AQI - no PM mass or PM-bound metal was measured, so 'air quality' enters only as an "
     "ecological covariate. Relevance: low - illustrates the gap that personal or indoor PM monitoring with filter "
     "speciation would fill.")),
 dict(pmid="", doi="10.5194/acp-26-14671-2026", journal="Atmos Chem Phys",
  short="Cheng LETKF WRF-Chem CALIOP component-resolved aerosol assimilation East Asia 2026",
  title="Constraining the vertical profiles of aerosol component and heating rate over east Asia through assimilating CALIOP observations",
  sub=corpus.EXPO, design="Chemical transport modelling", pm="Species-resolved extinction profiles: dust, sea salt, black carbon, water-soluble",
  geo="East Asia", endpoint="Not applicable (AOT, extinction, SSA, heating rate)", tier="B",
  n=("Component-resolved LETKF assimilation in WRF-Chem of CALIOP-MODIS synergistic species-specific extinction profiles "
     "(dust, sea salt, BC, water-soluble), with spatial and observational constraints. The analysis reconstructs "
     "multi-layer vertical structure and corrects severe underestimation of elevated BC plumes, including persistent "
     "free-tropospheric BC over South Asia; AERONET and AD-Net lidar validation shows gains in AOT, extinction and "
     "single-scattering albedo. Limitation: CALIOP's narrow curtain and 16-day repeat leave most of the domain "
     "unobserved, the species classification is retrieval-model dependent, and the abstract gives no quantitative skill "
     "figures; surface PM2.5 is not evaluated. Relevance: moderate - column and vertical constraints are what "
     "satellite-surface fusion with LCS networks currently lacks.")),
]
