# -*- coding: utf-8 -*-
P = [
 dict(pmid="42990503", doi="10.21203/rs.3.rs-11167409/v1", journal="Res Sq",
  short="Bonilla California CMAQ wildfire PM2.5 evaluation 2008-2018 random forest diagnostic",
  title="Evaluating CMAQ Representation of Wildfire PM2.5 in California (2008-2018): Regime-Dependent Performance and Nonlinear Error Structure.",
  sub=corpus.EXPO, design="Chemical transport model evaluation",
  pm="Daily CMAQ total and fire-only PM2.5 paired with monitor observations, June-October", geo="USA",
  endpoint="Bias, RMSE, event detection at 12 and 35 ug/m3", tier="B",
  basis="Model (CTM / LUR / ML)", affil="",
  n=("Preprint. 187,051 paired site-days across California fire seasons 2008-2018 (18 CMAQ values above 557 ug/m3 quarantined). Observed and modelled means "
     "10.69 and 9.29 ug/m3; r 0.502, mean bias -1.40, RMSE 9.96 ug/m3. CMAQ detected 45.4% of observed site-days above 12 and 40.8% above 35 ug/m3, and at 35 "
     "it produced more events overall yet missed 1,273 of 2,151 observed ones because events did not coincide by site-day. A random forest using fire-only "
     "CMAQ PM2.5 among its predictors reached R2 0.711, RMSE 5.82 on a held-out site-year partition. The diagnostic does not apportion error to emissions, "
     "plume rise or meteorology. Relevance: direct - quantifies why model-only smoke exposure misclassifies acute days; sensor-network fusion is the fix.")),
 dict(pmid="42989327", doi="10.1186/s13148-026-02215-9", journal="Clin Epigenetics",
  short="Zhang SMR multi-omics PM2.5-annotated genes diabetic nephropathy TNF NOS2 methylation 2026",
  title="A multi-omics Mendelian randomization framework identifies PM2.5-annotated candidate regulatory genes and methylation-linked pathways in diabetic nephropathy.",
  sub=corpus.MECH, design="Two-sample Mendelian randomisation",
  pm="No exposure measurement; genes annotated as PM2.5-responsive from curated databases, plus in vitro PM2.5 exposure", geo="Global / multi-region",
  endpoint="Genetically predicted diabetic nephropathy susceptibility", tier="C",
  basis="Genetic / biomarker proxy", affil="Guang'anmen Hospital, China Academy of Chinese Medical Sciences, China; Guang'anmen Hospital, China Academy of Chinese Medical Sciences, China",
  n=("Summary-data MR integrating eQTL, pQTL and mQTL with diabetic nephropathy GWAS, restricted to a curated set of PM2.5-annotated genes. Ten genes (TNF, "
     "NOS2, DUSP1 among them) showed genetically predicted effects; colocalisation supported a shared variant only at EIF2AK3 (PP.H4 0.90). 48 CpGs in 28 "
     "genes associated with DN risk, TNF methylation strongest; cell PM2.5 exposure reproduced TNF/NOS2 up and DUSP1 down; a two-gene nomogram gave AUC "
     "0.766 (training) and 0.726 (external). The MR tests gene expression on DN, not PM2.5 on DN: the PM link is a database annotation, so the causal claim "
     "about pollution is not identified. Relevance: weak - no exposure measurement of any kind.")),
 dict(pmid="42989273", doi="10.1186/s12890-026-04696-z", journal="BMC Pulm Med",
  short="Alimu Kashi Xinjiang ExWAS elastic-net air pollution meteorology pulmonary tuberculosis 2026",
  title="Associations between air pollution, meteorology, and pulmonary tuberculosis risk in Kashi, China.",
  sub=corpus.RESP, design="Exposome-wide association",
  pm="Ambient PM10, PM2.5, NO2 and meteorology; source and averaging window not stated", geo="China",
  endpoint="Pulmonary tuberculosis versus hospital non-TB controls", tier="C",
  basis="Reference / regulatory monitor", affil="First People's Hospital of Kashi, China; First People's Hospital of Kashi, China",
  n=("TB cases from a surveillance platform compared with hospital non-TB controls in Kashi, Xinjiang, using ExWAS, adaptive elastic-net and XGBoost. "
     "Retained predictors: PM10 OR 1.013, PM2.5 OR 1.008, NO2 OR 1.018 (all p<0.0001), wind speed 0.983 and humidity 0.944; XGBoost ranked PM10 most "
     "important. No confidence intervals, increments, exposure windows or sample size are given in the abstract, and controls drawn from a hospital record "
     "system against cases from a separate platform build in selection bias; Kashi PM10 is dominated by Taklamakan dust, so PM10 also marks season and "
     "desert-dust episodes. Relevance: weak - a dust-dominated setting where PM10 sensors would be informative, but the design cannot carry a causal reading.")),
 dict(pmid="42988924", doi="10.1007/s00125-026-06908-x", journal="Diabetologia",
  short="Singh German Diabetes Study long-term PM2.5 clamp insulin sensitivity albuminuria T1D T2D 2026",
  title="Associations of long-term exposure to air pollution with glucose homeostasis biomarkers and diabetes-related comorbidities in people with recent-onset type 1 and type 2 diabetes.",
  sub=corpus.CVM, design="Cross-sectional (cohort baseline)",
  pm="Five-year mean PM2.5, PM10 and NO2 at residential address", geo="Germany",
  endpoint="HbA1c, clamp insulin sensitivity, C-peptide secretion, insulin clearance, VO2max, albuminuria, DSPN", tier="A",
  basis="Model (CTM / LUR / ML)", affil="German Diabetes Center, Heinrich Heine University Dusseldorf, Germany; German Diabetes Center, Germany",
  n=("Cross-sectional analysis of 1,120 German Diabetes Study participants with recent-onset diabetes (417 T1D, 703 T2D), gold-standard clamp phenotyping. "
     "Per IQR PM2.5: T1D HbA1c exp(b) 1.07 (1.03-1.11), albuminuria 1.72 (1.34-2.20), VO2max 0.94 (0.89-0.99); T2D HbA1c 1.04 (1.01-1.06), insulin "
     "sensitivity b -0.42 (-0.82 to -0.03), insulin clearance 0.92 (0.87-0.98), albuminuria 1.71 (1.41-2.08), DSPN OR 1.53 (1.02-2.32). Many outcomes are "
     "tested without stated multiplicity control, and a single-time-point design cannot order exposure and disease progression. The IQR value is not in "
     "the abstract. Relevance: indirect - deep phenotyping makes this a strong mechanistic anchor; exposure is modelled, not measured.")),
]
