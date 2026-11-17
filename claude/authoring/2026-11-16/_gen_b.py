# -*- coding: utf-8 -*-
# Records for 16 Nov issue, part B (authored 2026-11-17 run).
R = {
13: dict(short="BTHS July 2020 WRF-Chem double-high PM2.5 O3 NOx-VOC perturbation meteorological regimes aerosol feedback",
  sub="EXPO", design="Emissions scenario modelling", pm="WRF-Chem simulated PM2.5 and O3 under joint NOx-VOC emission perturbations, five meteorological regimes",
  geo="China (Beijing-Tianjin-Hebei-Shandong)", endpoint="Modelled PM2.5 and O3 response to precursor reductions", tier="C",
  basis="Model (CTM / LUR / ML)", affil="not stated in record",
  n=("WRF-Chem for July 2020 over Beijing-Tianjin-Hebei-Shandong, classifying co-occurring PM2.5/O3 'double high' days into five regimes by boundary-layer height, temperature and humidity. "
     "PM2.5 was highest under Stable and WarmHumid (~46 ug/m3) and lowest under DryHot (~40); O3 highest under DryHot and Moderate (~163 ug/m3). At 50%/50% NOx/VOC cuts, PM2.5 fell 20.6% (Stable) and 20.9% (WarmHumid) but only 15.2% (DryHot); O3 fell 25.2% (WarmHumid) and 23.3% (DryHot). Aerosol-meteorology feedback amplified PM2.5 reductions in the Stable and WarmHumid regimes. "
     "One month, one model, no reported evaluation statistics in the abstract. "
     "Relevance: low-moderate - regime-dependent control efficacy is testable with dense sensor networks resolving boundary-layer-driven PM variability.")),
19: dict(short="Air-conditioner filter dust primordial radionuclides geo-environmental controls dose assessment",
  sub="OCC", design="Metadata only", pm="Metadata only - indoor air-conditioner filter dust as a settled-particle sampler",
  geo="Not stated", endpoint="Metadata only - radionuclide activity and dose estimates", tier="C",
  basis="Lab / research instrument", affil="not stated in record",
  n=("Metadata only: no abstract was retrievable from PubMed, Europe PMC or Crossref. "
     "The record (Atmospheric Pollution Research; Abedin, Rahman, Khan) uses air-conditioner filter dust to appraise primordial radionuclide sources and dose. "
     "No finding is asserted here. "
     "Relevance: indirect - HVAC filters as passive integrating particle samplers are a known complement to real-time indoor PM sensors.")),
21: dict(short="Low-cost PM sensor calibration hygroscopic growth factor Hungary AAQR",
  sub="SENS", design="Metadata only", pm="Metadata only - low-cost optical PM sensor corrected with a hygroscopic growth factor",
  geo="Not stated", endpoint="Metadata only - calibrated low-cost PM against reference", tier="B",
  basis="Low-cost sensor / network", affil="not stated in record",
  n=("Metadata only: no abstract was retrievable from Crossref or the harvest legs. "
     "The title states a calibration of a low-cost particulate matter sensor using the hygroscopic growth factor (Aerosol and Air Quality Research; Kiss, Kiss, Veres). "
     "No finding, sensor model or error metric is asserted here. "
     "Relevance: high - kappa-Kohler/growth-factor humidity correction is the physics-based alternative to purely empirical RH terms in LCS calibration; worth pulling the full text for R2/RMSE and sensor model.")),
39: dict(short="India AOD long-term trends Koppen climate regions regional disparities",
  sub="EXPO", design="Metadata only", pm="Metadata only - satellite aerosol optical depth trends",
  geo="India", endpoint="Metadata only - AOD spatiotemporal trends by Koppen region", tier="C",
  basis="Satellite-fused", affil="not stated in record",
  n=("Metadata only: no abstract was retrievable. "
     "The record (Atmospheric Research; Tiwari, Gupta, Singh) analyses long-term AOD trends and regional disparities across Koppen climatic regions of India. "
     "No finding is asserted here. "
     "Relevance: indirect - stratifying AOD by climate regime is relevant to how AOD-to-PM2.5 conversion should vary in satellite-fusion models.")),
56: dict(short="Lyon equine fibrosing ILD SEM/EDS lung mineral microparticles case-control geogenic anthropogenic steel",
  sub="RESP", design="Case-control", pm="SEM/EDS count and classification of mineral microparticles in lung tissue; owner questionnaire for environment",
  geo="France", endpoint="Equine fibrosing interstitial lung disease", tier="C",
  basis="Lab / research instrument", affil="VetAgro Sup, University of Lyon, France; VetAgro Sup, University of Lyon, France",
  n=("Case-control study of lung tissue from 21 equids with fibrosing interstitial lung disease and 10 healthy horses, particles counted and classified by SEM/EDS. "
     "Geogenic particles dominated all samples. Anthropogenic particle share was higher in idiopathic cases (median 20.2%, IQR 4.9-66.7) than controls (2.3%, 1.3-4.5; p=0.032); FeCrNi steel particles were more common in cases, and calcium compounds and iron oxide occurred only in idiopathic cases. Steel and iron-oxide proportions correlated with living indoors (R2 0.26 and 0.48). Questionnaire exposures did not differ. "
     "Ten controls, retrospective blocks, and no air measurements, so source attribution is inferential. "
     "Relevance: low - stable/barn particle exposure in a sentinel species; no sensing content.")),
57: dict(short="UCSF MGB review ambient and wildfire air pollution chronic rhinosinusitis olfaction allergic rhinitis head and neck cancer",
  sub="RESP", design="Narrative review", pm="Ambient air pollution and wildfire-specific air pollution as characterised in the reviewed studies",
  geo="Multinational (review)", endpoint="Chronic rhinosinusitis, olfactory dysfunction, allergic rhinitis, head and neck cancer", tier="C",
  basis="Review / no primary exposure", affil="University of California San Francisco, USA; Mass General Brigham, USA",
  n=("Narrative review of ambient and wildfire-specific air pollution and upper airway disease. "
     "Recent biobank and claims studies strengthen ambient associations with allergic rhinitis and chronic rhinosinusitis incidence, with emerging evidence that pollution shapes inflammatory endotype and blunts symptom improvement after endoscopic sinus surgery; wildfire smoke shows a dose-dependent association with acute rhinosinusitis care and with head and neck cancer incidence. "
     "No new estimates; the abstract gives no effect sizes, and the cited wildfire metrics are mostly modelled smoke PM2.5. "
     "Relevance: indirect - the call for prospective mechanistic studies would benefit from personal or home PM2.5 during smoke events.")),
58: dict(short="Scopus 2020-2025 scientometric air pollution and cancer 3056 documents collaboration networks",
  sub="BURD", design="Bibliometric analysis", pm="Not applicable - publication records",
  geo="Global (bibliometric)", endpoint="Scholarly output, citation impact, collaboration and thematic evolution", tier="C",
  basis="Review / no primary exposure", affil="Universidad Nacional Federico Villarreal, Peru; Universidad San Ignacio de Loyola, Peru",
  n=("Scientometric analysis of 3,056 Scopus documents (1,401 sources) on air pollution and cancer published 2020-2025, using SciVal and Bibliometrix: output growth (13.3% per year), CiteScore, SNIP, h-index, Bradford core journals, collaboration life-cycle and thematic evolution. "
     "The abstract does not report the leading themes, countries or networks in quantitative form. "
     "Bibliometrics counts papers, not evidence; it says nothing about effect sizes or exposure quality. "
     "Relevance: low - no exposure or measurement content.")),
60: dict(short="New Mexico 597 paediatric decedents postmortem CT bone mineral density gestational AQI trimester",
  sub="REPR", design="Cross-sectional", pm="County-level Air Quality Index over the 9 months before birth, by trimester; ambient temperature extremes",
  geo="United States (New Mexico)", endpoint="Bone mineral density and porous cranial lesions on postmortem CT", tier="C",
  basis="Reference / regulatory monitor", affil="University of New Mexico Health Sciences Center, USA; University of New Mexico, USA",
  n=("Postmortem CT scans of 597 paediatric decedents (6 months to 20.9 years) in New Mexico, 2011-2023, linked to county-level AQI and temperature during the 9 months before birth. "
     "Lower BMD was associated with poorer AQI in trimesters 2 and 3, trimester 2 being the candidate sensitive window; AQI was unrelated to porous cranial lesions and temperature extremes to either outcome. "
     "No effect sizes in the abstract. AQI is a composite dominated by whichever pollutant is worst on a day, assigned at county level, and a decedent sample is not representative of living children. "
     "Relevance: indirect - county AQI is the coarsest exposure surrogate; a pollutant-specific, address-level PM2.5 estimate is the obvious next step.")),
}
