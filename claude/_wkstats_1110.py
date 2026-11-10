import json,glob,collections,sys
def load(a,b):
    P=[];E=[];days={}
    for f in sorted(glob.glob("state/corpus/*.json")):
        d=f.split("/")[-1][:10]
        if a<=d<=b:
            j=json.load(open(f)); P+=j["PAPERS"]; E+=j["EFFECTS"]; days[d]=len(j["PAPERS"])
    return P,E,days
a,b,pa,pb=sys.argv[1:5]
P,E,days=load(a,b); Q,F,pd=load(pa,pb)
C=collections.Counter
print("days",days,"total",len(P),"uniqdoi",len({p['doi'].lower() for p in P}))
print("prev days",pd,"total",len(Q))
sp=C(p["sub"] for p in P); sq=C(p["sub"] for p in Q)
for k in sorted(set(sp)|set(sq)): print("  %-40s %3d -> %3d"%(k,sq[k],sp[k]))
meas=lambda X:sum(1 for p in X if p["sub"] in("Exposure assessment & modelling","Sensing, forecasting & instrumentation"))
print("measurement side",meas(Q),"->",meas(P))
print("tier",C(p.get("tier") for p in P),"prev",C(p.get("tier") for p in Q))
md=lambda X:sum(1 for p in X if p["design"].lower().startswith("metadata"))
print("metadata-only",md(P),"prev",md(Q))
print("effects",len(E),"withCI",sum(1 for e in E if e.get("lo") is not None),"metrics",C(e["metric"] for e in E),"inc",C(e.get("inc","none") for e in E))
print("prev effects",len(F),C(e["metric"] for e in F))
print("basis",C(p.get("basis","-") for p in P))
print("lcs records",[p["short"][:60] for p in P if p.get("basis")=="Low-cost sensor / network"])
print("journals",C(p["journal"] for p in P).most_common(10))
print("geo",C(p["geo"] for p in P).most_common(12))
inst=C()
for p in P:
    for x in (p.get("affil") or "").split(";"):
        x=x.strip().rsplit(",",1)[0]
        if x: inst[x]+=1
print("inst",[(k,v) for k,v in inst.most_common(12) if v>1])
print("TIER A:"); 
for p in P:
    if p.get("tier")=="A": print("  ",p["short"][:95])
