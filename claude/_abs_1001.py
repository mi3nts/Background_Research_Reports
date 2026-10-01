# -*- coding: utf-8 -*-
"""Abstract retry for admitted DOI-only records: PubMed [aid] -> EPMC -> Semantic Scholar."""
import json, sys, urllib.request, urllib.parse, re
D=sys.argv[1]; IDX=[int(x) for x in sys.argv[2].split(",")]
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode()
    except Exception as e: return ""
f=json.load(open("cache/%s/_fresh.json"%D))
for i in IDX:
    r=f[i]
    if r.get("abstract"): continue
    doi=r["doi"]; ab=""; via=""
    j=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:%22"+urllib.parse.quote(doi)+"%22")
    try:
        res=json.loads(j)["resultList"]["result"]
        if res and res[0].get("abstractText"): ab=res[0]["abstractText"]; via="epmc"; r["pmid"]=r.get("pmid") or res[0].get("pmid","")
    except Exception: pass
    if not ab:
        j=get("https://api.semanticscholar.org/graph/v1/paper/DOI:"+doi+"?fields=abstract")
        try:
            ab=json.loads(j).get("abstract") or ""; via="s2" if ab else ""
        except Exception: pass
    if ab: r["abstract"]=re.sub(r"<[^>]+>"," ",ab)[:2500]; r["abs_via"]=via
    print(i, doi, via or "NONE", len(ab))
json.dump(f,open("cache/%s/_fresh.json"%D,"w"),indent=1)
