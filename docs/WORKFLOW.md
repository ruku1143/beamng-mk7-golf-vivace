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
