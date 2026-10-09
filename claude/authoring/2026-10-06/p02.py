# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="42837936", doi="10.1016/j.marpolbul.2026.120437", journal="Mar Pollut Bull",
  short="Loh et al. 2026",
  title="Seasonal characteristics of submicron aerosols in the coastal atmosphere of southeastern Korea: Influence of urban-port outflow",
  sub=corpus.SENS, design="Long-term field measurement campaign",
  pm="PM1 mass, composition and size distribution by HR-ToF-AMS, four seasons, with PMF",
  geo="South Korea (Geoje Island, downwind of Busan)", endpoint="None (aerosol characterisation)", tier="B",
  n=("Seasonal HR-ToF-AMS measurement at a coastal receptor site southwest of Busan, winter 2021 to autumn "
     "2022. PM1 ranged 4.23-10.0 ug/m3; PMF resolved five organic factors including hydrocarbon-like, "
     "oxidised primary (OPOA), two oxygenated and biomass-burning. Ultrafine growth events were frequent, "
     "most in autumn, when OPOA reached 36% alongside elevated black carbon under north-easterly transport "
     "from the port. Limitation: one receptor site with no upwind reference, so 'port influence' rests on "
     "wind sector rather than on a source-resolved tracer, and AMS does not measure refractory sea salt or "
     "dust - the submicron mass is non-refractory by construction. Relevance: high - growth events at "
     "4-10 ug/m3 of mass are invisible to a mass-reporting network, which is the recurring theme of this "
     "week's issues.")),

 dict(pmid="", doi="10.5194/acp-26-14015-2026", journal="Atmos Chem Phys",
  short="Dai et al. 2026",
  title="Cross-phase partitioning of sulfur-nitrogen ratios and aerosol mixing-state evolution based on single-particle observations",
  sub=corpus.SENS, design="Long-term field measurement campaign",
  pm="Single-particle aerosol mass spectrometry with gas-, particle- and number-based S/N ratios",
  geo="China (Yangzhou, eastern China)", endpoint="None (aerosol chemistry)", tier="B",
  n=("SPA-MS through winter and summer emission-control periods and matched normal periods, with three "
     "sulfur-to-nitrogen metrics (gas gSNR, particle pSNR, number-based nSNR) analysed by causal inference "
     "plus interpretable machine learning. Control periods cut NOx while SO2 stayed roughly flat, raising "
     "gSNR, lifting pSNR by about 57% across particle classes and expanding mean vacuum aerodynamic "
     "diameter by 27%; enrichment was greatest in particles containing both black and organic carbon and "
     "least in BC-free inorganic particles. Limitation: emission-control periods are confounded with "
     "season and meteorology, and 'causal inference' on an observational time series with co-varying "
     "controls is a strong label for what remains an association. Relevance: high - a 27% diameter shift "
     "under a control policy is a direct change in the optical cross-section a nephelometric sensor "
     "measures, i.e. a calibration drift caused by policy rather than by hardware.")),

 dict(pmid="", doi="10.21203/rs.3.rs-10517753/v1", journal="Research Square (preprint)",
  short="Zhao et al. 2026e",
  title="Thermal-oxygen evolution and atmospheric pollutant emission characteristics during the vertical propagation of underground coal fires",
  sub=corpus.BURD, design="Chamber / laboratory",
  pm="PM2.5, PM10 and TSP with CO2, CO, CH4 and C2H6 through a simulated burn cycle",
  geo="China (laboratory, physical similarity simulation)", endpoint="None (emissions)", tier="C",
  n=("A scaled physical-similarity rig run from ignition to burnout with continuous monitoring at six "
     "depths. Thermal-oxygen evolution split into incubation, rapid heating, intensive reaction, rapid "
     "cooling and burnout; the upper layers burned out while the middle sustained reaction and the deepest "
     "was oxygen-limited; surface response lagged the seam. Particulate matter and light hydrocarbons were "
     "released early (CH4 and C2H6 concentrated in the first 40-60 h, at background by ~80 h) while CO2 "
     "and CO dominated later. Limitation: a similarity-scaled rig reproduces sequence, not magnitude - "
     "emission factors from it cannot be transferred to a real coal fire, and no scaling validation is "
     "offered; preprint. Relevance: moderate - the early-PM, late-CO sequence is a usable detection "
     "signature for surface sensor arrays over suspected underground fires.")),

 dict(pmid="", doi="10.1016/j.atmosenv.2026.122398", journal="Atmos Environ",
  short="Wang et al. 2026d",
  title="Physics-inspired inductive spatiotemporal kriging for PM2.5 with satellite gradient constraints",
  sub=corpus.EXPO, design=MO,
  pm="Metadata only - inductive spatiotemporal kriging for PM2.5 under satellite gradient constraints (by title)",
  geo="Not recoverable from metadata", endpoint=NA, tier="A",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 6 Oct with no abstract. By title, "
     "this is the central methodological problem of a sparse network - interpolating to unmonitored "
     "locations - attacked inductively (so that new sensors can be added without retraining) and "
     "constrained by satellite gradients rather than by a stationarity assumption. The Everglades record "
     "in the 2 October issue measured exactly how badly ordinary kriging and IDW fail day to day; this is "
     "the proposed repair. Relevance: high, the highest of any metadata-only record in this backfill; "
     "flagged for a full-text read as soon as the abstract appears.")),
]
