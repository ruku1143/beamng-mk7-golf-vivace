# Workflow

## Project phases (approved plan)
0. Foundation: git + docs (this folder) + modinfo/info.json
1. Research: fill docs/MK7_SPEC_TARGETS.md with sourced numbers
2. Baseline: log current mass, axle split, CoG, 0-100, 100-0, top speed per config in docs/BASELINE.md
3. Implement via NEW mod-owned parts (`vehicles/vivace/mk7_*.jbeam`): mass -> fuel -> wheels/tyres -> brakes -> suspension -> drivetrain -> engine retune
   (mass tuning via `$*` node weight modifiers or an adjust part; fuel tank; brakes; suspension; gearing/diffs; ECU+turbo retune LAST)
4. Validate in game, tolerance +-3% vs target; log in docs/VALIDATION.md

## Testing
- Game runs locally on Windows only. Mod is unpacked in the live dir, so respawn the vehicle (or restart) after edits.
- Check `C:\Users\lukem\AppData\Local\BeamNG\BeamNG.drive\current\beamng.log` for jbeam errors after each change.
- Use Vehicle config / part tree to confirm parts, the Dyno/performance apps for power, the debug mass display for weight/axle split.

## Packaging
Zip the mod root so `vehicles/` and `art/` are at the zip root (plus info.json). Exclude `docs/`, `.git`, `CLAUDE.md`.

## Conventions
- Never modify base game files. New parts only; name `vivace_mk7_*` / `mk7_*`.
- One subsystem per change; record before/after below.

## Change log
- 2026-11-05: docs created from discovery; no mod behaviour changed yet.
- 2026-11-05: Phase 1 spec research filled in docs/MK7_SPEC_TARGETS.md; added docs/GEARING_CALC.md. Docs only, no mod behaviour changed.
- 2026-11-05 (local): added docs/BASE_VALUES.md (stock Vivace fuel/brake/spring values). No mod behaviour changed.
- 2026-11-05: Wide Phase 1 research merged (variants, weights, brakes, gearing, engine). Docs only.
- 2026-11-05 (local): added docs/BASELINE.md procedure + docs/baseline_dump.lua (UNTESTED). Baseline NOT measured: needs the user to run the game and paste results.
- 2026-11-05 (local): baseline masses measured: GTI 1602.4, PP 1605.4, R 1704.4 kg (DSG). Split script bugged; ~300 kg over real.
- 2026-11-05 (local): correction: in-game masses include the default driver, so target is EU kerb weight. Gaps now ~200-250 kg, not ~300.
- 2026-11-05 (local): measured driver = 83.5 kg (R empty 1620.9 kg). Empty-car gaps vs DIN: GTI ~224, PP ~195, R ~190-245 kg.
- 2026-11-05 (local): added tools/mass_scan.py + docs/MASS_FINDINGS.md: mass is the Vivace body/chassis, not the engine swap (engine/turbo/DQ381 equal base parts). Method for cutting ~200 kg still open.

## Generated base-game derivatives (policy, 2026-11-05)
- Files generated from the user's own vivace.zip (e.g. a lightened body) go in vehicles/vivace/generated/ and are gitignored. NEVER commit them, and exclude them from any zip you share. The generator script lives in tools/ (no base data inside). Use NEW part names, not base names, so the stock Vivace is unaffected.
- 2026-11-05 (local): MASS PARKED (runtime scaling broke the car, see MASS_FINDINGS.md). Added tools/gen_mk7_parts.py (generates vehicles/vivace/generated/mk7_parts.generated.jbeam from the local vivace.zip; gitignored). New parts: vivace_brake_F/R_mk7_gti (314x30 / 300x12), vivace_brake_F/R_mk7_pp (340x30 / 310x22), vivace_fueltank_mk7_55. GTI .pc -> mk7_gti brakes; PP and R .pc -> mk7_pp brakes; R .pc -> 55 L tank. Brake torque/mass are FIRST ESTIMATES (torque ~9000*d front, ~4500*d rear), UNTESTED in game.

## BUILD STEP (required): generated parts
The .pc configs reference parts that exist only in the generated file. After a fresh clone, or a game update, run:
    python -I tools/gen_mk7_parts.py
(needs the local BeamNG install; default zip path is D:\SteamLibrary\...\vivace.zip, or pass the path as argument). Without it the configs fail to load those parts.
Never commit or ship vehicles/vivace/generated/.
- 2026-11-05 (local): user tested the three configs in game: spawn OK, Mk7 brakes + R 55 L tank show correctly, brakes feel fine (no log errors reported). Torque values still unverified by measurement.
- 2026-11-05 (local): tyre review, NO change made. GTI/PP already 225/40R18 on 18x8 = matches Mk7 (R std is the same size). Base game has no 235/35R19; only 245/35R19 (19x9), which the R keeps. The R is on the Vivace WIDE kit because AWD needs the multilink rear (narrow rear = torsion beam, 14 nodes); moving the R to 18" or narrow parts is a bigger change (real Mk7 R track 1541/1515 is ~ GTI's 1538/1516) - left for a later decision. Tyre grip/compound not compared to real cars.
- 2026-11-05 (local): added Mk7 ECUs (ea888_engine_mk7.jbeam), R/DQ250 gearboxes (ea888_transmissions_mk7.jbeam via tools/gen_mk7_gearboxes.py) and 7 generated configs (tools/gen_mk7_configs.py); see docs/CONFIGS.md. ALL UNTESTED IN GAME. Mk7 GTI/PP DSG not built (no DQ250 GTI ratios).
- 2026-11-05 (local): user spawned and drove the 7 new configs: all work (no errors reported). Performance, gearing feel and ECU power still unmeasured.
- 2026-11-05 (local): Mk7.5 R DSG switched to DQ381_R gearing (UNTESTED). Added inferred DQ250_GTI gearbox + 2 Mk7 GTI/PP DSG configs (ratios UNVERIFIED, caveated in names/docs). Added lua/vehicle/extensions/ea888PerfLogger.lua + docs/PERFORMANCE.md (UNTESTED). Now 12 configs.
