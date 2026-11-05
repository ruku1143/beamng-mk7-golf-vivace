#!/usr/bin/env python3
"""Generate extra .pc / info json / preview files from the three existing DSG configs (the Mk7.5 set).

Existing configs are used as templates and are NOT modified:
  vivace_ea888_gti, vivace_ea888_gti_performance, vivace_ea888_golf_r  (= Mk7.5, DSG)
New configs (output committed, mod-owned content): Mk7.5 manual x3, Mk7 manual x3, Mk7 R DSG.
Mk7 GTI / GTI Performance DSG (DQ250) use INFERRED, UNVERIFIED ratios (docs/GEARING_CALC.md).
Usage: python -I tools/gen_mk7_configs.py
"""
import json, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, '..', 'vehicles', 'vivace')


def load(name):
    with open(os.path.join(D, name + '.pc'), encoding='utf8') as f:
        pc = json.load(f)
    with open(os.path.join(D, 'info_' + name + '.json'), encoding='utf8') as f:
        info = json.load(f)
    return pc, info


def manual(parts, r):
    parts['vivace_shifter'] = 'vivace_shifter_M'
    parts['vivace_steer'] = 'vivace_steer_sport'
    parts.pop('vivace_dsg_sound_ea888', None)
    parts['vivace_transmission'] = 'vivace_transmission_ea888_MQ350_R' if r else 'vivace_transmission_ea888_MQ350'
    if not r:
        parts['vivace_finaldrive_F'] = 'vivace_finaldrive_F_3389'


# key, template, year-tag, label, transmission kind, ecu override, description
CONFIGS = [
    ('vivace_ea888_gti_mt',               'vivace_ea888_gti',             'Mk7.5', 'EA888 Mk7.5 GTI (230 PS) 6MT',               'mt',  None,                                  'Mk7.5 GTI 230 PS / 350 Nm, MQ350 6-speed manual.'),
    ('vivace_ea888_gti_performance_mt',   'vivace_ea888_gti_performance', 'Mk7.5', 'EA888 Mk7.5 GTI Performance (245 PS) 6MT',   'mt',  None,                                  'Mk7.5 GTI Performance 245 PS / 370 Nm, VAQ front LSD, MQ350 6-speed manual.'),
    ('vivace_ea888_golf_r_mt',            'vivace_ea888_golf_r',          'Mk7.5', 'EA888 Mk7.5 Golf R (310 PS) 6MT',            'mtr', None,                                  'Mk7.5 Golf R 310 PS, AWD, 6-speed manual (R gearing).'),
    ('vivace_ea888_mk7_gti_mt',           'vivace_ea888_gti',             'Mk7',   'EA888 Mk7 GTI (220 PS) 6MT',                 'mt',  'vivace_engine_ecu_ea888_gti_mk7',     'Mk7 (2013-16) GTI 220 PS / 350 Nm, MQ350 6-speed manual.'),
    ('vivace_ea888_mk7_gti_performance_mt', 'vivace_ea888_gti_performance', 'Mk7', 'EA888 Mk7 GTI Performance (230 PS) 6MT',     'mt',  'vivace_engine_ecu_ea888_gti',         'Mk7 (2013-16) GTI Performance 230 PS / 350 Nm, VAQ front LSD, MQ350 6-speed manual.'),
    ('vivace_ea888_mk7_golf_r_mt',        'vivace_ea888_golf_r',          'Mk7',   'EA888 Mk7 Golf R (300 PS) 6MT',              'mtr', 'vivace_engine_ecu_ea888_r_mk7',       'Mk7 (2014-16) Golf R 300 PS / 380 Nm, AWD, 6-speed manual (R gearing).'),
    ('vivace_ea888_mk7_gti_dsg',         'vivace_ea888_gti',             'Mk7',   'EA888 Mk7 GTI (220 PS) DSG [ratios unverified]',  'dq250g', 'vivace_engine_ecu_ea888_gti_mk7',  'Mk7 (2013-16) GTI 220 PS / 350 Nm, DQ250 6-speed DSG. CAVEAT: gear ratios are INFERRED (low confidence), see docs/GEARING_CALC.md.'),
    ('vivace_ea888_mk7_gti_performance_dsg', 'vivace_ea888_gti_performance', 'Mk7', 'EA888 Mk7 GTI Performance (230 PS) DSG [ratios unverified]', 'dq250g', 'vivace_engine_ecu_ea888_gti', 'Mk7 (2013-16) GTI Performance 230 PS / 350 Nm, VAQ LSD, DQ250 6-speed DSG. CAVEAT: gear ratios are INFERRED (low confidence), see docs/GEARING_CALC.md.'),
    ('vivace_ea888_mk7_golf_r_dsg',       'vivace_ea888_golf_r',          'Mk7',   'EA888 Mk7 Golf R (300 PS) DSG',              'dq250', 'vivace_engine_ecu_ea888_r_mk7',     'Mk7 (2014-16) Golf R 300 PS / 380 Nm, AWD, DQ250 6-speed DSG.'),
]


def main():
    for key, tmpl, tag, label, kind, ecu, desc in CONFIGS:
        pc, info = load(tmpl)
        parts = pc['parts']
        if kind == 'mt':
            manual(parts, False)
        elif kind == 'mtr':
            manual(parts, True)
        elif kind == 'dq250g':
            parts['vivace_transmission'] = 'vivace_transmission_ea888_DQ250_GTI'
        elif kind == 'dq250':
            parts['vivace_transmission'] = 'vivace_transmission_ea888_DQ250_R'
        if ecu:
            parts['vivace_engine_ecu_ea888'] = ecu
        pc['Configuration'] = key
        info['Configuration'] = label
        info['Description'] = desc + ' Mk7 spec data: see docs/MK7_SPEC_TARGETS.md.'
        info['Transmission'] = 'Automatic' if kind.startswith('dq250') else 'Manual'
        if 'defaultMultiPaintSetup' in info:
            info['defaultMultiPaintSetup']['name'] = key + ' Multi Paint Setup'
        with open(os.path.join(D, key + '.pc'), 'w', encoding='utf8', newline='\n') as f:
            json.dump(pc, f, indent=2)
            f.write('\n')
        with open(os.path.join(D, 'info_' + key + '.json'), 'w', encoding='utf8', newline='\n') as f:
            json.dump(info, f, indent=2)
            f.write('\n')
        shutil.copyfile(os.path.join(D, tmpl + '.jpg'), os.path.join(D, key + '.jpg'))
        print('wrote', key)


if __name__ == '__main__':
    main()
