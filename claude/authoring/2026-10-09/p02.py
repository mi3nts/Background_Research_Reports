# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="", doi="10.1080/02786826.2026.2726892", journal="Aerosol Sci Technol",
  short="Malik MPSS calibration 2026",
  title="Traceable calibration of MPSS in fast-scan mode: Recommendations for PNSD measurement at urban traffic hot spots",
  sub=corpus.SENS, design=MO,
  pm="Metadata only - traceable calibration of mobility particle size spectrometers in fast-scan mode (by title)",
  geo="Not stated (calibration method)", endpoint=NA, tier="A",
  n=("Metadata-only record: title, authors and DOI deposited 9 Oct with no abstract. By title, a "
     "metrology-grade calibration route for MPSS/SMPS operated in fast-scan mode, with recommendations "
     "for particle number size distribution at traffic hot spots. Fast scans trade sizing accuracy for "
     "time resolution - the scan-direction smearing and DMA transfer-function errors that dominate when "
     "concentrations change faster than a scan are the reason roadside PNSD is rarely comparable across "
     "sites. Relevance: high - a traceable reference for sub-100 nm number is the missing anchor for any "
     "UFP sensor co-location; on the abstract-retry list.")),

 dict(pmid="", doi="10.5194/acp-26-14165-2026", journal="Atmos Chem Phys",
  short="Petrovic Belgrade PMF 2026",
  title="Chemical characterization and source apportionment of PM10 in Belgrade, Serbia: influence of local and regional anthropogenic and natural sources",
  sub=corpus.EXPO, design="Source apportionment",
  pm="PM10 with 34 species (OC/EC, elements, ions, organic tracers), PMF 5.0",
  geo="Serbia (Belgrade urban background)", endpoint="None (source contributions)", tier="B",
  n=("USEPA PMF 5.0 on PM10 at an urban-background site using 34 inputs including organic tracers - "
     "broader than earlier Belgrade apportionments that used elements or ions alone. Biomass burning "
     "leads at 21% of PM10, concentrated in the heating season, then ammonium sulphate 18%, mineral dust "
     "17% and mixed traffic/industry 15%, with primary biological and biogenic secondary factors "
     "resolved separately. Limitation: one site, and a mixed traffic-industry factor means PMF could not "
     "separate the two sources most amenable to local control; PM10 mass weighting under-represents the "
     "fine combustion fraction that drives health effects. Relevance: moderate - a 21% residential "
     "biomass share in a Balkan capital is the case where low-cost optical networks track the winter "
     "smoke signal well but need composition-aware RH correction.")),

 dict(pmid="", doi="10.20944/preprints202610.0209.v1", journal="Preprints.org (preprint)",
  short="Dayare Navi Mumbai 2026",
  title="Weather, Co-Pollutants and Daily PM2.5 in a Coastal Indian City: Multi-Station Evidence for Meteorology-Triggered Air-Quality Warnings in Navi Mumbai",
  sub=corpus.SENS, design="Monitoring-record analysis",
  pm="Daily PM2.5 at five CAAQMS stations (2021-2025), hourly at two; ERA5 checked against radiosonde",
  geo="India (Navi Mumbai)", endpoint="None (forecast / warning skill)", tier="B",
  n=("VAR models with exogenous weather on screened, unimputed station data. Lagged co-pollutants add "
     "little: equivalence tests bound six of seven effects within +/-5% per SD; lagged ozone raises "
     "PM2.5 by 4%. Rain and boundary-layer height lower same-day PM2.5 by 10-24% per SD; date effects "
     "shared across stations explain 78% of variance, three-quarters of it weather. A stagnation index "
     "plus persistence warns as well as XGBoost, which does not beat persistence. Limitation: a "
     "preprint; ERA5 boundary-layer height over a coastal city is coarse, and five stations limit the "
     "spatial claim. Relevance: high - a clean demonstration that 'driver' inference from co-movement "
     "is weather confounding, and that persistence is the baseline any network forecast must beat.")),

 dict(pmid="", doi="10.21203/rs.3.rs-10864736/v1", journal="Research Square (preprint)",
  short="Rodriguez Bogota car-free 2026",
  title="Annual trends in ambient particulate matter during car free days in Bogota from 2016 to 2025",
  sub=corpus.BURD, design="Monitoring-record analysis",
  pm="PM2.5 and PM10 on Car-Free Day from the city monitoring network, 2016-2025 (2021 excluded)",
  geo="Colombia (Bogota)", endpoint="None (concentration trend)", tier="C",
  n=("Nine annual Car-Free Day observations from the regulatory network, OLS and weighted regressions with "
     "2,000-replicate bootstrap. PM10 fell significantly, slope -4.04 ug/m3 per year (weighted bootstrap "
     "CI -6.49 to -0.81), median change -41.8%; PM2.5 trend was -1.72 ug/m3 per year (CI -3.17 to 0.40), "
     "not significant. Limitation: n = 9 single days with no control days, so the trend is the city's "
     "background trend plus that day's weather - it says nothing about the effect of the car-free "
     "intervention itself. Relevance: low-moderate - the right design (Car-Free Day minus matched "
     "control days, by station) is one that a dense sensor network could deliver at street scale.")),
]
