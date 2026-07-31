#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DOI validation gate for PM Research Watch.

Every record's DOI is checked two ways before an issue ships:

  1. **Authority check** - if the record has a PMID, ask NCBI what DOI that PMID
     actually carries now. PubMed occasionally indexes a placeholder or an
     outright wrong DOI at entry time and corrects it days later; four such
     records shipped in the 28-29 Jul issues before this check existed.
  2. **Resolution check** - resolve the DOI and compare the registered title to
     the stored title. Catches minted, transcribed or hallucinated DOIs that
     happen to be well-formed. Crossref first; anything Crossref does not know
     (CMA journals, some society publishers) falls back to an HTTP HEAD against
     doi.org, which only proves the link is live.

Severity is split deliberately. A **FAIL** means the link is provably wrong and
the build should stop: no DOI, a DOI that disagrees with the PMID's own record,
or a DOI that does not resolve at all. A **WARN** means the heuristic fired but
judgement is needed - title overlap is low, which is normal for this digest
because the `title` field is an editorial focus line, not the verbatim
registered title. Warnings do not gate the build; all four real errors found in
the 28-29 Jul issues were FAIL-class, so the gate loses nothing by not
hard-failing on paraphrase.

Exit status is 1 if any record FAILs, so this can gate a build.

    python3 check_dois.py                # newest issue
    python3 check_dois.py 2026-07-29     # one issue
    python3 check_dois.py --all          # every issue in the store
"""
import os, sys, json, glob, time, urllib.request, urllib.error

HERE  = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "state", "corpus")
UA    = {"User-Agent": "PM-Research-Watch/1.0 (https://github.com/mi3nts)"}
TITLE_OVERLAP_MIN = 0.30


def _get(url, timeout=25):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)


def pubmed_dois(pmids):
    """PMID -> DOI as PubMed currently reports it."""
    out = {}
    for i in range(0, len(pmids), 100):
        chunk = pmids[i:i + 100]
        url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
               "?db=pubmed&retmode=json&id=" + ",".join(chunk))
        try:
            res = json.load(_get(url, 60))["result"]
        except Exception as e:
            print("  ! PubMed esummary failed (%s) - authority check skipped" % e)
            return out
        for p in chunk:
            for a in res.get(p, {}).get("articleids", []):
                if a["idtype"] == "doi":
                    out[p] = a["value"]
        time.sleep(0.4)
    return out


def crossref(doi):
    """(title, container) or (None, reason)."""
    try:
        m = json.load(_get("https://api.crossref.org/works/" + doi))["message"]
        return (m.get("title") or [""])[0], (m.get("container-title") or [""])[0]
    except Exception as e:
        return None, str(e)[:60]


def doi_org_live(doi):
    try:
        req = urllib.request.Request("https://doi.org/" + doi, headers=UA, method="HEAD")
        return urllib.request.urlopen(req, timeout=25).status < 400
    except urllib.error.HTTPError as e:
        return e.code < 400
    except Exception:
        return False


def overlap(a, b):
    wa = {w.lower().strip(".,:;()") for w in a.split() if len(w) > 4}
    wb = {w.lower().strip(".,:;()") for w in b.split() if len(w) > 4}
    return len(wa & wb) / max(1, len(wa))


def check(date):
    path = os.path.join(STORE, "%s.json" % date)
    papers = json.load(open(path))["PAPERS"]
    pmids = [str(p["pmid"]) for p in papers if str(p.get("pmid", "")).isdigit()]
    live = pubmed_dois(pmids)

    fails, warns = [], []
    for p in papers:
        doi, pmid, short = p.get("doi"), str(p.get("pmid") or ""), p.get("short")
        if not doi:
            fails.append((short, "NO-DOI", "record has no DOI"))
            continue

        # 1. authority - the reliable check
        if pmid in live and live[pmid].lower() != doi.lower():
            fails.append((short, "PUBMED-MISMATCH",
                          "stored %s but PubMed now reports %s" % (doi, live[pmid])))
            continue

        # 2. resolution
        title, container = crossref(doi)
        if title is None:
            if doi_org_live(doi):
                warns.append((short, "NOT-IN-CROSSREF",
                              "%s resolves at doi.org but Crossref has no record" % doi))
            else:
                fails.append((short, "DEAD-DOI", "%s does not resolve (%s)" % (doi, container)))
        else:
            ov = overlap(p["title"], title)
            if ov < TITLE_OVERLAP_MIN:
                warns.append((short, "TITLE-MISMATCH",
                              "%s registers as %r (overlap %.2f)" % (doi, title[:70], ov)))
        time.sleep(0.15)
    return fails, warns


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    dates = ([os.path.basename(p)[:-5] for p in sorted(glob.glob(os.path.join(STORE, "*.json")))]
             if "--all" in args else
             [a for a in args if not a.startswith("-")] or
             [sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(STORE, "*.json")))[-1]])

    n_fail = n_warn = 0
    for d in dates:
        print("== %s" % d)
        fails, warns = check(d)
        for short, kind, msg in fails:
            print("  FAIL %-16s %-16s %s" % (short, kind, msg))
        for short, kind, msg in warns:
            print("  warn %-16s %-16s %s" % (short, kind, msg))
        print("  %d fail, %d warn" % (len(fails), len(warns)))
        n_fail += len(fails); n_warn += len(warns)
    print("\nTOTAL: %d FAIL, %d warn" % (n_fail, n_warn))
    if n_warn and not n_fail:
        print("Warnings are advisory - title overlap is low when the digest's focus line "
              "paraphrases the registered title. Confirm by eye, then ship.")
    sys.exit(1 if n_fail else 0)
