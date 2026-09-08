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
import os, sys, json, glob, time, urllib.request, urllib.error, urllib.parse

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


def handle_registered(doi):
    """Authoritative last resort: is the DOI registered in the global Handle system?

    Added 2026-09-04. Two records FAILed as DEAD-DOI on the 3 Sep issue --
    10.12182/20260760103 (J Sichuan Univ Med Sci) and 10.3967/bes2026.072
    (Biomed Environ Sci). Both are indexed by PubMed under exactly those DOIs and
    both resolve in a browser. They failed because the two existing legs cannot see
    them: they are registered outside Crossref (Chinese registration agency), so
    Crossref returns 404, and their publishers drop or stall a bare HEAD from this
    sandbox, so the doi.org fallback times out. That combination -- non-Crossref
    agency plus HEAD-hostile publisher -- produced a false FAIL that would have
    silently dropped two tier-A cohort records from the issue.

    https://doi.org/api/handles/<doi> is the resolver's own metadata API. It answers
    with responseCode 1 and the registered target URL when the DOI exists, and 100
    when it does not, and it does not touch the publisher at all.
    """
    try:
        d = json.load(_get("https://doi.org/api/handles/" + urllib.parse.quote(doi), 30))
        return d.get("responseCode") == 1
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read()).get("responseCode") == 1
        except Exception:
            return False
    except Exception:
        return False


def doi_org_live(doi):
    try:
        req = urllib.request.Request("https://doi.org/" + doi, headers=UA, method="HEAD")
        if urllib.request.urlopen(req, timeout=25).status < 400:
            return True
    except urllib.error.HTTPError as e:
        if e.code < 400:
            return True
    except Exception:
        pass
    return handle_registered(doi)


def overlap(a, b):
    wa = {w.lower().strip(".,:;()") for w in a.split() if len(w) > 4}
    wb = {w.lower().strip(".,:;()") for w in b.split() if len(w) > 4}
    return len(wa & wb) / max(1, len(wa))


def prior_issue_dois(date):
    """DOI (lowercased) -> the issue that already shipped it, for every issue
    OTHER than `date`.

    Added 2026-09-01. The August monthly rollup found **8 duplicate records
    across 7 DOIs** (1-3 Aug x4, 7/9 Aug, 24/25 Aug x2) that had all been
    correctly written into `state/seen.json` under their first issue date and
    were then re-summarised the next day under a reworded title. So the index
    was being *written* and not *read*: the screening step is a human-in-the-
    loop judgement and cannot be trusted to consult it. This reads the shipped
    corpus itself rather than seen.json, so it cannot be defeated by a
    write-side bug either.
    """
    out = {}
    for path in sorted(glob.glob(os.path.join(STORE, "*.json"))):
        d = os.path.basename(path)[:-5]
        if d == date:
            continue
        for p in json.load(open(path)).get("PAPERS", []):
            if p.get("doi"):
                out.setdefault(p["doi"].strip().lower(), d)
    return out


def check(date):
    path = os.path.join(STORE, "%s.json" % date)
    papers = json.load(open(path))["PAPERS"]
    pmids = [str(p["pmid"]) for p in papers if str(p.get("pmid", "")).isdigit()]
    live = pubmed_dois(pmids)
    prior = prior_issue_dois(date)
    seen_here = {}

    fails, warns = [], []
    for p in papers:
        doi, pmid, short = p.get("doi"), str(p.get("pmid") or ""), p.get("short")
        if not doi:
            fails.append((short, "NO-DOI", "record has no DOI"))
            continue

        # 0. cross-issue duplicate - the index was written but not read
        key = doi.strip().lower()
        if key in prior:
            fails.append((short, "DUPLICATE-DOI",
                          "%s already shipped in the %s issue" % (doi, prior[key])))
            continue
        if key in seen_here:
            fails.append((short, "DUPLICATE-DOI",
                          "%s appears twice in this issue (also %s)" % (doi, seen_here[key])))
            continue
        seen_here[key] = short

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
            elif pmid in live and live[pmid].lower() == doi.lower():
                # Deposit lag, not a wrong DOI. Added 2026-09-07 after
                # 10.1016/j.envres.2026.125643 (Environ Res, indoor PAH across six
                # European cities) FAILed DEAD-DOI on both remaining legs: Crossref
                # 404 and the Handle API 404, i.e. the suffix is not registered
                # anywhere yet. Elsevier had accepted the article -- PubMed carries
                # the PII S0013-9351(26)01974-2 -- but had not deposited the DOI.
                #
                # The failure this gate exists to catch is a DOI belonging to some
                # OTHER paper, which is what the scoped-XPath defect in
                # pubmed_fetch.py used to produce. That failure mode is excluded
                # exactly when PubMed's own record asserts this same DOI string,
                # which is the authority leg at step 1. So when step 1 has already
                # confirmed the string and only registration is missing, this is a
                # warn, not a fail: the identifier is right and will resolve once
                # the publisher deposits. Do NOT relax this to records whose PMID
                # is absent from `live` -- an unconfirmed unresolvable DOI stays a
                # hard FAIL, because nothing then vouches for the string.
                warns.append((short, "UNREGISTERED-DOI",
                              "%s not yet deposited (Crossref and Handle both 404) "
                              "but PubMed reports this exact DOI" % doi))
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
