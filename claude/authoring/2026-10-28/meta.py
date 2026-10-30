# -*- coding: utf-8 -*-
W = "2026-10-28 -> 2026-10-28"
E = [
 dict(label="Paediatric asthma\nhospitalisation", exposure="PM2.5, cumulative lag 0-3",
      est=1.079, lo=1.052, hi=1.107, metric="OR", src="Louisiana n=28,499"),
 dict(label="Heart disease\nPM2.5", exposure="PM2.5 (per 1 ug/m3)",
      est=1.027, lo=1.022, hi=1.032, metric="HR", src="China 123 cities n=8,172"),
 dict(label="Heart disease\nBC", exposure="BC (per 1 ug/m3)",
      est=1.381, lo=1.266, hi=1.506, metric="HR", src="China 123 cities n=8,172"),
 dict(label="Lung cancer\nrecurrence", exposure="PM2.5 (per within-site SD), post-diagnosis",
      est=1.41, lo=1.08, hi=1.84, metric="HR", src="3-city cohort, 60 events"),
 dict(label="Adolescent anxiety\nPM10", exposure="PM10 (per IQR)",
      est=1.29, lo=1.22, hi=1.36, metric="OR", src="Sichuan n=71,364"),
 dict(label="LBW\nPurpleAir PM2.5", exposure="Area PM2.5 >75 vs <=75 ug/m3",
      est=1.18, lo=0.59, hi=2.36, metric="OR", src="Kinshasa n=355"),
 dict(label="Circulatory admissions\nfire density", exposure="+1,000 detections/100,000 km2/yr",
      est=0.998, lo=0.970, hi=1.028, metric="RR", src="Brazil 324 state-years"),
 dict(label="eGFR\nfire PM2.5", exposure="Landscape-fire PM2.5 (per IQR 0.505 ug/m3)",
      est=-0.83, lo=-1.03, hi=-0.62, metric="mL/min/1.73m2", src="China n=12,102"),
]
L = [
 dict(n=2, note="preconception /\nin utero:\nFujian Hb/anemia;\nKinshasa LBW"),
 dict(n=3, note="childhood:\nasthma; kidney;\nschool review"),
 dict(n=2, note="adolescence:\nSichuan anxiety;\nkidney (5-18 y)"),
 dict(n=3, note="working age:\nOSA; heart disease;\nlung ca. recurrence"),
 dict(n=0, note="older adults:\nno dedicated\nrecord"),
]
