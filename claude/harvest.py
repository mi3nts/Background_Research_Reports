# -*- coding: utf-8 -*-
"""Harvest PM-monitoring / PM-health records for an entry-date window."""
import os, sys, json, time, urllib.parse, urllib.request, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
UA = {"User-Agent": "PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}

def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1:
                sys.stderr.write("FAIL %s :: %s\n" % (url[:120], e)); return ""
            time.sleep(3)

EUT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

QUERIES = {
 "health": '((("particulate matter"[MeSH] OR "air pollutants"[MeSH] OR PM2.5[tiab] OR "PM2.5"[tiab] OR PM10[tiab] OR "fine particulate"[tiab] OR "ultrafine particle*"[tiab] OR "black carbon"[tiab] OR "wildfire smoke"[tiab]))',
 "sensing": '(("low-cost sensor*"[tiab] OR "low cost sensor*"[tiab] OR "sensor network"[tiab] OR "co-location"[tiab] OR "colocation"[tiab] OR "field calibration"[tiab] OR "sensor drift"[tiab] OR "optical particle counter"[tiab] OR "nephelometer"[tiab] OR "aerosol monitor"[tiab] OR "PurpleAir"[tiab] OR "Plantower"[tiab] OR "air quality monitoring network"[tiab] OR "satellite AOD"[tiab] OR "land use regression"[tiab] OR "exposure model*"[tiab] OR "machine learning"[tiab]) AND ("particulate"[tiab] OR PM2.5[tiab] OR PM10[tiab] OR aerosol[tiab] OR "air quality"[tiab]))',
}

def pubmed(window_start, window_end, tag, term, retmax=200):
    q = "%s AND (%s[EDAT] : %s[EDAT])" % (term, window_start, window_end)
    u = EUT + "esearch.fcgi?db=pubmed&retmax=%d&retmode=json&term=%s" % (retmax, urllib.parse.quote(q))
    r = json.loads(get(u) or '{"esearchresult":{"idlist":[]}}')
    ids = r["esearchresult"].get("idlist", [])
    out = []
    for i in range(0, len(ids), 100):
        chunk = ids[i:i+100]
        s = get(EUT + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(chunk))
        if not s: continue
        d = json.loads(s).get("result", {})
        for pid in chunk:
            if pid in d: out.append(d[pid])
        time.sleep(0.4)
    return ids, out

def europepmc(qs, frm, to):
    u = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s"
         "&format=json&pageSize=100&resultType=core") % urllib.parse.quote(
         '(%s) AND (FIRST_PDATE:[%s TO %s])' % (qs, frm, to))
    try: return json.loads(get(u) or "{}").get("resultList", {}).get("result", [])
    except Exception: return []

def openalex(qs, frm, to):
    u = ("https://api.openalex.org/works?filter=from_created_date:%s,to_created_date:%s"
         "&search=%s&per-page=100&mailto=rittikpatra2014@gmail.com") % (frm, to, urllib.parse.quote(qs))
    try: return json.loads(get(u) or "{}").get("results", [])
    except Exception: return []

def arxiv(qs, maxr=60):
    u = ("http://export.arxiv.org/api/query?search_query=%s&sortBy=submittedDate"
         "&sortOrder=descending&max_results=%d") % (urllib.parse.quote(qs), maxr)
    return get(u)

if __name__ == "__main__":
    ws, we, day = sys.argv[1], sys.argv[2], sys.argv[3]
    cache = os.path.join(HERE, "cache", day); os.makedirs(cache, exist_ok=True)
    summary = {}
    for tag, term in QUERIES.items():
        ids, recs = pubmed(ws.replace("-", "/"), we.replace("-", "/"), tag, term)
        json.dump(recs, open(os.path.join(cache, "pubmed_%s.json" % tag), "w"))
        summary["pubmed_" + tag] = len(recs)
    e = europepmc('("PM2.5" OR "particulate matter" OR "low-cost sensor" OR "air quality sensor")', ws, we)
    json.dump(e, open(os.path.join(cache, "europepmc.json"), "w")); summary["europepmc"] = len(e)
    o = openalex("low-cost particulate matter sensor calibration", ws, we)
    json.dump(o, open(os.path.join(cache, "openalex.json"), "w")); summary["openalex"] = len(o)
    a = arxiv('all:"particulate matter" OR all:"PM2.5 sensor" OR all:"air quality sensor"')
    open(os.path.join(cache, "arxiv.xml"), "w").write(a); summary["arxiv_bytes"] = len(a)
    print(json.dumps(summary, indent=1))
