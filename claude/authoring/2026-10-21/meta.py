# -*- coding: utf-8 -*-
W = "2026-10-21 -> 2026-10-21"
E = [
 dict(label="AF incidence\nsulfate PM2.5", exposure="Secondary-sulfate PM2.5 (per IQR)",
      est=1.056, lo=1.053, hi=1.058, metric="HR", src="Medicare 26.3 M"),
 dict(label="AF incidence\nvehicle PM2.5", exposure="Vehicle-source PM2.5 (per IQR)",
      est=1.029, lo=1.028, hi=1.030, metric="HR", src="Medicare 26.3 M"),
 dict(label="Cervical cancer\nrecurrence", exposure="PM2.5 (per IQR, post-surgery)",
      est=1.93, lo=1.40, hi=2.66, metric="HR", src="Fudan cohort n=3758 (SHR)"),
 dict(label="Cervical cancer\ndeath", exposure="PM2.5 (per IQR, post-surgery)",
      est=2.55, lo=1.78, hi=3.67, metric="HR", src="Fudan cohort n=3758"),
 dict(label="FEV1 change\nPM1", exposure="Long-term PM1 (per IQR)",
      est=-36.84, lo=-45.91, hi=-27.76, metric="mL", src="CPH Study n=50991"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\nfolic acid x\nbirthweight"),
 dict(n=1, note="childhood:\nHFMD time-series\n(Shenzhen)"),
 dict(n=0, note="adolescence:\nno record"),
 dict(n=5, note="working age:\nlung function;\nlipids; cervical Ca;\nRCS review; AMI"),
 dict(n=3, note="older adults:\nMedicare AF;\nCHARLS frailty;\nAMI index"),
]
