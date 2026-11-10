# -*- coding: utf-8 -*-
P = [
 dict(pmid="43003339", doi="10.1016/j.envpol.2026.129522", journal="Environ Pollut",
  short="Park residential testbed low-cost indoor particle sensor ML vs linear calibration data volume source heterogeneity 2026",
  title="Data-Dependent Performance of Machine Learning Calibration for Low-Cost Indoor Particle Sensors.",
  sub=corpus.SENS, design="Calibration model comparison",
  pm="Indoor PM from low-cost optical particle sensors against reference instruments, three controlled source conditions",
  geo="South Korea", endpoint="Calibration R2, normalised error and bias under intra-, cross- and multi-source training", tier="A",
  basis="Low-cost sensor / network", affil="Dankook University, South Korea; Sejong University, South Korea",
  n=("Full-scale residential testbed, three particle-source conditions, linear regression against three ML models under intra-source, cross-source and "
     "multi-source training. Adding sensor particle-number channels raised R2 by 0.05-0.10 and cut normalised error by up to 25%. LightGBM was the best "
     "nonlinear model and gained most from more training data, but at fixed data volume greater source heterogeneity lowered its error and bias without "
     "raising R2 or beating linear regression; with more multi-source data it won on error and bias while linear regression kept the higher R2. "
     "The abstract names neither the sensor models nor the reference, and three sources in one house is a narrow test of transfer. "
     "Relevance: direct - 'ML beats linear' is metric- and data-dependent, so calibration claims must state both.")),
 dict(pmid="", doi="10.1155/ina/1015833", journal="Indoor Air",
  short="Ramadan review spatial uncertainty indoor air quality monitoring mobile sensing position error response-time displacement 2026",
  title="Spatial Intelligence for Indoor Air Quality: Integrating Spatial Uncertainty Into Monitoring, Exposure Assessment, and Ventilation Control",
  sub=corpus.SENS, design="Mapping review",
  pm="Indoor pollutant concentrations from fixed and mobile sensors; position and response-time uncertainty",
  geo="Global / multi-region", endpoint="Propagation of spatial uncertainty through monitoring, exposure and control chains", tier="B",
  basis="Review / no primary exposure", affil="Istanbul Aydin University, Turkiye; Abu Dhabi University, UAE",
  n=("Scored review of 91 indoor air-quality publications using a 'Building Spatial Intelligence' framework: capability profile, a propagation level for how "
     "far spatial uncertainty travels downstream, and nine system archetypes. None of the 91 attaches a quantified uncertainty to measurement position, none "
     "quantifies sensor-response displacement, and none of the 31 mobile-platform studies reports position uncertainty. The key physical point: on a moving "
     "platform, speed times sensor time constant typically displaces a reading further than positioning error, a systematic shift correctable by "
     "re-registration. The scoring is the authors' own construct and the corpus is not claimed to represent the field. "
     "Relevance: direct - mobile low-cost PM mapping inherits exactly this lag-displacement error, and the scoring dataset is released.")),
 dict(pmid="43002327", doi="10.1007/s10661-026-16146-8", journal="Environ Monit Assess",
  short="Bengaluru CAAQM hybrid gap-filling random forest proxy station PM2.5 PM10 trends 2016-2025",
  title="Hybrid gap-filling framework and spatiotemporal analysis of urban air pollution in Bengaluru, India.",
  sub=corpus.EXPO, design="Long-term field measurement campaign",
  pm="PM2.5, PM10, NOx, NH3, O3 from three continuous regulatory monitors, gaps filled by interpolation, random forest and proxy stations",
  geo="India", endpoint="Data completeness; trends and exceedance days 2016-2025", tier="C",
  basis="Reference / regulatory monitor", affil="K S School of Engineering and Management, India; K S School of Engineering and Management, India",
  n=("Three Bengaluru CAAQM stations (Peenya, Majestic, Bellandur), 2016-2025. Short gaps are linearly interpolated, longer ones filled by random forest "
     "regression and proxy-station substitution, then trends, seasonality and exceedances computed on the reconstructed series. PM2.5 declined at Peenya "
     "while PM10 rose at Peenya and Bellandur, read as road dust and construction; exceedance days cluster in winter and pre-monsoon and are far more "
     "frequent against WHO than Indian NAAQS limits. The abstract reports no gap-filling validation metrics or the fraction of each series imputed, so "
     "trends could partly be imputation artefacts. Relevance: indirect - gap-filled regulatory series are the usual reference for sensor calibration in "
     "Indian cities, and imputed reference values must be flagged before use.")),
 dict(pmid="43002255", doi="10.1007/s10653-026-03578-x", journal="Environ Geochem Health",
  short="Clemente western Mediterranean suburban rural PM2.5 oxidative potential DTT AA PMF biomass burning traffic 2026",
  title="What drives the oxidative potential of fine particles? Insights from suburban and rural sites of the western Mediterranean.",
  sub=corpus.EXPO, design="Intensive field campaign, PMF source apportionment",
  pm="PM2.5 filters; OP by DTT and ascorbic-acid acellular assays; PMF with GLS regression",
  geo="Spain", endpoint="Source contributions to volume-normalised OP-DTT and OP-AA", tier="B",
  basis="Lab / research instrument", affil="Miguel Hernandez University, Spain; Miguel Hernandez University, Spain",
  n=("PM2.5 filters at one suburban and one rural site in south-eastern Spain, OP by DTT and AA assays, PMF sources regressed on OP by GLS. Mass and "
     "volume-normalised OP were higher at the suburban site. In winter biomass burning was nearly 50% of rural PM2.5 mass and the dominant driver of both "
     "OP measures there; at the suburban site traffic and biomass burning drove OP. In summer aged sea salt and secondary sulfate contributed substantially, "
     "which the authors attribute to co-varying redox-active organics or acid-enhanced metal solubility rather than sulfate itself. Two sites, source-OP "
     "regression without uncertainty in the abstract, and no exposure or health link. Relevance: indirect - mass-only sensors miss the source-dependent "
     "toxicity this shows; OP varies by season at fixed mass.")),
]
