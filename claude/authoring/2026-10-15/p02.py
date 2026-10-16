# -*- coding: utf-8 -*-
P = [
 dict(pmid="42877354", doi="10.3389/fpubh.2026.1945362", journal="Front Public Health",
  short="SEARO air-quality early-warning review 2026",
  title="Prediction accuracy of available early warning systems for air pollution across WHO South-East Asia region: a systematic review",
  sub=corpus.SENS, design="Systematic review", pm="Forecast PM2.5 and other pollutants (RMSE, R2, categorical accuracy, bias)",
  geo="South-East Asia (India, Bangladesh, Thailand)", endpoint="No health endpoint", tier="B",
  n=("PROSPERO-registered review (to Feb 2026): 14 modelling studies from 839 records, PROBAST+AI risk-of-bias. Hybrid "
     "deep-learning forecasters reported the lowest RMSE (0.84-4.61 ug/m3) and R2 up to 0.998 for PM2.5; ML reached 98.3% "
     "categorical accuracy; CTMs cut bias ~70% only with satellite data assimilation. Most studies were at high risk of "
     "bias from absent external validation and overfitting; heterogeneity precluded meta-analysis. Limitation: an "
     "R2 of 0.998 for daily PM2.5 is a leakage signature, and the review reports such figures without re-analysis. "
     "Relevance: moderate - operational forecast skill in the region is unproven; LCS networks could provide the "
     "out-of-sample validation these systems lack.")),
 dict(pmid="", doi="10.20944/preprints202610.0819.v1", journal="Preprints.org (preprint)",
  short="Gujral Dominici Memphis datacenter PM2.5 2026",
  title="Behind-the-Meter Versus Grid Electricity for AI Datacenters: Magnitude, Geography, and Equity of PM2.5-Attributable Mortality in Memphis",
  sub=corpus.BURD, design="Health impact model", pm="Modelled population-weighted PM2.5 from on-site turbines vs grid generation",
  geo="United States (Memphis)", endpoint="PM2.5-attributable mortality", tier="A",
  n=("Two datacenters 12 km apart. At a common 240 MW, grid-supplied C1 carried 10.83 attributable deaths/y (95% interval "
     "7.83-13.84) vs 3.67 (2.65-4.68) for behind-the-meter C2; at real/permitted capacities the order reversed, 11.35 "
     "(6.48-17.29) for C2 vs 8.10 (4.60-12.38) for C1. 94% of C1 deaths fell >250 km away; 82% of C2 deaths within 50 "
     "km, concentrated in the low-income, high people-of-colour stratum. Limitation: preprint; permitted capacity is not "
     "operating capacity, and on-site turbine emission factors and the reduced-form dispersion model are the whole "
     "result. Relevance: high - a near-source burden that a local LCS network around the site could verify directly.")),
 dict(pmid="42845222", doi="10.4168/aair.2026.18.5.640", journal="Allergy Asthma Immunol Res",
  short="Yoon pollutant asthma immune mechanisms review 2026",
  title="Impacts and Immune Mechanisms of Pollutant-Mediated Asthma and Airway Inflammation",
  sub=corpus.RESP, design="Narrative review", pm="PM, DEP, O3, NO2, SO2, VOCs, bioaerosols",
  geo="Not stated", endpoint="Asthma and airway inflammation (mechanisms)", tier="C",
  n=("Narrative review of epithelial injury, barrier disruption, oxidative stress and innate signalling (NF-kB, MAPK, "
     "PI3K/Akt, inflammasome) driving T2, non-T2 and mixed asthma phenotypes; pollutant-specific arms include PM-induced "
     "NLRP3 activation, O3 barrier disruption, DEP-driven IL-17A and pollutant-allergen co-exposure. Acknowledges that "
     "experimental doses and compositions do not map onto real-world exposure. Limitation: non-systematic, no new data, "
     "and no dose metric that a measurement study could target. Relevance: low - background for mechanism sections.")),
 dict(pmid="42849516", doi="10.1055/a-2977-5555", journal="Thromb Haemost",
  short="GBD 2023 G20 stroke air pollution temperature 2026",
  title="Estimates, temporal evolution, and contributors of the stroke burden due to air pollution and non-optimal temperature across G20 nations, 1990-2023",
  sub=corpus.BURD, design="GBD secondary analysis", pm="GBD ambient PM and household solid-fuel pollution; non-optimal temperature",
  geo="Global / multi-region (G20)", endpoint="Stroke mortality and DALYs", tier="C",
  n=("GBD 2023, G20 nations. Age-standardised stroke mortality attributable to air pollution plus non-optimal "
     "temperature fell from 52.81 to 17.46/100,000 (1990-2023; EAPC -3.44%, 95% CI -3.57 to -3.30); DALY rate EAPC "
     "-3.29%. The decline is driven by household air pollution; ambient PM and heat burdens rose or stalled, highest in "
     "low/middle-SDI members, and ARIMA projections to 2040 keep them flat. Limitation: GBD re-tabulation with joint "
     "attribution of two risk classes; the ARIMA projection adds no exposure information. Relevance: low - confirms that "
     "ambient PM, not household fuel, now carries the residual stroke burden.")),
]
