# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1021/acs.estlett.6c00610", journal="Environ Sci Technol Lett",
  short="NYC congestion pricing 2026",
  title="Attributing PM2.5 and NO2 Changes One Year after New York City's Congestion Pricing Policy",
  sub=corpus.BURD, design="Difference-in-differences evaluation",
  pm="Real-time PM2.5 from the NYC Community Air Survey plus TROPOMI tropospheric NO2 columns",
  geo="USA (New York City)", endpoint="None (policy evaluation)", tier="A",
  n=("The Central Business District Tolling Program began in January 2025; its first year is evaluated "
     "against 2022-2024 with difference-in-differences on NYCCAS real-time PM2.5 and on satellite NO2. "
     "Within the congestion relief zone, PM2.5 fell by 1.44 ug/m3 attributable to the policy (p<0.001), "
     "or 1.33 ug/m3 allowing for spillover, while nearby non-zone sites showed a non-significant 0.50 "
     "ug/m3 rise. Tropospheric NO2 fell over 20% across metropolitan New York against a 2018-2024 "
     "baseline, but only 1.23% was attributable to the programme (p=0.096). Limitation: one treated zone "
     "and one post-period, so the parallel-trends assumption rests on three pre-years; the non-zone "
     "increase is the signal that displacement may be real but underpowered. Relevance: high - a 1.4 ug/m3 "
     "step change across a few square kilometres is exactly the contrast a dense low-cost network resolves "
     "and a regulatory network, here a purpose-built survey, only barely does.")),

 dict(pmid="", doi="10.1021/acs.est.6c12227", journal="Environ Sci Technol",
  short="US vehicle emission burden 2026",
  title="Spatially Refined Analysis of Emission Burdens and Equity from Light-, Medium-, and Heavy-Duty Vehicle Traffic in the United States",
  sub=corpus.BURD, design="Modelling / inventory",
  pm="Census-block NOx and PM2.5 emission intensity from MOVES factors and street-level traffic, exhaust vs tyre/brake wear",
  geo="USA (national, every census block)", endpoint="None (emission burden and equity)", tier="A",
  n=("Block-level on-road emission intensities for the whole United States. Medium- and heavy-duty trucks "
     "are under 11% of vehicle kilometres but 46% of NOx and 50% of PM2.5 emission burden; truck PM2.5 is "
     "exhaust-dominated while tyre and brake wear are nearly half of light-duty PM2.5. People of colour "
     "face burdens averaging 40% above the national mean (Asian populations over 60%), lower-income "
     "populations 20-25% higher, with significant disparities in 85-89% of counties, rural as well as "
     "urban. Critically, spatial aggregation attenuates the measured disparity. Limitation: this is an "
     "emission-intensity metric, not a concentration or an exposure - no dispersion, no background, no "
     "infiltration - so it cannot be read as an inhaled dose. Relevance: high - the aggregation result is "
     "the quantitative case for network density: resolution is not cosmetic, it determines whether a "
     "disparity is visible at all.")),

 dict(pmid="42840506", doi="10.1016/j.eehl.2026.100283", journal="Eco Environ Health",
  short="BC outpatient risk 2026",
  title="Black carbon as a major contributor to ambient PM2.5-related cause-specific outpatient risks: implications for early warning and health benefits evaluation of air quality improvement",
  sub=corpus.BURD, design="Time-stratified case-crossover",
  pm="Daily PM2.5 and constituents (black carbon, organic matter, sulfate, nitrate, ammonium), 274 cities",
  geo="China (274 cities)", endpoint="Cause-specific outpatient visits, 12 disease groups", tier="A",
  n=("Over 212 million daily outpatient records, 2013-2017, with conditional logistic regression per city "
     "pooled by random effects and three complementary models testing constituent independence. Black "
     "carbon carried the strongest independent associations, and at lag0 rather than the lag0-1 typical of "
     "admissions: per IQR (1.8 ug/m3) increases ranged from 1.33% (0.93-1.74) for chronic kidney disease "
     "to 3.89% (3.30-4.49) for COPD, attributable fractions 2.38% to 6.12%. Both PM2.5- and BC-attributable "
     "burdens fell substantially after the 2013 clean-air programme. Limitation: constituents come from a "
     "modelled reanalysis and are collinear; outpatient visits are supply-sensitive, and the lag0 finding "
     "could reflect care-seeking on visibly bad days rather than a faster biological response. "
     "Relevance: high - BC is measurable by low-cost aethalometry, and a same-day constituent signal is "
     "the one an operational early-warning network could actually act on.")),

 dict(pmid="42843063", doi="10.1016/j.ijheh.2026.114923", journal="Int J Hyg Environ Health",
  short="Children's AIRE 2026",
  title="Ambient particulate matter exposure and children's blood pressure in rural California, 2019-2022",
  sub=corpus.CVM, design="Prospective cohort",
  pm="12-month and 7-day PM2.5 and PM10 from regulatory monitors linked to residence",
  geo="USA (rural California)", endpoint="Systolic and diastolic blood pressure", tier="B",
  n=("592 children aged 6-8 at enrolment, blood pressure measured up to five times through spring 2022, "
     "linear mixed models. An IQR increase (38 days) in prior-year days above 50 ug/m3 daily PM10 was "
     "associated with +1.1 mmHg DBP (95% CI 0.8, 1.5) and +0.9 mmHg SBP (0.3, 1.5); the top quartile of "
     "short-term PM2.5 and PM10 carried 5.8 (0.4, 11.2) and 5.9 (0.2, 11.6) percentage-point higher risk "
     "of elevated or hypertensive SBP against the lowest quartile. Limitation: exposure comes from "
     "regulatory monitors in a rural region where the nearest monitor can be tens of kilometres away and "
     "agricultural and wildfire sources are highly local, so non-differential misclassification is large "
     "and almost certainly biases toward the null; paediatric BP is noisy across visits. Relevance: high - "
     "this is the archetypal study whose exposure term a rural low-cost network would transform, and the "
     "'days above threshold' metric suits an inexpensive, lower-accuracy node better than an annual "
     "mean does.")),
]
