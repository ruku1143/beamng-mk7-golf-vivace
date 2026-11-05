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

## Update: runtime mass scaling is feasible (2026-11-05)
- jbeam cannot edit another part's nodeWeight (no `"nodeWeight":"$..."` expressions exist in the whole base Vivace; counted 0), BUT the game's vehicle Lua has
  `obj:setNodeMass(cid, m)`, `obj:getNodeMass(cid)`, `obj:getOriginalNodeMass(cid)` (used in lua/vehicle/beamstate.lua, energyStorage/fuelTank.lua, interactCargoContainers.lua).
- Plan: mod-owned auxiliary controller (same pattern as ea888DsgSounds.lua) run at init that scales node masses toward a per-variant dry-mass target. No base files touched, shippable.
- Targets (dry = DIN - ~34 kg fuel): GTI ~1261 (k~0.85 from 1481), PP ~1293 (k~0.87), R Mk7 ~1341 / Mk7.5 ~1396 (k~0.85 / 0.88). Refine by excluding wheels/engine nodes and fuel tank nodes (tank sets its own mass from a cached base value).
- Caveats to test: ride height rises and suspension frequency changes with lighter sprung mass (springs are fixed N/m); beam strengths unchanged; fuel-node mass handling; order vs other init controllers.
- Test 1 (console, UNTESTED): scale all nodes by 0.85 and print totals, then drive.

## RESULT of console runtime scaling tests (2026-11-05, GTI) - FAILED, DO NOT REPEAT
- Test 1: setNodeMass x0.85 on ALL nodes mid-session -> wheels fell off. (getNodeMass readback does not refresh immediately: showed before=after.)
- Test 2: setNodeMass x0.90 on 370 body-type nodes (862.1 -> 775.9 kg, cut 86.2) via partOrigin filter -> body came apart (doors, tailgate, bonnet flung open, rear panels torn). Unknown whether the user respawned first.
- Conclusion: changing node mass on a live, settled car breaks it. Cause unproven (latch/joint force spikes, or beam stiffness vs lighter nodes). Do NOT assume a spawn-time controller or a regenerated lighter body is safe: both change k/m of the structure. Test any further approach from a fresh spawn with a SMALL cut (<=5%) first, and keep every test on a throwaway spawn.
- Context: the Vivace body (417 kg nodes) is a big hatch; real Golf is ~15% lighter. A ~220 kg cut (~25% of the body-type nodes) is a large physics change, so mass may have to be only partly corrected.
