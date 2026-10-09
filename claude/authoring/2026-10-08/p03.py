# -*- coding: utf-8 -*-
P = [
 dict(pmid="42845224", doi="10.4168/aair.2026.18.5.668", journal="Allergy Asthma Immunol Res",
  short="Ko-CHENS 36 months 2026",
  title="Exposure to Environmental Pollutants and the Risk of Respiratory Illnesses in 36-Month-Old Children: The Korean Children's Environmental Health Study",
  sub=corpus.RESP, design="Prospective birth cohort (mixtures)",
  pm="Home-visit indoor PM10 and PM2.5 with VOCs and dust-mite allergen; blood metals and urinary metabolites",
  geo="South Korea (Ko-CHENS)", endpoint="Six respiratory illnesses at 36 months", tier="B",
  n=("4,059 children with measured indoor pollutants at a 36-month home visit, blood lead, mercury and "
     "cadmium, urinary endocrine-disruptor metabolites and questionnaire outcomes, analysed by "
     "quantile g-computation. Allergic rhinitis was most prevalent; children with respiratory illness had "
     "more tobacco-smoke exposure and pet ownership, and higher dust-mite levels with recurrent wheezing "
     "and pneumonia. The mixture was positively associated with allergic rhinitis (driven by lead and "
     "phthalates) and with pneumonia (phthalates). Limitation: the indoor PM measurement is a single "
     "home visit standing in for three years of exposure, and in a mixture model dominated by biomarkers "
     "with month-long half-lives, that one spot measurement is the weakest term - which is a likely "
     "reason PM does not drive any of the mixture associations. Relevance: high - a continuously logging "
     "indoor node would replace the single visit, and this cohort shows what the single visit costs.")),

 dict(pmid="42845995", doi="10.3389/fpubh.2026.1926405", journal="Front Public Health",
  short="Hefei conjunctivitis 2026",
  title="Ambient air pollutants and outpatient visits for conjunctivitis in Hefei, China: a time-series study of hospital-based data during 2014-2023",
  sub=corpus.OTHR, design="Monitoring-record analysis",
  pm="Daily PM2.5 and PM10 with O3, NO2 and SO2 from regulatory monitors",
  geo="China (Hefei)", endpoint="Outpatient visits for conjunctivitis", tier="C",
  n=("73,043 conjunctivitis outpatient records, 2014-2023, in a time-series design with stratification by "
     "sex, age, season and pandemic period. All five pollutants were positively associated with daily "
     "visits, strongest generally at lag0; SO2 carried the largest lag-0 estimate, then NO2, with "
     "pollutant-specific cumulative lag patterns. Limitation: no effect sizes, units or intervals appear "
     "in the abstract, so nothing can be entered; SO2 ranking first in a city where SO2 has fallen to a "
     "few ug/m3 suggests a marker for combustion-season conditions rather than a conjunctival effect, and "
     "single-city time series cannot separate co-varying pollutants. Relevance: low-moderate - ocular "
     "surface endpoints are plausible for coarse and irritant exposure, and a record of the claim is "
     "worth keeping even though this analysis does not establish it.")),

 dict(pmid="42846892", doi="10.3389/fped.2026.1899313", journal="Front Pediatr",
  short="Sao Paulo paediatric 2026",
  title="Climate and air pollution are associated with pediatric respiratory hospitalizations in Sao Paulo, Brazil",
  sub=corpus.RESP, design="Observational - cross-sectional",
  pm="IDW-interpolated pollutant and meteorological fields at geocoded residence, 2022",
  geo="Brazil (Metropolitan Sao Paulo)", endpoint="Bronchiolitis and acute respiratory infection hospitalisation", tier="C",
  n=("Paediatric emergency visits and admissions recorded in 2022, geocoded, with exposures assigned by "
     "inverse-distance weighting and multivariable logistic models for two outcomes. Higher ozone "
     "(OR 1.012, 1.005-1.019), higher relative humidity (1.016, 1.005-1.027) and spring were associated "
     "with greater odds that a respiratory encounter was a bronchiolitis admission; lower temperature was "
     "associated with the unspecified-ARI outcome (0.887, 0.793-0.993 per unit). Limitation: the outcome "
     "is conditional on presenting - these are odds of diagnosis given an encounter, not risk of disease, "
     "so the design cannot speak to incidence; IDW over a sparse monitor network in a metropolitan area of "
     "21 million is the same interpolation problem the 2 October Everglades record quantified. "
     "Relevance: moderate - no PM estimate reaches significance here, which is itself informative about "
     "what IDW exposure does to a signal.")),

 dict(pmid="", doi="10.5194/acp-26-14073-2026", journal="Atmos Chem Phys",
  short="Aerosol Fe isotopes 2026",
  title="Isotopic composition of aerosol iron from anthropogenic sources: implications for source apportionment of aerosol iron",
  sub=corpus.EXPO, design="Source apportionment",
  pm="delta-56Fe endmembers for desert dust and anthropogenic aerosol iron sources",
  geo="Global (source characterisation)", endpoint="None (source apportionment)", tier="B",
  n=("Iron isotope endmembers measured for desert dust and several anthropogenic sources: dust averaged "
     "+0.14 +/- 0.10 per mil (n=7, consistent with prior work), power-plant coal fly ash +0.26 +/- 0.18 "
     "(n=28) and steelwork fly ash -0.07 +/- 0.41, with a wide anthropogenic range overall. Limitation: "
     "the endmembers overlap heavily - a steelwork standard deviation of 0.41 per mil against a dust mean "
     "of +0.14 means a mixed urban sample cannot be apportioned by delta-56Fe alone, which the spread "
     "itself makes plain; small n for dust. Relevance: moderate - soluble aerosol iron matters for "
     "oxidative potential and for ocean biogeochemistry, and isotopic apportionment is the kind of "
     "offline chemistry that fixed networks will never do but that calibrates what they see.")),
]
