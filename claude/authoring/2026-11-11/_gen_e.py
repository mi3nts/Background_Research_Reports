# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"
R = {
110: dict(short="Yangtze 45 US sites 43576 reference-FEM PM2.5 pairs sparse 1-in-3 1-in-6 1-in-12 sampling comparability verdict bootstrap indeterminacy",
  sub="SENS", design="Statistical analysis of monitoring data", pm="Daily PM2.5 FRM reference and federal equivalent method pairs, 2022-2025",
  geo="USA", endpoint="Determinacy of equivalence (slope-intercept) verdicts under thinned reference schedules", tier="A",
  basis="Reference / regulatory monitor", affil="Yangtze University, China; Yangtze University, China",
  n=("45 US sites (2022-2025), 127 episodes, 43,576 same-site reference-equivalent PM2.5 pairs. Each near-daily record was thinned to every phase of 1-in-3, "
     "1-in-6 and 1-in-12 schedules; US equivalence slope-intercept envelopes gave point verdicts, a moving-block bootstrap their stability. 64.6% of near-daily "
     "benchmarks were already boundary-uncertain; on the 45 stable episodes, sparse-schedule indeterminacy was 33.0% (21.1-46.1%), 63.8% (53.0-73.8%) and "
     "73.8% (63.7-82.6%), and 88 of 90 point mismatches became indeterminate rather than reversed. In a known-truth 1-in-12 simulation, coverage was about "
     "88% and 14 of 64 stable verdicts had the wrong sign. Single-author-group statistical work, not yet replicated. "
     "Relevance: direct - most low-cost sensor 'equivalence' claims rest on sparser reference support than this; report bootstrap state with the verdict.")),
118: dict(short="Christiani Thorax editorial air pollution lung cancer survival population-level benefit",
  sub="RESP", design=MO, pm="Metadata only", geo="Not stated in record", endpoint="Metadata only", tier="C",
  basis="Review / no primary exposure", affil="Harvard T.H. Chan School of Public Health, USA; Harvard T.H. Chan School of Public Health, USA",
  n=("Metadata only: no abstract (editorial). Thorax editorial by Christiani on air pollution and lung cancer survival, framed around moving from association "
     "to population-level benefit; presumably accompanies a research paper in the same issue, which is not identified in the record. No finding is asserted here. "
     "Relevance: peripheral - locate the index paper in the weekly sweep.")),
119: dict(short="Xiamen 890 matched pairs prenatal greenness NDVI landscape indices congenital heart defects NO2 PM2.5 mediation",
  sub="REPR", design="Case-control", pm="First-trimester NDVI (250-1000 m) and landscape metrics; NO2, PM2.5, SO2, O3 as mediators",
  geo="China (Xiamen)", endpoint="Congenital heart defects; indirect effects via air pollutants", tier="B",
  basis="Not stated", affil="Key Laboratory of Urban Environment and Health, CAS, China; Women and Children's Hospital, Xiamen University, China",
  n=("Xiamen birth records 2016-2019: 1,785 CHD cases and 1,848 controls, 890 pairs after 1:1 propensity matching. First-trimester greenness was associated "
     "with lower CHD odds; at 1 km, large core patches and connectivity were protective and fragmentation and edge density harmful. Multi-pollutant mediation "
     "found indirect paths through NO2 and PM2.5, largest for NO2; the SO2 path did not survive joint modelling and the O3 indirect estimate was positive. "
     "The NDVI-NO2 relation turned at NDVI about 0.46. No effect sizes are given in the abstract, the PM2.5 exposure model is not stated, and propensity "
     "matching discarded half the cases. "
     "Relevance: indirect - PM2.5 enters only as a mediator of greenness.")),
123: dict(short="UL FSRI NIOSH live-fire training structures exterior real-time optical PM instructors fuels location",
  sub="OCC", design="Field measurement", pm="Stationary time-resolved optical real-time PM area measurements outside two live-fire training structures",
  geo="USA", endpoint="Exterior PM concentrations by fuel load, structure and staging location", tier="B",
  basis="Lab / research instrument", affil="Fire Safety Research Institute, UL Research Institutes, USA; NIOSH, USA",
  n=("Stationary optical real-time PM area monitors outside two training structures: a single-storey fire-behaviour lab (five fuels) and a two-storey "
     "concrete multicompartment structure (three fuels). In the fire-behaviour lab, fuel load had limited effect on exterior PM, but standing upwind and "
     "further from the structure lowered the hazard; at the multicompartment structure fuel load mattered more and the second floor showed high PM where "
     "instructors may be unable to relocate. No concentrations, instrument model or smoke-specific correction are given in the abstract; area monitors "
     "are not personal breathing-zone exposure. "
     "Relevance: indirect - optical monitors in fresh smoke need a smoke-specific mass correction before such numbers are compared with limits.")),
124: dict(short="OHSU Portland 29 older adults bedroom PM2.5 light noise temperature humidity TVOC CO2 objective sleep 211 nights",
  sub="OCC", design="Long-term indoor monitoring campaign", pm="Night-averaged bedroom PM2.5 among seven in-home environmental sensors",
  geo="USA (Portland, Oregon)", endpoint="Total sleep time, WASO, sleep efficiency, movement, heart and respiratory rate", tier="C",
  basis="Not stated", affil="Oregon Health and Science University, USA; Oregon Health and Science University, USA",
  n=("29 older adults (17 cognitively normal, 12 with MCI or dementia; mean age about 77) followed for a mean 211 nights at home with objective sleep metrics "
     "and seven bedroom environmental measures. Light had the strongest association with total sleep time, humidity with WASO and efficiency, temperature "
     "with movement and heart and respiratory rate; PM2.5 was associated with total sleep time (effect size -0.050) and sleep efficiency (-0.058), Bonferroni "
     "significant. The PM2.5 sensor is not identified, effect sizes are standardised without stated units, and 29 people give many nights but little "
     "between-person information. Conference paper. "
     "Relevance: direct - long-run in-home PM sensing paired with passive physiology is the deployment model for indoor exposure-response work.")),
}
