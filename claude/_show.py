import json,sys
D=sys.argv[1]; N=int(sys.argv[3]) if len(sys.argv)>3 else 1100
f=json.load(open('cache/%s/_fresh.json'%D))
for i in [int(x) for x in sys.argv[2].split(',')]:
    r=f[i]; print('##',i,r.get('pmid',''),r.get('doi',''),'|',r.get('journal',''),'|',r.get('authors','')[:60]); print('T:',r['title'][:250].replace('\n',' ')); print('A:',(r.get('abstract') or '')[:N].replace('\n',' ')); print()
