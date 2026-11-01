# -*- coding: utf-8 -*-
P = [
 dict(pmid="42957834", doi="10.1007/s10661-026-16067-6", journal="Environ Monit Assess",
  short="Schmidt AOD gap filling iterative singular spectrum analysis AERONET Cuiaba 2026",
  title="Gap filling in long-term AOD time series using Iterative Singular Spectrum Analysis at a tropical AERONET site",
  sub=corpus.SENS, design="Method / algorithm", pm="AERONET daily aerosol optical depth",
  geo="Brazil (Cuiaba-Miranda, Mato Grosso)", endpoint="Reconstruction error of gap-filled AOD series", tier="C",
  n=("Applies iterative singular spectrum analysis (ISSA) to fill a 2005-2024 daily AOD record from the Cuiaba-Miranda "
     "AERONET station, where ~47% of days are missing, mostly in the cloudy wet season. Climatological (day-of-year mean) "
     "initialisation beat global-mean initialisation, giving lower error and better temporal consistency, and the "
     "cross-validation design materially changed the optimal reconstruction parameters. No error magnitudes are "
     "given in the abstract. Limitation: gaps are not missing at random - they coincide with cloud and wet-season "
     "aerosol regimes - so a climatology-anchored fill will bias toward dry-season behaviour exactly where data are "
     "absent. Relevance: low-medium - the same informative-missingness problem affects sensor networks with "
     "humidity-triggered dropouts and satellite-surface fusion.")),
 dict(pmid="", doi="10.1021/acs.est.6c09700", journal="Environ Sci Technol",
  short="Chakraborty fog intensity droplet size aqueous SOA Kanpur 2026",
  title="Fog Intensity and Droplet Size-Resolved Aqueous Secondary Organic Aerosol (aqSOA) Formation in Polluted Winter Fog: New Insights from a Combined Observational and Modeling Study",
  sub=corpus.EXPO, design="Field campaign", pm="Size-resolved fogwater, offline HR-AMS with PMF; ambient OA",
  geo="India (Kanpur)", endpoint="Aqueous SOA mass and share of ambient SOA/OA", tier="C",
  n=("Two winters of size-resolved fogwater at Kanpur analysed by offline HR-AMS and PMF; three highly oxidised factors "
     "(O/C 0.95-1.19) were summed as an aqSOA proxy and scaled by liquid water content and WSOC. Across seven events "
     "aqSOA was 3.1-8.4 ug/m3, a median ~7% of ambient SOA and 5% of OA, up to 13% of SOA in the densest fogs. Fine "
     "droplets carried 43-84% of aqSOA, linked to dissolved Fe and Cu and longer residence. Limitation: the aqSOA proxy "
     "is a PMF construct, and offline AMS of fogwater may not represent residual particle mass after evaporation. "
     "Relevance: medium - Indo-Gangetic fog episodes are when optical PM sensors fail outright from droplet "
     "interference, while secondary mass is being added.")),
 dict(pmid="", doi="10.3390/atmos17111072", journal="Atmosphere",
  short="Wang carbon footprint air-pollutant emissions Beijing 2022 Winter Olympics 2026",
  title="Linking Carbon Footprints to Air-Pollutant Emissions from Mega Sporting Events: Evidence from the Beijing 2022 Winter Olympics",
  sub=corpus.BURD, design="Emission inventory", pm="Co-emitted PM2.5, NOx, SO2, CO, NMVOC from pollutant-to-CO2 ratios",
  geo="China (Beijing)", endpoint="Event-attributable air-pollutant emissions and avoided emissions", tier="C",
  n=("Screening-level inventory converting the verified 713,788 t CO2e footprint of the Beijing 2022 Winter Olympics "
     "(2016-2022) into co-emitted pollutants via Chinese pollutant-to-CO2 ratios over eight emission carriers, with "
     "Shapley attribution and Monte Carlo/Sobol uncertainty. Construction produced 63% of CO2e, ~70% of 1,335 t NOx and "
     "76% of 279 t PM2.5. Green electricity avoided 31% of no-measure emissions; offsets reduced no air pollutant. "
     "Limitation: emission-side only - ratio-based PM2.5 with no dispersion, concentration or exposure step, so there "
     "is no health quantity, and national average ratios may misstate construction-site fugitive dust. Relevance: low - "
     "construction dust is the source class that site-perimeter low-cost PM monitoring is typically deployed to police.")),
 dict(pmid="42962468", doi="10.1016/j.ecoenv.2026.120952", journal="Ecotoxicol Environ Saf",
  short="He FOXM1 lncRNA COPD-R biomass PM2.5 pulmonary inflammation rat 2026",
  title="FOXM1/LncRNA COPD-R regulates pulmonary inflammation in chronic obstructive pulmonary disease induced by biomass-related PM2.5",
  sub=corpus.MECH, design="Animal + in vitro", pm="Biomass-fuel smoke (rats, 7 months) and biomass-related PM2.5 (L2 cells)",
  geo="China (inferred from author group; laboratory)", endpoint="lncRNA expression and inflammatory mediators (CCL2, IL-17F, MMP-9, TIMP-1)", tier="C",
  n=("Rats exposed to biomass-fuel smoke for seven months developed COPD-like disease; lung RNA-seq found 312 "
     "differentially expressed lncRNAs (294 up). lncRNA COPD-R rose from 0.15 to 1.05 (relative expression, p<0.01). In "
     "rat L2 alveolar cells, biomass-related PM2.5 increased COPD-R; knockdown reduced PM-induced CCL2, IL-17F, MMP-9 "
     "and TIMP-1, and ChIP/luciferase assays placed FOXM1 upstream as its transcriptional activator, with rescue "
     "experiments consistent with a FOXM1-COPD-R axis. Limitation: whole-smoke exposure in vivo but PM2.5 only in vitro, "
     "dose not reported in the abstract, and a rat lncRNA whose human orthologue is not established. Relevance: low - "
     "mechanistic support for household biomass PM, where the exposure gap is measurement in homes.")),
]
