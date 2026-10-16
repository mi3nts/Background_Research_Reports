# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="42856995", doi="10.1016/j.pccm.2026.08.006", journal="Chin Med J Pulm Crit Care Med",
  short="Guo lung cancer burden 2026",
  title="Trends in lung cancer burden, risk factors, and disease projections in China and the United States, 1990-2023",
  sub=corpus.BURD, design="Health impact model",
  pm="GBD 2023 risk-factor attribution including ambient and household air pollution",
  geo="China and United States", endpoint="Lung cancer incidence, mortality, DALYs (to 2050)", tier="C",
  n=("GBD 2023 data with joinpoint regression, three-factor Das-Gupta decomposition and Bayesian "
     "age-period-cohort projection to 2050, comparing lung cancer burden and its attributable risks - "
     "smoking, air pollution, occupational exposure, metabolic and dietary factors - between China and "
     "the United States. Limitation: GBD attribution for air pollution is a modelled counterfactual built "
     "on exposure surfaces and borrowed concentration-response functions, so the pollution share is an "
     "assumption propagated forward, not an observation; the abstract reports no attributable fractions. "
     "Relevance: low-moderate - useful as the burden framing that the measurement side of this corpus "
     "feeds, but it adds no exposure information of its own.")),

 dict(pmid="", doi="10.3390/atmos17100992", journal="Atmosphere",
  short="Chiappini WRF-Chem nudging 2026",
  title="Regime-Dependent Effectiveness of Spectral Nudging in WRF-Chem: Meteorological and Saharan Dust Skill over the Central Mediterranean",
  sub=corpus.SENS, design="Chemical transport model",
  pm="Modelled Saharan dust AOD550 against AERONET; meteorological RMSE from nudged vs free runs",
  geo="Europe (Central Mediterranean)", endpoint="None (model skill)", tier="B",
  n=("A two-tier design separates the meteorological response to spectral nudging (a 104-day chemistry-"
     "free pair) from the dust-transport response (paired event simulations). Nudging improves sea-level "
     "pressure most (daily RMSE 2.08 to 1.53 hPa) and 10 m wind less (2.50 to 2.20 m/s), while 2 m "
     "temperature does not improve (2.05 to 2.15 C); the benefit recurs episodically rather than growing "
     "with simulation age. Dust skill is conditional: in the weakly forced June case all seven AERONET "
     "sites improved (station-mean RMSE 0.457 to 0.235, correlation 0.778 to 0.881), while in March RMSE "
     "fell at all eight sites but mean correlation was unchanged. Limitation: two outbreaks is a thin "
     "basis for a regime claim, and AOD is a column integral that constrains surface dust PM only weakly. "
     "Relevance: moderate - dust is the event class where satellite-and-model PM products diverge most "
     "from surface nodes.")),

 dict(pmid="42855819", doi="10.1097/cm9.0000000000004256", journal="Chin Med J (Engl)",
  short="Qiang maternal PM macrosomia 2026",
  title="Interaction of maternal PM2.5 exposure and psychosocial state on newborn macrosomia: A nationwide population-based study",
  sub=corpus.REPR, design=MO,
  pm="Metadata only - maternal PM2.5 exposure with psychosocial state, nationwide (by title)",
  geo="China (nationwide)", endpoint=NA, tier="B",
  n=("Metadata-only record: the publisher deposited title, authors and DOI on 10 Oct with no abstract, and "
     "the retry chain recovered none. By title, a nationwide study of the interaction between maternal "
     "PM2.5 exposure and maternal psychosocial state on newborn macrosomia. Interaction claims between a "
     "modelled environmental exposure and a self-reported psychosocial measure are the design most prone "
     "to residual confounding by socioeconomic position, and macrosomia is a thresholded birthweight "
     "outcome whose prevalence is sensitive to that. Relevance: moderate - birth cohorts are where "
     "personal rather than residential exposure measurement would change the estimate most. On the "
     "abstract-retry list.")),

 dict(pmid="", doi="10.1016/j.atmosenv.2026.122420", journal="Atmos Environ",
  short="Abdella Italy urban-rural 2026",
  title="Cleaning the air or shifting the burden? Characterizing urban-rural disparities in air pollution-attributable mortality across Italy",
  sub=corpus.BURD, design=MO,
  pm="Metadata only - urban-rural disparity in PM-attributable mortality across Italy (by title)",
  geo="Italy (national)", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 10 Oct with no abstract. By "
     "title, an attributable-mortality analysis asking whether Italian air-quality gains have been "
     "distributed or merely displaced from urban to rural populations. Rural exposure is systematically "
     "the worse-measured half of any national network, so a rural-urban disparity estimate inherits the "
     "monitoring asymmetry it is trying to describe - the 8 October US block-level record showed spatial "
     "aggregation attenuating exactly this kind of disparity. Relevance: moderate-high; on the "
     "abstract-retry list.")),

 dict(pmid="", doi="10.1007/s44408-026-00172-9", journal="Aerosol Air Qual Res",
  short="Anwar Pretoria FTIR 2026",
  title="PM2.5 Composition and Organic Matter Sources in Pretoria, South Africa Employing Fourier Transform-Infrared Spectroscopy",
  sub=corpus.EXPO, design=MO,
  pm="Metadata only - FT-IR functional-group speciation of PM2.5 organic matter (by title)",
  geo="South Africa (Pretoria)", endpoint=NA, tier="B",
  n=("Metadata-only record: title, authors and DOI deposited 10 Oct with no abstract. By title, FT-IR "
     "functional-group analysis of PM2.5 organic matter in Pretoria with source attribution. FT-IR on "
     "routine filters is one of the few speciation routes cheap enough to run network-wide, and "
     "sub-Saharan African composition data are scarce enough that any new site matters. Relevance: high "
     "for the composition gap this corpus repeatedly hits; on the abstract-retry list.")),
]
