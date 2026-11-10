# -*- coding: utf-8 -*-
P = [
 dict(pmid="42994781", doi="10.1016/j.envres.2026.126120", journal="Environ Res",
  short="Espinoza-Guillen Lima case-crossover PM2.5 asthma ED road proximity 2026",
  title="Ambient fine particulate matter and asthma emergency visits in Lima, Peru: Does Residential Proximity to Major Roads Matter?",
  sub=corpus.RESP, design="Case-crossover",
  pm="Daily PM2.5 from a 1x1 km multi-source model at geocoded residence", geo="Peru",
  endpoint="Asthma emergency department visits, lag 0-15 d", tier="A",
  basis="Model (CTM / LUR / ML)", affil="Johns Hopkins University, USA; Universidad Peruana Cayetano Heredia, Peru",
  n=("Time-stratified case-crossover of 75,602 asthma ED visits (mean age 16.2 y) at 10 Lima public hospitals, 2017-2023, with DLNM. At lag 0, PM2.5 rising "
     "from 5 to 15 ug/m3 gave OR 1.09 (1.01-1.16); the exposure-response curve was steeper at low concentrations. Cumulative lag 0-15 OR was 4.02 (1.97-8.19) "
     "within 400 m of a major road versus 1.66 (0.81-3.38) beyond it (interaction p=0.04). The cumulative ORs are for a contrast the abstract does not state "
     "and are implausibly large for a 15-day DLNM sum; the road modifier probably carries unmodelled traffic NO2 and ultrafine particles that a 1-km PM2.5 "
     "surface cannot resolve. Relevance: direct - a near-road gradient finer than the exposure grid is exactly what curbside low-cost nodes would test.")),
 dict(pmid="42994338", doi="10.1016/j.envpol.2026.129432", journal="Environ Pollut",
  short="Kim Korea urban forest PM2.5 stable isotopes receptor model seasonal 2026",
  title="Seasonal variation in urban PM(2.5) sources and the modulating role of urban forests.",
  sub=corpus.EXPO, design="Field campaign",
  pm="Filter PM2.5 with d13C and d15N isotopes, transects from expressway and industrial edge into forest", geo="South Korea",
  endpoint="Seasonal PM2.5, isotopic source signatures, vegetation index", tier="C",
  basis="Lab / research instrument", affil="Seoul National University, South Korea; Seoul National University, South Korea",
  n=("Two urban-forest regions (Gomae, expressway-to-forest transect; Sihwa, industrial complex to residential with a forest buffer) sampled across seasons with "
     "PM2.5 mass, stable carbon and nitrogen isotopes, meteorology and a vegetation index, plus receptor modelling. d15N pointed to vehicle emissions in both "
     "regions, rising in Sihwa in winter consistent with coal. Forest-interior PM2.5 was significantly lower in the growing season, but the difference "
     "vanished in the non-growing season, even under evergreen canopy, when concentrations are highest. No effect sizes, site counts or sampling durations are "
     "given; two regions cannot separate canopy from distance-to-source decay. Relevance: indirect - transect designs like this are cheap to densify "
     "with paired low-cost nodes and would resolve the season-by-canopy interaction properly.")),
 dict(pmid="42993963", doi="10.2196/89412", journal="JMIR Form Res",
  short="Kim New Mexico Wyoming coal miners self-reported dust SARS-CoV-2 seroconversion 2026",
  title="Novel Occupational and Environmental Risk Factors for SARS-CoV-2 Infection Among Coal Miners: Longitudinal Cohort Study.",
  sub=corpus.OCC, design="Cohort",
  pm="Self-reported occupational dust, residential wood burning and shared transport frequency", geo="USA",
  endpoint="Incident anti-nucleocapsid IgG seroconversion over 12 months", tier="C",
  basis="Proxy / questionnaire", affil="University of New Mexico Health Sciences Center, USA; University of New Mexico Health Sciences Center, USA",
  n=("230 surface coal miners (New Mexico 169, Wyoming 61), February 2021-March 2022, nucleocapsid IgG at 0, 3, 6 and 12 months. Higher self-reported "
     "mining-dust exposure was associated with lower odds of incident seroconversion, adjusted OR 0.42 (0.17-1.07), non-significant; wood burning and shared "
     "transport showed no association, and no frequent wood burner seroconverted (0/35). The hypothesis that particulate exposure raises infection risk via "
     "ACE2 upregulation was not supported. Exposure is a single questionnaire answer with no dust measurement, Firth-penalised models on few events, and "
     "vaccination plus prevalent seropositivity confound strongly. Relevance: weak - a negative occupational result resting entirely on perceived dust, "
     "a case for personal samplers in mining cohorts.")),
 dict(pmid="42993665", doi="10.1002/kjm2.70316", journal="Kaohsiung J Med Sci",
  short="Ba rat intratracheal PM2.5 IL-17A TXNIP NLRP3 cardiac fibrosis 2026",
  title="Neutralization of IL-17A Ameliorates PM2.5-Induced Cardiac Inflammation and Fibrosis in Rats by Suppressing the TXNIP/NLRP3 Signaling Pathway.",
  sub=corpus.MECH, design="Animal model",
  pm="Collected PM2.5 by intratracheal instillation; dose not stated in the abstract", geo="China",
  endpoint="Cardiac function, fibrosis, TXNIP/NLRP3 pyroptosis markers", tier="C",
  basis="Lab / research instrument", affil="First Hospital of Anhui University of Science and Technology, China; First Hospital of Anhui University of Science and Technology, China",
  n=("Rat cardiac-injury model by intratracheal PM2.5 instillation with an IL-17A-neutralising antibody arm, plus neonatal rat cardiac fibroblasts in vitro. "
     "PM2.5 raised splenic Th17 fraction and cardiac IL-17A/TRAF6, impaired cardiac function, and increased collagen I/III, alpha-SMA, NF-kB activation, IL-6, "
     "IL-1b, TXNIP and NLRP3-pyroptosis proteins (ASC, cleaved caspase-1, GSDMD-N, IL-18); antibody neutralisation reversed these. TXNIP knockdown abolished "
     "IL-17A effects in fibroblasts. No dose, particle source, group size or effect magnitude is reported in the abstract, and bolus instillation is far from "
     "inhaled ambient dose rates, so the human-relevant dose is unknown. Relevance: indirect - mechanism for cardiac endpoints; adds nothing to measurement.")),
]
