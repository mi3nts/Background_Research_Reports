# -*- coding: utf-8 -*-
P = [
 dict(pmid="42944937", doi="10.1007/s10661-026-16083-6", journal="Environ Monit Assess",
  short="Wang PM2.5-bound PAH association rules machine learning forecasting Nagoya 2026",
  title="Characterizing statistical association patterns and local forecasting of PM2.5-bound polycyclic aromatic hydrocarbon concentrations in Nagoya, Japan",
  sub=corpus.SENS, design="Machine-learning model", pm="Hourly PM2.5-bound PAHs, BC, NOx, oxidants, meteorology",
  geo="Japan (Nagoya)", endpoint="Not applicable (hourly PAH prediction; incremental lifetime cancer risk)", tier="C",
  n=("Hourly PM2.5-bound PAHs in Nagoya with association-rule mining and ML under time-blocked cross-validation. Low wind "
     "speed was the most consistent condition for PAH accumulation; BC and NOx peaked at rush hours. XGBoost and RF "
     "predicted high-molecular-weight PAHs best (R2 0.81-0.93, RMSE 0.02-0.11); SVR and MLP were poor. BaP dominated "
     "toxicity; lifetime cancer risks were below the USEPA negligible threshold. Limitation: a 10-day observation period, "
     "so the models learn one synoptic episode, and the authors themselves restrict the rules to site-specific "
     "description. Relevance: moderate - a BC-plus-meteorology proxy for PAHs is the kind of virtual sensor a network "
     "could run, if trained on far longer records.")),
 dict(pmid="42940685", doi="10.3390/children13101366", journal="Children (Basel)",
  short="Lovric ragweed sensitisation PM10 pollen model comparison Croatia ATOPICA 2026",
  title="Outdoor Environmental Risk Factors for Paediatric Ragweed Sensitisation: A Formal Model Comparison",
  sub=corpus.RESP, design="School-based cross-sectional", pm="Area-level PM10 and NO2; regional ragweed pollen; CORINE land cover (5 km)",
  geo="Croatia (ATOPICA / EDIAQI)", endpoint="Ragweed skin-prick sensitisation (wheal >=2 mm)", tier="B",
  n=("Re-analysis of 3,520 Croatian children from ATOPICA within EDIAQI; logistic models compared by AIC, adjusted for "
     "age and parental atopy. Sensitisation prevalence 10.8%. PM10 and categorical pollen area fit equally well "
     "(delta AIC 1.7) because both encode the same inland-coastal contrast; NO2 added nothing. Transitional "
     "woodland-shrub aOR 0.93 (0.90-0.97) survived Bonferroni; rural residence aOR 0.69 (0.50-0.96). Limitation: the "
     "authors state it directly - area-level exposure cannot separate particulate pollution from pollen, so a PM "
     "contribution can be neither confirmed nor excluded. Relevance: moderate - an explicit case where only "
     "sub-regional, co-located PM and pollen measurement could break the collinearity.")),
]
