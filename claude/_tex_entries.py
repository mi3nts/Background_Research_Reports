# -*- coding: utf-8 -*-
"""Emit the \\band / \\paperentry digest block for one issue date, straight from the
corpus JSON.

Written 2026-09-11. The paper-level digest had been hand-transcribed from the corpus
into the issue .tex, which is a fabrication surface (a mistyped DOI or a number that
drifts between the register table and the prose). This reads state/corpus/<date>.json
and emits the block, so the entry body, the journal and the DOI are by construction the
same strings the table and the figures are built from.

    python3 _tex_entries.py 2026-09-11 > /tmp/entries.tex
"""
import json, sys, re

ORDER = ["Neuro / mental health", "Cardiovascular & metabolic",
         "Respiratory & allergic", "Reproductive & developmental",
         "Mechanistic toxicology", "Exposure assessment & modelling",
         "Sensing, forecasting & instrumentation", "Occupational & indoor",
         "Burden, policy & mitigation", "Other clinical endpoints"]
BANDCOL = {ORDER[0]: "Deep", ORDER[1]: "Teal", ORDER[2]: "Sky", ORDER[3]: "Sage",
           ORDER[4]: "Violet", ORDER[5]: "Clay", ORDER[6]: "Amber",
           ORDER[7]: "Amber", ORDER[8]: "Coral", ORDER[9]: "Slate"}

ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
       "^": r"\textasciicircum{}", "~": r"\textasciitilde{}"}


def esc(s):
    s = "".join(ESC.get(c, c) for c in str(s))
    # subscript the particle sizes the way the rest of the design system does
    s = re.sub(r"\bPM(2\.5|10|1)\b", lambda m: "PM$_{%s}$" % m.group(1), s)
    s = s.replace("SO2", "SO$_2$").replace("NO2", "NO$_2$").replace("O3", "O$_3$")
    s = s.replace("CO2", "CO$_2$").replace("NH3", "NH$_3$")
    s = s.replace("ug m-3", r"$\mu$g\,m$^{-3}$").replace("ug/m3", r"$\mu$g\,m$^{-3}$")
    s = s.replace("cm-3", r"cm$^{-3}$").replace("W m-2", r"W\,m$^{-2}$")
    s = s.replace("g mol-1", r"g\,mol$^{-1}$")
    return s


def main(date):
    P = json.load(open("state/corpus/%s.json" % date))["PAPERS"]
    out = []
    for sub in ORDER:
        rows = [p for p in P if p["sub"] == sub]
        if not rows:
            continue
        out.append("\\band{%s\\hfill %d record%s}{%s}\n"
                   % (esc(sub), len(rows), "" if len(rows) == 1 else "s", BANDCOL[sub]))
        for p in rows:
            body = esc(p["n"])
            if p["design"].startswith("Metadata only"):
                body = "\\textsc{metadata only.} " + body
            out.append("\\paperentry{%s}\n{%s}\n{%s}\n{%s}\n{%s}\n"
                       % (esc(p["short"]), esc(p["title"]), esc(p["journal"]),
                          body, p["doi"]))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1])
