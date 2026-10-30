# -*- coding: utf-8 -*-
P = [
 dict(pmid="42932133", doi="10.1007/s11596-026-00255-z", journal="Curr Med Sci",
  short="Li ambient air pollution gastric cancer incidence 204 countries ecological 2026",
  title="Ambient Air Pollution and Gastric Cancer Incidence: A Multinational Ecological Analysis (1990-2020)",
  sub=corpus.OTHR, design="Ecological panel, fixed effects", pm="GBD 2021 national population-weighted PM2.5, NO2, O3",
  geo="Global (204 countries)", endpoint="Age-standardised gastric cancer incidence", tier="B",
  n=("Negative-binomial fixed-effects panel over 204 countries, 1990-2020, from GBD 2021. Per unit PM2.5: +0.3% (0.1-0.5%) "
     "in age-standardised gastric cancer incidence; NO2 +1.8% (1.2-2.4%), O3 +0.6% (0.3-0.9%). Splines show nonlinearity; "
     "PM2.5 lag window 3-4 years; male and high-middle-SDI strata most affected. Limitation: both exposure and outcome are "
     "GBD modelled quantities that share covariates (SDI), and a 3-4 year lag for a cancer with a decades-long "
     "Helicobacter-driven course is biologically implausible; country fixed effects do not remove the H. pylori decline "
     "that tracks development. The authors concede ecological status and call for individual-level validation. Relevance: low.")),
 dict(pmid="42932048", doi="10.1007/s10661-026-16082-7", journal="Environ Monit Assess",
  short="Vikas wavelet background PM2.5 India MERRA-2 2026",
  title="Estimating background PM2.5 concentrations using a wavelet-based convolution framework",
  sub=corpus.EXPO, design="Algorithm development", pm="MERRA-2 reanalysis PM2.5; CPCB monitors for evaluation",
  geo="India", endpoint="Regional background PM2.5 field", tier="B",
  n=("Wavelet coherence of low-frequency components across neighbouring MERRA-2 cells yields a spatiotemporal PM2.5 "
     "background map for India, capturing the IGP winter build-up and pre-monsoon dust in the northwest. Against a "
     "GMM-HMM background at four cities, MAD 2.2 (Kolkata) to 10.8 (Delhi) ug/m3. Against 5th-percentile PCHIP backgrounds "
     "across the Delhi network, MAE 21.95 and RMSE 29.45 ug/m3, improving to 14.03/17.65 at the Delhi background site. "
     "Limitation: validation is against other statistical background definitions, not tracer or model source "
     "attribution, and MERRA-2 PM2.5 is a reconstructed aerosol product with known bias over South Asia. "
     "Relevance: high - background/increment separation is a standard post-processing step for dense LCS networks.")),
 dict(pmid="42929746", doi="10.1080/10962247.2026.2754941", journal="J Air Waste Manag Assoc",
  short="Kara Pythagorean fuzzy PM2.5 monitoring station placement Trabzon 2026",
  title="A Pythagorean Fuzzy decision making framework for PM2.5 monitoring station placement in urban areas: A case study of Trabzon, Turkiye",
  sub=corpus.SENS, design="Delphi consensus", pm="PM2.5 monitoring network siting (criteria-weighted)",
  geo="Turkiye (Trabzon)", endpoint="Ranking of candidate monitoring sites", tier="B",
  n=("Modified Delphi to set eight criteria, PF-SWARA to weight them and PF-CODAS to rank five candidate sites in Trabzon. "
     "PM2.5 level weighted highest, then population density and distance to existing stations; a shopping-mall site "
     "ranked first. Limitation: the criterion weights are expert judgment; there is no objective function (coverage, "
     "representativeness, variance reduction) and no test that the chosen site improves exposure estimation. Weighting "
     "'PM2.5 concentration' highest is circular when the network is being sited to measure it, and five alternatives "
     "make the ranking near-trivial. Relevance: medium - a contrast case for data-driven siting (kriging variance, "
     "information gain) that LCS deployments use.")),
 dict(pmid="", doi="10.5194/acp-26-15003-2026", journal="Atmos Chem Phys",
  short="Liang deep learning low-visibility events fog-haze eastern China 2026",
  title="Classification and quantification of low-visibility events using deep learning over eastern China",
  sub=corpus.EXPO, design="Deep-learning model", pm="Surface PM2.5 with geostationary satellite and meteorology",
  geo="China (eastern)", endpoint="Low-visibility event class (fog, sea fog, fog-haze) and intensity", tier="B",
  n=("A unified CNN fuses geostationary imagery, meteorology and surface PM2.5 to map and classify low-visibility events, "
     "separating polluted fog-haze from clean fog over land and sea. Scenario analysis: a 20% cut in PM2.5 shrinks winter "
     "fog-haze area by 43% but population exposure to fog-haze only by 15%, because the most populated and most "
     "polluted regions coincide; >40% PM2.5 reduction is needed there. Limitation: the scenario perturbs PM2.5 as a model "
     "input, so it inherits the learned correlation rather than fog microphysics (hygroscopic growth, aerosol-fog "
     "feedback); classification skill metrics are not in the abstract. Relevance: medium - humidity-driven haze is the "
     "regime where optical LCS fail.")),
]
