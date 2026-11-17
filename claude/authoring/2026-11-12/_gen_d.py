# -*- coding: utf-8 -*-
# Records for 12 Nov issue, part D.
R = {
49: dict(short="Atmospheric Pollution Research local meteorology urban air quality complex topography metadata only",
  sub="EXPO", design="Metadata only - no abstract available", pm="Not stated (urban air quality; abstract unavailable)",
  geo="Not stated", endpoint="Not stated", tier="C",
  basis="Not stated", affil="",
  n=("Metadata only. Crossref deposit for Atmospheric Pollution Research with title, journal and DOI but no abstract or author affiliations; not "
     "retrievable from Europe PMC or Semantic Scholar at harvest. The title indicates an analysis of how local meteorology governs air quality in an "
     "urban area with complex topography; neither the pollutants, the site, the period nor the data source can be confirmed, and no finding is "
     "asserted here. Carried because terrain-driven stagnation and cold-air pooling are a recurring source of error when sparse reference monitors "
     "are interpolated and when low-cost sensors are sited in valleys. To be re-checked in the weekly Elsevier abstract sweep. "
     "Relevance: possible - siting and representativeness in complex terrain.")),
50: dict(short="Atmospheric Pollution Research Himawari-8 AOD hourly gap-filling wind field AOD gradient physical prior metadata only",
  sub="EXPO", design="Metadata only - no abstract available", pm="Himawari-8 aerosol optical depth (per title)",
  geo="Not stated", endpoint="Not stated", tier="C",
  basis="Satellite-fused", affil="",
  n=("Metadata only. Crossref deposit for Atmospheric Pollution Research with no abstract or affiliations at harvest. The title describes hourly "
     "gap-filling of geostationary Himawari-8 AOD using wind-field and AOD-gradient physical priors; the method, domain, validation data and skill "
     "cannot be confirmed and no finding is asserted. Carried because gap-filled hourly AOD is the usual satellite input to hourly PM2.5 fusion models "
     "that low-cost networks are blended with, and because the same issue carries a visibility-based all-hour AOD product for China, giving two "
     "routes to the same gap. To be re-checked in the weekly Elsevier abstract sweep. "
     "Relevance: possible - satellite input for hourly PM2.5 surfaces.")),
55: dict(short="CRAES Beijing-Tianjin-Hebei 2022 Winter Olympics Paralympics heavy PM2.5 episode 155 ug/m3 CAMx NOx mobile rebound nitrate",
  sub="BURD", design="Episode analysis (observations + CAMx)", pm="Observed and CAMx-simulated PM2.5 and nitrate; dynamic emission inventory",
  geo="China (Beijing-Tianjin-Hebei)", endpoint="Causes of a heavy-pollution episode; NOx reductions required", tier="B",
  basis="Model (CTM / LUR / ML)", affil="Chinese Research Academy of Environmental Sciences, China; Chinese Research Academy of Environmental Sciences, China",
  n=("Beijing kept daily PM2.5 at or below 75 ug/m3 through the 2022 Winter Olympics, but a heavy episode peaking at 155 ug/m3 (24-h) struck during the "
     "Paralympics. Field observations, dynamic emissions and CAMx show industrial controls held while mobile-source activity rebounded after the "
     "Chinese New Year, raising regional NOx emissions 13% and driving nitrate-dominated PM2.5; CO-normalised nitrate rose 3e-4 (Beijing) and 1e-5 "
     "(region) per tonne of NOx. Eliminating the heavy episode under that meteorology would need further NOx cuts of at least 1% in Beijing and 7% "
     "regionally. One episode and one meteorological situation; the sensitivities are model-derived. "
     "Relevance: indirect - nitrate-heavy, humid episodes are where optical sensors over-read most, and where mega-event evaluation leans on them.")),
60: dict(short="Capital Medical University mouse 5 and 35 ug/m3 PM2.5 180 days whole-body vascular calcification XBP1s osteogenic switching organoid",
  sub="MECH", design="Animal exposure study + in vitro", pm="Whole-body inhalation PM2.5 at 5 or 35 ug/m3 for 180 days",
  geo="China (laboratory)", endpoint="Arterial stiffness, vascular calcification, smooth-muscle osteogenic switching", tier="B",
  basis="Lab / research instrument", affil="Capital Medical University, China; Capital Medical University, China",
  n=("PM2.5 accelerated conversion of amorphous calcium phosphate to hydroxyapatite in simulated physiological solution, suggesting a heterogeneous "
     "nucleation role. Mice inhaled PM2.5 at 5 or 35 ug/m3 for 180 days: arterial stiffness, remodelling and calcification increased. In aortic "
     "smooth-muscle cells PM2.5 raised XBP1s and drove proliferative and osteogenic switching; Xbp1 deletion attenuated proliferation, migration, "
     "osteogenic transformation and mineralisation, and a human iPSC vessel-organoid plus macrophage co-culture amplified calcification. Concentrations "
     "are ambient-relevant, unusually for this literature, but group sizes, particle source and dose-response between 5 and 35 ug/m3 are not given "
     "in the abstract. "
     "Relevance: indirect - mechanism for PM-associated vascular calcification at WHO-guideline-to-standard levels; no measurement content.")),
64: dict(short="CAMS Fudan near-real-time seamless all-hour 5 km AOD China visibility forecast ML AERONET nighttime dust storm",
  sub="EXPO", design="Exposure model (ML, satellite-fused)", pm="Hourly 5 km aerosol optical depth from gridded visibility, forecast AOD and covariates",
  geo="China", endpoint="AOD reconstruction skill against geostationary, MODIS and AERONET", tier="B",
  basis="Satellite-fused", affil="Chinese Academy of Meteorological Sciences, China; Chinese Academy of Meteorological Sciences, China",
  n=("An automated ML framework fuses a new gridded visibility dataset with forecast AOD and spatiotemporal covariates to reconstruct hourly 5 km AOD over "
     "China in near-real time, filling cloud and night gaps. Cross-validated against geostationary training data R=0.95; independent validation gave "
     "R=0.61 against MODIS and 0.76 against nighttime AERONET. The record shows a midday minimum and early-morning maximum and a 2020-2022 decline, "
     "and tracked a record dust storm through cloud and darkness. The drop from 0.95 to 0.61 on independent data is the honest skill figure; "
     "visibility depends on humidity and composition, so AOD-to-PM2.5 conversion remains a separate step. "
     "Relevance: direct - all-hour AOD is the missing night input for hourly PM2.5 fusion with sensor networks.")),
74: dict(short="Southern California ACT ACF zero-emission truck regulations foregone emissions census tract telematics non-tailpipe PM2.5 92%",
  sub="BURD", design="Emissions scenario modelling", pm="Truck NOx and PM2.5 emissions (tailpipe and brake/tyre wear) at census-tract and 1 km",
  geo="United States (South Coast Air Basin)", endpoint="Projected emissions 2019-2045 by scenario; disadvantaged-community burden", tier="C",
  basis="Model (CTM / LUR / ML)", affil="",
  n=("Emission projections for Class 7-8 trucks in the South Coast Air Basin under no zero-emission-truck rules, ACT (sales) and ACT+ACF (sales plus "
     "fleet turnover), disaggregated with telematics to census tracts and 1 km grid. NOx falls from 80 to 12.9 tons/day by 2045 at baseline (84%) "
     "and to 2.7 tons/day under ACT+ACF (97%), 4.8-fold lower. Since 2022 non-tailpipe brake and tyre wear has dominated truck PM2.5 emissions and "
     "would make up 92% by 2045 under ACT+ACF. Foregone NOx benefits are 2.3-fold larger in disadvantaged communities. Emissions only: no "
     "concentration or health modelling, and wear-emission factors are uncertain. "
     "Relevance: direct - a shift to coarse-leaning non-exhaust PM is a shift in what roadside optical sensors under-count.")),
}
