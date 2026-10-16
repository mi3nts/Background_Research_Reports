# -*- coding: utf-8 -*-
W = "2026-10-15 -> 2026-10-15"
E = [
 dict(label="Chronic respiratory disease\nPAF, PM2.5", exposure="1 km PM2.5 (722-d mean)",
      est=18.98, lo=12.90, hi=24.90, metric="PAF %", src="Guangdong COPD surveillance, n=7,371"),
 dict(label="Chronic respiratory disease\nPAF, PM1", exposure="1 km PM1 (722-d mean)",
      est=19.09, lo=12.41, hi=25.02, metric="PAF %", src="Guangdong COPD surveillance, n=7,371"),
 dict(label="Chronic respiratory disease\nPAF, PM10", exposure="1 km PM10 (722-d mean)",
      est=21.40, lo=13.84, hi=27.67, metric="PAF %", src="Guangdong COPD surveillance, n=7,371"),
 dict(label="Fatty Liver Index >= 60\nPM2.5-NO2 score (SES-adj.)", exposure="2010 residential PM2.5-NO2 score",
      est=0.999, lo=0.993, hi=1.004, metric="OR", src="231,525 UK Biobank women"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nGuangdong CHD"),
 dict(n=1, note="childhood:\nschool-age\ninhaled dose"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=1, note="working age:\ncreosote PAH\nworkers"),
 dict(n=3, note="older adults:\nGuangdong >=40;\nMESA; UKB women"),
]
