# -*- coding: utf-8 -*-
P = [
 dict(pmid="42863238", doi="10.1016/j.jenvman.2026.131131", journal="J Environ Manage",
  short="Sao Paulo 2024 fire extremes 2026",
  title="Compound fire-meteorology extremes drove megacity air pollution during the 2024 South American fire season",
  sub=corpus.EXPO, design="Chemical transport model", pm="Surface PM2.5 and CO, AOT, trajectories; fire-on/fire-off global simulations",
  geo="Brazil (Sao Paulo State)", endpoint="No health endpoint", tier="B",
  n=("Three multi-day 2024 episodes with daily PM2.5 of 80-100 ug/m3 in metropolitan Sao Paulo. Fire-off simulations missed "
     "the PM2.5 and CO peaks; fire-attributable increments reached 17-21 ug/m3 state-wide and a cumulative metropolitan "
     "burden of ~547 ug/m3-day. Episodes differed in transport configuration, and the worst coincided with heat, dryness "
     "and weak ventilation. Limitation: all fire inventories underestimated the most extreme episode, so the attribution "
     "is a lower bound with unquantified error; a global model is coarse for a megacity receptor. Relevance: moderate - "
     "the inventory shortfall at the extreme is exactly where a dense surface network constrains attribution.")),
 dict(pmid="", doi="10.5194/amt-19-6415-2026", journal="Atmos Meas Tech",
  short="CONIOPOL CL61 aerosol typing 2026",
  title="New operational perspective to identify aerosols and hydrometeors in real-time with a pioneering algorithm (CONIOPOL) based on single-wavelength polarization lidar (CL61)",
  sub=corpus.SENS, design="Instrument development", pm="Volume depolarisation ratio and attenuated backscatter (Vaisala CL61 ceilometer)",
  geo="Belgium (Uccle)", endpoint="No health endpoint", tier="B",
  n=("Automated classification from a polarised automatic lidar-ceilometer combining depolarisation, attenuated backscatter "
     "and cloud base to separate aerosol, cloud phase and precipitation and to type aerosol as dust, smoke/marine, "
     "continental or mixed. One year at Uccle showed strong temporal and vertical correspondence with CAMS for transported "
     "dust and smoke. Limitation: single wavelength cannot separate smoke from marine aerosol, and validation against "
     "CAMS is model-conditioned agreement rather than in-situ truth. Relevance: high - ceilometers are already networked "
     "across Europe; vertical typing tells a surface sensor network when its column assumption is broken.")),
 dict(pmid="", doi="10.5194/acp-26-14487-2026", journal="Atmos Chem Phys",
  short="Dust lidar asymptotics 2026",
  title="Asymptotic behavior of lidar scattering properties of absorbing dust aerosols across Rayleigh and geometrical-optics regimes: theory and implications",
  sub=corpus.SENS, design="Theoretical / optical modelling", pm="Lidar ratio, depolarisation ratio, SSA vs size parameter and iron-oxide fraction",
  geo="Not applicable (theory)", endpoint="No health endpoint", tier="C",
  n=("TAMUdust2020 and triaxial-ellipsoid calculations give shape-insensitive limits: Rayleigh S ~ x^-3, SSA ~ x^3, small "
     "depolarisation; geometric-optics depolarisation falls, SSA -> 1/2 and lidar ratio rises with strong absorption. "
     "Large, strongly absorbing dust can therefore mimic weakly depolarising classes and bias classifiers toward "
     "under-counting coarse and super-coarse dust. Limitation: theory only, no field test. Relevance: moderate - the same "
     "physics explains why optical PM sensors under-read coarse absorbing dust; the bias direction carries over.")),
 dict(pmid="", doi="10.5194/acp-26-14417-2026", journal="Atmos Chem Phys",
  short="Drone boundary-layer profiles Germany 2026",
  title="Influence of irradiance and mixing layer height on the vertical trace matter distribution in the lower planetary boundary layer - drone-based investigation",
  sub=corpus.SENS, design="Field measurement", pm="Drone vertical profiles of particle mass and number, CO2, O3 to 500 m",
  geo="Germany (rural)", endpoint="No health endpoint", tier="B",
  n=("Two 2.5-week summer campaigns: night profiles in the lowest 120 m showed multi-layer fine-scale stratification; O3 and "
     "potential temperature were the most reliable mixing-height markers, and trace species outperformed several "
     "meteorological variables. Local sources and sinks affected in-layer distribution more than irradiance, but "
     "aerosol concentrations homogenised under strong radiation even at low mixing heights. Limitation: rural summer "
     "only; drone-borne particle sensors are themselves low-cost optical units with flow and RH artefacts that the "
     "abstract does not address. Relevance: high - directly tests when a ground node represents the mixed layer.")),
]
