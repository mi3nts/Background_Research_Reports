# -*- coding: utf-8 -*-
P = [
 dict(pmid="42988300", doi="10.1016/j.envres.2026.126121", journal="Environ Res",
  short="Tan Shenzhen PMF-ML firework burning PM2.5 source apportionment 2026",
  title="Apportioning Firework Burning and Routine Source Contributions to PM(2.5) in a Chinese Megacity Using Two PMF-Machine Learning Frameworks.",
  sub=corpus.EXPO, design="Source-apportionment method",
  pm="Hourly PM2.5 chemical constituents, Shenzhen, Jan-Mar 2023-2025", geo="China", endpoint="Source contributions to PM2.5 mass", tier="B",
  basis="Lab / research instrument", affil="Peking University Shenzhen Graduate School, China; Peking University Shenzhen Graduate School, China",
  n=("Three Spring Festival seasons of hourly speciation in Shenzhen; PMF resolved 11 routine sources plus firework burning. Fireworks contributed 4.7% of PM2.5 "
     "over the full period, 33% during display episodes and over 50% at peak hours. Two ML surrogates (direct and indirect) reproduced PMF contributions and "
     "flagged fireworks as dominant during episodes. Agreement with PMF is circular validation - the ML learns PMF output, so it inherits PMF's factor ambiguity "
     "and no independent tracer test is reported. Relevance: direct for networks - episodic sources at >50% of hourly mass are exactly where a fixed "
     "humidity/composition calibration on optical sensors breaks.")),
 dict(pmid="42988296", doi="10.1016/j.envres.2026.126094", journal="Environ Res",
  short="Sathish Kanpur Mumbai nine-stage size-resolved aerosol chemistry ICRP deposited dose 2026",
  title="Size-resolved measurements matter for chemistry and health: paired inland-coastal size-resolved aerosol chemistry and the inadequacy of bulk PM(2.5) dose estimates.",
  sub=corpus.EXPO, design="Filter sampling + composition",
  pm="Nine-stage impactor PM (<0.43 to >9 um), ions and OC/EC; ISORROPIA-II pH and water", geo="India", endpoint="Aerosol pH, SOC formation, ICRP 66 regional deposited dose", tier="B",
  basis="Lab / research instrument", affil="Indian Institute of Technology Bombay, India; Indian Institute of Technology Bombay, India",
  n=("Paired Kanpur (inland IGP) and Mumbai (coastal) impactor sampling over three seasons. Fine mode (PM2.1) is up to 62% of mass in Kanpur, not Mumbai; Kanpur "
     "fine aerosol is more acidic (pH 3.5-4.5 vs 4.5-5.0). ICRP 66 dosimetry: fine mode delivers 53-75% of alveolar dose from 40-62% of mass, and Kanpur alveolar "
     "doses are 1.3-2 times Mumbai's. The authors flag that SOC-water associations lose significance at one value per sample day, and dose depends on assumed "
     "deposition fractions. Relevance: direct - a calibration fitted at a coastal site will misweight the inland fine mode that carries the dose.")),
 dict(pmid="", doi="10.1021/acs.est.6c08882", journal="Environ Sci Technol",
  short="Subramanian chamber size-resolved emission rates PM oxidative potential six indoor sources 2026",
  title="Size- and Time-Resolved Emission Rates of Particulate Matter Mass, Chemical Constituents, and Oxidative Potential from Indoor Sources",
  sub=corpus.OCC, design="Chamber emission characterisation",
  pm="Size-resolved PM mass, composition and DTT oxidative potential, <0.25 to 10 um", geo="USA", endpoint="Emission rates; respiratory-tract deposited mass and OP", tier="B",
  basis="Lab / research instrument", affil="",
  n=("Chamber tests of two incenses, candle, toaster, humidifier and cigarette. Emission was mostly unimodal and concentrated below 0.25 um, where mass-normalised "
     "DTT OP was highest; composition and OPm varied with size but little with time. 37 +/- 3% of emitted PM10 mass and OP is deposition-capable, 45 +/- 2% of it "
     "alveolar. For equal PM10 mass and OP, these indoor sources give an estimated 76 +/- 10% higher alveolar dose than ambient PM. Six sources in one chamber; "
     "the dose comparison is modelled, not measured. Relevance: direct - optical sensors undercount below ~0.3 um, so indoor nodes systematically miss the "
     "fraction carrying most OP.")),
 dict(pmid="", doi="10.5194/acp-26-15543-2026", journal="Atmos Chem Phys",
  short="Chen TRACER Houston micropulse lidar aerosol vertical profile boundary layer parameterisation 2026",
  title="Aerosol vertical distributions shaped by boundary layer dynamics in a coastal urban environment: insights from the TRACER campaign",
  sub=corpus.SENS, design="Remote sensing / lidar retrieval",
  pm="Aerosol concentration profiles from micropulse lidar constrained by surface aerosol measurements", geo="USA", endpoint="Aerosol layer depth and stratification vs boundary layer", tier="B",
  basis="Lab / research instrument", affil="",
  n=("Six months of TRACER (Houston, 2022) micropulse lidar retrievals anchored to ground aerosol data. An S-shaped fitting function yields an aerosol-layer depth "
     "and a stratification-strength parameter. Concentrations drop sharply at strong capping inversions, layer depth tracks boundary-layer growth and collapse, "
     "and sea-breeze passage swaps continental for maritime aerosol. Relationships with BLH and the potential-temperature gradient are statistically significant "
     "but weak (no r given). No health endpoint. Relevance: direct for satellite-surface fusion - the AOD-to-surface PM2.5 ratio depends on exactly this profile "
     "shape, and the parameterisation offers a physical predictor in place of BLH alone.")),
]
