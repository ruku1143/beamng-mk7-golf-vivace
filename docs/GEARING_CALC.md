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

## Open items
- Real per-variant ratios and final drives: blocked, needs a VW SSP/spec sheet (see MK7_SPEC_TARGETS.md "Still unsourced").
- Brake torque scaling from disc size, mass-delta budget, fuel-tank litres: wait for baseline numbers from the local session (stock Vivace values unknown here).
