# W47 (15-21 Nov) vs W46 stats, 2026-11-22 run. Reuses plots_extra basis()/incr() source.
import json,collections,sys,re,math
import corpus
src=open("plots_extra.py").read()
g={"re":re,"corpus":corpus,"collections":collections}
seg=src[src.index("RULES = ["):src.index("if PAPERS:")]
seg=seg.replace("BCOL = {","BCOL0 = {")
exec("AMBER=CLAY=VIOLET=TEAL=CORAL=MUSK=SKY=SAGE=SLATE=DEEP=INK=GRID=PAPER=MUTED=GOLD=RUST='x'\n"+seg,g)
g["BCOL"]=g["BCOL0"]
i0=src.index("RATIO = {"); i1=src.index("R = [e for e in EFFECTS")
exec("AMBER=CLAY=VIOLET=TEAL=CORAL=MUSK='x'\n"+src[i0:i1],g)
basis,kind,incr,RATIO=g["basis"],g["kind"],g["incr"],g["RATIO"]
MEAS={corpus.SENS,corpus.EXPO}
def egger(R):
    x=[math.log(e["est"]) for e in R]; se=[max((math.log(e["hi"])-math.log(e["lo"]))/3.92,1e-4) for e in R]
    z=[a/b for a,b in zip(x,se)]; pr=[1/b for b in se]; n=len(z)
    mx=sum(pr)/n; mz=sum(z)/n; sxx=sum((p-mx)**2 for p in pr); b=sum((p-mx)*(q-mz) for p,q in zip(pr,z))/sxx; a=mz-b*mx
    res=[q-a-b*p for p,q in zip(pr,z)]; s2=sum(r*r for r in res)/(n-2); sea=math.sqrt(s2*(1/n+mx*mx/sxx)); return a,sea,n
def wk(days,show=False):
    P=[];E=[];per={}
    for d in days:
        c=json.load(open("state/corpus/%s.json"%d)); per[d[-2:]]=len(c["PAPERS"])
        for p in c["PAPERS"]: p["_d"]=d; P.append(p)
        for e in c["EFFECTS"]: e["_d"]=d; E.append(e)
    sub=collections.Counter(p["sub"] for p in P)
    meas=sum(sub[s] for s in MEAS)
    B=[(p,basis(p)) for p in P]
    lcs=[p for p,b in B if b=="Low-cost sensor / network"]; pers=[p for p,b in B if b=="Personal / wearable"]
    meta=[p for p in P if "etadata only" in (p.get("design","")+p.get("pm",""))]
    tier=collections.Counter(p.get("tier") for p in P)
    hk=collections.Counter(kind(b) for p,b in B if p["sub"] not in MEAS)
    hn=sum(hk[k] for k in("measured","modelled","proxy"))
    met=collections.Counter(e.get("metric") for e in E)
    ci=sum(1 for e in E if e.get("lo") is not None and e.get("hi") is not None)
    R=[e for e in E if e.get("metric") in RATIO and e.get("lo") and e.get("hi") and e["lo"]>0 and e["hi"]>e["lo"] and e["est"]>0]
    ic=collections.Counter(incr(e) for e in R)
    nsrc=len({e.get("src") or "?" for e in R})
    print("N",len(P),"udoi",len(set(p["doi"].lower() for p in P)),"per",per)
    print("sub",sorted(sub.items(),key=lambda t:-t[1]))
    print("meas",meas,round(100*meas/len(P)),"lcs",len(lcs),"personal",len(pers),"meta",len(meta),round(100*len(meta)/len(P)))
    print("tier",dict(tier),"A%",round(100*tier["A"]/len(P)))
    print("health basis",dict(hk),"n",hn,{k:round(100*hk[k]/hn) for k in("measured","modelled","proxy")} if hn else "")
    print("E",len(E),"ci",ci,"metric",dict(met)); print("ratio",len(R),"inc",dict(ic),"srcs",nsrc)
    if len(R)>=10: print("egger %.2f SE %.2f n %d"%egger(R))
    j=collections.Counter(p.get("journal","") for p in P); print("venues",j.most_common(8))
    af=collections.Counter()
    for p in P:
        for a in set(x.strip().rsplit(",",1)[0].strip() for x in (p.get("affil") or "").split(";") if x.strip()): af[a]+=1
    print("affil",af.most_common(10))
    if show:
        for p,b in B:
            if b in("Low-cost sensor / network","Personal / wearable") or p.get("tier")=="A": print(" ",p["_d"][-2:],p.get("tier"),b[:12],"|",p.get("short","")[:120])
        for e in E: print(" ",e["_d"][-2:],e.get("metric"),e.get("est"),e.get("lo"),e.get("hi"),incr(e) if e.get("metric") in RATIO else "-","|",e.get("src","")[:28],"|",e["label"].replace("\n"," ")[:40])
        for a,n in af.most_common(6):
            if n>=2: print("  AFF",a,[p["short"][:60] for p in P if a in (p.get("affil") or "")])
    return P,E
D=lambda a,b:["2026-11-%02d"%i for i in range(a,b+1)]
print("== W46"); wk(D(8,14)); print("== W47"); wk(D(15,21),len(sys.argv)>1)
