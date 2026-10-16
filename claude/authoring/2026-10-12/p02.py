# -*- coding: utf-8 -*-
P = [
 dict(pmid="42862814", doi="10.1371/journal.pone.0351928", journal="PLoS One",
  short="Nobin Bangladesh GNN PM2.5 2026",
  title="Explainable spatiotemporal Graph Neural Networks: Multi-City PM2.5 forecasting in Bangladesh with geographic graph topology validation",
  sub=corpus.SENS, design="Machine-learning model", pm="Daily PM2.5, 12-city network, 1-3 day forecasts",
  geo="Bangladesh (12 cities)", endpoint="No health endpoint", tier="B",
  n=("Graph-diffusion GRU on four years of daily multi-source data at 12 cities. Up to 3-day lead: MAE 8.85 ug/m3, "
     "R2 0.666, beating non-graph baselines (FDR-corrected Diebold-Mariano p<0.001) and DCRNN when pooled across horizons. "
     "The useful result is negative for complexity: a fixed distance-adjacency graph beat adaptive, wind-informed and "
     "hybrid graphs, and occlusion-based influence tracked geographic adjacency (r=0.928). Limitation: 12 nodes is "
     "too sparse to discriminate graph topologies - transport structure that matters at 10-50 km scale cannot be "
     "resolved by stations hundreds of km apart. Relevance: high - a direct test of what graph priors a denser "
     "LCS network would need before learned adjacency pays off.")),
 dict(pmid="42861645", doi="10.1093/annweh/wxag086", journal="Ann Work Expo Health",
  short="Shai Nanozen RT vs gravimetric 2026",
  title="Comparison of respirable dust concentrations between gravimetric weighing and real-time dust monitoring equipment in non-mining industries",
  sub=corpus.SENS, design="Field measurement", pm="Respirable dust: Nanozen DustCount 9000 optical vs its built-in filter cassette",
  geo="South Africa (Gauteng)", endpoint="No health endpoint", tier="B",
  n=("20 paired task-based stationary samples at 11 industrial sites. No significant difference between gravimetric and "
     "raw real-time (Wilcoxon p=0.067) or density-adjusted (p=0.277); proportional bias grew with concentration but was "
     "absent below 1 mg/m3 (R2 0.06 and 0.02). Limitation: n=20, and the gravimetric reference is the instrument's own "
     "cassette downstream of the same inlet, so inlet losses and size-selection error are shared and invisible to the "
     "comparison; Wilcoxon non-significance at n=20 is not agreement. Relevance: moderate - the 1 mg/m3 cut is a "
     "usable operating limit, and the shared-inlet design is a pattern to avoid in LCS co-location.")),
 dict(pmid="", doi="10.1021/acs.est.6c08137", journal="Environ Sci Technol",
  short="Zhang Fusion-DeepRSM satellite PM2.5 2026",
  title="Fusion-DeepRSM for Satellite-Derived PM2.5 Estimation and Precursor Sensitivity Prediction",
  sub=corpus.EXPO, design="Machine-learning model", pm="Gridded PM2.5 from CTM + multisource satellite + ground fusion",
  geo="China (nationwide)", endpoint="No health endpoint", tier="B",
  n=("Observation-constrained deep response-surface model fusing CTM runs, satellite products and ground PM2.5. "
     "R2 0.872, RMSE 11.82 ug/m3, and a 4.13 ug/m3 reduction in rural overestimation, the known failure of station-trained "
     "ML. It also returns precursor-PM2.5 response surfaces: for 2020-2023, meteorology offset part of emission-driven "
     "improvement (+1.2 vs -1.8 ug/m3), and precursor change drove the Feb 2023 BTH rebound. Limitation: validation "
     "against stations that are themselves inputs; the rural bias correction is quantified on a CTM testbed, not "
     "against independent rural monitors - exactly where LCS would be needed. Relevance: high - a fusion architecture "
     "into which rural sensor nodes would slot as the missing constraint.")),
 dict(pmid="42862460", doi="10.1007/s10661-026-16057-8", journal="Environ Monit Assess",
  short="Salem Riyadh PM2.5 vegetation 2026",
  title="Spatiotemporal variation of PM2.5 and its relationship with vegetation cover and meteorological factors during spring (2016-2022) in Riyadh, Saudi Arabia",
  sub=corpus.EXPO, design="Monitoring-record analysis", pm="Spring PM2.5 from 16 regulatory stations; fractional vegetation cover",
  geo="Saudi Arabia (Riyadh)", endpoint="No health endpoint", tier="C",
  n=("16 stations, spring 2016-2022: seasonal mean PM2.5 ranged from 94.6 (2018) to 55.0 ug/m3 (2020), highest in "
     "southern and central Riyadh. Meteorological correlations were non-significant; the vegetation-PM2.5 inverse "
     "association reached significance in one year only (rho=-0.539, p=0.031, n=16). Limitation: n=16 Spearman "
     "correlations per year cannot separate vegetation from land use, and dust events dominate spring variance; the "
     "one significant year out of seven is consistent with chance. Relevance: low-moderate - documents a dust-dominated "
     "regime where optical sensors' coarse-mode bias would govern any network.")),
]
