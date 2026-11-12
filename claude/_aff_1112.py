# affiliations (first; last) from PubMed XML or Crossref for admitted records of a day
import json,sys,urllib.request,re,xml.etree.ElementTree as ET
D=sys.argv[1]; IDX=[int(x) for x in sys.argv[2].split(",")]
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
f=json.load(open("cache/%s/_fresh.json"%D)); out={}
pm=[f[i]["pmid"] for i in IDX if f[i].get("pmid")]
if pm:
    x=urllib.request.urlopen(urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="+",".join(pm),headers=UA),timeout=60).read()
    for a in ET.fromstring(x).iter("PubmedArticle"):
        p=a.findtext(".//PMID"); au=a.findall(".//AuthorList/Author")
        g=lambda z:(z.findtext("AffiliationInfo/Affiliation") or "") if z is not None else ""
        out[p]=(g(au[0]) if au else "", g(au[-1]) if au else "")
for i in IDX:
    r=f[i]; k=r.get("pmid")
    if k in out: print(i,"PM|",out[k][0][:160],"||",out[k][1][:160]); continue
    if r.get("doi"):
        try:
            m=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/"+r["doi"],headers=UA),timeout=30).read())["message"]
            au=m.get("author",[]); g=lambda z:"; ".join(a.get("name","") for a in z.get("affiliation",[]))
            print(i,"XR|",g(au[0])[:160] if au else "","||",g(au[-1])[:160] if au else "")
        except Exception as e: print(i,"fail",e)
