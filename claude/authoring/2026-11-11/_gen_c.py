# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"
R = {
33: dict(short="Haramaya HDSS 923 kitchens PurpleAir II-SD PM2.5 rural biomass 473 vs urban 80 ug/m3 wet-dry season",
  sub="OCC", design="Cross-sectional study", pm="Kitchen PM2.5 by PurpleAir II-SD optical sensors, minute data over 3-5 days per household",
  geo="Ethiopia (Haramaya)", endpoint="24-h mean kitchen PM2.5 by residence, season and household factors", tier="B",
  basis="Low-cost sensor / network", affil="Haramaya University, Ethiopia; Haramaya University, Ethiopia",
  n=("Preprint. 923 kitchens (573 rural, 350 urban) in the Haramaya HDSS, eastern Ethiopia, monitored for 3-5 days each with 20 PurpleAir II-SD sensors, "
     "January 2023 to December 2024. Mean 24-h PM2.5 was 473 (SD 255) ug/m3 in rural and 80 (92) in urban kitchens, difference 393 ug/m3 (95% CI 370-416). "
     "In 96 kitchens measured in both seasons, rural means rose from 343 (dry) to 732 ug/m3 (wet), urban from 47 to 105. All rural homes used open fires. "
     "The abstract reports no correction or co-location: uncorrected Plantower readings in dense biomass smoke at high humidity carry large, "
     "humidity-dependent bias, which is the same axis as the wet-season contrast. "
     "Relevance: direct - the largest low-cost household PM dataset in the Horn of Africa; usable only once a smoke- and RH-specific correction is shown.")),
35: dict(short="Tufts OHDSI GIS toolchain OMOP exposure infrastructure synthetic 40000 persons simulated PM2.5 geocoding error attenuation",
  sub="EXPO", design="Statistical methods (simulation + application)", pm="Geospatial exposure linkage to OMOP CDM; simulated PM2.5 effects on a synthetic cohort",
  geo="USA", endpoint="Recovery of known exposure effects; attenuation under geocoding displacement", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Tufts Clinical and Translational Science Institute, USA; Tufts CTSI, USA",
  n=("Preprint describing an open-source toolchain that standardises geospatial sources into person-place-time exposure records in the OMOP Common Data Model "
     "(FAIR catalogue, GIS vocabulary, local geocoding, geometry-attribute index). Tested on a synthetic cohort of 40,000 persons placed in real US census "
     "tracts with eight simulated PM2.5 effects and six nulls: derived exposures matched an independent answer key and known effects were recovered. "
     "Displacing residences by empirical geocoding error changed estimates little for smooth regional exposure but attenuated them by up to half for "
     "exposures varying over 100 m. Synthetic data test plumbing, not real-world exposure validity. "
     "Relevance: direct - quantifies why fine-scale (sensor-resolved) surfaces lose half their signal under ordinary geocoding error.")),
55: dict(short="Wadden Sea size-resolved inorganic ions levoglucosan 13C 14C organic carbon ship sulfate continental outflow",
  sub="EXPO", design="Source apportionment", pm="Size-resolved impactor samples: inorganic ions, levoglucosan, total carbon, 13C and 14C of OC",
  geo="Europe (Wadden Sea, Germany/Netherlands)", endpoint="Size-resolved composition and fossil/non-fossil OC by season and wind sector", tier="C",
  basis="Lab / research instrument", affil="Not stated; University of Groningen, Netherlands",
  n=("Measurement report from a Wadden Sea coastal site: size-resolved samples by season and wind sector analysed for inorganic ions, levoglucosan, total "
     "carbon and stable and radiocarbon isotopes of organic carbon at several desorption temperatures. Land-sector samples were dominated by nitrate, ammonium "
     "and total carbon, the single sea-sector set by sulfate and total carbon; sulfate reached 0.5 ug/m3 in both, suggesting ship emissions. Fossil OC "
     "fractions were highest below 250 nm (traffic combustion), and 13C signatures pointed to SOA in smaller, more volatile carbon and photochemical "
     "processing at larger sizes. One sea-sector sample set limits the ship attribution. "
     "Relevance: peripheral - background composition for coastal network sites; no sensing content.")),
61: dict(short="IIT Madras operating procedures advanced aerosol instruments high-altitude observatories technical note",
  sub="SENS", design=MO, pm="Metadata only", geo="Not stated in record", endpoint="Metadata only", tier="C",
  basis="Lab / research instrument", affil="Indian Institute of Technology Madras, India; Indian Institute of Technology Madras, India",
  n=("Metadata only: no abstract in the Crossref deposit at issue time. A technical note in Aerosol Science and Technology on operating procedures for "
     "advanced aerosol instruments at high-altitude observatories, from IIT Madras. No finding is asserted here. "
     "Relevance: indirect - high-altitude sites are the reference anchors for regional aerosol networks; recheck for an abstract in the weekly sweep.")),
62: dict(short="Cholakian Bertrand northern hemisphere multi-annual concentration exposure simulations analysis",
  sub="EXPO", design=MO, pm="Metadata only", geo="Not stated in record", endpoint="Metadata only", tier="C",
  basis="Model (CTM / LUR / ML)", affil="",
  n=("Metadata only: no abstract in the Crossref deposit at issue time. Atmospheric Environment paper analysing large-scale, multi-annual concentration "
     "and exposure simulations over the northern hemisphere (first author Cholakian). No finding is asserted here. "
     "Relevance: indirect - hemispheric model exposure fields are the background that regional sensor fusion corrects; recheck in the weekly sweep.")),
63: dict(short="Chatoutsidou Lazaridis European major cities mortality burden long-term PM2.5 NO2 updated evidence",
  sub="BURD", design=MO, pm="Metadata only", geo="Europe", endpoint="Metadata only", tier="C",
  basis="Not stated", affil="",
  n=("Metadata only: no abstract in the Crossref deposit at issue time. Atmospheric Pollution Research paper on mortality burdens from long-term PM2.5 "
     "and NO2 exposure in major European cities under updated concentration-response evidence (first author Chatoutsidou). No finding is asserted here. "
     "Relevance: indirect - burden estimates of this kind inherit the exposure surface; recheck for an abstract.")),
64: dict(short="Jana Delhi road waterlogging post-event PM2.5 satellite-based association robustness road network",
  sub="EXPO", design=MO, pm="Metadata only", geo="India (Delhi)", endpoint="Metadata only", tier="C",
  basis="Satellite-fused", affil="",
  n=("Metadata only: no abstract in the Crossref deposit at issue time. Atmospheric Pollution Research paper using satellite data to test an association "
     "between road waterlogging and post-event PM2.5 on Delhi's road network, with robustness checks. No finding is asserted here. "
     "Relevance: indirect - a resuspension mechanism that kerbside low-cost networks in Delhi would observe directly; recheck for an abstract.")),
}
