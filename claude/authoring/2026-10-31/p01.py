# -*- coding: utf-8 -*-
P = [
 dict(pmid="42964290", doi="10.3389/fpubh.2026.1777772", journal="Front Public Health",
  short="Zhang short-term air pollution stroke incidence Guiyang karst city 2026",
  title="Time-series analysis of the impact of short-term exposure to atmospheric pollutants on stroke risk among residents in Guiyang City, 2016-2021",
  sub=corpus.CVM, design="Time-series (generalized additive model)", pm="Daily fixed-site PM2.5 and PM10 (city mean), with SO2, NO2, O3, CO",
  geo="China (Guiyang)", endpoint="Daily stroke incidence (registry)", tier="A",
  n=("Guiyang 2016-2021, 11,517 incident strokes (5.25/day), quasi-Poisson GAM with single-day and cumulative lags, "
     "controlling trend, weather, day-of-week and holidays. Per 10 ug/m3 at the maximal lag: PM2.5 RR 1.026 "
     "(1.005-1.048), PM10 1.015 (1.001-1.030); SO2 1.075, NO2 1.057, CO 1.346 per mg/m3. Women and adults >=65 carried "
     "more of the risk; under-65s responded only to NO2 and PM10. Limitation: single-pollutant models with the lag "
     "chosen at the maximum inflate the PM coefficients, co-pollutant collinearity is unaddressed, and the stroke "
     "series does not split ischaemic from haemorrhagic. Relevance: moderate - a low-concentration karst basin is "
     "where fixed-site averaging hides terrain-driven gradients that a dense low-cost network would resolve.")),
 dict(pmid="42965015", doi="10.1016/j.ghrp.2026.04.002", journal="Glob Health Res Policy",
  short="Wang climate air pollutants influenza 48 countries convergent cross mapping 2026",
  title="Delayed and nonlinear associations and predictive causal signals between climate factors, air pollutants, and influenza epidemics in 48 countries",
  sub=corpus.RESP, design="Bayesian spatiotemporal model", pm="Weekly cumulative SO2, organic carbon and dust PM2.5 (gridded; source not stated in abstract)",
  geo="Global (48 countries)", endpoint="Weekly influenza positivity (FluNet)", tier="B",
  n=("48 countries, 2022-2024; FluNet weekly positivity against national climate and pollutant series in "
     "hemisphere-specific Bayesian distributed-lag models, then convergent cross mapping (CCM) for 'predictive causal' "
     "drivers. Northern Hemisphere peak OR 1.74 (1.34-2.26) at weekly cumulative SO2 3100 ug/m3, lag 1.6 weeks; Southern "
     "peak for organic carbon OR 1.72 (0.65-4.58), null. CCM ranked dust PM2.5 the leading pollutant driver (19 "
     "countries). Limitation: national-level exposure against surveillance positivity is fully ecological; "
     "three post-pandemic seasons cannot separate pollution from NPI relaxation, and CCM detects shared dynamics, not "
     "causation. Relevance: low - surveillance-scale; dust PM2.5 is a size fraction low-cost optical sensors undercount.")),
 dict(pmid="42965991", doi="10.1016/j.chroma.2026.467564", journal="J Chromatogr A",
  short="Bei UPLC-MS/MS 74 antibiotics in PM2.5 Beijing 2026",
  title="Optimization and application of a sensitive UPLC-MS/MS method for the quantitative determination of antibiotics in PM2.5",
  sub=corpus.SENS, design="Analytical method validation", pm="Filter-collected 24 h PM2.5, 74 antibiotics by SPE + UPLC-MS/MS",
  geo="China (Beijing)", endpoint="Airborne antibiotic concentration (method validation)", tier="B",
  n=("Method for 74 antibiotics in PM2.5: T3 column, formic-acid mobile phase, Oasis HLB extraction with Na2EDTA. "
     "Recoveries 69.7-131.7%, RSD 1.0-18.1% at three spike levels, quantification limits down to 0.37 pg/m3. On 29 "
     "Beijing 24-h samples, 22 compounds exceeded detection limits (max 121.38 pg/m3); roxithromycin was in every sample "
     "and oxytetracycline had the highest mean (14.48 pg/m3). Limitation: 29 samples from one city and season give "
     "occurrence, not exposure; recoveries near 70% for some classes bias low, and the link to resistance spread is "
     "asserted, not tested. Relevance: low for sensing - a filter-bound chemical fraction no optical sensor sees, but "
     "co-located filter sampling at sensor nodes could support it.")),
]
