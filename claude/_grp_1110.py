import glob,corpus,collections,sys,re
D=sys.argv[1]
src=open("plots.py").read().split("_design_unmapped = set()")[0]
src=re.sub(r"^(import corpus|from corpus).*$","",src,flags=re.M)
import os; g={"__name__":"x","__file__":os.path.abspath("plots.py")}
try: exec(src,g)
except Exception as e: print("exec err",e)
dg=g.get("design_group",{})
P=[]
for f in sorted(glob.glob("authoring/%s/p*.py"%D)):
    h={"corpus":corpus}; exec(open(f).read(),h); P+=h["P"]
print(collections.Counter(dg.get(p["design"],"UNMAPPED:"+p["design"]) for p in P).most_common())
print(collections.Counter((p["sub"][:12],dg.get(p["design"],"?")[:22]) for p in P).most_common())
