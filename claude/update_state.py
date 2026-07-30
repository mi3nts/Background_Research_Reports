#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic state maintenance for a PM Research Watch issue.

  python3 update_state.py <date>

Idempotent. Appends the issue's records to state/seen.json (pmid / doi / tsig),
rewrites state/metrics.csv with csv.writer so subtopics containing a comma
cannot break the column count, and updates state/last_run.json.
"""
import os, sys, json, csv, glob, hashlib, re, datetime

HERE  = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state")
STORE = os.path.join(STATE, "corpus")


def tsig(rec):
    """SHA-1 of normalised title + first author surname + year."""
    t = re.sub(r"[^a-z0-9]+", " ", (rec.get("title") or "").lower()).strip()
    short = (rec.get("short") or "").split()
    au = short[0].lower() if short else ""
    yr = short[-1][:4] if short and short[-1][:4].isdigit() else ""
    return hashlib.sha1(("%s|%s|%s" % (t, au, yr)).encode("utf-8")).hexdigest()


def update_seen(date):
    path = os.path.join(STATE, "seen.json")
    seen = json.load(open(path)) if os.path.exists(path) else {}
    for k in ("pmid", "doi", "tsig"):
        seen.setdefault(k, {})
    papers = json.load(open(os.path.join(STORE, "%s.json" % date))).get("PAPERS", [])
    added = 0
    for r in papers:
        if r.get("pmid"):
            added += seen["pmid"].setdefault(str(r["pmid"]), date) == date
        if r.get("doi"):
            seen["doi"].setdefault(r["doi"].lower(), date)
        seen["tsig"].setdefault(tsig(r), date)
    json.dump(seen, open(path, "w"), indent=1)
    return len(papers), added


def rewrite_metrics():
    """Rebuild metrics.csv from the corpus store. Quoted, so commas are safe."""
    rows = []
    for p in sorted(glob.glob(os.path.join(STORE, "*.json"))):
        d = json.load(open(p))
        counts = {}
        for r in d.get("PAPERS", []):
            counts[r["sub"]] = counts.get(r["sub"], 0) + 1
        for sub in sorted(counts):
            rows.append([d["date"], sub, counts[sub]])
    with open(os.path.join(STATE, "metrics.csv"), "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(["date", "subtopic", "n"])
        w.writerows(rows)
    return len(rows)


def update_last_run(date):
    json.dump({"last_entry_date": date,
               "last_run_utc": datetime.datetime.now(datetime.timezone.utc)
                                       .strftime("%Y-%m-%dT%H:%M:%SZ")},
              open(os.path.join(STATE, "last_run.json"), "w"), indent=1)


if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    n, _ = update_seen(date)
    m = rewrite_metrics()
    update_last_run(date)
    print("seen updated from %d records; metrics.csv rewritten (%d rows); last_run=%s"
          % (n, m, date))
