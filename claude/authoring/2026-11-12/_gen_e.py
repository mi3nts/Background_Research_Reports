# -*- coding: utf-8 -*-
# Records for 12 Nov issue, part E.
R = {
95: dict(short="Peking University First Hospital 39015 endometriosis outpatient visits 2022-2024 DLNM apparent temperature PM2.5 PM10 ozone interaction",
  sub="REPR", design="Time series", pm="Daily PM2.5, PM10 and O3 (monitoring source not stated)",
  geo="China (Beijing)", endpoint="Daily endometriosis-related outpatient visits", tier="B",
  basis="Not stated", affil="Peking University First Hospital, China; Peking University First Hospital, China",
  n=("Quasi-Poisson DLNM time series of 39,015 endometriosis-related outpatient visits at one Beijing hospital, 2022-2024. Single-pollutant cumulative "
     "risks: PM2.5 lag 0-7 RR 1.109 (1.044-1.177) and PM10 lag 0-6 RR 1.070 (1.014-1.128), increments not stated in the abstract; high apparent "
     "temperature (P90 vs median) RR 1.126 (1.078-1.177) over lag 0-14; a positive additive interaction for temperature with ozone (IRR 1.114, "
     "1.053-1.180), not with PM. Outpatient visits for a chronic condition reflect care-seeking and scheduling as much as symptom flares, a single "
     "hospital limits generalisability, and 2022 includes COVID-era access disruption. "
     "Relevance: indirect - a new short-term endpoint for PM; exposure is city-wide, so within-city contrast is untested.")),
97: dict(short="Sydney bi-national semi-ecological small-area interstitial lung disease incidence air pollution climate land use metadata only",
  sub="RESP", design="Metadata only - no abstract available", pm="Ambient air pollution (per title; metrics not available)",
  geo="Australia; not confirmed (bi-national)", endpoint="Small-area ILD incidence (per title)", tier="C",
  basis="Not stated", affil="The University of Sydney, Australia; The University of Sydney, Australia",
  n=("Metadata only. European Respiratory Journal accepted manuscript with no abstract in PubMed at harvest. The title describes a bi-national "
     "semi-ecological study relating ambient air pollution, climate and land use to small-area incidence of interstitial lung disease; the second "
     "country, the pollutants, exposure model and effect estimates cannot be confirmed and no finding is asserted. Carried because ILD is an "
     "under-studied PM endpoint and small-area designs depend directly on the spatial resolution of the exposure surface. Recheck for the abstract "
     "in the weekly sweep. "
     "Relevance: possible - small-area exposure assignment where denser monitoring would reduce misclassification.")),
99: dict(short="Guangxi Minzu network meta-analysis 26 controlled trials 344 adults acute exercise heat cold hypoxia air pollution ventilation VO2 HR",
  sub="CVM", design="Systematic review + network meta-analysis", pm="Air pollution exposures in controlled exercise trials (types not specified in abstract)",
  geo="Global", endpoint="Minute ventilation, oxygen uptake, heart rate during acute exercise", tier="B",
  basis="Review / no primary exposure", affil="Guangxi Minzu University, China; Xinjiang Hetian College, China",
  n=("Network meta-analysis of 26 controlled trials (344 healthy adults) comparing acute exercise under heat, cold, hypoxia and air pollution against "
     "matched controls. Most pairwise contrasts were non-significant; hypoxia ranked highest for minute ventilation, heat for oxygen uptake and heart "
     "rate, and air pollution imposed the weakest effects on every outcome. No funnel asymmetry was found, though with 26 small trials that test has "
     "little power. Pollution exposures (diesel exhaust, PM, ozone) are pooled into one node in the abstract, so the null says nothing about any "
     "specific particle dose, and acute cardiorespiratory responses are not the pathway through which PM harms exercisers. "
     "Relevance: indirect - acute exercise physiology is an insensitive endpoint for PM.")),
100: dict(short="Durham Kathmandu Bandung 348 children 6-13 years KN95-style respirator unaided donning seven criteria nose clip",
  sub="BURD", design="Observational evaluation", pm="None measured; respirator use as protection against airborne particulates",
  geo="Nepal; Indonesia", endpoint="Correct unaided respirator donning", tier="C",
  basis="Not stated", affil="Durham University, United Kingdom; Durham University, United Kingdom",
  n=("348 children aged 6-13 in Kathmandu and Bandung donned two child-marketed KN95-style respirators without guidance. Only 21.8% met all seven "
     "essential donning criteria, though 79.6% completed at least five; nose-clip shaping was the commonest error. Older children and girls did "
     "better, prior KN95 experience improved technique and confidence, and respirator design mattered. Donning criteria are a proxy: no quantitative "
     "fit factor or inward leakage was measured, so the protective consequence of each error is inferred. "
     "Relevance: direct for mitigation - individual protection advice issued off sensor-network alerts assumes a fit that four in five children here "
     "did not achieve.")),
103: dict(short="Jingzhou Wuhan GBD 2021 204 countries cataract glaucoma geographic concordance 26 SEVs ambient particulate matter spatial-error",
  sub="OTHR", design="Ecological cross-country analysis", pm="GBD summary exposure value for ambient particulate matter pollution",
  geo="Global (204 countries)", endpoint="Age-standardised cataract and glaucoma prevalence, adults 55+", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Jingzhou Hospital, Yangtze University, China; Renmin Hospital of Wuhan University, China",
  n=("GBD 2021 country-level analysis of adults 55+ across 204 countries: 43.6% concordant for cataract and glaucoma burden, 25.5% cataract- and 30.9% "
     "glaucoma-dominant. Of 26 candidate summary exposure values modelled separately with SDI adjustment, ambient PM, ambient ozone, high BMI, low "
     "bone density and high temperature were positive for both outcomes (BH q<0.05); after super-region adjustment only temperature survived, while in "
     "spatial-error models only ambient PM did. Coefficients are not given in the abstract. Both exposure and outcome are GBD model outputs, so the "
     "association is between two modelled country aggregates, and results flip with specification. "
     "Relevance: indirect - weak ecological support for an ocular PM endpoint, consistent with yesterday's glaucoma cohort.")),
104: dict(short="Neuchatel Geneva Rev Med Suisse narrative review asthma air pollution climate change pollen thunderstorm wildfire",
  sub="RESP", design="Narrative review", pm="Outdoor and indoor air pollution (literature)",
  geo="Switzerland (clinical audience)", endpoint="Asthma development and control", tier="C",
  basis="Review / no primary exposure", affil="Reseau hospitalier neuchatelois, Switzerland; Hopitaux universitaires de Geneve, Switzerland",
  n=("Short French-language clinical review for Swiss practitioners. Outdoor and indoor pollution are described as major contributors to poor asthma "
     "control and possibly to disease onset; climate change adds longer pollen seasons, thunderstorm asthma, wildfires and flooding. Individual "
     "protective measures are judged of limited effectiveness, and source reduction through transport, urban planning and energy policy the most "
     "effective strategy, with a role for clinicians in education and advocacy. No new data, no stated search, and the effectiveness judgement on "
     "individual measures is not referenced in the abstract. "
     "Relevance: indirect - the scepticism about personal measures is relevant to sensor-driven personal alerting, which is where that judgement "
     "would need testing.")),
}
