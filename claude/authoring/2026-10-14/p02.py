# -*- coding: utf-8 -*-
P = [
 dict(pmid="42872554", doi="10.1002/alz.71837", journal="Alzheimers Dement",
  short="ALFA+ TRAP CSF GFAP 2026",
  title="Air pollution is associated with sex-specific longitudinal changes in astrocytic and neuroinflammatory processes linked to cognitive decline in Alzheimer's disease at-risk individuals",
  sub=corpus.NEU, design="Prospective cohort", pm="LUR NO2, PM10, PM2.5, PM2.5 absorbance",
  geo="Spain (Barcelona, ALFA+)", endpoint="3-year change in CSF GFAP, IL-6 and AD biomarkers; executive function", tier="B",
  n=("226 cognitively unimpaired middle-aged adults at elevated AD risk with baseline and 3-year CSF. Higher traffic-related "
     "exposure associated with longitudinal increases in GFAP and IL-6, mainly in women; GFAP partially mediated "
     "associations with worsening executive and attentional performance. Limitation: no effect sizes in the abstract; "
     "n=226 split by sex across four correlated pollutants and many biomarkers is a multiplicity problem, and "
     "single-address LUR estimates ignore time-activity. Relevance: moderate - CSF longitudinal biology is rare, but "
     "this is hypothesis-generating at this n.")),
 dict(pmid="42872515", doi="10.1111/risa.70368", journal="Risk Anal",
  short="Abu Dhabi PM burden 2008-2022 2026",
  title="Ambient Air Pollution Health Impacts in High-Income Countries, Part II: A Case Study in the United Arab Emirates",
  sub=corpus.BURD, design="Health impact model", pm="Anthropogenic PM and ozone, 2019-2022 vs 2008",
  geo="United Arab Emirates (Abu Dhabi)", endpoint="Attributable deaths and hospital visits", tier="B",
  n=("Attributable deaths from anthropogenic PM and ozone in Abu Dhabi rose from 231 (90% UI 59-427) in 2008 to 1,249 "
     "(507-2,169) in 2019-2022, despite air quality holding roughly steady while population doubled. The increase "
     "reflects population growth, better health records and, mainly, steeper concentration-response functions. "
     "Limitation: a fivefold change driven largely by swapping CRFs is a change in assumptions, not in burden; the "
     "'anthropogenic' split in a dust-dominated desert regime is itself model-dependent. Relevance: moderate - shows how "
     "far CRF choice swamps measured trends, which bounds what better monitoring alone can change.")),
 dict(pmid="42871629", doi="10.1021/acsestair.6c00155", journal="ACS EST Air",
  short="DC 1 km WRF-SMOKE-CMAQ 2026",
  title="Neighborhood-Scale O3, NO2, and PM2.5 in Washington, D.C. from a 1 x 1 km2 WRF-SMOKE-CMAQ Framework",
  sub=corpus.EXPO, design="Chemical transport model", pm="Hourly O3, NO2, PM2.5 at 1 km (2017)",
  geo="United States (Washington, D.C.)", endpoint="No health endpoint", tier="B",
  n=("1 km CMAQ for 2017: hourly O3 r up to 0.7; NO2 biased -14 to -29% from unresolved near-road gradients. NO2's "
     "coefficient of variation exceeded O3's and was more than three times PM2.5's; urban-core O3 was 4-11% lower from "
     "titration. Moving from 4 to 1 km changed population-weighted exposure by only -1.5 to -3% for PM2.5. Limitation: "
     "evaluation against a handful of AQS sites in one city cannot test intra-urban gradients - the very thing 1 km is "
     "meant to add. Relevance: high - quantifies that PM2.5 is the spatially smoothest pollutant, so dense PM2.5 "
     "networks buy less spatial information than NO2 networks would.")),
 dict(pmid="", doi="10.1021/acs.est.6c07592", journal="Environ Sci Technol",
  short="Indoor NPF from outdoor O3 2026",
  title="Elevated Outdoor O3 Can Sustain New Particle Formation and Growth Indoors",
  sub=corpus.OCC, design="Field measurement", pm="Indoor particle number size distributions; ventilated O3; limonene addition",
  geo="Not stated (aged unoccupied office, high-O3 region)", endpoint="No health endpoint", tier="B",
  n=("In an authentic office in a high-O3 region, mechanical ventilation supplied enough O3 that indoor new particle "
     "formation was VOC-limited, not O3-limited; limonene addition drove growth at 20-100 nm/h, one to two orders above "
     "outdoor rates, with meaningful mass from grown particles. Limitation: one building, injected limonene rather than "
     "real product use, and no occupancy. Relevance: high - indoor UFP and secondary mass from cleaning products are "
     "invisible to PM2.5-only indoor sensors until particles grow past ~300 nm.")),
]
