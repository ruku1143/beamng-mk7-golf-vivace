# Stock Vivace values (read from vivace.zip, 2026-11-05, local session)

Source: `vehicles/vivace/*.jbeam` inside the base `vivace.zip`. Units as in file. Spring beamSpring is N/m. NOT yet measured in game
(total mass, axle split, CoG still need Phase 2 in-game baseline: node weights inherit across many files, so do not sum by hand).

## Fuel tank (`vivace_fueltank.jbeam`)
- One part `vivace_fueltank`, slotType `vivace_fueltank`. `mainTank.fuelCapacity` = **50**; variable `$fuel` default 50, max 50 (L).
- To get 55 L (Golf R) a mod-owned tank part needs `fuelCapacity` 55 and `$fuel` max/default 55; same nodes/flexbodies can be re-declared or the
  part copied. Tank nodes ft1..ft3 (0.5 kg each). Slot default comes from the vehicle part tree.

## Brakes (`vivace_brakes.jbeam`; torque uses `$brakestrength`)
| Part | Torque coef | Dia (m) | brakeMass (kg) | type | venting | split |
|---|---|---|---|---|---|---|
| brake_F | 2500 | 0.280 | 6.7 | vented-disc | 1.0 | 1 |
| brake_R | 1200 | 0.260 | 4.5 | disc | 0.8 | 0.5 |
| brake_F_sport | 3000 | 0.320 | 9.4 | vented | 1.0 | 1 |
| brake_R_sport | 1300 | 0.290 | 5.2 | disc | 0.8 | 0.4 (parking 1300) |
| brake_F_sport_r (mod GTI/R now) | 3000 | 0.355 | 10.25 | vented | 1.2 | 1 |
| brake_R_sport_r | 1400 | 0.290 | 6.0 | vented | 0.8 | 0.4 (parking 1400) |
| brake_F_race / R_race | 4600*bias / 3800-4600*(1-bias) | 0.370 / 0.310 | 11 / 6.5 | vented | 1.5 / 1.0 | 1 |
Others: `_R_E`, `_R_sport_E` (EV variants), `_F_rally`, `_R_rally`. Pads are separate `brakepad_F/R_*` slots (not in this file).

Observation: the mod's current GTI/R discs are 355 mm F / 290 mm R, larger than real Mk7 GTI (314x30 / 300x12) and even PP/R (340x30 / 310x22).
Real targets (docs/MK7_SPEC_TARGETS.md): GTI 0.314 / 0.300; PP and R 0.340 / 0.310. Torque coef should scale with disc size
(effective radius) and be calibrated against stopping distance in game; brakeMass should scale with thickness (R 22 mm vented vs 12 mm solid).

## Springs / struts (inline in part, beamSpring N/m; shock damping inline)
| Part | Spring |
|---|---|
| vivace_strut_F (front std) | 20000 |
| vivace_strut_F_sport_adaptive (mod GTI) | 30000 (adaptive damper, beamDamp 3500 etc.) |
| vivace_spring_R (rear std) | 14000 |
| vivace_spring_R_sport (mod GTI) | 22000 |
| strut_F_race / F_rally | 70000 / 40000 (variable `$spring_F_*`) |
| spring_R_race / R_rally | 35000 / 27000 |
| WIDE: spring_R_wide_race / rally | 120000 / 60000; strut_F_wide_race / rally 70000 / 40000 |
Wide-kit sport/sport_r springs (used by current Golf R) are inline: read `vivace_spring_shock_R_wide.jbeam` `vivace_spring_R_wide_sport_r` and
`vivace_strut_F_wide.jbeam` `vivace_strut_F_wide_sport_r_adaptive` before editing (not extracted yet).
Strut bump-stop limit spring 25000, shock rebound/bump damping in `beamDamp*` fields; ride height is set by `$springheight_*` on race/rally parts only.
Note: the real Mk7 has no published OEM rates (MK7_SPEC_TARGETS.md), so tune relative to these stock numbers + handling feel; the GTI sport -15 mm / R -20 mm lowering is the one sourced hook.

## Drivetrain parts
- `vivace_transfer_case_FWD`: shaft, friction 0.22.
- `vivace_transfer_case_AWD`: `splitShaft` locked, `lockTorque` 3000, friction 0.35, controller `electronicSplitShaftLock`. This is the Haldex proxy:
  lockTorque, defaultClutchRatio and the controller drive the rear bias (Haldex Gen5 target: up to ~50% rear, ~30% default under accel; both Low confidence).
- Diffs/finals in `vivace_differential_F.jbeam` / `_R.jbeam` (`_4187`, `_3389`, `_437` etc.); LSD params for the PP live in `vivace_differential_F_LSD` (preload 10, lockCoef 0.3, revLockCoef 0.05).

## Vehicle shell
- `vivace.jbeam` main part: body slot `vivace_body`, default config in info.json `vivace_S_410q_DCT`. Mass is not stated here; it is the sum of node weights from the part tree.
  Use an in-game readout (Phase 2). Mass trimming plan: add a mod part that sets `nodeWeight` modifiers or adds ballast nodes.

## Still to read (local TODO)
`vivace_spring_R_wide_sport_r`, `vivace_strut_F_wide_sport_r_adaptive`, swaybar files (grep `swaybar` returned no file by name: search `vivace_swaybar_F_sport` across the zip),
body `nodeWeight` defaults, `vivace_differential_F` final-drive part variables, pad compounds (`brakepad_F_*`) and `$brakestrength` default.
