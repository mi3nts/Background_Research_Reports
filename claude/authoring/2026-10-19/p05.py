# -*- coding: utf-8 -*-
P = [
 dict(pmid="", doi="10.1016/j.buildenv.2026.115449", journal="Build Environ",
  short="Ren physics-constrained UQ urban PM2.5 prediction driving factors 2026",
  title="Integrating Implicit Physics Constraints and Uncertainty Quantification for Urban PM2.5 Prediction and Driving Factor Analysis",
  sub=corpus.SENS, design="Metadata only (no abstract)", pm="Urban PM2.5 (prediction target)",
  geo="Not stated in record", endpoint="Not applicable (prediction skill, uncertainty)", tier="C",
  n=("Title and authors only; no abstract retrievable at harvest. The title describes an urban PM2.5 prediction model "
     "with implicit physics constraints and uncertainty quantification, plus driving-factor attribution. Architecture, "
     "city, input features, horizon, skill metrics and whether the uncertainty is calibrated cannot be stated. "
     "Limitation: 'implicit' physics constraints in ML usually mean loss-function regularisation, which does not "
     "guarantee physical consistency out of distribution; nothing beyond the title is verifiable. Relevance: moderate - "
     "calibrated predictive uncertainty is what allows LCS-fed forecasts to propagate sensor error honestly.")),
 dict(pmid="", doi="10.1016/j.buildenv.2026.115399", journal="Build Environ",
  short="Suh residential occupant activities airborne microplastic emissions 2026",
  title="Microplastics emissions from occupant activities in residential spaces: Experimental quantification and relative importance analysis of particle generation factors",
  sub=corpus.OCC, design="Metadata only (no abstract)", pm="Airborne microplastic particles from occupant activities",
  geo="Not stated in record", endpoint="Not applicable (emission quantification)", tier="C",
  n=("Title and authors only; no abstract retrievable at harvest. The title reports experimental quantification of "
     "microplastic particle emissions from occupant activities in residential spaces and a relative-importance analysis "
     "of generation factors (activity type, textiles, surfaces presumably). Size range, identification method (FTIR, "
     "Raman, pyrolysis GC-MS), emission rates and whether the inhalable fraction was measured cannot be stated. "
     "Limitation: unverifiable beyond the title; microplastic counts are method-bound and seldom expressed as PM mass. "
     "Relevance: moderate - indoor activity-resolved particle sources are what household LCS see as unexplained spikes; "
     "polymer fibres also scatter differently from combustion aerosol.")),
 dict(pmid="", doi="10.1016/j.indenv.2026.100200", journal="Indoor Environments",
  short="Du classroom CO2 proxy PM VOC ventilation types 2026",
  title="CO2 as a proxy for PM and VOCs in classrooms across ventilation types and activities",
  sub=corpus.OCC, design="Metadata only (no abstract)", pm="Classroom PM (fractions not stated) vs CO2 and VOCs",
  geo="Not stated in record", endpoint="Not applicable (proxy validity)", tier="B",
  n=("Title and authors only; no abstract retrievable at harvest. The title tests whether CO2 tracks PM and VOCs in "
     "classrooms across ventilation types and activities - i.e. whether a cheap NDIR sensor can stand in for particle "
     "and VOC monitoring. Number of classrooms, ventilation categories, PM instrumentation and agreement statistics "
     "cannot be stated. Limitation: unverifiable beyond the title; physically, CO2 tracks occupant-generated "
     "bioeffluents and air exchange, whereas PM indoors also depends on outdoor infiltration, resuspension and "
     "filtration, so decoupling under mechanical ventilation is expected. Relevance: high - directly asks whether "
     "school CO2 monitor rollouts can be read as PM exposure surveillance.")),
]
