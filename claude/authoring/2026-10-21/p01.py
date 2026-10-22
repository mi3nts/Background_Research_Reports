# -*- coding: utf-8 -*-
P = [
 dict(pmid="42903701", doi="10.1021/envhealth.5c00638", journal="Environ Health (ACS)",
  short="Zhu source-specific PM2.5 atrial fibrillation Medicare cohort 2026",
  title="Source-Specific PM2.5 Exposure and Atrial Fibrillation Risk in U.S. Older Adults: A Nationwide Cohort Study",
  sub=corpus.CVM, design="Retrospective cohort", pm="Source-apportioned PM2.5 (Multilinear Engine on CSN/IMPROVE speciation; IDW to ZIP code, 100 km)",
  geo="USA (nationwide Medicare)", endpoint="Incident atrial fibrillation", tier="A",
  n=("26.3 million Medicare beneficiaries, 2000-2019, 171.6 M person-years, 4.44 M incident AF. Per IQR of source-specific "
     "PM2.5: secondary sulfate HR 1.056 (1.053-1.058), heavy oil/coal combustion 1.048 (1.046-1.050), secondary nitrate "
     "1.032 (1.030-1.034), vehicle 1.029 (1.028-1.030); biomass burning and dust modest, SOA null overall but positive in "
     "the West. Limitation: source profiles come from sparse speciation monitors interpolated by inverse distance over "
     "100 km, so source contrasts are largely regional contrasts; sulfate and nitrate fields are smooth and the "
     "per-IQR scaling differs by source, so 'sulfate is most toxic' is not a per-microgram statement. Claims-based AF "
     "under-ascertains paroxysmal AF. Relevance: high - speciation, not mass, is what optical LCS cannot give; "
     "source-resolved risk raises the value of co-located filter or ACSM nodes.")),
 dict(pmid="42903813", doi="10.1021/envhealth.6c00011", journal="Environ Health (ACS)",
  short="Lin air pollution cervical cancer recurrence mortality Fudan cohort 2026",
  title="Long-Term Exposure to Ambient Air Pollution and Cervical Cancer Outcomes in Chinese Women: A Prospective Study on Recurrence and Mortality Risks",
  sub=corpus.OTHR, design="Prospective cohort", pm="Residential PM2.5 and PM10 from high-resolution spatiotemporal models (post-surgery)",
  geo="China (Shanghai, single hospital)", endpoint="Cervical cancer recurrence and all-cause death", tier="B",
  n=("3,758 women with primary cervical cancer (2019-2022), median follow-up ~3 y; 217 recurrences, 113 deaths. Per IQR "
     "PM2.5: recurrence SHR 1.93 (1.40-2.66, Fine-Gray), death HR 2.55 (1.78-3.67); PM10 SHR 1.65 (1.13-2.42) and HR "
     "2.21 (1.38-3.54); NO2 and SO2 also positive, O3 null. Limitation: hazard ratios near 2-2.5 per IQR from 113 deaths "
     "are implausibly large for a residential long-term contrast and point to confounding by referral geography - "
     "patients from outside Shanghai (higher PM) likely differ in stage, HPV management and follow-up intensity; "
     "single-centre, short follow-up, no adjustment for distance to the hospital reported in the abstract. "
     "Relevance: low - model-based residential exposure, no sensing implication.")),
 dict(pmid="42903834", doi="10.1021/envhealth.5c00676", journal="Environ Health (ACS)",
  short="Li size-specific PM lung function China Pulmonary Health Study 2026",
  title="Associations between Size-Specific Particulate Matter and Lung Function: Results from the China Pulmonary Health Study",
  sub=corpus.RESP, design="Observational - cross-sectional", pm="Long-term PM1, PM1-2.5, PM2.5, PM2.5-10, PM10 (per IQR)",
  geo="China (national, CPH Study)", endpoint="Spirometry: FEV1, FVC, FEV1/FVC, FEF75, FEF25-75", tier="A",
  n=("50,991 adults >=20 y from the China Pulmonary Health Study; multivariable linear models on long-term size-resolved PM. "
     "Per IQR PM1: FEV1 -36.84 mL (-45.91 to -27.76), FVC -34.63 mL (-45.48 to -23.79); large-airway decrements grew as "
     "particle size fell, whereas the coarse fraction PM2.5-10 gave the largest small-airway (FEF75, FEF25-75) decrements. "
     "Limitation: size fractions are derived from correlated modelled surfaces (PM1 and PM2.5 share most of their mass), "
     "and the abstract reports no multi-fraction model, so 'size-specific' ranking may reflect differential exposure-model "
     "error rather than biology; cross-sectional. Relevance: high - optical LCS report PM1 and coarse bins natively, "
     "and this is evidence that those channels carry distinct health signal worth calibrating, not discarding.")),
 dict(pmid="42902466", doi="10.1097/jom.0000000000003913", journal="J Occup Environ Med",
  short="Lin PM2.5 frailty trajectories CHARLS 2026",
  title="The association of particulate matter 2.5 exposure with frailty trajectories in middle-aged and older Chinese adults and the potential modification by lifestyle and socioeconomic status",
  sub=corpus.OTHR, design="Prospective cohort", pm="Satellite-derived PM2.5 (Dalhousie/ACAG surface, per 10 ug/m3)",
  geo="China (national, CHARLS)", endpoint="Frailty-index trajectories (group-based trajectory modelling)", tier="B",
  n=("10,659 CHARLS participants; deficit-accumulation frailty index, three GBTM trajectories (stable low 64%, increasing to "
     "frailty 29%, continuously worsening 7%). Per 10 ug/m3 PM2.5, odds of the two adverse trajectories rose 15.2% and 12.3% "
     "(ordered logistic; no CIs in the abstract). Higher SES attenuated the association (RERI -0.067); unhealthy sleep "
     "duration amplified it (RERI 0.163). Limitation: GBTM classes are model artefacts with posterior misclassification "
     "carried into a second-stage regression without uncertainty propagation; CHARLS addresses are coarse (city/county), "
     "so exposure contrast is mostly between regions with different healthcare and diet. Relevance: low - "
     "regional satellite exposure, no sensing implication.")),
]
