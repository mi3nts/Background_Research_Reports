# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1016/j.envpol.2026.129384", journal="Environ Pollut",
  short="Pyae Tin Saw portable PM2.5 cross-site prediction fixed station 2026",
  title="Short-term PM2.5 data continuity: Cross-site prediction of portable measurements using a nearby fixed monitoring station",
  sub=corpus.SENS, design="Metadata only (no abstract)", pm="Portable PM2.5 monitor vs nearby fixed-station PM2.5",
  geo="Thailand (inferred from author affiliation; not stated in record)", endpoint="Cross-site prediction / gap-filling of portable PM2.5", tier="C",
  n=("Title and authors only (Pyae Tin Saw, Kallawicha); day-0 Elsevier deposit with no abstract anywhere at harvest. "
     "The title describes predicting short-term portable PM2.5 records from a nearby fixed monitoring station to maintain "
     "data continuity. Sensor model, distance, n, and skill metrics cannot be stated. Limitation: unverifiable beyond the "
     "title; cross-site transfer functions are typically valid only within the regional-background regime and fail for "
     "local sources, which is exactly when portable data matter. Relevance: high - gap-filling an LCS or portable "
     "record against a regulatory anchor is a core network-operations problem.")),
 dict(pmid="", doi="10.1016/j.envpol.2026.129391", journal="Environ Pollut",
  short="Tripathi satellite-reanalysis sulfate aerosol India ground measurements 2026",
  title="Improving Satellite-Reanalysis Sulfate Aerosol Estimates over India Using Ground Measurements",
  sub=corpus.EXPO, design="Metadata only (no abstract)", pm="Sulfate aerosol (satellite/reanalysis vs ground)",
  geo="India", endpoint="Bias-corrected sulfate PM component surface", tier="C",
  n=("Title and authors only (Tripathi, Sahu, Sharma, Gupta); no abstract indexed at harvest. The title indicates ground "
     "measurements used to correct satellite-reanalysis (likely MERRA-2/CAMS-type) sulfate aerosol over India. Data "
     "sources, method and skill cannot be stated. Limitation: unverifiable beyond the title; Indian speciation networks "
     "are sparse and urban-biased, so any correction trained on them risks transferring urban bias to rural cells. "
     "Relevance: moderate - component-resolved surfaces are the complement LCS mass networks lack; pairs with the "
     "sulfate-dominant AF signal in today's Medicare cohort.")),
 dict(pmid="", doi="10.1016/j.atmosenv.2026.122431", journal="Atmos Environ",
  short="Dayanandana CMIP6 dust optical depth MENA evaluation 2026",
  title="Evaluation of Dust Optical Depth in CMIP6 Simulations over the Middle East-North Africa Region",
  sub=corpus.EXPO, design="Metadata only (no abstract)", pm="Dust optical depth (CMIP6 models vs observations)",
  geo="Multi-country (Middle East and North Africa)", endpoint="Model skill for dust optical depth", tier="C",
  n=("Title and authors only (Dayanandana, Parottil, Abbas, Al-Harrasi et al.); no abstract at harvest. Evaluates CMIP6 "
     "dust optical depth over MENA, presumably against MODIS/MERRA-2 DOD. Models, metrics and biases cannot be stated. "
     "Limitation: unverifiable beyond the title; column optical depth maps to surface PM10 only through assumed "
     "vertical profiles and size distributions, so climate-model DOD skill says little about surface exposure. "
     "Relevance: low-moderate - MENA dust is where optical LCS mass error from coarse particles is largest.")),
]
