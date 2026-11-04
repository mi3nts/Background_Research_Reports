# -*- coding: utf-8 -*-
P = [
 dict(pmid="42074440", doi="10.3390/ijerph23040501", journal="Int J Environ Res Public Health",
  short="Sharon IoT vape detection school PM2.5 PM10 37 locations 18 months 2026",
  title="Smart Vape Detection in Schools for Mitigating Student E-Cigarette Use",
  sub=corpus.SENS, design="Longitudinal case study of a sensor deployment", pm="PM2.5 and PM10 at one-minute resolution, threshold alerting",
  geo="Australia", endpoint="Vaping alert events, CCTV verification, staff response", tier="B",
  basis="Low-cost sensor / network", affil="Blue IoT Pty Ltd, Australia; Queensland University of Technology, Australia",
  n=("BACKFILL (entry 4 May 2026). Low-cost IoT PM nodes at 37 restroom and change-room locations in one Australian independent school, one-minute data for 18 months, "
     "threshold alerts with school-led CCTV verification. More than 300 vaping-related incidents, clustered by time of day and among senior students; alerts showed "
     "rapid concurrent PM2.5 and PM10 excursions. Staff response declined through alert fatigue, and a regional smoke event produced false positives. "
     "No sensitivity, specificity or denominator of unverified alerts in the abstract. Limitation: first-author affiliation is the IoT vendor; 'highly effective' is claimed without "
     "a confusion matrix. Relevance: high - event detection from PM transients on low-cost nodes, with the human-response failure and the need for "
     "context-aware logic documented.")),
 dict(doi="10.1093/eurpub/ckag169.841", journal="Eur J Public Health",
  short="Dyer urban burden of disease 825 European cities joint PM2.5 NO2 green space 2026",
  title="Urban burden of disease estimation for policy making: health impacts of environmental stressors",
  sub=corpus.BURD, design="Comparative risk assessment", pm="Modelled PM2.5 and NO2, joint exposure estimation, against WHO guidelines",
  geo="Europe (825 cities)", endpoint="Deaths attributable to exposure above WHO guidelines and to insufficient green space", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Barcelona Institute for Global Health (ISGlobal), Spain; not stated in Crossref",
  n=("BACKFILL (Crossref deposit 26 October 2026; congress abstract). Comparative risk assessment across 825 European cities, three reporting periods 2015-2024. Exceeding WHO "
     "guidelines gave 213,889 deaths (95% CI 89,224-344,223) jointly attributable to PM2.5 and NO2 in 2018, reported as 76,833 fewer than summing single-pollutant estimates (PM2.5 145,747; NO2 143,646; the printed figures actually differ by 75,504). "
     "Limitation: abstract only; the joint method is not specified, the interval is wide, and attribution inherits the concentration-response function and the exposure model "
     "with no measured validation stated. Relevance: moderate - summing pollutant burdens overstates by about a quarter here, "
     "and city-scale burden accounting is where dense sensor fields could test the modelled surface.")),
 dict(pmid="42074891", doi="10.3390/jcm15083089", journal="J Clin Med",
  short="Kim prenatal PM2.5 pediatric inguinal hernia hydrocele kriging cohort 2026",
  title="Prenatal Fine Particulate Matter (PM2.5) Exposure and the Risk of Pediatric Inguinal Hernia or Hydrocele: A Retrospective Cohort Study",
  sub=corpus.REPR, design="Retrospective cohort", pm="Monthly residential PM2.5 by kriging from fixed monitoring stations",
  geo="South Korea", endpoint="Offspring inguinal hernia or hydrocele (ICD-10)", tier="C",
  basis="Reference / regulatory monitor", affil="Keimyung University, South Korea; Keimyung University School of Medicine, South Korea",
  n=("BACKFILL (entry 4 May 2026). 1,093 mother-offspring pairs, one tertiary centre, deliveries July 2016-June 2019, follow-up to March 2024; 53 cases (4.85%). Second-trimester PM2.5 "
     "OR 1.07 (1.01-1.14) per 1 ug/m3; an IQR increase gave OR 1.64 (no CI, IQR width not stated). Male sex OR 24.71 (5.95-102.54). AUC 0.804. Limitation: 53 events against several trimester "
     "windows with no stated multiplicity correction, referral-centre cohort, hernia and hydrocele pooled, and a mechanism inferred rather than tested. Treat as hypothesis. "
     "Relevance: low - kriging from fixed stations, with sparse-network error in a trimester-specific contrast, the setting where denser residential estimates would matter.")),
 dict(pmid="42970988", doi="10.1016/j.chemosphere.2026.145136", journal="Chemosphere",
  short="Karimi PMOS polycystic ovary metabolic syndrome Arak Iran PM2.5 PR IDW 2026",
  title="Air pollution and polycystic ovary metabolic syndrome (PMOS) in a heavily industrialized Middle Eastern city: A cross-sectional study.",
  sub=corpus.REPR, design="Cross-sectional study", pm="365-day residential PM2.5 and PM10 by inverse-distance weighting from three stations",
  geo="Iran (Arak)", endpoint="Polycystic ovary metabolic syndrome prevalence", tier="B",
  basis="Reference / regulatory monitor", affil="Arak University of Medical Sciences, Iran; Arak University of Medical Sciences, Iran",
  n=("301 women at gynecology clinics in Arak (153 PMOS, 148 non-PMOS), April 2024-March 2025. Modified Poisson, per 1-SD: PM2.5 PR 1.22 (1.09-1.35), PM10 PR 1.23 (1.09-1.36), NO2 1.21 (1.07-1.33), "
     "SO2 1.15 (1.01-1.28). Cases had 3.00 ug/m3 more PM2.5. Sensitivity windows and propensity matching agreed. SD widths are not in the abstract. Limitation: exposure from three stations "
     "by IDW in an industrial city carries little real spatial contrast, so residence and socioeconomic position are confounded with it; clinic controls and prevalent cases rule out "
     "temporal inference. Relevance: moderate - a study whose result hangs on three monitors is where a small low-cost network would directly test the contrast.")),
]
