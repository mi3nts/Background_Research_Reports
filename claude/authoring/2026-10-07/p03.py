# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="42839983", doi="10.3389/freae.2026.1833533", journal="Front Epigenet Epigenom",
  short="Env epigenetics review 2026",
  title="Environmental epigenetic modifiers in neurodegenerative diseases: a systematic review of epigenomic mechanisms and therapeutic targets",
  sub=corpus.MECH, design="Systematic review (PRISMA)",
  pm="Particulate matter among heavy metals, gaseous pollutants and synthetic neurotoxicants (review)",
  geo="Global", endpoint="Neurodegenerative outcomes (mechanistic)", tier="C",
  n=("A PRISMA-structured review of DNA methylation, histone modification and non-coding RNA changes "
     "linking environmental neurotoxicants - particulate matter among them - to neurodegeneration, with "
     "emphasis on developmental windows and life-course exposure. Limitation: PRISMA structure without "
     "quantitative synthesis, risk-of-bias assessment or any pooling, over a literature in which "
     "publication bias toward positive methylation findings is severe; particulate matter is treated "
     "interchangeably with metals and solvents despite incomparable exposure metrics. Relevance: low as "
     "evidence. Entered because the epigenetic mediator claim keeps appearing beside the dementia-mortality "
     "results in this backfill and it should be visible how thin the review base under it is.")),

 dict(pmid="", doi="10.1186/s12989-026-00702-8", journal="Part Fibre Toxicol",
  short="Mountain West wood smoke 2026",
  title="Household wood smoke exposure, lung black carbon deposition, and genomic instability in U.S. Mountain West residents",
  sub=corpus.MECH, design=MO,
  pm="Metadata only - household wood smoke, lung black carbon deposition and genomic instability (by title)",
  geo="USA (Mountain West)", endpoint=NA, tier="A",
  n=("Metadata-only record: Crossref deposited title, authors and DOI on 7 Oct; neither PubMed, Europe PMC "
     "nor Semantic Scholar held an abstract, and Scholar Gateway is still refusing. By title this is an "
     "unusually direct chain - a household exposure, a measured internal dose (lung black carbon "
     "deposition) and a genomic endpoint in the same human subjects. Internal dose is what every "
     "ambient-monitoring epidemiology study substitutes a model for, so a paper that measures it is worth "
     "the retry. Relevance: high, the highest of the day's metadata-only records; flagged for full-text "
     "read.")),

 dict(pmid="", doi="10.1016/j.envpol.2026.129304", journal="Environ Pollut",
  short="PM2.5 and Mn biomarkers 2026",
  title="Differential associations of PM2.5 and particulate manganese with blood-based amyloid and tau biomarkers",
  sub=corpus.NEU, design=MO,
  pm="Metadata only - PM2.5 and particulate manganese against blood amyloid and tau biomarkers (by title)",
  geo="Not recoverable from metadata", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 7 Oct with no abstract. By title, "
     "PM2.5 mass and a specific metal constituent are contrasted against blood-based amyloid and tau - "
     "the preclinical Alzheimer biomarkers. Separating a constituent from total mass against a "
     "mechanistic biomarker is precisely the design the UFP dementia-mortality cohort (5 October) and the "
     "nitrate lung-cancer cohort (3 October) both point toward. Relevance: high; on the retry list.")),

 dict(pmid="", doi="10.1002/lary.70976", journal="Laryngoscope",
  short="Vocal fold fibroblasts 2026",
  title="Effects of Fine Particulate Matter (PM2.5) in Cultured Human Vocal Fold Fibroblasts",
  sub=corpus.MECH, design=MO,
  pm="Metadata only - PM2.5 applied to cultured human vocal fold fibroblasts (by title)",
  geo="Not recoverable from metadata", endpoint=NA, tier="C",
  n=("Metadata-only record: Wiley deposited title, authors and DOI on 7 Oct with no abstract. By title, an "
     "in-vitro exposure of human vocal fold fibroblasts to PM2.5 - an unusual target tissue, and a "
     "plausible one given that the larynx sits in the deposition path of coarse and fine particles and "
     "that occupational voice disorders cluster in dusty trades. Relevance: low-moderate; on the retry "
     "list.")),

 dict(pmid="", doi="10.1016/j.atmosenv.2026.122406", journal="Atmos Environ",
  short="Hayli Gubbi eruption 2026",
  title="Short-term Atmospheric Impacts of the Hayli Gubbi Volcanic Eruption 2025",
  sub=corpus.EXPO, design=MO,
  pm="Metadata only - short-term atmospheric impacts of a 2025 eruption (by title)",
  geo="Ethiopia (Hayli Gubbi, Afar)", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 7 Oct with no abstract. By title, "
     "the short-term atmospheric impact of the 2025 Hayli Gubbi eruption. Volcanic SO2 and ash plumes are "
     "the natural experiment that tests whether a sparse monitoring network can detect and attribute a "
     "known, dated, large perturbation - and East African ground monitoring is close to absent, so the "
     "answer is informative either way. Relevance: moderate; on the retry list.")),

 dict(pmid="", doi="10.1016/j.atmosenv.2026.122408", journal="Atmos Environ",
  short="N-containing OA 2026",
  title="Unveiling the Precursor-Specific Aqueous Formation Mechanisms of Nitrogen-Containing Organic Aerosols",
  sub=corpus.EXPO, design=MO,
  pm="Metadata only - precursor-specific aqueous formation of nitrogen-containing organic aerosol (by title)",
  geo="Not recoverable from metadata", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 7 Oct with no abstract. By title, "
     "a mechanistic account of how particular precursors form nitrogen-containing organic aerosol in the "
     "aqueous phase. Aqueous-phase secondary formation is humidity-dependent, which makes it the physical "
     "process underneath the humidity correction every optical low-cost sensor applies - the correction "
     "treats growth as hygroscopic swelling when some of it is mass that was not there before. "
     "Relevance: moderate-high; on the retry list.")),
]
