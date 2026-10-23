# -*- coding: utf-8 -*-
W = "2026-10-22 -> 2026-10-22"
E = [
 dict(label="ADHD\nEC yr-2 (all)", exposure="EC >1.13 vs <0.49 ug/m3, 2nd year of life",
      est=1.24, lo=1.12, hi=1.36, metric="HR", src="Danish case-cohort"),
 dict(label="ADHD\nEC yr-2 (female)", exposure="EC >1.13 vs <0.49 ug/m3, 2nd year of life",
      est=1.44, lo=1.21, hi=1.72, metric="HR", src="Danish case-cohort"),
 dict(label="All-cause death\nBeijing elderly", exposure="PM2.5 (per 1 ug/m3)",
      est=1.053, lo=1.026, hi=1.080, metric="HR", src="Beijing cohort n=3472"),
 dict(label="CVD death\nBeijing elderly", exposure="PM2.5 (per 1 ug/m3)",
      est=1.046, lo=1.001, hi=1.100, metric="HR", src="Beijing cohort n=3472"),
 dict(label="Respiratory ED/UC\npeaker plant", exposure="HyADS peaker index (per unit)",
      est=1.044, lo=1.001, hi=1.090, metric="OR", src="MA case-crossover"),
 dict(label="HAZ\nLPG trial", exposure="LPG stove + fuel (ITT)",
      est=-0.06, lo=-0.16, hi=0.03, metric="HAZ", src="HAPIN n=2169"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nHAPIN LPG\n(gestation)"),
 dict(n=2, note="childhood:\nADHD yr-2 EC;\nHAPIN growth\nages 2-5"),
 dict(n=0, note="adolescence:\nno record"),
 dict(n=3, note="working age:\nCRS; ILD;\npeaker ED visits"),
 dict(n=1, note="older adults:\nBeijing elderly\nmortality"),
]
