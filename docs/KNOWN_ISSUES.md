# Known issues / gotchas

1. No `info.json`/modinfo, README or licence in the mod (no version/author/title). Sample credit only in jbeam strings.
2. `ea888_soundaktor.jbeam` references `tools/gen_soundaktor.ps1`; `ea888_dsg_sounds.jbeam` references `sounds_in/launch_original.wav`. Neither is shipped.
3. `vivace_ea888_gti.jpg` and `vivace_ea888_gti_performance.jpg` are both 54314 bytes (likely identical) - give PP its own preview.
4. Gear ratios are baked: overall ratios divided by a fixed 4.187 (DQ381) / 3.389 (MQ350). The R pairs these with `_437` finals on purpose; changing final drive changes everything.
5. ECU `torqueModMult` maps are offline-fitted fudge factors against the turbo `engineDef` tables. Change either and the power curve breaks - retune both together.
6. Golf R config uses the Vivace "wide" kit and 19" wheels - not Mk7 accurate (Mk7 R: 225/40R18, 19" optional). Also still selects `vivace_DSE_TC_FWD` on an AWD car.
7. jbeam files contain missing trailing commas (e.g. `deformGroups` lines, `"ICE": true` then `"EV": false`); BeamNG's parser tolerates this. Don't "fix" blindly. Mod uses `$+maxLoadMix` / `$*` operators in turbo/long-block parts.
8. Sound: looping SFX played raw WAVs wrongly on this game version, so both Lua controllers use overlapping `playSFXOnceCT` one-shots (may stutter).
9. MQ350 manual exists but no config uses it; GTI real cars have 6MT option.
10. R is currently Mk7.5 310 PS/400 Nm; project target is Mk7 300 PS/380 Nm.
11. Total vehicle mass, fuel (50 L) and all suspension/brake values are base Vivace, not Golf.
- Mk7 GTI/PP DSG gear ratios are INFERRED from a Passat 02E example (see GEARING_CALC.md); replace when a real GTI DQ250 table is found.
- EXTERNAL MOD DEPENDENCIES (added 2026-11-06): all 12 configs now require two other BeamNG repo mods, both installed/enabled on the user's PC: `vivace_steeringwheels_sk` (parts vivace_steer_Sport_round = manual, vivace_steer_Sport_round_paddles = DSG) and `subieberry_vivace_arsenic_int_alt` (skin_interior_arsca, "Arsenic without green accents"). Without them the configs lose those parts (wheel/interior fall back or error). Wheel rule: paddles on DSG, no paddles on manual.
