# -*- coding: utf-8 -*-
"""Generate authoring/2026-10-23/pNN.py from summaries keyed by _fresh index; pmid/doi/title
are copied from cache/2026-10-23/_fresh.json (never hand-written). 2026-10-30 recovery run."""
import json, html, re
D = "2026-10-23"
F = json.load(open("cache/%s/_fresh.json" % D))
S = {}
def a(i, journal, short, sub, design, pm, geo, endpoint, tier, n):
    S[i] = dict(journal=journal, short=short, sub=sub, design=design, pm=pm, geo=geo, endpoint=endpoint, tier=tier, n=n)

a(30, "Ann Work Expo Health", "Sim real-time dust monitor bias gravimetric meta-analysis 2026", "SENS",
  "Systematic review + random-effects meta-analysis", "Optical real-time dust monitors (DustTrak, SidePak, pDR) vs gravimetric samplers",
  "Global / multi-region (occupational literature 2010-2025)", "Log response ratio of geometric-mean concentration, RTM vs gravimetric", "A",
  "PRISMA meta-analysis of 112 occupational studies; 96 paired RTM-gravimetric comparisons pooled in a three-level random-effects model. "
  "Professional photometers read 36% high on average: pooled lnR 0.31 (0.25-0.37), I2 78.4%, prediction interval 0.11-0.63. Factory-calibrated "
  "units read 43% high, site-calibrated units 13% high; site-specific calibration was the strongest moderator (beta -0.24, P<0.001), followed by "
  "log GSD of the size distribution (beta 0.15) and RH (beta 0.002 per %). No eligible study compared sub-$500 sensors against gravimetry. "
  "Limitation: geometric-mean ratios from heterogeneous aerosols and campaign lengths; the prediction interval never crosses zero but its width "
  "means a single uncalibrated deployment can be off by 12-88%. Relevance: high - the size-distribution and RH moderators are the same terms LCS "
  "calibration models need, now with a pooled prior.")
a(13, "Environ Sci Technol", "Wang electret HVAC filter charge neutralisation wildfire smoke 2026", "OCC",
  "Materials / filtration", "Flaming/smouldering wood smoke, prescribed-burn smoke and soot challenges; EPA monitor PM2.5 for model inputs",
  "United States (laboratory, prescribed burns, regional wildfire scenario)", "Electret filter fractional efficiency vs loading; modelled indoor PM2.5 protection", "A",
  "Laboratory flaming and smouldering wood smoke, field sampling at prescribed burns and controlled soot challenges on residential electret HVAC "
  "filters. Filtration efficiency collapsed at particle loadings far below those that raise pressure drop; the driver was soot-rich particles "
  "neutralising electret charge irreversibly, not mechanical clogging or organic-aerosol deposition. Built into a dynamic indoor model driven by "
  "EPA monitor data for a regional wildfire event, effective filter life fell from months to days at moderate outdoor PM2.5, with protection "
  "varying by building and ventilation. No efficiency numbers are given in the abstract. Limitation: few filter products and smoke types; "
  "charge loss in the field depends on soot fraction, which varies by fire stage. Relevance: high - indoor/outdoor LCS pairs can detect the "
  "efficiency collapse that pressure-based replacement rules miss.")
a(28, "Environ Res", "Meng traffic noise air pollution lung function randomised crossover 2026", "RESP",
  "Randomised crossover trial", "Roadside PM1, PM2.5, PM10, O3, NO2 and noise during evening rush hour",
  "China (urban roadside)", "FVC, FEV1, FEV1/FVC, FEF25-75 and distal flows", "A",
  "Randomised crossover with four exposure conditions (noise and air pollution separated by intervention) in 51 healthy young adults beside "
  "a busy road at evening rush hour; pollutants and noise measured each session, mixed models adjusted for age, sex and BMI. Per 10 ug/m3 PM10, "
  "FEF75 fell 0.215 L/s; per 10 ug/m3 O3, 0.224 L/s. Noise independently reduced dynamic ventilatory indices, and exploratory interaction "
  "terms suggested noise amplified PM1- and PM2.5-associated FEV1 and small-airway decrements. No CIs in the abstract. Limitation: the four "
  "interventions are not described in the abstract and exposure conditions cannot be blinded, and pollutant contrasts within a single "
  "rush-hour session are small and collinear, so the interaction findings are hypothesis-generating. Relevance: medium - co-located acoustic "
  "and PM nodes are needed to separate the two stressors.")
a(2, "BMC Public Health", "Liu PM2.5 components small for gestational age IVF Guangzhou 2026", "REPR",
  "Case-control study", "Trimester-averaged PM2.5 and SO4, NO3, NH4, OM, BC (gridded estimates at residence)",
  "China (Guangzhou)", "Small for gestational age in IVF pregnancies", "B",
  "Propensity-score-matched case-control within 1,459 IVF conceptions in Guangzhou: 166 SGA cases matched 1:1. Whole-pregnancy PM2.5 OR 1.124 "
  "(1.015-1.245); second trimester 1.082 (1.005-1.165); third trimester 1.075 (1.002-1.154); the exposure increment is not given in the abstract. "
  "SO4, OM and BC were positively associated; mixture models ranked nitrate as the dominant driver, and no subgroup reached significance. "
  "Limitation: 332 matched women give lower CI bounds within 0.2-1.5% of the null across many component-by-window tests, with no multiplicity "
  "correction reported; the component estimates come from a modelled product whose component-specific error is unknown. Relevance: low-medium - "
  "component attribution here rests on modelled speciation that sensor networks cannot supply.")
a(81, "Environ Sci Technol", "Wang seasonal PM size constituents oxylipin panel Beijing 2026", "MECH",
  "Panel study", "27 PM2.5 metrics: mass, UFP and accumulation-mode number, OC, chloride and other constituents",
  "China (Beijing)", "Circulating LTB4 and 5-, 8-, 12-, 15-HETE", "A",
  "Panel of 123 adults in Beijing with repeated visits in winter and summer; 27 PM2.5 mass, size and constituent metrics against five "
  "lipoxygenase-derived oxylipins. Associations peaked at lag 0-1 d; across metrics, oxylipin increases ranged 3.3-114.2%, most robust for UFP, "
  "accumulation-mode number, OC and chloride. UFP showed an exposure-response only in summer: per IQR, +12.9 to +97.7% in summer vs -7.7 to "
  "+18.8% in winter; accumulation-mode and OC effects were larger in winter. No CIs in the abstract. Limitation: 27 metrics x 5 biomarkers x 2 "
  "seasons x several lags is a large test space, and the season contrast also changes time outdoors and ventilation. Relevance: high - size-"
  "resolved number, not mass, carries the summer signal, which mass-only optical sensors cannot report.")
a(107, "npj Clim Atmos Sci", "Langford cooking dominant primary PM1 eddy covariance London Beijing Delhi 2026", "EXPO",
  "Eddy covariance flux measurement, method development", "Chemically resolved non-refractory PM1 fluxes (aerosol mass spectrometry + eddy covariance)",
  "Global / multi-region (London, Beijing, Delhi)", "Source-attributed primary PM1 emission fluxes", "A",
  "Eddy-covariance fluxes with aerosol mass spectrometry and a new source-attribution method in three megacity neighbourhoods. In Delhi, "
  "traffic and combustion dominate primary PM1 emission. In London and Beijing, cooking is the largest local primary source at mealtimes: up to "
  "83% of midday and 87% of early-evening emission in London, 61% and 76% in Beijing. Cooking is absent from national, European and global "
  "inventories, though the London Atmospheric Emissions Inventory's estimate matched. Primary emission sources differ from those controlling "
  "ambient PM1 mass, which is secondary-dominated. Limitation: one flux footprint per city and non-refractory PM1 only (no BC or dust). "
  "Relevance: high - source-resolved flux benchmarks for inventory checks; cooking plumes are a known optical-sensor artefact at street level.")
a(9, "Environ Sci Technol", "Sun respirable mining dust natural killer cell dysfunction 2026", "MECH",
  "In vitro", "Compositionally distinct respirable PM (silica/silicate, iron-bearing, carbonaceous mine dusts)",
  "Not stated in record", "NK-cell viability, cytokines, perforin/granzyme B, K562 killing", "B",
  "In-vitro exposure of NK cells to respirable mineral dusts with a K562 target-cell challenge. Injury was dose- and composition-dependent: "
  "apoptosis/necrosis, shifted cytokines, altered perforin/granzyme B function and impaired killing. Silica- and silicate-rich dusts were worst; "
  "iron-bearing and carbonaceous dusts produced distinct oxidative patterns. Mitochondrial depolarisation, lower mitochondrial mass and lysosomal "
  "deacidification converged across dusts; ascorbic acid partially restored organelle function and IFN-gamma. Doses and their relation to "
  "inhaled lung burden are not given in the abstract. Limitation: an isolated cell line in submerged culture, no lung-burden dosimetry, so the "
  "proposed adverse outcome pathway to lung cancer is inferential. Relevance: low - composition (silica fraction) matters, which mass sensors "
  "cannot resolve. Note: this DOI was held from the 3 Oct issue as unauthored and is now carried here.")
a(77, "Environ Sci Technol", "Liang emergency haze controls causal ML synthetic control Shijiazhuang 2026", "BURD",
  "Augmented synthetic control + weather normalisation", "Monitor PM2.5, PM10, SO2, NO2, CO; PM2.5 source apportionment",
  "China (Shijiazhuang)", "Intervention-attributable emission strength and concentration change", "B",
  "Three-step causal evaluation (meteorological normalisation, augmented synthetic control, ML prediction) of Shijiazhuang's 45-day 'Sharp "
  "Sword' campaign in 2016. Local emission strength fell 4.3% (PM2.5), 4.8% (PM10), 15.8% (SO2), 5.8% (NO2), 15.3% (CO); concentrations fell "
  "42.1 ug/m3 (14.8%) for PM2.5 and 47.4 ug/m3 (12.4%) for PM10. Independent PMF showed vehicle, steelmaking and coal contributions 4.1%, 11.0% "
  "and 21.7% lower than in 2017. PM2.5 still averaged 243.2 ug/m3 during the campaign. Limitation: donor-city synthetic controls share the "
  "regional haze and possibly spillover controls, biasing the effect toward zero; no uncertainty intervals in the abstract. Relevance: medium - "
  "a transferable counterfactual framework for evaluating interventions from network data.")
a(27, "J Hazard Mater", "Perez-Vizcaino PM10 sources Riotinto mining multi-time-resolution PMF 2026", "EXPO",
  "Intensive field campaign, PMF source apportionment", "Hourly XRF elements and Aethalometer BC + daily filter PM10 chemistry",
  "Spain (Riotinto mining district)", "PM10 source contributions", "B",
  "Year-long (July 2024-July 2025) campaign combining an hourly XRF metals monitor and an Aethalometer with daily high-volume quartz-filter "
  "chemistry, merged in multi-time-resolution PMF. Seven sources: waste rock 4.9, regional + traffic 3.6, open pit 1.6, combustion 1.2, aged "
  "marine 1.2, dust 1.1 and copper concentrate 0.7 ug/m3. Daily species identified traffic tracers and SOA that the hourly subset alone missed. "
  "Arsenic was the main geochemical anomaly. Limitation: one receptor site; multi-resolution PMF weights the daily data heavily and factor "
  "uncertainty (bootstrap/DISP) is not reported in the abstract. Relevance: medium - hourly XRF + BC is the reference tier that low-cost "
  "networks around mines would need to be anchored to for metal-rich dust.")
a(62, "Atmos Chem Phys", "Chen primary brown carbon China 2005-2020 trends radiative effect 2026", "EXPO",
  "Chemical transport modelling", "Modelled primary brown carbon (internal-mixing optical model), PM2.5",
  "China", "Surface and column PBrC, sector shares, direct radiative effect", "B",
  "CTM simulation of primary BrC across China, 2005-2020, with an internal-mixing optical model. Mean surface PBrC 0.81 ugC/m3; residential, "
  "industrial and agricultural combustion contributed 57%, 22% and 18%, together 91% of column PBrC in 2010. PBrC fell 20.8% over the period vs "
  "8.1% for PM2.5; direct radiative effect fell from +0.032 to +0.023 W/m2 (-25.7%), 84.2% anthropogenic. Limitation: BrC emission factors and "
  "absorption Angstrom exponents are poorly constrained, and evaluation against measured absorption is not described in the abstract. "
  "Relevance: medium - multi-wavelength absorption (BrC) channels on sensor nodes could test the residential-combustion dominance.")
a(65, "Atmos Chem Phys", "Srivastav ion particle size distribution NPF Indo-Gangetic Plain 2026", "SENS",
  "Long-term field measurement campaign", "Air-ion (0.8-42 nm) and particle (2.5-42 nm) size distributions",
  "India (Sonipat, Haryana)", "NPF event frequency, condensation sink, growth rates", "B",
  "Ion and particle spectrometer measurements at a suburban IGP site, May-December 2023. NPF occurred on 30/35 valid days (86%) in May-June "
  "but 20/73 (28%) in winter/post-monsoon. Morning median condensation sink was lower on event days (0.0095 vs 0.0292 s-1). Growth rates "
  "rose with size, 14.7 nm/h (3-7 nm) to 19.0 nm/h (7-20 nm). Pollution plumes intermittently masked or distorted events, so both visual and "
  "automated classification and growth-rate fitting were unreliable. Limitation: no precursor gas (H2SO4, amines, HOMs) measurements, so "
  "mechanism is unconstrained; eight months at one site. Relevance: medium - in high-CS settings the UFP number seen by condensation or "
  "diffusion-charger sensors is plume- not nucleation-driven.")
a(106, "Atmosphere", "Kuye ultrafine particle respiratory deposition dose wood stoves UK homes 2026", "OCC",
  "Field measurement", "Indoor particle number concentration (1-min) with ICRP deposition model",
  "United Kingdom (four homes)", "Inhaled and respiratory-deposited UFP dose", "B",
  "Exploratory measurements in four UK homes (Ecodesign stove, multifuel Ecodesign stove x2, open fireplace), 11-12 winter days each, 1-min PNC "
  "combined with age/sex/activity ventilation rates and the ICRP model. Daily inhaled dose 0.45-16.0 x10^9 particles/kg/day sitting and "
  "2.37-73.2 x10^9 at moderate activity (4.5-5.3-fold higher). Child scenarios had 2.7-3.8x the adult body-mass-normalised dose; household "
  "mean deposition rate 1.50-5.99 x10^8 particles/min. Limitation: n=4 homes that differ simultaneously in appliance, fuel, room, ventilation "
  "and behaviour, so stove-type effects cannot be identified; doses are modelled from concentration, not measured. Relevance: medium - "
  "residential UFP is invisible to mass sensors; indoor PNC nodes are the relevant instrument.")
a(39, "Research Square (preprint)", "Stange SEM-Raman inhalable particles indoor artificial turf infill 2026", "OCC",
  "Field study", "PM10 mass; single-particle SEM + AI classification + micro-Raman of airborne dust",
  "Norway (two indoor sports halls)", "Infill-derived airborne particle composition and PM10", "B",
  "Air sampling during matches in two Norwegian indoor halls, one with crumb-rubber infill and one with olive-stone/quartz infill, analysed by "
  "correlative SEM, AI particle classification and micro-Raman. Both infills released airborne particles. Olive-stone particles appeared "
  "indoors only; tyre rubber appeared indoors and outdoors, implicating traffic as well as infill. PM10 was 58.4 ug/m3 in the olive-stone hall "
  "vs 6.0 ug/m3 with crumb rubber, and fungal spores were found with the organic infill. Limitation: one hall per infill, so the tenfold PM10 "
  "difference is confounded by hall ventilation, occupancy and cleaning. Preprint. Relevance: low-medium - substituting a 'sustainable' material "
  "changed composition and raised mass.")
a(40, "Research Square (preprint)", "Wang multi-omics Mendelian randomization PM2.5 depression 2026", "NEU",
  "Two-sample Mendelian randomisation", "Genetically predicted PM2.5 exposure (GWAS instruments)",
  "Global / multi-region (GWAS summary data)", "Major depressive disorder; omics mediators", "B",
  "LD-score regression found genetic correlation between 'PM2.5 exposure' and MDD (rg 0.334, P 1.9e-11); two-sample MR gave OR 1.27 "
  "(1.07-1.51) for MDD. Two-step MR identified five blood genes, six brain-region genes and two blood fatty-acid ratios as mediators; no "
  "mediation through CSF metabolites or imaging traits. Limitation: a GWAS of residential PM2.5 indexes where people live, so its instruments "
  "capture SES, urbanicity and migration; the genetic correlation itself shows horizontal pleiotropy with MDD is likely, which violates the "
  "exclusion restriction. The OR has no exposure unit. Preprint. Relevance: low - not an exposure-measurement result.")
a(140, "Ecotoxicol Environ Saf", "Guerra-Ruiz cytokines volcanic emissions Cumbre Vieja ASHES 2026", "RESP",
  "Observational - cross-sectional", "Volcanic gas and particulate exposure (hours of exposure, group membership)",
  "Spain (La Palma)", "Serum TH1/TH2/TH17 biomarkers (48-plex Olink)", "B",
  "Cross-sectional ASHES sub-study after the 2021 Tajogaite eruption: 102 adults (66 general population, 13 occupationally exposed, 23 "
  "asthmatic). Workers had the longest exposure (median 10 h vs 6 h) and higher IL-2, IL-7, IL-17A and IL-17F; asthmatics showed broader "
  "TH1/TH2/TH17 activation, and IL-4 correlated with exposure time in asthmatics (r 0.79). Limitation: exposure is hours of presence, not "
  "measured PM or SO2, and 13 workers is too few for a stable comparison; 48 markers tested without stated correction. Relevance: medium - "
  "the eruption had dense monitoring; linking those PM records to individuals would turn this into an exposure-response study.")
a(145, "Infect Prev Pract", "Mohammed mobile HEPA-UV air decontamination operating theatre 2026", "OCC",
  "Intervention field trial (non-randomised)", "Optical particle counts (0.3, 0.5 um and larger) and culturable CFU",
  "India (New Delhi)", "Particle count and airborne microbial load", "C",
  "Before-after evaluation of a mobile HEPA + UV decontamination unit in one operating theatre over 15 days (July 2025). Mean total particle "
  "count fell from 6,836 to 4,072 particles/m3 (-40.4%), significant in the 0.3 and 0.5 um channels; CFU fell from 34.5 to 15.2 CFU/m3 "
  "(P 0.003). Limitation: one theatre, short before-after design with no control period or blinding to activity level, and no clinical outcome "
  "(surgical-site infection). Relevance: low-medium - shows optical counters as the performance metric for portable cleaners in clinical rooms.")
a(128, "Environ Monit Assess", "Liu PM2.5 sources mixing state Chengdu Kangding altitude 2026", "EXPO",
  "Source apportionment", "Filter PM2.5 chemistry (ions, carbon) and single-particle mass spectrometry",
  "China (Chengdu and Kangding, Sichuan)", "PM2.5 composition, PMF sources, mixing state", "C",
  "Summer and winter PM2.5 sampling at Chengdu (500 m) and Kangding (2,500 m). Winter PM2.5 79.4 vs 15.2 ug/m3, summer 29.1 vs 8.1. "
  "Inorganic ions dominated in Chengdu, carbonaceous species in Kangding; sulfate in summer gave way to nitrate in winter. PMF: Chengdu "
  "combustion 26.0%, traffic 32.4%, secondary 35.3%; Kangding combustion 47.9%. Single-particle data showed more SIA particles in Chengdu "
  "(29.0% vs 17.6%) and more organic-SIA internal mixing in Kangding. Limitation: two seasons, two sites; the altitude contrast is confounded "
  "with city size and heating fuel. Relevance: low - descriptive regional chemistry.")
a(24, "Environ Sci Technol", "Ghosh meter-scale heterogeneity new particle formation 3D model 2026", "EXPO",
  "Theory / simulation", "Simulated nucleation-mode particle number and size distributions (3D-ICAM, 10 m resolution)",
  "Not stated in record", "Nucleation intensity, sub-3 nm growth rates, size distributions", "B",
  "A 10 m resolution 3D multiphysics aerosol model (3D-ICAM) compared with an equivalent box model across emission geometries. Under weak "
  "winds (<1 m/s), it reproduced nucleation hotspots, intermittent multi-episode nucleation and persistent bimodal size distributions that the "
  "homogeneous case lacks. Resolving spatial structure raised predicted sub-3 nm growth rates up to ~20-fold, bringing them into the observed "
  "range, because transport-generated microenvironments relax the growth-scavenging competition. Limitation: idealised geometries; agreement "
  "with observations is at the level of growth-rate ranges, not site-specific validation. Relevance: medium - implies point UFP measurements in "
  "streets sample sub-grid hotspots; dense number-sensor networks are the natural test.")
a(38, "Asia Pac J Clin Oncol", "Zhang early-onset female lung cancer burden GBD 2021 2026", "BURD",
  "Burden estimation (GBD)", "Ambient particulate matter pollution (GBD risk factor)",
  "Global / multi-region (GBD 2021)", "Early-onset female tracheal, bronchus and lung cancer ASIR, ASDR, DALYs", "C",
  "GBD 2021 secondary analysis of early-onset (under 50) female TBL cancer, 1990-2021. Global rates declined (all EAPCs <0), but low-middle SDI "
  "regions rose (DALY EAPC 0.66) and South Asia fastest (DALY EAPC 1.42). Ambient PM was the fastest-growing attributable risk "
  "(attributable DALY rate EAPC 1.22, ASDR 1.27). Limitation: GBD attributable burden is model output that inherits the exposure surface and "
  "IER curves; in young women with few cases, estimates in low-SDI regions rest largely on modelled covariates rather than registries. "
  "Relevance: low - burden, not measurement.")
a(1, "Nurs Clin North Am", "Cantu air quality across the lifespan nursing response review 2026", "BURD",
  "Narrative review", "PM2.5, O3, NO2 (reviewed)", "Global / multi-region (with United States focus)",
  "Cardiopulmonary, neurocognitive and perinatal morbidity (reviewed)", "C",
  "Narrative review for nurses of global and US air quality trends and health effects across the lifespan, citing ~8 million deaths/year "
  "attributable to air pollution, with PM2.5, O3 and NO2 as the principal pollutants. Covers cardiopulmonary, neurocognitive and perinatal "
  "outcomes, nursing practice and policy, and argues for integrating air-quality awareness into nursing curricula. No new data. Limitation: "
  "non-systematic; no synthesis of effect sizes. Relevance: low - possible audience for patient-facing use of public sensor maps.")
a(129, "Nurs Clin North Am", "Atkin air quality excess heat pregnancy outcomes review 2026", "REPR",
  "Narrative review", "Ambient air pollution and heat (reviewed)", "Not stated in record",
  "Adverse pregnancy outcomes (reviewed)", "C",
  "Narrative review on combined poor air quality and excess heat in pregnancy. Argues that physiological adaptations of pregnancy raise "
  "susceptibility, that structural determinants concentrate exposure in some populations, and that nurses should educate patients, promote "
  "adaptation and advocate for climate mitigation. No quantitative synthesis in the abstract. Limitation: non-systematic; heat-pollution "
  "interaction is asserted rather than quantified. Relevance: low - clinical guidance context only.")
a(68, "Atmos Environ", "Cai self-supervised stacking particulate nitrate sparse observations 2026", "SENS",
  "Metadata only (no abstract)", "Particulate nitrate (estimated from sparse ground observations)",
  "China (two urban agglomerations)", "Gridded particulate nitrate estimates", "B",
  "Title and authors only (Cai, He, Li, Liu et al.). No abstract was retrievable from Crossref, Europe PMC or Semantic Scholar at harvest. "
  "The title describes a self-supervised stacking ensemble that estimates particulate nitrate in two Chinese urban agglomerations from sparse "
  "ground observations. Predictors, validation design and skill cannot be stated. Limitation: unverifiable beyond the title; with sparse "
  "speciation sites, random cross-validation would overstate skill (see the 22 Oct blocked-CV record). Relevance: medium - component "
  "estimation under sparse reference sites is the same problem as filling between LCS anchors.")
a(70, "Atmos Environ", "Kaskaoutis in situ aerosol optical properties eastern Mediterranean 2026", "EXPO",
  "Metadata only (no abstract)", "In situ aerosol scattering and absorption",
  "Not stated in record (eastern Mediterranean)", "Seasonal aerosol optical properties and source attribution", "C",
  "Title and authors only (Kaskaoutis, Baalbaki, Bimenyimana et al.). No abstract was retrievable at harvest. The title describes in situ "
  "scattering/absorption measurements at a background eastern Mediterranean site, with seasonal variability, regional transport and source "
  "attribution. Site, instruments and values cannot be stated. Limitation: unverifiable beyond the title. Relevance: low-medium - background optical properties set the mass-scattering "
  "efficiency that optical PM sensors assume.")
a(71, "Atmos Pollut Res", "Zhao PM2.5-O3 co-pollution episodes BTH YRD 2026", "EXPO",
  "Metadata only (no abstract)", "PM2.5 and O3 co-pollution episodes (monitoring data)",
  "China (Beijing-Tianjin-Hebei and Yangtze River Delta)", "Characteristics and causes of co-pollution episodes", "C",
  "Title and authors only (Zhao, Xu, Gao, Zhang et al.). No abstract was retrievable at harvest. The title describes an episode analysis of "
  "simultaneous PM2.5 and O3 exceedance in BTH and the YRD, including causes. Data sources, period and attribution method cannot be stated. "
  "Limitation: unverifiable beyond the title. Relevance: low-medium - co-pollution episodes are where PM-only alerts from sensor networks "
  "understate risk.")

ORDER = [30,13,28,2,81,107,9,77,27,62,65,106,39,40,140,145,128,24,38,1,129,68,70,71]
def clean(t): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html.unescape(t))).strip()
recs = []
for i in ORDER:
    r = F[i]; s = S[i]
    recs.append(dict(pmid=r.get("pmid") or "", doi=r["doi"].lower(), journal=s["journal"], short=s["short"],
        title=clean(r["title"]), sub="corpus." + s["sub"], design=s["design"], pm=s["pm"], geo=s["geo"],
        endpoint=s["endpoint"], tier=s["tier"], n=s["n"]))
for k in range(0, len(recs), 4):
    out = ["# -*- coding: utf-8 -*-", "P = ["]
    for d in recs[k:k+4]:
        out.append(" dict(" + ", ".join("%s=%s" % (kk, vv if kk == "sub" else repr(vv)) for kk, vv in d.items()) + "),")
    out.append("]")
    open("authoring/%s/p%02d.py" % (D, k // 4 + 1), "w", encoding="utf-8").write("\n".join(out) + "\n")
    w = [len(d["n"].split()) for d in recs[k:k+4]]
    print("p%02d" % (k // 4 + 1), w)
print("records", len(recs))
