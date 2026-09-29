# -*- coding: utf-8 -*-
"""Leg-by-leg harvest under the device_bash 180 s cap (nohup does not survive).
Usage: python3 _harv_0929.py <day> <leg>   leg in pubmed|epmc|crossref|misc"""
import sys, os, json
import harvest as H
day, leg = sys.argv[1], sys.argv[2]
c = os.path.join(H.HERE, "cache", day); os.makedirs(c, exist_ok=True)
if leg == "pubmed":
    for tag, term in H.QUERIES.items():
        ids, recs = H.pubmed(day.replace("-", "/"), day.replace("-", "/"), tag, term)
        json.dump(recs, open(os.path.join(c, "pubmed_%s.json" % tag), "w")); print(tag, len(recs))
elif leg == "epmc":
    e = H.europepmc('("PM2.5" OR "particulate matter" OR "low-cost sensor" OR "air quality sensor")', day, day)
    json.dump(e, open(os.path.join(c, "europepmc.json"), "w")); print("epmc", len(e))
elif leg == "crossref":
    cj = H.crossref_sensing(day, day)
    json.dump(cj, open(os.path.join(c, "crossref_journals.json"), "w")); print("crossref", len(cj))
elif leg == "misc":
    try: o = H.openalex("low-cost particulate matter sensor calibration", day, day)
    except Exception as ex: o = []; print("openalex fail", ex)
    json.dump(o, open(os.path.join(c, "openalex.json"), "w")); print("openalex", len(o))
    try: a = H.arxiv('all:"particulate matter" OR all:"PM2.5 sensor" OR all:"air quality sensor"')
    except Exception as ex: a = ""; print("arxiv fail", ex)
    open(os.path.join(c, "arxiv.xml"), "w").write(a or ""); print("arxiv bytes", len(a or ""))
