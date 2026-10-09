# -*- coding: utf-8 -*-
"""Abstract fetch for candidate indices (2026-10-06 run): PubMed efetch by PMID, else
EPMC by DOI, else Semantic Scholar. Usage: python3 _abs_1006.py <day> <idx csv>"""
import json, sys, urllib.request, urllib.parse, re, xml.etree.ElementTree as ET
D=sys.argv[1]; IDX=[int(x) for x in sys.argv[2].split(",")]
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read().decode()
    except Exception: return ""
f=json.load(open("cache/%s/_fresh.json"%D))
for i in IDX:
    r=f[i]
    if r.get("abstract"): print(i,"has"); continue
    ab=via=""
    if r.get("pmid"):
        x=get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="+r["pmid"])
        try:
            root=ET.fromstring(x)
            ab=" ".join("".join(a.itertext()) for a in root.iter("AbstractText"))
            if not r.get("doi"):
                for a in root.iter("ArticleId"):
                    if a.get("IdType")=="doi": r["doi"]=a.text.lower()
            via="pubmed" if ab else ""
        except Exception: pass
    if not ab and r.get("doi"):
        j=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:%22"+urllib.parse.quote(r["doi"])+"%22")
        try:
            res=json.loads(j)["resultList"]["result"]
            if res and res[0].get("abstractText"): ab=res[0]["abstractText"]; via="epmc"; r["pmid"]=r.get("pmid") or res[0].get("pmid","")
        except Exception: pass
    if not ab and r.get("doi"):
        try: ab=json.loads(get("https://api.semanticscholar.org/graph/v1/paper/DOI:"+r["doi"]+"?fields=abstract")).get("abstract") or ""; via="s2" if ab else ""
        except Exception: pass
    if ab: r["abstract"]=re.sub(r"<[^>]+>"," ",ab)[:3000]; r["abs_via"]=via
    print(i, r.get("doi"), via or "NONE", len(ab))
json.dump(f,open("cache/%s/_fresh.json"%D,"w"),indent=1)
