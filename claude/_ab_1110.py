import json,sys
f=json.load(open("cache/%s/_fresh.json"%sys.argv[1]))
for i in map(int,sys.argv[2].split(",")):
    r=f[i]; print("\n#%d"%i,r.get("pmid"),r.get("doi"),"|",r.get("journal"),"|",r.get("authors","")[:60],"|",r["title"]); print(r.get("abstract","")[:2600])
