# -*- coding: utf-8 -*-
P = [
 dict(pmid="42828982", doi="10.1016/j.jhazmat.2026.143759", journal="J Hazard Mater",
  short="Xia et al. 2026",
  title="Long-term exposure to fine particulate matter constituents and lung cancer risk in Chinese never-smokers",
  sub=corpus.OTHR, design="Prospective cohort",
  pm="Annual PM2.5 and constituents (NO3-, NH4+, Cl-, SO4 2-, BC, OM), ChinaHighAirPollutants 2004-2018",
  geo="China (China Kadoorie Biobank, 10 regions)", endpoint="Incident lung cancer in never-smokers", tier="A",
  n=("262,785 never-smokers in the China Kadoorie Biobank, 2,646 incident lung cancers; time-dependent Cox "
     "models per IQR of each constituent, quantile g-computation for the mixture, and a polygenic risk score "
     "for interaction. HR per IQR: nitrate 1.35 (1.23-1.48), ammonium 1.22 (1.13-1.31), chloride 1.20 "
     "(1.12-1.28); mixture HR 1.13 (1.07-1.19), dominated by NO3- and NH4+; additive and multiplicative "
     "NO3- x PRS interaction. Limitation: constituents come from one satellite/ML reanalysis in which "
     "nitrate and ammonium are strongly collinear and partly inherited from total-mass predictors, so "
     "'nitrate drives the risk' may be 'the best-resolved component wins'; second-hand smoke and cooking "
     "fuel only partly captured. Relevance: high - constituent-specific risk is the argument for "
     "composition-capable nodes (nitrate is semi-volatile and biased low on heated optical sensors).")),

 dict(pmid="42827617", doi="10.1038/s43247-026-03732-4", journal="Commun Earth Environ",
  short="Quadros et al. 2026",
  title="Global air quality and human health impacts of growing aircraft emissions",
  sub=corpus.BURD, design="Health impact model",
  pm="Aviation-attributable PM2.5 and O3 from a global CTM, 2019 and 2040 scenarios",
  geo="Global", endpoint="Attributable mortality", tier="B",
  n=("Global aircraft emissions projected 2019-2040 and run through a chemistry transport model. 2019: "
     "33,900 (95% CI 23,500-45,600) PM2.5 deaths and 24,600 (15,500-34,200) O3 deaths attributable to "
     "aviation. By 2040 these rise 58%/82% (low), 119%/148% (baseline) and 169%/205% (high scenario); "
     "the non-aviation background shifts aircraft impacts by up to 44%. Limitation: the CIs propagate "
     "concentration-response uncertainty only, not CTM, inventory (especially cruise NOx-nitrate) or "
     "grid resolution, which dominate a marginal-sector estimate; most PM2.5 impact is secondary nitrate "
     "and sulfate far from airports. Relevance: moderate - the near-airport UFP signal low-cost networks "
     "can see is not the mass-based burden counted here.")),

 dict(pmid="", doi="10.64898/2026.09.30.26364391", journal="medRxiv (preprint)",
  short="Yang and Liu 2026",
  title="No evidence for large causal effects of six air pollutants on non-suppurative otitis media: a two-sample Mendelian randomization study",
  sub=corpus.OTHR, design="Two-sample Mendelian randomisation",
  pm="Genetic instruments for PM2.5, PM2.5 absorbance, PM2.5-10, PM10, NO2, NOx (UK Biobank GWAS)",
  geo="Europe (UK Biobank exposure; FinnGen R13 outcome)", endpoint="Otitis media with effusion", tier="C",
  n=("Two-sample MR with UK Biobank pollutant GWAS and FinnGen R13 OME (12,397 cases, 464,237 controls); IVW "
     "primary, full pleiotropy battery, positive (asthma, rhinitis, CRS) and negative (suppurative OM) "
     "controls. No pollutant survived FDR; the nominal PM10 OR 1.56 (0.95-2.55) reversed with the 88-SNP "
     "set (0.64, 0.24-1.69). Minimum detectable ORs 1.69-32.1, so moderate effects are not excluded - the "
     "authors say so. Limitation: 'genetic instruments for ambient PM' index residential and behavioural "
     "traits, not exposure; null MR here is uninformative by construction, and MVMR F < 10. "
     "Relevance: low - included as a properly bounded null, not as evidence of absence.")),

 dict(pmid="42824690", doi="10.1093/ckj/sfag318", journal="Clin Kidney J",
  short="Sandal et al. 2026",
  title="Disasters and hazard exposure in end-stage kidney disease: a scoping review of patient outcomes",
  sub=corpus.OTHR, design="Scoping review",
  pm="Poor air quality among heat, disaster and conflict hazards (metric varies by study)",
  geo="Global (30 studies, 10 countries/regions)", endpoint="Mortality, hospitalisation, dialysis disruption", tier="C",
  n=("PRISMA scoping review: 10,040 screened, 30 studies, ~1.07 million dialysis patients and 64,531 "
     "transplant recipients. Poor air quality was associated with 5-139% higher mortality; extreme heat "
     "9-45%; 23-59% of patients had dialysis disruption in disasters. Limitation: scoping design, no "
     "pooling or risk-of-bias grading, and 'poor air quality' spans wildfire smoke, PM2.5 increments and "
     "AQI categories, so the 5-139% range is not an effect size. Relevance: low-moderate - dialysis "
     "patients are an identifiable, routinely contacted population where sensor-triggered alerts "
     "could plausibly be tested.")),
]
