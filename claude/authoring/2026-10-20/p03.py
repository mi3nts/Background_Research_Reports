# -*- coding: utf-8 -*-
P = [
 dict(pmid="42899117", doi="10.1093/nsr/nwag570", journal="Natl Sci Rev",
  short="Wu ProNet physics-AI coupled CTM PM2.5 O3 forecasting 338 cities 2026",
  title="Fusing physics and AI enhances accuracy and diagnostic capabilities in air quality forecasting",
  sub=corpus.SENS, design="Deep-learning forecasting", pm="PM2.5 and O3 forecasts (338 Chinese cities)",
  geo="China (338 cities)", endpoint="Not applicable (forecast skill)", tier="A",
  n=("ProNet embeds observation-constrained neural correctors inside the governing equations of a chemical transport "
     "model rather than post-processing its output. On 2022-23 data across 338 Chinese cities it beat the physical "
     "CTM and AI-only baselines, generalised better to extreme events outside training, and surpassed "
     "forecaster-adjusted operational forecasts by 6.1% (PM2.5) and 3.0% (O3). The correctors yield process-level "
     "error bookkeeping that exposes systematic CTM parameterisation biases. Limitation: '6.1% accuracy' is an "
     "unspecified metric; one two-year period invites temporal leakage, and process attribution from learned "
     "correctors is not unique - compensating errors can be assigned to the wrong process. Relevance: high - "
     "in-equation assimilation is the natural slot for dense calibrated LCS observations.")),
 dict(pmid="42897397", doi="10.1007/s11356-026-38305-7", journal="Environ Sci Pollut Res Int",
  short="Nolles IGP vs NCP PM2.5 pollution forming efficiency CAMS 2026",
  title="Indo-Gangetic Plain experiences higher aerosol pollution than North China Plain despite lower emissions",
  sub=corpus.EXPO, design="Reanalysis / inventory analysis", pm="CAMS EAC4 PM2.5 vs CAMS-GLOB-ANT emissions",
  geo="South Asia and China (IGP vs NCP)", endpoint="Not applicable (emission-concentration efficiency)", tier="B",
  n=("CAMS EAC4 reanalysis, CAMS-GLOB-ANT emissions and ERA5 for 2019. The NCP emitted 65% more primary PM and "
     "precursors (28,860 vs 17,464 kt) yet the IGP had higher annual PM2.5 (123.6 vs 113.2 ug/m3); NCP logged more "
     "bad-air days (251 vs 238) but the IGP longer episodes, up to 170 consecutive days around Delhi. A 'pollution "
     "forming efficiency' was nearly double in the IGP in winter, attributed to winds <6 km/h and PBL <300 m. "
     "Limitation: both concentration and emissions are model products for one year; EAC4 assimilates AOD and is "
     "biased in the IGP, and emission inventories under-count agricultural and residential burning there, which "
     "inflates the efficiency ratio. Relevance: moderate - quantifies what reanalysis cannot replace ground networks for.")),
 dict(pmid="", doi="10.64898/2026.10.16.26365732", journal="medRxiv (preprint)",
  short="Falcon-Gracia BiSC placental sncRNA air pollution maternal smoking 2026",
  title="Impact of air pollution and tobacco smoke on the placental small non-coding RNA landscape",
  sub=corpus.REPR, design="Cross-sectional (birth cohort)", pm="Prenatal PM2.5, black carbon, NO2 (hybrid dispersion-LUR)",
  geo="Spain (Barcelona, BiSC)", endpoint="Placental small non-coding RNA expression", tier="B",
  n=("390 chorionic villus samples from the Barcelona Life Study Cohort, small-RNA sequencing; 979 sncRNA clusters "
     "(miRNA 33%, piRNA 26%, snoRNA 12%, tRF 8%). Maternal smoking was associated with miR-421 down-regulation and "
     "up-regulation of SNORD113/114 snoRNAs at the imprinted DLK1-DIO3 locus and piR-26394. No sncRNA was associated "
     "with PM2.5, BC or NO2 after multiple-testing correction; several miRNAs were suggestive. Limitation: preprint; "
     "a null after FDR across ~1000 features at n=390 says little about effect absence, and pregnancy-average LUR "
     "exposure is a blunt contrast for trimester-specific placental biology. Relevance: low - a usefully reported null "
     "for PM against a positive smoking control.")),
 dict(pmid="42898877", doi="10.5187/jast.2500087", journal="J Anim Sci Technol",
  short="Kim pig building air cleaner TSP PM2.5 productivity 2026",
  title="Association between indoor air pollutants and pig productivity index by on-site application of air cleaner",
  sub=corpus.OCC, design="Intervention field trial (non-randomised)", pm="TSP, PM2.5, airborne fungi in pig housing",
  geo="South Korea (commercial pig farm)", endpoint="Pig weight gain, feed conversion, activity, mortality", tier="C",
  n=("One commercial pig building, control vs air-cleaner-treated room, monitored six months across rearing stages. "
     "Air-cleaner reduction efficiency rose with stage, 5-10% at farrowing to 30-45% at fattening; treated rooms showed "
     "better weight gain, feed conversion, activity index and mortality. Weight gain and activity correlated with TSP "
     "and PM2.5 (and airborne fungi). Limitation: one room per arm, no randomisation or replication - room effects "
     "are inseparable from treatment; the cleaner technology and PM instrumentation are not stated. Relevance: low - "
     "livestock housing is a large agricultural PM source and an occupational exposure for farm workers, but this "
     "design supports neither inference.")),
]
