# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.21203/rs.3.rs-11210953/v1", journal="Research Square",
  short="Angita Jhansi semi-arid campus automatic sensor PM2.5 PM10 annual cycle 2023",
  title="Year-Round Seasonal Variation of PM2.5 and PM10 at a Semi-Arid Institutional Campus Site in Jhansi, Uttar Pradesh, India",
  sub=corpus.SENS, design="Field measurement",
  pm="Continuous PM2.5 and PM10 from an automatic sensor, one campus site, 2023", geo="India",
  endpoint="Seasonal and annual mean PM2.5, PM10", tier="C",
  basis="Low-cost sensor / network", affil="",
  n=("Preprint. One automatic sensor at a semi-arid campus in Jhansi, Bundelkhand, January-December 2023. Post-monsoon means were highest (PM2.5 63.55, "
     "PM10 190.63 ug/m3, November peak), monsoon lowest (33.17 and 99.52); annual PM2.5 37.45 ug/m3, under the Indian NAAQS of 40 but 7.5 times the WHO "
     "guideline, and PM10 113.00 against a standard of 60. ANOVA on 12 monthly means: F(3,8) 4.66 and 4.83. The instrument is unnamed, with no co-location, "
     "humidity correction or data-capture statistics, so the monsoon minimum and the PM2.5 standard compliance both sit inside unquantified sensor "
     "error. Relevance: direct - a single uncalibrated sensor reported as a compliance assessment, exactly the use the low-cost field warns against.")),
 dict(pmid="", doi="10.21203/rs.3.rs-11616075/v1", journal="Research Square",
  short="Wu Heyuan attention-LSTM SHAP hourly PM2.5 O3 forecasting persistence 2019-2023",
  title="Baseline-relative predictability of hourly PM2.5 and O3 in a low-emission South Chinese city: an attention-LSTM with feature attribution",
  sub=corpus.SENS, design="Deep-learning forecasting",
  pm="Hourly PM2.5 and O3 from two urban monitoring stations, 2019-2023", geo="China",
  endpoint="Next-hour prediction R2 and RMSE; SHAP attribution", tier="C",
  basis="Reference / regulatory monitor", affil="",
  n=("Preprint. Attention-LSTM on hourly observations from two Heyuan stations, 2019-2023, interpreted with SHAP. Test R2 0.9796-0.9877 for PM2.5 and "
     "0.9921-0.9975 for O3, RMSE 1.28-2.02 and 1.77-2.83 ug/m3; the most recent pollutant observations dominated attributions, humidity and temperature "
     "contributed for O3. The authors themselves frame the result against persistence: at one-hour horizon a lag-1 baseline already achieves R2 near 0.95, "
     "and the abstract does not report the skill gain over it. Two stations in a low-emission city limit generality. Relevance: indirect - a useful "
     "cautionary example that high R2 in short-horizon PM forecasting mostly measures autocorrelation, relevant to edge-inference claims on sensor nodes.")),
 dict(pmid="", doi="10.64898/2026.11.02.26367044", journal="medRxiv",
  short="Madej Poland 379 counties spatial Mundlak GAM mortality inequality PM2.5 2010-2025",
  title="Place-based structural disadvantage and mortality inequality across 379 Polish counties, 2010-2025: a spatial Mundlak analysis",
  sub=corpus.BURD, design="Ecological panel",
  pm="County-level PM2.5 (source not stated in the abstract)", geo="Poland",
  endpoint="Age-sex-standardised all-cause mortality per 100,000", tier="B",
  basis="Not stated", affil="",
  n=("Preprint. 379 harmonised Polish counties, 2010-2025, spatial Mundlak GAMs separating between-county from within-county associations. Pre-COVID median "
     "between-county slope per SD: +30.2 deaths per 100,000 for PM2.5, against -26.1 for higher education and +29.4 for low education; these gradients "
     "persisted across windows, while within-county terms were unstable and sometimes reversed in pandemic-inclusive models. Leave-one-year-out validation "
     "showed weak temporal transportability, and the PM2.5 contribution contrast shrank after COVID-19. The between-county PM term is cross-sectional and "
     "collinear with Silesian coal-mining deprivation; no uncertainty on the slope is given in the abstract. Relevance: indirect - PM2.5 matches education "
     "in explaining Poland's mortality geography at ecological scale.")),
 dict(pmid="42989128", doi="10.1186/s12883-026-05212-w", journal="BMC Neurol",
  short="Huang UK Biobank CKD dementia multidomain risk factors air pollution null 2026",
  title="Disease susceptibility and risk of dementia in patients with chronic kidney disease: a prospective cohort study based on UK Biobank.",
  sub=corpus.NEU, design="Cohort",
  pm="UK Biobank residential air pollution estimates (LUR), one of many candidate factors", geo="UK",
  endpoint="Incident dementia", tier="C",
  basis="Model (CTM / LUR / ML)", affil="West China Hospital of Sichuan University, China; West China Hospital of Sichuan University, China",
  n=("16,083 UK Biobank participants with CKD followed 13.8 years; 806 incident dementias. Cox models with inverse probability weighting, competing-risk "
     "and FDR correction screened lifestyle, clinical, social, device-use, environmental and sensory factors. Hypertension, diabetes, depression, hearing "
     "loss and low social activity raised risk; moderate activity and computer use lowered it. Air pollution showed no nominally significant association. "
     "With 806 events spread over dozens of exposures and UK Biobank's 2010 single-year LUR surfaces, power for a PM effect of the expected size (HR "
     "~1.05-1.10 per few ug/m3) in a subgroup is low, so the null is uninformative rather than reassuring. Relevance: weak - a null by underpowered screening.")),
]
