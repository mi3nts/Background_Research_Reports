# -*- coding: utf-8 -*-
"""Build the monthly paper-level digest.

Two tiers, visually distinct and labelled as such:
  * records that appeared in a daily issue keep their full critical summary, lifted
    verbatim from the archived issue .tex - nothing is re-written;
  * backfill records get an extractive precis: the single most quantitative sentence
    of the abstract, copied, never paraphrased and never assessed.

  PMRW_START / PMRW_END / PMRW_BUILD
"""
import os, re, json, glob, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus as C

HERE  = os.path.dirname(os.path.abspath(__file__))
BUILD = os.environ.get("PMRW_BUILD", os.path.join(HERE, "build"))
ORDER = [C.SENS, C.EXPO, C.CVM, C.NEU, C.RESP, C.REPR, C.MECH, C.OCC, C.BURD, C.OTHR]
BANDCOL = {C.SENS:"Amber", C.EXPO:"Amber", C.CVM:"Teal", C.NEU:"Deep", C.RESP:"Sage",
           C.REPR:"Sky", C.MECH:"Violet", C.OCC:"Clay", C.BURD:"Coral", C.OTHR:"Slate"}

def brk(doi):
    """DOIs sit in \texttt and never hyphenate, which produced 9 overfull boxes at 270
    records. Insert discretionary breaks after the separators so they wrap."""
    return doi.replace("/", "/\\allowbreak ").replace(".", ".\\allowbreak ")


def esc(s):
    """Decode HTML entities FIRST, then escape for LaTeX. Doing it the other way round
    turned &#x2264; into \&\#x2264; in the output."""
    s = s or ""
    s = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    for a, b in [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"')]:
        s = s.replace(a, b)
    s = s.replace("\\", " ")          # stray backslashes in source, before we add our own
    # unicode that LaTeX/T1 cannot set directly
    for a, b in [("\u2264", r"$\leq$"), ("\u2265", r"$\geq$"), ("\u2260", r"$\neq$"),
                 ("\u00b5", r"$\mu$"), ("\u03bc", r"$\mu$"), ("\u00b3", r"$^3$"),
                 ("\u00b2", r"$^2$"), ("\u2212", "-"), ("\u2013", "--"), ("\u2014", "---"),
                 ("\u2018", "`"), ("\u2019", "'"), ("\u201c", "``"), ("\u201d", "''"),
                 ("\u00a0", " "), ("\u2009", " "), ("\u202f", " "), ("\u00d7", r"$\times$"),
                 ("\u03b1", r"$\alpha$"), ("\u03b2", r"$\beta$"), ("\u03b3", r"$\gamma$"),
                 ("\u03b4", r"$\delta$"), ("\u2032", "'"), ("\u00b0", r"$^\circ$")]:
        s = s.replace(a, b)
    # sub/superscript unicode (PM2.5 written as PM\u2082.\u2085 etc.) - PubMed uses these
    SUBSUP = {"\u2080":"0","\u2081":"1","\u2082":"2","\u2083":"3","\u2084":"4","\u2085":"5",
              "\u2086":"6","\u2087":"7","\u2088":"8","\u2089":"9","\u208a":"+","\u208b":"-"}
    SUP    = {"\u2070":"0","\u00b9":"1","\u2074":"4","\u2075":"5","\u2076":"6","\u2077":"7",
              "\u2078":"8","\u2079":"9","\u207a":"+","\u207b":"-"}
    for k, v in SUBSUP.items():
        s = s.replace(k, "$_{%s}$" % v)
    for k, v in SUP.items():
        s = s.replace(k, "$^{%s}$" % v)
    # anything still outside Latin-1 that we have no rule for: drop it rather than
    # fail the build - the DOI and title carry the record either way
    s = "".join(ch if ord(ch) < 0x180 or ch in "\u2264\u2265" else "" for ch in s)
    # LaTeX specials (backslash already handled above)
    for a, b in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"),
                 ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}"), ("<", r"\textless{}"), (">", r"\textgreater{}")]:
        s = s.replace(a, b)
    # $ is legal only in the maths we just inserted; protect stray ones
    if s.count("$") % 2:
        s = s.replace("$", r"\$")
    return re.sub(r"\s+", " ", s).strip()


blocks = json.load(open(os.path.join(HERE, "cache/2026-07-monthly/daily_summaries.json")))

def build():
    papers = C.PAPERS
    by = collections.defaultdict(list)
    for p in papers:
        by[p["sub"]].append(p)
    out, nfull, nprecis, nbare = [], 0, 0, 0
    for sub in ORDER:
        grp = by.get(sub, [])
        if not grp:
            continue
        full   = [p for p in grp if p["doi"].lower() in blocks]
        others = [p for p in grp if p["doi"].lower() not in blocks]
        full.sort(key=lambda d: d["short"]); others.sort(key=lambda d: d["short"])
        out.append(r"\band{%s\hfill %d records}{%s}" % (esc(sub), len(grp), BANDCOL[sub]))
        out.append("")
        if full:
            out.append(r"\subsectionnote{Carried from the daily issues --- full summaries "
                       r"(%d of %d records in this subtopic)}" % (len(full), len(grp)))
            out.append("")
            for p in full:
                b = blocks[p["doi"].lower()]
                out.append("\\paperentry{%s}\n{%s}\n{%s}\n{%s}\n{%s}\n" %
                           (b["author"], b["title"], b["journal"], b["body"], p["doi"]))
                nfull += 1
        if others:
            out.append(r"\subsectionnote{Recovered by the month-wide harvest --- extractive "
                       r"precis, not an assessed summary (%d records)}" % len(others))
            out.append("")
            for p in others:
                pr = esc(p.get("precis", ""))
                if pr:
                    nprecis += 1
                else:
                    pr = r"\textit{No abstract was available from PubMed at entry; this record " \
                         r"is listed on title, journal and metadata alone.}"
                    nbare += 1
                out.append("\\precisentry{%s}\n{%s}\n{%s}\n{%s}\n{%s}{%s}\n" %
                           (esc(p["short"]), esc(p["title"]), esc(p["journal"]), pr,
                            p["doi"], brk(p["doi"])))
        out.append(r"\vspace{1.5mm}")
        out.append("")
    os.makedirs(BUILD, exist_ok=True)
    open(os.path.join(BUILD, "digest_body.tex"), "w").write("\n".join(out))
    print("digest_body.tex: %d full summaries, %d precis, %d title-only, %d records total"
          % (nfull, nprecis, nbare, nfull + nprecis + nbare))

if __name__ == "__main__":
    build()
