# -*- coding: utf-8 -*-
"""September 2026 monthly: pooled statistics over state/corpus (no API calls)."""
import json, glob, collections, re, sys
sys.argv=['x']; import os
os.environ.setdefault("PMRW_DATE","2026-09-30")
import plots as PL
def load(m):
    P=[];E=[];days=[]
    for f in sorted(glob.glob("state/corpus/%s-*.json"%m)):
        j=json.load(open(f)); days.append((j["date"],len(j["PAPERS"]),len(j["EFFECTS"])))
        for p in j["PAPERS"]: p["_d"]=j["date"]; P.append(p)
        for e in j["EFFECTS"]: e["_d"]=j["date"]; E.append(e)
    return P,E,days
S,SE,sd=load("2026-09"); A,AE,ad=load("2026-08")
print("SEP issues",len(sd),"records",len(S),"effects",len(SE),"| AUG",len(ad),len(A),len(AE))
print("days",[(d[8:],n) for d,n,_ in sd])
dois=[p["doi"].lower() for p in S if p.get("doi")]; print("unique dois",len(set(dois)),"dupes",[d for d,c in collections.Counter(dois).items() if c>1])
c=lambda L,k: collections.Counter(p[k] for p in L)
ss=c(S,"sub"); sa=c(A,"sub")
for k in ss|sa: print("  %-40s SEP %3d (%2.0f%%)  AUG %3d"%(k,ss[k],100*ss[k]/len(S),sa[k]))
print("tier",c(S,"tier"))
meta=[p for p in S if p["design"].startswith("Metadata only")]; print("metadata-only",len(meta), "%.0f%%"%(100*len(meta)/len(S)))
print("designs",collections.Counter(PL.design_group.get(p["design"],"Other") for p in S).most_common())
print("geo",collections.Counter(PL.geo_of(p["geo"]) for p in S).most_common())
print("pm",collections.Counter(PL.pm_group(p["pm"]) if hasattr(PL,"pm_group") else "" for p in S).most_common(12))
print("journals",collections.Counter(p["journal"] for p in S).most_common(15))
src=collections.Counter(e.get("src") for e in SE); print("effect sources",len(set((e["_d"],e.get("src")) for e in SE)))
harm=sum(1 for e in SE if e["lo"]>1); prot=sum(1 for e in SE if e["hi"]<1); print("harm",harm,"prot",prot,"cross",len(SE)-harm-prot)
print("metrics", collections.Counter(e["metric"] for e in SE))
for kw in ["ultrafine","particle number","black carbon","aethalometer","CPC","drift","ageing","aging"]:
    hits=[p["short"]+"@"+p["_d"][5:] for p in S if re.search(kw,p["n"]+p["title"]+p["pm"],re.I)]
    print(kw,len(hits),hits[:12])
