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

### 2026-08-01d — July monthly expanded to a complete listing, figures rebuilt
- **The register is now every PM-relevant July record, not a curated sample.** The 1--26 Jul
  backfill went from 51 selected to **all 164**: abstracts fetched for the remaining 115,
  rule-classified, then **every one reviewed by hand — 43 of 113 auto-assignments (38%) were
  corrected**, and 2 were rejected on reading as water-phase chemistry (stream sediment;
  antibiotic sorption to dissolved black carbon). **July total: 270 records, 62 estimates.**
  The classifier's own bugs are worth recording: `trial` matched inside *indus**trial***,
  and atmospheric-chemistry and plant/insect work fell through to "Other clinical endpoints".
- **Paper-level digest added** (`mkdigest.py`, wired into `--rollup`). Two tiers, visually
  distinct: 106 records keep their **verbatim** daily summary lifted from the archived
  issue `.tex`; 164 get an **extractive precis** — the single most quantitative sentence of
  the abstract, copied, never paraphrased — and 5 with no abstract are listed on metadata.
  The distinction is stated in the section header, not buried.
- **Figures rebuilt for legibility at rollup scale** (`BIG`/`FS`/`SZ` in `plots.py`):
  canvas +30/55%, fonts +35%, dpi 240. Specific fixes: endpoint labels **canonicalised**
  (Cognitive / Neurological / Neuro-cognitive had drifted into three bars), f2 height now
  scales with category count, the **forest split across two pages** at 32 rows each with
  row pitch raised 0.30→0.55 in/row and y-labels clipped (long labels were inflating figure
  width under `bbox_inches="tight"`, which then scaled the whole panel back down), and each
  analytics figure gets its own page capped at 0.70--0.78 `\textheight`.
- **`w1` replaced.** A stacked per-issue bar is meaningless when one "issue" is a 164-record
  batch and the rest are 11--33-record days — every segment became a stripe. It now plots
  *what the daily cadence missed*, per subtopic: dailies caught 106, missed 164 (**61%**).
- Escaping bugs fixed in `mkdigest.esc`: HTML entities were being LaTeX-escaped *before*
  decoding (`&#x2264;` → `\&\#x2264;`), `<`/`>` were set as raw text, and sub/superscript
  unicode from PubMed crashed the build with 20 errors. Also made DOIs breakable
  (`\allowbreak`) and `\precisentry` unbreakable (a minipage) after a stranded DOI page.
- Final: **46 pp, 0 LaTeX errors, 0 overfull boxes, 0 sparse pages, all 270 DOIs present.**

### 2026-08-01 — the sensing leg is built; first weekly ships
- **Window** 2026-08-01 (PubMed `[EDAT]`, Europe PMC `CREATION_DATE`), contiguous with 31 Jul.
  PubMed 11 in window / 5 retained; EPMC 2, both duplicates of the 31 Jul issue; arXiv 1,
  rejected (no PM application); OpenAlex still 403. **25 records in scope, 15 rejected with
  a logged reason.**
- **The prescribed fix works.** `harvest.crossref_journal` / `crossref_sensing` window
  Crossref `created` **per journal ISSN** over 8 titles (AMT, ACP, AS&T, Atmos Environ,
  J Aerosol Sci, Atmos Pollut Res, AAQR, ES:Atmos). A *global* `from-created-date` is
  useless; scoped to one ISSN it returns that journal's genuine new deposits. First run
  back-swept 26 Jul–1 Aug: **55 deposits, 12 PM-relevant, all 12 carried** (4 with
  abstracts, 8 metadata-only — Elsevier deposits no abstract to Crossref and these are not
  yet in EPMC/PubMed, so they are listed on metadata and explicitly *not* summarised).
  **Sensing went 0, 0, 1 → 9.** Consensus added 8 more (2 dropped as 29 Jul duplicates).
- **First weekly**: `Reports/weekly/PM-Research-Watch-Weekly_2026-08-01.pdf`, 14 pp.
  Cadence is Sunday→Saturday and is generated on **Saturday's run**, so it lands on the
  same calendar cell as that day's daily. **Pooled window is 27 Jul–1 Aug, not 26 Jul**:
  the `2026-07-26` corpus slot holds the 1–26 Jul retrospective backfill (164 records) and
  pooling it would put a month inside a week and double-count the July monthly. Stated in
  the issue, not hidden. `run_all.rollup` now honours `PMRW_START_OVERRIDE` for exactly
  this case.
- **Three figure defects found by proofing, all fixed in `plots.py`/`plots_weekly.py`:**
  (i) every instrumentation design string fell through to "Other / mixed", collapsing the
  architecture donut to one slice — 20 design mappings added plus an honest `Metadata only`
  bucket; (ii) f2's right-panel y-labels ran over the left panel's legend once an endpoint
  label was long — `wspace` now scales with the longest label; (iii) `w1` was hard-wired to
  the monthly "what the dailies missed" framing and showed an all-zero series for a week —
  it now switches to a per-issue line trend, with issue size on a twin axis, when the range
  is ≤10 issues and contains no backfill batch.
- Trial watch +3 sham-controlled filtration RCTs (NCT05867381, NCT05718245, NCT05016271);
  NCT05016271's primary completion was **June 2022 with no results posted**.
- Daily 11 pp, weekly 14 pp, **0 overfull boxes, 0 sparse pages, all DOIs resolved.**
- Carry forward: `state/` has no ORCID or affiliation field, so author-cluster analysis in
  the rollups degenerates to surname frequency (Chen 5, Zhou 5 — distinct groups). The
  weekly says so rather than reporting the noise; a schema change is the real fix.

### 2026-08-02 — the rollup digest becomes a contract; weekly layout rebalanced
Four fixes, all upstream of the one issue that exposed them.

- **`mkdigest.py` now serves every cadence.** It read a hand-built
  `cache/2026-07-monthly/daily_summaries.json`, so it only ever worked for July 2026.
  It now builds its index by **parsing `issues/digest_*.tex` inside the window**
  (`harvest_summaries`, brace-aware `_args`), which means any rollup — including ones that
  do not exist yet — gets verbatim full summaries for free, and a rollup can never quote a
  summary that was not actually shipped. `WITHDRAWN` issues are skipped. The July cache is
  kept as an overriding overlay so that monthly reproduces unchanged. Tier label is now
  cadence-neutral ("Not carried by a daily issue"), not "month-wide harvest".
- **The paper-level digest is now mandatory in `templates/weekly.tex` and
  `templates/monthly.tex`.** A rollup that only tabulates its records is a table of
  contents. The weekly carries 123 full summaries + 8 metadata-only across 131 records.
- **`\subsectionnote` and `\precisentry` moved into `preamble.tex`.** They were defined
  locally in `build/monthly.tex`, so the first weekly to use the digest failed with 40
  undefined-control-sequence errors. Related and worse: **`run_all` only copied
  `preamble.tex` into `build/` if it was absent**, so the fix was invisible to the build —
  a stale scratch copy silently compiled the old design system, exactly the failure class
  the stale-`fig`-symlink guard already existed for. It now always refreshes.
- **Figures.** (i) `w1`'s subtopic lines were completely hidden: a twin axis is created
  after its parent and draws over it, so `zorder` inside `ax` cannot beat artists in
  `ax2` — fixed by lifting the line axes above the bar axes and making its patch
  invisible, plus `alpha=0.55` on the bars. (ii) `plots.py` now also emits
  **`f2a_architecture.png` (wide/short) and `f2b_endpoint.png`** as separate panels; the
  combined `f2` is squeezed at rollup scale. The weekly puts the architecture donut in the
  whitespace under the trend text and gives the endpoint bars a full-width slot with `f1`.
  Both templates carry the placement rule as a comment so it survives.
- Weekly: **30 pp, 0 LaTeX errors, 0 overfull boxes**, no page given over to a single
  figure.

### 2026-08-02 — instrumentation backfill, two silently worthless figures, and an EDAT split
Window **2 Aug alone** (Sunday), contiguous with 1 Aug. **31 records, 4 rejected, 1 held back.**

- **Date correction, and the rule it establishes.** This issue was first built and pushed
  as `2026-08-03` because the harvest window was `last_entry_date+1 → today` = 2–3 Aug and
  the issue was dated to the query window's end. That is wrong when the run happens early
  in the day: it consumes tomorrow's entry date. **An issue must be dated to the entry date
  its records actually carry, and the harvest split on the per-record `[EDAT]` value, not
  on the query window.** Reading `PubmedData/History/PubMedPubDate[@PubStatus="pubmed"]`
  (*not* `entrez`, which runs a day earlier and does not match what `[EDAT]` filters on)
  showed **18 of 19 retained PubMed records at 2 Aug and exactly one at 3 Aug**. The issue
  was re-dated to 2 Aug, Nimmala et al. (PMID 42543389) was pulled and logged to
  `rejected.jsonl` as **`HELD BACK`** rather than as a rejection, and `last_entry_date` set
  to `2026-08-02` so the 3 Aug run picks it up. The withdrawn 3 Aug PDF, its mirror and its
  `.tex` were moved to `claude/build/trash/` (mount is delete-restricted).
- **Source counts.** PubMed connector 21 on the health axis vs **14 from the local
  harvester** on the same window — the connector is the better recall leg and both are
  worth running; instrumentation axis 2, both already in the health set; union 23, 19
  retained, 18 carried. Europe PMC 0. Crossref by-journal 1 (Lu, *Atmos Environ*,
  `created` 2 Aug, metadata-only). arXiv 0 inside the recency screen. **OpenAlex returned
  HTTP 429** on top of the standing paid-plan block — leg stays dead. Consensus ×4 sweeps
  returned **12**, all new.
- **The Consensus records are Jan–Jun 2026 publications, not 2 Aug entries.** A single
  Sunday on a literature PubMed does not index would have shipped an empty sensing section.
  They are carried, dated to this issue, and **labelled in the masthead, the f1 caption and
  the provenance box as a backfill** so no trend line through 12 sensing records is read as
  a one-day flux. **The next weekly must not treat it as one.**
- **`plots.py` design map was still incomplete and it cost two figures.** The 1 Aug fix
  covered the instrumentation designs that existed then; eleven more fell through here, so
  the architecture donut *and* the f4 heatmap both collapsed to a single "Other / mixed"
  column. Caught only by looking at the rendered page. Eleven mappings added plus two new
  groups (`Tool / software`, `Chamber / laboratory`); endpoint canon gained
  `None (monitoring)`, `Epigenetic ageing`, `Toxicological (in vitro)`, collapsing a
  17-bar endpoint panel to 6. **Any issue that introduces new `design` strings must be
  re-proofed at the figure, not just at the DOI gate.**
- **The forest plot was dropped, deliberately.** The window's only CI-bearing estimate is
  Thies et al.'s 1.93 percentage-point *survival difference*; on the log-ratio axis the
  null line at 1.0 falls inside its interval and it reads as a non-significant risk ratio.
  Replaced with a keybox stating that no ratio-metric estimate was reported and why.
  `EFFECTS` is `[]` for this date — `plots.py` writes no `f5_forest.png`, so the
  `\includegraphics` must be removed from the template too or a stale figure compiles.
- **Author attribution defect found before shipping.** First-author surnames were initially
  inferred rather than read; **16 of 19 were wrong**. Now taken from the `efetch`
  `AuthorList`. **Verify `short` against efetch every run.**
- Trial watch +14 (incl. NCT06376994, 770-participant multi-centre sham-controlled COPD
  air-cleaner RCT; NCT06070428, n=400 heart failure; NCT07536178/NCT06749093 controlled
  woodsmoke chambers). Surfaced in the weekly.
- Daily 11 pp, **0 LaTeX errors, 0 overfull/underfull boxes**, all DOIs resolved (6
  advisory paraphrase warnings). `metrics.csv` quoting confirmed correct — defect closed.
- **For the 3 Aug run:** window is `2026-08-03 → 2026-08-03`; Nimmala et al. is a known
  held-back record, not a gap; run Consensus on *different* axes (mobile/personal
  monitoring, source apportionment, drift over multi-year deployment) since the calibration
  and satellite-fusion axes were swept dry today.

### 2026-08-03 — geography map fall-through, a DOI I had to reject as my own fabrication
Window **3 Aug alone**, contiguous with 2 Aug. **25 records, 11 rejected, 2 of those duplicates.**

- **Source counts.** PubMed connector 11 health / 6 instrumentation (5 already in health), union
  12, **10 carried**; the local harvester found 12 on the health axis but 0 on sensing — the
  connector remains the better recall leg on both. Europe PMC 5 → 1 unique preprint.
  **Crossref by-journal 5 (all ACP/AMT, all carried)** — the single most productive leg this run
  and none of it visible to PubMed. arXiv 1 in-screen. **OpenAlex HTTP 429** on top of the
  paid-plan block; leg still dead. Consensus ×4 sweeps on the axes the 2 Aug log prescribed
  (drift, network apportionment, mobile/hyperlocal, personal) returned 8 new — but the free
  tier now **caps at 3 results per sweep**, which is the binding constraint on the sensing leg.
  Nimmala et al. picked up as planned from the 2 Aug hold-back.
- **`harvest.py` cannot be backgrounded from a tool call.** `nohup ... &` dies when the bash
  call returns (each call is its own sandbox), so it was killed mid-`crossref_sensing` and
  wrote a *stale* `crossref_journals.json` from the previous day. Caught because the file
  mtime did not move. Run the legs synchronously in chunks under the timeout, and **check
  cache mtimes against the run, not just file existence.**
- **`geo` was an exact-string lookup and 20 of 25 records fell through to
  "Global / multi-region".** Records carry free text ("Chiang Mai, Thailand", "Ile-Ife,
  Nigeria"), so f3's right panel was a single bar — same failure class as the design-map
  fall-through fixed 01–02 Aug, and again caught only by looking at the rendered figure.
  Resolution is now **exact → alias → substring**, with a `GEO_NONGEO` list so chamber/method
  labels land in the fallback *by intent*, and **anything still unresolved is printed** so the
  next unmapped place is visible in the run log. Backfilled the places this surfaced in the
  31 Jul – 2 Aug issues (Hong Kong, Finland, Northern Ireland, Sofia, Antwerp/Oslo/Zagreb,
  "Multi-country", chamber labels) — those issues had the same silent collapse and the fix
  improves the pending weekly/monthly rollups, not just today.
- **I fabricated a DOI and the gate caught it.** PMID 42544279 (Canadian wildfire PM2.5)
  carries a PMC id only; I guessed `10.60787/nmj.v67i1.783` from the journal prefix. It 404s,
  the NCBI ID converter returns no DOI and Crossref does not know the title. **Record dropped
  and logged, not shipped.** Rule: a DOI is *read* from efetch or Crossref or the record does
  not ship — never inferred from a journal's prefix pattern.
- **`EFFECTS` empty for a second consecutive day.** No ratio-metric estimate with a CI exists in
  the window; the strongest numbers are R² goodness-of-fit. Forest plot omitted and replaced
  with a keybox that says so. Do not let a rollup read two empty days as a data-loss bug.
- **Orphan pages.** The exec-brief spilled one line onto p2 and the final entry's DOI orphaned
  onto a page of its own — twice, through two rounds of prose-shaving. Fixed with
  `\enlargethispage{3\baselineskip}` before the last `\paperentry`: **pull the page down
  rather than shave prose until it happens to fit.** Final: 10 pp, 0 errors, 0 overfull.
- **`trials.json` has meta keys (`trials`, `windows`) alongside legacy top-level NCT records.**
  A naive list/dict normalisation flattened NCT05874479 and dropped `first_seen`/`note`;
  reverted and re-applied against the real schema. `git checkout` cannot restore a file on this
  mount (`unlink` EPERM) — restore by writing `git show HEAD:<path>` back in place.
  Trial watch: 2 updates, 1 new to state, 0 new interventional → `analyze_endpoints` not run.
- **For the 4 Aug run:** window `2026-08-04 → 2026-08-04`. **`templates/weekly.tex` exists and
  the Sat 8 Aug run owes a weekly for 2–8 Aug** — it must exclude the 2 Aug and 3 Aug sensing
  backfills from any trend line (both are dated, not entered, in their windows). Authenticate
  Consensus before the next backfill or the sensing leg stays capped at 3/sweep.
- **Step 9 verified over HTTP, not visually.** The Claude-in-Chrome extension was not connected
  on this run, so the calendar cell could not be eyeballed. Verified instead by fetching
  `Reports/reports.json` (8 daily entries, 2026-08-03 newest) and the live PDF itself (renders,
  10 pp, correct masthead) from `mi3nts.github.io`. **GitHub Pages served a cached manifest for
  ~1 min after the push** — the first fetch was missing 2026-08-02; a cache-busted query string
  returned the correct file. Do not treat the first post-push fetch as authoritative.
- **Manual cleanup owed:** the delete-restricted mount left ~377 `.git/objects/**/tmp_obj_*`
  files and ~32 moved lock files under `.git/lk/`. All inside `.git`, so untracked and harmless
  to the site, but they accumulate every run and should be cleared from a normal shell.

### 2026-08-04 — issue re-dated from 08-05; design map fell through for *every* record
Window **4 Aug** (issued as `2026-08-04`). The 4 Aug scheduled run never fired, so this run
executed early on 5 Aug and first built as an 08-05 issue over a 4–5 Aug window. **Withdrawn
and re-dated to 08-04 on request**: the 5 Aug run is scheduled for 23:00 the same day, and
per-record dates confirmed the split was unnecessary — every PubMed record carries an Entrez
date of 4 Aug or earlier and all six Crossref deposits a 4 Aug `created` date, so all 13
belong to the 4 Aug issue and none was held for the next. **13 records, 10 not shipped.**

- **Source counts.** PubMed 10 health / 2 sensing (connector and local harvester agreed
  exactly). Europe PMC 2 → 1 carried. **Crossref by-journal 6, all new, 2 carried** — again
  the only leg that sees ACP/AMT. Consensus ×3 sweeps → 3 new after DOI resolution; the other
  6 hits resolved to DOIs already in `seen.json` (Qian AMT, Ginsburg AS&T, Yaqoob IEEE Access,
  both Geo-spat Inf Sci fusion papers, Nguyen Eng Res Express) — **resolving Consensus titles
  to DOIs before screening is what stopped six re-summaries.** OpenAlex still paid-blocked.
- **`seen.json` is nested (`pmid`/`doi`/`tsig`), not flat.** A screening probe keyed on the
  top level reported "3 keys" and looked like total state loss. It was not. State is intact
  (294→303 pmid, 346→359 doi). **Check the level before concluding corruption.**
- **All 13 records fell through to `Other / mixed`.** Third recurrence (01, 02, 03 Aug) of the
  same class, and the root cause is that an unmapped design was *silent* — only a rendered
  donut ever revealed it. Fixed properly this time: added the 11 design labels **and** a
  `_design_unmapped` set with a printed warning, mirroring what GEO already did. Geo also
  surfaced `Arctic Ocean`, `Philippines`, `Computational (no site)`; added a
  `Polar / remote marine` bucket, Southeast Asia entries, and `computational`/`no site`/
  `theoretical` to `GEO_NONGEO`.
- **`state/metrics.csv` quoting defect is already fixed** — 83 rows, 0 malformed under
  `csv.reader`. The naive `awk -F,` check reports false positives on quoted fields; do not
  re-open this.
- **Five records found, verified, and deliberately *not* shipped.** 2×APR, Atmos Environ,
  J Aerosol Sci, IEEE OJ-ITS: DOIs verify in Crossref but no abstract exists in Crossref,
  Europe PMC or Consensus, and Elsevier/IEEE landing pages are client-rendered. Logged to
  `rejected.jsonl` as **held, not rejected**, and kept OUT of `seen.json` so a later issue can
  carry them. Prajapati (PM2.5 hygroscopicity, eastern IGP) is the priority pickup.
- **`\enlargethispage` has a ceiling.** At 4–7 `\baselineskip` it stopped reflowing and started
  **printing text over the folio** — worse than the sparse page it was fixing. Reverted to a
  plain `\clearpage` before the last band. Rule: pull the page down, but *look at the bottom
  margin*; if the last line reaches the page number, take the clean break instead.
- **EFFECTS non-empty but co-pollutant only.** No PM ratio estimate with a CI exists in the
  window (third straight issue). Plotted Russo's O3/NO2 estimates with the caption stating
  plainly that they are not PM, so a rollup cannot read the gap as data loss.
- **Trial watch:** the connector exposes no last-update-date filter, so the sweep is relevance-
  ranked, not windowed. 1 new to state (NCT07111208, MARKOPOLO/METSGREEN, n=180, recruiting);
  `analyze_endpoints` run. Weekly rollup, not daily.
- **Re-dating touches six state files, not one.** `state/corpus/<date>.json` (renamed, with
  `date` and `entry_window` rewritten), `seen.json` (35 values), `metrics.csv` (rewritten via
  `csv.writer`, still 0 malformed), `rejected.jsonl` (10 `issue` fields), `trials.json`
  (window + `first_seen`), `last_run.json`. The masthead, the exec-brief window bullet and the
  provenance box in `digest.tex` all state the window in prose and must be edited too — the
  `--date` flag alone does **not** re-date the issue body. Withdrawn artefacts (`Reports/daily`
  PDF, site mirror, `issues/digest_*.tex`, `fig/<date>/`) were **moved**, not deleted; the
  mount returns EPERM on `rm`. Superseded corpus left as `state/corpus/.withdrawn_2026-08-05.json`.
- **For the 5 Aug run (tonight, 23:00):** window `2026-08-05 → 2026-08-05`; `last_entry_date`
  is now `2026-08-04`. **The Sat 8 Aug run still owes a weekly for 2–8 Aug**; it must exclude
  the 2/3 Aug and the 3 Consensus sensing backfills from any trend line (dated, not entered,
  in their windows). Retry the five held DOIs first.
- Final: **9 pp, 0 errors, 1 overfull hbox of 1.18pt** in a table cell (sub-visual, left).

### 2026-08-05 — sensing is half the corpus; Semantic Scholar added to the abstract retry chain
Window **5 Aug** (`2026-08-05 -> 2026-08-05`), contiguous with 08-04, no gap. **10 shipped,
23 rejected, 7 held.** 7 pp, 0 errors, 0 overfull boxes.

- **Source counts.** PubMed 15 health / 8 sensing after merging connector + local harvester
  (the two disagree in *both* directions — connector missed 42554908 and 42552310, local
  missed 10 others; merging is worth the extra esummary call). **11 PubMed hits rejected
  as off-topic** — the worst health-axis yield to date. Europe PMC 2 → 1 (a medRxiv
  preprint). Crossref-by-journal 7 → 1 carried, 3 out of scope, 3 held. Consensus ×3 →
  **every hit resolved to a DOI created before the window**; 1 backfill carried, 9 rejected.
  OpenAlex now returns **HTTP 429** on top of the paid block.
- **Semantic Scholar Graph is a genuine fourth abstract source.** Retried all five DOIs held
  on 04 Aug across Crossref → Europe PMC → S2; **S2 recovered `10.1109/ojits.2026.3706855`
  (Jafari, IEEE OJ-ITS)** which the other three had failed on for two days. Add it to the
  retry chain permanently. The four Elsevier holds remain unretrievable; 3 new Elsevier/T&F
  holds joined them, so **7 held records now stand** — Prajapati (APR, PM2.5 hygroscopicity)
  still the priority pickup.
- **Design map fell through AGAIN — 4th recurrence, new root cause.** 6/10 landed in
  `Other / mixed` because I wrote **canonical group *values*** (`Modelling / inventory`)
  onto records, and the map only had granular *keys*. Fixed by making `design_group`
  **closed under its own output**: identity self-maps for all 9 group names, plus
  `Spatial analysis / GIS` → Modelling and `Time-series / case-crossover` → Obs-acute.
  Same fix applied to `geo_group` (`East Asia`, `South Asia`, `North America`,
  `Multi-country`). The printed-unmapped diagnostic is what caught it — keep it.
- **A figure caption was wrong until the proof.** Caption claimed "6 of ten carry no health
  endpoint"; the rendered chart said 7. **Read the numbers off the rendered figure, not off
  the corpus you think you wrote.**
- **`\enlargethispage{3\baselineskip}` was the right dose.** 3 lines of the last exec-brief
  bullet spilled onto an otherwise blank p.2. 3 baselines absorbed it cleanly, 8 pp → 7 pp,
  bottom margin re-proofed and clear of the folio. Confirms the 08-04 rule: small doses work,
  4–7 prints over the page number.
- **Unicode in `short` is safe** — `Gäbel & Hertig 2026` renders correctly through
  `mktable.py`. Don't ASCII-fold author names; it desynchronised the register from the body.
- **EFFECTS has one entry and it is a preprint** (7.1%, 95% UI 5.4–8.8, policy-attributable
  fraction — not a concentration–response ratio). 4th straight issue with no peer-reviewed PM
  ratio estimate carrying a CI. Caption states this explicitly.
- **Sat 8 Aug still owes the weekly for 2–8 Aug.** Exclude from trend lines: the 3 Consensus
  sensing backfills of 03/04 Aug and **Gäbel & Hertig (AMT, created 19 Feb 2026)** shipped
  today — dated outside their issue windows.

### 2026-08-06 — CI drought breaks; the geo/design closure fix from 08-05 was only half done
Window **6 Aug** (`2026-08-06 -> 2026-08-06`), contiguous with 08-05, no gap. **27 shipped,
23 rejected, 9 held.** 11 pp, 0 errors, 0 overfull boxes. Widest corpus since 27 Jul.

- **`geo_group` was never closed under its own output — 5th latent recurrence.** The 08-05
  fix self-mapped 9 of 13 `design_group` values and only **4 of 13** `geo_group` values, so
  `Sub-Saharan Africa`, `Global / multi-region`, `Oceania`, `Latin America`,
  `East Asia (ex-China)`, `Middle East & N. Africa`, `Southeast Asia`, `Central Asia` and
  `Polar / remote marine` would all have collapsed to the unmapped bucket. Both maps are now
  closed **generatively** (`m.update({v: v for v in set(m.values())})`) rather than by hand,
  so the closure cannot drift again. Verified 0 unmapped this run.
- **`\enlargethispage` must be read on the page it is meant to enlarge.** Two lines spilled
  onto a blank p.2; placing the macro after `\end{itemize}` did nothing, because TeX reads it
  on p.2 after the break has already happened. Moved **above the exec-brief section heading**
  (still p.1): 12 pp -> 11 pp at 2 baselines, bottom margin re-proofed and clear. Two rounds
  of prose trimming beforehand did **not** converge — the paragraph reflows and re-spills.
- **Source counts.** PubMed connector 20 health / 4 sensing, local harvester 14 / 4; the two
  disagree in **both** directions (10 connector-only, 3 harvester-only) — merging both legs is
  mandatory, not optional. Union 25, 18 carried, 7 rejected (incl. 1 already-shipped dup).
  Europe PMC on `FIRST_PDATE` **and** `CREATION_DATE` — 7 preprints, 5 carried. Crossref by
  ISSN 11 -> 4 carried, 5 out of scope, 2 new holds. Consensus x3 -> **all 9 hits resolved to
  DOIs created Jan-Jun 2026**, none in window, 0 backfilled. OpenAlex HTTP 429 again.
- **First peer-reviewed PM ratio estimate with a CI in five issues**: Jung et al., RA flare
  OR 1.113 (1.017-1.218). Six EFFECTS entries, four of them PM. The drought is over; the
  forest caption still marks the two co-pollutant entries explicitly.
- **efetch DOI parsing bug found and fixed in the ad-hoc merge script.** Taking the *last*
  `ArticleId[@IdType=doi]` in a `PubmedArticle` picks up a **reference-list DOI** — 6 of 25
  records got a wrong DOI (e.g. PMID 42558172 resolved to a Nature news item). Read
  `ELocationID[@EIdType='doi']` first, then `PubmedData/ArticleIdList` only. `check_dois.py`
  would have caught these as FAIL, but the cheaper fix is upstream.
- **Held: 9.** The 7 carried from 4-5 Aug were retried a third time across Crossref, Semantic
  Scholar and Scholar Gateway — all still abstract-less; Scholar Gateway's corpus is current
  only to **May 2026**, so it is not a useful retry source for same-week Elsevier deposits.
  2 new Atmos Environ holds joined. Prajapati (PM2.5 hygroscopicity, eastern IGP) still the
  priority pickup, with Ginsburg et al. (global PurpleAir calibration, AS&T) as the backfill
  candidate if a slot opens.
- **Sat 8 Aug owes the weekly for 2-8 Aug.** Exclude from trend lines: the five PubMed records
  in this issue carrying a 4-5 Aug entry date (re-indexed into today's window, flagged backfill
  in the provenance box), plus the 08-03/08-04/08-05 backfills already noted.

### 2026-08-07 — the CI drought reverses hard; design map falls through for a 6th time
Window **7 Aug** (`2026-08-07 -> 2026-08-07`), contiguous with 08-06, no gap. **26 shipped,
20 rejected, 4 carried on metadata alone.** 10 pp, 0 errors, 0 underfull, 4 sub-visual
1.18 pt overfull hboxes in the masthead metric strip (pre-existing, logged 08-04).

- **Source counts.** PubMed connector 19 health / 17 instrumentation, union 27; **the local
  harvester returned 18 health and 0 sensing** — its sensing query has now produced an empty
  set twice, and the connector is the only working instrumentation leg into PubMed. 1 dup,
  18 carried, 8 rejected. Europe PMC 1, already in the PubMed set. **Crossref by ISSN 10 —
  the most productive sensing leg again**, 6 carried, 4 out of scope. Consensus x3 sweeps
  returned 9 capped at 3/sweep by the free tier; **7 resolved to DOIs already in
  `seen.json`** and 2 were carried as backfill (DeMarsh, Blanco-Villafuerte, Crossref
  `created` Jan–Feb 2026). arXiv 60, none published on/after 1 Aug. OpenAlex HTTP 429 again.
- **All 27 PubMed records carry `PubMedPubDate[@PubStatus="pubmed"]` = 2026-08-07.** No
  record held back, none re-indexed from an earlier window — the first fully uniform EDAT
  window since the split rule was adopted on 2 Aug.
- **`design_group` fell through for 10 of 26 records — 6th recurrence.** The 08-05/08-06 fix
  closed the map under its own output but did not anticipate *new* granular labels, and this
  issue introduced ten (`Burden estimation (GBD)`, `Distributed-lag time-series`,
  `Satellite remote sensing`, `Monitoring-record analysis`, `Sensor deployment (pilot)`,
  `Biomonitoring transplant`, `Cross-sectional survey`, `Toxicological (in vitro)`,
  `Materials / filtration`, `Literature review`). Added; 0 unmapped after the patch, and the
  architecture donut went from 12-in-`Other / mixed` to 8 populated groups. **The printed
  `!! design unmapped` diagnostic is the only thing that catches this — never silence it.**
- **Sixteen effect estimates with intervals, the largest set this watch has carried** (6 on
  08-06, 1 on 08-05). Cause is compositional, not a trend: Cantuaria (COPD, n=159,769),
  Orr (wildfire PM2.5 x influenza, 6 states) and Sassano (Golestan household fuel,
  n=50,045) each report a family of stratified estimates. **Orr's effect boundary coincides
  exactly with the outcome-ascertainment boundary** — positive in the 4 lab-confirmed-
  influenza states, null in NV and *protective* in WA (0.884, 0.842–0.919), the two
  syndromic-ILI states. Flagged in the issue as misclassification, not geography.
- **Jiang's PM10 RR 1.63 (0.18–15.94) deliberately excluded from the forest plot** — the
  interval spans an order of magnitude and compresses every other estimate to a point. It
  stays in `EFFECTS`-adjacent prose and the register, not the figure. Precedent worth keeping.
- **Caption-vs-figure mismatch caught at the proof again**: the f2 caption claimed 12
  endpoint-free records against 14 in the rendered chart. Fixed. **Read counts off the
  rendered figure, not the corpus you think you wrote** — 3rd occurrence.
- **Orphan p.2 did not yield to `\enlargethispage` and needed prose surgery.** 4 spilled
  lines at 2 baselines; 3 baselines left 1 line; the fix that worked was **deleting the
  weakest exec-brief bullet and folding one clause of it into bullet 1**, then trimming 6
  words from the last bullet. 11 pp -> 10 pp. Confirms the 08-06 rule that trimming alone
  does not converge — but deleting a whole bullet does, because it removes the reflow.
- **Four records carried on metadata alone** (Yukhymchuk AAQR low-cost PM sensor performance,
  Zheng *Atmos Environ* winter PM2.5 XAI, Sanders AS&T hygroscopic growth, Huang APR brown
  carbon) — abstract-less across Crossref, Europe PMC and Semantic Scholar. All four are on
  the sensing axis, so **the day's most relevant instrumentation content is un-summarisable**.
  Listed, never summarised from a title. Yukhymchuk is the priority re-check.
- **Trial watch:** 62 returned, **3 new to state** — NCT07479420 (classroom HEPA vs
  ionisation cluster-RCT, n=180: primaries are *air-quality* measurements with health in the
  secondaries, the cleanest filtration->PM->health chain in state), NCT06197477 (Hasselt
  schools, n=900, **four cognitive co-primaries and zero secondaries**, multiplicity
  unaddressed), NCT05994937 (NYU prediabetes PAC, n=150, primary completion 2026-03-16 with
  no results posted). `analyze_endpoints` run on the two new interventional registrations.
- **For the 8 Aug run (tonight):** window `2026-08-08 -> 2026-08-08`; `last_entry_date` is
  now `2026-08-07`. **Saturday 8 Aug owes the weekly for 2–8 Aug** and must exclude from any
  trend line: the 2/3/4/5 Aug Consensus sensing backfills, Gäbel & Hertig (AMT, created
  19 Feb), the five 08-06 records re-indexed from 4–5 Aug, and today's two Consensus
  backfills (DeMarsh, Blanco-Villafuerte). Also carry the four metadata-only sensing records
  forward for an abstract retry.
- **`git commit` is now unusable on this mount and there is a working substitute.** Every
  lock file under `.git/` (`index.lock`, `HEAD.lock`, `refs/heads/main.lock`,
  `packed-refs.lock`) is a stale zero-byte leftover that **cannot be removed** — `rm` is
  EPERM and `mv` *reports success but leaves the file in place*, so the 08-03 note that
  "`mv` works" is now wrong. Porcelain `commit` dies on `index.lock`, then on `HEAD.lock`.
  The path that works, and should be used directly from now on:
  ```
  N=idx-$(date +%s%N); cp .git/index .git/$N; export GIT_INDEX_FILE=.git/$N
  T=$(git write-tree); C=$(git commit-tree "$T" -p $(git rev-parse HEAD) -m "<msg>")
  python3 -c "open('.git/refs/heads/main','w').write('$C\n')"   # in-place write, no unlink
  git push origin main
  ```
  `git add` still works (it warns about unlinkable temp objects and stages correctly), and
  `git push` is unaffected. A **fresh index copy per attempt** is required — the previous
  attempt's `.lock` also survives. Pushed `296d058..379be35` this way.
- **The site UI requests in the task file are already implemented and were verified in the
  source this run** — no work was needed and none was done. `index.dc.html` builds
  `many = reps.length > 1` and routes both the day cell and a corner count badge to
  `openPicker(iso)`, which renders a modal listing every report for that date with its
  cadence chip (so a multi-report day no longer opens the daily directly); and the "All
  reports" button opens an archive overlay built from `archiveGroups`, one group per
  cadence folder with per-group counts. Note `support.js` is a **generated bundle**
  ("do not edit, rebuild with `cd dc-runtime && bun run build`") and `dc-runtime/` is not
  in the repo — any future runtime change has to go through `index.dc.html`, not the bundle.
- **Step 9 verified over HTTP, not visually** — the Claude-in-Chrome extension was not
  connected. Live `reports.json` returns 12 daily entries with `2026-08-07` newest, and the
  live PDF returns HTTP 200, 1,525,903 bytes, 10 pages, correct title. Two cache-busted
  fetches 40 s apart agreed, so no Pages manifest lag this run.
