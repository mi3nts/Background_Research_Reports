# -*- coding: utf-8 -*-
W = "2026-10-08 -> 2026-10-08"
E = [
 dict(label="All-cause mortality\nindoor black carbon (per 1 ug/m3)", exposure="Indoor BC, ambient x infiltration factor",
      est=1.072, lo=1.035, hi=1.111, metric="HR", src="12,607 older adults, China, 8,643 deaths"),
 dict(label="All-cause mortality\nindoor sulfate (per 1 ug/m3)", exposure="Indoor SO4 2-, ambient x infiltration factor",
      est=1.010, lo=1.001, hi=1.019, metric="HR", src="12,607 older adults, China, 8,643 deaths"),
 dict(label="All-cause mortality\nindoor organic matter (per 1 ug/m3)", exposure="Indoor OM, ambient x infiltration factor",
      est=1.009, lo=1.002, hi=1.016, metric="HR", src="12,607 older adults, China, 8,643 deaths"),
 dict(label="All-cause mortality\nindoor PM2.5 (per 1 ug/m3)", exposure="Indoor PM2.5, ambient x infiltration factor",
      est=1.003, lo=1.001, hi=1.005, metric="HR", src="12,607 older adults, China, 8,643 deaths"),
 dict(label="Incident CKD\nPM10 (per 10 ug/m3)", exposure="Annual PM10, time-varying",
      est=1.18, lo=1.06, hi=1.31, metric="HR", src="15,580 adults, Beijing, 664 cases"),
 dict(label="Incident CKD\nPM2.5 (per 10 ug/m3)", exposure="Annual PM2.5, time-varying",
      est=1.22, lo=0.99, hi=1.50, metric="HR", src="15,580 adults, Beijing, 664 cases"),
]
L = [
 dict(n=0, note="preconception /\nin utero:\nno record"),
 dict(n=3, note="childhood:\nKo-CHENS, Sao\nPaulo, neonatal\nair cleaners"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=1, note="working age:\nBeijing CKD\ncohort"),
 dict(n=1, note="older adults:\nindoor constituent\nmortality"),
]
