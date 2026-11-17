# -*- coding: utf-8 -*-
# Records for 12 Nov issue, part C.
R = {
19: dict(short="Duke systematic review 27 studies environmental exposures brain MRI cognitively healthy older adults PM2.5 NO2 greenspace",
  sub="NEU", design="Systematic review", pm="PM2.5, PM10, NO2 and built/natural environment exposures (literature)",
  geo="Global (10 countries)", endpoint="Brain MRI structure: volumes, WMH, cortical thickness, hippocampus", tier="B",
  basis="Review / no primary exposure", affil="Duke University, United States; not stated",
  n=("Preprint systematic review (MEDLINE, Web of Science to 23 Feb 2026): 27 studies, more than 84,000 cognitively healthy adults aged 65+ in ten "
     "countries; 13 cross-sectional, 14 cohort, of which only five longitudinal. Higher PM2.5, NO2 and PM10 were associated with smaller total, grey "
     "and white matter volumes, more white-matter hyperintensities, cortical thinning and smaller medial temporal and hippocampal volumes; greenspace "
     "findings were favourable but inconsistent. Synthesis was by effect direction, without pooling. Outcome assessment was biased in 12 of 27 studies "
     "and four of five longitudinal studies had inadequate follow-up, so vote-counting over mostly cross-sectional designs cannot establish direction "
     "of effect. "
     "Relevance: indirect - neuroimaging endpoints with no exposure-method stratification; measurement error is not assessed.")),
34: dict(short="FMI Vehmasmaki tower optical pollen sensors 4 115 272 m Hirst CDA birch pine polarization SILAM vertical profile ML",
  sub="SENS", design="Field instrument evaluation", pm="Pollen (coarse bioaerosol) by optical pollen sensors at three heights; CDA 20-100 um",
  geo="Finland", endpoint="Inter-sensor agreement, vertical pollen profile, model comparison, taxon classification", tier="B",
  basis="Lab / research instrument", affil="Finnish Meteorological Institute, Finland; not stated",
  n=("Optical pollen sensors at 4, 115 and 272 m on a mast in eastern Finland, run with a Hirst-type sampler and a Cloud Droplet Analyzer over the "
     "2021-2024 seasons. The three sensors agreed during intercomparison (R2 >= 0.91); pollen dominated 20-100 um particle counts in intensive "
     "periods; birch and pine had distinct polarization signatures, modulated by background fine-mode aerosol. In a May 2024 birch episode "
     "concentrations fell with height, a profile SILAM reproduced in shape but overestimated at all heights; ML on sensor plus meteorology separated "
     "dominant taxa. One site, two taxa, and agreement among sensors is not accuracy against the Hirst reference. "
     "Relevance: direct - coarse bioaerosol inflates optical PM10 readings in spring; real-time taxon flags are a usable correction covariate.")),
35: dict(short="Arba Minch Lund Sensirion SPS30 SEN55 indoor outdoor gravimetric FIDAS RH biomass burning above 1000 ug/m3 truncation",
  sub="SENS", design="Sensor evaluation (co-location)", pm="PM2.5 by Sensirion SPS30 and SEN55 versus gravimetry (Ethiopia) and Palas FIDAS (Sweden)",
  geo="Ethiopia; Sweden", endpoint="Inter-/intra-sensor agreement, accuracy versus gravimetry, RH effect", tier="A",
  basis="Low-cost sensor / network", affil="Arba Minch University, Ethiopia; Lund University, Sweden",
  n=("Indoor and outdoor co-location of Sensirion SPS30 and SEN55 in Arba Minch (about 200,000 people) against gravimetry, plus a Swedish outdoor set "
     "against a FIDAS for humidity. SEN55 read 6-10% above SPS30; after that offset the two were functionally identical (CV <= 7.7%, between-sampler "
     "uncertainty <= 1.7 ug/m3). Both were stable through repeated events above 1000 ug/m3; SEN55 truncates at 6553.4 ug/m3, but readings beyond the "
     "1000 ug/m3 specification remained informative for biomass-smoke mass. Calibrated in use, accuracy error was <= 22% indoors and outdoors and "
     "outdoor expanded uncertainty <= 15% against gravimetry; the RH effect was small. Gravimetric sample numbers and the RH range are not given in "
     "the abstract. "
     "Relevance: direct - field evidence that Sensirion units can be locally calibrated for kitchen-smoke exposure in East Africa.")),
37: dict(short="University of Washington PM2.5 sensor network outlier detection Shannon entropy gradient boosting 11 smoke events 2024-2025 simulated faults",
  sub="SENS", design="Methods development (network QA)", pm="Hourly PM2.5 from multiple low-cost sensor types across North American networks",
  geo="North America", endpoint="Detection of simulated sensor faults during smoke events", tier="A",
  basis="Low-cost sensor / network", affil="University of Washington, United States; not stated",
  n=("Outlier detection for heterogeneous PM2.5 sensor networks during wildfire smoke, when real concentration swings mimic faults. A tuneable "
     "rule-based function balances the Shannon entropy of the local network against the information content of a single sensor's reading; it and "
     "information-theoretic plus short-term temporal features feed a gradient-boosted tree. Hourly data from 11 North American smoke events in "
     "2024-2025 were perturbed to simulate five common faults, and both methods detected them with adjustable sensitivity. Performance metrics are "
     "not in the abstract, and simulated faults may be easier than real drift, fouling or siting artefacts; there is no reference truth for "
     "hyper-local outliers. "
     "Relevance: direct - an automated QA layer for exactly the multi-vendor networks used in smoke response.")),
39: dict(short="Lamont-Doherty Columbia Ghana 1 km daily PM2.5 2005-2025 XGBoost satellite reanalysis low-cost sensor validation north-south gap",
  sub="EXPO", design="Exposure model (ML, satellite-fused)", pm="Daily surface PM2.5 at 1 km from ground monitors, satellite and reanalysis inputs",
  geo="Ghana", endpoint="Model performance against reference and calibrated low-cost sensors; 21-year spatial trend", tier="A",
  basis="Satellite-fused", affil="Lamont-Doherty Earth Observatory, Columbia University, United States; not stated",
  n=("A 1 km daily PM2.5 product for Ghana, 2005-2025, from several ML learners trained on ground monitoring, satellite and reanalysis composition and "
     "meteorology, evaluated against reference-grade monitors and a large calibrated low-cost sensor network. XGBoost performed best; SHAP ranked "
     "meteorology and aerosol optical properties as dominant drivers. The surface shows a north-south disparity, higher in the north and widening by "
     "about 0.15 ug/m3 per year. Skill statistics are not in the abstract; reference monitors in Ghana are few, and validation against calibrated "
     "sensors inherits their calibration error, while Harmattan dust challenges both satellite retrievals and optical sensors. "
     "Relevance: direct - one of few national surfaces in West Africa to use a low-cost network as validation rather than as an afterthought.")),
45: dict(short="Helsinki aerosol dynamics NPF contribution to aerosol mass regimes condensation sink Beijing Hyytiala future urban PM",
  sub="EXPO", design="Process modelling", pm="New-particle-formation contribution to particle mass (simulated, measurement-constrained)",
  geo="China (Beijing); Finland", endpoint="NPF mass contribution by background condensation sink regime", tier="C",
  basis="Model (CTM / LUR / ML)", affil="not stated; University of Helsinki, Finland",
  n=("Aerosol-dynamics simulations constrained by measurements define regimes for how much new particle formation adds to particle mass. New "
     "particles can add more than 10 ug/m3 when initial new-particle number and vapour production are high and the background condensation sink "
     "low: substantial at about 0.001 s-1 (regime I), negligible above 0.01 s-1 (regime III). Urban Beijing events fall mostly in the transition "
     "regime, a Finnish forest site in regimes I-II; declining urban sinks should move cities toward larger NPF mass contributions. Results rest on "
     "assumed accommodation coefficients and vapour yields, and the abstract does not quantify regime frequency. "
     "Relevance: indirect - as cities clean up, more PM2.5 mass may arrive as sub-100 nm growth that optical sensors detect late or not at all.")),
}
