# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="42854810", doi="10.1016/j.envres.2026.125888", journal="Environ Res",
  short="Zhang WWTP bioaerosol 2026",
  title="Comprehensive Characterization of Bioaerosol Microbial Communities, ARG, and Occupational Exposure Risks in WWTP and Comprehensive Landfill",
  sub=corpus.OCC, design="Field measurement",
  pm="Culturable bioaerosol (CFU/m3), fine biogenic particle fraction, airborne ARG/MGE copies",
  geo="China (central)", endpoint="Estimated inhalation dose / QMRA risk", tier="C",
  n=("Paired sampling at a wastewater plant and an integrated solid-waste facility with 16S sequencing, "
     "HT-qPCR, QMRA and ML. Culturable bacteria were 3.4-fold higher at the landfill (1,726 vs 502 "
     "CFU/m3) and so was the fine biogenic particle share (27% vs 15%), but airborne ARG/MGE copies were "
     "an order of magnitude higher at the WWTP (5,462 vs 584 copies/m3), giving it the larger estimated "
     "worker inhalation dose. Limitation: two facilities, short campaigns, and culturable counts "
     "undercount viable-but-nonculturable cells; ARG copies per m3 do not establish viable resistant "
     "organisms. Relevance: low-moderate - optical sensors see biogenic particles as generic mass; the "
     "case for fluorescence-capable occupational monitors.")),

 dict(pmid="", doi="10.5194/acp-26-14229-2026", journal="Atmos Chem Phys",
  short="Wu NCP brown carbon 2026",
  title="Light absorption properties and composition of water-soluble brown carbon in North China Plain: implication for an enhancing role of nitrogenous organic compounds",
  sub=corpus.EXPO, design="Field measurement",
  pm="Water-soluble BrC absorption (Abs365, MAE) and composition at five sites, winter 2023",
  geo="China (North China Plain, five sites)", endpoint="None (optical properties)", tier="C",
  n=("Simultaneous winter sampling at Beijing, Tianjin, Luancheng (rural), Handan and Jinan. Abs365 at "
     "the rural site was 1.1-3.5 times the urban values, but mass absorption efficiency peaked in Jinan "
     "(1.40 m2/g). Urban Abs365 fell ~45% from 2018 to 2023. BrC absorptivity rose from clean to haze "
     "with the N:C ratio, pointing to nitrogenous organics as chromophores. Limitation: water-soluble "
     "extracts miss the methanol-soluble, more absorbing BrC, and one winter cannot separate trend from "
     "meteorology. Relevance: moderate - the same nitrogenous organics the same-day Sci Adv record ranks "
     "most toxic are the ones that absorb at 365 nm, which a multi-wavelength absorption node can see.")),

 dict(pmid="", doi="10.21203/rs.3.rs-11058151/v1", journal="Research Square (preprint)",
  short="Ghajari fuzzy DL Tehran 2026",
  title="A Novel Fuzzy Hybrid Deep Learning Architecture for Spatiotemporal PM2.5 Prediction",
  sub=corpus.SENS, design="Machine-learning model",
  pm="Station PM2.5 with meteorological, satellite, topographic, population and road inputs, 2014-2016",
  geo="Iran (Tehran)", endpoint="None (one-day-ahead forecast)", tier="C",
  n=("A fuzzy transformer-CNN-GRU with cross-branch attention for one-day-ahead PM2.5 in Tehran, trained on "
     "2014-2015 and tested on 2016, outperforming seven comparator models with a reported RMSE of 0.73 "
     "ug/m3. Limitation: an RMSE below 1 ug/m3 for next-day PM2.5 in Tehran is implausible for a genuine "
     "forecast and suggests leakage (e.g. same-day inputs or normalised units); no persistence baseline is "
     "reported, and the data end in 2016. Relevance: low - the same-day Navi Mumbai record shows why "
     "persistence must be the reference; this one does not test against it.")),

 dict(pmid="", doi="10.48550/arXiv.2610.13882", journal="arXiv (preprint)",
  short="Pires quantum NN 2026",
  title="An Annealing-based Quantum Neural Network with Discrete Wavelet Transforms for Enhanced Air Pollution Nowcasting",
  sub=corpus.SENS, design="Machine-learning model",
  pm="Urban PM2.5 time series (UK, high-density data)",
  geo="United Kingdom", endpoint="None (nowcast skill)", tier="C",
  n=("Hybrid variational quantum circuits with quantum annealing, scaled to 172 qubits on a neuromorphic "
     "platform, nowcast PM2.5 from UK urban data and are reported to outperform MLP and LSTM on raw "
     "high-entropy inputs, more so with wavelet decomposition. Limitation: the abstract gives no error "
     "metric, horizon or persistence baseline, and beating an MLP/LSTM on unpreprocessed data is a weak "
     "comparator; 'quantum utility' claims need a classical model tuned on the same wavelet features. "
     "Relevance: low - nowcasting at node level is a solved problem for persistence-plus-meteorology.")),
]
