# -*- coding: utf-8 -*-
P = [
 dict(pmid="42950048", doi="10.1126/sciadv.aeb7647", journal="Sci Adv",
  short="Manchanda hyperlocal BC sensing Bayesian inverse modeling West Oakland 2026",
  title="Hyperlocal sensing and inverse modeling reveal community impacts of urban air pollutant emissions",
  sub=corpus.SENS, design="Method / algorithm", pm="Black carbon from dense fixed-site network (6.7 sites/km2) plus mobile mapping",
  geo="USA (West Oakland, California)", endpoint="Hourly 150 m BC emission maps; population-weighted exposure attribution", tier="A",
  n=("Dense mobile and fixed-site BC measurements were assimilated in a Bayesian inversion to produce hourly 150 x 150 m "
     "emission maps for West Oakland, a freight-corridor community. The posterior raised total BC emissions by ~33% over "
     "the bottom-up inventory and quadrupled the share of population-weighted exposure attributed to neighbourhood and "
     "port-related sources (5% to 20%), concentrated in low-income blocks. Sensitivity runs with ~10 fixed monitors "
     "(~1 site/km2) plus time-averaged mobile maps recovered similar results. Limitation: the posterior is only as good "
     "as the transport kernel and prior error covariance; unpermitted sources are inferred, not verified on the ground, "
     "and one community limits transfer. Relevance: high - a direct recipe for turning a sparse low-cost BC/PM network "
     "into source-resolved emission corrections.")),
 dict(pmid="42950059", doi="10.1126/sciadv.aei4455", journal="Sci Adv",
  short="Baliaka Eaton urban firestorm airborne toxic metals lead Los Angeles 2026",
  title="Fire at the boundary: Airborne toxic metals from the 2025 Los Angeles urban firestorm",
  sub=corpus.EXPO, design="Field measurement", pm="Real-time airborne trace elements (XRF) in PM during the Eaton fire",
  geo="USA (Los Angeles, California)", endpoint="Plume metal enrichment vs wildfire smoke; population exposure to 24-h lead", tier="A",
  n=("Hourly airborne trace-element measurements during the January 2025 Eaton fire tracked the transition from structure "
     "to wildland burning via the K/Pb ratio. Relative to wildfire smoke, the urban plume was enriched >50-fold in lead, "
     "~7-fold in halogens and ~3-fold in arsenic, attributed to vehicles, electronics and building materials. An estimated "
     "7 million residents (range 4.3-8.0 million) experienced 24-h lead above 50 ng/m3, >80 times background. "
     "Limitation: population exposure is extrapolated from a small number of monitoring points through a dispersion "
     "estimate, and the 24-h lead threshold has no health-based standard counterpart (NAAQS is a 3-month mean). "
     "Relevance: high - optical PM sensors would register the smoke but not its metal toxicity; speciation is needed.")),
 dict(pmid="42948851", doi="10.1097/ee9.0000000000000544", journal="Environ Epidemiol",
  short="Luglio air pollution pediatric asthma hospitalizations Louisiana vulnerable groups 2026",
  title="Associations between air pollution and pediatric asthma hospitalizations across vulnerable groups in Louisiana",
  sub=corpus.RESP, design="Time-stratified case-crossover", pm="Daily PM2.5, O3 and NO2 (NO2 2010-2016 only)",
  geo="USA (Louisiana)", endpoint="Pediatric (<18 y) asthma hospitalizations", tier="B",
  n=("28,499 asthma hospitalizations in children in Louisiana 2010-2019, time-stratified case-crossover with DLNM to lag 3. "
     "Cumulative lag 0-3: PM2.5 OR 1.079 (1.052-1.107), O3 1.082 (1.050-1.116), NO2 1.071 (1.034-1.111), with increments "
     "as defined in the paper. In multipollutant models O3 and NO2 attenuated while PM2.5 persisted. Effect modification "
     "by race and Medicaid status was not significant, although lag patterns differed (lags 1-2 Black children, lag 3 "
     "White children). Limitation: exposure assigned from area-level estimates in a state with sparse monitoring outside "
     "the industrial corridor, so differential misclassification by race/rurality could mask modification; NO2 covers "
     "only 2010-2016. Relevance: medium - higher-burden groups sit where reference coverage is thinnest.")),
 dict(pmid="42948717", doi="10.7759/cureus.118676", journal="Cureus",
  short="Andreotti active fire detections circulatory hospital admissions Brazil ecological panel 2026",
  title="Active Fire Detections and Hospital Admissions for Circulatory Diseases in Brazil: An Ecological Panel Study (2013-2024)",
  sub=corpus.CVM, design="Ecological panel, fixed effects", pm="Annual satellite active-fire detection density (INPE) as smoke proxy",
  geo="Brazil (27 federative units)", endpoint="Hospital admissions for ICD-10 chapter IX circulatory diseases", tier="C",
  n=("27 Brazilian federative units x 12 years (324 unit-years), 13.8 million circulatory admissions and 2.3 million fire "
     "detections. Correlations were null (rho -0.03 to 0.01). In negative-binomial models with state fixed effects, year "
     "effects, temperature, poverty and primary-care coverage, the rate ratio per additional 1,000 detections/100,000 "
     "km2/year was 0.998 (0.970-1.028), null in every subset and with clustered SEs. Limitation: annual state-level fire "
     "counts are far removed from short-term smoke PM2.5 at residence; smoke from Amazon fires is exported to other states, "
     "so the exposure is misplaced as well as aggregated. The authors correctly state this is not evidence of no effect. "
     "Relevance: low - illustrates why fire counts cannot substitute for measured PM.")),
]
