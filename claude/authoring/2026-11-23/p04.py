# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-23/_src.py", encoding="utf-8").read())
NO = "Metadata only: no abstract was retrievable from the harvest legs or Crossref at issue time. "
P = [
 R(57, tier='B', basis='Lab / research instrument', sub=corpus.OCC,
  short='Residential mechanical ventilation with SMPS-verified artificial PM2.5: 30T HEPA reaches 94.4-98.8% removal; replacement interval ~526 days (395-789) as an upper bound',
  design='Laboratory measurement', pm='Artificially generated PM2.5 verified by SMPS; whole-unit removal by filter type and thickness, with accelerated ageing',
  geo='Not stated', endpoint='Whole-system PM2.5 removal efficiency, reduction time and filter service life',
  n="Laboratory tests of whole residential ventilation units rather than filters alone, using dust-collection filters of several types and thicknesses challenged with artificial PM2.5 whose size distribution was verified by SMPS. A reduction-time model predicts the time to remove PM2.5 given indoor generation. A 30T HEPA filter achieved 94.4-98.8% PM2.5 mass removal; accelerated ageing gave an estimated replacement interval of about 526 days (395-789) under the 2024 ambient PM2.5 distribution, stated as an upper bound. Weakness: artificial aerosol and laboratory conditions omit real infiltration, occupant sources and humidity loading of filters. Relevance: moderate - ventilation-unit performance is what in-home low-cost sensors are increasingly used to verify in the field."),
 R(49, tier='C', basis='Review / no primary exposure', sub=corpus.BURD,
  short='Latin America and Caribbean air-pollution literature 2015-2025, 6,355 papers: attention scales sublinearly with burden (slope 0.72, 0.52-0.91); under-represented countries carry 30% of burden with 5% of attention',
  design='Scoping review', pm='Bibliometric mapping of PM2.5-centred air-pollution research; burden compared with research attention by country',
  geo='Latin America', endpoint='Research attention vs burden, themes and collaboration structure',
  n="Systematic Scopus and Web of Science search with regex plus LLM screening (94% agreement with author labels; ~80.5% relevance among retained records) yielding 6,355 LAC air-pollution publications, 2015-2025. Annual publications rose 83% (389 to 713); five countries held 82.7% of country mentions. Research attention tracked burden sublinearly (log-log slope 0.72, 95% CI 0.52-0.91, R2 0.64); under-represented countries carried 30% of burden but 5% of attention. Five themes centred on PM2.5 and health. Intra-LAC collaboration (9.4%) was about four times rarer than partnership with external, mostly high-income, institutions (38.0%). Weakness: LLM screening with ~20% irrelevant retained records and Scopus/WoS coverage that under-indexes Spanish- and Portuguese-language venues. Relevance: identifies where low-cost networks would add the most evidence per dollar."),
 R(24, tier='B', sub=corpus.EXPO,
  short='Crop-residue burning timing, PM2.5 and population exposure in Northeast China from Himawari-constrained CMAQ (per title)',
  design='Metadata only: no abstract in Crossref at issue time', pm='Not stated (title names Himawari-constrained CMAQ simulations of PM2.5)',
  geo='China (Northeast)', endpoint='PM2.5 and population exposure by timing of crop-residue burning (per title)',
  n=NO + "The record (Atmospheric Environment; Yang, Chen, Li, Li) uses Himawari-constrained CMAQ simulations to relate the timing of crop-residue burning to PM2.5 and population exposure in Northeast China. No finding, emission estimate or exposure figure is asserted here. Relevance: moderate - geostationary fire constraints on a CTM are the satellite half of the satellite-surface fusion problem; seasonal burning is where sparse regulatory networks miss rural peaks."),
 R(40, tier='C', sub=corpus.EXPO,
  short='Wintertime black-carbon variability and potential source regions at Aizawl, Northeast India (per title)',
  design='Metadata only: no abstract in Crossref at issue time', pm='Black carbon (title); instrument and period not available',
  geo='India (Aizawl, Mizoram)', endpoint='Black-carbon variability and source regions (per title)',
  n=NO + "The record (Science of The Total Environment; Gurung, Hazarika, Ranjan, Gupta) reports wintertime black-carbon variability and potential source regions over Aizawl in Northeast India. No concentration, source apportionment or instrument is asserted here. Relevance: low-moderate - an under-monitored hill region where BC is likely transported from biomass burning upwind."),
]
