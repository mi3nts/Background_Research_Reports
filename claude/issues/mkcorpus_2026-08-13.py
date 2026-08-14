# -*- coding: utf-8 -*-
"""Corpus writer for the 2026-08-13 issue.

Entry window 2026-08-13 -> 2026-08-13 (PubMed [EDAT]; Crossref created-date for
the AMT/ACP/RSC leg; Europe PMC CREATION_DATE for preprints). 17 records
carried, 12 rejected.

Design / geo / endpoint labels are taken ONLY from vocabularies already mapped
in plots.py and mktable.py. No new leaf label is written here.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import corpus
from corpus import MECH, CVM, NEU, RESP, REPR, EXPO, SENS, OCC, BURD, OTHR

P = []
def add(**kw): P.append(kw)

# ---------------------------------------------------------------- NEURO
add(pmid="42593216", short="Xu et al. 2026",
    doi="10.1111/ene.70716",
    title="Association between PM2.5 components and cerebral hypoperfusion: a mediation role of inflammatory biomarkers",
    journal="Eur J Neurol", sub=NEU, design="Retrospective clinical series",
    pm="PM2.5, black carbon, sulfate, nitrate, ammonium, organic matter", geo="China",
    endpoint="Neuro / cognitive",
    n="967 patients with symptomatic intracranial arterial stenosis, 3-year TAP exposures",
    tier="A")

# ---------------------------------------------------------------- CARDIOVASCULAR
add(pmid="", short="Chen et al. 2026",
    doi="10.21203/rs.3.rs-10547139/v1",
    title="Compound cold wave-PM2.5 exposure and cardiovascular emergency ambulance calls",
    journal="Research Square (preprint)", sub=CVM, design="Ecological panel",
    pm="PM2.5", geo="China",
    endpoint="Cardiovascular",
    n="82,714 ambulance calls, Shijiazhuang, 2014-2023; DLNM with quasi-Poisson",
    tier="B")

add(pmid="42589475", short="Gaggini & Vassalle 2026",
    doi="10.3390/ijms27156818",
    title="Gene-air pollution interaction in cardiovascular disease",
    journal="Int J Mol Sci", sub=CVM, design="Narrative review",
    pm="PM2.5, PM10, traffic-related pollutants", geo="Global",
    endpoint="Cardiovascular", n="PubMed narrative synthesis of gene-environment interaction studies",
    tier="C")

# ---------------------------------------------------------------- MECHANISTIC
add(pmid="42593595", short="Gomes et al. 2026",
    doi="10.1007/s12012-026-10171-2",
    title="Senolytics reverse PM2.5-induced cell and vascular dysfunction",
    journal="Cardiovasc Toxicol", sub=MECH, design="Animal + in vitro",
    pm="Concentrated ambient PM2.5", geo="United States",
    endpoint="Cardiovascular",
    n="C57BL/6J mice, concentrated ambient particles vs filtered air; dasatinib + quercetin rescue",
    tier="A")

add(pmid="42591855", short="Zhang et al. 2026",
    doi="10.21037/jtd-2026-1274",
    title="Impact of pleural anthracosis severity on structure and function of subcarinal lymph nodes",
    journal="J Thorac Dis", sub=MECH, design="Retrospective clinical series",
    pm="Deposited carbonaceous particles", geo="China",
    endpoint="Other clinical",
    n="Thoracoscopically graded pleural anthracosis with paired subcarinal nodes; Ki67, CD31, CD68, D2-40",
    tier="B")

# ---------------------------------------------------------------- OCCUPATIONAL
add(pmid="42588203", short="Tan et al. 2026",
    doi="10.3390/nu18152580",
    title="PM2.5 components, nutritional indices and physical activity vs lower eGFR in subway workers",
    journal="Nutrients", sub=OCC, design="Cross-sectional (cohort baseline)",
    pm="PM2.5 component mixture", geo="China",
    endpoint="Other clinical", n="8,477 subway workers, Wuhan; TAP components, WQS, QGC and BKMR",
    tier="A")

# ---------------------------------------------------------------- OTHER CLINICAL
add(pmid="42594124", short="Traisathit et al. 2026",
    doi="10.1371/journal.pone.0355856",
    title="Air pollution and mortality in acute lymphoblastic leukaemia across age groups, northern Thailand",
    journal="PLoS One", sub=OTHR, design="Retrospective cohort",
    pm="PM2.5, PM10, O3, CO", geo="Thailand",
    endpoint="Oncologic", n="604 ALL patients diagnosed 1999-2020, three age strata",
    tier="B")

# ---------------------------------------------------------------- BURDEN
add(pmid="42594038", short="He et al. 2026",
    doi="10.1159/ned/adwag005",
    title="Premature ischaemic stroke burden in adults aged 50-69 in China, India and the United States",
    journal="Neuroepidemiology", sub=BURD, design="GBD secondary analysis",
    pm="Ambient PM2.5 (population attributable fraction)", geo="Global",
    endpoint="Cardiovascular", n="GBD 2023 DALYs, YLLs, YLDs and PAFs; ARIMA projection to 2053",
    tier="C")

# ---------------------------------------------------------------- EXPOSURE ASSESSMENT
add(pmid="42593703", short="da Costa Cardoso et al. 2026",
    doi="10.1007/s10661-026-15743-x",
    title="Legacy Pb-Zn mine tailings as persistent sources of bioaccessible toxic elements in urban dust",
    journal="Environ Monit Assess", sub=EXPO, design="Field measurement",
    pm="Resuspended urban dust, Pb, Zn, Cd, Cu, Mn", geo="Brazil",
    endpoint="Oncologic", n="18 urban dust samples plus reference soils, Boquira mining district",
    tier="B")

add(pmid="", short="Gould & Jagarnath 2026",
    doi="10.21203/rs.3.rs-10623736/v1",
    title="Satellite monitoring for air quality and public health research in Africa: a scoping review",
    journal="Research Square (preprint)", sub=EXPO, design="Scoping review",
    pm="Satellite-derived PM2.5 and AOD", geo="West Africa",
    endpoint="Other clinical", n="26 records across five databases plus grey literature, to May 2026",
    tier="B")

# ---------------------------------------------------------------- SENSING
add(pmid="42590763", short="Benjamin et al. 2026",
    doi="10.3390/s26154988",
    title="Limitations of environmental extrapolation in low-cost carbon monoxide and PM2.5 sensors",
    journal="Sensors (Basel)", sub=SENS, design="Calibration model comparison",
    pm="PM2.5, CO", geo="United States",
    endpoint="None (monitoring)",
    n="Multi-season co-location of Plantower PMS5003 and Alphasense CO-B4 against FEM monitors",
    tier="A")

add(pmid="42590443", short="Fawaz et al. 2026",
    doi="10.3390/s26154666",
    title="Surface cleaning of SAW-based microparticle sensors in a cascade impactor via SAW-induced droplet displacement",
    journal="Sensors (Basel)", sub=SENS, design="Instrument development",
    pm="Size-segregated microparticles", geo="France",
    endpoint="None (monitoring)",
    n="Rayleigh-wave-actuated droplet on a lithium niobate chip; NaCl solution and SiC particles",
    tier="A")

add(pmid="", short="Gao et al. 2026",
    doi="10.5194/amt-19-5337-2026",
    title="Feasibility of an air sensor array for real-time detection and characterisation of VOCs",
    journal="Atmos Meas Tech", sub=SENS, design="Instrument development",
    pm="VOC sensor response (non-PM)", geo="Laboratory",
    endpoint="None (monitoring)", n="Array of three broadband VOC sensor types, laboratory characterisation",
    tier="B")

add(pmid="42587206", short="Wu & Qu 2026",
    doi="10.1007/s10661-026-15799-9",
    title="Interpretable short-term PM2.5 forecasting using meteorology-pollution coupling across Beijing stations",
    journal="Environ Monit Assess", sub=SENS, design="Method / algorithm",
    pm="PM2.5", geo="Beijing",
    endpoint="None (monitoring)",
    n="420,768 hourly observations, 12 stations, 2013-2017; chronological train-validation-test",
    tier="B")

add(pmid="", short="Adams et al. 2026",
    doi="10.1039/d6ea00033a",
    title="Sampling sub-pixel scale variability in total column NO2 within a coastal urban environment",
    journal="Environ Sci Atmos", sub=SENS, design="Field campaign / remote sensing",
    pm="Total column NO2", geo="United States",
    endpoint="None (monitoring)", n="Pandora spectrometers at Boston University and Harvard University",
    tier="B")

add(pmid="", short="Liu et al. 2026c",
    doi="10.5194/amt-19-5325-2026",
    title="Polarization calibration of spaceborne lidar using dense cirrus-scattered solar background",
    journal="Atmos Meas Tech", sub=SENS, design="Method / algorithm",
    pm="Aerosol depolarization ratio", geo="Global",
    endpoint="None (monitoring)", n="CALIOP 532 nm plus modelled EarthCARE ATLID 355 nm",
    tier="C")

add(pmid="42590662", short="Liu et al. 2026d",
    doi="10.3390/s26154887",
    title="LRM-YOLO: lightweight YOLOv10n model for forest fire smoke detection in UAV images",
    journal="Sensors (Basel)", sub=SENS, design="Method / algorithm",
    pm="Smoke plume (image proxy)", geo="China",
    endpoint="None (monitoring)", n="UFFS dataset (UAV perspective) plus Wildfire Smoke V1",
    tier="C")

# ---------------------------------------------------------------- EFFECT ESTIMATES
E = [
    dict(label="Cerebral hypoperfusion, PM2.5",
         exposure="3-year mean, top vs bottom exposure",
         est=4.344, lo=3.323, hi=5.734, metric="OR",
         src="Xu 2026 (Eur J Neurol)"),
    dict(label="Cerebral hypoperfusion, black carbon",
         exposure="3-year mean, top vs bottom exposure",
         est=4.396, lo=3.327, hi=5.869, metric="OR",
         src="Xu 2026 (Eur J Neurol)"),
    dict(label="Lower eGFR, PM2.5 component mixture (WQS)",
         exposure="mixture index, per quantile",
         est=1.183, lo=1.106, hi=1.266, metric="OR",
         src="Tan 2026 (Nutrients)"),
    dict(label="Lower eGFR, PM2.5 component mixture (QGC)",
         exposure="mixture index, per quantile",
         est=1.183, lo=1.083, hi=1.291, metric="OR",
         src="Tan 2026 (Nutrients)"),
]

# ---------------------------------------------------------------- LIFE-COURSE
L = [
    {"n": 0, "note": "no record\nthis issue"},
    {"n": 2, "note": "paediatric ALL <15,\nchildren's Pb\nbioaccessibility HI>1"},
    {"n": 1, "note": "adolescent and\nyoung-adult ALL\nstratum, 15-39"},
    {"n": 3, "note": "Wuhan subway\nworkers, adult ALL,\nstroke 50-69"},
    {"n": 1, "note": "older East Asian\nadults with\nintracranial stenosis"},
]

corpus.save("2026-08-13", P, E,
            entry_window="2026-08-13 -> 2026-08-13", lifecourse=L)
print("saved", len(P), "papers,", len(E), "effects")
