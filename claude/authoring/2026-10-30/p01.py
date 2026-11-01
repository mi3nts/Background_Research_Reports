# -*- coding: utf-8 -*-
P = [
 dict(pmid="42962723", doi="10.1016/j.jad.2026.122663", journal="J Affect Disord",
  short="Yang heat anomaly wildfire smoke PM2.5 incident depression All of Us 2026",
  title="Heat anomaly, wildfire smoke, social-material vulnerability, and incident depression in a national EHR-linked cohort: A preregistered secondary analysis",
  sub=corpus.NEU, design="Prospective cohort (registry linkage)", pm="30-day mean wildfire-smoke PM2.5 (Stanford ECHO model) at ZIP3",
  geo="USA (national, All of Us)", endpoint="First EHR-recorded depression diagnosis", tier="A",
  n=("Preregistered Cox analysis in All of Us: 179,218 adults free of recorded depression, 5,484 incident cases over a mean "
     "371 days. Exposures were the 30-day pre-index PRISM maximum-temperature anomaly, Stanford ECHO smoke PM2.5 and a "
     "social-material vulnerability (SMV) composite. Heat anomaly: HR 1.06 (1.03-1.10) and 1.08 (1.04-1.11) per SD; SMV: "
     "HR 1.36 (1.33-1.40) per SD. Mean smoke PM2.5 showed no association in the primary model; secondary smoke metrics "
     "were heterogeneous by metric and follow-up window. Limitation: exposure is assigned at the 3-digit ZIP level and "
     "frozen at baseline, so smoke-episode contrast is heavily smoothed and a null is weak evidence of no effect; "
     "EHR ascertainment depends on care access. Relevance: high - this is the misclassification problem that "
     "residence-scale sensor-corrected smoke PM2.5 exists to fix.")),
 dict(pmid="42959234", doi="10.3389/fped.2026.1941575", journal="Front Pediatr",
  short="Lin prenatal air pollution transient tachypnea newborn Taiwan 2026",
  title="Prenatal air pollution exposure and the risk of transient tachypnea of the newborn",
  sub=corpus.REPR, design="Case-cohort study", pm="40-week prenatal PM2.5, CO, NOx from nearest of 71 monitoring stations (postal code)",
  geo="Taiwan (national)", endpoint="Transient tachypnea of the newborn (TTN)", tier="B",
  n=("Nationwide matched design on the Taiwan NHIRD linked to the Maternal and Child Health Database, 2004-2020: 3,091 TTN "
     "cases in first-born infants and 12,364 controls (1:4 on maternal age, sex, birth date). Exposure over the 40 weeks "
     "before birth from the nearest of 71 stations to the residential postal code. Adjusted ORs: CO 1.806 (1.312-2.487), "
     "NOx 1.010 (1.005-1.015), PM2.5 1.001 (1.000-1.002), the last per unit concentration with a CI touching the null. "
     "Effects concentrated in the Taipei basin. Limitation: nearest-station assignment at postal-code scale, no "
     "multipollutant model reported, and the PM2.5 signal is marginal while CO dominates, pointing to traffic as a "
     "mixture rather than PM. Relevance: medium - traffic-gradient exposure in a dense basin is where street-level "
     "sensor networks change exposure contrast.")),
 dict(pmid="42959478", doi="10.1093/eep/dvag034", journal="Environ Epigenet",
  short="Gaylord DNA methylation signature prenatal air pollution ECHO cohort 2026",
  title="A methodology to identify a DNA methylation-based signature of prenatal air pollution exposure in the ECHO Cohort",
  sub=corpus.REPR, design="Cross-sectional (birth cohort)", pm="Prenatal PM2.5, NO2, 8-h max O3 from geocoded ML exposure models",
  geo="USA (multi-site ECHO cohorts)", endpoint="Cord-blood DNA methylation classifier of high vs low exposure (AUC)", tier="B",
  n=("Refines a pipeline that predicts high versus low in-utero air-pollution exposure from cord-blood DNA methylation "
     "(450K/EPIC) across multiple ECHO pregnancy cohorts. Exposures were ML-modelled at geocoded addresses; training and "
     "validation sets were matched on exposure level, site and array. Validation AUCs: PM2.5 0.64-0.68, NO2 0.62-0.95, "
     "O3 0.50-0.75, varying with region, exposure window and the high/low threshold. Limitation: the target is itself a "
     "model output, so the epigenetic classifier inherits exposure-model error, and PM2.5 discrimination is modest; "
     "dichotomisation discards dose information. Relevance: medium - a biomarker of cumulative exposure is only as good "
     "as the exposure surface it is trained on, which is where denser monitoring would raise the ceiling.")),
 dict(pmid="", doi="10.64898/2026.10.27.26366640", journal="medRxiv",
  short="Perez-Garcia nasal EWAS respiratory biomarkers Mexican American CHAMACOS 2026",
  title="Nasal Epigenome-Wide Association Study of Respiratory and Allergic Biomarkers in Mexican American Young Adults",
  sub=corpus.RESP, design="Cross-sectional (cohort baseline)", pm="Prenatal and past-year PM2.5 and O3 (residential)",
  geo="USA (Salinas Valley, California, CHAMACOS; Project Viva replication)", endpoint="Nasal DNA methylation vs FeNO, asthma, allergic sensitisation, FEV1/FVC", tier="B",
  n=("Preprint. Nasal EWAS (EPICv2, 804,220 CpGs) in 354 CHAMACOS young adults aged 22, replicated in 540 Project Viva "
     "adolescents aged 13. Forty-nine CpGs were associated with FeNO and 557 DMRs with respiratory outcomes (FDR<0.05); "
     "26 CpGs and 103 DMRs replicated (e.g. LRRFIP1, EPX, IL13). Ten FeNO-related CpGs were associated with prenatal "
     "and/or past-year PM2.5 or O3 at nominal p<0.05 only. Limitation: the air-pollution step is a secondary look-up "
     "without multiple-testing control, so the PM2.5 link is hypothesis-generating; cross-sectional nasal sampling "
     "cannot order exposure and methylation. Relevance: low-medium - an agricultural-valley cohort where PM sources are "
     "local and poorly served by regulatory monitors.")),
]
