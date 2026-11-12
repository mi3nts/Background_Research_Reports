# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-10/_rec.py", encoding="utf-8").read(), globals())
P = [
 R(81, "arXiv (preprint)",
  short="Tohidian Elia denoising neural processes input uncertainty PM2.5 spatial interpolation air quality sensors 2026",
  sub=corpus.SENS, design="Method / algorithm",
  pm="PM2.5 from real-world air-quality sensor networks used as a spatial-interpolation benchmark",
  geo="Not stated", endpoint="Interpolation RMSE and negative log-likelihood", tier="B",
  basis="Low-cost sensor / network", affil="",
  n=("Preprint. Denoising Neural Processes extend the neural-process meta-learner to treat inputs as noisy, trained by variational inference, "
     "with a proof that the Bayes-optimal predictor under input noise lies in the model class and that fixed-variance plug-in models carry an "
     "irreducible KL gap. On PM2.5 spatial interpolation from real-world air-quality sensors the method cut RMSE by up to 30% and NLL by up to "
     "73% against standard neural processes. The abstract names neither the network, its sensor type nor the baseline beyond vanilla NPs, so "
     "'real-world sensors' cannot be placed against kriging or calibrated-network practice. "
     "Relevance: modelling noisy and mis-located sensor inputs explicitly is exactly the low-cost network problem; worth reading if the PM "
     "data are PurpleAir-class.")),
 R(82, "Environ Monit Assess",
  short="Punjab ARIMA LSTM NARX forecasting Deep Blue AOD550 Thar Thal Karakum Kutch Kyzylkum Arabian deserts 2000-2030",
  sub=corpus.SENS, design="Benchmark / forecasting model comparison",
  pm="Monthly satellite AOD550 (MODIS Deep Blue), six Asian deserts",
  geo="Asia", endpoint="Test RMSE and R2; 6-year AOD projection", tier="C",
  basis="Satellite-fused", affil="Swami Premanand Mahavidyalaya, India; Guru Nanak Dev University College, India",
  n=("294 monthly Deep Blue AOD550 values (Feb 2000-Jul 2024) for the Thar, Thal, Karakum, Kutch, Kyzylkum and Arabian deserts; ARIMA, LSTM "
     "and NARX evaluated on a 44-month test set. NARX was best (test RMSE 0.0180-0.0275) over LSTM (0.0215-0.0350, R2 0.53-0.70) and ARIMA "
     "(0.0250-0.0400, R2 0.40-0.60), and was used to project AOD to July 2030. Monthly means of a column optical quantity carry no surface "
     "PM information, and a six-year recursive forecast from 250 training points has no credible uncertainty statement. "
     "Relevance: marginal - desert dust is the regime where AOD-to-PM2.5 conversion and optical low-cost sensors both fail, but this "
     "paper does not touch the surface.")),
 R(56, "Atmosphere",
  short="Anhui WRF-Chem GOCART Shao KOK dust schemes February 2026 East Asian dust storm size-resolved PM10 Gobi source attribution",
  sub=corpus.EXPO, design="Chemical transport model",
  pm="Size-resolved mineral dust contribution to surface PM10 and AOD, WRF-Chem with three emission schemes",
  geo="China", endpoint="AOD skill (R, RMSE), dust mass by size bin, source attribution", tier="C",
  basis="Model (CTM / LUR / ML)", affil="Anhui & Huaihe River Institute of Hydraulic Research, China; Anhui Institute of Meteorological Sciences, China",
  n=("WRF-Chem case study of the 18-23 February 2026 dust storm that reached the Yangtze basin, comparing GOCART, Shao2001 and KOK emission "
     "schemes. A tuned GOCART run matched observed AOD best (R 0.74, RMSE 0.16). Size bins 5-8 supplied over 90% of dust mass in surface PM10; "
     "regional emission peaked above 4.0 Tg on 20 February while area-mean loading peaked at about 90 mg/m2 a day later; the Gobi supplied about "
     "two-thirds of the loading. Validation is against AOD, not surface PM10 monitors, and one event cannot rank schemes. "
     "Relevance: coarse-dominated dust episodes are where PM2.5-tuned optical sensors under-read PM10 most; event-specific size splits like "
     "this are what a dust correction needs.")),
 R(9, "Nat Commun",
  short="Zhang Peking deep neural network global surface HONO reconstruction 2005-2021 megacities ozone particulate nitrate drivers",
  sub=corpus.EXPO, design="Data-fusion / ML surrogate model",
  pm="Secondary PM2.5 (particulate nitrate) and ozone driven by reconstructed surface HONO",
  geo="Global / multi-region", endpoint="HONO trends and attributed O3 / nitrate change", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Peking University, China; Peking University, China",
  n=("A deep neural network trained on worldwide field campaigns reconstructs surface HONO; Beijing fell 47.4% (2013-2021), Delhi rose 10.0% "
     "(2005-2018), and London, New York and Los Angeles declined slightly. HONO change is identified as a major driver of ozone and particulate "
     "nitrate variation, outweighing NOx and VOC abatement in Beijing and Delhi, and the framework recommends NOx control in summer and joint "
     "NOx, PM2.5 and direct-combustion cuts in winter. HONO is sparsely measured and campaign-biased, so the reconstruction and the "
     "attribution share one learned model; no uncertainty on the nitrate share is given in the abstract. "
     "Relevance: indirect - explains nitrate-driven PM2.5 trends that sensor networks record but cannot apportion.")),
]
