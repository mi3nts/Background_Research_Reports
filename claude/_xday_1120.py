# 17/18 Nov: drop rejected/seen; drop 18 Nov records already in 17 Nov (earliest day wins).
import json
rej_d=set();rej_p=set()
for l in open("state/rejected.jsonl"):
    try: j=json.loads(l)
    except: continue
    if j.get("doi"): rej_d.add(j["doi"].lower())
    if j.get("pmid"): rej_p.add(str(j["pmid"]))
seen=json.load(open("state/seen.json"))
sd=set(k.lower() for k in seen.get("doi",{})); sp=set(map(str,seen.get("pmid",{})))
taken=set()
def keys(r): return {"p:"+str(r.get("pmid") or ""),"d:"+(r.get("doi") or "").lower(),"t:"+r.get("nt","")[:60]}-{"p:","d:","t:"}
for r in json.load(open("cache/2026-11-16/_fresh.json")): taken|=keys(r)
for d in ["2026-11-17","2026-11-18"]:
    f=json.load(open("cache/%s/_fresh.json"%d)); out=[];rj=dp=0
    for r in f:
        if (r.get("doi") or "").lower() in rej_d|sd or str(r.get("pmid") or "") in rej_p|sp: rj+=1; continue
        if keys(r)&taken: dp+=1; continue
        taken|=keys(r); out.append(r)
    json.dump(out,open("cache/%s/_fresh.json"%d,"w"),indent=1)
    print(d,"in",len(f),"rej/seen",rj,"earlier-day dup",dp,"->",len(out),"no-abstract",sum(1 for r in out if not r.get("abstract")))
