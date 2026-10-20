# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.20944/preprints202610.1533.v1", journal="Preprints.org (preprint)",
  short="Qian MAG-MISD probabilistic multi-station PM2.5 forecasting 2026",
  title="MAG-MISD: A Mode-Specific Adaptive Graph Framework for Multiscale Interaction and Station Dependence in Probabilistic PM2.5 Forecasting",
  sub=corpus.SENS, design="Deep-learning forecasting", pm="Hourly station PM2.5, 127 Yangtze River Delta monitors, 8 years",
  geo="China (Yangtze River Delta)", endpoint="Not applicable (forecasting)", tier="B",
  n=("Variational mode decomposition into five components, cross-mode Transformer per station, and a separate directed "
     "graph per mode (geographic, persistent adaptive and sample-conditioned dynamic edges) before fusion into "
     "conditional quantiles. Against the same-input VMD-iTransformer, RMSE fell 4.76%, 2.78%, 0.13% and 0.72% at 1, 6, "
     "12 and 24 h, with better pinball loss and interval score and ~70% fewer parameters; the persistent adaptive "
     "relation drove most of the gain in ablation. Limitation: the improvement vanishes beyond 6 h, and decomposition "
     "of the full series before splitting risks leakage unless done causally - the abstract does not say. Relevance: "
     "moderate - station-graph forecasting transfers to LCS networks, where per-mode dependence could also flag "
     "drifting nodes.")),
 dict(pmid="", doi="10.20944/preprints202610.1559.v1", journal="Preprints.org (preprint)",
  short="Ghazaryan explainable ML annual PM2.5 Europe Central Asia 2026",
  title="Explainable Machine Learning for PM2.5 Prediction and Comparative Country-Level Risk Assessment in Europe and Central Asia",
  sub=corpus.EXPO, design="Machine-learning model", pm="Annual city PM2.5 vs climatic and socio-economic indicators",
  geo="Europe and Central Asia (10 cities)", endpoint="Not applicable (prediction)", tier="C",
  n=("Fifty-nine country-year observations (ten cities, 2020-2025) with eleven predictors; six models under five-fold "
     "CV. Linear regression had the lowest RMSE and highest R2, Extra Trees the lowest MAE; SHAP attributed added "
     "information to development indicators beyond meteorology. The authors call the result exploratory. Limitation: "
     "59 observations and 11 predictors with random-fold CV on autocorrelated city panels cannot support model "
     "ranking or attribution; numeric skill is not reported in the abstract. Relevance: low - illustrates why annual "
     "aggregate predictors are no substitute for measured spatial coverage.")),
 dict(pmid="", doi="10.1016/j.envint.2026.110570", journal="Environ Int",
  short="Dahl air pollution bone fractures high-risk population 2026",
  title="Air pollution and bone fractures in a high-risk population: differences by age and sex",
  sub=corpus.OTHR, design="Metadata only (no abstract)", pm="Ambient air pollution (metric not stated in record)",
  geo="Not stated in record", endpoint="Bone fractures", tier="C",
  n=("No abstract at harvest. The title indicates an analysis of ambient air pollution and fracture risk in a population "
     "at high fracture risk, stratified by age and sex. Recorded for coverage; no exposure model, design or estimate is "
     "inferred. Relevance: low-moderate - fracture is an under-studied PM endpoint, and bone-health associations have "
     "so far rested on residential annual means.")),
]
