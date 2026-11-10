# -*- coding: utf-8 -*-
W = "2026-11-07 -> 2026-11-07"
E = [
 dict(label="Asthma exacerbation\nwildfire smoke, lowest lag", exposure="Wildfire-smoke PM2.5, increment not stated in abstract, lags 0-7 d", est=1.27, lo=1.22, hi=1.33, metric="aOR", src="Huang All of Us n=18,935"),
 dict(label="Asthma exacerbation\nwildfire smoke, highest lag", exposure="Wildfire-smoke PM2.5, increment not stated in abstract, lags 0-7 d", est=1.38, lo=1.32, hi=1.44, metric="aOR", src="Huang All of Us n=18,935"),
 dict(label="Under-5 pneumonia visits\nPM2.5 lag 2", exposure="PM2.5 per IQR, city monitors", est=1.057, lo=1.015, hi=1.100, metric="RR", src="Tsogtbayar Ulaanbaatar", inc="per IQR / SD"),
 dict(label="Under-5 pneumonia visits\nPM1 lag 2", exposure="PM1 per IQR, city monitors", est=1.065, lo=1.025, hi=1.106, metric="RR", src="Tsogtbayar Ulaanbaatar", inc="per IQR / SD"),
 dict(label="Infant (<1 y) pneumonia\nPM1 lag 0", exposure="PM1 per IQR, city monitors", est=1.098, lo=1.046, hi=1.152, metric="RR", src="Tsogtbayar Ulaanbaatar", inc="per IQR / SD"),
 dict(label="CVD mortality Almaty\ncumulative lag 0-7", exposure="PM2.5, comparison increment not stated in abstract", est=1.011, lo=0.837, hi=1.222, metric="RR", src="Kulkayeva Almaty"),
 dict(label="CVD mortality Almaty\nage >=65", exposure="PM2.5, comparison increment not stated in abstract", est=1.174, lo=0.926, hi=1.489, metric="RR", src="Kulkayeva Almaty"),
 dict(label="FEV1 change Day 2\n(controlled exposure)", exposure="PM2.5 35 ug/m3 vs clean air, categorical contrast", est=-1.9, lo=-3.1, hi=-0.7, metric="% change", src="Pulczinski n=17", inc="categorical contrast"),
 dict(label="FEV1 change Day 3\n(controlled exposure)", exposure="PM2.5 35 ug/m3 vs clean air, categorical contrast", est=-1.8, lo=-3.5, hi=-0.1, metric="% change", src="Pulczinski n=17", inc="categorical contrast"),
 dict(label="Brachial diastolic BP\nclean heating policy", exposure="Coal-to-clean heating, treated vs untreated villages (categorical contrast)", est=-1.6, lo=-2.9, hi=-0.3, metric="mmHg", src="Sternbach n=1,003", inc="categorical contrast"),
 dict(label="Brachial systolic BP\nclean heating policy", exposure="Coal-to-clean heating, treated vs untreated villages (categorical contrast)", est=-1.4, lo=-3.3, hi=0.5, metric="mmHg", src="Sternbach n=1,003", inc="categorical contrast"),
]
L = [
 dict(n=4, note="ovarian (Mali, mouse);\nfollicular fluid (Tao);\nsperm (rat); Marques\npregnancy window"),
 dict(n=3, note="under-5 pneumonia\nUlaanbaatar; Marques\nchildhood; Lagos\nasthma protocol"),
 dict(n=3, note="fear circuitry\n(10-17 y); Marques\nadolescence; Lagos\nprotocol (to 18 y)"),
 dict(n=9, note="controlled exposure;\nyoung-adult panel;\nAll of Us asthma; farm,\ncannabis workers; veterans;\nCHARLS; clean heating"),
 dict(n=4, note="Almaty >=65 subgroup;\nCHARLS >=45; clean\nheating >40 y; smoke\nasthma, older adults"),
]
