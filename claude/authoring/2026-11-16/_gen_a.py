# -*- coding: utf-8 -*-
# Records for 16 Nov issue, part A (authored 2026-11-17 run). DOI/PMID/journal/title injected from cache by _gen.py.
R = {
1: dict(short="ECHO 18-site US pregnancy PM2.5 postpartum EPDS anhedonia BMI effect modification DLM",
  sub="NEU", design="Prospective cohort", pm="Daily residential PM2.5 from a validated satellite-based spatiotemporal hybrid model over the pregnancy residential history",
  geo="United States (18 ECHO sites)", endpoint="Edinburgh Postnatal Depression Scale total, anhedonia and depressive subscales within 1 y of delivery", tier="B",
  basis="Satellite-fused", affil="Icahn School of Medicine at Mount Sinai, USA; not stated in record",
  n=("6,407 pregnant women from 18 ECHO sites; residential PM2.5 from a satellite-based hybrid model, EPDS completed within a year of delivery, analysed with GAMs, distributed lag models and trimester windows. "
     "Main-effect models found no overall PM2.5-EPDS association. Thin-plate GAMs suggested a nonlinear PM2.5 x pre-pregnancy BMI interaction for the anhedonia subscale (interaction p=0.06), with positive associations at higher BMI, strongest for first-trimester exposure; DLM cumulative estimates agreed. No effect sizes or CIs are given in the abstract. "
     "The headline is a borderline interaction from a two-dimensional smooth after a null main effect, with multiple windows and three outcomes, so it is hypothesis-generating at best. "
     "Relevance: indirect - modelled exposure with no measurement contribution; susceptibility-by-BMI framing could inform targeted personal monitoring.")),
2: dict(short="Toulouse systematic review occupational pollutants arrhythmia atrial fibrillation lead CS2 solvents inhalable particles",
  sub="OCC", design="Systematic review", pm="Occupational inhalable particles among metals, solvents, gases and pesticides; exposure metrics as reported by 21 primary studies",
  geo="Multinational (review)", endpoint="Cardiac arrhythmia, including atrial fibrillation", tier="C",
  basis="Review / no primary exposure", affil="Toulouse-Purpan University Hospital, France; Toulouse-Purpan University Hospital, France",
  n=("Systematic review of 21 studies on chronic occupational exposure (metals, solvents, aldehydes, amines, cyanides, plastics, acids, gases, pesticides) and cardiac arrhythmia. "
     "Lead, carbon disulfide, certain solvents and inhalable particles were associated with arrhythmias, chiefly atrial fibrillation; oxidative stress, cytotoxicity and inflammation are proposed as mechanisms. "
     "No pooled estimate, risk-of-bias grading or particle size fraction is reported in the abstract, so the particle signal cannot be separated from co-exposures in the source workplaces. "
     "Metadata gives no search dates or databases beyond 'several'. "
     "Relevance: low - occupational particle exposure is mentioned but not quantified; wearable PM monitoring in factories is the obvious missing exposure layer.")),
3: dict(short="Korea narrative review indoor air quality management COPD IPF nine-parameter action references",
  sub="OCC", design="Narrative review", pm="Indoor PM2.5 and PM10 alongside NO2, CO2, formaldehyde, TVOC, CO, O3 and relative humidity; reference values from national and international standards",
  geo="Republic of Korea", endpoint="Practical IAQ action references and maintenance targets for COPD and IPF patients", tier="C",
  basis="Review / no primary exposure", affil="Yonsei University, Republic of Korea; Yonsei University College of Medicine, Republic of Korea",
  n=("Focused narrative review proposing residential indoor air quality management rules for patients with COPD and idiopathic pulmonary fibrosis. "
     "Nine parameters were selected (PM2.5, PM10, NO2, CO2, formaldehyde, TVOC, CO, O3, relative humidity), each with an action reference and a maintenance target that keep the source standard's averaging time; ambient forecast categories are used only for outdoor-driven pollutants. "
     "Recommendations: source control, forecast-guided ventilation, particle filtration and cooking/combustion control. "
     "The thresholds are explicitly not disease-specific clinical cut-offs, and no new exposure-response evidence is presented. "
     "Relevance: moderate - the framework presumes a home monitor reporting PM2.5 and PM10 at standard averaging times, exactly the use case for consumer-grade sensors, whose bias at high humidity is not addressed.")),
6: dict(short="GBD 2023 Ethiopia national subnational air pollution deaths DALYs ambient PM household solid fuel 1990-2023",
  sub="BURD", design="Burden of disease (GBD)", pm="GBD 2023 ambient PM2.5 and household air pollution from solid fuels exposure estimates",
  geo="Ethiopia", endpoint="Deaths, YLDs, YLLs and DALYs attributable to air pollution", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Adigrat University, Ethiopia; Bule Hora University, Ethiopia",
  n=("GBD 2023 secondary analysis for Ethiopia, national and subnational, 1990-2023. "
     "In 2023 air pollution was attributed 139 deaths per 100,000 (95% UI 106-177), 4,286 YLLs (3,475-5,107) and 4,557 DALYs per 100,000 (3,685-5,397); YLDs were driven by household solid fuels (247 per 100,000, UI 152-344). "
     "Addis Ababa had the highest ambient PM mortality (64 per 100,000, UI 43-88) and the lowest household air pollution mortality; Afar had the highest overall mortality (185, UI 137-232). Mortality rates were flat across 33 years while DALY rates fell. "
     "Every number inherits GBD's exposure surface, which in Ethiopia rests on very few ground monitors; the subnational contrasts are model outputs, not observations. "
     "Relevance: high in principle - Ethiopia is a textbook case where a low-cost network would constrain the ambient surface the burden depends on.")),
7: dict(short="GCARE review 60 studies indoor green infrastructure IEQ monitoring modelling VOC PM removal",
  sub="OCC", design="Systematic review", pm="Indoor PM and VOCs with temperature, humidity and CO2 as monitored in 60 indoor-greening studies",
  geo="Multinational (review)", endpoint="Indoor environmental quality change attributable to indoor green infrastructure", tier="C",
  basis="Review / no primary exposure", affil="University of Surrey (GCARE), United Kingdom; Federal Institute of Hydrology, Germany",
  n=("Review of 60 studies of passive (potted plants, green walls, indoor trees) and active (hydroponics, biofilters) indoor greening and indoor environmental quality. "
     "Passive systems typically cut VOCs 10-30% and buffer temperature and humidity; active systems removed VOCs and PM more efficiently. 59% of studies were laboratory, 33% in situ, many with 6-48 h chamber runs; controlled settings overstate removal relative to real buildings, and descriptors and ventilation data are not standardised. Passive configurations reduced cooling demand 22-27%. "
     "No PM removal rate is quantified in the abstract, and the evidence is dominated by short chamber tests with few taxa. "
     "Relevance: moderate - the review's main ask, long in-situ IEQ monitoring with ventilation logging, is a direct job for indoor low-cost PM/CO2 nodes.")),
8: dict(short="Eastern China lake and coastal bay large-aperture scintillometer aerosol mass flux RMN(RH) PM10 calibration",
  sub="SENS", design="Measurement campaign", pm="Path-averaged aerosol mass flux from large-aperture scintillometer log-intensity spectra; conversion factor calibrated against PM10, visibility and RH",
  geo="China (eastern; inland lake and coastal bay)", endpoint="Aerosol mass-flux magnitude over open water", tier="B",
  basis="Lab / research instrument", affil="not stated in record",
  n=("First large-aperture scintillometer (LAS) retrieval of path-averaged aerosol mass flux over open water, four campaigns at an inland lake and a coastal bay in eastern China. "
     "The aerosol (imaginary) and thermodynamic (real) refractive-index contributions were separated from the log-intensity spectrum, and the constant mass-to-optical conversion factor was replaced by a campaign-specific RMN(RH) calibrated against PM10, visibility and RH; RMN fell consistently with humidity. "
     "Campaign-median flux magnitudes were 0.091-0.399 ug m-2 s-1, with daytime enhancement; dense coastal fog was the main operational limit. "
     "Magnitudes only (no sign), validation is against calculated dry deposition rather than eddy covariance, and n=4 campaigns. "
     "Relevance: moderate - the RH-dependent optical-to-mass conversion is the same hygroscopic problem that biases optical low-cost PM sensors.")),
10: dict(short="Reunion Island September 2017 biomass-burning aerosol layers lidar AERONET FTIR CO CAMS FLEXPART",
  sub="EXPO", design="Episode analysis (observations + model)", pm="AERONET AOD 550 nm, Raman/elastic lidar layers, CALIOP, MODIS, CAMS EAC4 reanalysis; FLEXPART source attribution",
  geo="Reunion Island (France, SW Indian Ocean)", endpoint="Vertical structure and source of free-tropospheric smoke layers", tier="C",
  basis="Lab / research instrument", affil="not stated in record",
  n=("Case study of a September 2017 biomass-burning aerosol episode over Reunion Island combining AERONET, ground lidar, FTIR CO, MODIS, CALIOP, CAMS EAC4 and FLEXPART. "
     "AOD at 550 nm reached 0.16-0.42. Lidar resolved one layer at 2.8-4.7 km on 19 September (Angstrom 355/532 = 1.32 +/- 0.23) and two on 25 September: 3.3-5 km (1.45 +/- 0.12) and a drier 5-9 km layer (1.60 +/- 0.06). FLEXPART, checked against smoothed FTIR CO, attributes both to southern Africa with a South American contribution to the lower layer. "
     "Two days in one month; layers sit in the free troposphere, so surface PM implications are not addressed. "
     "Relevance: low - column/vertical context only; a reminder that column AOD in satellite-fusion models can be decoupled from surface PM.")),
}
