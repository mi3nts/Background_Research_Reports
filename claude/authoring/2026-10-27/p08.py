# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.21203/rs.3.rs-11078552/v1", journal="Research Square (preprint)",
  short="Upaul Khulna PM2.5 meteorology HYSPLIT random forest STL 2026",
  title="Meteorological and HYSPLIT-Derived Transport Influences on PM2.5 Exposure in a Khulna City, Bangladesh",
  sub=corpus.EXPO, design="Monitoring-record analysis", pm="Hourly PM2.5 from the CAMS-8 station (2024); NASA POWER meteorology; HYSPLIT",
  geo="Bangladesh (Khulna)", endpoint="Not applicable (meteorological and transport drivers)", tier="C",
  n=("One year (2024) of hourly PM2.5 at a single Khulna station, analysed with MLR, Random Forest, STL and K-means on "
     "HYSPLIT trajectories. Winter mean ~121 ug/m3 vs ~15 in the monsoon. Temperature and pressure were top RF predictors "
     "(OOB R2 0.64); temperature and RH were negative in MLR. Winter air arrived on short north-westerly continental "
     "paths, monsoon air on long southerly maritime paths; STL residuals flagged pre-monsoon spikes (~138 ug/m3). "
     "Limitation: one station, one year, and reanalysis meteorology at ~50 km; season is collinear with every predictor, "
     "and the 'variance explained' shares are not additive. Preprint. Relevance: low-moderate - a coastal South Asian "
     "city with almost no monitoring, where LCS would add the spatial dimension.")),
 dict(pmid="", doi="10.1093/eurpub/ckag169.1260", journal="Eur J Public Health (conference abstract)",
  short="Slovakia PM2.5 lung cancer mortality gender lag ecological 2026",
  title="PM2.5 exposure and lung cancer mortality in Slovakia: gender differences and delayed effects",
  sub=corpus.OTHR, design="Ecological", pm="National population-weighted PM2.5 (Indicator of Population Exposure), 2010-2023",
  geo="Slovakia", endpoint="Lung cancer mortality (GBD estimates)", tier="C",
  n=("National time-series ecology, 2010-2023: population-weighted PM2.5 fell from 24.4 to 15.2 ug/m3 while lung-cancer "
     "mortality fell from 30.7 to 25.3 per 100,000 (AAPC -1.5%), driven by men (56.8 to 42.6; AAPC -2.2%); female rates "
     "were flat (12.6). Correlation with PM2.5 r=0.95 overall and 0.97 in men, none in women; lags suggested emerging "
     "female associations. Limitation: 14 annual points of two monotonic trends correlate trivially; male smoking "
     "decline over the same period explains the male-only pattern, and the outcome is a GBD model output. Conference "
     "abstract. Relevance: low.")),
 dict(pmid="", doi="10.1093/eurpub/ckag169.1252", journal="Eur J Public Health (conference abstract)",
  short="Dublin air pollution fungal spores respiratory admissions time series 2026",
  title="Short-term effects of air pollution and aeroallergens on respiratory admissions",
  sub=corpus.RESP, design="Time-series", pm="Daily NO2, PM2.5, PM1 (EPA Ireland); fungal spore counts",
  geo="Ireland (Dublin)", endpoint="Daily admissions for asthma, COPD and all respiratory causes", tier="C",
  n=("Dublin daily HIPE admissions with NO2, PM2.5, PM1, fungal spores and meteorology; negative-binomial time series, "
     "lags 0-7. NO2 was consistently associated with asthma, COPD and all respiratory admissions (~3-5% per unit, "
     "p <0.01); particulate effects were 'outcome-specific' and not quantified in the abstract; spores showed no "
     "independent short-term effect. Limitation: per-unit NO2 effects of 3-5% are implausibly large per ppb or ug/m3 and "
     "suggest an unstated scale; study years and PM results are missing; conference abstract. Relevance: low-moderate - "
     "Dublin's PM1 series is unusual, and spore counts pair naturally with optical sensor coarse channels.")),
]
