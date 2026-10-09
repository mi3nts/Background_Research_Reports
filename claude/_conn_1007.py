# -*- coding: utf-8 -*-
"""PubMed connector PMIDs (EDAT 2026/10/06; health 14, sensing 1 (EDAT 3-6 Oct)) -> esummary,
bucket by entrez date into cache/<day>/pubmed_connector_raw.json. Merge into _fresh with
_connmerge_0929.py <day> after that day's screen."""
import json, urllib.request, sys
IDS = sys.argv[1].split(",")
UA = {"User-Agent": "PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
out = {}
for i in range(0, len(IDS), 100):
    u = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(IDS[i:i+100])
    j = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read())
    for uid in j["result"]["uids"]:
        r = j["result"][uid]
        ed = next((h["date"][:10].replace("/", "-") for h in r.get("history", []) if h["pubstatus"] == "entrez"), "")
        out.setdefault(ed, []).append(r)
for d, rs in sorted(out.items()):
    print(d, len(rs))
    if d in ("2026-10-06",):
        json.dump(rs, open("cache/%s/pubmed_connector_raw.json" % d, "w"), indent=1)
