# -*- coding: utf-8 -*-
W = "2026-10-05 -> 2026-10-05"
E = [
 dict(label="Dementia mortality\nUFP number (per 10,000 cm-3)", exposure="Residential UFP number concentration, 3-yr mean",
      est=1.22, lo=1.17, hi=1.27, metric="HR", src="2.1 M adults, CanCHEC Montreal + Toronto"),
 dict(label="Chronic disease incidence\nPM2.5 (per 5 ug/m3)", exposure="Annual PM2.5 at residence, land-use regression",
      est=1.22, lo=1.19, hi=1.26, metric="HR", src="313,534 participants, UK Biobank"),
 dict(label="Respiratory admissions\nPM2.5 (per 10 ug/m3)", exposure="Daily PM2.5, case-crossover",
      est=1.027, lo=1.006, hi=1.049, metric="OR", src="Pretoria, Apr 2017 - Feb 2020"),
]
L = [
 dict(n=0, note="preconception /\nin utero:\nno record"),
 dict(n=1, note="childhood:\npaediatric ward\n(metadata only)"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=1, note="working age:\nstone carvers\n(personal RD)"),
 dict(n=1, note="older adults:\nUFP dementia\nmortality"),
]
