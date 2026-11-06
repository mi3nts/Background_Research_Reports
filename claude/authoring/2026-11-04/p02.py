# -*- coding: utf-8 -*-
P = [
 dict(pmid="42209715", doi="10.1038/s41370-026-00883-6", journal="J Expo Sci Environ Epidemiol",
  short="Molina Rueda AirPen facility-wide personal PM noise formaldehyde one shift 2026",
  title="Facility-wide assessment of occupational exposure to dust, noise, and formaldehyde",
  sub=corpus.OCC, design="Field measurement",
  pm="Total particulate by personal AirPen sampler with on-board sensors, plus formaldehyde and A-weighted noise",
  geo="North America", endpoint="Exposure distribution parameters (mean, geometric mean, 95th percentile) and their uncertainty", tier="A",
  basis="Personal / wearable", affil="Colorado State University, USA; Colorado State University, USA",
  n=("Five people deployed 83 AirPen compact personal monitors across one full shift at a furniture plant of about 100 workers. Valid after screening: 67 PM, "
     "67 noise, 22 formaldehyde (72, 67, 31 counting samples below the LOD). On-board sensors identified anomalies and confirmed wear. Distribution parameters "
     "were estimated with high certainty, and confidence intervals grew several-fold when fewer samples were analysed. Limitation: one facility on one shift says "
     "nothing about day-to-day variance, usually the main occupational term; 16 of 83 PM samples were lost or below LOD, and no comparison values are in the "
     "abstract. Relevance: direct - sample count, not instrument class, sets the uncertainty. \\textsc{backfill}, entry 28 May 2026.")),
 dict(pmid="", doi="10.3390/s26010280", journal="Sensors",
  short="Kloppenborg ARMIE SPS30 node laboratory DustTrak SMPS APS source-out calibration 2026",
  title="Laboratory Evaluation of ARMIE, a Portable SPS30-Based Low-Cost Sensor Node for PM2.5 Monitoring",
  sub=corpus.SENS, design="Instrument evaluation",
  pm="PM2.5 from Sensirion SPS30 in a portable node, against DustTrak and combined SMPS+APS",
  geo="Europe", endpoint="Agreement, calibration error and limits of agreement by leave-one-sensor-out and leave-one-source-out", tier="B",
  basis="Low-cost sensor / network", affil="Aarhus University, Denmark; Aarhus University, Denmark",
  n=("SPS30 nodes were co-located in the laboratory with a DustTrak and an SMPS+APS across candle, cooking, cigarette smoke and clean air, at regular and high "
     "humidity. Agreement with the DustTrak was r 0.93-0.98; with SMPS+APS it was moderate, r 0.74-0.94, with systematic underestimation at high concentration. "
     "Leave-one-sensor-out and leave-one-source-out calibration reduced mean error and narrowed limits of agreement. Limitation: a DustTrak is itself a "
     "photometer, so the high r partly reflects shared optical bias; the sizing reference is the honest comparator and shows the gap. No gravimetric or field arm, "
     "and r is not accuracy. Relevance: direct - leave-one-source-out is the right test for epidemiology nodes. \\textsc{backfill}, Crossref 2 January 2026.")),
 dict(pmid="", doi="10.1007/s44291-026-00286-9", journal="Discover Electronics",
  short="Goyal PurpleAir PA-II kappa-Kohler Lorentz-Lorenz random forest moisture artefact 2026",
  title="A physics-aware digital twin for correcting moisture-induced material artifacts in PM2.5 sensors",
  sub=corpus.SENS, design="Calibration model comparison",
  pm="PM2.5 from a pair of PurpleAir PA-II units co-located with an EPA FEM monitor (site 220330009)",
  geo="North America", endpoint="Normalized mean bias and R2 after humidity correction", tier="C",
  basis="Low-cost sensor / network", affil="",
  n=("A pair of PA-II units beside one EPA FEM monitor for 150 days in an industrial area. kappa-Kohler growth and a Lorentz-Lorenz refractive index mixing rule "
     "motivate features for a polynomial-enhanced random forest. At RH 76.16% optical intensity rose 59.5%, summarised as a mass-intensity divergence factor of "
     "4.33. Raw bias of +17.55% fell to 0.13% NMB, R2 0.9010. Limitation: two sensors at one site, single author, and the abstract gives no train/test separation "
     "by time, sensor or site, so 0.13% cannot be read as field skill. Calling FEM 'gravimetric' is loose. Relevance: moderate - the physics is standard and "
     "testable; the transferability is untested. \\textsc{backfill}, Crossref 26 September 2026.")),
 dict(pmid="", doi="10.1016/j.jaerosci.2026.106908", journal="J Aerosol Sci",
  short="Mao wavelet attention LSTM indoor aerosol concentration prediction 2026",
  title="A Wavelet-Based Attention LSTM Framework for Aerosol Concentration Prediction in Indoor Environments",
  sub=corpus.SENS, design="Metadata only: no abstract in Crossref at issue time",
  pm="Indoor aerosol concentration", geo="Not stated", endpoint="Not recoverable", tier="C", basis="Not stated", affil="",
  n=("Metadata only; no abstract in Crossref at issue time, so no finding is asserted. The title describes a wavelet decomposition feeding an attention LSTM to "
     "predict indoor aerosol concentration. Carried because short-horizon indoor prediction is one of the candidate edge-inference tasks for a sensor node, and "
     "J Aerosol Sci is one of the venues where such work is tied to a measured aerosol. What decides its value is unknown until the abstract deposits: the "
     "measuring instrument, whether validation is by held-out episode rather than random split, and the prediction horizon. Relevance: possible, unassessed.")),
]
