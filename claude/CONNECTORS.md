# Connector routing for PM Research Watch

Authoritative list of the research/publication MCP connectors the daily run sweeps, what
each one is actually good for, and what it demonstrably cannot do. Established
2026-08-10, when the full connected set was swept for the first time and every leg was
measured rather than assumed.

**Read this with `PIPELINE.md`.** `PIPELINE.md` carries the run log; this file carries the
routing contract. Update the status column here whenever a leg's behaviour changes.

## Standing rule

> A connector is either a **recency index** (can resolve a single entry-date day) or a
> **relevance index** (ranks by topical similarity, ignores the window). Only recency
> indices belong on the daily spine. Relevance indices are run for **backfill and
> cross-checking**, and everything they return must be screened against `seen.json` and
> against an explicit entry-date lookup before it can ship.

Mixing the two silently was the failure mode this file exists to prevent: on 2026-08-09
three Consensus sweeps returned 9 DOIs, all of which resolved to Crossref creation dates
between 12 January and 15 July, and none of which belonged in a 9 August issue.

## Tier 1 — recency spine (run every day, in the window)

| Leg | Tool | Window mechanism | Measured status 2026-08-10 |
|---|---|---|---|
| PubMed connector | `search_articles` / `get_article_metadata` / `find_related_articles` / `convert_article_ids` / `get_full_text_article` | `[Date - Entry]` via `datetype="edat"` | **Works.** Only leg that reliably resolves a single day. Run **three** queries: health axis, instrumentation axis, broad MeSH sweep (`Particulate Matter`/`Air Pollutants`/`Environmental Monitoring`/`Inhalation Exposure`). 13 distinct records, 6 carried. |
| Local harvester `harvest.py` | `pubmed()` | E-utilities `[EDAT]` | Works. 5 health / 0 sensing. |
| Local harvester | `europepmc()` | `CREATION_DATE:[a TO b]` | Works, surfaces preprints. 3 hits, 2 carried. `FIRST_PDATE` still broken for recent windows. |
| Local harvester | Crossref by ISSN across 17 journals | `created` date-part filter | Works, and is the **only** leg that sees *Atmos. Meas. Tech.* / *Atmos. Chem. Phys.* / *Atmos. Environ.* — PubMed does not index them. 12 hits, 7 carried. Elsevier records arrive without abstracts (see Known gaps). |
| Local harvester | `arxiv()` | relevance query + local recency screen | Works but near-zero yield. 60 records, 1 on/after 26 Jul, off-topic. `submittedDate:[...]` still returns an empty body. |
| ClinicalTrials.gov | `search_trials`, `analyze_endpoints`, `search_investigators` | `advanced_query` with `AREA[LastUpdatePostDate]RANGE[...]` | Works. Accumulate to `state/trials.json`; **surface in the weekly rollup, not daily**. Note: `search_trials` has **no `query` parameter** — use `condition` / `intervention`. |

## Tier 2 — relevance and backfill (run daily, screen hard)

| Leg | Tool | What it is good for | Measured status 2026-08-10 |
|---|---|---|---|
| **Amass BiomedCore** | `search_amass_biomedcore_records` (+ `get_amass_biomedcore_record`) | 40M+ PubMed/PMC records with abstracts and JuFo journal-quality tier. `minPublicationDate` filters on **publication** date, not entry date. | **Highest-value Tier-2 leg.** 10 records: 4 duplicates caught by `seen.json`, 3 declined, **3 carried as flagged backfill** (entry dates 9 Jul, 29 Jun, 9 Jun). This is the leg that surfaces pre-watch literature nothing else can reach. |
| Consensus | `search` | Broad coverage incl. sensing/atmospheric venues PubMed misses | **0 carried, fourth consecutive run.** Relevance index. Free tier caps at 10 results. Still worth running as a duplicate/coverage check — it independently confirmed the 8 Aug calibration-transfer cluster. |
| Semantic Scholar | `paper-search-advanced`, `papers-citations`, `papers-references` | Citation graph, snowballing from tier-A hits | Rate-limited on 2026-08-10. Retry with backoff; do not block the run on it. |
| arXiv (toolbox) | `search_arxiv` | Second arXiv path | Relevance-ranked, results from 2019–2021. Redundant with the harvester's leg. |
| medRxiv / bioRxiv | `search_medrxiv`, `search_preprints` | Health preprints | Nothing inside the window. `search_preprints` takes date range + category but **no keyword**, so it needs local filtering. |
| Crossref (toolbox) | `search_crossref` | Cross-check on the ISSN sweep | Relevance-ranked; the harvester's ISSN+created filter is strictly better. |
| Google Scholar (toolbox) | `search_google_scholar` | Last resort | Unreliable, blocks scripts. Never a dependency. |

## Tier 3 — targeted, not swept

| Leg | Tool | Use it for |
|---|---|---|
| Scholar Gateway | `semanticSearch` | Full-text **passage** retrieval — calibration R²/RMSE, CIs, sensor model numbers that abstracts omit. **Corpus is Wiley full text, last updated May 2026.** It is not a recency leg and cannot resolve non-Wiley publishers. Confirmed 2026-08-10: could not return any of five Elsevier *Atmos. Environ.* abstracts. |
| Exa | `web_search_exa`, `web_fetch_exa` | Journal TOC pages, publisher landing pages when a DOI has no metadata. Web index, not a bibliographic one. |
| Nimble | `nimble_search` | Date-filtered web search. Returned 0 for a 2-day window on 2026-08-10. |
| Claude in Chrome / Control Chrome | `navigate`, `get_page_text` | Google Scholar sweep, journal TOCs, live-site verification. |
| pdf-viewer | `display_pdf` | PDF proofing (step 6). |
| GitHub connector | — | Repo state, push fallback, failure issues. |

## Known gaps (recheck, do not assume)

- **OpenAlex** — `from_created_date` / `to_created_date` returned HTTP **429** on 2026-08-10, the **eighth consecutive run** (previously 403 "plan upgrade required"). Leg is broken. Route the coverage through Amass and Consensus. If a free date filter reappears, note it in `PIPELINE.md` and promote it back to Tier 1.
- **Elsevier abstract famine** — *Atmospheric Environment*, *J. Aerosol Sci.*, *J. Hazard. Mater.* DOIs appear in Crossref with **no abstract**, and are absent from Europe PMC, Semantic Scholar and Scholar Gateway. Five such records shipped `METADATA ONLY` on 2026-08-10; the 8 August batch is still unresolved after 72 h. **The re-check is a weekly sweep, not a daily one** — a daily re-check is faster than the publishers deposit.
- **Crossref `from-index-date`** — unusable for entry-date windowing; continuous re-indexing returns works back to 2007.
- **PubMed does not index** *Atmos. Meas. Tech.* or *Atmos. Chem. Phys.* Pure instrumentation work is invisible there. The Crossref ISSN sweep is what closes that gap, not Consensus.

## Token discipline

Query each connector **once**, persist normalised records to
`claude/cache/YYYY-MM-DD/<source>.json` immediately, read from cache thereafter. Several
connectors (Exa, Scholar Gateway, the arXiv/medRxiv toolbox legs) return payloads large
enough to be spilled to a file by the host; screen those with a script rather than reading
them back into context. Full text only for tier-A records.

## Backfill policy

Tier-2 legs will surface high-value records whose entry dates predate this watch
(2026-07-26). Carrying them is allowed and useful, under three conditions:

1. Confirm the entry date with an explicit `esummary` lookup — never trust the connector's
   publication date, which is the journal issue date and can be months later.
2. Cap it. Three per issue is the working limit; rank by relevance to the sensing /
   calibration / exposure-modelling axis, not by recency.
3. Mark every one `\textsc{backfill}` in the digest **with its entry date**, and record the
   per-leg backfill count in the provenance box. A reader must be able to tell which
   records the date window actually produced.
