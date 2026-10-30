# -*- coding: utf-8 -*-
W = "2026-10-26 -> 2026-10-26"
E = [
 dict(label="ASD\nwildfire PM2.5", exposure="Prenatal wildfire PM2.5 (per IQR 0.75 ug/m3)",
      est=1.30, lo=1.07, hi=1.59, metric="HR", src="US Medicaid n=893,212"),
 dict(label="ADHD\nwildfire PM2.5", exposure="Prenatal wildfire PM2.5 (per IQR 0.75 ug/m3)",
      est=1.03, lo=0.91, hi=1.17, metric="HR", src="US Medicaid n=893,212"),
 dict(label="EOI MRD+\nB-ALL Q2", exposure="Induction PM2.5, Q2 vs Q1",
      est=1.56, lo=1.08, hi=2.24, metric="OR", src="REDIAL n=2,125"),
 dict(label="EOI MRD+\nB-ALL Q3", exposure="Induction PM2.5, Q3 vs Q1",
      est=1.51, lo=1.05, hi=2.17, metric="OR", src="REDIAL n=2,125"),
 dict(label="Live birth\nIVF", exposure="PM2.5 per 10 ug/m3, 85 d before retrieval",
      est=0.969, lo=0.954, hi=0.984, metric="OR", src="Chengdu IVF n=12,453"),
 dict(label="FEV1 age 6\nCOPSAC", exposure="Postnatal PM2.5 (per IQR 2.2 ug/m3)",
      est=-2.70, lo=-4.27, hi=-1.10, metric="% change", src="COPSAC n=846"),
 dict(label="sRaw age 6\nCOPSAC", exposure="Postnatal PM2.5 (per IQR 2.2 ug/m3)",
      est=7.30, lo=1.87, hi=13.07, metric="% change", src="COPSAC n=846"),
 dict(label="Gastric cancer\nincidence", exposure="National PM2.5 (per 1 ug/m3)",
      est=0.3, lo=0.1, hi=0.5, metric="% change", src="GBD 204 countries"),
]
L = [
 dict(n=3, note="preconception /\nin utero:\nwildfire ASD;\nIVF folliculo-\ngenesis window"),
 dict(n=4, note="childhood:\nCOPSAC lungs;\nALL MRD;\nneurodev review"),
 dict(n=1, note="adolescence:\nCOPSAC lung\ngrowth to 18"),
 dict(n=4, note="working age:\nindoor crossover;\nfarm respirators;\nAusDiab"),
 dict(n=2, note="older adults:\nAusDiab;\nlung-cancer\nsurgery"),
]
