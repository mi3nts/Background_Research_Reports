# -*- coding: utf-8 -*-
"""Merge connector records for <day> into cache/<day>/_fresh.json (dedup pmid/doi/title vs
fresh, seen.json and the corpus). DOI-only Crossref/EPMC records get the PMID merged on."""
import json, sys, glob, re, html
D = sys.argv[1]; C = "cache/%s" % D
def nt(t):
    t = re.sub(r"<[^>]+>", " ", html.unescape(t or "")).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t)).strip()
raw = json.load(open(C + "/pubmed_connector_raw.json"))
seen = json.load(open("state/seen.json"))
sp, sd = set(seen["pmid"]), set(k.lower() for k in seen["doi"])
ct = set()
for f in glob.glob("state/corpus/*.json"):
    for p in json.load(open(f))["PAPERS"]:
        ct.add(nt(p["title"])); sp.add(str(p.get("pmid", ""))); sd.add((p.get("doi") or "").lower())
fresh = json.load(open(C + "/_fresh.json"))
a = m = s = 0
for r in raw:
    p = r["uid"]
    doi = next((x["value"] for x in r.get("articleids", []) if x["idtype"] == "doi"), "").lower()
    t = r.get("title", "")
    if p in sp or (doi and doi in sd) or nt(t) in ct:
        s += 1; continue
    hit = next((f for f in fresh if f.get("pmid") == p or (doi and f.get("doi") == doi) or nt(f["title"]) == nt(t)), None)
    if hit:
        if not hit.get("pmid"):
            hit["pmid"] = p; hit["src"] += "+pubmed_connector"; m += 1
        continue
    fresh.append(dict(src="pubmed_connector", pmid=p, doi=doi, title=html.unescape(t), nt=nt(t),
                      journal=r.get("source", ""), authors="; ".join(x["name"] for x in r.get("authors", [])[:4]),
                      pubdate=r.get("pubdate", ""), abstract=""))
    a += 1
json.dump(fresh, open(C + "/_fresh.json", "w"), indent=1)
print(D, "connector raw", len(raw), "| seen", s, "| merged pmid", m, "| appended", a, "| fresh now", len(fresh))
