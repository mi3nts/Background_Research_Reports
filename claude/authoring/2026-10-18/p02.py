# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.22373/ljee.v7i1.10530", journal="Lingkar: J Environ Eng",
  short="Risti Jambi PMS5003 PMS7003 vs BAM-1020 2026",
  title="Evaluation of Low-Cost PM2.5 Sensor Accuracy in Comparison with Government Reference Instrument",
  sub=corpus.SENS, design="Co-location calibration campaign", pm="Plantower PMS5003 and PMS7003 vs BAM-1020 PM2.5",
  geo="Indonesia (Jambi)", endpoint="Not applicable (sensor evaluation)", tier="B",
  n=("Consensus sweep. IoT nodes with two Plantower sensors co-located with the BMKG BAM-1020 at the Sultan Thaha Jambi "
     "climatology station, December 2025-January 2026, followed by linear-regression correction. Both tracked the "
     "reference moderately (R2 0.60 PMS5003, 0.59 PMS7003) and overestimated: PMS7003 MBE 10.46, MAE 12.53, RMSE 18.02 "
     "ug/m3; PMS5003 MBE 11.84, MAE 13.60, RMSE 19.60 ug/m3. The authors attribute the positive bias to high humidity. "
     "Limitation: two wet-season months at one site, no RH-stratified or kappa-Kohler correction and no held-out "
     "validation of the regression, so the correction will not transfer to the dry or haze seasons. Relevance: high - "
     "an equatorial reference co-location adds to the regional-calibration evidence; the 10 ug/m3 bias matches "
     "humid-tropics PurpleAir behaviour.")),
 dict(pmid="42893462", doi="10.1007/s10661-026-16062-x", journal="Environ Monit Assess",
  short="Huang foliar particulate UV-Vis-NIR calibration transfer 2026",
  title="Nondestructive UV-Vis-NIR assessment of foliar particulate retention in urban vegetation: cross-species transfer and calibration correction",
  sub=corpus.SENS, design="Spectroscopic calibration-transfer study", pm="Leaf-surface particulate mass per area (washing-filtration reference)",
  geo="China (Nanjing)", endpoint="Not applicable (measurement method)", tier="B",
  n=("Reflectance models built on 180 Ligustrum leaves and transferred to 45 Photinia leaves from park, street and "
     "industrial zones. Zone classification reached 91.1% after excluding endpoint and water bands. Direct mass "
     "prediction on the target species failed (R2 0.265, positive bias); a linear output correction using 15 target "
     "reference leaves (five per zone), tested on the other 30 over 50 splits, gave R2 0.797 +/- 0.042. Limitation: "
     "target-based scheme selection and the correction set share zones with the test set, and deposit properties are "
     "unmeasured, so this is reference-assisted local calibration, not transfer. Relevance: moderate - the same "
     "slope-and-offset recalibration logic, and the same failure of naive transfer, governs moving LCS calibrations "
     "between sites.")),
 dict(pmid="", doi="10.1016/j.buildenv.2026.115452", journal="Build Environ",
  short="Chen ambient PM2.5 representativeness children microenvironments 2026",
  title="Evaluating the representativeness of ambient PM2.5 for children's exposure and source characteristics across microenvironments during school semesters",
  sub=corpus.EXPO, design="Metadata only (no abstract)", pm="Ambient vs microenvironmental PM2.5 (instrumentation not stated)",
  geo="Not stated in record", endpoint="Children's personal / microenvironmental exposure", tier="C",
  n=("No abstract at harvest. The title indicates a comparison of ambient PM2.5 with children's exposure and source "
     "profiles across school-semester microenvironments. Recorded for coverage; no estimate inferred. Relevance: high "
     "in principle - quantifying the ambient-to-personal gap for children is precisely what portable low-cost monitors "
     "are deployed for, and the full text should be checked.")),
 dict(pmid="42892432", doi="10.1016/j.envres.2026.125931", journal="Environ Res",
  short="Matuskova wood stove phase-resolved particle-bound PAHs 2026",
  title="Characterisation of particle-bound PAHs emitted from a residential wood-burning stove and their dependence on combustion phases",
  sub=corpus.OCC, design="Chamber emission characterisation", pm="Cascade-impactor size-resolved PM and particle-bound PAHs (GC-MS/MS)",
  geo="Central Europe (laboratory stove; beech, black locust, spruce)", endpoint="Not applicable (emission characterisation)", tier="B",
  n=("Three temperate wood species burned in a standard residential stove, aerosol split by cascade impactor across "
     "five combustion phases. PM peaked at ignition and flaming; PAHs followed for spruce and black locust, while beech "
     "peaked later (interval 4), coinciding with low flue-gas oxygen. Size distributions were monomodal at ~0.1 um "
     "aerodynamic diameter with PM1 70-89% of mass. Hardwoods emitted mainly LMW PAHs; spruce gave an initial HMW "
     "burst, shifting to LMW during burnout, when PAHs moved towards coarser particles. Limitation: one stove under "
     "nominal operation; real-world overloading and damp fuel dominate emissions. Relevance: moderate - an ~0.1 um mode "
     "sits below optical LCS detection efficiency, so wood-smoke PM is under-counted by size-blind calibrations.")),
]
