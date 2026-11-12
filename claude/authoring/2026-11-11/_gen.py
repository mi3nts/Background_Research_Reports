# -*- coding: utf-8 -*-
"""Emit p01..pNN.py for 11 Nov from _gen_[a-e].py, injecting pmid/doi/journal/title from the cache (DOIs never hand-typed)."""
import json, re, glob, os, html, unicodedata
B = "authoring/2026-11-11"
f = json.load(open("cache/2026-11-11/_fresh.json"))
R = {}
for g in sorted(glob.glob(B + "/_gen_[a-e].py")):
    d = {}; exec(open(g, encoding="utf-8").read(), d); R.update(d["R"])
def asc(t):
    t = re.sub(r"<[^>]+>", "", html.unescape(t)); t = re.sub(r"\s+", " ", t).strip()
    t = t.replace("PM(2.5)", "PM2.5").replace("PM(10)", "PM10").replace("NO(x)", "NOx").replace("O(3)", "O3")
    t = t.replace("α", "alpha").replace("‑", "-").replace("–", "-").replace("—", "-").replace("’", "'")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return t
keys = sorted(R); W = {}
for k in keys:
    w = len(R[k]["n"].split()); W[k] = w
chunks = [keys[i:i+4] for i in range(0, len(keys), 4)]
for j, ch in enumerate(chunks, 1):
    out = ["# -*- coding: utf-8 -*-", "P = ["]
    for k in ch:
        r = dict(R[k]); c = f[k]
        sub = r.pop("sub")
        r = dict(pmid=c.get("pmid") or "", doi=c["doi"].lower(), journal=re.sub(r"\s+", " ", c.get("journal") or ""), title=asc(c["title"]), **r)
        body = ", ".join("%s=%r" % (a, b) for a, b in r.items())
        out.append(" dict(%s, sub=corpus.%s)," % (body, sub))
    out.append("]")
    open(os.path.join(B, "p%02d.py" % j), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(keys), "records in", len(chunks), "files"); print("words", W)
