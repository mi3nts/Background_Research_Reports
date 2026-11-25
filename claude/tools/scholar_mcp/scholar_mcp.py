#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scholar_mcp — Google-Scholar-style paper search as a CLI and an MCP server.

Google Scholar has no public API, and since 2026 plain HTTP requests to
scholar.google.com are answered with a JavaScript "Verifying..." challenge
(checked 2026-11-24 from the PM Research Watch device). This tool therefore does
NOT scrape or try to get around that check. It offers three back ends:

  serpapi  Google Scholar results through SerpApi's licensed Scholar API.
           Needs SERPAPI_API_KEY (SerpApi has a small free monthly quota).
  open     A Scholar-like relevance search merged from free open indexes:
           OpenAlex + Semantic Scholar + Crossref, deduplicated by DOI and
           ranked by relevance with citation counts. No key needed.
  auto     serpapi when a key is configured, otherwise open (default).

Every result carries `scholar_url`, a Google Scholar link for the same query or
title, so a person (or a browser agent driving the user's own logged-in browser)
can check a hit by hand.

Usage
  CLI : python3 scholar_mcp.py search "low-cost PM2.5 sensor calibration" --since 2026 -n 10
        python3 scholar_mcp.py cited-by 10.1073/pnas.2526851123 -n 10
        python3 scholar_mcp.py author "Joshua Apte" -n 5
  MCP : python3 scholar_mcp.py serve          (stdio; needs `pip install mcp`)

Config: env vars or ~/.config/scholar-mcp/.env (KEY=value lines):
  SERPAPI_API_KEY, SEMANTIC_SCHOLAR_API_KEY (optional), OPENALEX_API_KEY (optional),
  SCHOLAR_MCP_MAILTO (optional contact for the OpenAlex/Crossref polite pools).
"""
import json, os, re, sys, time, argparse, urllib.parse, urllib.request, urllib.error

UA = "scholar-mcp/1.0 (research literature search)"
TIMEOUT = 30


# ----------------------------------------------------------------- config / http
def _load_env():
    p = os.path.expanduser("~/.config/scholar-mcp/.env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
_load_env()


def _get(url, params=None, headers=None, retries=2):
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(
            {k: v for k, v in params.items() if v not in (None, "")})
    h = {"User-Agent": UA, "Accept": "application/json"}
    h.update(headers or {})
    last = None
    for i in range(retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = "HTTP %s" % e.code
            if e.code in (429, 500, 502, 503) and i < retries:
                time.sleep(2 * (i + 1)); continue
            raise RuntimeError("%s for %s" % (last, url.split("?")[0]))
        except Exception as e:  # network
            last = str(e)
            if i < retries:
                time.sleep(2 * (i + 1)); continue
            raise RuntimeError("%s for %s" % (last, url.split("?")[0]))


def scholar_url(q=None, title=None, since=None, until=None):
    p = {"hl": "en", "q": q if q else ('"%s"' % title if title else "")}
    if since: p["as_ylo"] = since
    if until: p["as_yhi"] = until
    return "https://scholar.google.com/scholar?" + urllib.parse.urlencode(p)


def _norm_doi(d):
    if not d: return ""
    d = d.lower().strip()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d)


def _rec(**k):
    base = dict(title="", authors=[], year=None, venue="", doi="", url="", pdf_url="",
                abstract="", cited_by=None, source="", scholar_url="")
    base.update({a: b for a, b in k.items() if b is not None})
    if not base["scholar_url"] and base["title"]:
        base["scholar_url"] = scholar_url(title=base["title"])
    return base


# ----------------------------------------------------------------- SerpApi (licensed Google Scholar)
def serpapi_search(q, n=10, since=None, until=None, sort_by_date=False, start=0):
    key = os.environ.get("SERPAPI_API_KEY")
    if not key:
        raise RuntimeError("SERPAPI_API_KEY not set")
    p = {"engine": "google_scholar", "q": q, "api_key": key, "num": min(n, 20), "hl": "en",
         "as_ylo": since, "as_yhi": until, "start": start or None, "scisbd": 2 if sort_by_date else None}
    j = _get("https://serpapi.com/search.json", p)
    if j.get("error"):
        raise RuntimeError("SerpApi: " + j["error"])
    out = []
    for r in j.get("organic_results", []):
        pub = r.get("publication_info", {}) or {}
        summ = pub.get("summary", "")
        yr = re.search(r"\b(19|20)\d{2}\b", summ)
        res = r.get("resources") or []
        out.append(_rec(
            title=r.get("title", ""), url=r.get("link", ""),
            authors=[a.get("name") for a in pub.get("authors", [])] or ([summ.split(" - ")[0]] if summ else []),
            year=int(yr.group(0)) if yr else None,
            venue=summ.split(" - ")[1] if summ.count(" - ") >= 1 else "",
            abstract=r.get("snippet", ""),
            cited_by=((r.get("inline_links") or {}).get("cited_by") or {}).get("total"),
            pdf_url=res[0].get("link", "") if res else "",
            source="google_scholar(serpapi)"))
    return out


# ----------------------------------------------------------------- open indexes
def openalex_search(q, n=10, since=None, until=None, sort_by_date=False):
    flt = []
    if since: flt.append("from_publication_date:%s-01-01" % since)
    if until: flt.append("to_publication_date:%s-12-31" % until)
    p = {"search": q, "per-page": min(n, 50), "filter": ",".join(flt) or None,
         "sort": "publication_date:desc" if sort_by_date else None,
         "mailto": os.environ.get("SCHOLAR_MCP_MAILTO"), "api_key": os.environ.get("OPENALEX_API_KEY")}
    j = _get("https://api.openalex.org/works", p)
    return [_oa_rec(w) for w in j.get("results", [])]


def _oa_abstract(inv):
    if not inv: return ""
    pos = sorted((i, w) for w, idx in inv.items() for i in idx)
    return " ".join(w for _, w in pos)


def _oa_rec(w):
    loc = w.get("primary_location") or {}
    src = (loc.get("source") or {}).get("display_name", "")
    oa = w.get("best_oa_location") or {}
    return _rec(title=w.get("title") or "", year=w.get("publication_year"),
                authors=[(a.get("author") or {}).get("display_name") for a in w.get("authorships", [])][:12],
                venue=src, doi=_norm_doi(w.get("doi")), url=w.get("doi") or w.get("id", ""),
                pdf_url=oa.get("pdf_url") or "", abstract=_oa_abstract(w.get("abstract_inverted_index")),
                cited_by=w.get("cited_by_count"), source="openalex")


def semantic_search(q, n=10, since=None, until=None, sort_by_date=False):
    yr = None
    if since or until:
        yr = "%s-%s" % (since or "", until or "")
    p = {"query": q, "limit": min(n, 100), "year": yr,
         "fields": "title,year,authors,venue,externalIds,abstract,citationCount,openAccessPdf,url,publicationDate"}
    h = {}
    if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        h["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]
    j = _get("https://api.semanticscholar.org/graph/v1/paper/search", p, h)
    out = []
    for r in j.get("data", []) or []:
        ext = r.get("externalIds") or {}
        out.append(_rec(title=r.get("title") or "", year=r.get("year"),
                        authors=[a.get("name") for a in r.get("authors", [])][:12], venue=r.get("venue") or "",
                        doi=_norm_doi(ext.get("DOI")), url=r.get("url") or "",
                        pdf_url=(r.get("openAccessPdf") or {}).get("url") or "",
                        abstract=r.get("abstract") or "", cited_by=r.get("citationCount"),
                        source="semantic_scholar"))
    if sort_by_date:
        out.sort(key=lambda x: x["year"] or 0, reverse=True)
    return out


def crossref_search(q, n=10, since=None, until=None, sort_by_date=False):
    flt = []
    if since: flt.append("from-pub-date:%s-01-01" % since)
    if until: flt.append("until-pub-date:%s-12-31" % until)
    p = {"query.bibliographic": q, "rows": min(n, 50), "filter": ",".join(flt) or None,
         "sort": "published" if sort_by_date else None, "order": "desc" if sort_by_date else None,
         "mailto": os.environ.get("SCHOLAR_MCP_MAILTO")}
    j = _get("https://api.crossref.org/works", p)
    out = []
    for it in j.get("message", {}).get("items", []):
        dp = (it.get("issued") or {}).get("date-parts") or [[None]]
        ab = re.sub(r"<[^>]+>", " ", it.get("abstract", "") or "")
        out.append(_rec(title=(it.get("title") or [""])[0], year=dp[0][0],
                        authors=[(" ".join(x for x in (a.get("given"), a.get("family")) if x)) for a in it.get("author", [])][:12],
                        venue=(it.get("container-title") or [""])[0], doi=_norm_doi(it.get("DOI")),
                        url=it.get("URL", ""), abstract=re.sub(r"\s+", " ", ab).strip(),
                        cited_by=it.get("is-referenced-by-count"), source="crossref"))
    return out


def _tokens(s):
    return set(re.findall(r"[a-z0-9.]+", (s or "").lower())) - {"the", "of", "and", "a", "in", "for", "on", "to", "with"}


def open_search(q, n=10, since=None, until=None, sort_by_date=False, sources=("openalex", "semantic", "crossref")):
    fn = {"openalex": openalex_search, "semantic": semantic_search, "crossref": crossref_search}
    merged, errors = {}, {}
    for s in sources:
        try:
            rs = fn[s](q, n=n, since=since, until=until, sort_by_date=sort_by_date)
        except Exception as e:
            errors[s] = str(e); continue
        for rank, r in enumerate(rs):
            key = r["doi"] or re.sub(r"\W+", "", r["title"].lower())[:80]
            if not key: continue
            if key in merged:
                m = merged[key]
                m["found_in"].append(s)
                m["best_rank"] = min(m["best_rank"], rank)
                for f in ("abstract", "pdf_url", "venue", "doi"):
                    if not m[f] and r[f]: m[f] = r[f]
                if (r["cited_by"] or 0) > (m["cited_by"] or 0): m["cited_by"] = r["cited_by"]
            else:
                r["found_in"] = [s]; r["best_rank"] = rank
                merged[key] = r
    qt = _tokens(q)
    def score(r):
        overlap = len(qt & _tokens(r["title"] + " " + r["abstract"][:400])) / max(1, len(qt))
        return (overlap * 3 + len(r["found_in"]) * 0.7 - r["best_rank"] * 0.15
                + min(1.5, (r["cited_by"] or 0) ** 0.5 / 20))
    out = sorted(merged.values(), key=(lambda r: (r["year"] or 0, score(r))) if sort_by_date else score, reverse=True)
    for r in out:
        r["source"] = "+".join(r.pop("found_in")); r.pop("best_rank", None)
    return out[:n], errors


# ----------------------------------------------------------------- public API
def search_papers(query, n=10, since=None, until=None, sort_by_date=False, backend="auto"):
    """Scholar-style search. Returns {backend, results, errors, scholar_url}."""
    since = int(since) if since else None
    until = int(until) if until else None
    errors = {}
    if backend in ("auto", "serpapi") and os.environ.get("SERPAPI_API_KEY"):
        try:
            return dict(backend="serpapi", results=serpapi_search(query, n, since, until, sort_by_date),
                        errors=errors, scholar_url=scholar_url(query, since=since, until=until))
        except Exception as e:
            errors["serpapi"] = str(e)
            if backend == "serpapi":
                return dict(backend="serpapi", results=[], errors=errors, scholar_url=scholar_url(query, since=since, until=until))
    elif backend == "serpapi":
        errors["serpapi"] = "SERPAPI_API_KEY not set"
        return dict(backend="serpapi", results=[], errors=errors, scholar_url=scholar_url(query, since=since, until=until))
    srcs = ("openalex", "semantic", "crossref") if backend in ("auto", "open") else (backend,)
    res, e2 = open_search(query, n, since, until, sort_by_date, srcs)
    errors.update(e2)
    return dict(backend="open:" + ",".join(srcs), results=res, errors=errors,
                scholar_url=scholar_url(query, since=since, until=until))


def cited_by(doi, n=10, since=None):
    """Works citing a DOI (OpenAlex), newest first. The forward-citation view Scholar's 'Cited by' gives."""
    w = _get("https://api.openalex.org/works/doi:" + _norm_doi(doi),
             {"mailto": os.environ.get("SCHOLAR_MCP_MAILTO"), "api_key": os.environ.get("OPENALEX_API_KEY")})
    flt = "cites:" + w["id"].rsplit("/", 1)[-1]
    if since: flt += ",from_publication_date:%s-01-01" % since
    j = _get("https://api.openalex.org/works", {"filter": flt, "per-page": min(n, 50), "sort": "publication_date:desc",
                                                 "mailto": os.environ.get("SCHOLAR_MCP_MAILTO"), "api_key": os.environ.get("OPENALEX_API_KEY")})
    return dict(seed=_oa_rec(w), total=j.get("meta", {}).get("count"), results=[_oa_rec(x) for x in j.get("results", [])])


def author_papers(name, n=10, since=None):
    """An author's recent works (OpenAlex author match, most-cited author of that name)."""
    a = _get("https://api.openalex.org/authors", {"search": name, "per-page": 5,
                                                   "mailto": os.environ.get("SCHOLAR_MCP_MAILTO")}).get("results", [])
    if not a:
        return dict(author=None, results=[])
    a = sorted(a, key=lambda x: x.get("cited_by_count", 0), reverse=True)[0]
    flt = "author.id:" + a["id"].rsplit("/", 1)[-1]
    if since: flt += ",from_publication_date:%s-01-01" % since
    j = _get("https://api.openalex.org/works", {"filter": flt, "per-page": min(n, 50), "sort": "publication_date:desc",
                                                 "mailto": os.environ.get("SCHOLAR_MCP_MAILTO")})
    inst = (a.get("last_known_institutions") or [{}])
    return dict(author=dict(name=a.get("display_name"), openalex_id=a["id"], works=a.get("works_count"),
                            cited_by=a.get("cited_by_count"), h_index=(a.get("summary_stats") or {}).get("h_index"),
                            institution=(inst[0] or {}).get("display_name") if inst else None),
                results=[_oa_rec(x) for x in j.get("results", [])])


# ----------------------------------------------------------------- MCP server
def serve():
    try:  # MCP Python SDK 2.x
        from mcp.server.mcpserver import MCPServer as _Server
    except ImportError:
        try:  # SDK 1.x
            from mcp.server.fastmcp import FastMCP as _Server
        except ImportError:
            sys.exit("The MCP SDK is not installed: pip install 'mcp>=1.2'")
    app = _Server("scholar-search")

    @app.tool()
    def scholar_search(query: str, max_results: int = 10, year_from: int = 0, year_to: int = 0,
                       sort_by_date: bool = False, backend: str = "auto") -> dict:
        """Google-Scholar-style paper search. backend: auto (SerpApi Google Scholar if
        SERPAPI_API_KEY is set, else open), serpapi, open (OpenAlex + Semantic Scholar +
        Crossref merged), openalex, semantic, crossref. Each result has title, authors,
        year, venue, doi, abstract, cited_by, pdf_url, source and scholar_url (a
        Google Scholar link to check the hit by hand)."""
        return search_papers(query, max_results, year_from or None, year_to or None, sort_by_date, backend)

    @app.tool()
    def scholar_cited_by(doi: str, max_results: int = 10, year_from: int = 0) -> dict:
        """Papers citing a DOI, newest first (OpenAlex), like Scholar's 'Cited by'."""
        return cited_by(doi, max_results, year_from or None)

    @app.tool()
    def scholar_author(name: str, max_results: int = 10, year_from: int = 0) -> dict:
        """An author's profile (works, citations, h-index, institution) and recent papers (OpenAlex)."""
        return author_papers(name, max_results, year_from or None)

    @app.tool()
    def scholar_link(query: str = "", title: str = "", year_from: int = 0, year_to: int = 0) -> str:
        """Build a Google Scholar URL for a query or an exact title, for checking by hand in a browser."""
        return scholar_url(query or None, title or None, year_from or None, year_to or None)

    app.run()


# ----------------------------------------------------------------- CLI
def _print(obj, as_json):
    if as_json:
        print(json.dumps(obj, indent=1, ensure_ascii=False)); return
    rs = obj.get("results", [])
    if obj.get("backend"): print("# backend:", obj["backend"])
    if obj.get("author"): print("# author:", json.dumps(obj["author"], ensure_ascii=False))
    if obj.get("seed"): print("# seed:", obj["seed"]["title"], "| citing works:", obj.get("total"))
    for e, m in (obj.get("errors") or {}).items(): print("# %s failed: %s" % (e, m))
    for i, r in enumerate(rs, 1):
        au = ", ".join([a for a in r["authors"] if a][:3]) + (" et al." if len(r["authors"]) > 3 else "")
        print("%2d. %s (%s) %s | %s | cited_by=%s | %s" % (i, r["title"], r["year"], au, r["venue"],
                                                          r["cited_by"], r["doi"] or r["url"]))
    if obj.get("scholar_url"): print("# check on Google Scholar:", obj["scholar_url"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("query"); s.add_argument("-n", type=int, default=10)
    s.add_argument("--since", type=int); s.add_argument("--until", type=int)
    s.add_argument("--by-date", action="store_true"); s.add_argument("--backend", default="auto")
    s.add_argument("--json", action="store_true")
    c = sp.add_parser("cited-by"); c.add_argument("doi"); c.add_argument("-n", type=int, default=10)
    c.add_argument("--since", type=int); c.add_argument("--json", action="store_true")
    a = sp.add_parser("author"); a.add_argument("name"); a.add_argument("-n", type=int, default=10)
    a.add_argument("--since", type=int); a.add_argument("--json", action="store_true")
    sp.add_parser("serve")
    x = ap.parse_args(argv)
    if x.cmd == "serve": return serve()
    if x.cmd == "search":
        _print(search_papers(x.query, x.n, x.since, x.until, x.by_date, x.backend), x.json)
    elif x.cmd == "cited-by":
        _print(cited_by(x.doi, x.n, x.since), x.json)
    elif x.cmd == "author":
        _print(author_papers(x.name, x.n, x.since), x.json)


if __name__ == "__main__":
    main()
