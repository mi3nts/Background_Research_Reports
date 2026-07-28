# -*- coding: utf-8 -*-
import os, re
from corpus import PAPERS

HERE = os.path.dirname(os.path.abspath(__file__))

ORDER = ["Neuro / mental health", "Cardiovascular & metabolic",
         "Reproductive & developmental", "Respiratory & allergic",
         "Mechanistic toxicology", "Occupational & indoor",
         "Sensing, forecasting & instrumentation",
         "Exposure assessment & modelling",
         "Burden, policy & mitigation", "Other clinical endpoints"]

BANDCOL = {ORDER[0]: "Deep", ORDER[1]: "Teal", ORDER[2]: "Sky", ORDER[3]: "Sage",
           ORDER[4]: "Violet", ORDER[5]: "Clay", ORDER[6]: "Amber",
           ORDER[7]: "Amber", ORDER[8]: "Coral", ORDER[9]: "Slate"}


def esc(s):
    s = (s.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")
          .replace("#", r"\#"))
    s = s.replace("PM2.5", r"PM$_{2.5}$").replace("PM10", r"PM$_{10}$")
    s = s.replace("ug/m3", r"$\mu$g/m$^3$")
    s = s.replace("PMcoarse", r"PM$_{\mathrm{coarse}}$")
    s = s.replace("-", "--") if False else s
    return s


def shorten_title(t):
    t = re.sub(r"\s*\(.*?\)\s*$", "", t)
    return t


rows = []
for sub in ORDER:
    grp = [p for p in PAPERS if p["sub"] == sub]
    if not grp:
        continue
    rows.append(
        r"\multicolumn{6}{@{}l@{}}{\cellcolor{Mist}\textsf{\textbf{\textcolor{%s}{%s}}}}\\[0.6mm]"
        % (BANDCOL[sub], esc(sub)))
    for p in sorted(grp, key=lambda d: d["short"]):
        author = p["short"].replace(" 2026b", "").replace(" 2026", "")
        rows.append(" & ".join([
            r"\href{https://doi.org/%s}{%s}" % (p["doi"], esc(author)),
            esc(shorten_title(p["title"])),
            r"\textit{%s}" % esc(p["journal"]),
            esc(p["design"]),
            esc(p["pm"]),
            esc(p["geo"]),
        ]) + r"\\")
    rows.append(r"\addlinespace[0.9mm]")

HEAD = r"""{\fontsize{6.7}{8.4}\selectfont
\setlength{\tabcolsep}{2.4pt}
\begin{longtable}{@{}>{\RaggedRight}p{25mm}>{\RaggedRight}p{41mm}>{\RaggedRight}p{27mm}%
>{\RaggedRight}p{23mm}>{\RaggedRight}p{18mm}>{\RaggedRight}p{15mm}@{}}
\toprule
\textsf{\textbf{First author}} & \textsf{\textbf{Focus}} & \textsf{\textbf{Journal}} &
\textsf{\textbf{Design}} & \textsf{\textbf{Metric}} & \textsf{\textbf{Region}}\\
\midrule
\endfirsthead
\toprule
\textsf{\textbf{First author}} & \textsf{\textbf{Focus}} & \textsf{\textbf{Journal}} &
\textsf{\textbf{Design}} & \textsf{\textbf{Metric}} & \textsf{\textbf{Region}}\\
\midrule
\endhead
"""
TAIL = "\\bottomrule\n\\end{longtable}}\n"

with open(os.path.join(HERE, "table_rows.tex"), "w") as f:
    f.write(HEAD + "\n".join(rows) + "\n" + TAIL)

print("rows written:", len([r for r in rows if r.endswith(r"\\") and "multicolumn" not in r]))
