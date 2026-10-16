# -*- coding: utf-8 -*-
P = [
 dict(pmid="42859288", doi="10.1007/s40572-026-00566-2", journal="Curr Environ Health Rep",
  short="Fang LCS calibration review 2026",
  title="Calibration of Low-Cost Particulate Matter Sensors for Exposure Assessment: A Critical Review",
  sub=corpus.SENS, design="Systematic review (PRISMA)",
  pm="Calibrated R2 and RMSE of low-cost PM sensors against reference instruments, laboratory vs field",
  geo="Global (66 studies, 2015-2025)", endpoint="None (measurement performance)", tier="A",
  n=("Sixty-six studies, 32 laboratory evaluations and 34 field studies. Median calibrated R2 was "
     "0.92 (n = 31) in the laboratory against 0.72 (n = 29) in the field, and median RMSE 2.6 ug/m3 "
     "(n = 7) against 12.3 ug/m3 (n = 9) - a factor of nearly five in error on crossing from bench to "
     "deployment. The authors are explicit that these are summaries of a heterogeneous literature, not a "
     "pooled effect: aerosol mixture, comparison instrument, concentration range, averaging interval and "
     "validation design all differ. RH and temperature were handled in most studies; ML and hybrid models "
     "appear more often in field work and sometimes lower error, but independent validation across time, "
     "place and sensor unit is uneven. Limitation: only 7 and 9 studies reported RMSE at all, so the "
     "headline error figures rest on a small and probably favourable subset. Relevance: high - this is "
     "the reference statement that calibration does not transfer, which is the standing assumption behind "
     "every distributed network claim in this corpus.")),

 dict(pmid="", doi="10.20944/preprints202610.0577.v1", journal="Preprints.org (preprint)",
  short="Fazelvalipour LA microplastics 2026",
  title="Size-Resolved Characteristics and Source Influences of Airborne Microplastics in Central Los Angeles",
  sub=corpus.EXPO, design="Field measurement",
  pm="PM10-associated airborne microplastics (counts/m3, morphology, size) with PM10 composition",
  geo="United States (central Los Angeles)", endpoint="None (concentration and source association)", tier="B",
  n=("Two seasonal campaigns in central Los Angeles: microplastics were in every sample at 2.2-4.0 MP/m3 "
     "(cool season) and 2.2-3.4 MP/m3 (warm), dominated by fibres and by the 5-50 and 50-100 um size "
     "fractions. Total MP correlated strongly (rho >= 0.79) with crustal (Fe, Si, Mn, Ca, Al, Mg), "
     "traffic (Ba, Cu, Ni) and carbonaceous (OC, EC) tracers, while short-term meteorology showed no "
     "consistent relationship, implying MPs travel as part of the resuspended urban particle mixture "
     "rather than as a separate contaminant. Limitation: a preprint; microscopy-based MP counts carry "
     "large operator and blank uncertainty, correlation with crustal tracers is also what resuspension "
     "artefact looks like, and particles under 5 um - the inhalable fraction - are not resolved. "
     "Relevance: moderate-high - supports the same-day tyre-wear argument that the growing non-exhaust, "
     "coarse, resuspended fraction is what networks increasingly measure badly.")),

 dict(pmid="42858206", doi="10.1007/s10661-026-15915-9", journal="Environ Monit Assess",
  short="Chaudhary India meteorology 2026",
  title="Meteorological modulation of ground-level air quality in India based on in situ measurements",
  sub=corpus.EXPO, design="Monitoring-record analysis",
  pm="PM10, PM2.5, O3, NO2, SO2 with PBL height, RH, temperature, precipitation, wind, surface pressure (2017-2024)",
  geo="India (national, Indo-Gangetic Plain focus)", endpoint="None (trend and meteorological modulation)", tier="B",
  n=("Eight years of in-situ measurements across Indian monitoring sites with Sen's slope trends. PM2.5 "
     "fell at several Indo-Gangetic sites (-0.893 to -0.097 ug/m3/month) and PM10 likewise (-1.320 to "
     "-0.169), while Punjab rose on local sources; ozone increased (0.041 to 0.529 ug/m3/month), read as "
     "aerosol inhibition weakening plus more precursors. Declining boundary-layer height and wind speed "
     "over north and east India modulate all of it. Limitation: Sen's slope on eight years of CPCB data "
     "cannot separate emission change from meteorological trend, which is the paper's own point turned "
     "against its trend estimates; station siting and instrument changes over that period are "
     "undocumented. Relevance: moderate - the regional version of the same-day argument that a "
     "concentration trend is not an emissions trend.")),

 dict(pmid="", doi="10.3390/atmos17100993", journal="Atmosphere",
  short="Mukhamediyarov Kazakhstan code 2026",
  title="Air Quality and Emission Trends Following the 2021 Environmental Code Reform in Kazakhstan Across Regions and Industrial Sectors",
  sub=corpus.BURD, design="Monitoring-record analysis",
  pm="Stationary-source emissions (PM2.5, SO2, CO, NO2) and ambient indicators by region and sector",
  geo="Kazakhstan (national)", endpoint="None (policy evaluation)", tier="B",
  n=("A before-and-after comparison of Kazakhstan's 2021 Environmental Code reform, which tightened "
     "standards and pushed Best Available Techniques. Reported stationary-source emissions fell roughly "
     "5-6% between 2021 and 2024, but no statistically significant improvement in assessed ambient "
     "indicators appeared between 2021 and 2025, and episodic PM exceedances persisted in several "
     "cities. Limitation: no control region and no counterfactual, so the null is as much about the "
     "design as about the policy; reported emissions are self-declared inventory, and the ambient "
     "network is sparse enough that a 5% emission change would be undetectable even if real. Relevance: "
     "moderate - a clean example of why policy evaluation needs measurement density the regulatory "
     "network does not have; the 7 October congestion-pricing record is the version that had it.")),
]
