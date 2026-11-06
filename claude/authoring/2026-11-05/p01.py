# -*- coding: utf-8 -*-
P = [
 dict(pmid="42982790", doi="10.1038/s41467-026-77148-1", journal="Nat Commun",
  short="Agrawal Bihar low-cost sensor network ML exposure inequity short-term mortality 2026",
  title="Unveiling hidden air pollution exposure and impacts with low-cost sensor network-based frameworks.",
  sub=corpus.SENS, design="Network deployment + statistical model",
  pm="PM2.5 from a dense statewide low-cost sensor network, gap-filled by machine learning",
  geo="India", endpoint="District exposure by socioeconomic group; attributable short-term mortality", tier="A",
  basis="Low-cost sensor / network", affil="Indian Institute of Technology Kanpur, India; Indian Institute of Technology Kanpur, India",
  n=("Dense low-cost PM2.5 network across Bihar, fused with ML surfaces, NFHS socioeconomic data and India-specific relative risks. Northern districts carried "
     "1.2 times the mean exposure of southern ones; district mortality per 100,000 varied up to 1.7-fold and daily attributable mortality 3.2-fold. State-level "
     "exposure inequity was limited, intra-regional inequity substantial. The abstract gives no sensor count, calibration R2/RMSE, or uncertainty on the "
     "attributable deaths, and the mortality is borrowed risk functions applied to sensor-derived surfaces, not an observed association; network calibration "
     "error propagates straight into the burden. Relevance: direct - the clearest flagship case for low-cost networks as a burden-estimation input outside cities.")),
 dict(pmid="42986618", doi="10.1001/jamaoto.2026.3453", journal="JAMA Otolaryngol Head Neck Surg",
  short="Yang US claims case-control PM2.5 sinonasal malignant neoplasm 2026",
  title="Fine Particulate Matter Exposure and Sinonasal Malignant Neoplasm.",
  sub=corpus.OTHR, design="Case-control (registry)",
  pm="PM2.5 from NASA 1-km satellite-meteorology-land-use models, averaged to residential MSA over 6 months, 1 and 5 years",
  geo="USA", endpoint="First observed sinonasal malignant neoplasm diagnosis", tier="A",
  basis="Satellite-fused", affil="Stanford University, USA; Mayo Clinic Florida, USA",
  n=("National commercial-claims case-control, 2007-2020: 3,600 SNM cases, 17,695 controls (~1:5). Per SD PM2.5 (about 2.5 ug/m3), adjusted OR 1.25 (1.05-1.49) "
     "for the 6-month mean, 1.31 (1.08-1.59) for 1 year and 1.36 (1.11-1.66) for 5 years, rising with averaging window. Exposure is assigned at "
     "metropolitan-area level, so a 1-km product is collapsed to an ecological contrast of ~0.2-0.3 ug/m3 between groups; smoking and deprivation are regional, "
     "not individual, and occupational wood/leather dust - the dominant SNM cause - is unmeasured. Cases are 10 years older than controls. "
     "Relevance: indirect - a rare endpoint where residence-level exposure from dense sensing would remove the MSA misclassification.")),
 dict(pmid="42988295", doi="10.1016/j.envres.2026.126109", journal="Environ Res",
  short="Zhang Shanxi 11-city time-series pollutant mixtures influenza vaccination 2026",
  title="Influenza Incidence in Relation to Air Pollution Mixtures and the Modifying Role of Vaccination in Shanxi Province, China.",
  sub=corpus.RESP, design="Multi-city time-series + random-effects meta-analysis",
  pm="Daily city-mean PM2.5, PM10, NO2, SO2, CO, O3 from regulatory monitors",
  geo="China", endpoint="Reported influenza incidence, lag 0-7 d", tier="B",
  basis="Reference / regulatory monitor", affil="Shanxi Medical University, China; Shanxi Medical University, China",
  n=("11 Shanxi cities, 2014-2022, DLNM with zero-inflated negative binomial and meta-analysis. Per 10 ug/m3 PM2.5, RR 1.024 (1.015-1.034); PM10 1.018 "
     "(1.010-1.025); NO2 1.115 (1.086-1.146). WQS (1.078, 1.005-1.157) and qgcomp (1.122, 1.064-1.182) mixture effects were driven by SO2 and NO2, not PM. "
     "Vaccination modification is city-level coverage, therefore ecological, and labelled exploratory. Surveillance incidence is care-seeking and testing "
     "dependent; 2020-2022 includes COVID-era behavioural shifts the abstract does not say were handled. Relevance: indirect - PM signal is small next to "
     "gases, which argues for multi-pollutant nodes rather than PM-only networks for infectious endpoints.")),
 dict(pmid="41860719", doi="10.1007/s00484-026-03163-y", journal="Int J Biometeorol",
  short="Hao Shanghai case-crossover lab-confirmed influenza six pollutants 2026",
  title="Association between short-term air pollutant exposure and influenza incidence in Shanghai, China: A case-crossover study",
  sub=corpus.RESP, design="Time-stratified case-crossover",
  pm="PM2.5, PM10, SO2, NO2, O3, CO interpolated by inverse distance weighting to individual address",
  geo="China", endpoint="Laboratory-confirmed influenza", tier="B",
  basis="Reference / regulatory monitor", affil="Sun Yat-sen University, China; Sun Yat-sen University, China",
  n=("Laboratory-confirmed influenza cases, Shanghai 2013-2017, time-stratified case-crossover with IDW exposure at the individual level. Per 10 ug/m3 PM10, "
     "OR 1.019 (1.004-1.034); O3 was inverse (OR 0.959, 0.941-0.977). PM2.5, SO2, NO2 and CO were positive across lags but their point estimates are not in the "
     "abstract. Laboratory confirmation is the design's strength over syndromic counts; IDW from a sparse regulatory grid and selection into testing are the "
     "weaknesses, and the negative O3 term likely absorbs season. Read alongside the same-day Shanxi series: two independent Chinese designs give PM effects "
     "near 2% per 10 ug/m3. Relevance: indirect. \\textsc{backfill}, entry 20 March 2026.")),
]
