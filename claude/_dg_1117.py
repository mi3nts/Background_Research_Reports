# Insert design_group mappings before _design_unmapped (run 2026-11-17). Usage: python3 _dg_1117.py 'Label=Group' ...
import sys
src=open('plots.py').read(); k='_design_unmapped = set()'; i=src.index(k)
m={}
for a in sys.argv[1:]:
    l,g=a.split('=',1)
    if repr(l) in src[:i] or ('"%s"'%l) in src[:i]: continue
    m[l]=g
if m:
    blk='design_group.update({\n'+''.join('    %r: %r,\n'%(l,g) for l,g in m.items())+'})  # 2026-11-17\n'
    src=src[:i]+blk+src[i:]; open('plots.py','w').write(src)
print('added',len(m))
