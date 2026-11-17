# -*- coding: utf-8 -*-
# Records for 14 Nov issue, part A (authored 2026-11-16 run). DOI/PMID/journal/title injected from cache by _gen.py.
R = {
2: dict(short="Wuhan PLWH vitamin D RCT PM1 PM2.5 PM10 CD4 CD19 DNA methylation mediation 2023",
  sub="MECH", design="Randomised controlled trial", pm="PM1, PM2.5 and PM10 averaged over 72 h before each visit (source not stated in abstract)",
  geo="China (Wuhan)", endpoint="CD4+ T and CD19+ B cell counts; cytokines; CpG methylation", tier="B",
  basis="Not stated", affil="Yangzhou University, China; Yangzhou University, China",
  n=("Double-blind placebo-controlled trial of daily vitamin D in 80 people living with HIV (75 analysed, 271 follow-ups, March-July 2023), PM averaged over the 72 h before each 28-day visit. "
     "Supplementation attenuated the negative PM-cell count associations: the PM-associated change in CD4+ T cells differed from placebo by 3.37%, 2.21% and 1.96% per 10 ug/m3 PM1, PM2.5 and PM10, and in CD19+ B cells by 4.71%, 2.98% and 2.65%. "
     "173 vitamin D-related CpG sites changed; 25 mediated 28-79% of effects on TLR4, IL-6 and TNF-alpha. "
     "No CIs for the between-arm differences are given, randomisation is to vitamin D not to PM, and the exposure source is unstated; the PM contrast is observational within a small trial. "
     "Relevance: indirect - a short-window effect modifier study whose exposure assignment is exactly where a home sensor would sharpen it.")),
3: dict(short="Wonkwang ApoE-/- diesel exhaust particle nebulisation retinoic acid eNOS BH4 atherosclerosis 8 weeks",
  sub="CVM", design="Animal + in vitro", pm="Diesel exhaust particles by nebulisation chamber, 8 weeks; dose not stated in abstract",
  geo="Republic of Korea (laboratory)", endpoint="Lung inflammation, blood pressure, lipids, aortic wall thickening; HUVEC eNOS coupling", tier="C",
  basis="Lab / research instrument", affil="Wonkwang University, Republic of Korea; Wonkwang University, Republic of Korea",
  n=("Retinoic acid was nominated by connectivity mapping of COPD lung transcriptomes (GEO, 5 vs 6 donors), then tested in ApoE-/- mice nebulised with diesel exhaust particles for 8 weeks with oral all-trans retinoic acid at 1 or 5 mg/kg/day. "
     "Treatment lowered BAL CXCL1/2 and lung Muc5ac, IL-1b, IL-6 and TNF-alpha, reduced blood pressure, improved serum lipids and attenuated aortic inflammatory infiltration and wall thickening; in HUVECs it raised GTPCH-1, eNOS phosphorylation, BH4 and BH4/BH2. "
     "The abstract gives no DEP concentration, group sizes or effect sizes, and DEP is a single-source surrogate for ambient PM2.5. "
     "Relevance: indirect - mechanistic cardiovascular arm; no measurement content.")),
4: dict(short="TU Delft Brussels multi-modal low-cost sensor calibration transfer DANN drift detection residual monitor",
  sub="SENS", design="Calibration model comparison", pm="PM2.5, PM10 and PM1 from custom multi-modal low-cost devices, with O3 and NO2",
  geo="Belgium (Brussels)", endpoint="Calibration error (MAE, RMSE, R2, bias) on source and transfer devices; injected-drift detection", tier="A",
  basis="Low-cost sensor / network", affil="TU Delft, The Netherlands; TU Delft, The Netherlands",
  n=("Five custom multi-modal devices at two Brussels sites (9-68 days each), reference data for only a subset. MLR, Elastic Net, random forest, gradient boosting and a domain-adversarial network (DANN) were benchmarked for O3, NO2, PM2.5 and PM10 on the source unit and transferred to other units at the same and the other site, with block-bootstrap intervals. "
     "Tree ensembles had the lowest source-device errors, but for PM10 lost their advantage over the uncalibrated sensor once transferred; DANN had the best mean Calibration Transfer Ratio, not significantly. "
     "A cross-sensor residual monitor flagged injected gradual drift in reconstructable channels (PM1, UV, T, RH, CO). "
     "Five devices and short records; drift was injected, not real ageing, and the monitor cannot localise the faulty channel. "
     "Relevance: direct - quantifies the failure of calibrate-one-deploy-many for coarse PM.")),
5: dict(short="Strong Heart Air Study PurpleAir SD card logging failure cold temperature WiFi Oklahoma South Dakota Arizona",
  sub="SENS", design="Pilot field measurement", pm="PM2.5 by PurpleAir monitors, 10 co-located per site, SD-card logging without WiFi",
  geo="USA (Arizona, Oklahoma, South Dakota)", endpoint="Data recovery and logging failure versus ambient temperature", tier="A",
  basis="Low-cost sensor / network", affil="Columbia University Irving Medical Center, USA; Columbia University Mailman School of Public Health, USA",
  n=("Pilot co-locations of ten PurpleAir monitors at each of three American Indian community sites in a cardiovascular cohort, logging to SD card without WiFi to keep data under community control. "
     "Data recovery was 100% in Arizona but 57% in Oklahoma and 10% in South Dakota; logging failed when ambient temperature fell to a mean (SD) of 4.4 (3.2) C and 7.7 (2.0) C. "
     "Outdoor tests suggested WiFi connection protects logging at low temperature, and 4 C cold-room tests reproduced the failure without WiFi. "
     "This is a data-completeness finding, not an accuracy evaluation; firmware and SD-card models tested are not given in the abstract. "
     "Relevance: direct - offline PurpleAir deployments in cold climates will lose winter data non-randomly, exactly when wood-smoke exposure peaks, biasing any health analysis built on them.")),
6: dict(short="CHMI Prague Sensirion SEN54 SPS30 vs Fidas 200S 19 months dew point deficit MARS correction PM10 dust",
  sub="SENS", design="Long-term field measurement campaign", pm="PM2.5 and PM10 from two SEN54 and two SPS30 OPCs against a Palas Fidas 200S equivalent monitor",
  geo="Czech Republic", endpoint="R2 and RMSE versus equivalent monitor before and after humidity correction", tier="A",
  basis="Low-cost sensor / network", affil="Czech Hydrometeorological Institute, Czech Republic; Czech Hydrometeorological Institute, Czech Republic",
  n=("Two pairs of Sensirion OPCs (SEN54, SPS30) co-located with a Fidas 200S for 19 months. Raw agreement was far worse for PM10 (mean R2 0.50, RMSE 13.70 ug/m3) than PM2.5 (R2 0.87, RMSE 5.53 ug/m3); no unit captured mineral-dust PM10 episodes. "
     "Performance was better in the cold season and much of the seasonal variation tracked dew point deficit; MARS models with sensor PM and DPD raised PM10 to R2 0.68 (RMSE 8.25) and PM2.5 to R2 0.92 (RMSE 3.29), with particle counts helping the SPS30 further. "
     "Four sensors at one site; residual warm-season underestimation remains unexplained, and the Fidas is itself an optical equivalent rather than gravimetric. "
     "Relevance: direct - dew point deficit is a cheap, transferable humidity covariate; the PM10 dust blind spot is not fixed by it.")),
7: dict(short="University of Silesia SDS011 unheated vs heated software humidity compensation polynomial SVR DNN LSTM latency",
  sub="SENS", design="Calibration model comparison", pm="PM2.5 from an unheated SDS011 with T, RH, P, targeting a co-located heated SDS011",
  geo="Poland (Upper Silesia)", endpoint="R2, MAE, RMSE against the heated sensor; inference latency", tier="B",
  basis="Low-cost sensor / network", affil="University of Silesia, Poland; University of Silesia, Poland",
  n=("48,860 10-min records in Upper Silesia: six ML models trained to make an unheated SDS011 plus T, RH and pressure emulate a co-located heated SDS011. "
     "Sixth-degree polynomial, SVR and dense networks reached R2 94%, MAE 1.41-1.61 and RMSE 3.69-3.79 ug/m3 for PM2.5; LSTM was worse (R2 88%, MAE 2.56, RMSE 5.33) and over 500 times slower at inference (0.1215 ms/sample). "
     "The target is another low-cost sensor, so the work reproduces the heater's behaviour, not reference-grade mass; a heated inlet also evaporates semi-volatile material, so the target is biased in its own right. Single site and sensor pair. "
     "Relevance: direct - supports static non-linear RH correction on microcontrollers, but needs validation against FEM data before it substitutes for calibration.")),
8: dict(short="Universidad del Magdalena mobile WSN-IoT node edge fog cloud PM2.5 PM10 CO2 MQTT TRL 6 Santa Marta",
  sub="SENS", design="Instrument development and laboratory validation", pm="PM2.5 and PM10 from a mobile low-cost sensor node (sensor model not stated in abstract)",
  geo="Colombia", endpoint="System function (TRL 6) and RMSE after validation", tier="C",
  basis="Low-cost sensor / network", affil="Universidad del Magdalena, Colombia; Universidad del Magdalena, Colombia",
  n=("Engineering paper describing a mobile environmental node (precipitation, PM2.5, PM10, CO2, irradiance, T, pressure, wind) with a fixed sink, edge-fog-cloud architecture, MQTT broker and web interface with geospatial queries. "
     "Store-and-forward, integrity checks and flow control are built in; laboratory and field tests reached TRL 6. Metrological evaluation against independent validation reduced RMSE for four of six variables, most for PM2.5, but no numbers are given in the abstract. "
     "No sensor model, reference instrument, duration or mobile-sampling design is reported, so the PM data quality cannot be judged from the abstract. "
     "Relevance: direct but thin - an architecture template for mobile low-cost PM mapping, without the calibration evidence needed to use its data.")),
10: dict(short="Chiang Mai rural adults biomass burning PM2.5 lag 0-90 d leukocyte telomere length 8-OHdG wild cluster bootstrap",
  sub="MECH", design="Cross-sectional study", pm="Ambient PM2.5 cumulative averages over lag 0-7 to 0-90 days (source not stated in abstract)",
  geo="Thailand (northern)", endpoint="Relative leukocyte telomere length (qPCR T/S); 8-OHdG, SII, SIRI", tier="B",
  basis="Not stated", affil="Chiang Mai University, Thailand; Chiang Mai University, Thailand",
  n=("179 rural adults in biomass-burning northern Thailand; PM2.5 averaged over five windows up to the blood draw. Positive associations with telomere length appeared only for the 0-30, 0-60 and 0-90 day windows: per window-specific IQR (8.13 and 7.25 ug/m3) relative LTL was 0.050 T/S higher (95% CI 0.012-0.089) at 0-30 days and 0.079 (0.035-0.123) at 0-60 days. "
     "Crucially, the authors' own wild cluster bootstrap over eight site-date groups left none of the five associations significant (p 0.247-0.787); the standard errors ignore site-date clustering, and p-values are unadjusted. "
     "Longer telomeres with more PM run against the usual hypothesis. "
     "Relevance: indirect - exposure varies by only eight site-date clusters, so the effective sample is eight; personal or sensor-resolved exposure is what this design lacks.")),
}
