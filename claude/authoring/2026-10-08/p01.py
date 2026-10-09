# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.21203/rs.3.rs-11182286/v1", journal="Research Square (preprint)",
  short="Conformal PM2.5 mapping 2026",
  title="Preregistered External Validation of Spatially Valid Conformal Prediction for Air-Pollution Exposure Mapping in China",
  sub=corpus.EXPO, design="Statistical model",
  pm="Province-level population-weighted PM2.5, 1998-2024 (n=837), with distribution-free prediction intervals",
  geo="China (provincial)", endpoint="None (uncertainty quantification)", tier="A",
  n=("A preregistered external validation - rare in this literature - of spatially valid conformal "
     "prediction against gradient boosting, with an acceptance band of [0.85, 0.95] on pooled coverage "
     "declared in advance. Under spatial hold-out the spatially weighted method reached 0.873 coverage at "
     "nominal 90% (gradient boosting: 0.486), 5 of 7 macro-regions met the block criterion (worst, North "
     "China, 0.719), and interval widths matched equal-weight conformal prediction, so coverage was not "
     "bought with wider intervals. Under temporal hold-out coverage fell to 0.794, outside the band, and "
     "the preregistered joint hypothesis failed - traced to the sharp post-2017 PM2.5 decline. "
     "Limitation: province-level annual means are a very coarse spatial unit; coverage there says little "
     "about a 1 km surface, and the temporal failure is the one that matters for forecasting. "
     "Relevance: high - every exposure map in this corpus ships point estimates with no interval, and "
     "this is the first record in the series to preregister the test and report the failure.")),

 dict(pmid="", doi="10.1021/acs.est.6c10850", journal="Environ Sci Technol",
  short="Budapest deposition 2026",
  title="Aerosol Deposition in the Human Respiratory System from Distinct Urban Sources Using Multiple Exposure Metrics",
  sub=corpus.EXPO, design="Exposure model (secondary data)",
  pm="Source-apportioned particle number size distributions, 6-1000 nm, with lung deposition modelling",
  geo="Hungary (Budapest urban background)", endpoint="None (deposited dose)", tier="A",
  n=("Source apportionment of particle number at an urban background site feeds a lung deposition model "
     "under reference breathing conditions. Most particles reach the deep lung with maximum deposition at "
     "airway generations 17-21 depending on activity; deposition fraction varies by source from 76% (new "
     "particle formation) to 27% (solid fuel combustion). Exercise raises total deposition and shifts it "
     "from extra-thoracic to alveolar; deposition rates are more sensitive to activity than deposition "
     "fractions, and number and surface-area curves are similar in shape but rank sources differently. "
     "Limitation: a deposition model, not a measurement - ICRP-type models are calibrated on healthy "
     "adults at rest and carry large uncertainty below 20 nm, exactly where the new-particle-formation "
     "fraction sits. Relevance: high - a factor of nearly three in deposited fraction between sources at "
     "the same ambient number concentration is the clearest statement in this backfill that mass, and even "
     "number, is not dose.")),

 dict(pmid="42844301", doi="10.1038/s41467-026-77632-8", journal="Nat Commun",
  short="China BC burden 2026",
  title="The Hidden Health and Climate Burden of Black Carbon under China's Dual Carbon Strategy",
  sub=corpus.BURD, design="Health impact model",
  pm="Localized black carbon emission inventory with revised health risk function; CMIP6 comparison",
  geo="China (national)", endpoint="Premature mortality; radiative forcing", tier="A",
  n=("A localized BC inventory and revised risk function put over 540,000 premature deaths attributable to "
     "black carbon in China in 2015 - more than twice previous estimates - while the CMIP6 inventory is "
     "found to overestimate BC radiative forcing by 45%. Projections suggest demographic ageing may offset "
     "the health gains from falling emissions. Limitation: a doubled burden rests on a 'revised health "
     "risk function' whose derivation is the entire result and cannot be checked from the abstract; "
     "BC-specific concentration-response functions are confounded with co-emitted species in every source "
     "study they come from, so attributing 540,000 deaths to BC rather than to combustion mixture is a "
     "strong claim. Relevance: high - BC is measurable by low-cost aethalometry, and the inventory-vs-"
     "measurement gap this paper quantifies is what a dense BC network would close.")),

 dict(pmid="42849692", doi="10.1016/j.envpol.2026.129302", journal="Environ Pollut",
  short="Beijing CKD cohort 2026",
  title="Association between Long-term Exposure to Air Pollution and Incident Chronic Kidney Disease among Adults in Beijing, China",
  sub=corpus.OTHR, design="Prospective cohort",
  pm="Annual PM10, PM2.5, NO2, CO and O3, with a composite pollution score",
  geo="China (Beijing)", endpoint="Incident chronic kidney disease (eGFR-defined)", tier="B",
  n=("15,580 adults in the Beijing Air Pollution and Population Health Cohort, 664 incident CKD cases "
     "2019-2025, time-varying Cox models. Per 10 ug/m3: PM10 HR 1.18 (1.06-1.31) and CO 1.02 (1.01-1.03) "
     "were significant; PM2.5 1.22 (0.99-1.50) and NO2 1.17 (0.96-1.43) were positive but crossed unity; "
     "O3 was inverse, 0.77 (0.68-0.87). The composite score gave 1.51 (1.07-2.12) per IQR, with stronger "
     "associations in women, older adults and urban residents. Limitation: six years of follow-up in one "
     "city where all pollutants fell together makes single-pollutant HRs nearly uninterpretable - the "
     "inverse ozone estimate is the tell, since ozone rose as PM fell; eGFR-defined incident CKD is "
     "sensitive to a single creatinine measurement. Relevance: moderate - kidney endpoints are "
     "under-studied, but this design cannot separate the pollutants.")),
]
