# -*- coding: utf-8 -*-
W = "2026-11-05 -> 2026-11-05"
E = [
 dict(label="Sinonasal cancer\n6-month mean", exposure="PM2.5 per SD (~2.5 ug/m3), MSA-level satellite-fused", est=1.25, lo=1.05, hi=1.49, metric="aOR", src="Yang n=21,295", inc="per IQR / SD"),
 dict(label="Sinonasal cancer\n1-year mean", exposure="PM2.5 per SD (~2.5 ug/m3), MSA-level satellite-fused", est=1.31, lo=1.08, hi=1.59, metric="aOR", src="Yang n=21,295", inc="per IQR / SD"),
 dict(label="Sinonasal cancer\n5-year mean", exposure="PM2.5 per SD (~2.7 ug/m3), MSA-level satellite-fused", est=1.36, lo=1.11, hi=1.66, metric="aOR", src="Yang n=21,295", inc="per IQR / SD"),
 dict(label="Influenza\nShanxi PM2.5", exposure="PM2.5 per 10 ug/m3, lag 0-7 d", est=1.024, lo=1.015, hi=1.034, metric="RR", src="Zhang 11 cities", inc="per 10 µg/m³"),
 dict(label="Influenza\nShanxi PM10", exposure="PM10 per 10 ug/m3, lag 0-7 d", est=1.018, lo=1.010, hi=1.025, metric="RR", src="Zhang 11 cities", inc="per 10 µg/m³"),
 dict(label="Lab-confirmed influenza\nShanghai PM10", exposure="PM10 per 10 ug/m3, IDW to address", est=1.019, lo=1.004, hi=1.034, metric="OR", src="Hao Shanghai", inc="per 10 µg/m³"),
]
L = [
 dict(n=0, note=""),
 dict(n=2, note="all ages incl. children:\ninfluenza Shanxi,\nShanghai"),
 dict(n=2, note="all ages incl. adolescents:\ninfluenza Shanxi,\nShanghai"),
 dict(n=5, note="working age:\nfirefighters; mining-dust\nreview; sinonasal (mean 51 y);\ninfluenza x2"),
 dict(n=4, note="older adults:\nCAP cohort; Alzheimer\nreview; influenza x2"),
]
