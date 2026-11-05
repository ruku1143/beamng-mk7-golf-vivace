# Plan: Make EA888_Gen3_Vivace a Mk7 Golf GTI / GTI PP / R-accurate mod

## Context
The mod is an EA888 Gen3 swap for the base-game Vivace (FWD hatch). It is small: 4 jbeam
(`ea888_engine`, `ea888_transmissions`, `ea888_dsg_sounds`, `ea888_soundaktor`), 3 `.pc` configs
(GTI, GTI Performance, Golf R), 3 info json, 2 Lua sound controllers, sound assets. Body, suspension,
brakes, fuel tank, diffs, wheels all come from base-game `vivace.zip`
(`D:\SteamLibrary\steamapps\common\BeamNG.drive\content\vehicles\vivace.zip`, read-only, do not copy into repo).
Today the mod adds power/gearing only: vehicle mass, 50 L tank, springs, brakes and tyres are Vivace values
(the R config even uses Vivace "wide" parts, 19" wheels). Goal: real Mk7 data for chassis + drivetrain.
Decided with user: scope = data only (keep Vivace body geometry); variants = GTI (230 PS), GTI Performance
(245 PS), R (300 PS Mk7, 4Motion). Mk7.5 not in scope (existing R is 310 PS Mk7.5 -> retune to 300 PS/380 Nm;
keep the 310 calibration as an optional extra part if user wants).

> **UPDATE 2026-11-05:** user decided to cover BOTH pre-facelift (Mk7) and facelift (Mk7.5) variants. Mk7.5 is now IN scope; see the variant matrix in docs/MK7_SPEC_TARGETS.md. Wherever this plan says "Mk7.5 out of scope" or lists three variants, read it as up to six (Mk7 and Mk7.5 each: GTI, GTI Performance, R).

## Phase 0 - Foundation (first, so the next session needs no rediscovery)
1. `git init` in the mod folder + `.gitignore` (no base-game extracts, no `*.zip`, no backups). Private GitHub repo.
2. Write docs in-repo (the user's explicit request):
   - `CLAUDE.md` - short entry point: what the mod is, rules, links to docs.
   - `docs/MOD_MAP.md` - full file map, every part name/slotType, which base parts each config uses
     (content of the discovery report: tree, parts, ECU/turbo tables, gear ratios, diffs, brakes, wheels).
   - `docs/BASE_GAME_REFERENCE.md` - where base Vivace lives, which base jbeam files hold mass
     (`vivace_body.jbeam` node weights), fuel (`vivace_fueltank.jbeam`), brakes (`vivace_brakes.jbeam`),
     springs/dampers (`vivace_strut_F*.jbeam`, `vivace_spring_shock_R*.jbeam`), suspension geometry,
     diffs/final drives (`vivace_differential_F/R.jbeam`), `vivace_transfercase.jbeam`; how to read them
     without extracting (`unzip -p` / `python -I zipfile`).
   - `docs/MK7_SPEC_TARGETS.md` - the sourced target table (below) with source + confidence per number.
   - `docs/KNOWN_ISSUES.md` - gotchas found: no modinfo/info.json; referenced-but-missing
     `tools/gen_soundaktor.ps1` and `sounds_in/launch_original.wav`; GTI and GTI PP preview jpgs identical;
     gear ratios normalised to a hard-coded 4.187 final drive; ECU maps are offline-fitted `torqueModMult`
     fudge factors tied to turbo `engineDef` (retune together); jbeam missing-comma tolerance;
     one-shot SFX workaround.
   - `docs/WORKFLOW.md` - how to test (see Verification), how to package, conventions, change log.
3. Add `info.json`/modinfo metadata (title, author, version) so it is zip-ready.

## Phase 1 - Research & spec table (WebSearch, cite sources)
Build `docs/MK7_SPEC_TARGETS.md`. Starting targets from memory - ALL to be verified against VW spec sheets before use:
- Power/torque: GTI 230 PS/350 Nm; PP 245 PS/370 Nm; R (Mk7) 300 PS/380 Nm.
- Dimensions: wheelbase 2631 mm, length ~4255, width ~1799, track ~1535/1510 (varies w/ wheels).
- Kerb weight (DIN, no driver): GTI ~1,280-1,300 kg (6MT) / DSG +~20; PP ~+10; R ~1,400-1,450 kg; front/rear split ~60/40 (GTI), ~58/42 (R).
- Fuel tank: GTI 50 L, R 55 L.
- Brakes: std GTI ~312x25 vented F / 272x10 R; PP and R ~340x30 F / 310x22 R. Confirm pad/caliper type.
- Tyres: GTI 225/45R17 or 225/40R18; PP 225/40R18; R 225/40R18 (235/35R19 option).
- Gearboxes: MQ350/MQ350-6 (6MT) and DQ381/DQ250 ratios + final drives per variant; GTI PP front LSD (VAQ); R Haldex gen5 with ~rear bias limits.
- Suspension: spring rates, damper tuning, ARB sizes, ride height, camber/toe, steering ratio (Progressive steering ~13.0:1 / 2.1 turns lock-lock), GTI sport suspension -15 mm, R -20 mm.
- Top speed/limiter: GTI 250 limited, R 250 limited.

## Phase 2 - Baseline measurement
Use the game (local) to log current mod values per config: total mass, axle weights, CoG, 0-100, 100-0, top speed, skidpad.
Record in `docs/BASELINE.md` so changes are measurable.

## Phase 3 - Implementation (new mod-owned parts; never edit base game files)
All new parts live in new jbeam files under `vehicles/vivace/`, slot-compatible with the Vivace so configs just select them.
- `mk7_mass.jbeam` - mass tuning part: scale/override node weights so total = target and F/R split = target
  (use `$*` modifiers on `nodeWeight` or a ballast/adjust-node part; avoid editing body).
- `mk7_fueltank.jbeam` - `vivace_fueltank` replacement/override with 50 L (GTI/PP) and 55 L (R).
- `mk7_brakes.jbeam` - disc diameter, thickness/thermal mass, torque coefficients, front/rear bias per variant; pad parts.
- `mk7_suspension.jbeam` - front strut + rear multilink springs, dampers, ARBs, ride height, geometry variables per variant
  (GTI, PP, R); use the standard (non-wide) Vivace suspension for all three, drop the R's wide kit unless needed for tyre fitment.
- `mk7_wheels_tires.jbeam` (or `.pc` part choices) - rim sizes and tyre sizes per variant.
- Drivetrain: re-derive gear ratios + final drives from real tables (remove the hard-coded 4.187 normalisation or keep and document),
  MQ350 6MT config added for GTI (existing but unused), DSG variants, PP VAQ LSD tuning, R Haldex torque split (rear bias, preload).
- Engine: retune ECU `torqueModMult` + turbo `engineDef` to hit 230/245/300 PS and exact torque plateaus; rev limiter, idle, redline.
- `.pc` files: rewrite 3 configs (+ optional MT variants); fix info json (names, specs, weights); give GTI PP its own preview.
- Order: mass -> fuel -> tyres/wheels -> brakes -> suspension -> drivetrain -> engine retune (power last, since mass/gearing affect tune checks).

## Phase 4 - Validation
Per variant, compare in-game vs real: kerb weight, F/R split, 0-100 km/h (GTI ~6.4 DSG/6.5 MT, PP ~6.2, R ~4.6-5.0), 100-0 (~35-37 m),
top speed ~250 limiter, fuel range. Iterate until within tolerance (define +-3% in WORKFLOW.md).

## Critical files
- Modify: `vehicles/vivace/ea888_engine.jbeam`, `ea888_transmissions.jbeam`, 3x `vivace_ea888_*.pc`, 3x `info_vivace_ea888_*.json`
- New: `vehicles/vivace/mk7_*.jbeam`, docs listed above, `.gitignore`, `info.json`
- Read-only reference: base `vivace.zip` (`vivace_body.jbeam`, `vivace_fueltank.jbeam`, `vivace_brakes.jbeam`, suspension/strut/spring files, differential/transfercase files)

## Verification
- Load in BeamNG (Windows, local), check `beamng.log` for jbeam errors after each part.
- In-game: Vehicle config > part tree shows new parts; Mass & weight distribution via the debug/`Vehicle > Performance` data; dyno via Tuning/Dyno app; brake and accel tests.
- Compare against Phase-1 table; log results in `docs/VALIDATION.md`.

## GitHub / cloud question (answer)
GitHub: yes for version control and for docs persistence - recommended. Cloud editing: only partly useful.
BeamNG only runs locally on Windows, and base-game `vivace.zip` (1.1 GB, proprietary) should not be uploaded, so every test
and the base-value lookups must happen on this PC. Cloud is fine for pure research, docs and jbeam text/math (e.g. solving
torque maps) but adds sync overhead. Recommendation: keep working locally in this folder, commit/push to a private GitHub repo
for backup and history; use cloud only if you want long unattended research/spec compilation.
