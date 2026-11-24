# -*- coding: utf-8 -*-
# Bibliographic fields copied from the harvest cache only (no hand-written DOIs).
import json, re
_F = json.load(open("cache/2026-11-23/_fresh.json", encoding="utf-8"))
def R(i, **k):
    r = _F[i]
    t = re.sub(r"\s+", " ", r["title"]).strip()
    j = re.sub(r"\s+", " ", r["journal"]).replace("&amp;", "&").strip()
    d = dict(pmid=r.get("pmid", "") or "", doi=r["doi"].lower(), journal=j, title=t)
    d.update(k); return d
