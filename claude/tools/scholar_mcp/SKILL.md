---
name: scholar-search
description: Google-Scholar-style literature search plus routing across the free paper-search MCPs and connected research connectors. Use when asked to find papers, check what Google Scholar would show for a query, get "cited by" lists or an author's recent work, cross-check a literature leg that came back thin, or fill an abstract or citation count. Covers scholar_mcp (this skill's own CLI and MCP server), the openags paper-search CLI, and when to use OpenAlex, PubMed, Europe PMC, bioRxiv, alphaXiv, Wiley, Scite, Consensus, SciSpace, Valency and Citeproof.
---

# Scholar search

Google Scholar has no public API. Since 2026, scripted requests to scholar.google.com
get a JavaScript "Verifying..." page (checked 2026-11-24 from a device VM; openags
paper-search's `google_scholar` source returns 0 results for the same reason).
**Do not try to get around that check** with headless browsers, rotating proxies or
CAPTCHA solvers. Use one of the three legitimate routes below, in this order.

1. **Licensed Scholar results** — `scholar_mcp` with `SERPAPI_API_KEY` set (SerpApi's
   Google Scholar engine, with a free monthly quota), or the Smithery
   `google-scholar.search_papers` tool when its quota has searches left.
2. **Scholar-equivalent open search** — `scholar_mcp` with no key. It merges
   OpenAlex, Semantic Scholar and Crossref, deduplicates by DOI, and ranks by
   relevance and citations. No key is needed.
3. **By hand** — every result and every search carries `scholar_url`. A person, or a
   browser agent driving the user's **own** signed-in browser at human pace, can open
   it to confirm a hit. Use this sparingly, a few queries at a time.

## scholar_mcp (CLI and MCP server)

File: `claude/tools/scholar_mcp/scholar_mcp.py` (Python 3.10+, standard library only.
Serve mode needs `pip install mcp`, and works with SDK 1.x and 2.x.)

```
python3 scholar_mcp.py search "low-cost PM2.5 sensor calibration" --since 2026 -n 10 [--by-date] [--backend auto|serpapi|open|openalex|semantic|crossref] [--json]
python3 scholar_mcp.py cited-by 10.1073/pnas.2526851123 -n 10 [--since 2026]     # forward citations, newest first (OpenAlex)
python3 scholar_mcp.py author "Joshua S. Apte" -n 10 [--since 2025]            # profile, h-index, recent works (OpenAlex)
python3 scholar_mcp.py serve                                                    # stdio MCP server
```
MCP tools: `scholar_search`, `scholar_cited_by`, `scholar_author`, `scholar_link`.

Config goes in env vars or in `~/.config/scholar-mcp/.env`: `SERPAPI_API_KEY` (optional,
gives real Google Scholar results), `SEMANTIC_SCHOLAR_API_KEY` (optional; without it,
Semantic Scholar often returns 429 and the tool reports that and carries on),
`OPENALEX_API_KEY` (optional), and `SCHOLAR_MCP_MAILTO` (optional). Never put a personal
email in a committed file.

Claude Desktop / Claude Code config:
```json
{"mcpServers": {"scholar-search": {"command": "python3",
  "args": ["/ABSOLUTE/PATH/Background_Research_Reports/claude/tools/scholar_mcp/scholar_mcp.py", "serve"],
  "env": {"SERPAPI_API_KEY": ""}}}}
```

## openags paper-search (CLI / MCP, free, 20+ sources)

Install: `uv tool install paper-search-mcp`. This puts `paper-search` in
`~/.local/bin`; the device VM home is per-session, so reinstall when it is missing.
- `paper-search search "<q>" -n 5 -s openalex,crossref,europepmc,pubmed,arxiv,biorxiv,medrxiv`
  returns JSON with `papers`, `source_results` and `errors`. Name the sources
  explicitly: the installed build rejects the `fast` and `fastest` presets.
- `paper-search read <source> <id>` / `download <source> <id> -o build/pdf` extract
  open-access full text. Use this for numbers that abstracts leave out.
- `paper-search tool --list` exposes the MCP tools from the command line. This
  includes `get_citing_papers`, `get_referenced_papers` and `get_crossref_paper_by_doi`.
- Free sources with no key: arxiv, pubmed, biorxiv, medrxiv, crossref, openalex, pmc,
  europepmc, dblp, zenodo, hal, doaj, openaire. Optional keys:
  `PAPER_SEARCH_MCP_CORE_API_KEY` (free), `PAPER_SEARCH_MCP_SEMANTIC_SCHOLAR_API_KEY`,
  and `PAPER_SEARCH_MCP_UNPAYWALL_EMAIL` (required for Unpaywall).
- `google_scholar` returns 0 (bot check), `ssrn` returns 403, `base` needs a registered
  IP. Never pass `--use-scihub`.
- The same server is in the Smithery toolbox (`adamamer20-paper-search-mcp-openai`,
  `titansneaker-paper-search-mcp-openai-v2`) as `search_pubmed`, `search_crossref`,
  `search_semantic`, `read_*_paper` and `download_*`.

## Connected connectors: what each one is for

| Need | Use |
|---|---|
| Entry-date window (recency) | PubMed `search_articles` (`datetype=edat`); Europe PMC `CREATION_DATE`; Crossref-ISSN `created`; **OpenAlex connector** `search_works` with a created-date filter in OQL (`check_oql` first; it is free) |
| Atmospheric and sensing venues PubMed misses | OpenAlex connector; Crossref; `scholar_mcp --backend open` |
| Preprints | **bioRxiv** `search_preprints` (date range + category, no keyword: filter locally); **alphaXiv** for arXiv sensing/ML; Europe PMC preprints |
| Relevance cross-check / backfill | `scholar_mcp search`, Consensus `search`, SciSpace `search`, Valency `semantic_search_papers`, Elicit `search_papers`, Amass BiomedCore |
| Numbers abstracts leave out | **Wiley Scholar Gateway** `search_wiley_fulltext` (Wiley only, check `getUsageLimit`); PubMed `get_full_text_article` (OA); `paper-search read`; SciSpace `extract_data` |
| Forward citations / author clusters | `scholar_mcp cited-by` / `author`; OpenAlex `list_citations`, `get_work` (affiliations for `affil`) |
| Retractions, citation stance | **Scite** `verify_papers`, `check_claim` |
| DOI / reference validation | Citeproof `resolve_reference`; OpenAlex `resolve_references`; Crossref |

Rule carried over from CONNECTORS.md: relevance indexes (`scholar_mcp`, Consensus,
SciSpace, Valency, Elicit, Smithery Scholar) never put a record in a daily issue by
themselves. Every hit must pass an explicit entry/created-date check and the
`seen.json` / `rejected.jsonl` screen before it can ship.

## Other free servers worth installing locally (not connectors)

- `uvx arxiv-mcp-server` (blazickjp): arXiv search, LaTeX section reading, citation graph through Semantic Scholar.
- `zotero-mcp-server` (54yyyu): search and annotate a Zotero library. It can write to the library, so give it read-only use in the pipeline.
- `uvx --from docling-mcp docling-mcp-server`: PDF to structured text with OCR. Use local mode (`[local]` extra) for unpublished PDFs.
- `markitdown-mcp` (Microsoft): converts URLs or files to Markdown. It has no auth and can read any file the user can, so run it only on trusted input.
- K-Dense `scientific-agent-skills`: a Paper Lookup skill over PubMed, PMC, bioRxiv, medRxiv, arXiv, OpenAlex, Crossref, Semantic Scholar, CORE and Unpaywall.

## Workflow

1. Pick the recency leg for a dated window, or `scholar_mcp search` for "what does Scholar show".
2. Show results as title | first author | year | venue | DOI | cited_by | source.
3. Copy DOIs from tool output only. Never type one by hand.
4. For a single important hit, open its `scholar_url` by hand only when SerpApi isn't available and the open search disagrees with expectations.
