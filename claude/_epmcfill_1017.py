# -*- coding: utf-8 -*-
"""Fill DOI/PMID/abstract for EPMC records lacking DOI via EPMC core lookup by source/id.
Usage: python3 _epmcfill_1017.py <day> <idx csv>"""
import json, sys, urllib.request, urllib.parse, re
D=sys.argv[1]; IDX=[int(x) for x in sys.argv[2].split(",")]
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
f=json.load(open("cache/%s/_fresh.json"%D)); raw=json.load(open("cache/%s/europepmc.json"%D))
def nt(t): return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9 ]"," ",re.sub(r"<[^>]+>"," ",t or "").lower())).strip()
byt={nt(r["title"]):r for r in raw}
for i in IDX:
    r=f[i]; e=byt.get(nt(r["title"]))
    if not e: print(i,"no raw"); continue
    q="EXT_ID:%s AND SRC:%s"%(e["id"],e["source"])
    u="https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query="+urllib.parse.quote(q)
    try: res=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read())["resultList"]["result"]
    except Exception as x: print(i,"ERR",x); continue
    if not res: print(i,"empty"); continue
    c=res[0]
    r["doi"]=(c.get("doi") or r.get("doi") or "").lower(); r["pmid"]=c.get("pmid") or r.get("pmid","")
    if c.get("abstractText"): r["abstract"]=re.sub(r"<[^>]+>"," ",c["abstractText"])[:3000]; r["abs_via"]="epmc"
    print(i, r["doi"], r["pmid"], len(r.get("abstract") or ""))
json.dump(f,open("cache/%s/_fresh.json"%D,"w"),indent=1)
