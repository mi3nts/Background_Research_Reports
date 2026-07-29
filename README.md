# Background Research Reports

[Visit the report calendar](https://mi3nts.github.io/Background_Research_Reports/index.dc.html)

**PM Research Watch** — an automated literature-surveillance pipeline for MINTS
Research that tracks new publications on particulate matter (PM) monitoring
(sensing, calibration, exposure modelling) and PM health effects, and publishes
them as dated PDF digests on a GitHub Pages calendar site.

## How it works

1. A daily job (`claude/harvest.py`) queries PubMed, Europe PMC, OpenAlex, and
   arXiv for new records since the last run.
2. Candidates are screened and deduplicated against `claude/state/seen.json`,
   then stored as structured records in `claude/state/corpus/`.
3. `claude/plots.py` and `claude/mktable.py` generate figures and tables, which
   are assembled into a LaTeX digest (`claude/templates/daily.tex`) and rendered
   to PDF.
4. The PDF is copied into `Reports/daily/`, and `claude/build_manifest.py`
   rebuilds `Reports/reports.json` — the manifest the website reads.
5. Periodic rollups (weekly, monthly, yearly) aggregate the daily records into
   `Reports/weekly/`, `Reports/monthly/`, and `Reports/yearly/`.

See `claude/PIPELINE.md` for the full pipeline contract, run order, and
per-source notes.

## Repo layout

```
Reports/reports.json                      # manifest the website reads
Reports/{daily,weekly,monthly,yearly}/    # generated PDF digests
claude/                                   # pipeline scripts + persistent state
index.dc.html, index.html, support.js     # GitHub Pages calendar site
assets/                                   # site images/logo
```

`index.html` redirects to `index.dc.html`, which renders the report calendar
and an in-browser PDF reader driven by `Reports/reports.json`.
