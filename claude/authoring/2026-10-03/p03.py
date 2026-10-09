# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1016/j.atmosenv.2026.122395", journal="Atmos Environ",
  short="Rawat et al. 2026",
  title="Integrated Assessment of PM2.5 in the Central Himalaya using Satellite, Reanalysis, and a new In-situ CUPI Sensor network",
  sub=corpus.SENS, design="Metadata only (no abstract)",
  pm="Metadata only - satellite + reanalysis + a new in-situ low-cost PM sensor network (by title)",
  geo="India (Central Himalaya)", endpoint="None (abstract not deposited)", tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 3 Oct with no abstract; Europe PMC "
     "and Semantic Scholar returned nothing and Scholar Gateway is still refusing the connection. By title "
     "this is exactly the fusion problem this watch tracks - a new in-situ sensor network (CUPI) evaluated "
     "against satellite and reanalysis PM2.5 in complex mountain terrain, where both gridded products are "
     "weakest. Relevance: potentially high; on the retry list, and worth a full-text read when the "
     "abstract appears.")),

 dict(pmid="42829095", doi="10.1016/j.envpol.2026.129276", journal="Environ Pollut",
  short="Wen and Chang 2026",
  title="Estimating marine PM2.5 concentrations and exploring the drivers over the eastern China seas using multi-source data and machine learning",
  sub=corpus.EXPO, design="Machine-learning model",
  pm="Marine PM2.5 from AOD + meteorology + NO2/CO/O3/SO2, 2019-2024",
  geo="China (eastern China seas)", endpoint="None (exposure surface)", tier="B",
  n=("BPNN, random forest and XGBoost compared under sample-, spatial- and temporal-held-out validation for "
     "PM2.5 over the Bohai, Yellow and East China seas; XGBoost best. Estimated fields fall west-to-east and "
     "north-to-south with maxima in Bohai Bay and off Shandong, a declining trend with winter maxima, a "
     "visible 2020 drop, and SHAP attributing spring-autumn variance to AOD and winter variance to "
     "meteorology. Limitation: there are almost no marine ground monitors, so training and validation both "
     "lean on coastal land sites - held-out skill over open water is unverified and the 'marine' field is an "
     "extrapolation; no shipping-emission predictor. Relevance: moderate - the obvious use case for "
     "buoy- or vessel-mounted low-cost nodes is precisely this validation gap.")),

 dict(pmid="", doi="10.1155/ina/8494753", journal="Indoor Air",
  short="Aljabri et al. 2026",
  title="Indoor Air Quality and Exposure Characterization in Operational Waterpipe Cafes: Field Measurements of Particulate and Volatile Pollutants in Al-Madinah Al-Munawwarah",
  sub=corpus.OCC, design="Field measurement",
  pm="Indoor PM2.5 and PM10 with TVOC and formaldehyde, peak occupancy, 5 venues",
  geo="Saudi Arabia (Al-Madinah)", endpoint="None (exposure characterisation)", tier="B",
  n=("Direct measurement in five operating waterpipe cafes on weekdays and weekends: mean weekday PM2.5 "
     "285.5 +/- 149 ug/m3 and PM10 301.6 +/- 156 ug/m3, weekend TVOC 0.50 mg/m3, formaldehyde below "
     "short-term reference values. Variability tracked smoking intensity and ventilation. The PM2.5/PM10 "
     "ratio near 0.95 is the signature of a pure combustion source with no coarse fraction. Limitation: "
     "instrument make, calibration and whether an optical sensor was humidity- or composition-corrected are "
     "not stated - charcoal and tobacco smoke is exactly where optical PM monitors read high; five venues, "
     "no personal sampling, no worker shift-length exposure. Relevance: high for occupational indoor "
     "monitoring, where a factor-of-two optical bias still leaves concentrations an order of magnitude "
     "above guideline.")),
]
