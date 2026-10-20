# -*- coding: utf-8 -*-
# HELD 2026-10-20: arXiv DataCite DOI not yet registered (404). Re-run check_dois and add to the next issue.
P = [
 dict(pmid="", doi="10.48550/arXiv.2610.25941", journal="arXiv (preprint)",
  short="Kheder Foehn generative km-scale global PM2.5 forecast 2026",
  title="Global probabilistic forecasting of air pollution",
  sub=corpus.SENS, design="Deep-learning forecasting", pm="Global kilometre-scale PM2.5 estimates (training and target)",
  geo="Global", endpoint="Not applicable (forecast skill vs stations)", tier="A",
  n=("Foehn, a generative model trained on global kilometre-scale PM2.5 estimates that also computes air-mass origin. "
     "In one year of retrospective forecasts it beat the operational forecast at three of four stations; its ensembles "
     "are reported as calibrated, and the ensemble mean detects local pollution extremes four days ahead about as well "
     "as the operational system does one day ahead. Limitation: preprint; 'kilometre-scale estimates' are themselves "
     "satellite/model fusion products, so skill is partly measured against the training distribution, and the authors "
     "concede real-time km-scale inputs do not yet exist - operational use is hypothetical. Skill metrics and station "
     "counts are not given in the abstract. Relevance: high - calibrated LCS networks are the plausible real-time "
     "km-scale input this model says it lacks.")),
]
