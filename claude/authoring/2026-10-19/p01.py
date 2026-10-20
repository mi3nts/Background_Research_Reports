# -*- coding: utf-8 -*-
P = [
 dict(pmid="42895283", doi="10.7189/jogh.16.04307", journal="J Glob Health",
  short="Zhang CLHLS PM2.5 components cognitive disorders lifestyle mediation 2026",
  title="Association between long-term ambient air pollution exposure and cognitive disorders among older adults in China: the mediating role of lifestyle",
  sub=corpus.NEU, design="Prospective cohort", pm="Long-term PM2.5, sulphate, nitrate, ammonium, O3 (per 10 ug/m3)",
  geo="China (CLHLS, multi-province)", endpoint="Incident cognitive disorders", tier="B",
  n=("Chinese Longitudinal Healthy Longevity Study; Cox, Bayesian WQS and mediation models. Per 10 ug/m3, PM2.5 HR 1.005 "
     "(1.001-1.009), sulphate 1.030 (1.003-1.056), nitrate 1.020 (1.003-1.037), ammonium 1.033 (1.005-1.062), O3 1.006; "
     "mixture OR 1.028 (1.006-1.040) with O3 carrying the largest WQS weight. Favourable vs unfavourable lifestyle HR "
     "0.488 (0.336-0.710); lifestyle mediated 8.4-9.5% of the pollutant associations. Limitation: an HR of 1.005 per "
     "10 ug/m3 is at the floor of detectability and the abstract gives neither n, case count nor how cognitive disorder "
     "was ascertained (MMSE cut-offs in CLHLS are education-sensitive); 'mediation' by lifestyle that is itself a "
     "confounder of residential exposure is not identifiable. Relevance: low - gridded component surfaces, no sensor "
     "component.")),
 dict(pmid="42894454", doi="10.5853/jos.2026.03265", journal="J Stroke",
  short="Lee CRCS-K post-discharge SO2 stroke recurrence PM null 2026",
  title="Post-Discharge Ambient Sulfur Dioxide Exposure and Stroke Recurrence After Acute Ischemic Stroke",
  sub=corpus.CVM, design="Prospective cohort (registry linkage)", pm="3-month post-discharge district PM10, PM2.5, NO2, SO2, CO, O3 (IDW)",
  geo="South Korea (CRCS-K-NIH registry)", endpoint="Stroke recurrence 3-15 months post-discharge", tier="B",
  n=("27,340 acute ischaemic stroke patients (2014-2021), district-level IDW-interpolated pollutant means over the "
     "3 months after discharge; cause-specific Cox with death as competing risk, cluster-robust SEs, splines. 764 "
     "recurrences, 542 deaths over a median 364.8 days. PM10 and PM2.5 showed no association; only SO2 did (overall "
     "spline p=0.024), with Q4 vs Q1 HR 1.19 (0.94-1.50), stronger in age >=75 and women (interaction p 0.051, 0.062). "
     "Limitation: district IDW from sparse monitors gives Berkson-type error that biases PM toward the null, and SO2 "
     "concentrates in harbour cities (Incheon, Ulsan, Busan) - a place effect cannot be excluded. Relevance: moderate - "
     "a null PM result built on interpolation is exactly where denser networks change the answer.")),
 dict(pmid="", doi="10.1021/acs.est.6c05462", journal="Environ Sci Technol",
  short="Wang Guangdong PM2.5 oxidative potential DTT childhood allergy 2026",
  title="Associations of PM2.5 and Its Oxidative Potential with Childhood Allergy-Related Symptoms: A Cross-Sectional Study in Guangdong Province, China",
  sub=corpus.RESP, design="School-based cross-sectional", pm="PM2.5 mass, oxidative potential (DTTv, DTTm), metals, carbonaceous, ions",
  geo="China (Guangdong, six cities)", endpoint="Rhinitis, rhinoconjunctivitis, eczema symptoms", tier="A",
  n=("131,346 children aged 6-18 in six Guangdong cities. PM2.5 mass and DTT oxidative potential were positively "
     "associated with all three symptom outcomes; mass-normalised OP (DTTm) gave the most consistent associations, "
     "lower AIC/BIC and the greatest stability in two-pollutant models. Mixture analyses implicated several "
     "constituents; OP plausibly carried part of the Co, OC, Cu and Hg associations, the largest indirect share 36.2% "
     "for OC and rhinoconjunctivitis via DTTm. Limitation: cross-sectional symptom questionnaires; OP is presumably "
     "modelled or assigned from few filter sites, and the abstract reports no effect sizes, so the model-fit comparison "
     "cannot be weighed against exposure-error differences between metrics. Relevance: high - OP is not measurable by "
     "optical LCS, which bounds what a mass-only network can say about allergy.")),
 dict(pmid="", doi="10.1021/acs.est.6c07407", journal="Environ Sci Technol",
  short="Tang CPS-II plasma proteome air pollution lung cancer ever-smokers 2026",
  title="Analysis of the Potential Mediating Role of Plasma Proteins in the Association Between Air Pollution Exposure and Lung Cancer Risk Among Ever-Smokers",
  sub=corpus.MECH, design="Nested case-control", pm="Six ambient pollutants and their mixture (pre-diagnosis)",
  geo="USA (CPS-II Nutrition Cohort)", endpoint="Incident lung cancer; plasma proteome", tier="B",
  n=("95 matched case-control pairs of ever-smokers with pre-diagnostic plasma proteomics from the CPS-II Nutrition "
     "Cohort. Seventeen proteins associated with both exposures and lung cancer (CX3CL1, ADAM15, CXCL17 among them, "
     "p<0.05); high-dimensional mediation (HIMA) flagged six, including CX3CL1 and CXCL17 (Bonferroni p<0.05). "
     "Limitation: 190 people against a high-dimensional proteome, and the mediation signals disappeared when cases "
     "diagnosed within a year of blood draw were excluded - consistent with reverse causation by subclinical tumour. "
     "The abstract does not name the pollutants' exposure model. Pathways (chemokine signalling, immune modulation) are "
     "hypothesis-generating only. Relevance: low - biomarker discovery, no sensing implication.")),
]
