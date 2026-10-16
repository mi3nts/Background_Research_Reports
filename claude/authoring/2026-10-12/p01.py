# -*- coding: utf-8 -*-
P = [
 dict(pmid="42863479", doi="10.1016/j.lanplh.2026.101526", journal="Lancet Planet Health",
  short="Yu multicountry PM2.5 admissions 2026",
  title="Cause-specific hospital admissions associated with short-term PM2.5 exposure: a multicountry time-series analysis",
  sub=corpus.BURD, design="Multi-location time-series", pm="Daily ambient PM2.5 (community-level), lags to 21 days",
  geo="Multi-country (Australia, Brazil, Canada, Chile, New Zealand, Taiwan)", endpoint="Cause-specific hospital admissions", tier="A",
  n=("346.5 million admissions from 949 communities in six countries/territories, 2000-2019; quasi-Poisson "
     "time series pooled by meta-analysis. Per 10 ug/m3, all-cause admissions RR 1.080 (1.074-1.086), with effects "
     "persisting to 21 days. Malignant neoplasms (1.108, 1.094-1.123), mental disorders (1.100) and nervous system "
     "disease (1.085) all exceed respiratory (1.067, 1.060-1.074). Attributable fraction against the WHO daily 15 "
     "ug/m3 fell from 8.9% (2000-09) to 3.9% (2010-19). Limitation: a 21-day distributed lag on cancer admissions "
     "invites harvesting and scheduling artefacts - an elective oncology admission is not an acute PM event - and "
     "heterogeneity across countries is described as substantial but the pooled RR is reported without it. "
     "Relevance: high - the long-lag, non-respiratory signal argues for continuous rather than episodic sensing.")),
 dict(pmid="", doi="10.64898/2026.10.08.26364863", journal="medRxiv (preprint)",
  short="Jin wildfire carbonaceous ADRD 2026",
  title="Carbonaceous Components Underlying Wildfire Smoke PM2.5-Associated Alzheimer's Disease and Related Dementias in Older US Adults",
  sub=corpus.NEU, design="Retrospective cohort", pm="Annual smoke vs non-smoke PM2.5 and smoke EC/OC (high-resolution model)",
  geo="United States (Medicare, nationwide)", endpoint="Incident AD and ADRD", tier="A",
  n=("39.7 million fee-for-service Medicare beneficiaries, 2005-2019, 8.4 million incident ADRD cases; stratified Cox. "
     "Per 1 ug/m3, smoke PM2.5 HR 1.029 (1.024-1.035) for ADRD and 1.015 (1.005-1.026) for AD; the smoke carbonaceous "
     "fraction HR 1.090 (1.077-1.103) for ADRD. Per IQR the non-smoke association is larger (ADRD 1.048 vs 1.009) because "
     "smoke exposure contrast is narrow. Attributable: 11,142 ADRD cases/year. Limitation: preprint; annual smoke "
     "partitioning is model-derived and its error is not propagated, and claims-based incident dementia carries "
     "diagnostic-intensity confounding that tracks rurality and fire-prone regions. Relevance: high - argues for "
     "composition-resolved smoke metrics that optical LCS cannot supply without co-located carbon measurement.")),
 dict(pmid="42860804", doi="10.1080/09603123.2026.2745894", journal="Int J Environ Health Res",
  short="Chen Lanzhou PM2.5 components CVD 2026",
  title="Acute cardiovascular mortality risks from PM2.5 and its chemical components in an industrial valley city: evidence from Lanzhou, China",
  sub=corpus.CVM, design="Time-series (GAM) with mixture models", pm="Daily PM2.5; random-forest-predicted components (PAHs, metals, ions)",
  geo="China (Lanzhou)", endpoint="Cardiovascular mortality", tier="B",
  n=("69,669 CVD deaths, 2015-2023. PM2.5 lag 0: excess risk 2.06% per 10 ug/m3 (0.66-3.48%), larger in men and under-65s. "
     "qgcomp/WQS attribute risk to PAHs and Tl/Pb/Mn in traffic-dominated Chengguan, and to nitrate/chloride/sulfate and "
     "PAHs in industrial Xigu. Limitation: components are not measured but predicted by a random forest with r>0.70, so "
     "the mixture weights inherit the predictor set of that model - district contrasts may reflect which inputs drove "
     "the prediction rather than toxicity. Relevance: moderate - a valley inversion city where source-specific nodes "
     "would test exactly these district contrasts.")),
 dict(pmid="", doi="10.21203/rs.3.rs-11301519/v1", journal="Research Square (preprint)",
  short="Kinzunga Kinshasa PM2.5 respiratory 2026",
  title="Acute Respiratory Impacts of Fine Particulate Matter (PM2.5) in Kinshasa: Epidemiological Evidence and Pulmonological Implications",
  sub=corpus.RESP, design="Time-stratified case-crossover", pm="Daily PM2.5 from PurpleAir and QuantAQ Modulair sensors plus bias-corrected GEOS-CF",
  geo="Democratic Republic of the Congo (Kinshasa)", endpoint="Adult respiratory emergency admissions", tier="B",
  n=("13,049 adult admissions at one hospital, 2018-2022; mean daily PM2.5 46-50 ug/m3. Per 10 ug/m3 over lag 0-5, "
     "adjusted OR 1.01 (1.00-1.03), strongest at 35-64 years and in Tshangu and Funa. Limitation: a single-hospital "
     "catchment against a city-wide exposure series, and an estimate whose lower bound sits on the null; the sensor "
     "and model fusion step is described but its validation against any reference in Kinshasa is not. Relevance: high - "
     "one of the first African health analyses whose exposure series is built on low-cost sensors, which makes the "
     "uncorrected sensor error the main threat to the inference.")),
]
