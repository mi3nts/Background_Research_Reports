# -*- coding: utf-8 -*-
"""Fill missing abstracts (and own DOI) for PMID-bearing _fresh records via efetch.
Scoped DOI lookup per pubmed_fetch.doi_of (never .//ArticleId). Usage: _absfill_1030.py <day>..."""
import sys, json, urllib.request, xml.etree.ElementTree as ET, time
from pubmed_fetch import doi_of
UA = {"User-Agent": "PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
for D in sys.argv[1:]:
    p = "cache/%s/_fresh.json" % D; f = json.load(open(p))
    need = [r for r in f if r.get("pmid") and not r.get("abstract")]
    got = 0
    for i in range(0, len(need), 100):
        ids = ",".join(r["pmid"] for r in need[i:i+100])
        x = urllib.request.urlopen(urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=" + ids, headers=UA), timeout=90).read()
        for art in ET.fromstring(x).findall("PubmedArticle"):
            pm = art.findtext("./MedlineCitation/PMID")
            ab = " ".join("".join(a.itertext()) for a in art.findall("./MedlineCitation/Article/Abstract/AbstractText"))
            for r in need:
                if r["pmid"] == pm:
                    if ab: r["abstract"] = ab[:3000]; r["abs_via"] = "efetch"; got += 1
                    if not r.get("doi"):
                        d = doi_of(art)
                        if d: r["doi"] = d.lower()
        time.sleep(0.4)
    json.dump(f, open(p, "w"), indent=1)
    print(D, "need", len(need), "filled", got)
