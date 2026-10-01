# -*- coding: utf-8 -*-
"""Assemble build/digest.tex for one issue from a prose module (issues_prose/<date>.py
defines HEAD dict + SIGNAL, CHANGED list, CONT, CAPS dict, FOREST, PROV strings) and the
corpus-driven paper block (_tex_entries.py). Masthead/metric strip copied from the house
layout of issues/digest_2026-09-25.tex. Written 2026-09-29 for the 26-28 Sep backfill."""
import sys, subprocess, importlib.util, json, os
D = sys.argv[1]
spec = importlib.util.spec_from_file_location("prose", "issues_prose/%s.py" % D)
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
H = M.HEAD
tpl = open("issues/digest_2026-09-25.tex").read()
mast = tpl[:tpl.index("% -------------------------------------------------------------- metric strip")]
mast = mast.replace("\\newcommand{\\DIGESTDATE}{25 September 2026}", "\\newcommand{\\DIGESTDATE}{%s}" % H["long"])
old = mast[mast.index(" Issue 2026-09-25"):mast.index("\\vspace{18mm}")]
mast = mast.replace(old, " Issue %s\\;\\;\\textcolor{Amber}{\\textbar}\\;\\;Entry window %s\\;\\;%%\n"
                    " \\textcolor{Amber}{\\textbar}\\;\\;%d records screened in scope\\par}\n" % (D, H["window"], H["n"]))
def met(v, lab, col):
    return "\\begin{minipage}[t]{0.190\\linewidth}\\metric{%s}{%s}{%s}\\end{minipage}" % (v, lab, col)
strip = "\\noindent\n" + "\\hfill\n".join([
    met(H["n"], "RECORDS IN SCOPE\\\\(%d EXCLUDED)" % H["excl"], "Deep"),
    met(H["bands"], "OF 10 SUBTOPIC\\\\BANDS POPULATED", "Teal"),
    met(H["eff"], "EFFECT ESTIMATES\\\\WITH A CI", "Sky"),
    met(H["tierA"], "TIER-A\\\\RECORDS", "Amber"),
    met(H["meta"], "RECORDS CARRIED ON\\\\METADATA ALONE", "Clay")]) + "\n\n\\vspace{6mm}\n\n"
def sec(t): return "\\section*{\\sffamily\\bfseries\\color{Deep}%s}\n\\vspace{-1.5mm}{\\color{Amber}\\rule{\\linewidth}{1.1pt}}\\vspace{2.5mm}\n\n" % t
body = sec("Signal of the day") + "\\begin{keybox}\n" + M.SIGNAL + "\\par\n\\end{keybox}\n\n\\vspace{3mm}\n\n"
body += sec("What changed today") + "\\footnotesize\n\\begin{itemize}\n\n" + "\n\n".join("\\item " + c for c in M.CHANGED) + "\n\n\\end{itemize}\n\n\\vspace{2mm}\n\n"
body += ("\\begin{keybox}\n{\\sffamily\\bfseries\\footnotesize\\color{Deep}Window continuity}\\\\[1.2mm]\n"
         "{\\fontsize{7.2}{8.8}\\selectfont\n" + M.CONT + "\\par}\n\\end{keybox}\n\n\\vspace{3mm}\n")
body += "\\par\\vskip 0pt plus 18\\baselineskip\\penalty-200\\vskip 0pt plus -18\\baselineskip\n" + sec("Corpus analytics")
for f in ("f1_subtopics", "f2_design_endpoint", "f3_metric_geography", "f6_lifecourse", "f4_heatmap"):
    body += "\\noindent\\includegraphics[width=\\linewidth]{\\FIGDIR/%s.png}\n\\figcap{%s}\n\n\\vspace{2mm}\n" % (f, M.CAPS[f])
body += "\n" + M.FOREST + "\n\n\\vspace{4mm}\n\n"
ent = subprocess.run(["python3", "_tex_entries.py", D], capture_output=True, text=True, check=True).stdout
# keep a band heading with its first entry (orphaned band at a page foot, 26 Sep proof):
# conditional break = break here if < ~10 lines remain, otherwise no effect.
_k = ent.find("\\band{") + 1   # 2026-09-30: no conditional break before the FIRST band - it
# pushed the first band off the page and left "Paper-level digest" orphaned at the foot.
ent = ent[:_k] + ent[_k:].replace("\\band{", "\\par\\vskip 0pt plus 10\\baselineskip\\penalty-200\\vskip 0pt plus -10\\baselineskip\n\\band{")
# 2026-09-30 proof: "Paper-level digest" orphaned at the foot of p4 under the forest plot.
body += "\\par\\vskip 0pt plus 24\\baselineskip\\penalty-200\\vskip 0pt plus -24\\baselineskip\n"
body += (sec("Paper-level digest") + "{\\fontsize{7.4}{9}\\selectfont\\color{Slate}Ordered by cluster. Each entry gives the\n"
         "methodological core and the finding that matters, not an abstract paraphrase. Records\n"
         "marked \\textit{metadata only} carry no recoverable abstract and assert no finding.\\par}\n\n" + ent)
body += ("\n\\clearpage\n" + sec("Corpus register") + "\\input{table_rows}\n\n\\vspace{2mm}\n\n\\begin{keybox}\n"
         "{\\sffamily\\bfseries\\footnotesize\\color{Deep}Provenance and method}\\\\[1.2mm]\n{\\fontsize{7.2}{8.8}\\selectfont\n"
         + M.PROV + "\\par}\n\\end{keybox}\n\n\\end{document}\n")
os.makedirs("build", exist_ok=True)
open("build/digest.tex", "w").write(mast + strip + body)
print("wrote build/digest.tex", len(mast + strip + body))
