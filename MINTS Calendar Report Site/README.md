# Background_Research_Reports

Summary reports of research published in relevant topics of MINTS research, published as a
calendar website on GitHub Pages.

**Live site:** `https://mi3nts.github.io/Background_Research_Reports/`

---

## Adding a new report

1. Drop the PDF into the folder for its cadence — `Reports/daily/`, `Reports/weekly/`,
   `Reports/monthly/` or `Reports/yearly/`. Name it `Title-Words_YYYY-MM-DD.pdf`: the date
   places it on the calendar and the words before the underscore become the display title
   (`PM-Research-Watch_2026-07-27.pdf` → "PM Research Watch", 27 Jul 2026).
2. Add the filename to the matching list in `Reports/reports.json`:

   ```json
   {
     "daily":   ["PM-Research-Watch_2026-07-27.pdf", "PM-Research-Watch_2026-07-28.pdf"],
     "weekly":  ["Weekly-Digest_2026-08-02.pdf"],
     "monthly": [],
     "yearly":  []
   }
   ```

   Filenames are resolved as `Reports/<cadence>/<filename>`. An entry may also be an object if
   you want a custom title: `{ "file": "odd-name_2026-08-03.pdf", "title": "Custom title" }` —
   keep `YYYY-MM-DD` in the filename either way.
3. Commit and push. GitHub Pages redeploys and the day lights up on the calendar. Several
   reports on the same day are all listed; the day circle opens the first (daily first).

Folder and file names are **case-sensitive** on GitHub Pages — the folder is `Reports`.

## Enabling GitHub Pages

Repository → **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main`, folder
`/ (root)` → Save. No build step, no Jekyll (`.nojekyll` is present).

## Using the site

- **Week / Month / Year** toggle in the top right; `←` / `→` keys or the arrow buttons move
  through periods, **Today** jumps back. In Year view, click a month name to open that month.
- Every date is a circle; circles with a report are tinted and clickable — clicking opens that
  day's PDF in an in-page reader with New tab / Download actions. `Esc` returns to the calendar.
- The MINTS logo (top left) always returns to the home view.
- Any report is directly linkable: `…/index.dc.html#2026-07-27`.

## Layout

```
index.html                  entry point — redirects to the site (keeps deep links)
index.dc.html               the site: calendar, view toggle, PDF reader
support.js                  runtime for index.dc.html
.nojekyll                   tells Pages to serve files as-is
assets/
  mints-logo.png            header logo (web-sized)
  mintsLarge.png            original full-resolution logo
Reports/
  reports.json              the manifest the calendar reads
  daily/    *.pdf
  weekly/   *.pdf
  monthly/  *.pdf
  yearly/   *.pdf
_ds/nocturne-…/             Nocturne design system (tokens + components)
```
