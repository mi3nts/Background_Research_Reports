# -*- coding: utf-8 -*-
P = [
 dict(pmid="42959475", doi="10.3389/fpubh.2026.1987084", journal="Front Public Health",
  short="Wang climate-adaptive city pilot PM2.5 health dividend China 2026",
  title="Does climate adaptation policy deliver a health dividend? Exposure, modeled health burden, and defensive capacity in China's climate-adaptive city pilots",
  sub=corpus.BURD, design="Difference-in-differences evaluation", pm="City-level annual PM2.5 (gridded product), GEMM burden",
  geo="China (264 cities)", endpoint="PM2.5 change; GEMM-modelled pollution burden; health-system capacity", tier="B",
  n=("Difference-in-differences on a 2011-2022 panel of 264 prefecture cities, 21 treated by China's 2017 climate-adaptive "
     "city pilot. The pilot is associated with PM2.5 lower by 3.87 ug/m3 (95% CI -6.49 to -1.25; wild-bootstrap p=0.0067); "
     "GEMM translates this into an ~8.1% lower modelled burden (-11.32 to -4.76%) - an accounting result, not observed "
     "mortality. Defensive-capacity responses (physicians, beds, insurance) are imprecise. Limitation: the estimate "
     "shrinks and loses precision in the matched sample and after pollution-convergence adjustment, so selection of "
     "already-improving cities is not excluded; 21 treated units is a small base. Relevance: low-medium - policy "
     "evaluation at city scale rests on gridded PM2.5 whose own error is not propagated.")),
 dict(pmid="42958199", doi="10.1186/s12889-026-28148-9", journal="BMC Public Health",
  short="Musa outdoor air pollution cardiovascular health school children Dar es Salaam 2026",
  title="Effects of outdoor air pollution on the cardiovascular health of school-aged children residing near polluted areas and the efficacy of mitigation measures in Dar es Salaam, Tanzania",
  sub=corpus.CVM, design="Cross-sectional survey", pm="None measured; residence near industry, major roads or waste burning used as proxy",
  geo="Tanzania (Dar es Salaam)", endpoint="Elevated blood pressure and cardiovascular symptoms", tier="C",
  n=("Community cross-sectional study, December 2024-July 2025, of 653 school-aged children living in areas classed as "
     "highly polluted by proximity to industrial zones, major roads and waste-burning sites. Single oscillometric BP "
     "reading; 19.9% had elevated BP. In log-binomial models, prior respiratory disease carried ARR 8.81 (6.12-12.67) for "
     "cardiovascular symptoms. Awareness of mitigation policy was mixed. Limitation: no pollutant was measured and there "
     "is no unexposed comparison group, so the title's causal framing is not supported; one-visit BP overstates "
     "prevalence in children. Relevance: high as a gap marker - urban East Africa has almost no PM monitoring, and this "
     "design shows what health studies look like without it.")),
 dict(pmid="42960997", doi="10.13075/ijomeh.1896.02875", journal="Int J Occup Med Environ Health",
  short="Kobza respiratory ambulatory care air quality Upper Silesia 2026",
  title="The assessment of respiratory diseases in ambulatory care attributable to air quality in the Upper Silesian agglomeration",
  sub=corpus.RESP, design="Ecological", pm="Daily PM2.5, PM10, SO2, NOx, Pb, benzene from ~50 regional stations",
  geo="Poland (Upper Silesia)", endpoint="Outpatient incidence of pharyngitis, tonsillitis, laryngotracheitis, pneumonia, bronchitis, asthma", tier="C",
  n=("Five-year ecological analysis correlating daily mean concentrations from about 50 monitoring stations with National "
     "Health Fund outpatient incidence for seven respiratory ICD codes across eight regions of the Upper Silesian "
     "voivodeship. The strongest signal was for SO2, not PM: tau 0.99 and rho 0.9 in regions 7 and 8, rho 0.78 in regions "
     "1 and 4. Limitation: rank correlations on aggregated series without control for season, influenza, temperature or "
     "autocorrelation - seasonality alone would generate these coefficients, so the results carry no causal or "
     "PM-specific information. Relevance: low - included because PM2.5/PM10 were analysed; the coal-heating region is a "
     "classic case where denser residential PM sensing would sharpen exposure contrast.")),
 dict(pmid="42960269", doi="10.1016/j.mex.2026.104217", journal="MethodsX",
  short="Waghmare machine learning explainable AI PM2.5 prediction Nagpur 2026",
  title="Machine learning models with explainable AI for PM2.5 prediction for Urban air quality assessment",
  sub=corpus.SENS, design="Gradient-boosting model + SHAP interpretability", pm="Station PM2.5 with co-pollutants and meteorology",
  geo="India (Nagpur, Maharashtra)", endpoint="PM2.5 prediction skill (R2, RMSE, MAE, MAPE)", tier="C",
  n=("Six regressors (decision tree, extra trees, random forest, KNN, XGBoost, SVR) trained on ~4,000 observations of "
     "PM2.5, NO2, SO2, NH3, O3 and meteorology in Nagpur, 70/30 split with 10-fold CV. A single decision tree scored best: "
     "test R2 0.90, RMSE 7.5-8.9 ug/m3, MAE 5.4-6.6 ug/m3; SHAP ranked NO2, O3, RH and NH3 top. Limitation: random splits "
     "of autocorrelated time series leak information, so skill is inflated; co-pollutants measured at the same station "
     "make this a nowcast, not a forecast, and a lone tree beating ensembles is a warning sign. Relevance: low-medium - "
     "illustrates the validation discipline (blocked or spatial CV) that sensor-network ML calibration needs.")),
]
