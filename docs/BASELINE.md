# Baseline (Phase 2) - TO BE FILLED IN-GAME

Nothing here has been measured yet. This needs BeamNG running; Claude cannot drive the game itself, so the user records the numbers and pastes them back.

## Procedure (do each config: GTI, GTI Performance, Golf R)
1. Fresh spawn on a flat level (e.g. West Coast USA / Gridmap flat area). Full tank as spawned, no driver/passengers, no cargo.
2. Mass/CoG/axle split: open console (~), switch context to Vehicle, paste `docs/baseline_dump.lua`. Copy the `BASELINE` lines.
   (Script is untested; if it errors, paste the error. Fallback: Vehicle Config > Info/Debug mass readout, or the "Vehicle > Weight distribution" debug view.)
3. Performance: with ESC/TC defaults, use the Performance Tests app (or a stopwatch) for 0-100 km/h, 100-0 km/h braking distance, top speed (flat straight, e.g. Gridmap), and note launch mode used.
4. Dyno: note peak power/torque and rpm of each from the Dyno/engine app (important because the R is 310 PS Mk7.5-tuned).
5. Check `beamng.log` for jbeam warnings at spawn.

## Results (fill in)
| Config | Mass kg | Front % | CoG y/z | 0-100 s | 100-0 m | Top km/h | Peak PS @ rpm | Peak Nm @ rpm | Fuel L |
|---|---|---|---|---|---|---|---|---|---|
| vivace_ea888_gti (DSG) | 1602.4 | unreliable | | | | | | | | 50 (stock tank) |
| vivace_ea888_gti_performance (DSG) | 1605.4 | unreliable | | | | | | | | 50 |
| vivace_ea888_golf_r (DSG) | 1704.4 | unreliable | | | | | | | | 50 |

Real targets for comparison are in `docs/MK7_SPEC_TARGETS.md` (EU kerb includes 75 kg driver; derived DIN = EU - 75).

## Notes (2026-11-05)
- Masses measured in game by summing node masses with the default DRIVER in the front-left seat (user-confirmed) and default fuel. Driver mass inside the sum is ASSUMED ~75 kg, not yet measured (check: spawn with the driver removed/seat empty and compare).
- So compare to the EU kerb weight (ADAC, incl. 75 kg driver, 90% tank), NOT the derived DIN. Fuel: 50 L full ~37 kg vs ~45 L (90%) in the EU basis, a ~4 kg difference.
- Front % from the first script is WRONG (printed wheelbase 1.758-1.799 m, expected ~2.6 m); diagnostic pending.

| Config (DSG) | In game | EU kerb target | Over by |
|---|---|---|---|
| GTI (Mk7) | 1602.4 | 1370 | ~232 |
| GTI Performance (Mk7) | 1605.4 | 1402 | ~203 |
| Golf R | 1704.4 | 1505 (Mk7.5, 310 PS) / ~1450 (Mk7, low confidence) | ~199 / ~254 |

(The earlier "~300 kg over" figure was against DIN and is superseded by this table.)

## Driver mass measured (2026-11-05)
Golf R DSG with driver removed: 1620.9 kg (with driver 1704.4) => the in-game driver = **83.5 kg** (not 75). Empty-car masses (derived for GTI/PP by subtracting 83.5):
GTI ~1519, PP ~1522, R 1620.9 kg. Compare these to derived DIN (GTI DSG ~1295, PP DSG ~1327, R ~1430 Mk7.5 / ~1375 Mk7): over by ~224 / ~195 / ~190-245 kg.
Preferred basis going forward: empty car vs DIN. (EU kerb includes 75 kg driver; the game driver is 83.5 kg, so EU comparisons are ~8.5 kg pessimistic.)

## Deferred (user decision 2026-11-05)
Performance readings (0-100, 100-0, top speed, dyno) postponed to a later date. Mass baseline done; split diagnostic still pending.
- Diagnostic result: v.data.nodes[].pos is the vehicle frame (front y=-1.342, rear y=+1.338, wheelbase 2.680); obj:getNodePosition is world-oriented and WRONG for the split. Use v.data.nodes.

## Corrected split + mass methods (2026-11-05)
- Golf R (DSG), v.data.nodes method (vehicle frame): MASS 1583.4 kg, FRONT 55.6%, wheelbase 2.680 m. Assumed no driver.
- Old `obj:getNodeMass` method (1620.9 kg R empty) INCLUDES fuel: 1620.9 - 1583.4 = 37.5 kg = 50 L x 0.75. New method (`v.data.nodes[].nodeWeight`) = dry, no fuel, and matches tools/mass_scan.py (R scan 1586.1).
- So: R dry 1583.4 | + full fuel 1620.9 | + driver (83.5) 1704.4. GTI/PP dry derived: GTI 1602.4-83.5-37.5 = ~1481, PP ~1484 (derived, not measured with the new method).
- DIN/EU targets assume ~90% fuel (45 L ~ 34 kg), so compare "full tank minus ~4 kg". Gaps unchanged (~190-245 kg R).
- R static front share 55.6% (dry, empty). Real Mk7 R split unsourced (plan's 58/42 is memory). GTI/PP split still to measure with the corrected command.
