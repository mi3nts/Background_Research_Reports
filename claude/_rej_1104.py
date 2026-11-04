# -*- coding: utf-8 -*-
"""Log screened-out records for the 2 Nov issue (2026-11-04 00Z run). idx into _fresh.json; plus one Amass hit."""
import json, datetime
NOW = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
D = "2026-11-02"
ADMIT = {0,1,4,6,7,8,11,12,23,24,33,35,51,57,68,70}
WHY = {2:"urban topsoil metals; PM10 enters only as a resuspension term in hazard indices, no airborne measurement",
3:"hospital sustainability modelling; no PM-specific result",5:"coal-combustion condensable PM emission control, stack-level; no ambient or exposure",
9:"health-care waste energy recovery; off topic",10:"playground soil metals; NO2 association only, no PM measure",13:"container workplaces after earthquake; spirometry with no PM or air measurement",
14:"extracellular vesicles dermatology review; off topic",15:"Fenton catalysis; off topic",16:"stratospheric aerosol lidar retrieval; not surface PM",17:"microwave sounding spectroscopy; off topic",
18:"greenhouse gas network traceability; not PM",19:"cloud microphysics; not PM exposure",20:"metadata only, live-virus aerosol chamber for air purifiers; no PM or sensing content recoverable",
21:"ozone and oxidation capacity modelling; not PM",22:"N2O simulation; off topic",25:"fog optical retrieval from RGB images; not PM mass or exposure",26:"PCDD/F formation; not PM",27:"lithium extraction; off topic",
28:"carbon storage; off topic",29:"electrocatalyst interface; off topic",30:"humus formation; off topic",31:"passive sampling eyewear calibrated for gas-phase and semi-volatile organics, not PM; note wearable vs stationary sampling rates",
32:"fuel water footprint; off topic",34:"diaper oligomers dermal; off topic",36:"ecotoxicity prediction; off topic",37:"heatwave and stillbirth, metadata only; no PM exposure in title",38:"airport wastewater metagenomics; off topic",
39:"antibiotic resistance hybrid capture; off topic",40:"retraction notice, polyethylene-degrading enzymes; off topic",41:"soil nitrogen; off topic",42:"embodied emissions accounting; not PM exposure",43:"microplastics in benthos; off topic",
44:"cyanobacteria and pesticides; off topic",45:"marine litter in seabirds; off topic",46:"rhizosphere viruses; off topic",47:"PPCPs in reclaimed water; off topic",48:"odor mixture ML; off topic",
49:"Beijing vehicle emission inventory trend, metadata only; emissions rather than PM exposure",50:"LC-HRMS screening; no PM in title",52:"WRF PBL schemes for sea-land breeze; no PM",53:"lake pCO2 retrieval; off topic",
54:"fugitive VOC quantification; not PM",55:"NH3 satellite trend; gas phase, no PM result",56:"climate extremes projection; off topic",58:"nocturnal convection; off topic",59:"generative weather assimilation; no PM",
60:"intra-day temperature variability and mortality; no PM result",61:"mosquito-borne disease remote sensing; off topic",62:"urban weather files; off topic",63:"X-ray CT partial volume simulation; off topic",64:"GNSS spoofing; off topic",
65:"colorimetric analysis system; off topic",66:"shotcrete sensing; off topic",67:"fiber interferometry; off topic",69:"large vessel vasculitis scoping review; air pollution one candidate among many, no PM estimate",
71:"blue-green spatial pattern and carbon sequestration; off topic"}
EX = [dict(title="Assessment of inhalation toxicity hazard from particulate matter associated with sandstorms originating from Al-Dahna desert region", doi="10.1080/09603123.2026.2671300", journal="Int J Environ Health Res", reason="Amass: A549 in-vitro with no reported dose or effect size in the abstract")]
f = json.load(open("cache/%s/_fresh.json" % D)); n = 0
with open("state/rejected.jsonl", "a") as out:
    for i, r in enumerate(f):
        if i in ADMIT: continue
        out.write(json.dumps({"issue": D, "logged_utc": NOW, "idx": i, "title": r["title"], "doi": r.get("doi",""), "pmid": r.get("pmid",""), "src": r["src"], "journal": r.get("journal",""), "reason": WHY[i]}, ensure_ascii=False) + "\n"); n += 1
    for e in EX:
        out.write(json.dumps(dict(issue=D, logged_utc=NOW, idx=-1, pmid="", src="amass", **e), ensure_ascii=False) + "\n"); n += 1
print(D, "rejected", n)
