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


def save(date, papers, effects, entry_window="", lifecourse=None):
    """Persist one issue. `lifecourse` is a 5-element list of {"n", "note"} for the
    preconception / infancy / puberty / working-age / 65+ stages.

    It is optional in the signature only so older callers still import; omitting it
    is nevertheless a build failure downstream. plots.py used to fall back to a
    hardcoded [5, 3, 2, 3, 4] with exemplars from unrelated issues when this key was
    absent, which shipped a figure describing records the issue did not contain
    (found 2026-08-11). plots.py now raises instead, so a missing key stops the
    build rather than producing a plausible-looking fabrication.
    """
    out = {"date": date, "entry_window": entry_window,
           "PAPERS": papers, "EFFECTS": effects}
    if lifecourse is not None:
        out["LIFECOURSE"] = lifecourse
    json.dump(out, open(os.path.join(STORE, "%s.json" % date), "w"),
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

def _lifecourse_range(start, end):
    """Pooled life-course counts over a date range. Sums the per-stage n and merges
    the per-stage notes, so a rollup figure describes the period rather than
    silently reusing one issue's annotations. Notes from issues that contributed
    no records to a stage are dropped, and wrapping is on word boundaries."""
    stages, notes = None, None
    for ds in available_dates():
        if not (start <= ds <= end):
            continue
        lc = _lifecourse(ds)
        if not lc:
            continue
        if stages is None:
            stages = [0] * len(lc); notes = [[] for _ in lc]
        for i, cell in enumerate(lc[:len(stages)]):
            n = cell.get("n", 0)
            stages[i] += n
            if not n:                     # an empty stage has nothing to describe
                continue
            head = (cell.get("note") or "").split(":")[-1].replace("\n", " ")
            head = " ".join(head.split()).strip(" ;,")
            for part in (x.strip() for x in head.split(",")):
                if part and part not in notes[i] and len(notes[i]) < 5:
                    notes[i].append(part)

    def wrap(txt, width=26):
        out, line = [], ""
        for w in txt.split():
            if len(line) + len(w) + 1 > width:
                out.append(line); line = w
            else:
                line = (line + " " + w).strip()
        if line:
            out.append(line)
        return "\n".join(out[:4])

    if stages is None:
        return None
    return [{"n": n, "note": wrap(", ".join(ns)) if ns else "no record\nthis period"}
            for n, ns in zip(stages, notes)]


LIFECOURSE = _lifecourse_range(_start, _end) if (_start and _end) else _lifecourse(_date)
