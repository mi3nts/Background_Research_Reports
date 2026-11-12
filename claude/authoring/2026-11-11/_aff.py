import json,urllib.request,re,xml.etree.ElementTree as ET
ADM=[0,3,8,9,14,15,17,18,19,20,21,22,25,26,27,28,29,33,35,55,61,62,63,64,65,66,75,82,85,89,106,110,118,119,123,124]
f=json.load(open('cache/2026-11-11/_fresh.json'))
UA={"User-Agent":"PM-Research-Watch/1.0 (mailto:rittikpatra2014@gmail.com)"}
out={}
pm=[f[i]['pmid'] for i in ADM if f[i].get('pmid')]
x=urllib.request.urlopen(urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="+",".join(pm),headers=UA),timeout=60).read()
for a in ET.fromstring(x).findall('.//PubmedArticle'):
    p=a.findtext('.//PMID'); au=a.findall('.//AuthorList/Author')
    def af(z):
        t=z.findtext('.//AffiliationInfo/Affiliation') if z is not None else None
        return t or ''
    out[p]=(af(au[0]) if au else '', af(au[-1]) if au else '', ', '.join((z.findtext('LastName') or '') for z in au[:1]+au[-1:]))
for i in ADM:
    r=f[i]
    if r.get('pmid') in out: v=out[r['pmid']]
    else:
        try:
            m=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/"+r['doi'],headers=UA),timeout=30).read())['message']
            au=m.get('author',[])
            g=lambda z:(z.get('affiliation') or [{}])[0].get('name','') if z else ''
            v=(g(au[0]) if au else '',g(au[-1]) if au else '',', '.join(z.get('family','') for z in (au[:1]+au[-1:])))
        except Exception as e: v=('ERR '+str(e),'','')
    print(i,'|',v[2],'|F:',v[0][:110],'|L:',v[1][:110])
