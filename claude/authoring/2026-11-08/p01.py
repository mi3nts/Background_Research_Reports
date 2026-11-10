# -*- coding: utf-8 -*-
P = [
 dict(pmid="43000521", doi="10.1007/s44197-026-00623-x", journal="J Epidemiol Glob Health",
  short="Liu CHARLS cohort county PM2.5 solid fuel joint exposure incident stroke 2026",
  title="Associations of PM(2.5) Exposure and Solid Fuel Use With Incident Stroke: Evidence From a Longitudinal Chinese Cohort.",
  sub=corpus.CVM, design="Prospective cohort",
  pm="One-year pre-baseline county-level PM2.5 from the China High Air Pollutants (CHAP) dataset; household solid cooking/heating fuel by questionnaire",
  geo="China", endpoint="Incident stroke", tier="B",
  basis="Satellite-fused", affil="First Affiliated Hospital of Henan Medical University, China; First Affiliated Hospital of Henan Medical University, China",
  n=("CHARLS, 13,917 adults (mean age 58.9 y), 1,060 incident strokes. High vs low ambient PM2.5: HR 1.25 (1.04-1.51); solid fuel users vs non-users: "
     "HR 1.38 (1.18-1.62); multiplicative interaction p=0.022; HR 1.10 (1.05-1.15) per step of an ordinal joint-exposure score. The PM2.5 contrast is categorical "
     "and the cut-point and per-unit estimate are not in the abstract. County-level assignment from a satellite-fused product with one pre-baseline year gives "
     "every resident of a county the same value, and solid fuel is a one-time self-report with no measured household PM, so the joint category mixes an "
     "ecological and a proxy exposure. Relevance: indirect - indoor-outdoor co-exposure is exactly what paired household and ambient low-cost sensors could resolve.")),
 dict(pmid="43000441", doi="10.1186/s40246-026-01012-y", journal="Hum Genomics",
  short="Sarigiannis URBANOME nine-city urban living labs exposome wearable sensors interventions 2026",
  title="URBANOME: an exposome-based framework linking urban interventions to molecular, health, and policy-relevant outcomes.",
  sub=corpus.EXPO, design="Intervention field trial (non-randomised)",
  pm="Ambient and personal exposure monitoring (wearable sensors, smartphone apps) plus agent-based population exposure modelling",
  geo="Europe", endpoint="Annoyance, sleep breathing problems, FVC, metabolomics/transcriptomics", tier="C",
  basis="Personal / wearable", affil="Aristotle University of Thessaloniki, Greece; Aristotle University of Thessaloniki, Greece",
  n=("Horizon 2020 framework run in nine European urban living labs (Aarhus to Thessaloniki) evaluating co-created active-mobility, greening and "
     "traffic-calming interventions before and after, with wearable and ambient monitoring, agent-based exposure modelling, spirometry, blood pressure, HRV and "
     "omics. Pilot findings are qualitative: self-reported pollution annoyance and sleep-related breathing problems fell, pollution-related FVC differences "
     "attenuated in higher-exposure neighbourhoods; a four-metabolite panel separated pre/post samples with AUROC near 1.0, which the authors call likely "
     "overoptimistic. No PM concentration change, effect size or CI is reported in the abstract; designs, comparators and follow-up differ by site, and "
     "there is no control arm. Relevance: direct for method - an operational template for coupling personal sensors to intervention evaluation.")),
 dict(pmid="42997827", doi="10.1016/j.isci.2026.118066", journal="iScience",
  short="Jeong review automated robotic field-deployable platforms aerosol cytotoxicity analysis 2026",
  title="Automated small-scale devices and robotic systems for analyzing the cellular impact of ambient aerosol particles.",
  sub=corpus.SENS, design="Narrative review",
  pm="Ambient aerosol particles sampled onto cell-based assays", geo="Global / multi-region", endpoint="Cellular toxicity platforms (no primary endpoint)", tier="C",
  basis="Review / no primary exposure", affil="KIST Europe, Germany; Delft University of Technology, Netherlands",
  n=("Conceptual review of small, automated and robotic platforms that deliver ambient aerosol to cells for on-site cytotoxicity analysis, with emphasis on "
     "mobile and field-deployable systems, biomimetic device design, and the data acquisition and processing needed for a source-to-effect workflow. It reports "
     "no new measurements, no comparison of platforms against standard air-liquid-interface exposure, and no performance numbers in the abstract; "
     "search strategy and inclusion criteria are not described, so coverage cannot be judged. Relevance: indirect - toxicity-weighted sensing at the node "
     "is the logical step beyond mass concentration, and this is a map of the hardware candidates rather than evidence that any of them works in the field.")),
 dict(pmid="42999780", doi="10.1016/j.dib.2026.113370", journal="Data Brief",
  short="Toor SHoRT-CA smart home indoor air quality time series contextual anomalies dataset 2026",
  title="SHoRT-CA: Smart home data repository of time series with contextual anomalies.",
  sub=corpus.SENS, design="Network deployment / data descriptor",
  pm="Multivariate indoor air-quality time series from IoT smart-home sensors (channels not itemised in the abstract)",
  geo="Norway", endpoint="Labelled contextual anomalies for detection benchmarking", tier="C",
  basis="Low-cost sensor / network", affil="Norwegian University of Science and Technology, Norway; Norwegian University of Science and Technology, Norway",
  n=("Open repository of multivariate indoor air-quality time series from one IoT smart home, with human-activity and environmental-interaction records and "
     "contextual anomalies deliberately induced by experiments on the sensors, each documented and labelled for anomaly-detection benchmarking. The abstract "
     "does not list which pollutants or particle channels are measured, the sensor models, calibration, or record length, and a single dwelling with "
     "induced rather than naturally occurring faults limits how far detectors trained here transfer. Relevance: direct for quality control - labelled "
     "anomaly sets are scarce, and automated fault flagging is a standing need for unattended low-cost indoor networks, provided a PM channel is present.")),
]
