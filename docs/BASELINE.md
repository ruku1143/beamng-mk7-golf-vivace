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
| vivace_ea888_gti | | | | | | | | | 50 (stock tank) |
| vivace_ea888_gti_performance | | | | | | | | | 50 |
| vivace_ea888_golf_r | | | | | | | | | 50 |

Real targets for comparison are in `docs/MK7_SPEC_TARGETS.md` (EU kerb includes 75 kg driver; derived DIN = EU - 75).
