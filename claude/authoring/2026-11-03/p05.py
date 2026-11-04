# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.5194/amt-19-6973-2026", journal="Atmos Meas Tech",
  short="Glienke HOLODROPS holographic droplet sensor event-based PIV characterization 2026",
  title="Development and characterization of an advanced holographic instrument for atmospheric research",
  sub=corpus.SENS, design="Instrument development and laboratory validation",
  pm="Digital holography of droplets and ice crystals above 8.8 um, with event-based particle image velocimetry",
  geo="Not stated (laboratory and one outdoor test)", endpoint="Size, shape and 3D position retrieval; cut-off size; operational duty cycle", tier="B",
  basis="Lab / research instrument", affil="",
  n=("Two configurations: HOLODROPS for long-term droplet size distributions and HOLODROPS-TRACK for short-interval 3D particle tracking of turbulence and "
     "collision-coalescence. Both recover size, shape and three-dimensional position of multiple particles above 8.8 um in one sample volume, replacing "
     "several probes. Hologram reconstruction is the binding constraint, so a complementary event-based PIV system identifies when to trigger the tracking "
     "mode at far lower data volume. All three were characterized in the laboratory, with one outdoor drizzle test of the prototype. Limitation: 8.8 um is far "
     "above the accumulation mode, so this is cloud microphysics instrumentation, not a PM2.5 method. Relevance: low directly, but the trigger architecture "
     "- a cheap continuous channel deciding when to run the expensive one - is the design pattern dense networks need for event capture.")),
 dict(pmid="", doi="10.5194/acp-26-15423-2026", journal="Atmos Chem Phys",
  short="Tirpitz UV aerosol absorption retrieval actinic flux FIREX-AQ plume age 2026",
  title="Retrieval of ultraviolet aerosol absorption from radiation measurements in young wildfire plumes",
  sub=corpus.SENS, design="Airborne retrieval algorithm development",
  pm="Imaginary refractive index k(308-440 nm) of biomass-burning aerosol from airborne actinic flux",
  geo="North America (western US wildfires)", endpoint="k, absorption Angstrom exponent, volume absorption cross section versus plume age", tier="A",
  basis="Lab / research instrument", affil="University of Colorado Boulder, USA; University of California Los Angeles, USA",
  n=("A VLIDORT-based algorithm retrieves the imaginary refractive index from airborne actinic flux over three FIREX-AQ flights, giving k(387 nm) of 0.02-0.03 "
     "and absorption Angstrom exponents of 3-5. Absorption decayed with physical plume age, with half-lives of 13+/-3 h for k, 16+/-4 h for the volume "
     "absorption cross section and 17+/-4 h for single-scattering co-albedo, and the authors publish a parameterization of absorptivity as a function of "
     "wavelength and plume age. Agreement with aircraft observations is good but less variable, which they attribute to spatial averaging in the method. "
     "Limitation: three flights, one fire regime. Relevance: direct - a measured decay timescale for optical properties is exactly the term that makes an "
     "optical sensor's response to smoke change with distance from the fire.")),
 dict(pmid="", doi="10.5194/acp-26-15461-2026", journal="Atmos Chem Phys",
  short="Peletidou fluorescence Raman depolarization lidar aerosol typing Thessaloniki 2026",
  title="Vertical profiling and aerosol typing using fluorescence Raman and depolarization lidar measurements over Thessaloniki, Greece",
  sub=corpus.SENS, design="Multi-year lidar measurement campaign",
  pm="Fluorescence backscatter, spectral fluorescence capacity and particle depolarization ratio, vertically resolved",
  geo="Europe (Thessaloniki, Greece)", endpoint="Aerosol type classification of 108 layers", tier="B",
  basis="Lab / research instrument", affil="Aristotle University of Thessaloniki, Greece; Aristotle University of Thessaloniki, Greece",
  n=("First fluorescence lidar observations over the Eastern Mediterranean: 108 aerosol layers from 50 cases, April 2024 to December 2025, classified into "
     "smoke, dust, polluted continental, clean continental and mixed pollen. Spectral fluorescence capacity separated the types cleanly, highest for smoke "
     "(3.5e-6 to 12.7e-6 /nm), then mixed pollen, polluted continental, clean continental and dust (0.4e-6 to 1.3e-6 /nm), and a subset was compared against "
     "the EARLINET Mahalanobis typing algorithm. Pollen depolarization differed from values reported at more northern latitudes, possibly reflecting pollen "
     "type. Limitation: one site, one instrument, and typing is validated against another algorithm rather than against in-situ composition. Relevance: "
     "moderate - a column method that distinguishes smoke from dust is the external constraint a surface mass network cannot supply for itself.")),
 dict(pmid="", doi="10.3390/atmos17111083", journal="Atmosphere",
  short="Liu CNN-xLSTM attention SHAP PM2.5 forecasting Beijing hourly 2026",
  title="Hybrid Network Models Based on SHAP Interpretability for PM2.5 Concentration Prediction: A Case Study of Beijing",
  sub=corpus.SENS, design="Machine-learning model development",
  pm="Hourly PM2.5 with co-pollutants and meteorology as predictors", geo="East Asia (Beijing, China)",
  endpoint="RMSE and R2 at 1, 2 and 10 h horizons; SHAP attribution", tier="B",
  basis="Model (CTM / LUR / ML)", affil="University of Emergency Management, China; Beijing University of Civil Engineering and Architecture, China",
  n=("A 1D CNN, extended LSTM and attention stack on Beijing hourly data for 2020-21 reached RMSE 9.845 ug/m3 and R2 0.977 one step ahead, cutting RMSE by "
     "about 8.5% against CNN-xLSTM at one step and by 8.9% and 12.3% at the 2 h and 10 h horizons. SHAP put 57.09% of predictive power on the pollutant block, "
     "carbon monoxide alone at 32.791%, with non-linear dependence and candidate turning points for CO, humidity, wind speed and direction; the authors warn "
     "these are model-derived, not physical thresholds. Limitation: two years at one city, no external-year test, and a forecast whose dominant feature is "
     "another measured pollutant is unavailable to a PM-only node. Relevance: moderate.")),
]
