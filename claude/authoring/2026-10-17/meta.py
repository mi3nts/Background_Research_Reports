# -*- coding: utf-8 -*-
W = "2026-10-17 -> 2026-10-17"
E = [
 dict(label="Cataract (pooled)", exposure="Long-term PM2.5 (per 1 ug/m3)",
      est=1.036, lo=0.988, hi=1.086, metric="HR", src="Meta-analysis, I2 99.7%"),
 dict(label="Cataract (pooled)", exposure="Black carbon (per IQR)",
      est=1.010, lo=0.983, hi=1.038, metric="HR", src="Meta-analysis, I2 33%"),
 dict(label="Life expectancy\nconventional FE", exposure="Country PM2.5 (per 10 ug/m3), years",
      est=0.406, lo=0.144, hi=0.668, metric="Years", src="186 economies 2000-2023"),
 dict(label="Life expectancy\n+ country trends", exposure="Country PM2.5 (per 10 ug/m3), years",
      est=-0.023, lo=-0.175, hi=0.129, metric="Years", src="186 economies 2000-2023"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nWuhan cohort"),
 dict(n=1, note="childhood:\nWuhan Bayley\nat age 2"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=2, note="working age:\nLPG cooks;\nThai adults"),
 dict(n=1, note="older adults:\nsmoke deaths\n>=65"),
]
