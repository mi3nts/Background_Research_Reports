# -*- coding: utf-8 -*-
"""Append PubMed-connector PMIDs the harvester missed (EDAT 2026/09/23) to _fresh.json.
Connector queries: health axis (17 PMIDs), sensing axis (2), broad aerosol/air-quality axis (51).
Dedup against seen.json + corpus on PMID and DOI before appending."""
import json, glob
D = "2026-09-23"; C = f"cache/{D}"
KEEP = ["42778001","42775260","42775205","42775181","42774807","42774786","42778201","42778012","42778014"]
raw = {r.get("uid"): r for r in json.load(open(f"{C}/pubmed_connector_raw.json")) if r.get("uid")}
seen = json.load(open("state/seen.json"))
sp, sd = set(seen["pmid"]), set(k.lower() for k in seen["doi"])
fresh = json.load(open(f"{C}/_fresh.json"))
fd = {r["doi"] for r in fresh if r.get("doi")}; fp = {r["pmid"] for r in fresh if r.get("pmid")}
norm = []
for p in KEEP:
    r = raw[p]
    doi = next((a["value"] for a in r.get("articleids", []) if a["idtype"] == "doi"), "").lower()
    rec = dict(src="pubmed_connector", pmid=p, doi=doi, title=r.get("title", ""),
               journal=r.get("source", ""), authors="; ".join(a["name"] for a in r.get("authors", [])[:4]),
               pubdate=r.get("pubdate", ""), abstract="")
    norm.append(rec)
    if p in sp or doi in sd:
        print("SEEN", p, doi); continue
    if doi and doi in fd:
        # merge PMID onto the Crossref record already in _fresh
        for f in fresh:
            if f.get("doi") == doi:
                f["pmid"] = p; f["src"] += "+pubmed_connector"; print("MERGED", p, doi)
        continue
    if p in fp:
        continue
    fresh.append(rec); print("APPEND", len(fresh) - 1, p, doi, rec["title"][:80])
json.dump(norm, open(f"{C}/pubmed_connector.json", "w"), indent=1)
json.dump(fresh, open(f"{C}/_fresh.json", "w"), indent=1)
