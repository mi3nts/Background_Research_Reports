#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Single orchestrator for a PM Research Watch run.

Deterministic steps only. Screening and paper summaries are model work and are
written into state/corpus/<date>.json before this is invoked with --post.

  python3 run_all.py --harvest [--date YYYY-MM-DD]   # steps 1-2
  python3 run_all.py --post    [--date YYYY-MM-DD]   # steps 5-9 (figures -> manifest)
"""
import os, sys, json, subprocess, datetime, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STATE = os.path.join(HERE, "state")


def run(cmd, env=None, cwd=HERE):
    e = dict(os.environ); e.update(env or {})
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True, env=e, cwd=cwd)


def last_entry_date():
    p = os.path.join(STATE, "last_run.json")
    return json.load(open(p))["last_entry_date"] if os.path.exists(p) else None


def harvest(date):
    prev = last_entry_date()
    start = (datetime.date.fromisoformat(prev) + datetime.timedelta(days=1)).isoformat() if prev else date
    run(["python3", "harvest.py", start, date, date])
    print("entry window:", start, "->", date)


def post(date):
    figdir = os.path.join(HERE, "fig", date)
    build = os.path.join(HERE, "build")
    os.makedirs(figdir, exist_ok=True); os.makedirs(build, exist_ok=True)
    env = {"PMRW_DATE": date, "PMRW_FIGDIR": figdir, "PMRW_BUILD": build}
    run(["python3", "plots.py"], env)
    run(["python3", "mktable.py"], env)
    if not os.path.exists(os.path.join(build, "preamble.tex")):
        run(["cp", os.path.join(HERE, "preamble.tex"), build])
    link = os.path.join(build, "fig")
    if not os.path.exists(link):
        os.symlink(figdir, link)
    for _ in range(2):
        run(["pdflatex", "-interaction=nonstopmode", "digest.tex"], cwd=build)
    out = os.path.join(ROOT, "Reports", "daily", "PM-Research-Watch_%s.pdf" % date)
    run(["cp", os.path.join(build, "digest.pdf"), out])
    run(["python3", "build_manifest.py"])
    print("wrote", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--harvest", action="store_true")
    ap.add_argument("--post", action="store_true")
    a = ap.parse_args()
    if a.harvest: harvest(a.date)
    if a.post: post(a.date)
    if not (a.harvest or a.post): ap.print_help()
