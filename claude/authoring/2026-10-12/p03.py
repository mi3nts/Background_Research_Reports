# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.5194/acp-26-14345-2026", journal="Atmos Chem Phys",
  short="Stutz Fairbanks inversion layers 2026",
  title="Vertical distribution of pollution trapped by wintertime surface inversions in Fairbanks, Alaska, during the ALPACA experiment",
  sub=corpus.SENS, design="Field measurement", pm="Vertical trace-gas profiles (LP-DOAS) with 1-D chemistry-transport model",
  geo="United States (Fairbanks, Alaska)", endpoint="No health endpoint", tier="B",
  n=("Long-path DOAS profiles during ALPACA 2022 resolve polluted surface layers 20-40 m deep persisting for days, with "
     "SO2 to 35 ppb, NO2 60 ppb, HONO 2.5 ppb, HCHO 7 ppb and depleted ozone. PACT-1D, with mixing parameterised from "
     "surface temperature gradient and wind, reproduces the profiles and gives a 1-4 h residence time. Limitation: "
     "gas-phase only - particulate profiles, the health-relevant quantity in Fairbanks, are not retrieved - and one "
     "winter at one city. Relevance: high for siting - a 20-40 m layer means a node on a rooftop and one at breathing "
     "height sample different air masses under inversions.")),
 dict(pmid="", doi="10.5194/acp-26-14329-2026", journal="Atmos Chem Phys",
  short="Chen Chengdu WSON partitioning 2026",
  title="Simultaneous measurements of gas- and aerosol-phase water-soluble organic nitrogen in the winter urban atmosphere of Chengdu, China",
  sub=corpus.EXPO, design="Field measurement", pm="Gas- and particle-phase WSON and amines; aerosol liquid water content",
  geo="China (Chengdu)", endpoint="No health endpoint", tier="C",
  n=("Winter urban campaign: particulate WSON 2.3+/-1.4 ugN/m3, twice gaseous, rising with PM2.5; particle fraction 0.70+/-0.14. "
     "WSON partitions into organic phase under warm-dry and into aerosol liquid water under cold-humid conditions; "
     "amines are mainly gaseous but shift to particles as aminium sulfate/nitrate during episodes. ALWC dominated "
     "partitioning over T, RH and pH; NH4NO3 was the main ALWC contributor. Limitation: one site, one season, and "
     "thermodynamic S-curve confirmation is model-on-model. Relevance: moderate - ALWC is precisely what inflates "
     "optical PM readings at high RH, so the nitrate-ALWC link is a calibration covariate as well as a chemistry result.")),
 dict(pmid="", doi="10.3390/atmos17101000", journal="Atmosphere",
  short="Comis Turin oxidative potential 2026",
  title="Oxidative Potential and Elemental Fingerprints of Urban and Suburban Particulate Matter in Turin",
  sub=corpus.MECH, design="Chamber / laboratory", pm="PM10 oxidative potential (ascorbic acid assay); total and bioaccessible metals",
  geo="Italy (Turin)", endpoint="Oxidative potential (acellular)", tier="C",
  n=("32 PM10 filters (urban traffic vs rural background, 2020-2021, min and max days of four months). Urban OP-AA "
     "0.12-0.60 vs suburban 0.10-0.38 nmol AA/min/m3; Cu was the most active single metal. Total and phosphate-buffer "
     "bioaccessible metal fractions were compared. Limitation: filters were selected at monthly concentration extremes, "
     "so OP-mass relationships are inflated by design, and n=32 cannot support source attribution of OP. Relevance: "
     "low-moderate - OP remains unmeasurable by optical nodes; the Cu dominance points to brake-wear tracers as the "
     "practical proxy.")),
 dict(pmid="", doi="10.3390/atmos17101001", journal="Atmosphere",
  short="Li Guangzhou 3D vegetation 2026",
  title="Scale-Dependent Effects of Three-Dimensional Urban Vegetation on Land Surface Temperature and Air Pollutants: Synergy and Trade-Off Zones in Guangzhou, China",
  sub=corpus.EXPO, design="Statistical model", pm="1 km gridded PM2.5, O3, NO2; layered vegetation volume",
  geo="China (Guangzhou)", endpoint="No health endpoint", tier="C",
  n=("Field LAI in 570 quadrats showed MODIS LAI is uninformative (r=0.15), so 3-D greenness was proxied by canopy height "
     "x tree cover. MGWR at 1-5 km: one SD of vegetation volume associated with 1.3 C lower LST, 0.30 ug/m3 lower PM2.5 "
     "and 1.3 ug/m3 lower NO2; O3 null citywide with offsetting local responses. Limitation: PM2.5 is a 1 km product "
     "whose own predictors include land cover, so the vegetation coefficient is partly the model reading its inputs "
     "back. Relevance: low-moderate - 0.3 ug/m3 is below the error floor of any LCS network, which is itself the point.")),
]
