import json,collections,sys,re
def wk(days):
    P=[];E=[];per={}
    for d in days:
        c=json.load(open("state/corpus/%s.json"%d)); per[d]=len(c["PAPERS"])
        for p in c["PAPERS"]: p["_d"]=d; P.append(p)
        for e in c["EFFECTS"]: e["_d"]=d; E.append(e)
    sub=collections.Counter(p["sub"] for p in P)
    meas=sub["Exposure assessment & modelling"]+sub["Sensing, forecasting & instrumentation"]
    lcs=[p for p in P if p.get("basis")=="Low-cost sensor / network"]
    pers=[p for p in P if p.get("basis")=="Personal / wearable"]
    meta=[p for p in P if "etadata only" in (p.get("design","")+p.get("pm",""))]
    tier=collections.Counter(p.get("tier") for p in P)
    basis=collections.Counter(p.get("basis","(none)") for p in P)
    met=collections.Counter(e.get("metric") for e in E)
    inc=collections.Counter(e.get("inc","(none)") for e in E)
    ci=sum(1 for e in E if e.get("lo") is not None and e.get("hi") is not None)
    dois=len(set(p["doi"].lower() for p in P))
    print("N",len(P),"unique doi",dois,"per",per)
    print("sub",dict(sub)); print("meas",meas,round(100*meas/len(P)),"lcs",len(lcs),"personal",len(pers),"meta",len(meta),round(100*len(meta)/len(P)))
    print("tier",dict(tier)); print("basis",dict(basis)); print("E",len(E),"ci",ci,"metric",dict(met)); print("inc",dict(inc))
    return P,E
D=lambda a,b:["2026-11-%02d"%i for i in range(a,b+1)]
print("== W45"); wk(D(1,7)); print("== W46"); P,E=wk(D(8,14))
if len(sys.argv)>1:
    for p in P:
        if p.get("basis") in("Low-cost sensor / network","Personal / wearable") or p.get("tier")=="A": print(p["_d"][-2:],p.get("tier"),p.get("basis","")[:12],"|",p.get("short","")[:110])
    for e in E: print(e["_d"][-2:],e.get("metric"),e.get("est"),e.get("lo"),e.get("hi"),e.get("inc","-"),"|",e.get("src","")[:30],"|",e["label"].replace("\n"," ")[:45])
