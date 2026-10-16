# -*- coding: utf-8 -*-
W = "2026-10-09 -> 2026-10-09"
E = [
 dict(label="Incident dementia\nPM2.5 road transport (per IQR)", exposure="Source-specific PM2.5, time-varying",
      est=1.12, lo=1.04, hi=1.21, metric="HR", src="5,648 cases, median 11.9 y follow-up"),
 dict(label="Incident dementia\nPM2.5 other transport (per IQR)", exposure="Source-specific PM2.5, time-varying",
      est=1.12, lo=1.06, hi=1.19, metric="HR", src="5,648 cases, median 11.9 y follow-up"),
 dict(label="Incident dementia\nPM2.5 industry (per IQR)", exposure="Source-specific PM2.5, time-varying",
      est=1.07, lo=1.03, hi=1.11, metric="HR", src="5,648 cases, median 11.9 y follow-up"),
 dict(label="Incident dementia\nPM2.5 domestic (per IQR)", exposure="Source-specific PM2.5, time-varying",
      est=1.05, lo=1.01, hi=1.08, metric="HR", src="5,648 cases, median 11.9 y follow-up"),
 dict(label="30-day readmission, ADRD\nPM2.5 lag 0-2 (per 7.2 ug/m3)", exposure="Daily modelled PM2.5, ZIP Code",
      est=1.010, lo=1.006, hi=1.015, metric="OR", src="6.1 M Medicare index admissions, 759,128 readmissions"),
]
L = [
 dict(n=0, note="preconception /\nin utero:\nno record"),
 dict(n=0, note="childhood:\nno record"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=1, note="working age:\nWWTP / landfill\nbioaerosol\nworkers"),
 dict(n=2, note="older adults:\ndementia cohort,\nMedicare ADRD\nreadmission"),
]
