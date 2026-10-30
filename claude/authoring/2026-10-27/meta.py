# -*- coding: utf-8 -*-
W = "2026-10-27 -> 2026-10-27"
E = [
 dict(label="Respiratory ED/adm.\nPSPS + wildfire", exposure="Severe power shutoff + 10 ug/m3 wildfire PM2.5 vs neither",
      est=1.16, lo=1.10, hi=1.22, metric="OR", src="California case-crossover"),
 dict(label="Sick absence\nHead Start", exposure="+100 regional FIRMS fire detections (7-day mean)",
      est=1.106, lo=1.018, hi=1.201, metric="OR", src="OK-AIR n=204"),
 dict(label="Infant amoxicillin\n(CDE)", exposure="Observed prenatal PM2.5 vs counterfactual 5 ug/m3",
      est=1.12, lo=1.10, hi=1.14, metric="OR", src="Scotland births n=498,123"),
 dict(label="Ragweed SPT\nrural residence", exposure="Rural vs urban residence (PM10/pollen contrast)",
      est=0.69, lo=0.50, hi=0.96, metric="OR", src="Croatia ATOPICA n=3,520"),
 dict(label="Cancer YLL\nPudong", exposure="PM2.5 per 10 ug/m3, lag 0-1",
      est=2.22, lo=0.71, hi=3.74, metric="Years", src="Shanghai time series"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nScotland prenatal\nPM2.5"),
 dict(n=3, note="childhood:\nHead Start smoke;\nPatras; ragweed;\ninfant LE"),
 dict(n=0, note="adolescence:\nno record"),
 dict(n=3, note="working age:\ncortisol (24 y);\nPSPS; La Palma"),
 dict(n=0, note="older adults:\nno dedicated\nrecord"),
]
