# -*- coding: utf-8 -*-
P = [
 dict(pmid="42931706", doi="10.3390/toxics14100920", journal="Toxics",
  short="Cerin air pollution road environment cardiometabolic walking AusDiab 2026",
  title="Associations of Ambient Air Pollution and Road-Related Environmental Characteristics with Cardiometabolic Health: The Role of Walking",
  sub=corpus.CVM, design="Cross-sectional (cohort baseline)", pm="Residential PM2.5 and NO2 (modelled); road density, distance to nearest busy road",
  geo="Australia (AusDiab wave 3)", endpoint="Blood pressure, lipids, HbA1c, waist; walking time", tier="B",
  n=("4,141 middle-aged and older adults; GAMMs with FDR control within test families. PM2.5 associated positively with "
     "diastolic and non-linearly with systolic BP; road density with lower HDL and higher triglycerides. Higher PM2.5 and NO2 "
     "were associated with more walking for transport, setting up opposing pathways via physical activity. Coefficients "
     "are not reported in the abstract. Limitation: cross-sectional, so walking cannot be ordered between exposure and "
     "outcome, as the authors state; Australian PM2.5 contrasts are narrow (single-digit ug/m3) and track urbanity, which "
     "drives both walkability and pollution. Relevance: low-medium - co-located PM and mobility data would let LCS "
     "studies separate these pathways.")),
 dict(pmid="42929017", doi="10.22074/ijfs.2026.2072188.1959", journal="Int J Fertil Steril",
  short="Ai air pollution IVF outcomes Chengdu retrospective cohort 2026",
  title="Association between Ambient Air Pollution Exposure and Reproductive Outcomes following In Vitro Fertilization: A Retrospective Cohort Study",
  sub=corpus.REPR, design="Retrospective cohort", pm="CHAP 1 km PM2.5, PM10, O3, NO2 at residence by IVF stage",
  geo="China (Chengdu)", endpoint="Biochemical pregnancy, clinical pregnancy, live birth after fresh embryo transfer", tier="B",
  n=("12,453 women with fresh embryo transfer at one Chengdu centre, 2019-2022; exposure windows defined around oocyte "
     "retrieval and transfer; GLMs adjusted for clinical, sociodemographic and paternal factors. Exposure in the 85 days "
     "before oocyte retrieval (folliculogenesis window) was associated with lower odds of biochemical pregnancy, clinical "
     "pregnancy and live birth; live birth OR 0.969 (0.954-0.984) per 10 ug/m3 PM2.5. Limitation: four pollutants over several "
     "overlapping windows from 4 years of gridded data raise multiplicity, and in a single-city clinic cohort the exposure "
     "contrast is mostly temporal, confounded by season and protocol changes (including COVID-era disruption). Relevance: "
     "low.")),
 dict(pmid="42930928", doi="10.1093/ajrccm/aamag575", journal="Am J Respir Crit Care Med",
  short="Zhou preoperative short-term PM2.5 postoperative pulmonary complications lung cancer surgery 2026",
  title="Preoperative short-term PM2.5 Exposure and Postoperative Pulmonary Complications After Lung Cancer Surgery",
  sub=corpus.RESP, design="Retrospective cohort", pm="Short-term preoperative PM2.5 (metadata only)",
  geo="China", endpoint="Postoperative pulmonary complications after lung cancer resection", tier="B",
  n=("Metadata only: the record (AJRCCM research letter) carried no abstract at PubMed, Crossref or Semantic Scholar on "
     "the issue date. The title reports an association of short-term PM2.5 exposure before surgery with postoperative "
     "pulmonary complications after lung cancer resection; design, n and effect size are not available here and are not "
     "inferred. Limitation (structural): preoperative exposure windows are short, so day-of-week and seasonal surgical "
     "scheduling and hospital load are the confounders any such analysis has to defeat. Relevance: medium - a "
     "perioperative window is one where short-horizon PM forecasts could change clinical scheduling. Retry the abstract "
     "before the weekly.")),
 dict(pmid="42932945", doi="10.1152/ajpcell.00103.2026", journal="Am J Physiol Cell Physiol",
  short="Chen PM2.5 mitochondria-associated membranes mouse liver 2026",
  title="Exposure to airborne PM2.5 suppresses mitochondrial associated membranes and MAM-associated metabolic regulators in mouse liver",
  sub=corpus.MECH, design="Animal exposure study + in vitro receptor overexpression", pm="Concentrated ambient PM2.5 inhalation (mouse); PM2.5 particles on hepatocytes/macrophages",
  geo="USA (laboratory)", endpoint="Hepatic MAM abundance, UPRmt and fatty-acid oxidation programs (CREBH/PPARalpha)", tier="B",
  n=("Mice inhaling environmentally relevant PM2.5 showed fewer mitochondria-associated membranes and fewer MAM-forming "
     "mitochondria in liver (TEM). In hepatocytes, PM2.5 suppressed basal and glucagon-induced MAM formation (BiFC sensor); "
     "macrophage particle uptake was blocked by antioxidants or calcium chelation. Mechanism: repression of CREBH/PPARalpha "
     "programs for the mitochondrial unfolded protein response and fatty-acid oxidation. Limitation: in vitro particle "
     "doses and the inhaled dose to liver are not reconciled, and the translocation route (systemic particles vs "
     "lung-derived mediators) is assumed rather than shown. Sample sizes are not in the abstract. Relevance: low - "
     "mechanism for PM-metabolic associations.")),
]
