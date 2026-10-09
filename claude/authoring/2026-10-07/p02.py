# -*- coding: utf-8 -*-
P = [
 dict(pmid="42842776", doi="10.1093/schbul/sbag138", journal="Schizophr Bull",
  short="ABCD air pollution 2026",
  title="The Relationship between Air Pollution Exposure, Genetic Liability for Schizophrenia, and Brain Outcomes in the ABCD Study",
  sub=corpus.NEU, design="Prospective cohort",
  pm="Modelled annual PM2.5, NO2 and O3 at age 9-10",
  geo="USA (ABCD Study)", endpoint="Cortical surface area, subcortical volume, functional connectivity at 13-14", tier="B",
  n=("1,580 adolescents with genotype, age 9-10 exposure and structural plus resting-state MRI at 13-14; "
     "linear mixed-effects models with a schizophrenia polygenic score as moderator. Higher PM2.5 was "
     "associated with smaller right frontal pole surface area (p-FDR 0.039); the PRS interactions were "
     "non-monotonic - among low-PRS individuals, higher PM2.5 went with larger bilateral caudate volumes, "
     "while low-PRS/medium-PM2.5 showed smaller left caudate than medium/medium. Higher NO2 was "
     "associated with stronger negative connectivity between networks. Limitation: a single surviving "
     "FDR-corrected main effect across a very large imaging search space, and interaction patterns that "
     "do not order monotonically in either PRS or exposure, is the signature of noise - the authors' own "
     "'first test' framing is the right reading. Relevance: moderate - the exposure is a modelled annual "
     "surface at the residence of adolescents who move around a city all day.")),

 dict(pmid="42840018", doi="10.3389/fpubh.2026.1921126", journal="Front Public Health",
  short="Kazakhstan PRISm 2026",
  title="Occupational associations of preserved ratio impaired spirometry (PRISm) in a population-based study",
  sub=corpus.OCC, design="Observational - cross-sectional",
  pm="Lifetime occupational vapour, gas, dust and fume exposure by job-exposure matrix; no PM measured",
  geo="Kazakhstan (Aktobe, Karaganda, Kostanay)", endpoint="Preserved ratio impaired spirometry", tier="B",
  n=("2,275 adults from the general population with spirometry and a lifetime job-exposure matrix. PRISm "
     "prevalence was 12% (95% CI 10.7-13.3), higher in women (14%) than men (10%). Occupational airborne "
     "exposure including VGDF was not associated with PRISm, as ever-exposure or cumulative years; BMI was "
     "(adjusted OR 1.05 per unit). Limitation: a job-exposure matrix built for European job titles applied "
     "to Kazakh work histories misclassifies heavily and will null out a real association; cross-sectional "
     "design cannot separate PRISm from healthy-worker selection out of dusty jobs. Relevance: moderate - "
     "a clean negative in a heavily industrial country, and a direct argument for measured rather than "
     "matrix-assigned occupational exposure.")),

 dict(pmid="", doi="10.21203/rs.3.rs-10637757/v1", journal="Research Square (preprint)",
  short="Calabar ZigBee WSN 2026",
  title="Design and Performance Evaluation of a ZigBee-Based Wireless Sensor Network for CO and PM2.5 Air Quality Monitoring in Calabar Metropolis",
  sub=corpus.SENS, design="Instrument development",
  pm="Low-cost CO and PM2.5 nodes on an IEEE 802.15.4 ZigBee mesh, with MATLAB models of sensing, link, energy and dispersion",
  geo="Nigeria (Calabar)", endpoint="None (network performance)", tier="C",
  n=("A ZigBee mesh of low-cost CO and PM2.5 nodes, with analytical models for sensing, communication, "
     "energy use and dispersion exercised in MATLAB. Reported: reliable links, coverage growing with node "
     "count, a lifetime of about 4,065 transmissions, mean CO 30 ppm, mean PM2.5 40 ug/m3, AQI 112.5, and "
     "a composite 'performance index' of 76.5%. Limitation: the central weakness is that no calibration, "
     "co-location or reference comparison is reported at all - a 40 ug/m3 mean from uncalibrated optical "
     "nodes in a humid tropical city is not a measurement, and a self-defined performance index is not a "
     "validation; the dispersion component is simulated, not observed. Relevance: moderate as a record of "
     "the deployment gap in West Africa, where ambient data is genuinely absent; low as evidence. This is "
     "the failure mode this watch exists to flag.")),

 dict(pmid="42843035", doi="10.1016/j.ecoenv.2026.120879", journal="Ecotoxicol Environ Saf",
  short="Melatonin DPM2.5 2026",
  title="Melatonin protects keratinocytes from diesel-derived PM2.5-induced damage by suppressing JNK/p38 MAPK signaling and caspase activation",
  sub=corpus.MECH, design="Animal + in vitro",
  pm="Diesel-derived PM2.5 applied to HaCaT keratinocytes and to HR-1 hairless mice",
  geo="South Korea (laboratory)", endpoint="Keratinocyte oxidative injury and apoptosis", tier="C",
  n=("Diesel PM2.5 raised intracellular ROS, damaged macromolecules, disrupted mitochondrial membrane "
     "potential and drove apoptosis in HaCaT cells; melatonin scavenged radicals, restored viability and "
     "membrane potential, partly restored Bcl-2 against raised Bax and Bim, and suppressed caspase-9 and "
     "-3 and JNK/p38 MAPK activation, with a hairless-mouse arm. Limitation: the same template as the "
     "curcumin-nanosphere record on 3 October - a protective-agent paper in which the PM arm is a generic "
     "oxidant stimulus, with no composition, no dose-response against a deposited-dose estimate and no "
     "endotoxin control; diesel PM is a reference material, not an ambient aerosol. Relevance: low as "
     "mechanism; logged to keep the dermal-endpoint strand complete and because the DPM2.5 reference "
     "material is at least characterised, unlike most such papers.")),
]
