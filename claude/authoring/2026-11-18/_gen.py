# -*- coding: utf-8 -*-
"""Generate p01..pNN.py for 18 Nov from cache (pmid/doi/journal/title copied, never typed)."""
import json, re, html, unicodedata, os
D = "2026-11-18"; H = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(H, "..", "..", "cache", D, "_fresh.json")))
def asc(t):
    t = html.unescape(re.sub(r"<[^>]+>", " ", t or ""))
    t = t.replace("–", "-").replace("—", "-").replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"').replace("₂", "2").replace("₃", "3").replace("₅", "5").replace("₀", "0").replace("₁", "1").replace("₈", "8").replace("₄", "4").replace("µ", "u").replace("μ", "u")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip()
def jn(r): return asc(r.get("journal", ""))
R = []
def add(i, **k):
    r = f[i]; d = dict(pmid=str(r.get("pmid") or ""), doi=r.get("doi", ""), journal=jn(r), title=asc(r["title"]))
    d.update(k); R.append((d, k["sub"]))
MD = "Metadata only: no abstract in Crossref at issue time"
exec(open(os.path.join(H, "_recs.py"), encoding="utf-8").read())
for c in range(0, len(R), 4):
    with open(os.path.join(H, "p%02d.py" % (c // 4 + 1)), "w", encoding="utf-8") as o:
        o.write("# -*- coding: utf-8 -*-\nP = [\n")
        for d, sub in R[c:c+4]:
            dd = {k: v for k, v in d.items() if k != "sub"}
            o.write(" dict(" + ", ".join("%s=%r" % (k, v) for k, v in dd.items()) + ", sub=corpus.%s),\n" % sub)
        o.write("]\n")
print(len(R), "records ->", (len(R) + 3) // 4, "files")
