# Gearing maths

Pure maths, no game needed. Real ratio sources are still missing (see MK7_SPEC_TARGETS.md), so this records the method and the mod's CURRENT numbers.

## Mod convention
`gearRatios[i] = overall[i] / FD_ref`, where FD_ref is the final-drive part the config selects
(DQ381: 4.187 via `_4187`; MQ350: 3.389 via `_3389`; the Golf R uses `_437`). In-game overall = `gearRatios[i] * FD_part`.
Check: with the R's 4.37 final, DQ381 overall is 4.37/4.187 = 1.044x the GTI's, i.e. ~4.4% shorter.

## Current overall ratios (derived, unmodified mod)
| Gear | R | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| DQ381 (x4.187) | -12.092 | 14.177 | 8.608 | 5.539 | 3.877 | 2.918 | 2.378 | 2.001 |
| MQ350 (x3.389) | -11.923 | 12.214 | 6.771 | 4.762 | 3.531 | 2.881 | 2.382 | - |

## Converting real data
Given a real set of gear ratio `g_i` and the final drive(s) `F` for that gear (DQ250/DQ381/MQ350 have two output shafts, so `F` differs by gear):
1. overall_i = g_i * F_i
2. mod value = overall_i / FD_ref (keep the existing convention) - or set FD_ref = 1 and use a 1.0 final-drive part.
3. Top-gear check: rpm = v / circumference * overall * 60. With 225/40R18 (rolling circ ~2.002 m) at 250 km/h:
   DQ381 7th (2.001 overall) = ~4170 rpm; MQ350 6th (2.382) = ~4960 rpm. Real limiter-speed rpm is not sourced, so these are only a sanity check on the current gearing.
4. Tyre circumference: C = 2*pi*(rim_in*25.4/2 + aspect*width)/1000 m. 225/45R17 ~1.97 m, 225/40R18 ~2.00 m, 235/35R19 ~2.01 m.

## Candidate real gear sets (secondary sources, 2026-11-05 research pass)
Overall = gear x final drive (FD differs for gears 1-4 and 5-6 on MQ350/DQ250).
| Set | Ratios 1-6 | FD (1-4 / 5-6) | Overall 1-6 | Conf / source |
|---|---|---|---|---|
| GTI 6MT (MQ350) | 3.77 / 2.09 / 1.47 / 1.09 / 1.10 / 0.91 (vwvortex snippet: 3.76/2.08/1.46/1.08/1.09/0.91) | 3.24 / 2.62 | 12.21 / 6.77 / 4.76 / 3.53 / 2.88 / 2.38 | L-M, Derhase sheet + vwvortex snippets |
| R 6MT (0FB) | 3.36 / 2.09 / 1.48 / 1.09 / 1.10 / 0.91 | 4.24 / 3.27 | 14.25 / 8.86 / 6.28 / 4.62 / 3.60 / 2.98 | M-H, FCP Euro + Derhase sheet, matches Mk5/6 02Q 72:17, 72:22 |
| R DQ250 6DSG | 2.92 / 1.83 / 1.31 / 0.97 / 1.04 / 0.81 | 4.77 / 3.44 | 13.93 / 8.73 / 6.25 / 4.63 / 3.58 / 2.79 | M-H, same |
| GTI DQ250 | not found (gearboxlist 02E example 3.462/2.050/1.300/0.902/0.914/0.756, FD 4.118/3.043 is a TDI Passat) | | | L |
| DQ381 (Taos table) | 3.190 / 2.750 / 1.897 / 1.040 / 0.793 / 0.860 / 0.661, rev 2.900 | 4.813 / 3.667 (gearboxlist) or 4.47 / 3.30 (FCP Euro R 7.5) | 6th > 5th: suspect | L |
| GTI DQ381 top gear | 0.64 with FD ~3.11-3.13 => overall 2.00 (~2000 rpm at 75 mph) | | | L, snippets |

**Key finding: the mod's CURRENT MQ350 ratios already match the GTI 6MT set** (3.77x3.24=12.215, 2.09x3.24=6.772, 1.47x3.24=4.763, 1.09x3.24=3.532, 1.10x2.62=2.882, 0.91x2.62=2.384 vs mod 12.214/6.771/4.762/3.531/2.881/2.382).
The mod's DQ381 7th (overall 2.001) matches 0.64 x 3.13 = 2.00. So the previous author likely used real GTI data; the mod's current gearing is plausible for the Mk7.5 GTI.
Still to source: Mk7 DQ250 GTI/PP ratios, PP MQ350 (same as GTI?), R DQ381 overall, reverse ratios, rev limiter.
Tyre circumference (nominal): 225/45R17 1.993 m, 225/40R18 2.002 m, 235/35R19 2.033 m.

## Open items
- Real per-variant ratios and final drives: blocked, needs a VW SSP/spec sheet (see MK7_SPEC_TARGETS.md "Still unsourced").
- Brake torque scaling from disc size, mass-delta budget, fuel-tank litres: wait for baseline numbers from the local session (stock Vivace values unknown here).
