# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-10/_rec.py", encoding="utf-8").read(), globals())
P = [
 R(4, "Environ Epidemiol",
  short="Song Fresenius hemodialysis ESKD wildfire smoke plume PM2.5 extreme heat case-crossover mortality West US 2010-2018",
  sub=corpus.OTHR, design="Time-stratified case-crossover",
  pm="Smoke-plume presence (satellite plume polygons) and wildfire-attributed PM2.5 at each dialysis facility; extreme heat events",
  geo="USA", endpoint="All-cause mortality and hospitalization, lag 0", tier="A",
  basis="Model (CTM / LUR / ML)", affil="University of Maryland School of Public Health, USA; University of Maryland School of Public Health, USA",
  n=("55,223 adult hemodialysis patients at Fresenius clinics in California, Oregon and Washington, warm seasons 2010-2018; conditional quasi-Poisson. "
     "A smoke plume overhead raised same-day mortality (RR 1.19, 1.11-1.27); each 10 ug/m3 of wildfire PM2.5 raised mortality 3% (RR 1.03, 1.02-1.06) and "
     "hospitalization 1% (1.01, 1.00-1.03). Plume plus extreme heat gave RR 1.92 (1.71-2.17) against 1.02 (0.95-1.10) for plume alone, so the plume "
     "signal is mostly heat-coincident. Exposure is assigned to the clinic, not the residence, and wildfire PM2.5 is a modelled split of total PM2.5; "
     "the interaction contrast is large enough that residual confounding by heat timing remains the main threat. "
     "Relevance: a dialysis population attends clinics thrice weekly, which makes clinic-sited low-cost monitors a cheap, exact exposure point.")),
 R(43, "Environ Sci Technol Lett",
  short="Huang Wei Pearl River Cohort PM2.5 components NH4 NO3 BC OM SO4 Cl respiratory mortality quantile g-computation South China",
  sub=corpus.RESP, design="Prospective cohort",
  pm="Long-term PM2.5 components (NH4+, NO3-, BC, OM, SO4 2-, Cl-), modelled surfaces",
  geo="China", endpoint="Respiratory disease mortality", tier="A",
  basis="Model (CTM / LUR / ML)", affil="Sun Yat-sen University, China; Sun Yat-sen University, China",
  n=("182,009 Pearl River Cohort participants; marginal structural Cox models for single components and quantile g-computation for the mixture. "
     "All six components raised respiratory mortality, single-component HRs 1.42-2.75 (increments not given in the abstract). Each quartile "
     "increase in the mixture index gave HR 1.29 (1.23-1.34), with nitrate carrying the largest weight (0.48), then organic matter and chloride. "
     "Older adults, non-smokers and non-exercisers were most susceptible (HRs 1.25-2.02). Component surfaces are model products whose errors "
     "are correlated across species, so the weight ranking partly reflects which component the model resolves best; HRs of 1.4-2.8 per "
     "component are implausibly large without the increment. "
     "Relevance: nitrate is the semi-volatile, hygroscopic fraction behind most low-cost-versus-reference disagreement in humid seasons.")),
 R(11, "Research Square (preprint)",
  short="Parthenope independent evaluation Aurora 0.4 degree air pollution foundation model CAMS persistence stations negative PM2.5 2024",
  sub=corpus.SENS, design="Benchmark / forecasting model comparison",
  pm="Forecast PM2.5 and PM10 (Aurora foundation model, 0.4 degree) against CAMS and hourly background stations",
  geo="Global / multi-region", endpoint="MSE skill vs persistence, station MAE, physical consistency, input sensitivity", tier="A",
  basis="Model (CTM / LUR / ML)", affil="Parthenope University of Naples, Italy; Parthenope University of Naples, Italy",
  n=("Preprint. 96 initialisations across 2024 of the released Aurora air-pollution checkpoint, scored against CAMS, persistence and hourly "
     "background stations in three regions. Relative to persistence, Aurora cut MSE by 38.1-42.6% for PM2.5 and 49.1-52.3% for PM10, and its "
     "station MAE beat the benchmark-selected CAMS fields in all six region-pollutant pairs with bootstrap intervals excluding zero. But at +12 h, "
     "6.27% of PM2.5 and 7.84% of PM10 grid values were negative, the model gives no forecast distribution, and its response to perturbed "
     "emission inputs is untested against real emission change. Background stations only, so urban hotspots are unscored. "
     "Relevance: dense low-cost networks are the obvious test bed for exactly the near-source skill this evaluation could not reach.")),
 R(1, "Environ Pollut",
  short="Shenzhen Mini-WRAS size-resolved ultrafine particle hourly forecasting MLR RF XGBoost LSTM history window 2023-2025",
  sub=corpus.SENS, design="Benchmark / forecasting model comparison",
  pm="Ultrafine particle number in eight bins 10-100 nm, Mini-WRAS, one urban site",
  geo="China", endpoint="One-hour-ahead NRMSE by size bin and history window", tier="B",
  basis="Lab / research instrument", affil="Sun Yat-sen University, China; Sun Yat-sen University, China",
  n=("8,982 quality-controlled hourly observations (Sep 2023-Jun 2025) from a Mini-WRAS at an urban Shenzhen site; 270 model-window-target "
     "configurations (MLR, RF, XGBoost, LSTM, BiLSTM; 1-24 h histories) scored on the same 533 test hours. Best NRMSE was 60.2% at 10 nm and "
     "22.1% at 14 nm against 13.4-14.8% at 19-100 nm; a 2 h history was best for 10-19 nm and 4 h for 27-100 nm, while the summed UFP target "
     "reached 13.7% at 12 h. Several model classes tied, so architecture mattered less than window. One site, one-step-ahead, and no "
     "meteorological or traffic covariates are described. "
     "Relevance: aggregate number forecasts hide the poorly predictable nucleation mode, which is also the size range low-cost counters miss.")),
]
