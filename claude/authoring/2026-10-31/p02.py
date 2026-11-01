# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.21203/rs.3.rs-11373778/v1", journal="Research Square (preprint)",
  short="Anjum Idaho PM2.5 2005-2024 wildfire vs wood-smoke regimes 2026",
  title="Long-Term Spatiotemporal Variability of Fine Particulate Matter (PM2.5) Across Idaho, USA, Using Statistical and Geospatial Tools",
  sub=corpus.EXPO, design="Monitoring-record analysis", pm="EPA AQS daily PM2.5, 32 sites (4,260 site-months)",
  geo="USA (Idaho)", endpoint="PM2.5 trends, seasonality and source regimes", tier="A",
  n=("EPA AQS daily PM2.5 at 32 Idaho sites, 2005-2024, aggregated to 4,260 site-months; Mann-Kendall/Theil-Sen trends, "
     "PCA and IDW. Mean 7.53 ug/m3 (site range 3.16-12.08). Bimodal climatology: an August-September wildfire peak and a "
     "November-February wood-smoke/inversion peak; July-September carries 36.6% of annual mass. Cold-season and "
     "background series declined while fire-season PM2.5 rose 2.54 ug/m3 per decade, holding the annual mean flat; "
     "32.7% of site-years exceed the 9.0 ug/m3 standard. Limitation: unreviewed preprint; IDW over 32 sites in "
     "mountainous terrain is not an exposure surface, and the 'regimes' are PCA loadings, not source apportionment. "
     "Relevance: high - two diverging seasonal regimes in inversion valleys are precisely where sparse FRM coverage "
     "fails and a calibrated PurpleAir layer (smoke-specific correction) adds most.")),
 dict(pmid="", doi="10.21203/rs.3.rs-10780874/v1", journal="Research Square (preprint)",
  short="Arif Agra footwear cluster ventilation IAQ tiers 2026",
  title="Ventilation, indoor air quality and thermal comfort in India's leather footwear manufacturing cluster: a tier-resolved field study",
  sub=corpus.OCC, design="Cross-sectional (occupational)", pm="Breathing-zone PM2.5 with CO2, TVOC, formaldehyde, air velocity",
  geo="India (Agra)", endpoint="Workplace IAQ vs WHO/OEL limits; thermal comfort", tier="B",
  n=("Agra footwear cluster, three enterprise tiers (formal factory to cottage unit), 378 worker-sessions over four "
     "seasons and 147 days, breathing-zone measurements paired with ASHRAE 55 ballots. All pollutants rose linearly "
     "from large to cottage scale as air velocity fell from 0.80 to 0.16 m/s; velocity explained 79% of between-tier "
     "pollutant variance. No session anywhere met the WHO PM2.5 guideline; 91.3% exceeded the ACGIH formaldehyde TLV. "
     "Limitation: unreviewed preprint; PM instrument and calibration are not described in the abstract, and session "
     "means against an annual guideline overstate comparability. Relevance: moderate - informal-sector workplaces with "
     "no monitoring are an obvious deployment niche for wearable or wall-mounted low-cost PM nodes.")),
 dict(pmid="", doi="10.1029/2025gh001735", journal="GeoHealth",
  short="Li spatiotemporal causal machine learning PM2.5 asthma Colorado counties 2026",
  title="A Spatiotemporal Causal Machine Learning Framework for Quantifying the Impact of PM2.5 on Asthma at the Community Level",
  sub=corpus.RESP, design="Causal ML on monitoring records", pm="County-month PM2.5 (exposure surface not stated in abstract)",
  geo="USA (Colorado)", endpoint="Asthma hospitalisations and ED visits (county-month)", tier="B",
  n=("Colorado county-level monthly asthma hospitalisations and ED visits, 2011-2019, modelled with a spatiotemporal "
     "representation-learning network plus a causal-inference layer that estimates counterfactual outcomes under "
     "hypothetical PM2.5 reductions. Estimated effects were heterogeneous, larger in communities with compounded "
     "environmental and social stressors, with wider uncertainty in data-sparse counties. No effect size per ug/m3 is "
     "given in the abstract. Limitation: county-month aggregation with monthly PM2.5 is ecological; 'causal' here "
     "rests on unconfoundedness given learned covariates, which a neural model cannot verify, and sparse rural counties "
     "are exactly where exposure error peaks. Relevance: moderate - the model's uncertainty is concentrated where "
     "monitors are absent, an explicit argument for sensor densification in rural Colorado.")),
]
