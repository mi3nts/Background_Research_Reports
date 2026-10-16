# -*- coding: utf-8 -*-
P = [
 dict(pmid="42871707", doi="10.1021/acsestair.5c00443", journal="ACS EST Air",
  short="Sylvester PurpleAir Philadelphia 2026",
  title="Validation of PurpleAir PM2.5 Sensors in Temperate Urban Environments",
  sub=corpus.SENS, design="Field measurement", pm="PurpleAir PA-II PM2.5 (cf_1 vs atm outputs) co-located with reference; RH from PA and weather station",
  geo="United States (Philadelphia)", endpoint="No health endpoint", tier="A",
  n=("Co-location in Philadelphia across summer and spring plus a one-year re-evaluation. Best performance came from the "
     "nationwide Barkjohn (2021) correction applied to the mean of the two channels' atm outputs: RMSE 1.64 ug/m3, MBE "
     "0.10 ug/m3, R2 0.683 at 1 h and 24 h, ahead of locally derived corrections. RH source (on-board vs weather station) "
     "changed R2 by only 0.04. After a year in the field R2 fell to 0.567. Limitation: R2 0.68 at low temperate "
     "concentrations means RMSE is the honest metric and the R2 drop partly reflects a narrower concentration range in "
     "the later period, not drift alone - the abstract does not separate them. Applying Barkjohn, derived on cf_1, to atm "
     "outputs is off-label. Relevance: high - direct evidence that a national correction can beat local fitting, and that "
     "year-one degradation needs scheduled re-co-location.")),
 dict(pmid="42870377", doi="10.1002/lary.70874", journal="Laryngoscope",
  short="SEER wildfire PM2.5 head and neck cancer 2026",
  title="Wildfire Air Pollution Exposure and Head and Neck Cancer Incidence",
  sub=corpus.OTHR, design="Ecological / registry analysis", pm="County-level wildfire-specific PM2.5 (exceedance days, any exposure, % days > 5 ug/m3), 0-10-y lags",
  geo="United States (SEER counties)", endpoint="Head and neck cancer incidence by subsite", tier="A",
  n=("SEER 2016-2022, county-level DLNM with 0-10-year lags, adjusted for tobacco, alcohol and demographics with county "
     "random effects. Cumulative RR per additional smoke-exceedance day 1.06 (1.04-1.09); any annual exposure 1.41 "
     "(1.24-1.60); per percentage-point of days >5 ug/m3 1.23 (1.13-1.33). Larynx largest (1.13, 1.07-1.19 per day), "
     "oropharynx 1.09. Limitation: ecological county-level exposure and covariates, a ten-year lag fitted on seven years "
     "of incidence, and wildfire-exposed western counties differ in screening and HPV epidemiology; the p16 "
     "stratification is the right control but its result is truncated in the abstract. Relevance: moderate-high - a "
     "second smoke-cancer signal this week (cf. 13 Oct China), both favouring upper aerodigestive sites.")),
 dict(pmid="42873846", doi="10.1126/sciadv.aea9749", journal="Sci Adv",
  short="Global heatwave-fire smoke coexposure 2026",
  title="Rising global population coexposure to heatwaves and landscape fire-sourced air pollution",
  sub=corpus.BURD, design="Exposure model (secondary data)", pm="Landscape fire-sourced PM2.5 (modelled) coincident with heatwave days",
  geo="Global / multi-region", endpoint="No health endpoint", tier="B",
  n=("Global 2000-2019: 55.9% of the population lived where heatwave-smoke coexposure increased; 916 million people/year "
     "had at least one coexposure day, rising by 287 million per decade; mean coexposure days per person rose from 1.0 "
     "to 1.7. Of the 5.5 billion person-day/decade increase, 70.5% was intensity and 29.5% population growth; low-HDI "
     "countries carried the most. Limitation: the fire-PM product is model-derived with no stated threshold sensitivity, "
     "and 'coexposure day' is a binary that discards concentration. Relevance: moderate - joint heat-smoke days are also "
     "when optical sensors are most biased (low RH, fresh smoke), so the exposure most in need of measurement is the "
     "hardest to measure cheaply.")),
]
