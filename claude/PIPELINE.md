# PM Research Watch — pipeline

Automated daily literature surveillance on **particulate matter monitoring**
(sensing, calibration, exposure modelling) and **PM health effects**.
Output: a LaTeX/PDF digest in `Reports/daily/`, plus periodic rollups, indexed by
`Reports/reports.json` which the calendar site (`index.dc.html`) reads.

---

## Repo contract

```
Reports/reports.json                      # THE manifest the website reads
Reports/{daily,weekly,monthly,yearly}/    # flat PDFs, no nested year folders
claude/                                   # machinery + persistent state
index.dc.html, support.js, assets/, .nojekyll
"MINTS Calendar Report Site/"             # mirror; written by build_manifest.py, never by hand
```

Manifest entries are **always** object form `{"file": ..., "title": ...}`, sorted
newest first, and every filename contains a literal `YYYY-MM-DD` — that string alone
places the report on the calendar. Filenames stay flat inside the cadence folder
(the site parser prepends `Reports/<folder>/`).

Naming: `PM-Research-Watch_YYYY-MM-DD.pdf`, `PM-Research-Watch-Weekly_YYYY-MM-DD.pdf`,
`-Monthly_`, `-Yearly_`. Rollups use the **period-end date** (the Sunday of generation)
so they land on a real calendar cell.

---

## Layout of `claude/`

| Path | Role |
|---|---|
| `corpus.py` | **Loader** over `state/corpus/*.json`. Exposes `PAPERS`, `EFFECTS`, `LIFECOURSE`, the ten subtopic constants, and `load(date)` / `load_range(start, end)` / `save(...)`. Env: `PMRW_DATE`, or `PMRW_START`+`PMRW_END` for pooled rollups. |
| `state/corpus/YYYY-MM-DD.json` | One issue's records. Keys: `date`, `entry_window`, `PAPERS`, `EFFECTS`, `LIFECOURSE`. |
| `state/seen.json` | Dedup index: `pmid` / `doi` (lowercased) / `tsig` (SHA-1 of normalised title + first author + year) → issue date. |
| `state/last_run.json` | `last_entry_date`, `last_run_utc`. |
| `state/metrics.csv` | `date,subtopic,n` — history for trend figures and rollups. |
| `state/rejected.jsonl` | One line per screened-out record with a reason. |
| `harvest.py` | PubMed / Europe PMC / OpenAlex / arXiv fetchers; caches raw JSON to `cache/YYYY-MM-DD/`. |
| `plots.py` | Six figures. Env `PMRW_FIGDIR` sets the output dir. Fixed `SUBCOL` map keeps a subtopic's colour stable across issues. |
| `mktable.py` | Writes `table_rows.tex` (env `PMRW_BUILD`). Owns `ORDER` and `BANDCOL`. |
| `preamble.tex` | Shared design system — palette (Deep/Teal/Sky/Sage/Amber/Clay/Coral/Violet on Paper `#FBF9F5`), `\metric`, `\keybox`, `\band`, `\paperentry`, `\figcap`, `\DIGESTDATE`. **Do not redesign.** |
| `templates/daily.tex` | Daily template (was `digest.tex`). Uses `\FIGDIR`. |
| `build_manifest.py` | Rebuilds `Reports/reports.json` by **scanning** the tree, validates every entry resolves, mirrors to the MINTS site copy. |
| `build/` , `cache/` , `fig/` | Untracked working dirs (`.gitignore`). |

---

## Run order

1. `git pull --rebase origin main`; read `state/last_run.json`.
2. `python3 harvest.py <window_start> <window_end> <issue_date>` — entry window is
   `last_entry_date + 1 → today`. Never leave a gap.
3. Screen; dedup against `state/seen.json` **before** summarising; log exclusions to
   `state/rejected.jsonl`.
4. Write the day's records with `corpus.save(date, papers, effects, entry_window)`.
5. `PMRW_DATE=<date> PMRW_FIGDIR=fig/<date> python3 plots.py`
   and `PMRW_DATE=<date> PMRW_BUILD=build python3 mktable.py`.
6. Author `build/digest.tex` from `templates/daily.tex`; two `pdflatex` passes;
   render pages with `pdftoppm` and **look at them** before shipping.
7. Copy to `Reports/daily/PM-Research-Watch_<date>.pdf`.
8. Append to `state/seen.json` and `state/metrics.csv`; update `state/last_run.json`.
9. `python3 build_manifest.py` (rebuild + validate + mirror).
10. Commit and push. Never force-push. On rebase conflict: prefer remote for site
    files, keep both sides under `Reports/`; on failure write `state/last_error.log`
    and report rather than push a broken tree.

Rollups (`weekly` every Sunday, `monthly` last Sunday of month, `yearly` last Sunday of
December) aggregate `state/corpus/*.json` and `metrics.csv` over the period via
`PMRW_START`/`PMRW_END`. **They never re-query the APIs**, and they are idempotent —
skip if the output file already exists.

---

## Source notes (state of the world, 2026-07-28)

- **PubMed E-utilities** — the reliable spine. Window on `[EDAT]`. Does *not* index
  `Atmos. Meas. Tech.` or `Atmos. Chem. Phys.`, so pure instrumentation work is invisible here.
- **Europe PMC** — `CREATION_DATE:[a TO b]` works and surfaces preprints PubMed misses.
  `FIRST_PDATE` does not work for recent windows.
- **Crossref** — `from-index-date` is **unusable** for entry-date windowing: Crossref
  re-indexes historical records continuously, so the filter returns works from 2007 onward.
- **OpenAlex** — `from_created_date` / `to_created_date` now return
  HTTP 403 *"Plan upgrade required"*. **This leg of the pipeline is broken** until a free
  alternative is found (candidate: date-of-publication filter + local recency screen).
- **arXiv** — the unfiltered relevance query works; `submittedDate:[...]` range queries
  returned an empty body on 2026-07-28. Needs revisiting.
- **Google Scholar** — no API, blocks scripted access. Supplementary web sweep only.

---

## Run log

### 2026-07-28
- Executed the one-time **Step 0 migration**: `state/` created (corpus store, `seen.json`
  seeded with all 33 records from the 27 Jul issue, `last_run.json`, `metrics.csv`,
  `rejected.jsonl`); `corpus.py` rewritten as a loader; `digest.tex` → `templates/daily.tex`
  with a `\FIGDIR` hook; `.gitignore` added; `build_manifest.py` written; this file created.
  Proofing debris (`pg-*.png`, `prev2/`–`prev6/`, `__pycache__/`, `digest.{aux,log,out}`,
  `l2.txt`, `log2.txt`) **could not be deleted** — the mount is delete-restricted in the
  automation sandbox — so it was untracked with `git rm --cached` and is now gitignored.
  Delete it manually on a local checkout.
- Window searched: PubMed `[EDAT]` 2026/07/28; Europe PMC `CREATION_DATE` 2026-07-26…28.
- Found 21 candidates → **19 included**, 2 rejected (deep-mine battery-fleet review;
  water-transparency review). 5 Europe PMC hits dropped by the dedup key as already
  published on 27 Jul.
- Rollups produced: **none** (28 Jul is a Tuesday).
- `plots.py` patched for correctness, not redesign: data-driven forest-plot x-limits
  (all estimates lie in 1.03–1.09 and were unreadable on the hardcoded 0.97–10 axis),
  whiskers suppressed where no CI was reported, legend restricted to metrics present,
  `f6` life-course counts made data-driven via a `LIFECOURSE` key, fixed `SUBCOL` map so a
  subtopic keeps its colour across issues, and tolerant fallbacks in the
  `design_group` / `geo_group` lookups.
- Broke: OpenAlex created-date filter (now paid); arXiv date-range query (empty body).
  Both documented above; neither blocked the issue.
