# -*- coding: utf-8 -*-
"""Crossref title lookup for records lacking DOI/abstract; then S2 abstract by DOI.
Usage: python3 _xrfill_1017.py <day> <idx csv>"""
import json, sys, urllib.request, urllib.parse, re
D=sys.argv[1]; IDX=[int(x) for x in sys.argv[2].split(",")]
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
def get(u):
    try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read())
    except Exception: return {}
def nt(t): return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]"," ",re.sub(r"<[^>]+>"," ",t or "").lower())).strip()
f=json.load(open("cache/%s/_fresh.json"%D))
for i in IDX:
    r=f[i]
    if not r.get("doi"):
        j=get("https://api.crossref.org/works?rows=3&query.bibliographic="+urllib.parse.quote(r["title"]))
        for it in j.get("message",{}).get("items",[]):
            if nt((it.get("title") or [""])[0])==nt(r["title"]):
                r["doi"]=it["DOI"].lower()
                if it.get("abstract") and not r.get("abstract"): r["abstract"]=re.sub(r"<[^>]+>"," ",it["abstract"])[:3000]; r["abs_via"]="crossref"
                break
    if r.get("doi") and not r.get("abstract"):
        j=get("https://api.crossref.org/works/"+urllib.parse.quote(r["doi"]))
        a=j.get("message",{}).get("abstract")
        if a: r["abstract"]=re.sub(r"<[^>]+>"," ",a)[:3000]; r["abs_via"]="crossref"
    if r.get("doi") and not r.get("abstract"):
        a=get("https://api.semanticscholar.org/graph/v1/paper/DOI:"+r["doi"]+"?fields=abstract").get("abstract")
        if a: r["abstract"]=a[:3000]; r["abs_via"]="s2"
    print(i, r.get("doi"), len(r.get("abstract") or ""))
json.dump(f,open("cache/%s/_fresh.json"%D,"w"),indent=1)
