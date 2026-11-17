# -*- coding: utf-8 -*-
# Records for 14 Nov issue, part C (authored 2026-11-16 run).
R = {
25: dict(short="J Aerosol Sci comment Gharibzadeh Yunesian low-cost sensor network guidelines tutorial",
  sub="SENS", design="Metadata only: no abstract in Crossref at issue time", pm="Not stated (comment on low-cost sensor network guidance for aerosol monitoring)",
  geo="Not stated", endpoint="Not stated", tier="C", basis="Not stated", affil="",
  n=("Metadata only. A comment in the Journal of Aerosol Science on the published tutorial 'Guidelines for implementing low-cost sensor networks for aerosol monitoring'; Crossref carried no abstract at issue time and no finding is asserted here. "
     "Authors are Gharibzadeh and Yunesian. The content of the comment and any reply is unknown from the metadata, so it cannot be said which recommendations of the tutorial it disputes or extends. "
     "Relevance: direct - any challenge to consensus guidance on deployment, co-location and QA of low-cost aerosol networks bears on how this watch grades sensor studies; to be re-checked when full text is accessible.")),
26: dict(short="Atmos Pollut Res Xuzhou street view visual landscape quantity configuration air pollution",
  sub="EXPO", design="Metadata only: no abstract in Crossref at issue time", pm="Not stated (street-level air pollution, metric not given in metadata)",
  geo="China (Xuzhou)", endpoint="Not stated", tier="C", basis="Not stated", affil="",
  n=("Metadata only. An Atmospheric Pollution Research case study of Xuzhou relating the quantity versus the spatial configuration of the visual street landscape to air pollution along urban streets. "
     "Crossref carried no abstract, so the pollutant, measurement method (fixed, mobile or sensor-based) and any effect size are unknown and no finding is asserted. "
     "Relevance: possibly direct - street-view landscape features are increasingly used as predictors in hyperlocal exposure models fed by mobile or low-cost sensor data; whether this study measured PM, and how, needs the full text.")),
39: dict(short="Atmos Res southern Taiwan northeast monsoon PM2.5 trajectory simulation long-range transport",
  sub="EXPO", design="Metadata only: no abstract in Crossref at issue time", pm="PM2.5 (simulated along transport trajectories)",
  geo="Taiwan", endpoint="Not stated", tier="C", basis="Model (CTM / LUR / ML)", affil="",
  n=("Metadata only. An Atmospheric Research paper simulating PM2.5 along the transport pathway into southern Taiwan under the winter northeast monsoon. "
     "Crossref carried no abstract; the model, evaluation data and any source attribution are unknown and no finding is asserted. "
     "Relevance: indirect - transported PM in the monsoon season changes aerosol composition and hygroscopicity, the conditions under which optical low-cost sensor calibrations built on local sources tend to drift.")),
46: dict(short="HCMUT Ho Chi Minh City Sentinel-5P ERA5 MODIS GEE XGBoost PM2.5 R2 0.784 four stations",
  sub="EXPO", design="Machine-learning model", pm="PM2.5 estimated from Sentinel-5P, ERA5 and MODIS predictors trained on four certified stations",
  geo="Viet Nam (Ho Chi Minh City)", endpoint="Predictive skill (R2, MAE); annual mean PM2.5 surface", tier="B",
  basis="Satellite-fused", affil="Ho Chi Minh City University of Technology, Viet Nam; Ho Chi Minh City University of Technology, Viet Nam",
  n=("Ho Chi Minh City has four certified PM2.5 stations. Sentinel-5P composition products, ERA5 meteorology and MODIS-derived parameters were combined in Google Earth Engine and four learners compared; XGBoost performed best (R2 0.784, MAE 2.53 ug/m3), giving a citywide annual mean of 21.55 +/- 0.92 ug/m3, about 4.3 times the WHO guideline. "
     "With four training stations the validation scheme matters more than the learner; the abstract does not say whether it was spatially held out, so R2 may reflect temporal rather than spatial skill, and the tight +/-0.92 spread suggests a smooth surface. "
     "Relevance: direct - the textbook case where a dense low-cost network would supply the spatial training data four reference stations cannot.")),
47: dict(short="Geneva children adolescents excess weight household finances PM2.5 NO2 noise greenness mediation moderation",
  sub="CVM", design="Cross-sectional study", pm="Residential PM2.5 and NO2 at geocoded address (model not stated in abstract)",
  geo="Switzerland (Geneva)", endpoint="Parent-reported excess weight (overweight or obesity)", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Geneva University Hospitals, Switzerland",
  n=("Population sample of 1,006 children (2-9 y) and 1,154 adolescents (10-17 y) in Geneva. Among children, average-to-poor household finances raised odds of excess weight (aOR 1.79, 1.13-2.84) and daytime and night-time noise were associated with it (aOR 1.40, 1.10-1.77; 1.37, 1.08-1.74). "
     "PM2.5 was not associated on its own; the financial situation x PM2.5 interaction was aOR 1.59 (0.98-2.59), suggestive but null. No associations in adolescents. "
     "Height and weight were parent-reported, the design is cross-sectional, and the PM2.5 increment is not stated in the abstract; Geneva PM2.5 contrasts are narrow and collinear with NO2 and noise. "
     "Relevance: indirect - modelled residential PM; no sensor content.")),
48: dict(short="Korea Institute of Toxicology yellow dust BALB/c MH-S alveolar macrophage AKT Nrf2 mitochondrial ROS",
  sub="MECH", design="Animal + in vitro", pm="Yellow (Asian) dust instilled in mice and applied to MH-S macrophages; dose not stated in abstract",
  geo="Republic of Korea (laboratory)", endpoint="Lung inflammation, mitochondrial function, ROS, AKT/Nrf2 signalling, cell death", tier="C",
  basis="Lab / research instrument", affil="Korea Institute of Toxicology, Republic of Korea; Korea Institute of Toxicology, Republic of Korea",
  n=("Yellow dust instilled in male BALB/c mice produced inflammatory infiltration with pigment-laden alveolar macrophages and cytokine release. "
     "In MH-S macrophages dust depolarised mitochondria, lowered ATP, raised ROS and lipid peroxidation, increased SOD2 and GPX1 but decreased SOD1 and catalase, inhibited AKT phosphorylation and Nrf2 nuclear translocation and caused necrotic-type death; an ROS inhibitor attenuated ROS, cell death and LDH release. "
     "Dose, particle size distribution and dust provenance are not given in the abstract, and instillation bypasses deposition physics. "
     "Relevance: indirect - mechanistic arm for mineral dust, the coarse fraction optical low-cost sensors under-read.")),
49: dict(short="ISCIII Madrid heatwave threshold air pollution Saharan dust biomass combustion mortality 2014-2023 overestimate 27.7%",
  sub="BURD", design="Time-series (generalised linear model)", pm="Daily PM10 and PM2.5 with NO2 and O3 from monitors (network not stated in abstract)",
  geo="Spain (Madrid)", endpoint="Heatwave definition temperature; daily all-cause mortality attributable to heat and pollution", tier="B",
  basis="Reference / regulatory monitor", affil="Carlos III Health Institute, Spain; Carlos III Health Institute, Spain",
  n=("Madrid daily all-cause mortality 2014-2023 with maximum temperature and NO2, O3, PM10 and PM2.5. Mortality anomalies were prewhitened without and with pollution to locate the heatwave threshold temperature. "
     "Accounting for pollution moved the threshold from 36.7 to 37.4 C, implying heatwave mortality is overestimated by 27.7% when pollution is ignored. Saharan dust intrusion and biomass-burning days raised all four pollutants. "
     "No CI is given for the threshold shift or the 27.7%, a single city is analysed, and prewhitening-based threshold estimation is sensitive to the smoothing choices. "
     "Relevance: indirect - heat-pollution attribution depends on monitor-level PM on dust days, when optical sensors are least accurate.")),
50: dict(short="HAPIN Peru LPG vs biomass RCT follow-up oscillometry 3-5 year olds R7 X7 AX7 PM2.5 CO",
  sub="RESP", design="Randomised controlled trial (follow-up)", pm="Prenatal and postnatal personal PM2.5 and CO exposure from the trial's monitoring",
  geo="Peru (Puno)", endpoint="Oscillometric lung function z-scores (R7, X7, fres, AX7) at age 3-5", tier="A",
  basis="Personal / wearable", affil="Johns Hopkins University, USA; Johns Hopkins University, USA",
  n=("Follow-up of 101 children aged 3-5 whose mothers were randomised to LPG stoves or usual biomass during pregnancy and infancy (HAPIN Peru). Oscillometry z-scores did not differ by arm (e.g. R7 -0.1 vs -0.2; AX7 1.2 vs 1.3); the only difference was a larger post-bronchodilator fall in fres z-score with LPG (-0.36, -0.71 to -0.02). "
     "No exposure-response association was found for prenatal or postnatal PM2.5; postnatal CO was associated with worse reactance (AX7 +0.041 z per 1 ppm, 0.003-0.078). "
     "Small subsample of the trial, many endpoints, and the CO signal is exploratory. "
     "Relevance: direct - a randomised exposure contrast with personal monitoring that still found no PM2.5 lung-function gradient in early childhood.")),
52: dict(short="Ahmedabad urban slum household air pollution biomass 47.1% PMUY uptake 16.7% mosquito coil incense",
  sub="OCC", design="Cross-sectional study", pm="No PM measured; household fuel and indoor combustion sources by interview",
  geo="India (Ahmedabad)", endpoint="Prevalence of indoor combustion sources; PMUY LPG scheme awareness and uptake; respiratory symptoms", tier="C",
  basis="Proxy / questionnaire", affil="B. J. Medical College, India; Christian Medical College and Hospital, India",
  n=("Community survey of 139 households in three urban slums in western India. Biomass fuel was used in 47.1% of households, often alongside indoor smoking, mosquito coils and incense; ventilation was poor and separate kitchens and exhausts rare. "
     "80.4% knew of the PMUY clean-cooking scheme but only 16.7% had used it. No household variable predicted unclean fuel use in multivariable models and CIs were wide. "
     "No pollutant was measured, symptoms were self-reported, and the sample was powered for fuel prevalence, not for association. "
     "Relevance: indirect - documents stacked indoor sources (coils, incense, biomass) that a single kitchen PM sensor would integrate but not apportion.")),
54: dict(short="National Jewish Health wood smoke PM mouse eosinophilic asthma Sprouty2 deletion ILC2 ERK1/2 IL-13",
  sub="RESP", design="Animal knockout experiment", pm="Wood smoke particulate matter by airway exposure; dose not stated in abstract",
  geo="USA (laboratory)", endpoint="Airway hyperreactivity, eosinophilic/neutrophilic inflammation, mucus, remodelling; ILC2 and Th cytokines", tier="B",
  basis="Lab / research instrument", affil="National Jewish Health, USA; National Jewish Health, USA",
  n=("Short-term airway exposure of naive B6 mice to wood smoke PM induced methacholine hyperreactivity, eosinophilic and modest neutrophilic inflammation, mucus production and remodelling, with more ILC2s and CD4 T cells, ERK1/2 phosphorylation and IL-5, IL-13 and IL-17A. "
     "Inducible Spry2 deletion prevented hyperreactivity, inflammation, mucus, collagen deposition and ERK1/2 activation, reduced ILC2 (not CD4 T cell) expansion and cut IL-13 and IL-17A. "
     "Dose, particle generation and group sizes are not in the abstract; acute dosing in naive mice models an exposure pattern, not chronic ambient smoke. "
     "Relevance: indirect - mechanism behind wildfire-smoke asthma, the exposure most commonly tracked with PurpleAir networks.")),
}
