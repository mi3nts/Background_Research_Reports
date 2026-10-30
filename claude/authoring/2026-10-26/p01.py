# -*- coding: utf-8 -*-
P = [
 dict(pmid="42931781", doi="10.1001/jamapediatrics.2026.5045", journal="JAMA Pediatr",
  short="Papatheodorou prenatal wildfire PM2.5 ASD ADHD Medicaid 2026",
  title="Prenatal Exposure to Wildfire PM2.5 and Risk of ASD and ADHD in Children Enrolled in Medicaid",
  sub=corpus.NEU, design="Retrospective cohort + DLNM", pm="Weekly wildfire-smoke-attributable PM2.5 (1 km), aggregated to residential ZIP code across pregnancy",
  geo="USA (nationwide Medicaid, 2007-2014)", endpoint="Incident ASD and ADHD (validated claims algorithms)", tier="A",
  n=("Nationwide Medicaid (MAX) cohort of 893,212 mother-child pairs with stable ZIP code in pregnancy; 8,357 ASD and 22,302 "
     "ADHD diagnoses (cumulative incidence to age 8: 1.9% and 10.4%). Cox models with distributed-lag nonlinear terms. Per IQR "
     "(0.75 ug/m3) of cumulative smoke PM2.5: ASD HR 1.30 (1.07-1.59); ADHD HR 1.03 (0.91-1.17). The ASD window sat in mid "
     "to late gestation. Limitation: a 30% hazard increase per 0.75 ug/m3 is very steep for a ZIP-level smoke fraction; "
     "smoke years and regions coincide with secular and regional shifts in ASD claims coding, and claims-based diagnosis in "
     "Medicaid depends on service access. Relevance: high - smoke-specific PM at sub-ug/m3 contrasts is exactly where "
     "dense sensor networks add resolution over 1 km model fields.")),
 dict(pmid="42933820", doi="10.1136/bmjresp-2025-003297", journal="BMJ Open Respir Res",
  short="Pedersen early-life air pollution lung function COPSAC 2026",
  title="Impact of air pollution exposure in early life on lung function development in the COPSAC cohorts",
  sub=corpus.RESP, design="Prospective birth cohort", pm="Modelled multi-source PM2.5 and NO2 at home address (DEHM/UBM/AirGIS-type chain)",
  geo="Denmark (COPSAC2000 and COPSAC2010)", endpoint="FEV1 and specific airway resistance (spirometry, plethysmography) age 3-18", tier="A",
  n=("Two Copenhagen birth cohorts (n=846) with repeated spirometry and plethysmography from age 3 to 18 years; linear "
     "mixed models. Per IQR (2.2 ug/m3) of postnatal PM2.5: FEV1 at age 6 -2.70% (-4.27 to -1.10) and specific airway "
     "resistance +7.30% (1.87-13.07). The deficit and the resistance increase persisted in growth trajectories through "
     "childhood, stronger in males. Limitation: COPSAC is an asthma-enriched cohort (COPSAC2000 enrolled children of "
     "asthmatic mothers), so effect sizes may not transfer to the general population; a 2.2 ug/m3 IQR in Copenhagen is "
     "small and partly a proxy for urban residence. Relevance: medium - effects at very low contrast argue for "
     "address-level precision rather than municipal means.")),
 dict(pmid="42927184", doi="10.1016/j.isci.2026.117904", journal="iScience",
  short="Zhou short-term indoor PM2.5 cognition HRV randomized crossover 2026",
  title="Short-term indoor fine particulate matter exposure impedes cognitive performance and autonomic nervous system in adults",
  sub=corpus.NEU, design="Randomised crossover trial", pm="Candle-generated indoor PM2.5, 1.70 vs 31.22 ug/m3 (purifier vs sham filter)",
  geo="UK (laboratory)", endpoint="Cognitive tests (attention, memory, coordination, reasoning); HRV; electrodermal activity", tier="A",
  n=("Randomised single-blind crossover in 90 working-age adults, two stable chamber conditions set by an air purifier with "
     "real or sham filter: 1.70 vs 31.22 ug/m3 PM2.5 from candle burning. The high condition lowered heart rate "
     "variability and attention and memory scores, but not coordination or reasoning; reduced HRV partly mediated some "
     "cognitive declines. Effect sizes with CIs are not given in the abstract. Limitation: candle smoke carries VOCs, CO, "
     "odour and visible haze, so blinding and the PM-specific attribution are both weak; multiple cognitive domains invite "
     "selective significance. Relevance: medium - controlled indoor steps of this size are what consumer PM monitors can "
     "verify in occupied rooms.")),
 dict(pmid="42928613", doi="10.1093/jncics/pkag116", journal="JNCI Cancer Spectr",
  short="Hoang PM2.5 minimal residual disease childhood ALL REDIAL 2026",
  title="Fine particulate matter and minimal residual disease in childhood acute lymphoblastic leukemia from the REDIAL consortium",
  sub=corpus.OTHR, design="Retrospective cohort", pm="CDC daily census-tract PM2.5 during induction (residence; centre then residence)",
  geo="USA (REDIAL consortium, Texas-led)", endpoint="Positive end-of-induction MRD (>=0.1% or >=0.01%)", tier="A",
  n=("2,125 children with ALL; mean daily residential PM2.5 during induction in quartiles; logistic regression. In B-ALL, "
     "positive end-of-induction MRD: Q2 aOR 1.56 (1.08-2.24), Q3 1.51 (1.05-2.17), Q4 1.19 (n.s.). Restricted to NCI "
     "high-risk B-ALL, aORs rose to 1.73-2.28 across Q2-Q4. Limitation: a non-monotone quartile pattern with the top "
     "quartile null is not a dose-response; census-tract PM2.5 over a ~4-week induction is tightly tied to treatment centre "
     "and ethnicity, which REDIAL was built to study and which also predicts MRD. Relevance: low-medium - induction-window "
     "exposure is short enough that a home monitor would be the right instrument.")),
]
