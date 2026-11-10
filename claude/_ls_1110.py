import json,sys
f=json.load(open("cache/%s/_fresh.json"%sys.argv[1]))
for i,r in enumerate(f): print(i,("A" if r.get("abstract") else "-"),r["src"][:8],(r.get("journal") or "")[:22],"|",r["title"][:105])
