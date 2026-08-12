#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch full PubMed records (title, journal, abstract, DOI, entry date) by PMID.

  python3 pubmed_fetch.py <issue-date> <pmid> [<pmid> ...]

Writes cache/<issue-date>/connector_pubmed.json and prints a one-line-per-record
table. `harvest.py` uses esummary, which does not return a DOI at all; this is the
efetch path used to resolve the PMIDs the PubMed *connector* returns.

DEFECT FIXED 2026-08-11 -- READ BEFORE EDITING THE XPATH.
An efetch PubmedArticle embeds the full reference list, and every cited reference
carries its own <ArticleId IdType="doi">. A `.//ArticleId` search therefore matches
the first DOI *anywhere in the record*, which for many articles is a reference, not
the article. On 2026-08-11 that gave 15 of 33 records a DOI belonging to a paper they
merely cited -- several from the 2010s -- and the failure is invisible in the rendered
PDF because a wrong DOI still typesets as a plausible link. Scope the lookup to
PubmedData/ArticleIdList (the record's own identifier block) and fall back to
Article/ELocationID[@EIdType="doi"]. check_dois.py is the backstop, not the fix.
"""
import os, sys, json, urllib.request, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
EFETCH = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
          "?db=pubmed&retmode=xml&id=%s")


def doi_of(art):
    """The article's OWN doi. Never `.//ArticleId` -- see the module docstring."""
    idl = art.find("./PubmedData/ArticleIdList")
    if idl is not None:
        for i in idl.findall("ArticleId"):
            if i.get("IdType") == "doi" and (i.text or "").strip():
                return i.text.strip()
    for e in art.findall("./MedlineCitation/Article/ELocationID"):
        if e.get("EIdType") == "doi" and (e.text or "").strip():
            return e.text.strip()
    return ""


def entry_date(art):
    """Entrez create date. NOT the same field as PubMed's [EDAT] search tag: on
    2026-08-11, 10 of 33 records matched an [EDAT] of 11 Aug while carrying an
    Entrez date of 10 Aug. Report it, do not window on it."""
    for pd in art.findall(".//PubMedPubDate"):
        if pd.get("PubStatus") == "entrez":
            try:
                return "%s-%02d-%02d" % (pd.findtext("Year"),
                                         int(pd.findtext("Month")),
                                         int(pd.findtext("Day")))
            except (TypeError, ValueError):
                return ""
    return ""


def fetch(pmids):
    xml = urllib.request.urlopen(EFETCH % ",".join(pmids), timeout=120).read()
    out = []
    for art in ET.fromstring(xml).findall(".//PubmedArticle"):
        ti = art.find(".//ArticleTitle")
        out.append({
            "pmid": art.findtext("./MedlineCitation/PMID") or "",
            "doi": doi_of(art),
            "title": " ".join(ti.itertext()).strip() if ti is not None else "",
            "journal": art.findtext(".//Journal/ISOAbbreviation") or "",
            "abstract": " ".join(" ".join(a.itertext())
                                 for a in art.findall(".//Abstract/AbstractText")).strip(),
            "entrez_date": entry_date(art),
        })
    return out


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    date, pmids = sys.argv[1], sys.argv[2:]
    recs = fetch(pmids)
    d = os.path.join(HERE, "cache", date)
    os.makedirs(d, exist_ok=True)
    json.dump(recs, open(os.path.join(d, "connector_pubmed.json"), "w"), indent=1)
    for r in recs:
        print("[%s] %s %-26s | %-92s | abs=%d"
              % (r["pmid"], r["entrez_date"], r["journal"][:26], r["title"][:92],
                 len(r["abstract"])))
    print("%d records -> cache/%s/connector_pubmed.json" % (len(recs), date))
