# -*- coding: utf-8 -*-
W = "2026-11-20 -> 2026-11-20"
E = [
 dict(label="CKM progression,\nPM2.5 overall", exposure="365-day mean PM2.5 per IQR (5.008 ug/m3); multistate Cox, Shenzhen cohort", est=1.054, lo=1.030, hi=1.078, metric="HR", src="Shenzhen CKM", inc="per IQR / SD"),
 dict(label="CKM early progression,\nPM2.5", exposure="365-day mean PM2.5 per IQR (5.008 ug/m3); transition to CKM stages 1-2", est=1.073, lo=1.030, hi=1.118, metric="HR", src="Shenzhen CKM", inc="per IQR / SD"),
 dict(label="CKM advanced progression,\nPM2.5", exposure="365-day mean PM2.5 per IQR (5.008 ug/m3); transition to CKM stages 3-4", est=1.055, lo=1.027, hi=1.085, metric="HR", src="Shenzhen CKM", inc="per IQR / SD"),
 dict(label="Under-five mortality,\nPM2.5", exposure="Satellite annual mean PM2.5 per 10 ug/m3; survey-adjusted logistic, NFHS-5 clusters", est=1.07, lo=1.04, hi=1.10, metric="aOR", src="India NFHS-5 preprint", inc="per 10 µg/m³"),
 dict(label="Under-five mortality,\n>80 vs <40 ug/m3", exposure="Satellite annual mean PM2.5 above 80 vs below 40 ug/m3; survey-adjusted logistic", est=1.40, lo=1.17, hi=1.67, metric="aOR", src="India NFHS-5 preprint", inc="categorical contrast"),
 dict(label="Dementia,\ntraffic-exhaust PM2.5", exposure="Dispersion-modelled vehicular-exhaust PM2.5 per 0.1 ug/m3; Cox, FINRISK Helsinki/Vantaa", est=0.95, lo=0.85, hi=1.05, metric="HR", src="FINRISK dementia", inc="per 1 µg/m³ / unit"),
 dict(label="Dementia,\nwood-combustion PM2.5", exposure="Dispersion-modelled residential-wood-combustion PM2.5 per 0.1 ug/m3; Cox, FINRISK", est=1.23, lo=0.79, hi=1.92, metric="HR", src="FINRISK dementia", inc="per 1 µg/m³ / unit"),
 dict(label="Respiratory OPD visits,\nAQHI 7 vs median", exposure="Bangkok AQHI 7 vs citywide median, same day; DLNM on 23-hospital outpatient counts", est=1.023, lo=1.004, hi=1.042, metric="RR", src="Bangkok AQHI", inc="categorical contrast"),
 dict(label="Live-birth-identified\nconceptions, PM2.5 wk21", exposure="County weekly PM2.5 per 10 ug/m3, gestational week 21; quasi-Poisson DLNM (RR<1 = more loss)", est=0.993, lo=0.990, hi=0.995, metric="RR", src="New Jersey pregnancy loss", inc="per 10 µg/m³"),
 dict(label="Incident IHD,\nPM2.5 (administrative)", exposure="Residential PM2.5 per one-quartile increment; % higher IHD incidence, 6 administrative cohorts", est=1.4, lo=0.8, hi=1.9, metric="% change", src="Europe exposome IHD", inc="per IQR / SD"),
 dict(label="Incident IHD,\nPM10 (administrative)", exposure="Residential PM10 per one-quartile increment; % higher IHD incidence", est=0.9, lo=0.1, hi=1.7, metric="% change", src="Europe exposome IHD", inc="per IQR / SD"),
 dict(label="Incident IHD,\nair-pollution domain", exposure="Air-pollution domain (PM2.5, PM10, NO2) per one-quartile increment, quantile g-computation", est=2.5, lo=1.9, hi=3.1, metric="% change", src="Europe exposome IHD", inc="per IQR / SD"),
]
L = [
 dict(n=3, note="New Jersey pregnancy loss;\nUrumqi heating-season\nbirth outcomes; rat DPM\nco-exposure"),
 dict(n=2, note="India under-five mortality;\nnear-roadway developmental\nexposure (metadata only)"),
 dict(n=0, note=""),
 dict(n=2, note="Bangkok outpatient visits;\nThailand dengue incidence"),
 dict(n=6, note="Shenzhen CKM cohort;\nCHARLS cognition; Fuzhou\npersonal exposure; FINRISK\ndementia; DRC dementia;\nEurope IHD"),
]
