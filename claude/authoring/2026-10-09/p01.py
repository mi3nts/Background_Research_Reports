# -*- coding: utf-8 -*-
P = [
 dict(pmid="42853922", doi="10.1126/sciadv.aea8654", journal="Sci Adv",
  short="Zeng RON toxicity 2026",
  title="Reduced organic nitrogen compounds dominate the toxicity of PM2.5 organics following internal exposure",
  sub=corpus.MECH, design="Chamber / laboratory",
  pm="Urban PM2.5 organic fraction: nontargeted HRMS, serum-albumin adductomics, multi-endpoint toxicity prediction",
  geo="China (urban)", endpoint="Predicted multi-organ toxicity (in silico)", tier="A",
  n=("Nontargeted high-resolution MS of urban PM2.5 organics is combined with protein-adductomics to define "
     "the fraction that actually reaches the circulation, then scored with multi-endpoint toxicity "
     "prediction. Reduced organic nitrogen (RON: amines, amides, N-heterocycles) carries 39% of the "
     "predicted multi-organ toxicity of the internally exposed fraction against 23% for the oxygenated "
     "organics the field usually targets, and binds human serum albumin strongly enough to explain "
     "systemic distribution. Limitation: the toxicity shares are model predictions on annotated features, "
     "not measured dose-response; nontargeted annotation confidence and ionisation bias toward basic "
     "nitrogen both inflate RON's apparent share. Relevance: high - the toxic fraction is invisible to "
     "optical mass sensing, an argument for adding composition proxies (e.g. N-containing BrC absorption) "
     "to networks.")),

 dict(pmid="42850241", doi="10.1038/s41467-026-77475-3", journal="Nat Commun",
  short="Ma TRWP China 2026",
  title="Spatiotemporal dynamics of tire wear particles reveal escalating emission inequalities across China's road network",
  sub=corpus.BURD, design="Modelling / inventory",
  pm="Tire and road wear particle (TRWP) PM2.5 emissions, road-network resolved, ML-harmonised field data",
  geo="China (national road network)", endpoint="Population exposure / health risk (modelled)", tier="A",
  n=("A road-segment-resolved national inventory fuses harmonised field measurements, ML and traffic "
     "activity: China's roads emitted 425 kt of TRWP-derived PM2.5 in 2023, ~80% from modelled "
     "vehicle-induced resuspension. TRWP's share of traffic PM2.5 is projected to rise 34-fold from 2011 "
     "to 2050, reaching 67% of traffic PM2.5 emissions, with exposure concentrated in megacity "
     "corridors; combined mitigation cuts emissions 41%. Limitation: resuspension dominates the total and "
     "is the least constrained term - it is modelled, not measured, and its emission factor varies by an "
     "order of magnitude with road silt loading and humidity. Relevance: high - non-exhaust PM is coarse-"
     "skewed and rubber/mineral-rich, exactly the aerosol on which Plantower-class sensors misreport mass, "
     "so a growing TRWP share silently changes network calibration.")),

 dict(pmid="42853264", doi="10.1007/s00406-026-02391-y", journal="Eur Arch Psychiatry Clin Neurosci",
  short="Tang source PM dementia 2026",
  title="Associations of long-term exposure to source-specific PM2.5, lifestyle, and genetic susceptibility with dementia risk: a prospective cohort study",
  sub=corpus.NEU, design="Prospective cohort",
  pm="Source-specific PM2.5 (domestic, road transport, other transport, industry), time-varying",
  geo="Not stated (large prospective cohort)", endpoint="Incident all-cause dementia", tier="B",
  n=("Cox models with time-varying source-specific PM2.5; median follow-up 11.9 years, 5,648 incident "
     "dementia cases. Per IQR: domestic HR 1.05 (1.01-1.08), road transport 1.12 (1.04-1.21), other "
     "transport 1.12 (1.06-1.19), industry 1.07 (1.03-1.11). High exposure plus high polygenic risk gave "
     "a 236-352% excess versus the lowest-lowest stratum. Limitation: source fields come from a dispersion "
     "model whose sources are spatially collinear, and per-IQR scaling differs by source, so the ranking "
     "of transport over domestic is not a per-ug comparison; the joint-effect excess mostly restates "
     "genetic risk; the abstract does not name the cohort or country. Relevance: moderate - source attribution at residence is what a speciated or BC-capable "
     "node network could provide directly.")),

 dict(pmid="42852011", doi="10.1021/ehp.6c00147", journal="Environ Health Perspect",
  short="Byun ADRD readmission 2026",
  title="PM2.5 and 30-Day Readmission in Medicare Beneficiaries with Alzheimer's Disease and Related Dementias: Effect Modification by Neighborhood Green and Blue Space",
  sub=corpus.NEU, design="Time-stratified case-crossover",
  pm="Daily modelled PM2.5 at residential ZIP Code, lag 0-2",
  geo="United States (contiguous, Medicare 2000-2016)", endpoint="30-day all-cause readmission", tier="B",
  n=("Nationwide time-stratified case-crossover over 6,098,836 ADRD index admissions, 759,128 (12.4%) "
     "readmitted within 30 days. Per IQR (7.2 ug/m3) of lag 0-2 PM2.5: OR 1.010 (1.006-1.015), "
     "stronger for readmissions after day 7. Landsat- and Street-View-derived green and blue space did "
     "not conclusively modify the association. Limitation: ZIP-level modelled PM2.5 for a largely "
     "homebound or institutionalised population is a poor proxy for the air actually breathed, which "
     "biases toward the null and makes the null modification uninterpretable. Relevance: moderate - a 1% "
     "per-IQR effect on a 6-million-person denominator is the scale at which indoor sensing in care "
     "settings would change the exposure estimate more than the model does.")),
]
