# -*- coding: utf-8 -*-
W = "2026-10-30 -> 2026-10-30"
E = [
 dict(label="TTN\nprenatal PM2.5", exposure="40-week PM2.5, per unit", est=1.001, lo=1.000, hi=1.002, metric="OR", src="Taiwan NHIRD 3,091 cases"),
 dict(label="City PM2.5\nadaptation pilot", exposure="2017 climate-adaptive city pilot (DiD)", est=-3.87, lo=-6.49, hi=-1.25, metric="ug/m3", src="China 264 cities"),
 dict(label="Modelled burden\nadaptation pilot", exposure="Pilot-attributable PM2.5 change via GEMM", est=-8.10, lo=-11.32, hi=-4.76, metric="% change", src="China 264 cities"),
]
L = [
 dict(n=3, note="preconception /\nin utero:\nTTN; ECHO cord\nDNAm; CHAMACOS"),
 dict(n=1, note="childhood:\nDar es Salaam\nschool BP"),
 dict(n=1, note="adolescence /\nyoung adult:\nnasal EWAS"),
 dict(n=1, note="working age:\nAll of Us\nsmoke-depression"),
 dict(n=0, note="older adults:\nnone today"),
]
