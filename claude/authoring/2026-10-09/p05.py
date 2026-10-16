# -*- coding: utf-8 -*-
MO = "Metadata only (no abstract)"; NA = "None (abstract not deposited)"
P = [
 dict(pmid="", doi="10.1016/j.buildenv.2026.115378", journal="Build Environ",
  short="Mahmoud filtration risk 2026",
  title="The link between aerosol dispersion, infection risk and air filtration",
  sub=corpus.OCC, design=MO,
  pm="Metadata only - indoor aerosol dispersion against filtration and modelled infection risk (by title)",
  geo="Not stated (indoor)", endpoint=NA, tier="C",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 9 Oct with no abstract. By title, "
     "a link between indoor aerosol dispersion, filtration and infection risk - the Wells-Riley family of "
     "models, whose weak point is that a well-mixed room assumption and a measured clean-air delivery rate "
     "rarely both hold. Relevance: moderate - filtration intervention studies in this corpus (the 4 Oct "
     "AFRI-c HEPA null among them) keep failing on exposure verification, which is a monitoring problem "
     "before it is a filtration problem. On the abstract-retry list.")),

 dict(pmid="", doi="10.1016/j.buildenv.2026.115373", journal="Build Environ",
  short="Chen dormitory Stokes 2026",
  title="Size-resolved aerosol transport and exposure risk in university dormitories driven by Stokes number topology and source-flow coupling",
  sub=corpus.OCC, design=MO,
  pm="Metadata only - size-resolved indoor aerosol transport and exposure, Stokes-number framing (by title)",
  geo="Not stated (university dormitories)", endpoint=NA, tier="C",
  n=("Metadata-only record: Elsevier deposited title, authors and DOI on 9 Oct with no abstract. By title, "
     "size-resolved aerosol transport and exposure risk in dormitories organised around Stokes number and "
     "source-flow coupling - i.e. the regime where inertia, not the mean flow, decides where particles "
     "land, which is why a single room-average concentration misrepresents exposure for coarse particles. "
     "Relevance: moderate - the argument for size-resolved rather than PM2.5-mass indoor nodes. On the "
     "abstract-retry list.")),

 dict(pmid="", doi="10.1016/j.indenv.2026.100199", journal="Indoor Environments",
  short="Carnec adjoint nodal IAQ 2026",
  title="Adjoint-based corrective approach for nodal indoor air quality predictions",
  sub=corpus.EXPO, design=MO,
  pm="Metadata only - adjoint correction of nodal (multi-zone) indoor air quality models (by title)",
  geo="Not stated (building model)", endpoint=NA, tier="B",
  n=("Metadata-only record: title, authors and DOI deposited 9 Oct with no abstract. By title, an "
     "adjoint-based correction for nodal indoor air quality models, which treat each room as one "
     "well-mixed node and are fast but systematically wrong where a room is not well mixed. An adjoint "
     "formulation gives sensitivity of predicted concentrations to each input at the cost of one extra "
     "solve, which is what makes correction from sparse sensor data tractable. Relevance: high - this is "
     "the data-assimilation route by which a handful of indoor nodes can correct a whole-building model, "
     "the indoor analogue of the conformal-coverage question raised on 8 October. On the abstract-retry "
     "list.")),
]
