# -*- coding: utf-8 -*-
P = [
 dict(pmid="42931658", doi="10.3390/toxics14100871", journal="Toxics",
  short="Zhao interpretable machine learning multi-window PM2.5 hypertension CHNS Beijing 2026",
  title="An Interpretable Machine Learning Framework Integrating Multi-Window Environmental Exposure for Hypertension Risk Assessment",
  sub=corpus.CVM, design="Gradient-boosting model + SHAP interpretability", pm="Cumulative PM2.5 over 0, 7, 15, 30 and 60 days",
  geo="China (Beijing, CHNS subsample)", endpoint="Prevalent hypertension (classification)", tier="C",
  n=("Five classifiers (GLM, Lasso, tree, RF, XGBoost) with SHAP and partial-dependence layers on 2,523 participant-visits "
     "from the CHNS Beijing subsample; person-level and year-based splits; BP excluded from predictors. Test AUC 0.69-0.77, "
     "Brier 0.17-0.23. The 60-day PM2.5 window was the top exposure feature and added ~0.02-0.03 AUC (p=0.03-0.05). "
     "Adjusted window-specific analyses showed inverse PM2.5-hypertension associations, stronger for longer windows. "
     "Limitation: a ~0.02 AUC gain at borderline p with inverse associations indicates that the PM2.5 windows act as "
     "calendar/season proxies, not causal exposure; feature importance is not effect estimation, and the CHNS visit spacing is irregular. Relevance: low.")),
 dict(pmid="42931070", doi="10.3390/jox16060184", journal="J Xenobiot",
  short="Chen PM2.5 mixtures Parkinson disease INPP5D SHIP1 PI3K-AKT multi-omics 2026",
  title="Neurotoxicity of PM2.5-Bound Multi-Pollutant Mixtures in Parkinson's Disease: Exploring the INPP5D/SHIP1-PI3K-AKT Axis via an Integrative Multi-Omics Study",
  sub=corpus.MECH, design="Mendelian randomisation + TWAS", pm="GWAS-instrumented PM2.5; NIST SRM 1648a urban PM in SH-SY5Y cells",
  geo="Not stated (public GWAS; laboratory)", endpoint="PD susceptibility; SHIP1/PI3K-AKT signalling, neuroinflammation, apoptosis", tier="C",
  n=("Two-sample MR on public GWAS suggested a positive genetic association of PM2.5 with PD; network toxicology intersected "
     "PM2.5-component targets, PD risk genes and differential transcripts (195 genes), and LASSO/RF picked INPP5D (SHIP1) as "
     "hub. Docking and SH-SY5Y experiments with SRM 1648a showed SHIP1 up-regulation, PI3K-AKT suppression, inflammation "
     "and apoptosis, rescued by INPP5D knockdown. Limitation: MR for an environmental exposure rests on GWAS of residential "
     "PM2.5, whose instruments mostly encode where people live (pleiotropy); docking affinities are not evidence. MR "
     "estimates are not reported in the abstract, nor is the SRM dose. Relevance: low.")),
 dict(pmid="42931077", doi="10.3390/jox16060191", journal="J Xenobiot",
  short="Al-Atram early-life air pollution child neurodevelopment critical review 2026",
  title="Early Life Ambient Air Pollution and Child Neurodevelopment: Critical Review of Cohort Evidence",
  sub=corpus.NEU, design="Critical review", pm="Prenatal and early-childhood PM2.5, PM10, NO2",
  geo="Global / multi-region", endpoint="Psychomotor, cognitive, behavioural outcomes; ASD/ADHD", tier="C",
  n=("Narrative critical review (purposive selection, PubMed through 30 Aug 2026) weighing null findings, exposure "
     "assessment, confounding and causal interpretation. European and US multicohort studies show small associations "
     "with selected outcomes alongside substantial nulls; Canadian and Korean cohorts show pollutant- and age-specific "
     "heterogeneity. Birth weight and prematurity require total vs conditional effect distinctions; placental and "
     "imaging data support plausibility but not mediation. The authors conclude the evidence does not make pollution a "
     "determinative cause of ASD or ADHD. Limitation: no protocol, duplicate screening or risk-of-bias scoring, so "
     "selection is the authors' own, and it predates today's Medicaid wildfire-ASD cohort. Relevance: low.")),
 dict(pmid="42931071", doi="10.3390/jox16060185", journal="J Xenobiot",
  short="Awasthi air pollution oxidative stress inflammation molecular mechanisms review 2026",
  title="Molecular Mechanisms Linking Air Pollution-Induced Oxidative Stress to Inflammation and Human Disease",
  sub=corpus.MECH, design="Mechanistic review", pm="PM, NOx, O3, SO2, VOCs (generic)",
  geo="Global / multi-region", endpoint="Oxidative stress, inflammation, multi-system disease", tier="C",
  n=("Broad review of ROS/RNS generation by PM, NOx, O3, SO2 and VOCs and downstream Nrf2, NF-kB and MAPK signalling, "
     "mitochondrial dysfunction, ER stress and epigenetic reprogramming, mapped to respiratory, cardiovascular, "
     "neurological, metabolic and carcinogenic outcomes; also covers biomarkers, susceptible windows and "
     "antioxidant-based interventions. No quantitative synthesis. Limitation: pollutants with very different chemistry are "
     "pooled under one oxidative-stress narrative, and in vitro dose relevance is not appraised; nothing here is new "
     "relative to the established mechanistic literature. Relevance: low - background for oxidative-potential (OP) "
     "metrics, which are the measurable bridge to sensing.")),
]
