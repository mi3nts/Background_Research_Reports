# -*- coding: utf-8 -*-
P = [
 dict(pmid="42958371", doi="10.1186/s12931-026-03804-1", journal="Respir Res",
  short="Chen pirfenidone fine particulate matter EMT mitochondrial fission autophagy 2026",
  title="Pirfenidone reduces fine particulate matter-induced epithelial to mesenchymal transition in lung epithelial cells through regulating mitochondrial fission and autophagy",
  sub=corpus.MECH, design="Animal + in vitro", pm="Fine PM (standard reference material type not stated), 100 ug/mL in vitro; intratracheal in mice",
  geo="Laboratory (no field site)", endpoint="EMT markers, mitochondrial fission, autophagic flux, lung histology", tier="C",
  n=("A549 cells exposed to 100 ug/mL fine PM lost E-cadherin and gained vimentin, alpha-SMA, TGF-beta1, Snail and Slug, "
     "turned spindle-shaped and migrated more; PM increased mitochondrial fission and LC3B/p62 accumulation, i.e. "
     "impaired autophagic flux. Intratracheal PM in mice reproduced EMT markers, inflammatory infiltration and alveolar "
     "wall thickening. Pirfenidone reversed these effects in vitro and reduced collagen deposition in vivo. Limitation: "
     "100 ug/mL on a cell monolayer and bolus instillation are far above realistic deposited doses, and A549 is a "
     "carcinoma line; the drug result says nothing about population exposure. Relevance: low - mechanism for "
     "PM-associated fibrosis; no measurement content.")),
 dict(pmid="42962646", doi="10.1016/j.jhazmat.2026.143978", journal="J Hazard Mater",
  short="Zakari PM1 microbial profiles lung gut microbiome mice 2026",
  title="Associations of particulate matter-associated microbial profiles with lung and intestinal microbiomes in healthy mice",
  sub=corpus.MECH, design="Murine inhalation exposure", pm="Ambient PM1 (ions, metals, carbon, oxidative potential, 16S) vs HEPA-filtered and clean air",
  geo="Not stated in record (ambient-air exposure chamber)", endpoint="Lung and gut 16S microbiome composition; faecal SCFAs", tier="C",
  n=("Mice were housed under ambient PM1, HEPA-filtered air or clean air; PM1 was characterised for ions, metals, carbon "
     "fractions, oxidative potential and its own 16S microbiome (Proteobacteria-dominated). Lung diversity barely "
     "changed while the gut microbiome shifted: PM1 reduced Actinobacteriota and Bacteroidota and raised Proteobacteria "
     "versus both control arms. Eleven families and six genera overlapped among PM1, lung and gut communities in the PM1 "
     "group. Limitation: group sizes and exposure concentrations are not given in the abstract, gases co-vary with PM1, "
     "and taxon overlap does not show transfer from air to gut. Relevance: low - airborne microbial load is a PM "
     "component no optical sensor resolves.")),
 dict(pmid="42958911", doi="10.1002/em.70088", journal="Environ Mol Mutagen",
  short="Gautam diesel exhaust miR-133b-3p CTGF Hippo ECM remodeling mouse lung 2026",
  title="Diesel Exhaust-Induced miR-133b-3p Downregulation and CTGF-Linked Hippo Pathway Inactivation Promote ECM Remodeling and Inflammation in Mouse Lungs",
  sub=corpus.MECH, design="Animal exposure study", pm="Whole diesel exhaust, 30 min/day, 5 d/week, 8 weeks vs filtered air",
  geo="India (inferred from author group; laboratory)", endpoint="Lung miRNA expression, Hippo/CTGF signalling, BALF cytokines, MMP/LOX", tier="C",
  n=("C57BL/6 mice received diesel exhaust 30 min/day, 5 days/week for 8 weeks versus filtered air. Microarrays showed "
     "miR-133b-3p down more than 2-fold; CTGF was confirmed as a direct target in A549 cells (mimic reduced CTGF mRNA "
     "p=0.0054, protein p=0.0001). In vivo, exhaust raised CTGF, lowered P-YAP/YAP (Hippo inactivation), increased "
     "BALF IL-18, IL-1beta and GM-CSF, raised MMP-3/7/12 and lowered LOXL1/4, consistent with ECM remodelling. "
     "Limitation: exhaust dose (PM mass, NO2) is not reported in the abstract, so particle and gas effects cannot be "
     "separated; the CTGF link is correlative in vivo. Relevance: low - traffic-exhaust mechanism; supports particle "
     "number or black carbon over mass as the near-road metric.")),
 dict(pmid="", doi="10.1016/j.atmosenv.2026.122447", journal="Atmos Environ",
  short="Yingkar PM2.5-bound PAHs Central Asia urban trends sources risk 2026",
  title="Environment-to-Health Linkages of PM2.5-Bound Polycyclic Aromatic Hydrocarbons in Urban Cities of Central Asia: Trends, Sources, and Risk Assessment",
  sub=corpus.EXPO, design="Metadata only (no abstract)", pm="PM2.5-bound PAHs",
  geo="Kazakhstan (Central Asian cities; inferred from title and author group)", endpoint="PAH trends, sources and health risk", tier="C",
  n=("Title and authors only (Yingkar, Omarova, Sovetova, Alibekov et al.). No abstract was retrievable from Crossref or "
     "Semantic Scholar at harvest. The title describes trends, source apportionment and health-risk assessment of "
     "PM2.5-bound PAHs across urban Central Asian cities - a region with sparse speciation data and heavy coal "
     "heating. Cities, sampling design, concentrations and risk estimates are not available; nothing is inferred. "
     "Relevance: medium - coal-heating PAH peaks in Almaty-type basins are where low-cost PM networks already operate "
     "without any chemical reference; retry the abstract on a later run.")),
]
