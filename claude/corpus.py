# -*- coding: utf-8 -*-
"""Persistent corpus store for PM Research Watch.

State lives in claude/state/corpus/YYYY-MM-DD.json (one file per daily issue).
This module is a *loader*: it exposes the same PAPERS / EFFECTS names the
figure and table generators have always used, so plots.py and mktable.py keep
working unmodified.

    PMRW_DATE   env var - which day to expose as PAPERS/EFFECTS (default: newest)
    PMRW_START  env var - with PMRW_END, expose a pooled range instead (rollups)
    PMRW_END
"""
import os, json, glob, datetime

HERE  = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, "state", "corpus")

# subtopic keys - canonical, do not renumber or rename
MECH = "Mechanistic toxicology"
CVM  = "Cardiovascular & metabolic"
NEU  = "Neuro / mental health"
RESP = "Respiratory & allergic"
REPR = "Reproductive & developmental"
EXPO = "Exposure assessment & modelling"
SENS = "Sensing, forecasting & instrumentation"
OCC  = "Occupational & indoor"
BURD = "Burden, policy & mitigation"
OTHR = "Other clinical endpoints"

SUBTOPICS = [MECH, CVM, NEU, RESP, REPR, EXPO, SENS, OCC, BURD, OTHR]


def available_dates():
    return sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(STORE, "*.json")))


def load(date=None):
    """Return (papers, effects) for one issue date."""
    if date is None:
        ds = available_dates()
        if not ds:
            return [], []
        date = ds[-1]
    path = os.path.join(STORE, "%s.json" % date)
    if not os.path.exists(path):
        return [], []
    d = json.load(open(path))
    return d.get("PAPERS", []), d.get("EFFECTS", [])


def load_range(start, end):
    """Pooled (papers, effects) over an inclusive date range; each record is
    tagged with `_date` so rollups can do trend analysis."""
    papers, effects = [], []
    for ds in available_dates():
        if start <= ds <= end:
            p, e = load(ds)
            for r in p:
                r = dict(r); r["_date"] = ds; papers.append(r)
            for r in e:
                r = dict(r); r["_date"] = ds; effects.append(r)
    return papers, effects


def save(date, papers, effects, entry_window=""):
    os.makedirs(STORE, exist_ok=True)
    json.dump({"date": date, "entry_window": entry_window,
               "PAPERS": papers, "EFFECTS": effects},
              open(os.path.join(STORE, "%s.json" % date), "w"),
              indent=1, ensure_ascii=False)


_start, _end, _date = os.environ.get("PMRW_START"), os.environ.get("PMRW_END"), os.environ.get("PMRW_DATE")
if _start and _end:
    PAPERS, EFFECTS = load_range(_start, _end)
else:
    PAPERS, EFFECTS = load(_date)

def _lifecourse(date=None):
    if date is None:
        ds = available_dates()
        date = ds[-1] if ds else None
    if not date:
        return None
    p = os.path.join(STORE, "%s.json" % date)
    if not os.path.exists(p):
        return None
    return json.load(open(p)).get("LIFECOURSE")

LIFECOURSE = None if (_start and _end) else _lifecourse(_date)
