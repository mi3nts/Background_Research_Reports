# Cross-day candidate set for backfill 6-9 Nov: assign each record to its earliest day, drop rejected DOIs/PMIDs.
import json
days=["2026-11-06","2026-11-07","2026-11-08","2026-11-09"]
rej_d=set();rej_p=set()
for l in open("state/rejected.jsonl"):
    try: j=json.loads(l)
    except: continue
    if j.get("doi"): rej_d.add(j["doi"].lower())
    if j.get("pmid"): rej_p.add(str(j["pmid"]))
seen=json.load(open("state/seen.json"))
sd=set(k.lower() for k in seen.get("doi",{})); sp=set(seen.get("pmid",{}))
taken=set()
for d in days:
    f=json.load(open("cache/%s/_fresh.json"%d)); out=[]; drop=0; rj=0
    for r in f:
        keys={"p:"+str(r.get("pmid") or ""),"d:"+(r.get("doi") or "").lower(),"t:"+r.get("nt","")[:60]}-{"p:","d:","t:"}
        if (r.get("doi") or "").lower() in rej_d|sd or str(r.get("pmid") or "") in rej_p|sp: rj+=1; continue
        if keys & taken: drop+=1; continue
        taken|=keys; out.append(r)
    json.dump(out,open("cache/%s/_fresh.json"%d,"w"),indent=1)
    print(d,"in",len(f),"prior-rejected/seen",rj,"later-day dup",drop,"->",len(out),"no-abstract",sum(1 for r in out if not r.get("abstract")))
