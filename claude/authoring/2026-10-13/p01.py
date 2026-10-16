# -*- coding: utf-8 -*-
P = [
 dict(pmid="42869371", doi="10.1016/j.envpol.2026.129330", journal="Environ Pollut",
  short="Shanghai prenatal UFP postpartum depression 2026",
  title="Prenatal exposure to ultrafine particles and positive screening for postpartum depression: a prospective pregnancy cohort in Shanghai, China",
  sub=corpus.NEU, design="Prospective cohort", pm="Residential trimester-specific UFP number and PM2.5 (modelled)",
  geo="China (Shanghai)", endpoint="Postpartum depression screen (EPDS >= 10)", tier="A",
  n=("2,647 pregnant women, two centres; 20.4% screened positive at 6-10 weeks postpartum. Per IQR, first-trimester UFP "
     "OR 1.252 (1.065-1.471) and whole-pregnancy UFP OR 1.104 (1.047-1.164); both survived adjustment for PM2.5, which "
     "had no stable independent association. Stronger with male infants. Limitation: EPDS is a screen, not a diagnosis, "
     "and the UFP surface's spatial resolution and validation are not stated - UFP gradients decay over ~100-300 m from "
     "roads, so residential misclassification is likely large and non-differential only if traffic proximity is "
     "unrelated to deprivation, which in Shanghai it is not. Relevance: high - a second UFP-specific neuro signal this "
     "month that PM2.5 mass does not carry, and that optical nodes cannot measure.")),
 dict(pmid="42869373", doi="10.1016/j.envpol.2026.129343", journal="Environ Pollut",
  short="China fire-sourced PM2.5 cancer 2026",
  title="Extreme, Accumulated, and Lagged Exposure to Fire-Sourced PM2.5 and Site-specific Cancer Risk in China",
  sub=corpus.OTHR, design="Ecological / registry analysis", pm="Fire-sourced vs all-source PM2.5; lagged, accumulated and extreme metrics",
  geo="China (nationwide)", endpoint="Site-specific cancer incidence", tier="B",
  n=("Fire-sourced PM2.5 was positively associated with several site-specific cancers, with lagged and accumulated metrics "
     "showing the broadest pattern (thyroid, kidney, breast, lung, leukaemia, lymphoma) and extreme exposure the narrowest "
     "(strongest for larynx). Against all-source PM2.5, fire PM2.5 associations were stronger for thyroid, kidney, larynx, "
     "lymphoma and oral cancers, and stronger in the north and in low-GDP areas. Limitation: no effect sizes, n or "
     "geographic unit in the abstract; many sites x three metrics is a multiple-comparison surface, and thyroid cancer "
     "incidence is notoriously driven by screening intensity, which tracks region and income. Relevance: moderate - "
     "source-resolved smoke again outperforms mass.")),
 dict(pmid="42869372", doi="10.1016/j.envpol.2026.129340", journal="Environ Pollut",
  short="Taiwan transboundary PM10 forecast 2026",
  title="Forecasting transboundary PM10 pollution in northern Taiwan using upwind observations and transport timing",
  sub=corpus.SENS, design="Machine-learning model", pm="PM10 at 3 receptors; 9 continental upwind records; trajectory timing composite",
  geo="Taiwan (northern)", endpoint="No health endpoint", tier="B",
  n=("Upwind-transition-receptor framework with temporally separated training and evaluation for 1-4-day PM10 forecasts. "
     "Nested models attribute most added skill to distributed upwind observations; trajectory timing adds a smaller, "
     "receptor-dependent refinement. Best model (CatBoost with upwind data): RMSE 11.04 ug/m3, 13.0% below persistence. "
     "Limitation: 13% over persistence at 1-4 days is modest, and upper-tail precision is limited by event scarcity - "
     "the episodes that matter are the ones the model sees least. Relevance: high - quantitative evidence that upwind "
     "observation density, not trajectory sophistication, buys forecast skill; a siting argument for upwind nodes.")),
 dict(pmid="", doi="10.1016/j.envpol.2026.129339", journal="Environ Pollut",
  short="North Macedonia biomass PMF 2026",
  title="Biomass burning drives urban PM2.5 across the Western Balkans: evidence from a six-city source apportionment study in North Macedonia",
  sub=corpus.EXPO, design="Source apportionment", pm="PM2.5 from 1,195 daily filters, EPA PMF 5.0",
  geo="North Macedonia (six cities)", endpoint="No health endpoint", tier="B",
  n=("1,195 filters at six urban-background sites over two year-long campaigns. Campaign means 29.1-62.2 ug/m3 (1.2-2.5x "
     "the EU annual limit); residential wood combustion and open/waste burning resolved as distinct factors everywhere, "
     "together 21-35% of PM2.5, with heating-season RWC up to 33x non-heating. Biomass exceeded 50% of PM2.5 on 83% of "
     "Skopje episode days; an undocumented winter signal in Strumica fits greenhouse boilers. Limitation: PMF factor "
     "naming relies on tracer interpretation, and RWC/OBB separation without levoglucosan isotopes or 14C is "
     "assumption-laden. Relevance: high - a wood-smoke regime with bimodal evening peaks to 93 ug/m3, where optical "
     "sensor response to fresh smoke is the calibration problem.")),
]
