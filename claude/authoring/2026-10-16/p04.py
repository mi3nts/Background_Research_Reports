# -*- coding: utf-8 -*-
P = [
 dict(pmid="42884220", doi="10.3390/s26196020", journal="Sensors (Basel)",
  short="Wildfire smoke onset detection fixed cameras 2026",
  title="Detecting Wildfire Smoke Onset from Fixed View Camera Networks",
  sub=corpus.SENS, design="Method / algorithm", pm="Visible smoke plumes in fixed-camera video (no mass metric)",
  geo="United States (California) + transfer sets", endpoint="No health endpoint", tier="C",
  n=("Reframes smoke detection as onset detection: a scene model learned from unlabelled fire-free video yields per-tile "
     "prediction residuals, read through four cues (residual magnitude, opacity accretion, motion coherence, temporal "
     "persistence), with detection delay and false alarms in the loss. On FIgLib the first alarm comes 1.52 min after "
     "ignition at 0.21 false alarms per camera-day, transferring to PyroNear-2025 and SKLFS-WildFire without labels. "
     "Limitation: ignition-to-alarm is benchmarked on curated sequences; night, fog and low-cloud performance is not "
     "reported. Relevance: low-moderate - an upstream trigger, not a PM measurement, but camera onset times could "
     "gate event-mode sampling and plume attribution in LCS networks.")),
 dict(pmid="", doi="10.5194/acp-26-14655-2026", journal="Atmos Chem Phys",
  short="OA molecular composition predicts ROS yield MCR-VK 2026",
  title="Linking molecular composition of organic aerosols to reactive oxygen species formation using an MCR-VK framework",
  sub=corpus.EXPO, design="Laboratory + field measurement", pm="Filter PM2.5: H2O2 + radical ROS yields; FT-ICR/Orbitrap OA composition",
  geo="Multi-site (China, Germany, Finland) + chamber SOA", endpoint="Oxidative potential (ROS formation)", tier="B",
  n=("Ambient fine PM from four Chinese megacities, a German semi-urban site and a boreal forest, plus chamber SOA, "
     "analysed by ultrahigh-resolution MS and H2O2/radical assays. Volume-normalised ROS rose with PM mass and dominates "
     "exposure in polluted cities, but mass-normalised ROS varied independently of loading and tracked the ratio of "
     "oxidised to unsaturated organic fractions (RF_OOC/RF_UOC); biogenic aerosol carried the highest per-mass yield. "
     "Limitation: correlational across few sites; cell-free ROS is a surrogate, and transition metals - a major ROS "
     "driver - are outside the framework. Relevance: moderate - mass-based LCS cannot see per-mass toxicity variation "
     "of this size; a case for pairing networks with periodic speciation.")),
 dict(pmid="", doi="10.3390/atmos17101021", journal="Atmosphere",
  short="Five megacities PM2.5 O3 trends meteorology 2018-2023",
  title="Urban Air Quality Trends and Meteorological Influences Across Five Global Megacities, 2018-2023",
  sub=corpus.EXPO, design="Monitoring-record analysis", pm="Monitor PM2.5, PM10, O3, NO2, SO2 with temperature, SLP, wind",
  geo="Global (Shanghai, Delhi, Paris, Los Angeles, Sao Paulo)", endpoint="No health endpoint", tier="C",
  n=("Descriptive 2018-2023 comparison. Shanghai PM2.5 fell from 43.5 to 27.0 ug/m3 (2018-2022) then rose to 30.3 in "
     "2023; Delhi stayed above 87 ug/m3 throughout; Paris declined; Sao Paulo rose by 2023. PM2.5 exceedance days: Delhi "
     "2,025, Shanghai 1,881, Los Angeles 366. Temperature correlated negatively with PM2.5 in Delhi (r = -0.66), sea-level "
     "pressure positively (r = 0.65); wind speed was negative everywhere. Limitation: pairwise correlations without "
     "meteorological normalisation, so trends conflate emissions and weather; exceedance counts summed over pollutants "
     "and stations are hard to compare. Relevance: low - context only.")),
]
