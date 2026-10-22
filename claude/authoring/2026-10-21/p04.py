# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1021/acs.est.6c07635", journal="Environ Sci Technol",
  short="Du Air Health Index acute myocardial infarction 325 cities 2026",
  title="Establishing an Air Health Index for Predicting the Risk of Acute Myocardial Infarction Onset Associated with Air Pollution and Ambient Temperature",
  sub=corpus.CVM, design="Health impact model", pm="Daily PM2.5 (with NO2, O3, temperature) from high-resolution surfaces",
  geo="China (325 cities)", endpoint="AMI onset; composite Air Health Index (0-10+)", tier="A",
  n=("1,207,625 AMI cases across 325 Chinese cities; excess risks from PM2.5, NO2, O3 and temperature aggregated into a "
     "normalised AHI. Per IQR, AHI associated with +5.97% (5.32-6.63%) AMI incidence vs +3.33% (2.93-3.72%) for AQHI and "
     "+2.04% (1.73-2.35%) for AQI; near-linear, no threshold; validated on an independent external dataset; 8,534 per "
     "100,000 AMI cases attributed. Limitation: the index is fitted to the same outcome it is scored on, so in-sample "
     "superiority over AQI/AQHI is expected; IQR-scaled comparisons across indices with different distributions are not "
     "like-for-like, and 'attributable' fractions for a composite that includes temperature mix avoidable and "
     "non-avoidable risk. Relevance: high - an outcome-weighted index is a natural output layer for real-time LCS "
     "networks, provided the PM2.5 input is calibrated.")),
 dict(pmid="", doi="10.1021/acs.est.6c08602", journal="Environ Sci Technol",
  short="Zhang respirable magnetite emissions coal-fired power China 2026",
  title="Emissions of Respirable Magnetite from the Coal-Fired Power Sector in China: Spatial Inequalities and Mitigation Pathways",
  sub=corpus.BURD, design="Emission inventory", pm="Respirable magnetite (Fe3O4) particle emissions",
  geo="China (national, provincial)", endpoint="Annual magnetite emission and mitigation scenarios", tier="B",
  n=("Multifactor emission model for respirable magnetite from Chinese coal-fired power: 2,828.7 (2,307.1-3,371.4) t/y, "
     "spatially concentrated by tiered emission standards. Guizhou and Sichuan supply 4% of coal power but tightening "
     "their standards alone would cut >31% of national magnetite emissions. Limitation: emission factors for magnetite "
     "specifically (as opposed to total PM or Fe) rest on few stack measurements, and the uncertainty interval looks "
     "narrow for a species-level inventory; health relevance is asserted from brain-magnetite literature rather than "
     "exposure-response data. Relevance: moderate - magnetite is invisible to optical LCS mass; magnetic or "
     "filter-based speciation would be needed to verify hotspots.")),
 dict(pmid="", doi="10.1016/j.apr.2026.103244", journal="Atmos Pollut Res",
  short="Ghaffarpasand Pope vehicle remote sensing real-world emissions high emitters 2026",
  title="Emerging Evidence on Real-World Exhaust Emissions and High Emitting Vehicles from Remote Sensing Observations",
  sub=corpus.SENS, design="Metadata only (no abstract)", pm="On-road remote sensing of exhaust (pollutants not stated in record)",
  geo="Not stated (review)", endpoint="Real-world exhaust emission factors; high-emitter identification", tier="C",
  n=("Title and authors only (Ghaffarpasand, Pope); no abstract at harvest. Appears to synthesise vehicle emission "
     "remote-sensing (VERSS) evidence on real-world exhaust and high emitters. Whether PM/smoke opacity or only NOx/CO/HC "
     "is covered cannot be stated. Limitation: unverifiable beyond the title; VERSS PM is inferred from UV opacity "
     "with large per-pass uncertainty, and single-pass snapshots overweight hot-running conditions. Relevance: moderate "
     "- high-emitter fractions explain the kerbside spikes roadside LCS record but cannot attribute.")),
 dict(pmid="", doi="10.21203/rs.3.rs-11381994/v1", journal="Research Square (preprint)",
  short="Idowu medical waste incinerator airborne heavy metals Monte Carlo Nigeria 2026",
  title="Monte Carlo-Based Probabilistic Health Risk Assessment of Airborne Heavy Metals from a Medical Waste Incinerator in Southwestern Nigeria",
  sub=corpus.BURD, design="Health impact model", pm="PM-bound heavy metals (passive glass-slide deposition samplers)",
  geo="Nigeria (Ido-Ekiti)", endpoint="Inhalation HQ and ILCR distributions", tier="C",
  n=("Particulate matter collected on passive glass slides around a medical-waste incinerator for two months; ten metals "
     "analysed, converted to airborne concentrations, and propagated through 10,000 Monte Carlo draws. Median HQ ~400, "
     "95th percentile 850; exceedance probability near 100%; ILCR above benchmarks. Limitation: passive deposition slides "
     "measure settled mass, not airborne concentration - the conversion to C_air requires an assumed deposition velocity "
     "that dominates the result, and an HQ of 400 almost certainly reflects that conversion rather than real inhalation "
     "dose. Preprint. Relevance: moderate as a cautionary example - fence-line LCS or low-volume samplers would have given "
     "a defensible air concentration.")),
]
