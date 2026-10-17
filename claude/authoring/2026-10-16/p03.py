# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.5194/amt-19-6517-2026", journal="Atmos Meas Tech",
  short="Fluorescence-Raman-Mie lidar PM2.5 profiles Beijing 2026",
  title="Classification-constrained retrieval of PM2.5 vertical profiles from fluorescence-Raman-Mie polarization lidar",
  sub=corpus.SENS, design="Remote sensing / lidar retrieval", pm="Lidar extinction to PM2.5, aerosol typed by depolarisation ratio and fluorescence capacity",
  geo="China (Beijing)", endpoint="No health endpoint", tier="A",
  n=("Beijing lidar separates anthropogenic pollution aerosol from desert and mineral dust using particle depolarisation "
     "ratio plus fluorescence capacity, then applies an extinction-to-PM2.5 regression only to the anthropogenic "
     "fraction. Date-separated near-surface validation (411 hourly samples, 69 days): RMSE 17.32, MAE 13.54, bias 3.30 "
     "ug/m3; versus the unconstrained model RMSE -38.2%, MAE -45.0%, bias about -83%. Limitation: validation is at the "
     "surface only, so the vertical profile itself is unverified, and residual scatter of the empirical extinction-mass "
     "relation, not the classification, dominates uncertainty. Relevance: high - the same coarse-dust mass bias wrecks "
     "optical LCS; type-gated calibration is directly transferable to network QC during dust events.")),
 dict(pmid="", doi="10.5194/amt-19-6503-2026", journal="Atmos Meas Tech",
  short="MISR Research Product Algorithm 1.1 km AOD 2026",
  title="The MISR Research Product Algorithm - producing global, self-consistent, pixel-level aerosol retrievals for the Multi-angle Imaging SpectroRadiometer",
  sub=corpus.SENS, design="Satellite retrieval evaluation", pm="MISR AOD, Angstrom exponent, particle shape and SSA at 1.1 km",
  geo="Global", endpoint="No health endpoint", tier="B",
  n=("Automates the MISR research aerosol retrieval into a production algorithm (MRPA) at 1.1 km pixels versus 4.4 km for "
     "the standard product. Against AERONET over land, MRPA mid-visible AOD has roughly half the RMSE and a higher "
     "correlation than the standard algorithm, at the cost of somewhat higher bias; Angstrom exponent improves, "
     "especially at high AOD. Smoke regions retrieve small-medium spherical absorbing particles, dust regions large "
     "non-spherical weakly absorbing ones. Limitation: automation reduces particle-type sensitivity, SSA and shape are "
     "validated only qualitatively, and MISR's 9-day global revisit limits daily PM2.5 use. Relevance: moderate - "
     "type-resolved AOD is a plausible covariate for compositional correction of LCS-satellite fusion.")),
 dict(pmid="42884376", doi="10.3390/s26196178", journal="Sensors (Basel)",
  short="UAV rotor-wash bias in airborne pollutant sensing 2026",
  title="UAV-Induced Measurement Bias in Air Pollution Sensing: A Physics-Informed Framework for Characterization, Sensor Placement, and Correction",
  sub=corpus.SENS, design="UAV instrument deployment", pm="UAV-mounted PM2.5, PM10 and gas sensors vs fixed reference",
  geo="Not stated", endpoint="No health endpoint", tier="B",
  n=("Actuator-disk momentum theory and literature constraints are combined into a four-zone rotor-wash contamination map, "
     "a sensor-placement rule and a two-stage bias correction for nine pollutants. Hover and 5 m/s co-location flights "
     "on a 21-inch quadrotor against a fixed reference showed bias of 3-10% in hover and 6-15% in forward flight across "
     "NO2, CO, O3, PM10 and PM2.5, directionally matching predictions, but correlation fell to r = 0.44 in forward "
     "flight. Limitation: a single airframe, few flights and no wind tunnel - the authors concede qualitative rather than "
     "quantitative support. Relevance: high for vertical-profile LCS work - mounting position is a first-order error "
     "term and r = 0.44 is below any usable validation threshold.")),
 dict(pmid="42884477", doi="10.3390/s26196276", journal="Sensors (Basel)",
  short="HMAC message authentication vs LoRa telemetry poisoning 2026",
  title="Securing AI-Driven Systems for Environmental Sustainability in IoT Applications: A Lightweight Message-Authentication Scheme Against Telemetry Poisoning",
  sub=corpus.SENS, design="Method / algorithm", pm="Network PM2.5 telemetry (public datasets) used for forecast-poisoning test",
  geo="Not applicable", endpoint="No health endpoint", tier="C",
  n=("Proposes an encryption-free HMAC-SHA-256 tag over device ID, timestamp, monotonic counter and payload for raw LoRa "
     "links, with a durable server-side counter high-water mark to reject forgeries and replays. Host-side reference "
     "tests: zero false accepts/rejects over 25,000 adversarial messages. In a ten-seed poisoning study on public "
     "environmental datasets, a value-based outlier defence raised PM2.5 forecast RMSE by up to ~104% by discarding real "
     "extremes, whereas authentication held the clean baseline. Cost: payload 34 to 99 B, airtime ~2.2x. Limitation: "
     "never run on the ESP32-S3 hardware; energy unquantified. Relevance: moderate - smoke-event extremes are precisely "
     "what outlier filters in LCS pipelines wrongly remove.")),
]
