#!/usr/bin/env python3
"""Generate the extra gearbox parts (Golf R sets, DQ250) by cloning this mod's OWN DQ381 / MQ350 parts.

Output: vehicles/vivace/ea888_transmissions_mk7.jbeam (committed: it only contains mod-owned content).
Ratios = overall / FD_REF, where the config uses the matching final-drive part (4.37 for the R; see docs/GEARING_CALC.md).
Sources and confidence: docs/GEARING_CALC.md and docs/MK7_SPEC_TARGETS.md (R 6MT and DQ381 = VW sheet; DQ250 R = FCP + Derhase, M-H;
DQ381 final-drive assignment and DQ250 reverse are INFERRED).
Usage: python -I tools/gen_mk7_gearboxes.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'vehicles', 'vivace', 'ea888_transmissions.jbeam')
OUT = os.path.join(HERE, '..', 'vehicles', 'vivace', 'ea888_transmissions_mk7.jbeam')
FD_REF = 4.37  # default reference final drive (R configs use the 4.37 part)
FD_GTI = 4.187  # GTI configs use the 4.187 part


def overall_to_ratios(rev, fwd, ref=None):
    ref = ref or FD_REF
    vals = [-rev, 0.0] + list(fwd)
    return [round(v / ref, 3) if v else 0 for v in vals]


def fmt(a):
    return '[' + ', '.join(('%g' % x) for x in a) + ']'


# overall ratios (gear x its final drive)
R_DQ381 = ([3.19 * 4.47, 2.75 * 3.30, 1.90 * 3.30, 1.04 * 4.47, 0.79 * 4.47, 0.86 * 3.30, 0.66 * 3.30], 2.90 * 4.47)
R_MQ350 = ([3.36 * 4.24, 2.09 * 4.24, 1.48 * 4.24, 1.09 * 4.24, 1.10 * 3.27, 0.91 * 3.27], 3.99 * 3.27)
# INFERRED (LOW confidence): Mk6/Mk7-era 02E/DQ250 set 3.462/2.050/1.300/0.902/0.914/0.756 with finals 4.118 (1-4) / 3.043 (5,6).
# That set was only found as a TDI Passat example (gearboxlist), NOT as a verified Mk7 GTI table. Reverse overall 12.1 is an assumption.
GTI_DQ250 = ([3.462 * 4.118, 2.050 * 4.118, 1.300 * 4.118, 0.902 * 4.118, 0.914 * 3.043, 0.756 * 3.043], 12.1)
R_DQ250 = ([2.92 * 4.77, 1.83 * 4.77, 1.31 * 4.77, 0.97 * 4.77, 1.04 * 3.44, 0.81 * 3.44], 13.0)  # reverse: assumed, no source

PARTS = [
    # new name, template part, display name, (fwd overall, rev overall), comment, extra substitutions
    ('vivace_transmission_ea888_DQ381_R', 'vivace_transmission_ea888_DQ381', 'DQ381 7-Speed DSG (Golf R gearing)', R_DQ381,
     'Golf R DQ381: gears 3.19/2.75/1.90/1.04/0.79/0.86/0.66 R 2.90, finals 4.47 (1,4,5,R) / 3.30 (2,3,6,7) - assignment INFERRED. Use the 4.37 final drive part.', None),
    ('vivace_transmission_ea888_MQ350_R', 'vivace_transmission_ea888_MQ350', 'MQ350 6-Speed Manual (Golf R gearing)', R_MQ350,
     'Golf R 6MT (0FB): gears 3.36/2.09/1.48/1.09/1.10/0.91 R 3.99, finals 4.24 (1-4) / 3.27 (5,6,R). Use the 4.37 final drive part.', None),
    ('vivace_transmission_ea888_DQ250_GTI', 'vivace_transmission_ea888_DQ381', 'DQ250 6-Speed DSG (Mk7 GTI, RATIOS UNVERIFIED)', GTI_DQ250,
     'UNVERIFIED / INFERRED Mk7 GTI DQ250: gears 3.462/2.050/1.300/0.902/0.914/0.756, finals 4.118 (1-4) / 3.043 (5,6), reverse 12.1 overall assumed. Source is a Passat 02E example, not a GTI table. Use the 4.187 final drive part. See docs/GEARING_CALC.md.',
     {'lowShiftDownRPM': '[0,0,0,1400,1500,1400,1400,1400]', 'lowShiftUpRPM': '[0,0,2600,2300,2100,2000,1900]'}, FD_GTI),
    ('vivace_transmission_ea888_DQ250_R', 'vivace_transmission_ea888_DQ381', 'DQ250 6-Speed DSG (Mk7 Golf R gearing)', R_DQ250,
     'Mk7 Golf R DQ250: gears 2.92/1.83/1.31/0.97/1.04/0.81, finals 4.77 (1-4) / 3.44 (5,6). Reverse 13.0 overall is an ASSUMPTION. Use the 4.37 final drive part.',
     {'lowShiftDownRPM': '[0,0,0,1400,1500,1400,1400,1400]', 'lowShiftUpRPM': '[0,0,2600,2300,2100,2000,1900]'}),
]


def split_parts(text):
    lines = text.replace('\r\n', '\n').split('\n')
    heads = [i for i, l in enumerate(lines) if re.match(r'^"[A-Za-z0-9_]+"\s*:\s*\{\s*$', l)]
    out = {}
    for n, i in enumerate(heads):
        end = heads[n + 1] if n + 1 < len(heads) else len(lines)
        chunk = lines[i:end]
        # drop file-closing brace and trailing blanks
        while chunk and chunk[-1].strip() in ('', '}') and not chunk[-1].startswith('},') :
            if chunk[-1].strip() == '}' and len(chunk) > 1 and chunk[-2].strip() == '},':
                chunk.pop(); break
            chunk.pop()
        name = re.match(r'^"([A-Za-z0-9_]+)"', lines[i]).group(1)
        out[name] = '\n'.join(chunk)
    return out


def sub1(pat, repl, s):
    new, n = re.subn(pat, repl, s, count=1)
    if n != 1:
        raise SystemExit('pattern not found: ' + pat)
    return new


def main():
    src = open(SRC, encoding='utf8').read()
    parts = split_parts(src)
    blocks = []
    for spec in PARTS:
        new, tmpl, title, (fwd, rev), comment, extra = spec[:6]
        ref = spec[6] if len(spec) > 6 else None
        b = parts[tmpl]
        b = sub1(r'^"%s"' % re.escape(tmpl), '"%s"' % new, b)
        b = sub1(r'("name"\s*:\s*)"[^"]*"', r'\1"%s"' % title, b)
        b = re.sub(r'\n[ \t]*//Mk7\.5 GTI[^\n]*', '', b)
        b = re.sub(r'\n[ \t]*//overall:[^\n]*', '', b)
        b = re.sub(r'\n[ \t]*//values below[^\n]*', '', b)
        ratios = overall_to_ratios(rev, fwd, ref)
        b = sub1(r'"gearRatios"\s*:\s*\[[^\]]*\]', '//%s\n        "gearRatios":%s' % (comment, fmt(ratios)), b)
        if extra:
            for k, v in extra.items():
                b = sub1(r'"%s"\s*:\s*\[[^\]]*\]' % k, '"%s":%s' % (k, v), b)
        b = b.rstrip().rstrip(',') + ','
        blocks.append(b)
        print(new, fmt(ratios))
    with open(OUT, 'w', encoding='utf8', newline='\n') as f:
        f.write('// GENERATED by tools/gen_mk7_gearboxes.py from ea888_transmissions.jbeam (mod-owned content only). Edit the script, not this file.\n{\n')
        f.write('\n'.join(blocks))
        f.write('\n}\n')
    print('wrote', os.path.normpath(OUT))


if __name__ == '__main__':
    main()
