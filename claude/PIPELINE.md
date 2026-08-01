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
| `check_dois.py` | **DOI gate**, run automatically by `run_all.py --post`. FAIL (blocks build): no DOI, DOI disagrees with the PMID's own PubMed record, DOI does not resolve. warn (advisory): low title overlap, or not in Crossref but live at doi.org. |
| `issues/digest_YYYY-MM-DD.tex` | **Tracked archive** of each published issue's source, written by `--post`. `build/` is scratch and is overwritten every run. |
| `build/` , `cache/` , `fig/` , `rebuild/` | Untracked working dirs (`.gitignore`). |

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
- **Push failed**: the scheduled-run sandbox has no GitHub credentials (HTTPS remote,
  no helper, no `~/.ssh`, no `GH_TOKEN`). Commit `8259319` is on `main`, rebased onto
  an up-to-date `origin/main`, and needs a manual `git push origin main` from a local
  checkout. Details in `state/last_error.log`. Also note the repo mount is
  **delete-restricted** (`rm` → EPERM, `mv` works), so git's `index.lock` must be
  renamed away between operations; stray `.git/lk.*` files are leftovers of that.

### 2026-07-29
- Window: PubMed `[EDAT]` 2026/07/29 (health axis 18, sensing axis 1 — the sole sensing hit
  was an off-topic Li-ion battery paper); Europe PMC `CREATION_DATE` 2026-07-29 → 1, already
  in the PubMed set. OpenAlex created-date filter now **429 then 403** — still broken.
  arXiv relevance query returned 60 entries, **none submitted on/after 2026-07-20**, so it
  contributed nothing; its date-range parameter remains unusable. 8 instrumentation/modelling
  records added from a **Consensus** sweep (no entry-date filter exists there, so they are
  dated by DOI registration 2025-11…2026-06 and are flagged as a *backfill* in the issue);
  DOIs resolved via Crossref bibliographic query. **25 included, 3 rejected** (battery
  ultrasonics; workshop proceedings; one IoT paper with no retrievable abstract).
- Fixed the documented `metrics.csv` defect: now written by `csv.writer`, existing rows
  rewritten from the corpus store, and a new `update_state.py` owns seen/metrics/last_run
  so step 8 is deterministic rather than hand-done.
- Correctness fixes, no redesign: `plots.py` forest plot crashed on `lo`/`hi` = None (first
  record without a reported CI) — guarded; f3 panel spacing widened (right panel's y-labels
  were overprinting the left panel's value labels); `geo_group` gained South Africa and
  Mexico, which were silently counted as "Global / multi-region". `preamble.tex`
  `\paperentry` now `\detokenize`s the DOI it displays — two DOIs today contain underscores
  and broke the build. `run_all.py` now always repoints `build/fig`; the stale symlink was
  compiling the 28 Jul figures into the 29 Jul PDF. `build_manifest.py` mkdir -p's the
  rollup folders and `.gitkeep` files were added.
- Rollup groundwork done ahead of the first Sunday: `templates/weekly.tex` derived from
  `daily.tex` (trend/inflection, emerging vs. fading, pooled forest with heterogeneity
  stated, author clusters, most-cited, trial watch, gaps, direction) plus `plots_weekly.py`
  for `w1_subtopic_trend` from `metrics.csv`. Test compile clean, 10 pages — **2026-08-02 is
  unblocked**.
- Trial watch: 1 registration updated in 2026-07-23…29 — NCT05874479, 440-participant
  sham-controlled portable-air-cleaner BP trial (NYU Langone). Logged to `state/trials.json`.
- Proofed all 11 pages as rasters: 0 LaTeX errors, 0 overfull boxes. Two defects found and
  fixed on the second pass — an f2 caption that said 8 records had no health endpoint when
  the figure showed 9, and the f4 caption orphaned onto the next page away from its figure.
- **Push succeeded** this run (`bd81530..aba4871`); the remote now carries a PAT, so the
  28 Jul credential failure is resolved and that commit went up too. Verified: `origin/main`
  == HEAD, live `reports.json` and all three daily PDFs return 200, and the 29 Jul entry was
  traced through `index.dc.html`'s own `parse()` to iso 2026-07-29 with a resolvable `src`.
  Chrome extension was not connected, so the calendar check was contract-level, not visual.
- Two PubMed records carry wrong DOIs upstream (PMID 42521969 → a 2019 *Sci Rep* DOI;
  PMID 42524698 → an *Environ Sci Technol* DOI). Reproduced as indexed and flagged in the
  issue; those two links misresolve.
- Sandbox debris for manual cleanup on a local checkout: `.git/lk.*` (6) and
  ~68 `.git/objects/*/tmp_obj_*`, all left by the delete-restricted mount (`rm` → EPERM).
  Harmless to git, but they accumulate every run.

### 2026-07-30
- Window 2026-07-30 (contiguous with 29 Jul). Hits: PubMed health 16, PubMed instrumentation 66,
  Europe PMC 5 (3 dupes, 2 new preprints), arXiv 60 (none in window), OpenAlex HTTP **429**,
  ClinicalTrials.gov 0. **18 included, 11 rejection groups logged.** Rollups: none (Thursday).
- **Consensus cannot supply a windowed record and this is now a known defect, not a workaround.**
  It has no entry-date filter: all 8 low-cost-sensor hits resolved via Crossref `created` to
  20 Jan–6 Jul 2026, and `10.1080/02786826.2026.2676293` (Ginsburg) was already in the 29 Jul
  issue. All 8 rejected. **The pipeline has no date-windowed channel into AMT/ACP.** Fix next
  run: a Crossref `/journals/{issn}/works?filter=from-created-date` feed for AMT (1867-8548) and
  ACP (1680-7324) — per-journal `created` windowing works even though the global `from-index-date`
  does not (see Source notes). Until then the SENS subtopic will keep under-counting.
- Rule adopted: **never mint a DOI.** Consensus returns no DOI field, so every non-PubMed record
  must be resolved through `api.crossref.org/works?query.bibliographic=` before it is written to
  the corpus. Drafting this issue produced 8 plausible-looking fabricated DOIs before that check
  caught them.
- Correctness fixes, no redesign: `plots.py` `design_group` gained Cross-sectional imaging,
  Time-series, Physical exposure model, Machine-learning model, Source apportionment,
  Sensor co-location, Chamber sensor evaluation; `geo_group` gained Lebanon, Bangladesh,
  Kazakhstan, Greece, Bulgaria, Norway (previously silently "Global / multi-region").
- Proofed all pages as rasters over three passes; final 9 pages, 0 LaTeX errors, 0 overfull boxes.
  Three defects found and fixed: f2 caption claimed 7 endpoint-free records against 5 in the
  figure; `LIFECOURSE` notes were misaligned with the figure's five fixed stage headers (an
  adolescence note sat under "Preconception / in utero"); and the Burden band spilled two lines
  onto an otherwise blank page — resolved by dropping the `\clearpage` before the Neuro band,
  which trimming the entries above it did not fix.
- Note for the 2026-08-02 weekly: `metrics.csv` now has 38 rows across 27–30 Jul and the
  quoting defect stays fixed (`update_state.py` rewrites the whole file via `csv.writer`).

### 2026-07-31 — corrections release (no new harvest)
- Audited all 95 DOIs across the four published issues two ways: PMID→DOI against NCBI, and
  DOI→title against Crossref. **Four broken links found, not the two logged on 29 Jul.**
  PubMed had indexed a wrong DOI at entry time for each; all four have since been corrected
  upstream. Title, journal and author were correct in every case — the link alone was wrong.

  | Issue | Record | Was | Now |
  |---|---|---|---|
  | 28 Jul | Sun (PMID 42509466) | `10.1016/j.lanwpc.2024.101106` | `10.1038/s41416-026-03555-2` |
  | 29 Jul | Patton (42521969) | `10.1038/s41598-019-44409-3` (dead) | `10.1007/s11356-026-38083-2` |
  | 29 Jul | Rusconi (42524698) | `10.1021/acs.est.2c06752` | `10.1029/2025GH001636` |
  | 29 Jul | Mokoena (42524488) | `10.3390/ijerph23020182` | `10.1002/puh2.70325` |

  Mokoena was **not** in the 29 Jul run log — that issue's provenance box claimed two bad
  DOIs when there were three.
- The two `10.3760/cma.*` DOIs flagged by Crossref are **not** errors: CMA journals are not
  Crossref-registered but resolve 200 at doi.org. Three low-title-overlap flags are
  paraphrase, not error. Hence FAIL/warn severity split in `check_dois.py`.
- **The 29 Jul `.tex` had been lost** — `build/` is gitignored and gets overwritten each run,
  so the only surviving copy of a published issue was the PDF. Reconstructed the source from
  `pdftotext` output, then verified by word-level `difflib` against the original PDF: the only
  differences are the 3 DOIs and the rewritten correction paragraph. All 25 summaries and every
  caption are word-identical. 28 Jul rebuilt from its `.bak` (5-line diff, all intended).
- Both issues reissued at 11 pages, 0 overfull boxes. Hyperlink **annotations** verified by
  `qpdf --qdf`: 19 and 25 links, 0 stale, corrected targets present. A correction note was
  added to each provenance box rather than silently swapping the links.
- Hardening so this cannot recur: (1) `check_dois.py` now gates `run_all.py --post`;
  (2) `--post` archives `build/digest.tex` to tracked `claude/issues/`; (3) all four existing
  issues back-filled into `issues/`. Current state: **0 FAIL, 5 advisory warns** across
  27–30 Jul.

### 2026-08-01
- Window **2026-07-31 -> 2026-08-01** (two days: 31 Jul was the corrections release and
  carried no harvest). Hits: PubMed health 13, PubMed instrumentation 9 (2 new),
  Europe PMC 2 (both new), arXiv 146 kB none in window, OpenAlex HTTP **429** again,
  ClinicalTrials.gov **1** update. **24 screened, 15 included, 9 rejected**, 0 dupes.
- Rejections were mostly query recall noise, and are named in the issue rather than
  hidden: 4 non-particulate occupational/clinical, 3 air-pollution-as-a-mention documents,
  1 heat-mortality paper with PM as covariate, 1 e-cigarette aerosol study excluded as
  engineered rather than ambient/combustion PM (**a scope boundary, flagged for review**).
- **Sensing = 0 for the second consecutive window.** Still the AMT/ACP channel defect
  logged on 30 Jul, not a real absence. Crossref by-journal `created` feed remains the fix.
- **`templates/weekly.tex` already existed** (written 29-30 Jul, git-tracked, all 8 rollup
  sections) — the task-file warning was stale. The real gap was that `run_all.py` had **no
  rollup path at all**. Added `--rollup {weekly,monthly,yearly}`: idempotent on the output
  PDF, `mkdir -p`s the cadence dir, derives the period start from the period-end date,
  runs `plots.py` + `plots_weekly.py` + `mktable.py` under `PMRW_START`/`PMRW_END`, two
  pdflatex passes, archives to `issues/`, rebuilds the manifest. Never queries an API.
  Smoke-tested the whole pooled path over 27 Jul–2 Aug: 110 rows, w1 trend figure written,
  5 issues aggregated. It correctly refuses until `build/weekly.tex` is authored.
- `plots.py` correctness only: +4 design labels (Proxy validation vs personal exposure,
  Exposome-wide association, Case-control, Ex vivo perfused organ) and +3 geographies
  (Taiwan, Czech Republic, Gambia/Kenya/Mozambique) that were silently falling through.
- `state/trials.json` seeded with its first record (NCT05160948) for the weekly watch.
  `metrics.csv` rewritten by `update_state.py` — 46 rows, quoting still correct.
- Proofed all 9 pages as rasters. 0 LaTeX errors, 0 overfull boxes. Two defects caught and
  fixed before shipping: the f2 caption claimed two "no health endpoint" records against
  one in the figure (Park is labelled *Microenvironment*), and the provenance box claimed
  ClinicalTrials.gov returned nothing when it had returned NCT05160948. Reissued.

### 2026-08-01b — July monthly (user-requested; breaks the rollup contract deliberately)
- Daily coverage of July existed only for 27--30 Jul, so **1--26 Jul was harvested fresh**
  rather than aggregated: PubMed `[EDAT]` 2026/07/01--07/26, health 352 + instrumentation 53
  = 368 unique, 22 already in `seen.json`, **166 passed a PM-relevance title screen, 51
  selected** for full classification into `state/corpus/2026-07-26.json` (`backfill: true`).
  Pooled month = **146 records, 54 effect estimates, all 10 subtopics**.
  Output: `Reports/monthly/PM-Research-Watch-Monthly_2026-07-31.pdf` (14 pp), dated to the
  31st per request rather than the last-Sunday convention.
- **The month refutes the daily Sensing=0 finding.** Sensing is the *largest* subtopic at
  23/146 against 0, 0, 1 and 6 in four consecutive daily issues. The narrow daily windows
  were under-recovering; this is now measured, not suspected. The 23 is a floor, not a
  prevalence — the backfill was a curated sample and preferentially retained sensing work,
  which is stated in the issue's provenance box.
- `update_state.py 2026-07-26` **regressed `last_entry_date` to 2026-07-26**; restored to
  2026-08-01 by hand. Any future backfill must restore the frontier or the next harvest
  will re-scan a month. Worth a guard in `update_state.py`.
- Three correctness fixes, no redesign. (1) `corpus.py` now **pools `LIFECOURSE` over a
  date range** (`_lifecourse_range`) — previously a rollup silently fell back to one
  issue's annotations, so the July f6 was showing 27 Jul's life-course data under a caption
  claiming the month. (2) `plots.py` figure titles are period-aware ("the period's" vs
  "today's") instead of hardcoding "today". (3) **`f5` forest height now scales with N** —
  at 54 estimates the fixed 4.6in canvas collapsed every label into an unreadable smear;
  now ~0.26in/row to a 15.5in cap with a smaller font above 20 estimates.
- Also fixed while proofing: an orphan page where the exec brief spilled two lines before a
  `\clearpage` (same defect class as 30 Jul). Proofed all 14 pages; 0 errors, 0 overfull.
- `templates/monthly.tex` created from the shipped July issue as the exemplar.
- **Correction inside the same run.** The first monthly build asserted "the 30 July and
  1 August issues each recorded zero sensing records" and, in the gaps box, "0, 0, 1 and 6
  across four consecutive daily issues". `state/metrics.csv` says the true series is
  **2, 2, 6, 1, 0** across 27--30 Jul and 1 Aug (11 records). Both passages were rewritten
  against `metrics.csv` and the issue reissued before the run closed. Lesson worth keeping:
  **derive any cross-issue count from `metrics.csv`, never from memory of the prose** ---
  the headline (23 for the month vs 11 across the dailies) survives and is still decisive.

### 2026-08-01c — scheduling correction: the daily is re-cut as the **31 July** issue
- **Defect.** The 1 Aug run harvested a two-day window (31 Jul--1 Aug) because 31 Jul had
  been a corrections release, and published the result as the **1 August** issue. Wrong on
  both counts: papers entering PubMed on 1 Aug belong to the 1 Aug 23:00 run, and 31 July
  was left with no report at all.
- **Fix.** Every record's PubMed `entrez` entry date was fetched and the window re-cut:
  **9 records EDAT 2026-07-31**, **4 records EDAT 2026-08-01**, 2 Europe PMC records with
  earlier PubMed EDATs (Knapova 8 Jul, Balu 21 Jul) that only the EPMC `CREATION_DATE`
  window surfaced. The 2 EPMC records are dated to the 31 Jul issue and the non-uniform
  window is stated in the issue rather than hidden. Result: **11-record 31 July issue**,
  8 effect estimates, 8 pp, 0 overfull. Every retained summary is byte-identical to its
  original text --- entries were extracted verbatim from `issues/digest_2026-08-01.tex`,
  not re-authored.
- The 4 deferred records were **removed from `state/seen.json`** (12 keys) so tonight's run
  re-finds them, and stashed to `state/deferred_2026-08-01.json` for reconciliation.
  `last_entry_date` is back to **2026-07-31**, so the 23:00 window is 2026-08-01 alone.
- `Reports/daily/PM-Research-Watch_2026-08-01.pdf` withdrawn (moved to `build/trash/`),
  manifest rebuilt: dailies now 27--31 July, contiguous, no 1 Aug entry.
- **The July monthly was rebuilt** because it now contains the 31 July issue:
  146 -> **157 records**, 54 -> **62 effect estimates**, China 44 -> 49, and the sensing
  series is now wholly inside July (2, 2, 6, 1, 0 on 27--31 July, 11 total against 23 for
  the month). All dependent counts in the monthly prose and captions were updated.
- **Rule to carry forward:** a daily issue's window is `last_entry_date + 1 -> today`, but
  "today" for a 23:00 run means *that day's* entries only. Never publish an issue dated
  later than its newest entry date, and never let a two-day window silently absorb the
  next run's material.
