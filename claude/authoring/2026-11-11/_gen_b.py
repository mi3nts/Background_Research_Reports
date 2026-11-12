# -*- coding: utf-8 -*-
R = {
20: dict(short="Western Australia mining TiO2 604 personal inhalable samples 2018-2025 proposed ultrafine fine exposure limits",
  sub="OCC", design="Monitoring-record analysis", pm="Personal inhalable TiO2 samples from the state regulator's database",
  geo="Australia (Western Australia)", endpoint="Exceedance of current (10 mg/m3) and proposed (0.3, 2.4 mg/m3) TiO2 limits", tier="C",
  basis="Personal / wearable", affil="Edith Cowan University, Australia; Edith Cowan University, Australia",
  n=("De-identified regulator data: 604 personal inhalable TiO2 samples from Western Australian mining, 2018-2025, compared with the current 10 mg/m3 "
     "inhalable limit and proposed limits of 0.3 mg/m3 (ultrafine/nanoscale) and 2.4 mg/m3 (fine, respirable). Exposures were consistently low; one sample "
     "exceeded the numerical value of the proposed ultrafine limit and the second highest was 0.12 mg/m3; none exceeded 2.4 mg/m3; trends were stable or "
     "falling. The weakness is the conclusion itself: inhalable gravimetric mass says nothing about the ultrafine/nanoscale fraction the 0.3 mg/m3 limit "
     "targets, so 'conservative evidence of compliance' does not follow for that limit. "
     "Relevance: peripheral - illustrates why size-specific limits need size-resolved measurement, not legacy inhalable samples.")),
21: dict(short="UK Biobank 348247 PM2.5 PM10 PM2.5-10 absorbance NO2 oral inflammatory disease KDM-BA PhenoAge mediation",
  sub="OTHR", design="Prospective cohort", pm="Residential LUR PM2.5, PM10, PM2.5-10, PM2.5 absorbance, NO2, NOx (2010)",
  geo="UK", endpoint="Incident oral inflammatory diseases; biological-age acceleration as mediator", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Central Hospital of Wuhan, Huazhong University of Science and Technology, China; Gannan Medical University, China",
  n=("UK Biobank, 348,247 adults, median follow-up 16.49 years, 3,967 incident oral inflammatory diseases. Per SD increment, PM2.5, PM10, PM2.5-10 and PM2.5 "
     "absorbance were associated with 8%, 4%, 3% and 5% higher incidence (NO2 10%, NOx 8%; all p<0.05). PhenoAge acceleration mediated 8.52-16.65% of the "
     "associations, KDM biological age 1.21-5.42%. The abstract reports no confidence intervals. Exposure is a single-year (2010) land-use regression "
     "surface applied over 16 years, the outcome comes from hospital coding of a condition mostly managed in primary dental care, and mediation by "
     "a biomarker measured at baseline alongside exposure cannot establish temporal ordering. "
     "Relevance: peripheral - modelled exposure, no measurement content.")),
22: dict(short="Luxembourg Institute of Health ExposomeMap-PM disease map 304 entities 497 processes AOP transcriptomic overlay",
  sub="MECH", design="Mechanistic review", pm="Fine and ultrafine particle exposure (knowledge model); one reference particle, 3-day exposure for the overlay",
  geo="Global / multi-region (review)", endpoint="Mechanistic network coverage; enrichment of differentially expressed genes", tier="B",
  basis="Review / no primary exposure", affil="Luxembourg Institute of Health, Luxembourg; Luxembourg Institute of Health, Luxembourg",
  n=("A curated mechanistic disease map linking fine and ultrafine particle exposure to outcomes: 304 entities and 497 processes in five blocks (alveolar "
     "deposition, oxidative stress, barrier disruption, mitochondrial dysfunction, pro-inflammatory signalling) ending in asthma, COPD, atherosclerosis and "
     "neurodegeneration, built in SBGN and served on MINERVA. In a test overlay from one reference particle and a 3-day exposure, map nodes captured "
     "1.50-fold more differentially expressed transcripts than size-matched random gene sets (permutation p=0.0074); proteomics 1.13-fold. One "
     "particle type and a short exposure validate coverage, not completeness, and enrichment is partly guaranteed by curating from the same literature. "
     "Relevance: indirect - a reusable scaffold for attaching composition-resolved exposure, which low-cost mass sensors do not provide.")),
25: dict(short="Laval retinal pigment epithelium wood smoke extract high-energy visible blue light synergy Nrf2 oxidative stress",
  sub="MECH", design="In vitro cell exposure", pm="Wood combustion smoke extract with high-energy visible light co-exposure",
  geo="Canada (laboratory)", endpoint="RPE cell viability, oxidative stress, Nrf2 activation", tier="C",
  basis="Lab / research instrument", affil="CHU de Quebec - Universite Laval, Canada; CHU de Quebec - Universite Laval, Canada",
  n=("Human retinal pigment epithelium cells co-exposed to wood combustion smoke extract and high-energy visible (blue) light. The two acted synergistically "
     "to reduce viability through oxidative stress that antioxidant treatment mitigated, implying light-sensitive chromophores among smoke constituents; "
     "cells activated Nrf2 detoxification. No doses, extract preparation, or how smoke components would reach the retina in vivo are given in the abstract, "
     "and an extract is not deposited particulate matter. "
     "The plausible exposure path is ocular surface contact or systemic translocation, neither of which the design addresses; the result is a hazard "
     "signal for heavy wood-smoke settings rather than an ambient effect. "
     "Relevance: peripheral - extends wood-smoke toxicity to a photosensitisation route; no exposure-measurement content.")),
26: dict(short="Brown Rhode Island 144 sites 531 site-sessions PM2.5 sound night-time illuminance variance place vs time",
  sub="EXPO", design="Multi-site monitoring campaign", pm="Short-session PM2.5 measured at 144 sites, day and night, over 39 days",
  geo="USA (Rhode Island)", endpoint="Variance partition of PM2.5 and sound between sites and days; predictors", tier="B",
  basis="Not stated", affil="Brown University, USA; Brown University, USA",
  n=("Preprint. PM2.5, sound and night-time illuminance measured at 144 sites in eight Rhode Island municipalities, four day/night session types over 39 days "
     "(531 site-sessions). Sound and PM2.5 were uncorrelated and had different predictors: sound rose near industrial land and varied mainly between sites; "
     "PM2.5 tracked weather (falling with wind, rising with temperature and precipitation) and varied mainly between days, rising at night. Results held "
     "under penalised regression and spatial-cluster adjustment. The instrument is not named, and short sessions at one site per visit confound site with "
     "day, which is exactly the decomposition being estimated. "
     "Relevance: direct - quantifies how little between-site PM2.5 contrast short mobile campaigns resolve against day-to-day variance.")),
27: dict(short="Ojota landfill Lagos bio-cover QFIELD QGIS PM2.5 PM10 SO2 CO six ML methods AQI risk surface",
  sub="EXPO", design="Pilot field measurement", pm="Point PM2.5 and PM10 at six sampling points 15 m apart, interpolated by ML",
  geo="Nigeria (Lagos)", endpoint="AQI classification and pollutant risk surface; microbial indicators after bio-cover", tier="C",
  basis="Not stated", affil="Yaba College of Technology, Nigeria; Yaba College of Technology, Nigeria",
  n=("Preprint. Six geo-referenced sampling points at 15 m spacing across the Ojota landfill, Lagos, measuring PM2.5, PM10, SO2 and CO as baseline, then six "
     "machine-learning methods (random forest, gradient boosting, SVM, kNN, Gaussian process/regression kriging, ANN) to classify AQI drivers and produce an "
     "uncertainty-aware risk surface; a laboratory bio-cover (topsoil, compost, rice husk, earthworm castings) reduced microbial indicators. No PM "
     "concentrations, instrument or model skill are reported in the abstract, and six points cannot support six learned spatial models. "
     "Relevance: peripheral - shows the demand for landfill-fenceline PM monitoring in West Africa; the analysis is underpowered.")),
28: dict(short="AirQo LOCATE GeoAI population-weighted p-median sensor placement Kampala Jinja Nairobi Lagos budgets 5-80",
  sub="SENS", design="Machine-learning model", pm="No PM data: siting by modelled residential population plus OpenStreetMap roads and buildings",
  geo="Africa (Uganda, Kenya, Nigeria)", endpoint="Population-and-context coverage of candidate low-cost sensor layouts", tier="B",
  basis="Low-cost sensor / network", affil="Makerere University / AirQo, Uganda; Makerere University / AirQo, Uganda",
  n=("Preprint from the AirQo group. LOCATE is a pre-deployment siting framework for data-constrained cities that prioritises proximity to modelled residential "
     "population while adding road and building context. Six feature-informed clustering methods, two allocation methods and two uninformed baselines were "
     "compared across Kampala, Jinja, Nairobi and Lagos for budgets of 5-80 sensors (20 seeds). The context-augmented population-weighted p-median ranked "
     "first in all four cities; coverage rose with budget but stayed lower in the larger Lagos and Nairobi domains. The authors state the limitation "
     "plainly: layouts are shortlists, not evidence of pollution reconstruction or exposure accuracy, because no concentration field enters the objective. "
     "Relevance: direct - siting for low-cost PM networks where no reference surface exists.")),
29: dict(short="UCLA California four refinery retirements difference-in-differences term LBW SGA births 2008-2022",
  sub="REPR", design="Quasi-experimental (difference-in-differences)", pm="Residential proximity to a retiring petroleum refinery (source proxy; no PM measured)",
  geo="USA (California)", endpoint="Term low birth weight and small for gestational age", tier="A",
  basis="Proxy / questionnaire", affil="UCLA Fielding School of Public Health, USA; UCLA Fielding School of Public Health, USA",
  n=("Singleton births 2008-2022 conceived within three years before or after the closure of one of four California refineries; difference-in-differences "
     "logistic regression, exposed versus unexposed communities by air district. Most retirements were followed by lower odds of term LBW and SGA; strongest "
     "for Alon Bakersfield, tLBW OR 0.68 (0.55-0.83) and SGA OR 0.81 (0.74-0.89). Exposure is proximity, not measured PM or any pollutant, so the result "
     "cannot be attributed to particles rather than VOCs, SO2 or concurrent economic change; parallel trends across four distinct regions is an assumption "
     "the abstract does not test, and the per-refinery heterogeneity is not summarised. "
     "Relevance: indirect - fenceline sensor records before and after a closure would supply the exposure contrast this design lacks.")),
}
