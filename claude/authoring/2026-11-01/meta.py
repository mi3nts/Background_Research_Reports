# -*- coding: utf-8 -*-
W = "2026-11-01 -> 2026-11-01"
E = [
 dict(label="Kidney death\nPM2.5 lag 0-2", exposure="PM2.5 per IQR (width not in abstract)", est=1.0195, lo=1.0122, hi=1.0269, metric="OR", src="China 466,543 deaths", inc="per IQR / SD"),
 dict(label="Kidney death\nPM2.5-10 lag 0-3", exposure="PM2.5-10 per IQR (width not in abstract)", est=1.0240, lo=1.0158, hi=1.0323, metric="OR", src="China 466,543 deaths", inc="per IQR / SD"),
 dict(label="Death, Native Am.\nlow PM2.5", exposure="PM2.5 per 1 ug/m3", est=1.12, lo=1.06, hi=1.18, metric="OR", src="US Medicare lowest decile", inc="per 1 µg/m³ / unit"),
 dict(label="Death, non-Native\nlow PM2.5", exposure="PM2.5 per 1 ug/m3", est=1.01, lo=1.001, hi=1.02, metric="OR", src="US Medicare lowest decile", inc="per 1 µg/m³ / unit"),
 dict(label="Elevated BP\nAccra children", exposure="Home PM2.5 per 10 units", est=0.75, lo=0.39, hi=1.41, metric="OR", src="Accra n=919", inc="per 10 µg/m³"),
 dict(label="SBP Accra\nchildren", exposure="Home PM2.5 per 10 units", est=-0.70, lo=-3.34, hi=1.94, metric="mmHg", src="Accra n=919", inc="per 10 µg/m³"),
]
L = [
 dict(n=0, note="preconception /\nin utero:\nno record"),
 dict(n=2, note="childhood:\nAccra BP;\nMexico City brain"),
 dict(n=0, note="adolescence:\nno separate\nrecord"),
 dict(n=1, note="working age:\nsick leave\n(metadata only)"),
 dict(n=1, note="older adults:\nMedicare\nmortality"),
]
