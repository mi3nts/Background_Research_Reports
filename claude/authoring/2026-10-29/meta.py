# -*- coding: utf-8 -*-
W = "2026-10-29 -> 2026-10-29"
E = [
 dict(label="Severe AECOPD\nbiomass+smoke", exposure="Combined vs cigarette-only exposure", est=1.89, lo=1.22, hi=2.96, metric="OR", src="Turkiye COPD n=319"),
 dict(label="Stillbirth\nbiomass fuel", exposure="Household biomass fuel use", est=1.37, lo=1.21, hi=1.57, metric="IRR", src="ICMR-SPIC n=227,821"),
 dict(label="Kidney ED visits\nUFP lag 0-3", exposure="UFP per IQR (modelled)", est=0.74, lo=0.28, hi=1.20, metric="%ER", src="New York case-crossover"),
]
L = [
 dict(n=2, note="preconception /\nin utero:\nstillbirth;\nCHAPS prenatal"),
 dict(n=3, note="childhood:\nCHAPS; respirator\nfit; caregivers"),
 dict(n=1, note="adolescence:\nCHAPS to 18"),
 dict(n=2, note="working age:\nCOPD; coal dust"),
 dict(n=1, note="older adults:\nUFP kidney\n(>65 stronger)"),
]
