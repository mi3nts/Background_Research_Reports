# -*- coding: utf-8 -*-
# Helper for 2026-11-10 authoring: pmid/doi/title are copied from the harvest cache, never typed.
import json, re, html, unicodedata
_F = json.load(open("cache/2026-11-10/_fresh.json"))
_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
def _ascii(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t or "")).translate(_SUB).replace("‐", "-")
    t = re.sub(r"PM\s*\(?\s*2\s*\.\s*5(?:\s*\))?", "PM2.5", t); t = re.sub(r"PM\s*\(?10\)?", "PM10", t)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip()
def R(i, journal, **k):
    r = _F[i]
    doi = (r.get("doi") or "").lower()
    if not doi and r.get("src") == "arxiv":
        x = open("cache/2026-11-10/arxiv.xml").read(); j = x.find(r["title"][:30]); s = x.rfind("<entry>", 0, j)
        aid = re.search(r"<id>http://arxiv.org/abs/([0-9.]+)v\d+</id>", x[s:j]).group(1); doi = "10.48550/arXiv." + aid
    d = dict(pmid=str(r.get("pmid") or ""), doi=doi, journal=journal, title=_ascii(r["title"]))
    d.update(k); return d
