# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.64898/2026.10.15.26365428", journal="medRxiv (preprint)",
  short="Zhang US wildfire smoke five-year mortality impulse response 2026",
  title="Wildfire smoke leaves a large five-year imprint on mortality in the United States",
  sub=corpus.BURD, design="Distributed-lag panel deconvolution", pm="Monthly county-level wildfire-attributable PM2.5 (smoke PM2.5 surface)",
  geo="United States (all counties)", endpoint="All-cause, circulatory and respiratory mortality", tier="A",
  n=("County-month mortality and wildfire-PM2.5 panels 2011-2023; episodic smoke pulses are used to deconvolve overlapping "
     "responses and recover an impulse-response function. Excess mortality peaks about three years after a pulse and is "
     "gone by five. Integrated over 2011-2023 this gives 1.7 million smoke-associated deaths (95% UI 1.1-2.3 million), "
     "roughly ten times what long-term ambient PM2.5 relative risks imply; circulatory and respiratory causes contribute "
     "comparably, adults >=65 dominate, and responses were larger during COVID-19. Limitation: a three-year lag in an "
     "ecological panel is exposed to slow confounders (migration, economic shocks, drought, heat) co-varying with fire "
     "years; the order-of-magnitude excess needs independent replication before it enters burden accounting. "
     "Relevance: high - a multi-year lag makes historical smoke-PM2.5 reconstructions, including LCS-corrected ones, the "
     "binding input.")),
 dict(pmid="", doi="10.21203/rs.3.rs-11157411/v1", journal="Research Square (preprint)",
  short="Chyzhykov gravimetric filter water Karl Fischer bias 2026",
  title="Impact of Mass Loading and Water Speciation on Precision and Artifacts in Gravimetric Measurements of Atmospheric Particulate Matter",
  sub=corpus.SENS, design="Laboratory metrology", pm="Gravimetric PM1, PM2.5, PM10 on 47 mm glass-fibre filters; Karl Fischer coulometric filter water",
  geo="Poland (Krakow steelworks; Zdzieszowice coal)", endpoint="Not applicable (reference-method metrology)", tier="A",
  n=("Thirty filters (n=5 per fraction per site) plus five field blanks, weighed under PN-EN 12341:2024 conditioning, "
     "then stepwise thermal water release at 50, 120, 180 and 250 C. Between-filter variability was U-shaped in mass "
     "loading, minimal near 1330-1360 ug; PM1 was the most variable fraction (CV up to 53%). Strongly bound water "
     "(180-250 C) made up 51-60% of filter water, survives standard conditioning, and adds a systematic +3% to +18% mass "
     "bias, largest for PM1 at the steelworks. Limitation: 35 filters at two industrial sites; the bias is not yet "
     "resolved by composition or RH history, so transfer to urban background aerosol is untested. Relevance: high - "
     "every LCS calibration inherits the reference's error; a positive, composition-dependent water bias in gravimetric "
     "PM1 and PM2.5 propagates directly into co-location slopes.")),
 dict(pmid="42889176", doi="10.3389/fmed.2026.1969759", journal="Front Med (Lausanne)",
  short="Zhang air pollution cataract meta-analysis 2026",
  title="Air pollution exposure and cataract outcomes: a systematic review and pollutant-specific meta-analysis",
  sub=corpus.OTHR, design="Systematic review & meta-analysis", pm="Long-term PM2.5, PM10, NO2, black carbon (study-specific models)",
  geo="Global / multi-region (15 studies)", endpoint="Incident cataract / cataract surgery", tier="B",
  n=("Fifteen observational studies, seven pooled with REML random effects (search to 10 Aug 2026; ROBINS-E). PM2.5: HR "
     "1.036 (0.988-1.086) per 1 ug/m3, I2 99.7%; NO2: HR 1.041 (1.013-1.070) per 10 ug/m3, I2 86%; black carbon per IQR: "
     "HR 1.010 (0.983-1.038), I2 33%. Highest-vs-lowest quartile was positive for NO2 (HR 1.094, 1.057-1.133) and null "
     "for PM2.5 and PM10; Knapp-Hartung widened the NO2 interval. Limitation: with I2 near 100% the pooled PM2.5 point "
     "estimate is not interpretable as a common effect - it averages incompatible exposure models and outcome "
     "definitions across too few studies. Relevance: low-moderate - the NO2 > PM2.5 ordering points at traffic "
     "proximity, which a dense network resolves better than satellite PM2.5.")),
 dict(pmid="42889153", doi="10.3389/fpubh.2026.1936760", journal="Front Public Health",
  short="Lu PM2.5 longevity country panel specification analysis 2026",
  title="Paradoxical PM2.5-longevity estimates in global country panels are sensitive to differential trend control: a specification analysis, 2000-2023",
  sub=corpus.BURD, design="Ecological panel, fixed effects", pm="Population-weighted annual ambient PM2.5 (World Bank WDI)",
  geo="Global / multi-region (186 economies)", endpoint="Life expectancy at birth", tier="B",
  n=("4,406 country-years, two-way fixed effects with GDP, health spending and urbanisation. The conventional model "
     "gives a paradoxical +0.406 y life expectancy per 10 ug/m3 PM2.5 (0.144-0.668); economy-specific linear trends "
     "remove it (-0.023 y, -0.175 to 0.129), as do first differences (-0.006 y, -0.085 to 0.073). A future-exposure "
     "lead (+2 y) was positive alone (0.296, 0.042-0.549) but attenuated with current exposure. Limitation: the "
     "trend-adjusted estimates are null rather than negative, so the paper diagnoses bias without recovering the "
     "expected harm; national averaging discards almost all exposure contrast. Relevance: moderate - a methods "
     "warning for any ecological PM2.5 panel, including those fed by sensor-network or satellite exposure surfaces.")),
]
