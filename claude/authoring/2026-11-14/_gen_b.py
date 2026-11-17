# -*- coding: utf-8 -*-
# Records for 14 Nov issue, part B (authored 2026-11-16 run).
R = {
11: dict(short="Warsaw Fischer 344 rats 7-day whole-body biodiesel exhaust B7 SHB20 DPF colon oxidative stress",
  sub="MECH", design="Animal inhalation experiment", pm="Diesel engine exhaust from B7 and SHB20 biofuels, measured PM 2.13-2.19 mg/m3 without and 0.17-0.19 mg/m3 with DPF",
  geo="Poland (laboratory)", endpoint="Colon lipid peroxidation, redox and antioxidant markers, inflammation", tier="B",
  basis="Lab / research instrument", affil="Warsaw University of Life Sciences, Poland; Institute of Nuclear Chemistry and Technology, Poland",
  n=("Male Fischer 344 rats breathed whole-body diesel exhaust from first-generation B7 or second-generation SHB20 (FAME plus hydrotreated vegetable oil) blends for 7 days, 6 h/day, at measured PM of 2.19 and 2.13 mg/m3 without a particle filter and 0.17 and 0.19 mg/m3 with one. "
     "Exhaust induced colonic lipid peroxidation, redox shifts, antioxidant mobilisation and inflammation-associated responses; effects were blend-specific, strongest for SHB20 without DPF, and only partly mitigated by the filter. "
     "Doses are two to three orders above ambient, exposure is the whole mixture (NOx and VOCs included), and the abstract gives no effect sizes or group sizes. "
     "Relevance: indirect - the DPF arm cuts PM about 12-fold without abolishing effects, pointing at the gas phase or ultrafines that mass-based sensors do not see.")),
12: dict(short="NC A&T review organic dust livestock chronic bronchitis macrophages lymphocytes TLR4 NF-kB 18 studies",
  sub="OCC", design="Narrative review", pm="Organic dust and its components (e.g. LPS) in livestock production",
  geo="Global (review)", endpoint="Macrophage and lymphocyte activation in organic dust-associated chronic bronchitis", tier="C",
  basis="Review / no primary exposure", affil="North Carolina A&T State University, USA; North Carolina A&T State University, USA",
  n=("Review of the cellular basis of chronic bronchitis from livestock organic dust: 25,488 database hits narrowed to 18 research articles (2015-2025). "
     "Repetitive dust or LPS exposure keeps macrophages and lymphocytes activated through TLR4, TLR2, NF-kB, PKC, ERK and MAPK signalling, sustaining cytokine and chemokine output that drives mucus hypersecretion and airway remodelling; micronutrient or anti-inflammatory co-treatment blunted inflammation in experimental work. "
     "The selection from 25,488 hits to 18 papers is not described with a reproducible protocol, no exposure-response information is extracted, and dust is characterised by source rather than size or mass. "
     "Relevance: indirect - agricultural dust is a coarse, bioactive fraction that optical low-cost sensors size poorly; no measurement content.")),
13: dict(short="Chiang Mai veterinary review PM2.5 lung pathology short vs long lifespan animal models One Health sentinel",
  sub="MECH", design="Narrative review", pm="PM2.5 in laboratory rodents versus long-lived animals breathing ambient air",
  geo="Global (review)", endpoint="Pulmonary phenotype by lifespan: acute reversible injury versus chronic remodelling and neoplasia", tier="C",
  basis="Review / no primary exposure", affil="Chiang Mai University, Thailand; Chiang Mai University, Thailand",
  n=("Review contrasting PM2.5 lung disease in short-lifespan laboratory rodents, typically dosed high for a small fraction of life, with long-lived species breathing ambient air for decades. "
     "Rodents show acute, often reversible inflammation; long-lived animals show cumulative particle bioaccumulation, airway remodelling and spontaneous neoplasia. The authors concede lifespan is confounded with exposure intensity and duration and cannot be separated from them, and propose veterinary sentinel cohorts, cross-species dosimetric scaling and in-tissue particle burden measurement. "
     "No systematic search or quantitative synthesis. "
     "Relevance: indirect - sentinel-animal cohorts would need long, spatially resolved ambient exposure records, the kind dense low-cost networks can supply.")),
16: dict(short="Penn State Soongsil electric stove hot plate ceramic pan UFP 5.08e6 cm-3 coagulation source strength decay",
  sub="OCC", design="Source-isolated emission test", pm="Size-resolved ultrafine particle number during electric-stove heating at 250 and 540 C",
  geo="USA (laboratory)", endpoint="Peak UFP number, source strength, size distribution, loss processes", tier="B",
  basis="Lab / research instrument", affil="Soongsil University, Republic of Korea; Pennsylvania State University, USA",
  n=("Chamber-style tests of six electric-stove surface configurations at controller settings of 250 and 540 C, followed by decay. With no pan, total UFP reached 2.53 x 10^6 cm-3 at 250 C and 5.08 x 10^6 cm-3 at 540 C; repeated heating cut peaks by up to 91%. "
     "At 540 C the bare hot plate and a ceramic-coated pan emitted 5.47 x 10^12 and 4.89 x 10^12 particles/min in their first episodes, mostly in the smallest sizes; cookware shifted the distribution by material. "
     "Coagulation removed over 60% of early particles; deposition and ventilation dominated later, and a well-mixed model underpredicted measured concentrations. "
     "No food was cooked, so these are heater/cookware emissions only; single test space. "
     "Relevance: direct for indoor sensing - these particles are below the detection range of optical low-cost sensors, which will report a clean kitchen.")),
17: dict(short="Dalian Maritime Tianjin Port AIS bottom-up ship emission inventory AERMOD PM2.5 216.73 Mg May-July 2021",
  sub="BURD", design="Health impact model", pm="Ship PM10 and PM2.5 emissions (AIS bottom-up) and AERMOD-dispersed ambient contributions",
  geo="China (Tianjin)", endpoint="Emissions by vessel type and mode; contribution to ambient pollutants at nearest station", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Dalian Maritime University, China; Dalian Maritime University, China",
  n=("AIS-based bottom-up inventory of ship emissions at Tianjin Port for May-July 2021, dispersed with AERMOD. Ships emitted 237.97 Mg PM10 and 216.73 Mg PM2.5 alongside 1,663.85 Mg SO2 and 8,123.43 Mg NOx; conventional ships produced 40.70% of total emissions and berthing more than 32% of SO2 and 43% of NOx. "
     "At the monitoring station nearest the port ships contributed 79.13% of ambient SO2 and 58.22% of NOx but under 10% of particulate matter. "
     "Three summer months only, no model evaluation statistics in the abstract, and AERMOD omits secondary particle formation, which is how ship SO2 and NOx become PM. "
     "Relevance: indirect - port fenceline PM sensors will miss the ship signal in primary mass; SO2/NOx co-sensing is the better tracer.")),
19: dict(short="Chengdu 30 synthetic cities emission inversion sensor placement vs source coverage calibration error truth-free residual",
  sub="SENS", design="Methodological simulation with applied case study", pm="Pollutant-agnostic receptor network inversion; applied to seven Chengdu NO2 stations",
  geo="China (Chengdu; synthetic cities)", endpoint="Normalised source-rate error by design decision; residual AUC for model error", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Chengdu Vocational & Technical College of Industry, China; Dalian University of Technology, China",
  n=("Benchmark over 30 synthetic cities placing five network design decisions on one error scale for emission-rate inversion from concentration-mapping monitors. Under matched transport, covering traffic in the source dictionary changed normalised source error by 0.74 and dictionary fidelity and sensor calibration by about 0.68 each, versus 0.13-0.15 across placement criteria; under a mismatched dispersion generator the coverage effect fell to the size of placement. "
     "Unmodelled mixing height was among the commonest errors (0.41-0.53); a truth-free residual flagged severe model error (AUC 0.89-0.95). Applied to seven Chengdu NO2 stations, estimates were withheld for poor skill. "
     "Synthetic only; no PM application. "
     "Relevance: direct for network design - sensor calibration error outweighs siting choice by about fivefold for source inversion.")),
20: dict(short="UW medRxiv CONUS 1-km daily total and wildfire PM2.5 2018-2024 ML smoke density attributable deaths",
  sub="EXPO", design="Machine-learning model development", pm="Daily 1-km total and wildfire-specific PM2.5 from an ML model with precursors and smoke density",
  geo="USA (contiguous)", endpoint="Cross-validated R2; wildfire share of PM2.5 and of attributable deaths", tier="A",
  basis="Model (CTM / LUR / ML)", affil="University of Washington, USA; University of Washington, USA",
  n=("Preprint. ML framework estimating daily 1-km total and wildfire-attributable PM2.5 over the contiguous US for 2018-2024 from public data, including chemical precursors and smoke density. Cross-validated R2 was 0.72 daily and 0.89 annual. "
     "Wildfire smoke supplied about 35% of PM2.5 along the west coast in 2020 and over 25% in the eastern US in 2023; wildfire PM2.5 accounted for 20% of PM2.5-attributable deaths on the west coast in 2020 (30 times 2019) and 24% in the north-east in 2023 (14 times 2019). "
     "Not peer reviewed; the abstract gives no error on the wildfire component itself, the hardest part to validate, nor the concentration-response function used. "
     "Relevance: direct - a candidate exposure surface whose daily skill (R2 0.72) leaves room for PurpleAir fusion in smoke events.")),
21: dict(short="UCLouvain Research Square silica mice type I interferon Ifnar1 knockout B1 cells CXCL13 autoantibodies",
  sub="MECH", design="Animal knockout experiment", pm="Crystalline silica particles instilled (dose not stated in abstract)",
  geo="Belgium (laboratory)", endpoint="IFN-I signature, autoantibodies, pulmonary B1-cell recruitment, CXCL13/CXCR5", tier="C",
  basis="Lab / research instrument", affil="UCLouvain, Belgium; UCLouvain, Belgium",
  n=("Preprint. Silica exposure produced a sustained type I interferon signature in wild-type mice with raised lung and circulating anti-dsDNA, class-switched IgG, natural IgM and IgA; these humoral changes were markedly attenuated in Ifnar1-/- mice. "
     "Silica recruited innate-like B1 cells to the lung via the CXCL13/CXCR5 axis; without IFNAR, B1 cells accumulated in tracheobronchial nodes and spleen instead and CXCL13 induction was lost. "
     "Not peer reviewed; dose, route detail, group sizes and effect sizes are absent from the abstract, and crystalline silica is an occupational particle with toxicity specific to its surface chemistry, not ambient PM. "
     "Relevance: indirect - mechanistic link from particle lung injury to systemic autoimmunity; no measurement content.")),
22: dict(short="Sichuan CDC seven sentinel hospitals DLNM multi-pathogen ARI positivity humidity RSV PM2.5 H. influenzae FDR",
  sub="RESP", design="Time-series (distributed lag non-linear)", pm="Weekly PM2.5 among six pollutants plus temperature and humidity (source not stated in abstract)",
  geo="China (Sichuan)", endpoint="Pathogen-specific positivity among acute respiratory infection cases", tier="C",
  basis="Not stated", affil="Sichuan Center for Disease Control and Prevention, China; Sichuan Center for Disease Control and Prevention, China",
  n=("Preprint. Weekly panel of 23,014 acute respiratory infection cases from seven Sichuan sentinel hospitals (2024-2026); quasi-Poisson DLNMs (6-week lag) gave cumulative RRs for the 90th versus 10th percentile of each exposure with within-pathogen FDR control. "
     "Humidity-RSV was the most stable single association (RR 2.01, 1.06-3.82) but failed FDR (adjusted p 0.130) and vanished with temperature co-adjustment (RR 1.05). H. influenzae positivity fell with PM2.5 (no estimate given in the abstract); 12 of 40 estimates survived FDR. "
     "Positivity is a ratio among tested cases, not incidence, and two years of weekly data give little seasonal replication. "
     "Relevance: indirect - the PM2.5 result is a screening signal, not an effect estimate.")),
}
