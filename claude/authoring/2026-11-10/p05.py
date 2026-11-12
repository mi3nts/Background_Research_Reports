# -*- coding: utf-8 -*-
exec(open("authoring/2026-11-10/_rec.py", encoding="utf-8").read(), globals())
P = [
 R(86, "Environ Pollut",
  short="Chi NYCU PM-bound PCDD/F PCB PCN TEQ Ulaanbaatar Beijing Taipei PMF source apportionment cancer risk dust events",
  sub=corpus.EXPO, design="Intensive field campaign, PMF source apportionment",
  pm="PM2.5-bound (Beijing, Taipei) and TSP-bound (Ulaanbaatar) PCDD/Fs, PCBs, PCNs; filter sampling",
  geo="Asia", endpoint="TEQ concentrations, PMF sources, lifetime cancer risk", tier="B",
  basis="Lab / research instrument", affil="National Cheng Kung University, Taiwan; National Yang Ming Chiao Tung University, Taiwan",
  n=("61 TSP samples in Ulaanbaatar, 24 in Beijing (22 PM2.5) and 26 PM2.5 in the Taipei area. PM2.5-bound PCDD/F TEQ averaged 107 fg/m3 in "
     "Beijing against 11.5 in Taipei; Ulaanbaatar TSP reached 128. Beijing cold-season PCDD/F TEQ rose 19-fold, and during dust events Beijing TSP "
     "TEQ (76.7) exceeded Ulaanbaatar's (48.9). PMF attributed PCDD/Fs to open burning and traffic (Ulaanbaatar), waste incineration and dust "
     "(Beijing) and boilers plus incineration and traffic (Taipei). PCDD/Fs drove over 98% of carcinogenic risk, which exceeded 1e-6 in "
     "Ulaanbaatar and Beijing, but non-inhalation pathways carried 65-90% of it. Sampling periods and size cuts differ by city, limiting comparison. "
     "Relevance: indirect - mass-based sensors cannot see the toxic-equivalent fraction that drives risk here.")),
 R(28, "Atmos Pollut Res",
  short="Peanusaha Auvermann Texas cattle feedlot evening dust peak Hot-Dry-Windy index water balance PM10 surface moisture",
  sub=corpus.EXPO, design="Statistical analysis of monitoring data",
  pm="Evening PM10 concentrations downwind of a cattle feedlot",
  geo="USA", endpoint="Variance in evening PM10 explained by an HDW-based moisture index", tier="B",
  basis="Not stated", affil="",
  n=("Partial abstract (Crossref). Feedlot evening dust peaks have been documented for decades but their meteorological drivers lack long-term "
     "study, and direct surface-moisture measurement is labour-intensive. The authors adapt the Hot-Dry-Windy index and couple it with "
     "precipitation in an empirical water-balance model to estimate pen-surface moisture from routine meteorology. Under the driest surface "
     "conditions the index explained 43% of the variance in evening PM10 (R2 0.433, r 0.658). The deposited text ends there, so the site, record "
     "length, PM10 instrument and performance under wetter conditions are unknown. "
     "Relevance: a cheap meteorological predictor of agricultural dust episodes, testable against low-cost PM10 sensors at feedlot fences.")),
 R(0, "Toxicology",
  short="Shandong mouse intratracheal PM2.5 ovary single-cell RNA-seq leukocyte infiltration granulosa cholesterol biosynthesis STAT1 atresia",
  sub=corpus.REPR, design="Animal experiment",
  pm="Repeated pulmonary PM2.5 instillation in mice (dose not stated in abstract)",
  geo="China", endpoint="Ovarian single-cell transcriptome, immune infiltration, follicular atresia", tier="C",
  basis="Lab / research instrument", affil="Shandong Provincial Hospital, China; Shandong First Medical University, China",
  n=("Mouse model of repeated pulmonary PM2.5 instillation with ovarian single-cell RNA-seq and in situ validation. Instillation expanded the "
     "ovarian immune compartment (B-lineage lymphocytes, neutrophils); resident macrophages took a C1qa-rich scavenger profile without NLRP3 "
     "activation. Immune-derived TGF-beta1 and TNF signalling raised JAK-STAT activity in somatic cells and suppressed the granulosa "
     "cholesterol-biosynthesis programme; trajectory modelling nominated STAT1 for follicular atresia, with p-STAT1 and TUNEL confirming in "
     "tissue. Dose, particle source and group sizes are not in the abstract, and bolus instillation is not inhalation. "
     "Relevance: low for sensing; extends the lung-to-ovary immune route behind epidemiological fecundity signals.")),
 R(2, "Environ Toxicol Pharmacol",
  short="Korea University PM10 brain vascular endothelial cells apoptosis DNA damage MAPK NF-kB NAC zebrafish developmental toxicity",
  sub=corpus.MECH, design="Animal + in vitro",
  pm="PM10 (source and dose not stated in abstract)",
  geo="South Korea", endpoint="Endothelial viability, apoptosis markers, zebrafish brain vascular phenotype", tier="C",
  basis="Lab / research instrument", affil="Korea University, South Korea; Korea University, South Korea",
  n=("PM10 reduced brain vascular endothelial cell viability and raised TUNEL labelling, cleaved caspase-3 and PARP, intrinsic and death-receptor "
     "apoptotic proteins, DNA-damage-response markers, MAPK/NF-kB components and lipid and protein oxidation. N-acetylcysteine pretreatment "
     "improved survival and reduced caspase-substrate cleavage, implicating redox processes. In zebrafish, PM10 produced concentration-dependent "
     "developmental toxicity and altered brain vascular phenotypes. The authors themselves describe the causal chain as unresolved; doses, "
     "particle provenance and whether concentrations approach realistic deposition are not given in the abstract. "
     "Relevance: low - mechanism plausibility for the cerebrovascular and neurodevelopmental associations seen in cohorts.")),
]
