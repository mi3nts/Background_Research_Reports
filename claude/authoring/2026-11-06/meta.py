# -*- coding: utf-8 -*-
W = "2026-11-06 -> 2026-11-06"
E = [
 dict(label="Asthma ED visit\nLima, lag 0", exposure="PM2.5 5 -> 15 ug/m3 (per 10 ug/m3), 1-km model at residence", est=1.09, lo=1.01, hi=1.16, metric="OR", src="Espinoza-Guillen n=75,602", inc="per 10 µg/m³"),
 dict(label="Hospital-acquired pneumonia\npost-cardiac surgery", exposure="PM2.5 30 vs 10 ug/m3, city monitors, lag 1", est=1.142, lo=1.026, hi=1.27, metric="OR", src="Li Shandong ICU n=6,196", inc="categorical contrast"),
 dict(label="Seroconversion\nhigh vs low mining dust", exposure="Self-reported occupational dust, high vs low", est=0.42, lo=0.17, hi=1.07, metric="aOR", src="Kim coal miners n=230", inc="categorical contrast"),
 dict(label="HbA1c, T1D", exposure="PM2.5 per IQR, 5-y residential mean", est=1.07, lo=1.03, hi=1.11, metric="GMR", src="Singh GDS n=417", inc="per IQR / SD"),
 dict(label="Albuminuria, T1D", exposure="PM2.5 per IQR, 5-y residential mean", est=1.72, lo=1.34, hi=2.20, metric="GMR", src="Singh GDS n=417", inc="per IQR / SD"),
 dict(label="HbA1c, T2D", exposure="PM2.5 per IQR, 5-y residential mean", est=1.04, lo=1.01, hi=1.06, metric="GMR", src="Singh GDS n=703", inc="per IQR / SD"),
 dict(label="Albuminuria, T2D", exposure="PM2.5 per IQR, 5-y residential mean", est=1.71, lo=1.41, hi=2.08, metric="GMR", src="Singh GDS n=703", inc="per IQR / SD"),
 dict(label="Polyneuropathy (DSPN), T2D", exposure="PM2.5 per IQR, 5-y residential mean", est=1.53, lo=1.02, hi=2.32, metric="OR", src="Singh GDS n=703", inc="per IQR / SD"),
]
L = [
 dict(n=0, note=""),
 dict(n=2, note="children:\nLima asthma ED;\nSomalia under-five"),
 dict(n=1, note="adolescents:\nLima asthma ED\n(mean age 16)"),
 dict(n=5, note="working age:\ncoal miners; metro\nworkers; diabetes cohort;\nICU HAP; AML review"),
 dict(n=4, note="older adults:\nneuro review; CKD\ndementia; ICU HAP >=60;\nCarVasCLiMa"),
]
