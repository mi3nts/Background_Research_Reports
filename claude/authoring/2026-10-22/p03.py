# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.3390/atmos17101033", journal="Atmosphere",
  short="Bloise water-soluble carbon nitrogen PM10 Chennai street vertical 2026",
  title="Seasonal, Spatial, and Near-Surface Vertical Variability of Water-Soluble Carbon and Nitrogen in PM10 in Chennai, India",
  sub=corpus.EXPO, design="Field measurement", pm="PM10 mass, WSOC, WSTN, WSIN at 3, 16 and 37 m",
  geo="India (Chennai street sites)", endpoint="Seasonal, site and vertical variability of soluble PM10 composition", tier="B",
  n=("Three Chennai street environments across three campaigns, sampled at nominal heights of 3, 16 and 37 m: 76 PM10 "
     "samples, 75 WSOC/WSTN and 74 WSIN determinations. Means: PM10 65.3 ug/m3, WSOC 2.53 ug C/m3, WSTN 1.28 and WSIN "
     "1.26 ug N/m3. WSOC fell from 4.01 to 0.62 ug C/m3 between campaigns while WSIN rose from 1.12 to 1.86. Site "
     "contrasts were strong for PM10, and vertical differences were not significant. Limitation: about 25 samples per "
     "campaign split across sites and heights gives little power for the vertical null. Campaigns confound season with "
     "meteorology. Relevance: medium - no vertical gradient between 3 and 37 m supports rooftop siting of street-canyon "
     "LCS for PM10, though the null is underpowered.")),
 dict(pmid="42907699", doi="10.1007/s10661-026-16071-w", journal="Environ Monit Assess",
  short="Magalhaes extreme rainfall landslides PM10 PM2.5 Sao Sebastiao 2026",
  title="Can extreme rainfall associated with landslides affect air quality? A case study in a coastal city (Sao Sebastiao, Sao Paulo State, Brazil)",
  sub=corpus.EXPO, design="Monitoring-record analysis", pm="Hourly PM10 and PM2.5 (regulatory station), Dec 2021-Feb 2025",
  geo="Brazil (Sao Sebastiao, Sao Paulo State)", endpoint="PM response to extreme precipitation and landslide event", tier="B",
  n=("Hourly PM and meteorology from December 2021 to February 2025, with k-means meteorological clusters and openair "
     "polar and time-variation analysis around the February 2023 extreme rainfall and landslides. Rain first scavenged PM. "
     "The post-landslide period then showed PM10 up 124% and PM2.5 up 93.3%. Two comparison rain events showed similar "
     "scavenging but different recovery, so the authors do not attribute the rise to landslides alone. Limitation: a "
     "single station and one event; clean-up traffic, resuspension of dried debris and meteorology are not separated, "
     "and there is no composition data. Relevance: medium - post-disaster resuspension is a case for rapidly deployable "
     "sensor nodes.")),
 dict(pmid="", doi="10.1080/02786826.2026.2746515", journal="Aerosol Sci Technol",
  short="Cover solvatochromic fluorophores in situ aerosol fluorescence 2026",
  title="Evaluation of solvatochromic fluorophores for in situ fluorescence characterization of aerosols",
  sub=corpus.SENS, design="Metadata only (no abstract)", pm="Aerosol particles (in situ fluorescence probes)",
  geo="Not stated in record", endpoint="Fluorophore performance for in situ aerosol characterisation", tier="C",
  n=("Title and authors only (Cover, Gibbons, Boadu, Ohno et al.). No abstract was retrievable from Crossref or Semantic "
     "Scholar at harvest. The title describes evaluating solvatochromic dyes, whose emission shifts with local polarity, "
     "as in-situ probes of aerosol particle properties. Analytes, particle types and performance metrics cannot be "
     "stated. Limitation: unverifiable beyond the title. Solvatochromic readouts also confound polarity with viscosity "
     "and water content, so any phase-state inference needs independent calibration. Relevance: low-medium - a "
     "laboratory composition probe, not a field-deployable sensor channel.")),
 dict(pmid="42907900", doi="10.1186/s13073-026-01770-3", journal="Genome Med",
  short="Kim SpaMixed spatial mixed models microbiome PM2.5 2026",
  title="Spatial mixed models for assessing environmental exposure effects on the microbiome",
  sub=corpus.EXPO, design="Statistical methods (simulation + application)", pm="PM2.5 (two applied studies)",
  geo="Not stated (methods paper)", endpoint="PM2.5-associated microbiome taxa", tier="C",
  n=("SpaMixed is a spatial mixed model for microbiome count data that handles both spatial dependence across regions "
     "(conditional autoregressive priors) and ecological correlation among taxa. In simulations it achieved high "
     "feature-selection power with low false-positive rates and lower estimation error than existing methods. Applied to "
     "two PM2.5 studies, it found 'biologically plausible' PM2.5-associated taxa. Limitation: the abstract gives no "
     "sample sizes, regions or effect sizes for the applications. CAR priors absorb the spatial variance that carries "
     "the PM2.5 contrast, so the method trades confounding for attenuation. Relevance: low - statistical method, no "
     "sensing content.")),
]
