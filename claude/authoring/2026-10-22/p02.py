# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.3390/atmos17101035", journal="Atmosphere",
  short="Alturki ensemble ML emulation GEOS-CF PM2.5 Arabian Peninsula spatial transfer 2026",
  title="Interpretable Ensemble Machine Learning for Statistical Emulation of Summer PM2.5 Change in GEOS-CF over the Arabian Peninsula: How Far Does Spatially Blocked Skill Transfer?",
  sub=corpus.EXPO, design="Machine-learning model", pm="GEOS-CF summer PM2.5 relative change 2020-2025 (0.25 deg); TROPOMI, ERA5-Land, CHIRPS, MODIS predictors",
  geo="Arabian Peninsula", endpoint="Emulator skill under spatial blocking and held-out sectors", tier="A",
  n=("Emulated the 2020-2025 change in summer PM2.5 over 3,933 GEOS-CF cells from 13 satellite and reanalysis predictors. "
     "Tree ensembles reached spatially blocked CV R2 0.82-0.84 (linear 0.55), but a Random Forest on latitude and "
     "longitude alone scored higher (R2 0.91). The predictor model lost all skill once cells within 300 km were excluded, "
     "failed on an unseen eastern sector (r 0.11) and did not transfer to other summers. Plain interpolation filled gaps "
     "better than any emulator. Split-conformal 90% intervals covered 82-98% of test cells, but only 60% in the east. "
     "Limitation: the target is model output, not observations. Relevance: high - a clean demonstration that blocked-CV "
     "R2 in PM mapping can be pure interpolation; the same diagnostics belong in sensor-fusion papers.")),
 dict(pmid="42905376", doi="10.1007/s11356-026-38306-6", journal="Environ Sci Pollut Res Int",
  short="Amato mobile air-liquid interface toxicity Barcelona harbor urban 2026",
  title="Assessment of air pollution toxicity in urban environments in Barcelona, Spain, using a mobile air-liquid interface system",
  sub=corpus.MECH, design="Exposure assessment + in vitro", pm="Co-measured particle and gas concentrations; whole-air ALI exposure",
  geo="Spain (Barcelona harbour and urban background)", endpoint="A549 cytotoxicity (LDH release)", tier="B",
  n=("A mobile air-liquid interface system exposed A549 cells directly to ambient air at a harbour site and an urban "
     "background site, alongside co-located particle and gas monitoring. Partial least squares explained up to 80% of "
     "the variance in ALI toxicity from air-quality parameters. Gas-phase pollutants, ozone above all, contributed more "
     "than particles. Limitation: LDH release in a single tumour-derived cell line is a crude endpoint. With two sites "
     "and highly collinear predictors, PLS loadings cannot separate ozone from photochemical-age covariates. n and "
     "exposure durations are not given in the abstract. Relevance: medium - pairing in-situ bioassays with "
     "multipollutant monitors is the template for testing whether mass-based LCS metrics track toxicity.")),
 dict(pmid="42903668", doi="10.1016/j.joclim.2026.100762", journal="J Clim Change Health",
  short="Jung peaker power plant emissions ED urgent care visits Massachusetts 2026",
  title="Individual-level health effects of living near a gas-fired \"Peaker\" power plant",
  sub=corpus.RESP, design="Case-crossover", pm="HyADS trajectory-derived peaker-plant exposure index (unitless); background PM2.5 adjusted",
  geo="USA (Massachusetts)", endpoint="Cause-specific ED/urgent-care visits", tier="B",
  n=("Primary-care patients living within 30 km of a gas-fired peaker plant, 2017-2021; 2,310 ED/UC visits analysed with "
     "a case-crossover design. Exposure was a daily HyADS parcel-trajectory index (mean 1.4, SD 16, reflecting plant "
     "intermittency); models adjusted for heat index and non-peaker PM2.5 (mean 8.5 ug/m3). Respiratory visits OR 1.044 "
     "(1.001-1.090) per unit; non-white patients OR 1.347 (1.034-1.755). Cardiovascular, headache and pregnancy visits "
     "were null. Limitation: the exposure is unitless and ZIP-code assigned, so the OR has no concentration scale. "
     "Peaker 'on' days coincide with peak heat and grid stress. A lower CI of 1.001 across four outcome families invites "
     "multiplicity concerns. Relevance: high - intermittent point sources are exactly what fence-line LCS can time-resolve.")),
 dict(pmid="42906364", doi="10.1016/j.ecoenv.2026.120945", journal="Ecotoxicol Environ Saf",
  short="He ozone-dominant air pollution risk ageing inequality China counties 2026",
  title="A nationwide effect-based assessment of ozone-dominant air pollution risk patterns and ageing-related inequality in China",
  sub=corpus.BURD, design="Ecological / registry analysis", pm="Cold-season PM2.5 and warm-season O3 (multi-source county exposures)",
  geo="China (813 counties)", endpoint="Cancer-panel-derived exceedance and excess-hazard indices, 2017-2023", tier="B",
  n=("Interpretable machine learning was fit to cancer data from 813 Chinese counties (2018-2019) to get non-linear "
     "long-term exposure-response shapes for cold-season PM2.5 and warm-season O3. Model-based thresholds then anchored "
     "exceedance and excess-hazard indices projected over 2017-2023. PM2.5 pressure fell while O3 pressure rose, with "
     "hotspots in Sichuan-Chongqing and the Yangtze River Delta that coincide with ageing. Limitation: two years of "
     "county cancer data cannot identify a dose-response threshold. ML-derived 'thresholds' in an ecological panel are "
     "model artefacts confounded by region, and the abstract gives no effect sizes or CIs. Relevance: low - "
     "county-level modelled exposure.")),
]
