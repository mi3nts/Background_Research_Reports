# -*- coding: utf-8 -*-
P = [
 dict(pmid="42945187", doi="10.1371/journal.pmed.1005270", journal="PLoS Med",
  short="Wilner public safety power shutoff wildfire PM2.5 healthcare California 2026",
  title="Co-exposure to planned power outages and wildfire PM2.5 and acute healthcare utilization in California: A time-stratified case-crossover study",
  sub=corpus.RESP, design="Time-stratified case-crossover", pm="ZIP-level daily wildfire PM2.5 (per 10 ug/m3) jointly with public safety power shutoffs",
  geo="USA (California, 2013-2019)", endpoint="Respiratory, COPD, cardiovascular and psychiatric ED visits and unscheduled admissions", tier="A",
  n=("Statewide California encounters for adults 20+, time-stratified case-crossover, temperature-adjusted. Severe PSPS "
     "events alone: same-day respiratory encounters OR 1.06 (1.02-1.11), stronger for COPD. Joint PSPS and +10 ug/m3 "
     "wildfire PM2.5 vs neither: OR 1.16 (1.10-1.22), with multiplicative interaction. Cardiovascular and psychiatric "
     "encounters null. Limitation: PSPS is circuit-level but assigned by ZIP, and outage plausibly changes the exposure "
     "itself (no power for filtration or HVAC, more time outdoors or relocation), so the interaction mixes effect "
     "modification with exposure modification. Relevance: high - outages disable mains-powered sensors and purifiers "
     "precisely during smoke; battery-backed nodes are needed to measure this window.")),
 dict(pmid="42944304", doi="10.3390/s26206441", journal="Sensors (Basel)",
  short="Mercado-Velazquez low-cost sensors three-tier London calibration transferability 2026",
  title="How Accurate Are Low-Cost Air Quality Sensors? A 10-Month Study of Three-Tier Comparison with Three Calibration Methods and Cross-Site Transferability",
  sub=corpus.SENS, design="Calibration model comparison", pm="Low-cost optical PM2.5 plus MOS/electrochemical NO2, CO, O3 vs reference",
  geo="United Kingdom (London, two sites 1.6 km apart)", endpoint="Not applicable (sensor agreement, R2, seasonal drift, transfer)", tier="A",
  n=("Ten-month co-location of low-cost (MOS, optical), mid-cost electrochemical and reference instruments at two London "
     "sites. Calibration by manufacturer curve, T/RH linear regression and ML. Field-calibrated PM2.5 explained over half "
     "of reference variance at both sites, and linear calibration matched ML. PM2.5 calibrations trained April-October "
     "2025 held through winter, whereas NO2 and CO did not; transferred between sites, PM2.5 reached R2 >=0.56 and gases "
     "R2 <=0.28. The mid-cost NO2 and low-cost O3 sensors failed under all methods. Limitation: two sites 1.6 km apart in one "
     "city share aerosol type and humidity regime, so 'transferability' is tested at its easiest. Relevance: high - "
     "supports simple T/RH regression for PM2.5 nodes and mandatory co-location for gas channels.")),
 dict(pmid="42944390", doi="10.3390/s26206527", journal="Sensors (Basel)",
  short="Ai optical trapping Raman single carbonaceous aerosol smoke 2026",
  title="In-Situ Single-Particle Sensing of Carbonaceous Aerosols in Freshly Generated Smoke Using Optical Trapping-Raman Spectroscopy",
  sub=corpus.SENS, design="Laboratory instrument development", pm="Single airborne smoke particles (several um, ~10 pg), Raman spectra",
  geo="Not stated (laboratory)", endpoint="Not applicable (particle chemical fingerprinting)", tier="B",
  n=("Optical trapping-Raman spectroscopy captured smoke particles from nylon rope and plastic fibre ignited by the trapping "
     "laser itself, and analysed them airborne within seconds. Particles of several micrometres (~10 pg) gave full Raman "
     "fingerprints; band analysis separated two particle types, and spatially resolved spectra showed organic carbon and "
     "soot segregated within single particles. Limitation: freshly generated, supermicron, laser-ignited particles from two "
     "polymer fuels in an open chamber; ambient carbonaceous PM is mostly accumulation-mode, aged and far lighter, and the "
     "trapping laser may heat and alter what it measures. No throughput or detection-limit figures. Relevance: low-"
     "moderate - a reference technique for particle chemistry, not a field sensor.")),
 dict(pmid="42944708", doi="10.1080/10962247.2026.2754932", journal="J Air Waste Manag Assoc",
  short="Dhital on-road black carbon PM exposure Nepal route travel mode 2026",
  title="On-road exposure to black carbon and particulate matter in Nepal: Effects of route attributes and travel modes",
  sub=corpus.EXPO, design="Mobile monitoring campaign", pm="Equivalent BC (aethalometer), PM1, PM2.5, PM10 (portable optical)",
  geo="Nepal (Kathmandu Valley and intercity highways)", endpoint="Not applicable (on-road exposure concentrations)", tier="B",
  n=("Mobile monitoring across Nepali road types, gradients and travel modes. Mean on-road eBC 45.7 +/- 32.5 ug/m3, ~11x "
     "background; eBC made up 51% of on-road PM2.5 and 75% of PM1. Concentrations rose from residential streets to "
     "intercity highways. Upgraded orbital-highway segments had lower PM2.5 and PM10 but unchanged eBC and PM1, so paving "
     "cut resuspended dust rather than exhaust. High-gradient (4.5%) segments: median eBC 86.7 vs 41.5 ug/m3 on 0.6% "
     "segments. Motorcycles gave the highest exposure, then non-AC and AC buses. Limitation: no n of runs or season "
     "control is reported, and the old-vs-upgraded comparison is not a before-after design. Relevance: high - shows "
     "optical PM2.5 nodes miss the exhaust-dominated BC contrast that drives on-road exposure.")),
]
