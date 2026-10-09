# -*- coding: utf-8 -*-
W = "2026-10-03 -> 2026-10-03"
E = [
 dict(label="Lung cancer, never-smokers\nPM2.5 nitrate (per IQR)", exposure="Annual PM2.5 NO3-, 2004-2018",
      est=1.35, lo=1.23, hi=1.48, metric="HR", src="262,785 never-smokers, China Kadoorie Biobank"),
 dict(label="Lung cancer, never-smokers\nPM2.5 ammonium (per IQR)", exposure="Annual PM2.5 NH4+, 2004-2018",
      est=1.22, lo=1.13, hi=1.31, metric="HR", src="262,785 never-smokers, China Kadoorie Biobank"),
 dict(label="Lung cancer, never-smokers\nPM2.5 chloride (per IQR)", exposure="Annual PM2.5 Cl-, 2004-2018",
      est=1.20, lo=1.12, hi=1.28, metric="HR", src="262,785 never-smokers, China Kadoorie Biobank"),
 dict(label="Lung cancer, never-smokers\nconstituent mixture", exposure="Quantile g-computation, all constituents",
      est=1.13, lo=1.07, hi=1.19, metric="HR", src="262,785 never-smokers, China Kadoorie Biobank"),
 dict(label="Otitis media with effusion\nPM10 (MR, IVW)", exposure="Genetic instrument for PM10, UK Biobank",
      est=1.555, lo=0.947, hi=2.553, metric="OR", src="12,397 cases / 464,237 controls, FinnGen R13"),
]
L = [
 dict(n=1, note="preconception /\nin utero:\ngestational mouse\nPM2.5 (PE model)"),
 dict(n=0, note="childhood:\nno age-specific\nrecord"),
 dict(n=0, note="adolescence:\nno age-specific\nrecord"),
 dict(n=1, note="working age:\nCKB never-smoker\nlung cancer"),
 dict(n=0, note="older adults:\nno age-specific\nrecord"),
]
