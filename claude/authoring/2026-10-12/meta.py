# -*- coding: utf-8 -*-
W = "2026-10-12 -> 2026-10-12"
E = [
 dict(label="All-cause admissions\nPM2.5 (6 countries)", exposure="Short-term PM2.5 per 10 ug/m3",
      est=1.080, lo=1.074, hi=1.086, metric="RR", src="346.5 M admissions, 949 communities"),
 dict(label="Malignant neoplasm admissions\nPM2.5 (6 countries)", exposure="Short-term PM2.5 per 10 ug/m3",
      est=1.108, lo=1.094, hi=1.123, metric="RR", src="346.5 M admissions, 949 communities"),
 dict(label="Respiratory admissions\nPM2.5 (6 countries)", exposure="Short-term PM2.5 per 10 ug/m3",
      est=1.067, lo=1.060, hi=1.074, metric="RR", src="346.5 M admissions, 949 communities"),
 dict(label="Incident ADRD\nsmoke PM2.5 (per 1 ug/m3)", exposure="Annual wildfire-smoke PM2.5",
      est=1.029, lo=1.024, hi=1.035, metric="HR", src="39.7 M Medicare beneficiaries"),
 dict(label="Incident ADRD\nsmoke carbonaceous (per 1 ug/m3)", exposure="Annual smoke EC+OC",
      est=1.090, lo=1.077, hi=1.103, metric="HR", src="39.7 M Medicare beneficiaries"),
 dict(label="CVD mortality, Lanzhou\nPM2.5 lag 0", exposure="Daily PM2.5 per 10 ug/m3",
      est=1.0206, lo=1.0066, hi=1.0348, metric="RR", src="69,669 deaths, 2015-2023"),
 dict(label="Respiratory admissions, Kinshasa\nPM2.5 lag 0-5 (sensor-based)", exposure="Daily PM2.5 per 10 ug/m3",
      est=1.01, lo=1.00, hi=1.03, metric="OR", src="13,049 adult admissions"),
 dict(label="Accelerated biological aging\npollution mixture (WQS)", exposure="PM2.5/PM10/SO2/O3 mixture",
      est=1.16, lo=1.08, hi=1.24, metric="OR", src="11,760 adults 20-65"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nCHD nested\ncase-control"),
 dict(n=1, note="childhood:\nGambia personal\nPM2.5, 5-14 y"),
 dict(n=1, note="adolescence:\nGambia cohort\n(to 14 y)"),
 dict(n=1, note="working age:\nbiological aging\ncohort, 20-65 y"),
 dict(n=1, note="older adults:\nMedicare smoke\nPM2.5 and ADRD"),
]
