#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write state/corpus/2026-08-17.json.

Entry window 2026-08-17 -> 2026-08-17 (Monday). 12 records carried, 9 rejected.
Two records ship metadata-only: Taylor & Francis and Elsevier both refused the
abstract on this run and Semantic Scholar was rate-limited throughout, so the
AS&T CAPS-PM_SSA paper and the J Aerosol Sci refractive-index inversion are
carried on title/author/journal alone and labelled as such.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import corpus

DATE = "2026-08-17"
WINDOW = "2026-08-17 -> 2026-08-17"

PAPERS = [
    # ---------------------------------------------------- Cardiovascular & metabolic
    {"pmid": "42607596", "short": "Chen et al. 2026",
     "doi": "10.1016/j.ecoenv.2026.120666",
     "title": "Pollutant-specific plasma proteomic signatures, mediators and atrial-fibrillation-free life lost",
     "journal": "Ecotoxicol Environ Saf",
     "sub": "Cardiovascular & metabolic",
     "design": "Prospective cohort",
     "pm": "Long-term modelled PM2.5 and PM10 (plus NO2, NOx, SO2, benzene, O3)",
     "geo": "UK",
     "endpoint": "Cardiovascular",
     "n": "UK Biobank, ~2,900 plasma proteins, median 13.53 y follow-up",
     "tier": "A"},

    # ---------------------------------------------------- Reproductive & developmental
    {"pmid": "42604998", "short": "Zhao et al. 2026",
     "doi": "10.1097/CM9.0000000000004259",
     "title": "PM2.5 constituents and spontaneous abortion, modified by residential greenness",
     "journal": "Chin Med J (Engl)",
     "sub": "Reproductive & developmental",
     "design": "Prospective cohort (mixtures)",
     "pm": "Residential annual PM2.5 with NO3-, SO42-, NH4+, BC and OM fractions",
     "geo": "China",
     "endpoint": "Reproductive",
     "n": "20,117 pregnant women, Nanjing",
     "tier": "A"},

    # ---------------------------------------------------- Respiratory & allergic
    {"pmid": "42608143", "short": "Tornevi et al. 2026",
     "doi": "10.1136/bmjresp-2025-003279",
     "title": "Short-term urban-background PM2.5 and the timing of confirmed COVID-19, three Swedish cities",
     "journal": "BMJ Open Respir Res",
     "sub": "Respiratory & allergic",
     "design": "Case-crossover",
     "pm": "Daily urban-background PM2.5 and PM10 from fixed reference monitors",
     "geo": "Sweden",
     "endpoint": "Respiratory infection",
     "n": "3,999 PCR-confirmed cases, Stockholm/Gothenburg/Uppsala, Mar 2020-Jan 2022",
     "tier": "A"},

    # ---------------------------------------------------- Mechanistic toxicology
    {"pmid": "42606525", "short": "Li et al. 2026",
     "doi": "10.1096/fj.202600065RR",
     "title": "Size-resolved carbon-black nanoparticle effects on the maternal-fetal lung axis",
     "journal": "FASEB J",
     "sub": "Mechanistic toxicology",
     "design": "Animal model",
     "pm": "Ultrafine carbon-black nanoparticles, 30 nm and 120 nm, high-dose mechanistic exposure",
     "geo": "Laboratory (murine)",
     "endpoint": "Developmental / oxidative",
     "n": "Pregnant mice, two particle sizes, CIL LC-MS metabolomics",
     "tier": "B"},

    # ---------------------------------------------------- Exposure assessment & modelling
    {"pmid": "42608205", "short": "Moryani et al. 2026",
     "doi": "10.1002/jat.70398",
     "title": "PM2.5-bound Cu, Cd, Ni, Pb and Zn in 20 schools across two contrasting South China cities",
     "journal": "J Appl Toxicol",
     "sub": "Exposure assessment & modelling",
     "design": "Source apportionment",
     "pm": "Heavy-metal content of PM2.5, summer and winter",
     "geo": "China",
     "endpoint": "Carcinogenic risk",
     "n": "20 schools, Guangzhou and Maoming, two seasons of 2018",
     "tier": "B"},

    {"pmid": "42607792", "short": "Ianiri et al. 2026",
     "doi": "10.1016/j.envpol.2026.128965",
     "title": "Street- vs roof-level deposition fluxes of POPs and metals, normalised to sedimentable PM",
     "journal": "Environ Pollut",
     "sub": "Exposure assessment & modelling",
     "design": "Deposition sampling",
     "pm": "Settleable particulate matter, monthly deposimeter collection",
     "geo": "Italy",
     "endpoint": "None (exposure)",
     "n": "13 monthly samples at two heights, Rome, Aug 2023-Aug 2024",
     "tier": "B"},

    {"pmid": "", "short": "Awan et al. 2026",
     "doi": "10.1007/s44408-026-00160-z",
     "title": "BRIQ-PM2.5: quantile-mapping attribution of industrial excess PM2.5 across Pakistan",
     "journal": "Aerosol Air Qual Res",
     "sub": "Exposure assessment & modelling",
     "design": "Spatial analysis / GIS",
     "pm": "Satellite-derived surface PM2.5",
     "geo": "Pakistan",
     "endpoint": "None (exposure)",
     "n": "Four provinces of Pakistan, station-level series vs province baseline cities",
     "tier": "B"},

    # ---------------------------------------------------- Sensing, forecasting & instrumentation
    {"pmid": "", "short": "Filioglou et al. 2026",
     "doi": "10.5194/acp-26-11525-2026",
     "title": "Particle linear depolarisation ratio at 1565 nm from Halo Doppler lidar: smoke vs volcanic ash",
     "journal": "Atmos Chem Phys",
     "sub": "Sensing, forecasting & instrumentation",
     "design": "Multi-instrument field evaluation",
     "pm": "Lidar depolarisation ratio and aerosol layer optical properties at 1565 nm",
     "geo": "Finland",
     "endpoint": "None (instrument)",
     "n": "Three case studies: extremely fresh smoke, aged smoke, volcanic ash",
     "tier": "B"},

    {"pmid": "", "short": "Dal Porto et al. 2026",
     "doi": "10.1080/02786826.2026.2711663",
     "title": "Humidified CAPS-PM_SSA with a revised truncation-correction methodology",
     "journal": "Aerosol Sci Technol",
     "sub": "Sensing, forecasting & instrumentation",
     "design": "Metadata only (no abstract)",
     "pm": "Aerosol optical extinction and scattering, single-scattering albedo",
     "geo": "Chamber / laboratory",
     "endpoint": "None (instrument)",
     "n": "Metadata only - abstract not released by publisher on this run",
     "tier": "B"},

    {"pmid": "", "short": "Zhao et al. 2026",
     "doi": "10.1016/j.jaerosci.2026.106883",
     "title": "Monte-Carlo inversion of aerosol complex refractive index from multi-wavelength lidar plus size distribution",
     "journal": "J Aerosol Sci",
     "sub": "Sensing, forecasting & instrumentation",
     "design": "Metadata only (no abstract)",
     "pm": "Complex refractive index, multi-wavelength lidar backscatter, particle size distribution",
     "geo": "Not stated",
     "endpoint": "None (algorithm)",
     "n": "Metadata only - abstract not released by publisher on this run",
     "tier": "C"},

    # ---------------------------------------------------- Burden, policy & mitigation
    {"pmid": "", "short": "Xia et al. 2026 (preprint)",
     "doi": "10.48550/arXiv.2608.14928",
     "title": "Surface PM2.5 mass and composition under stratospheric sulfate geoengineering (GLENS)",
     "journal": "arXiv (preprint)",
     "sub": "Burden, policy & mitigation",
     "design": "Chemical transport modelling",
     "pm": "Modelled surface PM2.5 mass and speciation (dust, sea salt, OC, sulfate, SOA)",
     "geo": "Global",
     "endpoint": "None (modelling)",
     "n": "GLENS ensemble, CESM1, SO2 injection against RCP8.5 forcing",
     "tier": "B"},

    # ---------------------------------------------------- Other clinical endpoints
    {"pmid": "42607991", "short": "Choi et al. 2026",
     "doi": "10.1016/j.envres.2026.125497",
     "title": "Time-varying long-term PM2.5 and leukaemia incidence from childhood into early adulthood",
     "journal": "Environ Res",
     "sub": "Other clinical endpoints",
     "design": "Nationwide cohort",
     "pm": "Annual district PM2.5 from a machine-learning ensemble, 226 inland districts",
     "geo": "South Korea",
     "endpoint": "Oncological",
     "n": "384,606 aged 0-18 at enrolment, 272 incident leukaemias, NHIS-NSC 2002-2020",
     "tier": "A"},
]

EFFECTS = [
    {"label": "COVID-19 PCR positive, PM2.5 lag 0", "exposure": "per IQR 3.3 ug/m3",
     "est": 1.084, "lo": 1.011, "hi": 1.162, "metric": "OR",
     "src": "Tornevi 2026 (BMJ Open Respir Res)"},

    {"label": "Incident leukaemia, ages 0-18 at entry", "exposure": "per 5 ug/m3 annual PM2.5",
     "est": 1.40, "lo": 1.04, "hi": 1.90, "metric": "HR",
     "src": "Choi 2026 (Environ Res)"},

    {"label": "Spontaneous abortion, PM2.5 total mass", "exposure": "per IQR",
     "est": 1.18, "lo": 1.11, "hi": 1.26, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, ammonium", "exposure": "per IQR",
     "est": 1.19, "lo": 1.11, "hi": 1.26, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, nitrate", "exposure": "per IQR",
     "est": 1.18, "lo": 1.11, "hi": 1.26, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, sulfate", "exposure": "per IQR",
     "est": 1.17, "lo": 1.10, "hi": 1.25, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, organic matter", "exposure": "per IQR",
     "est": 1.14, "lo": 1.07, "hi": 1.21, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, black carbon", "exposure": "per IQR",
     "est": 1.14, "lo": 1.08, "hi": 1.22, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, lowest greenness quartile", "exposure": "PM2.5 per IQR, NDVI-1000m Q1",
     "est": 1.30, "lo": 1.14, "hi": 1.48, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
    {"label": "Spontaneous abortion, highest greenness quartile", "exposure": "PM2.5 per IQR, NDVI-1000m Q4",
     "est": 1.11, "lo": 0.97, "hi": 1.26, "metric": "OR", "src": "Zhao 2026 (Chin Med J)"},
]

LIFECOURSE = [
    {"n": 2, "note": "Spontaneous abortion\nfrom residential PM2.5;\nprenatal CBNP in mice"},
    {"n": 2, "note": "Leukaemia cohort\nentered at age 0;\nschool-age metal HRA"},
    {"n": 2, "note": "Leukaemia follow-up\nthrough adolescence;\nschool cohort to age 18"},
    {"n": 2, "note": "Swedish adult\ncase-crossover;\nUK Biobank at entry"},
    {"n": 1, "note": "UK Biobank ages into\n65+ over 13.5 y of\nAF follow-up"},
]

corpus.save(DATE, PAPERS, EFFECTS, WINDOW, LIFECOURSE)
print("saved", DATE, len(PAPERS), "papers,", len(EFFECTS), "effects")
