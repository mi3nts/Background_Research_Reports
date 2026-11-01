# -*- coding: utf-8 -*-
P = [
 dict(pmid="42962798", doi="10.1016/j.envpol.2026.129429", journal="Environ Pollut",
  short="Yousaf nanoscale curvature hygroscopic growth respiratory deposition ultrafine 2026",
  title="Nanoscale Curvature Controls Hygroscopic Growth and Respiratory Deposition of Atmospheric Nanoparticles",
  sub=corpus.EXPO, design="Laboratory measurement", pm="15-100 nm NaCl particles, HTDMA growth factors fed to MPPD dosimetry",
  geo="Laboratory (no field site)", endpoint="Hygroscopic growth factor, DRH and modelled regional respiratory deposition", tier="B",
  n=("HTDMA measurements of 15-100 nm NaCl particles fed into the MPPD lung-deposition model. The Kelvin effect raised "
     "deliquescence RH to 77-81% for 15-36 nm particles and suppressed growth; at 80-90% RH, growth factors were 1.95-2.25 "
     "(15 nm) and 1.99-2.36 (100 nm). Ignoring hygroscopic growth overestimated total deposition by up to 25%, with an "
     "18% tracheobronchial difference for particles <=50 nm, and shifted larger UFPs deeper into the lung. Limitation: "
     "pure NaCl is a best-case hygroscopic aerosol; ambient UFP is organic-rich with far lower kappa, so the correction "
     "is an upper bound. Relevance: medium - the same size-dependent water uptake that biases optical sensors in humid "
     "air also changes delivered dose, so dry-size number counts understate the problem.")),
 dict(pmid="42960271", doi="10.1016/j.mex.2026.104216", journal="MethodsX",
  short="Martin simplified method portable air cleaner CADR low-cost sensors 2026",
  title="A simplified method for evaluating fine particulate matter removal performance of portable air cleaners",
  sub=corpus.OCC, design="Field co-location + chamber", pm="PM2.5 decay measured with low-cost sensors vs research-grade instruments",
  geo="USA (residence and laboratory)", endpoint="Clean air delivery rate (CADR) of DIY and commercial air cleaners", tier="B",
  n=("Methods paper for community-run CADR testing: release a short-lived nebuliser aerosol in a sealed room, log PM2.5 decay "
     "with and without the cleaner on low-cost sensors, and compute CADR from the decay-rate difference. Residential "
     "low-cost-sensor CADRs ran ~26% below laboratory values from research-grade instruments - a conservative bias. Of "
     "ten units, a four-filter Corsi-Rosenthal box performed best among DIY builds; a fan shroud added ~11%. Across 135 "
     "models DIY units cost far less per CADR unit. Limitation: the 26% gap mixes sensor size-response with room mixing "
     "and leakage, and is not decomposed; nebuliser aerosol is not wildfire smoke. Relevance: high - a practical "
     "protocol in which the low-cost sensor is the reference, with its bias quantified.")),
 dict(pmid="", doi="10.5194/acp-26-15333-2026", journal="Atmos Chem Phys",
  short="Wu source-dependent organic aerosol hygroscopicity eastern China biomass burning 2026",
  title="Source-dependent organic aerosol hygroscopicity in eastern China: observational evidence for conditional enhancement under biomass-burning influence",
  sub=corpus.SENS, design="Field campaign", pm="Humidified light scattering f(RH) with OA composition; ZSR closure for kappa_OA",
  geo="China (eastern, rural site)", endpoint="Organic aerosol hygroscopicity parameter kappa_OA", tier="B",
  n=("Winter field campaign at a rural eastern-China site retrieving organic-aerosol hygroscopicity from humidified "
     "nephelometry and ZSR closure. kappa_OA ranged from ~0 to 0.49 (mean 0.11 +/- 0.11) and correlated only weakly with "
     "O:C; instead it rose with biomass-burning influence, and ageing enhanced kappa_OA only when biomass burning "
     "dominated. Highly oxidised OA under weak biomass influence stayed weakly hygroscopic. Limitation: kappa_OA is a "
     "residual after subtracting inorganic contributions, so errors in the inorganic closure load onto the organic term; "
     "one site, one season. Relevance: high - humidity correction of optical PM sensors usually assumes a fixed kappa; "
     "this shows kappa shifts with source, so smoke-affected periods need a different growth correction.")),
 dict(pmid="", doi="10.1016/j.envpol.2026.129453", journal="Environ Pollut",
  short="Kalkavouras ammonia sulfuric acid BVOC urban new particle formation Athens 2026",
  title="Assessing the combined roles of ammonia, sulfuric acid, and biogenic volatile organic compounds in urban new particle formation",
  sub=corpus.EXPO, design="Long-term field measurement campaign", pm="Particle number size distributions with NH3, BVOCs and proxy H2SO4",
  geo="Greece (Athens, Thissio)", endpoint="NPF frequency, formation rate J14 and growth rate", tier="B",
  n=("Seven months (June 2023-January 2024) of particle number size distributions, NH3 and BVOCs at the Thissio urban "
     "background site in Athens, with a proxy for H2SO4. Mean NH3 2.3 +/- 0.7 ug/m3. NPF occurred on 19% of days, most "
     "often in autumn (29-33%) when ventilation and condensation sink were low. Precursor levels barely differed between "
     "event and non-event days; the highest J14 came at intermediate NH3 and H2SO4 with low BVOCs, while growth rates "
     "rose with NH3 and isoprene/monoterpenes. Limitation: H2SO4 is a proxy, not measured, and the record lacks a full "
     "annual cycle. Relevance: medium - NPF bursts dominate urban number concentration but are invisible to mass-based "
     "optical sensors, which see nothing below ~300 nm.")),
]
