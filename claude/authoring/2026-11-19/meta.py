# -*- coding: utf-8 -*-
W = "2026-11-19 -> 2026-11-19"
E = [
 dict(label="CRC death,\nPM2.5", exposure="1-year lagged residential PM2.5 per 5 ug/m3 (CHAP); time-varying Cox, all-cause death after CRC resection", est=1.079, lo=1.045, hi=1.115, metric="HR", src="Chongqing CRC cohort"),
 dict(label="CRC death,\nPM10", exposure="1-year lagged residential PM10 per 5 ug/m3 (CHAP); time-varying Cox", est=1.050, lo=1.027, hi=1.074, metric="HR", src="Chongqing CRC cohort"),
 dict(label="CRC death,\nPM2.5 organic matter", exposure="1-year lagged PM2.5 organic matter per IQR (TAP); time-varying Cox", est=1.088, lo=1.028, hi=1.152, metric="HR", src="Chongqing CRC cohort", inc="per IQR / SD"),
 dict(label="Incident stroke,\nPM10", exposure="Annual satellite-ML PM10 per 10 ug/m3; Cox, CHARLS adults 45+", est=1.144, lo=1.101, hi=1.188, metric="HR", src="CHARLS stroke", inc="per 10 µg/m³"),
 dict(label="COVID-19 cases,\nPM2.5 pooled", exposure="Daily PM2.5 per 10 ug/m3; pooled RR from GAM + spatial meta-autoregression, contiguous US", est=1.0341, lo=1.0308, hi=1.0375, metric="RR", src="US COVID clusters", inc="per 10 µg/m³"),
 dict(label="Child ICA-cIMT,\nearly-life PM2.5", exposure="Pregnancy + first-year PM2.5 (increment not stated); % change in internal carotid IMT", est=8.49, lo=3.09, hi=14.17, metric="% change", src="Wuhan child cIMT"),
 dict(label="Child CCA-cIMT,\nearly-life PM2.5", exposure="Pregnancy + first-year PM2.5 (increment not stated); % change in common carotid IMT", est=2.87, lo=0.71, hi=5.09, metric="% change", src="Wuhan child cIMT"),
]
L = [
 dict(n=1, note="Wuhan cIMT\n(pregnancy window)"),
 dict(n=3, note="Wuhan cIMT first year;\nIllinois paediatric asthma;\nNSCH chronic pain"),
 dict(n=1, note="NSCH chronic pain\n(ages 0-17)"),
 dict(n=4, note="LHON carriers; CRC patients;\nBangkok ED; milling markets"),
 dict(n=2, note="RoCAV men 50-75;\nCHARLS adults 45+"),
]
