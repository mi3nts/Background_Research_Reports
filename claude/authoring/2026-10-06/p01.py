# -*- coding: utf-8 -*-
P = [
 dict(pmid="42838330", doi="10.1016/j.envpol.2026.129269", journal="Environ Pollut",
  short="Wang et al. 2026c",
  title="Long-Term Air Pollution Exposure and Brain Structural Decline: A Longitudinal Analysis",
  sub=corpus.NEU, design="Prospective cohort",
  pm="Residential PM2.5 and PM10 from high-resolution spatiotemporal models",
  geo="Not stated in abstract (middle-aged and older adult imaging cohort)", endpoint="Grey matter volume, white matter hyperintensity progression", tier="B",
  n=("4,276 middle-aged and older adults with repeated brain MRI; global, grey- and white-matter volumes "
     "and white-matter hyperintensity burden regressed on modelled residential PM2.5 and PM10 in fully "
     "adjusted multivariable models. Higher long-term particulate exposure was associated with accelerated "
     "global and regional grey-matter loss and greater WMH progression, which the authors read as both a "
     "neurodegenerative and a cerebrovascular pathway. Limitation: the abstract gives no effect sizes, no "
     "confidence intervals, no exposure contrast and does not name the cohort or country - unusual for a "
     "quantitative imaging analysis, and it makes the result unassessable as reported; repeat-MRI "
     "subsamples are also selected for survival and compliance. Relevance: moderate - brain structure is "
     "the mediator between the UFP dementia-mortality signal and clinical disease, but this record cannot "
     "be entered as an effect estimate.")),

 dict(pmid="42836291", doi="10.19191/ep26.4-5.s1.a1030.092", journal="Epidemiol Prev",
  short="Ranzi et al. 2026",
  title="Atlante Aria e Salute: methods for estimating the health impacts of air pollution and national application",
  sub=corpus.BURD, design="Health impact model",
  pm="Modelled annual PM2.5 and NO2 at 1x1 km, random forest over monitors, satellite and covariates, 2016-2024",
  geo="Italy (national, municipality level)", endpoint="Natural, cardiovascular, respiratory and lung-cancer mortality", tier="B",
  n=("Methodological description of the Air and Health Atlas, an interactive national platform. PM2.5 and "
     "NO2 are modelled at 1 km with random forests, converted to population-weighted exposure at "
     "municipality level against 2021 census blocks, and combined with provincial death-certificate rates "
     "through HRAPIE-2 concentration-response functions against the 5 ug/m3 WHO counterfactual; 2019 is "
     "shown as an illustration, with pronounced north-south gradients. Limitation: population-weighted "
     "exposure at municipality scale cannot capture within-municipality contrast, the random-forest surface "
     "is validated against the same monitors that train it, and HRAPIE-2 functions are transferred from "
     "other populations. Relevance: high - this is the operational template a low-cost network would be "
     "asked to improve, and the 1 km population-weighted step is exactly where added density pays.")),

 dict(pmid="", doi="10.1155/ina/5050009", journal="Indoor Air",
  short="Othman et al. 2026",
  title="Impact of Urban Land Use on Indoor Air Quality: Quantifying Ambient Particle Infiltration and Asthma Risk in Naturally Ventilated School Buildings",
  sub=corpus.OCC, design="Field measurement",
  pm="Paired indoor-outdoor 24 h PM2.5 and PM1 with infiltration factor, 10 schools across five land-use classes",
  geo="Malaysia (Klang Valley)", endpoint="Asthma risk (modelled)", tier="A",
  n=("Ten primary schools stratified by land use (high-traffic, industrial, residential, mixed "
     "industrial/high-traffic, mixed industrial/port) with paired indoor-outdoor PM2.5 and PM1. Indoor "
     "maxima were at mixed industrial/port schools (24 h PM2.5 35.33 +/- 9.25, PM1 23.79 +/- 5.87 ug/m3); "
     "outdoor maxima at high-traffic schools (34.50 +/- 20.64 and 23.78 +/- 13.09); land-use class "
     "differences were significant (p<0.05) and the mean infiltration factor exceeded 0.6. Limitation: "
     "ten buildings across five classes is two per class, so the land-use contrast is confounded with "
     "building; Finf estimated from indoor-outdoor ratios without an independent air-change measurement "
     "absorbs any indoor source into the infiltration term. Relevance: high - Finf > 0.6 in naturally "
     "ventilated classrooms means outdoor network data is a usable proxy for children's exposure in this "
     "climate, which is the assumption most school studies make without testing.")),

 dict(pmid="", doi="10.3390/atmos17100977", journal="Atmosphere",
  short="Mukhamediyarov et al. 2026",
  title="Elemental Composition, Sources, and Health Risks of Ambient PM2.5 in Ust-Kamenogorsk (Oskemen) and Pavlodar, Kazakhstan",
  sub=corpus.EXPO, design="Source apportionment",
  pm="PM2.5 elemental composition by ICP-OES and ICP-MS with PCA source resolution",
  geo="Kazakhstan (Ust-Kamenogorsk, Pavlodar)", endpoint="Non-carcinogenic and carcinogenic inhalation risk (modelled)", tier="C",
  n=("PCA separates a non-ferrous metallurgical profile in Ust-Kamenogorsk from coal fly ash, ferrous "
     "metallurgy and petrochemicals in Pavlodar. The risk arithmetic then reports cumulative hazard "
     "indices exceeding 1 by more than 500-fold, driven by Zn (HQinh 304.7) and Al (129.5), and "
     "carcinogenic risks for Cr and As up to 9x the 1e-4 threshold. Limitation: a hazard quotient of 300 "
     "for zinc is a sign that the reference concentration is being misapplied, not that residents are "
     "inhaling a toxic zinc dose - EPA inhalation RfCs do not exist for several of these elements and the "
     "substitutes used are oral values scaled by default breathing rates; sampling duration and n are not "
     "stated. Relevance: moderate for the Central Asian composition data, which is genuinely scarce; the "
     "risk numbers should not be propagated.")),
]
