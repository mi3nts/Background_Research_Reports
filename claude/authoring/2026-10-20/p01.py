# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1021/acs.est.6c04677", journal="Environ Sci Technol",
  short="Wen landscape fire PM2.5 renal hospitalisations six-country time-series 2026",
  title="Landscape Fire-Sourced PM2.5 and Cause-Specific Renal Hospitalizations: A Multicountry Two-Stage Time-Series Analysis of 12.5 Million Admissions",
  sub=corpus.OTHR, design="Multi-location time-series", pm="Landscape-fire-sourced vs non-fire PM2.5 (per 10 ug/m3, lag 0-5)",
  geo="Multi-country (Australia, Brazil, Canada, Chile, New Zealand, Thailand)", endpoint="Cause-specific renal hospitalisation (AKI strongest)", tier="A",
  n=("12.5 million renal admissions across 1020 locations in six countries, 2000-2019; two-stage time-series with "
     "fire-sourced PM2.5 separated from the non-fire remainder. Per 10 ug/m3 cumulative lag 0-5, RR 1.011 "
     "(1.007-1.015) for all renal admissions, strongest for acute kidney injury; associations larger for fire-sourced "
     "than non-fire PM2.5, larger in warmer areas and graded by GDP per capita. Attributable burden 1.38 admissions per "
     "100,000 per year. Limitation: the fire/non-fire split comes from a chemical-transport-plus-ML partition, not "
     "measured tracers, so 'fire PM is more toxic' partly inherits the partition's error structure; heat co-occurs with "
     "smoke and dehydration drives AKI, and residual confounding by temperature is the obvious threat. Relevance: "
     "moderate - smoke-episode exposure is where LCS density most improves over sparse FRM/FEM coverage.")),
 dict(pmid="42897330", doi="10.1007/s00431-026-07527-9", journal="Eur J Pediatr",
  short="Huang PM2.5 coronary artery dilatation Kawasaki disease case-crossover 2026",
  title="Association between PM(2.5) and coronary artery dilatation with Kawasaki disease in China",
  sub=corpus.CVM, design="Case-crossover", pm="Short-term PM2.5 (distributed lag 0-7 d)",
  geo="China (single paediatric centre)", endpoint="Coronary artery dilatation (Z score) in Kawasaki disease", tier="B",
  n=("847 children with Kawasaki disease, 2017-2021; case-crossover with a distributed-lag Poisson GLM on coronary "
     "Z score. Risk of coronary artery dilatation rose at lags 2-4, peaking at lag 3 with RR 1.11 (1.02-1.21); the "
     "abstract does not state the PM2.5 increment. Mediation via CRP, ALT and haemoglobin. Limitation: a "
     "case-crossover needs an acute event with a datable onset, yet CAD is detected at echocardiography whose timing "
     "follows admission and IVIG, so the referent-window logic is shaky; the 'mediators' are markers of disease "
     "severity measured after onset, and the highlights' claim of a 'population-based cohort' contradicts the design. "
     "Relevance: low - city-monitor assignment, no sensing implication.")),
 dict(pmid="42901555", doi="10.1136/bmjopen-2026-120476", journal="BMJ Open",
  short="Wongcharoen short-term PM2.5 MACE high-risk population nationwide case-crossover 2026",
  title="Associations between short-term PM(2.5) exposure and major cardiovascular events in high-risk population: a nationwide case-crossover study",
  sub=corpus.CVM, design="Metadata only (no abstract)", pm="Short-term PM2.5",
  geo="Thailand (inferred from author group; not stated in record)", endpoint="Major adverse cardiovascular events", tier="C",
  n=("Title and authors only (Wongcharoen et al.); no abstract indexed at harvest. A nationwide time-stratified case-crossover of short-term PM2.5 and "
     "major adverse cardiovascular events restricted to a 'high-risk population' (presumably prior CVD, diabetes or "
     "hypertension). Country, n, lag structure and effect size cannot be stated. Limitation: unverifiable beyond the "
     "title; case-crossover in a pre-selected high-risk group estimates a conditional acute effect that is not "
     "comparable with general-population estimates. Relevance: low-moderate - short-lag acute effects are what "
     "real-time LCS alerts are meant to act on.")),
 dict(pmid="42897393", doi="10.1007/s10903-026-02022-7", journal="J Immigr Minor Health",
  short="Morales El Paso port-of-entry PM2.5 immigration COPD census tracts 2026",
  title="Breathing at the Border: PM2.5 Exposure, Immigration, and COPD Across Census Tracts Close to Ports-of-Entry",
  sub=corpus.RESP, design="Ecological / registry analysis", pm="Census-tract PM2.5 (NASA satellite-derived)",
  geo="USA (El Paso, Texas, US-Mexico border)", endpoint="Tract-level COPD prevalence (CDC PLACES)", tier="B",
  n=("El Paso census tracts; NASA satellite-derived PM2.5 merged with CDC tract COPD prevalence and ACS social "
     "vulnerability; GLMs with distance to the port-of-entry. PM2.5 and percent foreign-born non-citizens were "
     "positively associated with COPD prevalence; tracts within three miles of a port had higher prevalence, and the "
     "PM2.5 effect was stratified by proximity. No coefficients or CIs in the abstract. Limitation: CDC PLACES "
     "prevalence is itself small-area modelled from BRFSS demographics, so regressing it on demographic covariates is "
     "partly circular; smoking is not addressed; satellite PM2.5 at ~1 km cannot resolve truck-idling gradients at "
     "bridge queues. Relevance: high - port-of-entry diesel queues are a textbook case for dense LCS siting.")),
]
