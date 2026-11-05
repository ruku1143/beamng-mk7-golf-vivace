import zipfile, re, json, sys, os, glob
ZIP = 'D:/SteamLibrary/steamapps/common/BeamNG.drive/content/vehicles/vivace.zip'
MOD = 'C:/Users/lukem/AppData/Local/BeamNG/BeamNG.drive/current/mods/unpacked/EA888_Gen3_Vivace/vehicles/vivace'
z = zipfile.ZipFile(ZIP)

def sources():
    for n in z.namelist():
        if n.startswith('vehicles/vivace/') and n.endswith('.jbeam') and n.count('/') == 2:
            yield 'base:' + n.split('/')[-1], z.read(n).decode('utf8', 'replace')
    cz = zipfile.ZipFile(ZIP.replace('vivace.zip','common.zip'))
    for n in cz.namelist():
        if n.endswith('.jbeam') and ('/wheels/' in n or '/passengers/' in n or 'tire' in n):
            yield 'common:' + n.split('/')[-1], cz.read(n).decode('utf8','replace')
    for f in glob.glob(MOD + '/*.jbeam'):
        yield 'mod:' + os.path.basename(f), open(f, encoding='utf8', errors='replace').read()

wnum = re.compile(r'"nodeWeight"\s*:\s*("?[^,}\]"]*"?)')
def parse_parts(text):
    parts = {}
    cur = None; in_nodes = False; w = None
    for line in text.split('\n'):
        l = line.split('//')[0]
        m = re.match(r'^"([A-Za-z0-9_]+)"\s*:\s*\{?\s*$', l.rstrip()) or re.match(r'^"([A-Za-z0-9_]+)"\s*:\s*\{', l)
        if m:
            cur = m.group(1); parts[cur] = {'mass': 0.0, 'n': 0, 'vars': []}; in_nodes = False; w = None; continue
        if cur is None: continue
        if re.search(r'"nodes"\s*:\s*\[', l): in_nodes = True; w = None; continue
        if in_nodes and re.match(r'^\s*\]', l): in_nodes = False; continue
        if not in_nodes: continue
        s = l.strip()
        if not s: continue
        if s.startswith('{'):
            mm = wnum.search(s)
            if mm:
                v = mm.group(1).strip('"')
                try: w = float(v)
                except: w = ('expr', v)
            continue
        if s.startswith('["id"'): continue
        if s.startswith('['):
            mm = wnum.search(s)
            ww = w
            if mm:
                v = mm.group(1).strip('"')
                try: ww = float(v)
                except: ww = ('expr', v)
            if isinstance(ww, float):
                parts[cur]['mass'] += ww
            elif ww is None:
                pass
            else:
                parts[cur]['vars'].append(ww[1])
            parts[cur]['n'] += 1
    return parts

allparts = {}
for src, t in sources():
    for k, v in parse_parts(t).items():
        v['src'] = src
        if k in allparts and allparts[k]['src'].startswith('mod:'): continue
        allparts[k] = v

def load_pc(path):
    if os.path.exists(path): return json.load(open(path, encoding='utf8'))['parts']
    return json.loads(z.read('vehicles/vivace/'+os.path.basename(path)).decode('utf8'))['parts']

rows = {}
for cfg in sys.argv[1:]:
    parts = load_pc(MOD + '/' + cfg + '.pc')
    tot = 0; lst = []; missing = []
    for slot, p in parts.items():
        if not p: continue
        if p in allparts:
            lst.append((allparts[p]['mass'], p, allparts[p]['n'], len(allparts[p]['vars'])))
            tot += allparts[p]['mass']
        else:
            missing.append(p)
    lst.sort(reverse=True)
    print('=====', cfg, 'sum of parsed node weights: %.1f kg over %d parts' % (tot, len(lst)))
    for m, p, n, nv in lst[:30]:
        print('  %7.1f  %-44s nodes=%d exprNodes=%d' % (m, p, n, nv))
    print('  parts not found in jbeam scan (no nodes / variable files):', len(missing))

print('--- probe')
for k in ['vivace_body','vivace_body_panoramic','vivace_wheeldata_F','wheel_F_5','tire_F_225_40_18_sport','vivace_brake_F_sport_r','vivace_fueltank','vivace_radiator']:
    print(k, allparts.get(k))
cfg='vivace_ea888_gti'
parts=load_pc(MOD+'/'+cfg+'.pc')
print('body slot:',parts.get('vivace_body'),'| wheels:',parts.get('wheel_F_5'),parts.get('tire_F_225_40_18_sport'))
nf=[p for p in parts.values() if p and p not in allparts]
print(nf)

if len(sys.argv)==3:
    a,b=[ {p for p in load_pc(MOD+'/'+c+'.pc').values() if p} for c in sys.argv[1:3]]
    # multiset by slot
    A=load_pc(MOD+'/'+sys.argv[1]+'.pc'); B=load_pc(MOD+'/'+sys.argv[2]+'.pc')
    print('--- diff', sys.argv[1], 'vs', sys.argv[2])
    rows=[]
    for k in sorted(set(A)|set(B)):
        pa,pb=A.get(k) or '',B.get(k) or ''
        if pa!=pb:
            ma=allparts.get(pa,{}).get('mass',0); mb=allparts.get(pb,{}).get('mass',0)
            rows.append((mb-ma,k,pa,ma,pb,mb))
    for d,k,pa,ma,pb,mb in sorted(rows,reverse=True):
        if abs(d)>0.4: print('%+7.1f  %-30s %s(%.1f) -> %s(%.1f)'%(d,k,pa,ma,pb,mb))
    print('total delta %.1f'%sum(r[0] for r in rows))
