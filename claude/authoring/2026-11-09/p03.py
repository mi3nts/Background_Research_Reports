# -*- coding: utf-8 -*-
P = [
 dict(pmid="43003337", doi="10.1016/j.envpol.2026.129530", journal="Environ Pollut",
  short="Kanchanasuta Bangkok AQHI temporal transportability PM2.5 AQI coarse PM cardiovascular morbidity 2021-2024",
  title="Temporal Transportability and Component Deconstruction of a Multipollutant Air Quality Health Index: Health Information Beyond the Composite Score.",
  sub=corpus.CVM, design="Time-series",
  pm="Daily PM2.5, PMcoarse (PM10-PM2.5), O3, SO2 and composite AQHI / PM2.5-based AQI from Bangkok monitors",
  geo="Thailand", endpoint="Daily total, cardiovascular and respiratory hospital morbidity", tier="B",
  basis="Reference / regulatory monitor", affil="Mahidol University, Thailand; Bangkok Metropolitan Administration, Thailand",
  n=("Out-of-period test of the Bangkok AQHI, 2021-2024: 1,461 days, 26 postcodes, 23 hospitals, negative binomial models against a PM2.5-based AQI. The "
     "composite AQHI did not consistently improve fit or out-of-time prediction over the AQI. PMcoarse (PM10 minus PM2.5) stayed associated with "
     "cardiovascular morbidity after nonlinear PM2.5 and gas adjustment, MA0-1 IRR 1.175 (1.076-1.283); the increment is not given in the abstract. "
     "On discordant days, removing O3 brought every AQHI below 7. Multiple comparisons are acknowledged and several signals are not multiplicity-robust. "
     "Relevance: direct - coarse PM carries independent cardiovascular signal, and a PM2.5-only sensor network cannot report it.")),
 dict(pmid="43003300", doi="10.1016/j.jare.2026.11.009", journal="J Adv Res",
  short="Xi 1898 Chinese counties green blue space life expectancy mediation PM1 PM1-2.5 PM2.5-10 2000-2021",
  title="Associations of green and blue spaces with life expectancy are partly explained by lower ambient particulate matter: Evidence from 1898 Chinese counties over two decades.",
  sub=corpus.BURD, design="Ecological panel",
  pm="County PM1, PM1-2.5 and PM2.5-10 from high-resolution gridded datasets",
  geo="China", endpoint="County life expectancy", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Sun Yat-sen University, China; Sun Yat-sen University, China",
  n=("1,898 counties, 2000-2021, generalised additive mixed models in a mediation framework. A simultaneous 10-percentage-point rise in green and blue "
     "cover was associated with 0.968 years more life expectancy (0.945-0.991); lower PM explained about 23%, PM1 most (0.109 y, 0.095-0.123), then "
     "PM2.5-10 (0.065 y) and PM1-2.5 (0.050 y). Indirect effects were strongest in the Northwest and roughly twice as large in underdeveloped regions. "
     "County-level ecological mediation with modelled, collinear size fractions cannot separate deposition by vegetation from the fact that greener "
     "counties are less industrial. Relevance: indirect - size-fractionated PM1 surfaces are uncommon; PM1 channels on optical sensors could test them.")),
 dict(pmid="43002489", doi="10.1159/ned/adwag033", journal="Neuroepidemiology",
  short="Kim GBD 2023 Asia Alzheimer dementia mortality attributable air pollution tobacco FPG BMI decomposition 1990-2023",
  title="Decoding the Drivers of Alzheimer's Disease and Other Dementias Mortality in Asia, 1990-2023: A Global Burden of Diseases Study 2023.",
  sub=corpus.NEU, design="GBD secondary analysis",
  pm="GBD 2023 air-pollution risk factor (ambient PM, household air pollution) as modelled by GBD",
  geo="Asia", endpoint="ADOD mortality attributable to risk factors, adults >=70 y", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Kyung Hee University, South Korea; Kyung Hee University, South Korea",
  n=("GBD 2023 comparative risk assessment in 34 Asian countries, adults aged 70 and over, with Das Gupta decomposition into population growth, ageing and "
     "epidemiological change. ADOD mortality was highest in high-income Asia Pacific (661 per 100,000, UI 190-1,505) and lowest in Central Asia (273). "
     "The abstract calls air pollution 'a major driver' but gives no attributable rate for it, while high fasting glucose rose everywhere (high-income Asia "
     "Pacific 76 to 139 per 100,000). The uncertainty intervals span roughly an order of magnitude, and the air-pollution-dementia link enters as a GBD "
     "relative-risk function, not an estimate from these data. Relevance: indirect - burden accounting only.")),
 dict(pmid="43003302", doi="10.1016/j.jare.2026.11.010", journal="J Adv Res",
  short="Duan KDM4B PTX3 dendritic cell senescence severe asthma HDM PM2.5 mouse model biologic non-response 2026",
  title="KDM4B-PTX3-mediated dendritic cell senescence drives severe asthma and predicts biologic non-response.",
  sub=corpus.MECH, design="Animal + in vitro + human cohort",
  pm="PM2.5 used as one airway trigger in mouse models alongside house dust mite; dose not stated in the abstract",
  geo="China", endpoint="cDC2 senescence, airway remodelling, plasma PTX3, biologic response", tier="C",
  basis="Lab / research instrument", affil="Guangzhou University of Chinese Medicine, China; Shenzhen University, China",
  n=("Discovery cohort of 226 patients plus scRNA-seq, ChIP/ATAC-seq and HDM and PM2.5 mouse models. Plasma PTX3 was raised in severe asthma and tracked "
     "impaired lung function and exacerbations; CD1c+ cDC2 cells were its main source, and DC-specific Ptx3 knockout showed lung cDC2 supply about 61% of "
     "circulating PTX3. KDM4B demethylates H3K9me3 at PTX3 and PTX3 induces KDM4B through NF-kB, a loop the authors call conserved across triggers; "
     "inhaled KDM4B inhibition was tested. PM2.5 is one of two triggers and its dose and source are not given, so the PM-specific contribution cannot be "
     "separated from HDM. Relevance: indirect - mechanism for PM-triggered severe asthma, not an exposure result.")),
]
