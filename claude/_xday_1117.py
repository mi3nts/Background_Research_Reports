# 16 Nov: drop records already assigned to 12-15 Nov (unshipped, not yet in seen.json), rejected or seen. Also pull the 2 connector PMIDs bucketed to 15 Nov if unassigned.
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
for d in ["2026-11-12","2026-11-13","2026-11-14","2026-11-15"]:
    for r in json.load(open("cache/%s/_fresh.json"%d)): taken|=keys(r)
    try:
        for r in json.load(open("state/corpus/%s.json"%d)).get("papers",[]): taken|=keys(r)
    except Exception as e: print("corpus",d,e)
f=json.load(open("cache/2026-11-16/_fresh.json")); out=[];rj=dp=0
for r in f:
    if (r.get("doi") or "").lower() in rej_d|sd or str(r.get("pmid") or "") in rej_p|sp: rj+=1; continue
    if keys(r)&taken: dp+=1; continue
    taken|=keys(r); out.append(r)
json.dump(out,open("cache/2026-11-16/_fresh.json","w"),indent=1)
print("16 Nov in",len(f),"rej/seen",rj,"earlier-day dup",dp,"->",len(out),"no-abstract",sum(1 for r in out if not r.get("abstract")))
c15=[r for r in json.load(open("cache/2026-11-15/pubmed_connector_raw.json"))]
print("15-Nov-bucketed connector:",[(r["uid"], ("p:"+r["uid"]) in taken or r["uid"] in rej_p|sp, r["title"][:70]) for r in c15 if r["uid"] in "43039175,43038691,43038568,43038319,43038083,43037792,43036674,43036418,43036397,43036120,43035936,43035818,43035740"])
