# Where the extra weight is (2026-11-05)

Method: `tools/mass_scan.py <config> [config2]` sums `nodeWeight` per part for a config's parts from the base `vivace.zip`, `common.zip` and this mod
(run with `python -I tools/mass_scan.py vivace_ea888_gti`). It reproduces the in-game masses closely, so it can be trusted for ranking:
| Config | Scan (kg) | Measured empty (kg) | Diff |
|---|---|---|---|
| GTI | 1507.3 | ~1519 (derived) | ~12 (tyres etc. not parsed) |
| Golf R | 1586.1 | 1620.9 | ~35 (bigger 19" tyres etc.) |
Limits: partial parser (parts with expression-based weights/no nodes show 0), tyres not counted, stock .pc files only list non-default parts.

## Finding: the swap is NOT the problem
The mod's `vivace_engine_ea888` (115.5 kg) and turbo (16.3 kg) are an exact copy of the base `vivace_engine_i4_2.0_petrol` (115.5) and turbo (16.3).
DQ381 (25 kg) = base `vivace_transmission_7DCT` (25). The excess is the Vivace itself, not the engine swap.

## GTI heaviest parts (kg, node weight)
Body 417, engine 115.5, front suspension 108, dash 76, rear suspension 70, glass 40+23+16, diff 32, seats 31+31+32, tailgate 31, DQ381 25, hood 21,
wheels 20+20 (tyres extra), turbo 16, doors ~12-13 each + door panels ~15.5 each, bumpers ~15-16, exhaust 18.
Golf R adds: wide suspension (+13 rear/+0.4 front), rear diff 31, AWD transfer case 9, wide panels. Occupant nodes: 5.1 kg each x4 (in config).

## Gap
Empty car in game vs real DIN: GTI ~1519 vs ~1295 (~224 over), PP ~1522 vs ~1327 (~195), R 1620.9 vs ~1375-1430 (~190-245).
Roughly 14-15% of the car. The body shell (417 kg), chassis/suspension (~180-230 kg) and dash/seats/glass are where the mass is.

## Open question (needs a decision/test before building mass.jbeam)
How to cut ~200 kg in a mod-owned way without copying base-game files:
1. A mod part cannot change another part's `nodeWeight`; check whether jbeam/slot variable operators (`$*`) or a global mass scale can scale existing nodes (UNTESTED).
2. Override the body part with a scaled copy: simple but copies base-game data into the mod (licensing/redistribution concern) - avoid or generate at build time from the user's own install.
3. Reduce mass by dropping optional heavy parts per config (e.g. panoramic roof/glass, rear seats, undertray), which only gets part of the way.
4. Accept lighter-than-stock mass by editing only mod-owned parts (engine mounts, etc.): negligible.
Real car also ~83.5 kg driver vs 75 kg assumed (measured in game).
