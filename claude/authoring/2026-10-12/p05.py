# -*- coding: utf-8 -*-
P = [
 dict(pmid="42850264", doi="10.1038/s41467-026-77623-9", journal="Nat Commun",
  short="Liang CHD circulating proteins 2026",
  title="A nested case-control study of air pollution and congenital heart defects via circulating proteins",
  sub=corpus.REPR, design="Nested case-control", pm="Periconception PM2.5, PM10, NO2; maternal and cord serum proteomics",
  geo="China", endpoint="Congenital heart defects", tier="B",
  n=("Maternal periconception PM2.5, PM10 and NO2 were each associated with CHD, NO2 most strongly; supervised sparse "
     "PLS identified pollutant-specific protein signatures in maternal and umbilical cord serum that tracked exposure "
     "and CHD, implicating FGF-4, VEGF-D, MSP and angiogenin. Limitation: the abstract gives no effect sizes or n; "
     "cord serum is sampled at delivery, months after cardiogenesis, so a cord-protein signature cannot be the mechanism "
     "of a first-trimester malformation, and supervised signature selection on the same outcome inflates association. "
     "Relevance: moderate - periconception exposure windows are short, which favours high-resolution residential "
     "estimates. Held from the 9 Oct issue.")),
 dict(pmid="42852147", doi="10.3389/ftox.2026.1943932", journal="Front Toxicol",
  short="Yu alveolar organoid PM2.5 2026",
  title="Differential toxicity of water- and DMSO-extractable PM2.5 fractions in human alveolar organoids",
  sub=corpus.MECH, design="In vitro exposure", pm="Water- vs DMSO-extractable PM2.5 fractions",
  geo="Laboratory (human alveolar organoids)", endpoint="Organoid morphology, ROS, cell death, AT2/AT1 ratio", tier="C",
  n=("Human alveolar organoids exposed to extracted PM2.5 showed dose- and time-dependent morphological damage, more "
     "severe for the DMSO-extractable (organic) fraction, with ROS rise, cell death and a sustained fall in AT2 cells "
     "plus a small AT1 increase suggesting AT2-to-AT1 transdifferentiation. Limitation: doses are not reported in "
     "deposited-mass terms, so relevance to ambient exposure is unknowable, and extraction solvents select chemistry "
     "rather than particles. Relevance: low - model development. Held from the 9 Oct issue.")),
 dict(pmid="42861712", doi="10.1093/annalsats/aaoag317", journal="Ann Am Thorac Soc",
  short="Trachalaki IPF PM2.5 2026",
  title="Are Short-Term Increases in PM2.5 Linked to Respiratory Hospitalizations in IPF?",
  sub=corpus.RESP, design="Metadata only (no abstract)", pm="Short-term PM2.5",
  geo="Not stated", endpoint="Respiratory hospitalisation in IPF", tier="C",
  n=("No abstract in PubMed, Europe PMC or Semantic Scholar at harvest; the title format suggests a research letter on "
     "short-term PM2.5 and respiratory admissions in idiopathic pulmonary fibrosis. Recorded for coverage only - no "
     "result can be summarised, and none is inferred. Relevance: moderate if positive, because IPF is a small, "
     "identifiable cohort for which personal or home-sensor exposure is feasible.")),
 dict(pmid="", doi="10.1016/j.atmosenv.2026.122407", journal="Atmos Environ",
  short="Chen toluene soot toxicity 2026",
  title="Oxidative toxicity and cytotoxicity of toluene combustion soot particles mediated by their microstructure",
  sub=corpus.MECH, design="Metadata only (no abstract)", pm="Laboratory toluene-flame soot",
  geo="Laboratory", endpoint="Oxidative potential and cytotoxicity", tier="C",
  n=("No abstract retrievable at harvest. From the title: soot generated from toluene combustion, with oxidative "
     "potential and cytotoxicity attributed to particle microstructure (likely graphitisation/nanostructure order). "
     "Recorded for coverage; no result is inferred. Relevance: low-moderate - if microstructure rather than mass sets "
     "toxicity, mass-based optical sensing misses a toxicity axis entirely.")),
]
