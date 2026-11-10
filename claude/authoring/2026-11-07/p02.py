# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1029/2026gh001972", journal="GeoHealth",
  short="Huang All of Us case-crossover wildfire smoke PM2.5 adult asthma exacerbation 2026",
  title="Asthma Exacerbations Following Wildfire Smoke PM2.5 Exposure Among U.S. Adults",
  sub=corpus.RESP, design="Time-stratified case-crossover",
  pm="Wildfire-smoke PM2.5 at residence, lags 0-7 d, April-August 2006-2019",
  geo="USA", endpoint="Asthma exacerbation events (EHR)", tier="A",
  basis="Model (CTM / LUR / ML)", affil="",
  n=("NIH All of Us: 18,935 adult asthma exacerbations, four matched control periods each, warm months 2006-2019. Wildfire-smoke PM2.5 was associated with "
     "exacerbation at every lag 0-7 d, adjusted OR 1.27 (1.22-1.33) to 1.38 (1.32-1.44); higher in older adults, non-Hispanic White, Midwestern residents and in May. "
     "The abstract does not state the exposure increment or the smoke-PM product, so the OR cannot be scaled, and an OR near 1.3 is large for smoke PM per usual "
     "increments - likely a binary smoke-day or large contrast. All of Us EHR linkage selects insured, engaged participants. Relevance: indirect - the Midwestern "
     "excess points at long-range transported smoke, where PurpleAir density is thinnest.")),
 dict(pmid="42996647", doi="10.21037/jtd-2026-1940", journal="J Thorac Dis",
  short="Tsogtbayar Ulaanbaatar time-series PM1 PM2.5 under-5 pneumonia outpatient 2026",
  title="Associations between air pollution and pediatric pneumonia incidence in Ulaanbaatar, Mongolia: age and sex susceptibility.",
  sub=corpus.RESP, design="Time-series (quasi-Poisson GAM)",
  pm="Daily city PM1, PM2.5, PM10, SO2, NO2, O3 from monitors, per IQR",
  geo="Mongolia", endpoint="Daily outpatient pneumonia visits, children <5 y", tier="B",
  basis="Reference / regulatory monitor", affil="Mongolian National University of Medical Sciences, Mongolia; Mongolian National University of Medical Sciences, Mongolia",
  n=("Ulaanbaatar 2014-2019, 48,488 under-5 outpatient pneumonia visits, adjusted for season, weather, holidays and the raw-coal ban. At lag 2, per IQR: PM2.5 RR 1.057 "
     "(1.015-1.100), PM1 1.065 (1.025-1.106), SO2 1.136 (1.023-1.261), NO2 1.383 (1.108-1.726); PM10 and O3 non-significant. Infants <1 y showed PM1 RR 1.098 "
     "(1.046-1.152) at lag 0. PM2.5 and NO2 survived co-pollutant adjustment. IQR values are not in the abstract, outpatient visits depend on care-seeking, and NO2 "
     "dwarfs PM. Relevance: indirect - PM1 outperforming PM10 in a coal-heating city favours sub-micron-capable nodes in ger districts, where the regulatory monitors that fed this series are sparse.")),
 dict(pmid="42996406", doi="10.3389/fpubh.2026.1950463", journal="Front Public Health",
  short="Kulkayeva Almaty time-series PM2.5 cardiovascular mortality null 2026",
  title="Short-term effects of ambient PM2.5 exposure on cardiovascular mortality in Almaty, Kazakhstan.",
  sub=corpus.CVM, design="Time-series (DLNM, quasi-Poisson)",
  pm="Daily city PM2.5, mean 36.9 +/- 33.3 ug/m3, lags 0-7 d",
  geo="Kazakhstan", endpoint="Daily cardiovascular mortality", tier="B",
  basis="Reference / regulatory monitor", affil="Salidat Kairbekova National Scientific Research Center for Health Development, Kazakhstan; Al-Farabi Kazakh National University, Kazakhstan",
  n=("Almaty 2017-2025, 3,287 days, 43,095 cardiovascular deaths, mean PM2.5 36.9 ug/m3. Cumulative lag 0-7 RR 1.011 (0.837-1.222), null; age >=65 RR 1.174 "
     "(0.926-1.489), also null; lag-specific risk peaked at 2-4 days. The comparison increment for the cumulative RR is not given in the abstract, the CI spans a 16% "
     "deficit to a 22% excess, and the PM2.5 series source and station count are unstated. Relevance: indirect - Almaty's monitor record is thin and its PurpleAir "
     "network is one of the denser in Central Asia; a sensor-fused exposure series could narrow exactly this interval. Included as a reported null from an under-studied region.")),
 dict(pmid="42995455", doi="10.1177/10815589261507081", journal="J Investig Med",
  short="Xu CHARLS PM1 PM2.5 PM10 cardiometabolic multimorbidity cohort 2026",
  title="EXPRESS: Air pollution increases cardiometabolic diseases in China: A nationwide longitudinal cohort study.",
  sub=corpus.CVM, design="Prospective cohort",
  pm="Long-term PM1, PM2.5, PM10, O3, NO2 (exposure model not stated in the abstract)",
  geo="China", endpoint="Incident cardiometabolic multimorbidity", tier="C",
  basis="Not stated", affil="First Affiliated Hospital of Harbin Medical University, China; First Affiliated Hospital of Harbin Medical University, China",
  n=("CHARLS, 8,725 adults aged >=45 free of cardiometabolic multimorbidity (two or more of hypertension, diabetes, CVD, stroke) at 2011 baseline, followed to 2020. "
     "All five pollutants - PM1, PM2.5, PM10, O3, NO2 - were associated with incident multimorbidity, more strongly with lower education and short sleep. The abstract "
     "reports no hazard ratios, increments, case counts or exposure model, so magnitude cannot be judged; participants with one condition at baseline were retained, "
     "which mixes progression with onset. Relevance: indirect - one more CHARLS reuse with a satellite-type exposure inferred; no new measurement contribution.")),
]
