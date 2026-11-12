# -*- coding: utf-8 -*-
W = "2026-11-10 -> 2026-11-10"
E = [
 dict(label="Hemodialysis mortality\nwildfire PM2.5, lag 0", exposure="Wildfire-attributed PM2.5 per 10 ug/m3 at the dialysis facility", est=1.03, lo=1.02, hi=1.06, metric="RR", src="Song ESKD wildfire", inc="per 10 µg/m³"),
 dict(label="Hemodialysis hospitalization\nwildfire PM2.5, lag 0", exposure="Wildfire-attributed PM2.5 per 10 ug/m3 at the dialysis facility", est=1.01, lo=1.00, hi=1.03, metric="RR", src="Song ESKD wildfire", inc="per 10 µg/m³"),
 dict(label="Hemodialysis mortality\nsmoke plume vs none", exposure="Smoke plume present vs absent (categorical contrast), lag 0", est=1.19, lo=1.11, hi=1.27, metric="RR", src="Song ESKD wildfire", inc="categorical contrast"),
 dict(label="Hemodialysis mortality\nplume + extreme heat", exposure="Smoke plume and extreme heat event together vs neither (categorical contrast)", est=1.92, lo=1.71, hi=2.17, metric="RR", src="Song ESKD wildfire", inc="categorical contrast"),
 dict(label="Respiratory mortality\nPM2.5 component mixture", exposure="Quantile g-computation mixture index of six PM2.5 components, per quartile increase", est=1.29, lo=1.23, hi=1.34, metric="HR", src="Huang Pearl River", inc="per IQR / SD"),
 dict(label="Substance use disorder\nPM2.5 (UK Biobank)", exposure="LUR PM2.5, increment not stated in abstract", est=1.111, lo=1.081, hi=1.142, metric="HR", src="Liu UK Biobank"),
 dict(label="Substance use disorder\nPM10 (UK Biobank)", exposure="LUR PM10, increment not stated in abstract", est=1.070, lo=1.054, hi=1.086, metric="HR", src="Liu UK Biobank"),
 dict(label="MS progression (PIRA)\nbaseline PM2.5", exposure="Satellite-derived zip-code PM2.5, baseline annual mean, increment not stated, adjusted", est=1.01, lo=0.96, hi=1.06, metric="HR", src="Lebiedz Brigham MS"),
 dict(label="MS EDSS >= 6\nbaseline PM2.5", exposure="Satellite-derived zip-code PM2.5, baseline annual mean, increment not stated, adjusted", est=1.03, lo=0.94, hi=1.13, metric="HR", src="Lebiedz Brigham MS"),
]
L = [
 dict(n=1, note="ovarian toxicity\n(mouse, reproductive)"),
 dict(n=1, note="GBD burden: under-5\nPM2.5 mortality highest"),
 dict(n=0, note=""),
 dict(n=7, note="UKB SUD; MS cohort;\nPearl River; hemodialysis;\nurolithiasis; ED protocol"),
 dict(n=4, note="burden projection (>=60 y);\nPearl River older adults;\narthritis cohort; hemodialysis"),
]
