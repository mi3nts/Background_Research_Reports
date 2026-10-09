# -*- coding: utf-8 -*-
P = [
 dict(pmid="42844605", doi="10.1186/s12889-026-29130-1", journal="BMC Public Health",
  short="CLHLS indoor constituents 2026",
  title="Association between exposure to indoor PM2.5 constituents and mortality risk among Chinese older adults: a nationwide prospective cohort study",
  sub=corpus.OTHR, design="Prospective cohort",
  pm="Indoor PM2.5 and constituents (BC, OM, sulfate, ammonium, nitrate) from ambient fields x infiltration factors",
  geo="China (nationwide, CLHLS-type cohort)", endpoint="All-cause mortality", tier="A",
  n=("12,607 participants (mean age 86.8) followed 2008-2018, 8,643 deaths over a median 4.14 years, "
     "time-varying Cox with restricted cubic splines. Per 1 ug/m3: PM2.5 HR 1.003 (1.001-1.005), black "
     "carbon 1.072 (1.035-1.111), organic matter 1.009 (1.002-1.016), sulfate 1.010 (1.001-1.019); "
     "associations were stronger in rural residents, non-linear, robust to excluding hypertensive and "
     "diabetic participants, and PM2.5 tracked the neutrophil-to-lymphocyte ratio as a candidate "
     "inflammatory mediator. Limitation: 'indoor' here is an ambient field multiplied by a modelled "
     "infiltration factor, not a measurement - and the infiltration factor is itself a function of "
     "building and season, so constituent contrasts partly encode housing type; black carbon's HR is an "
     "order of magnitude above PM2.5's per unit mass, which is biologically plausible and also what "
     "collinearity with a small-magnitude constituent produces. Relevance: high - this is the exact "
     "quantity a cheap indoor node measures directly, and the study had to model it.")),

 dict(pmid="42849652", doi="10.1016/j.envres.2026.125881", journal="Environ Res",
  short="Tampere SOA toxicity 2026",
  title="From primary to secondary aerosol: chemical transformation and toxicity of gasoline vehicle exhaust under contrasting driving conditions",
  sub=corpus.MECH, design="Chamber / laboratory",
  pm="Primary and photochemically aged gasoline exhaust; PAHs, nitro- and oxy-PAHs, water-soluble elements, SP-AMS",
  geo="Finland (Tampere, chassis dynamometer)", endpoint="A549 cytotoxicity at the air-liquid interface", tier="A",
  n=("A Euro 6 plug-in hybrid with a gasoline particulate filter run over a mild RDE cycle and a highly "
     "dynamic Combined cycle, cold and hot, with diluted exhaust aged in the Tampere Secondary Aerosol "
     "Reactor and delivered to A549 cells through a mobile air-liquid-interface system, fresh and aged, "
     "whole exhaust and gas-phase only. Ageing consistently shifted aerosol composition and toxicity "
     "relative to primary emissions. Limitation: one vehicle, one fuel, and an OFR delivers days of "
     "equivalent ageing in minutes at OH concentrations far above ambient, which over-produces "
     "highly oxygenated products; ALI dose at the cell surface is rarely quantified in the same units as "
     "an inhaled dose. Relevance: high - a GPF-equipped modern vehicle emitting little primary PM and "
     "substantial secondary aerosol is the case in which a tailpipe-mass regulatory metric and a "
     "downwind sensor network disagree by construction.")),

 dict(pmid="", doi="10.1021/acs.est.6c06323", journal="Environ Sci Technol",
  short="Aged traffic particles 2026",
  title="Aging of Urban Traffic Fine Particles Modulates Toxicity Mechanisms and Oxidative Stress Responses",
  sub=corpus.MECH, design="Chamber / laboratory",
  pm="Parking-garage aerosol (cold-start plus urban), fresh and OFR-aged; oxidative potential, SOA mass, O:C",
  geo="Not stated in abstract (parking-garage sampling)", endpoint="A549 and HepG2 oxidative stress and DNA damage", tier="B",
  n=("Real cold-start and urban emissions sampled in a parking garage, aged in an oxidation flow reactor. "
     "Ageing raised SOA mass up to 6.9-fold, O:C from 0.26 to 0.79, and both intrinsic and "
     "volume-normalised oxidative potential, while peroxide-sensitive DCF activity fell. Aged extracts "
     "raised cellular ROS in lung and liver cells and produced greater oxidative-stress and DNA-damage "
     "responses; fresh extracts instead suppressed cellular respiration, especially in HepG2, with "
     "distinct cell-painting morphological profiles. Limitation: extracts, not whole aerosol, so the "
     "soluble fraction is tested and the particle is not; the divergence between acellular DCF and "
     "cellular ROS shows how assay-dependent 'oxidative potential' remains. Relevance: high - oxidative "
     "potential is the leading candidate for a health-relevant metric a sensor network could one day "
     "report, and this is a direct demonstration that it changes downwind of the source.")),

 dict(pmid="", doi="10.1029/2026gh001884", journal="GeoHealth",
  short="GOES-R PM2.5 CONUS 2026",
  title="Machine Learning Predictions of PM2.5 and Their Applications to Exposure and Health Assessment in the CONUS",
  sub=corpus.EXPO, design="Machine-learning model",
  pm="Hourly PM2.5 at 0.01 degrees from gap-filled GOES-R geostationary AOD plus random forest",
  geo="USA (contiguous)", endpoint="None (exposure surface)", tier="B",
  n=("A two-phase framework: a U-Net-like partial convolutional network inpaints missing geostationary AOD "
     "(agreement with AERONET R=0.75, paired observations raised from 430,603 to 728,115 by iterative "
     "gap-filling), then a random forest predicts hourly surface PM2.5 at ~1 km for 2019 onward. "
     "Limitation: the inpainting is validated against AERONET, which is sited where retrievals already "
     "work - gap-filled cells are by definition cloudy, humid or smoke-covered, and their skill is not "
     "demonstrated; a random forest on gap-filled inputs inherits that uncertainty without propagating it. "
     "Relevance: high - hourly rather than daily is the step that makes a satellite product comparable to "
     "a sensor network's native time resolution, and the same day's conformal-prediction record is the "
     "missing half of this one.")),
]
