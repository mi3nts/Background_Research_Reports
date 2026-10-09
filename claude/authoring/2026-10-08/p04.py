# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="42849691", doi="10.1016/j.envpol.2026.129305", journal="Environ Pollut",
  short="PM2.5 and GPP 2026",
  title="Climate-dependent nonlinear relationships between PM2.5 and ecosystem productivity across China's urban agglomerations",
  sub=corpus.EXPO, design="Machine-learning model",
  pm="Satellite PM2.5 against gross primary productivity across five urban agglomerations",
  geo="China (five urban agglomerations)", endpoint="None (ecosystem productivity)", tier="C",
  n=("Satellite observations and interpretable machine learning relate PM2.5 to gross primary "
     "productivity across climate and pollution gradients. The relationship is robust everywhere but "
     "changes sign by region: moderate aerosol loading goes with enhanced productivity in arid "
     "environments, while elevated PM2.5 generally suppresses it elsewhere, jointly shaped by climate and "
     "pollution regime. Limitation: the authors flag the central problem themselves - PM2.5, radiation, "
     "humidity and temperature co-vary, so a diffuse-radiation fertilisation effect cannot be separated "
     "from co-varying meteorology by feature attribution on observational data; both PM2.5 and GPP are "
     "satellite products with shared retrieval dependencies. Relevance: low for health, moderate as a "
     "reminder that aerosol has non-health consequences that enter policy arithmetic.")),

 dict(pmid="", doi="10.1016/j.atmosenv.2026.122410", journal="Atmos Environ",
  short="Izmir maritime 2026",
  title="Quantifying Maritime Contributions to Urban Air Quality in Izmir Bay Using Tier 3 Emission Inventory and AERMOD",
  sub=corpus.BURD, design=MO,
  pm="Metadata only - Tier 3 ship emission inventory with AERMOD dispersion (by title)",
  geo="Turkiye (Izmir Bay)", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 8 Oct with no abstract. By title, "
     "a bottom-up Tier 3 (movement-based) ship emission inventory coupled to AERMOD for a port city. Port "
     "and shipping contributions are among the hardest urban sources to attribute from a land-based "
     "network, because the source is offshore, mobile and upwind only part of the time - the same problem "
     "the Geoje Island AMS record (6 October) attacked by measurement rather than by model. "
     "Relevance: moderate-high; on the retry list.")),

 dict(pmid="", doi="10.1016/j.apr.2026.103227", journal="Atmos Pollut Res",
  short="Indo-Gangetic BC 2026",
  title="Long-term decline in Black Carbon Aerosol and Associated Health Risk over north-western Indo-Gangetic Plain",
  sub=corpus.BURD, design=MO,
  pm="Metadata only - long-term black carbon trend and associated health risk (by title)",
  geo="India (north-western Indo-Gangetic Plain)", endpoint=NA, tier="B",
  n=("Metadata-only record: title, authors and DOI deposited 8 Oct with no abstract. By title, a long-term "
     "decline in black carbon over the north-western Indo-Gangetic Plain with an attached health-risk "
     "estimate. A declining BC trend in one of the most polluted regions on earth is a strong claim that "
     "depends entirely on aethalometer calibration and filter-loading correction being stable across the "
     "record - the commonest source of spurious long-term trends in BC. The same day carries two "
     "independent BC burden records (China, 540,000 deaths; the 274-city outpatient series on 7 October), "
     "so the trend direction matters. Relevance: high; on the retry list.")),

 dict(pmid="", doi="10.1016/j.buildenv.2026.115381", journal="Build Environ",
  short="Neonatal air cleaners 2026",
  title="Portable air cleaners in neonatal facilities: Hybrid experimental-CFD assessment of different configurations",
  sub=corpus.OCC, design=MO,
  pm="Metadata only - portable air cleaner placement assessed by experiment plus CFD (by title)",
  geo="Not recoverable from metadata", endpoint=NA, tier="B",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 8 Oct with no abstract. By title, "
     "a combined experimental and CFD assessment of portable air cleaner configurations in neonatal "
     "facilities. Placement, not device rating, is what decides delivered clean-air rate in a real room, "
     "and the AFRI-c care-home null (4 October) is the clinical consequence of getting it wrong "
     "unmeasured. A neonatal unit is the setting where the dose argument is strongest. "
     "Relevance: high; on the retry list.")),
]
