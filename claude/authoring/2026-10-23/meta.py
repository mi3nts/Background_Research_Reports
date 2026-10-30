# -*- coding: utf-8 -*-
W = "2026-10-23 -> 2026-10-23"
E = [
 dict(label="SGA (IVF)\nwhole pregnancy", exposure="PM2.5, whole-pregnancy average (increment not stated)",
      est=1.124, lo=1.015, hi=1.245, metric="OR", src="Guangzhou IVF case-control n=332"),
 dict(label="SGA (IVF)\n2nd trimester", exposure="PM2.5, 2nd-trimester average (increment not stated)",
      est=1.082, lo=1.005, hi=1.165, metric="OR", src="Guangzhou IVF case-control n=332"),
 dict(label="SGA (IVF)\n3rd trimester", exposure="PM2.5, 3rd-trimester average (increment not stated)",
      est=1.075, lo=1.002, hi=1.154, metric="OR", src="Guangzhou IVF case-control n=332"),
 dict(label="MDD\n(MR)", exposure="Genetically predicted PM2.5 (unit not stated)",
      est=1.27, lo=1.07, hi=1.51, metric="OR", src="Two-sample MR (preprint)"),
 dict(label="Optical RTM vs\ngravimetric", exposure="Real-time photometer vs gravimetric sampler",
      est=0.31, lo=0.25, hi=0.37, metric="lnR", src="Meta-analysis, 96 pairs"),
]
L = [
 dict(n=2, note="preconception /\nin utero:\nIVF SGA;\nheat+AQ review"),
 dict(n=1, note="childhood:\nwood-stove UFP\nchild dose\nscenarios"),
 dict(n=0, note="adolescence:\nno record"),
 dict(n=5, note="working age:\ncrossover lungs;\noxylipin panel;\nvolcano; turf;\nmining dust RTMs"),
 dict(n=0, note="older adults:\nno record"),
]
