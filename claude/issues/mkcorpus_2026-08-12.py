# -*- coding: utf-8 -*-
"""Corpus writer for the 2026-08-12 issue.

Entry window 2026-08-12 -> 2026-08-12 (PubMed [EDAT]; Crossref created-date for
the AMT/ACP/Elsevier leg). 28 records carried, 14 rejected in-harvest, 3
Consensus hits rejected as out-of-window.

Design / geo / endpoint labels are taken ONLY from the vocabularies already
mapped in plots.py and mktable.py. No new leaf labels are written here.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import corpus
from corpus import MECH, CVM, NEU, RESP, REPR, EXPO, SENS, OCC, BURD, OTHR

P = []
def add(**kw): P.append(kw)

# ---------------------------------------------------------------- NEURO
add(pmid="42583532", short="Delaney et al. 2026",
    doi="10.1097/EE9.0000000000000519",
    title="Cumulative annual air pollution exposure and first hospitalization with Parkinson's disease",
    journal="Environ Epidemiol", sub=NEU, design="Registry cohort + geospatial",
    pm="PM2.5, NO2, summer O3", geo="United States",
    endpoint="Neuro / cognitive", n="10,366,083 Medicare FFS beneficiaries 65+, 2000-2016",
    tier="A")

# ---------------------------------------------------------------- CARDIO-METABOLIC
add(pmid="42585725", short="Kakhaia et al. 2026",
    doi="10.1016/j.envint.2026.110441",
    title="Causal effects of time-varying air pollution mixtures on cardiovascular disease incidence",
    journal="Environ Int", sub=CVM, design="Prospective cohort (mixtures)",
    pm="PM2.5, NO2", geo="United Kingdom",
    endpoint="Cardiovascular", n="UK Biobank, 10-year follow-up, annual LUR exposures 2005-2019",
    tier="A")

# ---------------------------------------------------------------- OTHER CLINICAL
add(pmid="42582230", short="Li et al. 2026",
    doi="10.1016/j.xinn.2026.101429",
    title="Global and national CKD burden attributable to fine particles: updated exposure-response meta-analysis",
    journal="Innovation (Camb)", sub=OTHR, design="Umbrella review / meta-analysis",
    pm="PM2.5", geo="Global",
    endpoint="Other clinical", n="38 CKD studies, 16 eGFR studies; burden 1990-2020",
    tier="A")

add(pmid="42581044", short="Chow et al. 2026",
    doi="10.1038/s41467-026-75116-3",
    title="Blood metabolomic signatures linking air pollution to lung cancer",
    journal="Nat Commun", sub=OTHR, design="Prospective cohort",
    pm="PM2.5, O3, plus four co-pollutants", geo="United States",
    endpoint="Oncologic", n="1,357 participants, >1,100 metabolites, nested case-control in CPS-II/CPS-3",
    tier="A")

add(pmid="42582814", short="Jain et al. 2026",
    doi="10.5005/jp-journals-10078-1522",
    title="Ambient air pollution and glaucoma: systematic review and meta-analysis",
    journal="J Curr Glaucoma Pract", sub=OTHR, design="Systematic review (PRISMA)",
    pm="PM2.5, PM10, NO2, NOx, CO", geo="Global",
    endpoint="Other clinical", n="18 observational studies; 8 pooled for PM2.5",
    tier="B")

add(pmid="42582821", short="Schlaepfer et al. 2026",
    doi="10.21037/tau-2026-0338",
    title="Environmental hazards and risk of idiopathic urethral stricture",
    journal="Transl Androl Urol", sub=OTHR, design="Retrospective cohort",
    pm="Ambient PM, VOCs, metal oxides", geo="Salt Lake City",
    endpoint="Other clinical", n="2,048 cases matched to 1,939 controls (Utah Population Database)",
    tier="C")

add(pmid="42585852", short="Liu et al. 2026",
    doi="10.1016/j.jacadv.2026.103149",
    title="Reply: statistical fragility and methodological constraints in metabolomic mediation",
    journal="JACC Adv", sub=OTHR, design="Metadata only (no abstract)",
    pm="PM2.5", geo="United States",
    endpoint="Cardiovascular", n="Correspondence; abstract not indexed",
    tier="C")

# ---------------------------------------------------------------- RESPIRATORY
add(pmid="42584485", short="Feng & Chao 2026",
    doi="10.1007/s00484-026-03283-5",
    title="Lower respiratory infection burden attributable to PM2.5 in China and the G20, 1990-2023",
    journal="Int J Biometeorol", sub=RESP, design="GBD secondary analysis",
    pm="Ambient PM2.5, household PM2.5", geo="China",
    endpoint="Respiratory", n="GBD 2023; China plus 19 G20 members",
    tier="B")

add(pmid="42583122", short="Yang et al. 2026",
    doi="10.21037/jtd-2026-0284",
    title="COPD and LRI burden attributable to household air pollution and secondhand smoke, 1990-2021",
    journal="J Thorac Dis", sub=RESP, design="GBD secondary analysis",
    pm="Household PM from solid fuel", geo="Global",
    endpoint="Respiratory", n="GBD 2021, 204 countries; BAPC and ARIMA projection to 2030",
    tier="B")

add(pmid="42583188", short="Wu et al. 2026",
    doi="10.21037/jtd-2026-0784",
    title="Air pollution and COPD-related health outcomes: bibliometric and visualisation analysis",
    journal="J Thorac Dis", sub=RESP, design="Mapping review",
    pm="PM2.5, PM10, household PM", geo="Global",
    endpoint="Respiratory", n="11,167 articles and reviews, Web of Science to May 2025",
    tier="C")

add(pmid="42586116", short="Lancet Respir Med 2026",
    doi="10.1016/S2213-2600(26)00256-0",
    title="The far-reaching effects of wildfire smoke",
    journal="Lancet Respir Med", sub=RESP, design="Metadata only (no abstract)",
    pm="Wildfire PM2.5", geo="Global",
    endpoint="Respiratory", n="Editorial; abstract not indexed",
    tier="C")

# ---------------------------------------------------------------- MECHANISTIC
add(pmid="42546767", short="Choi et al. 2026",
    doi="10.1088/1758-5090/ae9402",
    title="Degradable PLGA/PCL membrane alveoli-on-a-chip for particulate-induced alveolar injury",
    journal="Biofabrication", sub=MECH, design="In vitro (cell lines)",
    pm="Diesel particulate matter", geo="In vitro",
    endpoint="Toxicological (in vitro)",
    n="Primary human alveolar epithelium and microvascular endothelium, air-liquid interface, cyclic strain",
    tier="A")

add(pmid="42582228", short="Yuan et al. 2026",
    doi="10.1016/j.xinn.2026.101347",
    title="Hallmarks of lung cancer driven by inhalable particulate matter",
    journal="Innovation (Camb)", sub=MECH, design="Critical review",
    pm="PM2.5, PM10", geo="Global",
    endpoint="Oncologic", n="12-hallmark framework spanning epidemiology to tumour microenvironment",
    tier="B")

# ---------------------------------------------------------------- BURDEN / POLICY
add(pmid="42583250", short="Xie et al. 2026",
    doi="10.21037/jtd-2026-0740",
    title="Thirty-year change and projection of Asian tracheal, bronchus and lung cancer burden",
    journal="J Thorac Dis", sub=BURD, design="GBD secondary analysis",
    pm="Ambient particulate matter pollution", geo="Asia",
    endpoint="Oncologic", n="GBD 2021, Asian subregions 1990-2021, BAPC projection",
    tier="C")

add(pmid="42582216", short="Liu et al. 2026b",
    doi="10.3389/fonc.2026.1873592",
    title="Lung cancer incidence and mortality trends with age-period-cohort analysis, Zibo 2014-2024",
    journal="Front Oncol", sub=BURD, design="Ecological panel",
    pm="Ambient air pollution (contextual)", geo="China",
    endpoint="Oncologic", n="Registered residents of Zibo, Shandong; 11 years of registry data",
    tier="C")

add(pmid="42584334", short="Tian et al. 2026",
    doi="10.3390/nano16150941",
    title="Bioinspired honeycomb-structured nanofibrous membranes for high-efficiency PM capture",
    journal="Nanomaterials (Basel)", sub=BURD, design="Bench / device experiment",
    pm="PM0.3, PM2.5", geo="Laboratory",
    endpoint="No health endpoint", n="Template-assisted electrospinning; mesh-size optimisation",
    tier="B")

add(pmid="42581290", short="Suryanarayanareddy et al. 2026",
    doi="10.1007/s11356-026-38118-8",
    title="Low-cost bio-based particle-capturing device for vehicular emissions: pilot study",
    journal="Environ Sci Pollut Res Int", sub=BURD, design="Bench / device experiment",
    pm="PM2.5, PM10, CO, CO2", geo="India",
    endpoint="No health endpoint", n="Indoor simulation of two junction scenarios at three turbulence intensities",
    tier="C")

# ---------------------------------------------------------------- EXPOSURE ASSESSMENT
add(pmid="42586353", short="Park et al. 2026",
    doi="10.1016/j.envpol.2026.128941",
    title="City-scale non-exhaust PM10 from emissions to exposure with a coupled chemistry-CFD framework",
    journal="Environ Pollut", sub=EXPO, design="CTM simulation + source attribution",
    pm="Non-exhaust PM10", geo="Seoul",
    endpoint="No health endpoint",
    n="FASU 3-D model over a dense Seoul district; EMEP/EEA vs KIMM emission factors; 2022 time-activity profile",
    tier="A")

add(pmid="42583566", short="Chillrud et al. 2026",
    doi="10.1097/EE9.0000000000000515",
    title="pcpr: principal component pursuit for exposure pattern recognition and outlier detection",
    journal="Environ Epidemiol", sub=EXPO, design="Software / tool description",
    pm="26 PM2.5 constituents", geo="United States",
    endpoint="No health endpoint", n="Queens, New York City speciation series 2015-2021",
    tier="A")

add(pmid="42584729", short="Zhang et al. 2026",
    doi="10.1007/s10653-026-03422-2",
    title="National-scale heavy metal contamination in urban road dust across 82 Chinese cities",
    journal="Environ Geochem Health", sub=EXPO, design="Review / synthesis",
    pm="Road dust heavy metals", geo="China",
    endpoint="No health endpoint", n="13,269 samples pooled from 169 studies",
    tier="B")

add(pmid="", short="Florencio et al. 2026",
    doi="10.1016/j.atmosenv.2026.122286",
    title="Comprehensive analysis of PM10 in the Metropolitan Area of Sao Paulo, Part I",
    journal="Atmos Environ", sub=EXPO, design="Metadata only (no abstract)",
    pm="PM10", geo="Brazil",
    endpoint="No health endpoint", n="Abstract not deposited at Crossref on the entry date",
    tier="B")

add(pmid="", short="Stevens et al. 2026",
    doi="10.1016/j.atmosenv.2026.122303",
    title="Biomass burning marker fingerprints for Australian hardwoods, softwoods and grasses",
    journal="Atmos Environ", sub=EXPO, design="Metadata only (no abstract)",
    pm="Biomass burning PM tracers", geo="Australia",
    endpoint="No health endpoint", n="Abstract not deposited at Crossref on the entry date",
    tier="B")

add(pmid="", short="Ibrahim 2026",
    doi="10.21203/rs.3.rs-10666765/v1",
    title="Air pollution status and temporal patterns in Bukit Rambai and Muar, 2013-2017",
    journal="Research Square (preprint)", sub=EXPO, design="Ecological panel",
    pm="PM10, O3, CO, SO2, NO2", geo="Malaysia",
    endpoint="No health endpoint", n="Two Malaysian DOE stations, five years of API and meteorology",
    tier="C")

# ---------------------------------------------------------------- SENSING / INSTRUMENTATION
add(pmid="", short="Kirchhoff et al. 2026",
    doi="10.5194/amt-19-5243-2026",
    title="Evaluation of DMSO as working fluid in condensation particle counters",
    journal="Atmos Meas Tech", sub=SENS, design="Laboratory metrology",
    pm="Ultrafine particle number", geo="Laboratory",
    endpoint="No health endpoint",
    n="Six months of laboratory and field operation vs a butanol CPC across pressure, temperature and aerosol type",
    tier="A")

add(pmid="42581291", short="Perez-Pastor et al. 2026",
    doi="10.1007/s11356-026-38136-6",
    title="Robust quantification of anhydrosugars and reference material evaluation for biomass burning tracers",
    journal="Environ Sci Pollut Res Int", sub=SENS, design="Laboratory metrology",
    pm="PM biomass burning tracers", geo="Spain",
    endpoint="No health endpoint", n="ASE-BSTFA-GC/MS validated against SRM 2787 and SRM 1649b",
    tier="B")

add(pmid="", short="Zhang et al. 2026b",
    doi="10.5194/amt-19-5281-2026",
    title="Impact of aerosol-type assumption on Landsat 8 atmospheric correction over land",
    journal="Atmos Meas Tech", sub=SENS, design="Model intercomparison",
    pm="Aerosol optical depth", geo="Global",
    endpoint="No health endpoint", n="600 Landsat 8 scenes over 100 AERONET sites",
    tier="B")

add(pmid="", short="Cao et al. 2026",
    doi="10.1016/j.atmosenv.2026.122302",
    title="On-road NO2 and particulate matter across urban road environments from city-scale mobile monitoring",
    journal="Atmos Environ", sub=SENS, design="Metadata only (no abstract)",
    pm="PM2.5, NO2", geo="Not stated",
    endpoint="No health endpoint", n="Abstract not deposited at Crossref on the entry date",
    tier="B")

add(pmid="", short="Zhang et al. 2026c",
    doi="10.1016/j.atmosenv.2026.122298",
    title="Air pollution transport from absorbing aerosol index across multiple payloads",
    journal="Atmos Environ", sub=SENS, design="Metadata only (no abstract)",
    pm="Absorbing aerosol index", geo="Global",
    endpoint="No health endpoint", n="Abstract not deposited at Crossref on the entry date",
    tier="C")

# ---------------------------------------------------------------- EFFECT ESTIMATES
# Only interval estimates transcribed verbatim from abstracts are carried. Exposure
# contrasts are heterogeneous and are stated per row; nothing is pooled.
E = [
    dict(label="Hospitalisation with Parkinson's disease, PM2.5",
         exposure="11.8 vs 3.0 ug/m3, 10-y cumulative",
         est=1.634, lo=1.489, hi=1.792, metric="OR",
         src="Delaney 2026 (Environ Epidemiol)"),
    dict(label="Hospitalisation with Parkinson's disease, NO2",
         exposure="31.7 vs 3.7 ppb, 10-y cumulative",
         est=1.474, lo=1.379, hi=1.575, metric="OR",
         src="Delaney 2026 (Environ Epidemiol)"),
    dict(label="Chronic kidney disease, PM2.5",
         exposure="per 10 ug/m3",
         est=1.32, lo=1.21, hi=1.43, metric="RR",
         src="Li 2026 (Innovation)"),
    dict(label="Glaucoma, long-term PM2.5",
         exposure="highest vs lowest, study-specific",
         est=1.12, lo=1.06, hi=1.18, metric="RR",
         src="Jain 2026 (J Curr Glaucoma Pract)"),
    dict(label="Idiopathic urethral stricture, cumulative exposure",
         exposure="first year of life, weighted index",
         est=1.21, lo=1.07, hi=1.36, metric="RR",
         src="Schlaepfer 2026 (Transl Androl Urol)"),
]

# ---------------------------------------------------------------- LIFE-COURSE
# Counts are non-exclusive and describe THIS issue only.
L = [
    {"n": 0, "note": "no record\nthis issue"},
    {"n": 3, "note": "LRI under-5s,\nLRI children <15,\nfirst-year exposure\nand urethral stricture"},
    {"n": 0, "note": "no record\nthis issue"},
    {"n": 4, "note": "UK Biobank CVD,\nCPS lung-cancer\nmetabolomics,\nCKD ERF, glaucoma"},
    {"n": 3, "note": "Medicare Parkinson's\n65+, COPD >=60,\nLRI >=70"},
]

corpus.save("2026-08-12", P, E,
            entry_window="2026-08-12 -> 2026-08-12", lifecourse=L)
print("saved", len(P), "papers,", len(E), "effects")
