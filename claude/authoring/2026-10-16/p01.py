# -*- coding: utf-8 -*-
P = [
 dict(pmid="42887622", doi="10.1016/j.hrthm.2026.10.013", journal="Heart Rhythm",
  short="MESA incident AF time-varying pollution 2026",
  title="Association of Air Pollution Exposure and Risk of Incident Atrial Fibrillation: The Multi-Ethnic Study of Atherosclerosis",
  sub=corpus.CVM, design="Prospective cohort", pm="Spatiotemporal-model PM2.5, NO2, NOx, O3 at residence; 2-y rolling means updated every 30 d",
  geo="United States (6 MESA metros)", endpoint="Incident atrial fibrillation", tier="A",
  n=("6,618 MESA participants (mean age 62), 16.5 y median follow-up, 1,055 incident AF events. Exposure came from the "
     "MESA Air hierarchical spatiotemporal models, which assimilate cohort-specific snapshot monitoring, entered as "
     "time-varying 2-y averages. Per IQR of NO2 (13.5 ppb) AF hazard rose 29% (HR 1.29, 95% CI 1.00-1.67); PM2.5, NOx and "
     "O3 were weaker and directionally positive, with no estimates in the abstract. Limitation: AF ascertainment from "
     "hospitalisation and study ECGs misses paroxysmal disease, and the NO2 CI touches the null; the PM2.5 contrast "
     "within six metros is narrow. Relevance: high methodologically - this is the cohort where supplemental "
     "community monitoring was built to cut exposure error, and PM2.5 still came out null-leaning.")),
 dict(pmid="42885770", doi="10.1161/jaha.126.049988", journal="J Am Heart Assoc",
  short="West Florida temperature x PM2.5 CVD admissions 2026",
  title="Joint Impacts of Ambient Air Pollution and Temperature on Cardiovascular Disease in West Florida",
  sub=corpus.CVM, design="Time-series", pm="Daily network-monitor PM2.5 and temperature, DLNM lags 0-7 with tensor-product interaction",
  geo="United States (West Florida)", endpoint="Admissions for MI, heart failure, stroke", tier="B",
  n=("BayCare Health System admissions 2017-2024 analysed with distributed-lag GAMs and tensor-product temperature x "
     "PM2.5 surfaces, copollutant-adjusted. Temperature dominated: MI risk in adults >=65 was lower at warmer days "
     "(RR75/25 0.92, 0.89-0.95), heart failure was U-shaped with heat risk in younger and Black patients (RR75/25 1.05, "
     "1.02-1.09). PM2.5 was weak; the largest signal was stroke in Black patients, RR75/25 1.02 (0.96-1.08). Limitation: "
     "a single-system admissions series assigns one area-wide monitor value to a coastal region with low, compressed "
     "PM2.5, so near-null PM results partly reflect a small exposure contrast; subgroup multiplicity is unaddressed. "
     "Relevance: moderate - low-concentration subtropical settings are where denser networks would sharpen the contrast.")),
 dict(pmid="42887288", doi="10.1016/j.ijheh.2026.114932", journal="Int J Hyg Environ Health",
  short="Uberlandia street vendors PM2.5 micronuclei panel 2026",
  title="Urban air pollution and genotoxic damage in street vendors: a longitudinal repeated-measures panel study",
  sub=corpus.OCC, design="Panel study", pm="PM1, PM2.5, PM10 at seven fixed work-area monitoring points",
  geo="Brazil (Uberlandia)", endpoint="Buccal-cell micronucleus frequency", tier="B",
  n=("238 men over four campaigns spanning rainy and dry seasons: 116 outdoor street vendors in the city centre vs 122 "
     "indoor formal vendors in a reference area. PM concentrations and MN frequency were both consistently higher in the "
     "centre. Poisson GEE: per 1 ug/m3 PM2.5, MN IRR 1.024 (1.013-1.034) rainy and 1.026 (1.019-1.034) dry; no season "
     "interaction (p=0.378). Limitation: exposure is fixed-point area monitoring, not personal, and is collinear with "
     "occupation group, so the PM2.5 slope partly encodes street vs indoor work (traffic gases, PAHs, sun, smoking "
     "patterns). Relevance: moderate - seven fixed points is exactly the density at which a small low-cost array could "
     "convert an ecological contrast into personal-scale exposure.")),
 dict(pmid="42881829", doi="10.3390/jcm15197367", journal="J Clin Med",
  short="Northern Thailand NPC survival PM2.5 and coarse PM 2026",
  title="The Effect of Fine (PM2.5) and Coarse (PM10-2.5) Particulate Matter on Survival Outcomes in Nasopharyngeal Carcinoma Patients: A Retrospective Cohort Study in a Northern Thailand Tertiary Care Center",
  sub=corpus.OTHR, design="Metadata only (no abstract)", pm="PM2.5 and PM10-2.5 (exposure model not stated)",
  geo="Thailand (northern)", endpoint="Survival in nasopharyngeal carcinoma", tier="C",
  n=("No abstract at harvest. Title indicates a single-centre retrospective cohort of nasopharyngeal carcinoma patients "
     "in northern Thailand relating fine and coarse PM to survival. Recorded for coverage; no estimate inferred. "
     "Relevance: moderate - northern Thailand's biomass-burning season is a well-instrumented low-cost-sensor region, "
     "and a coarse-fraction prognosis question needs PM10-2.5 that optical LCS estimate poorly.")),
]
