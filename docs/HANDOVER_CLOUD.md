# Handover: local session -> cloud session

Written 2026-11-05. Read `CLAUDE.md`, then `docs/PLAN.md` (approved plan), then this file.

## State
- Phase 0 (docs, git) DONE and pushed. No mod behaviour has changed. All mod files are unmodified from the original.
- Phase 1 (verify Mk7 specs) is NOT started: `docs/MK7_SPEC_TARGETS.md` holds unverified memory values.
- Decisions made with the user: scope = data only (keep Vivace body); variants = GTI 230 PS, GTI Performance 245 PS, R 300 PS (Mk7, not 7.5).

## What the cloud session CAN do (no game, no base-game files there)
1. Phase 1: web-research and fill `docs/MK7_SPEC_TARGETS.md` for every row, with a source URL and confidence per number.
   Add the missing rows: gear ratios + final drives per gearbox (MQ350-6, DQ250, DQ381) and variant, spring rates, damper tuning,
   ARB diameters, ride height, camber/toe, steering ratio, Haldex rear bias, VAQ LSD behaviour, kerb weights and axle loads per variant
   (state DIN vs EU, with/without driver), tyre/wheel options per trim, brake disc sizes.
2. Pre-compute numbers for later (pure maths, no game): overall -> normalised gear ratios for the mod's `/4.187` convention,
   mass-delta budget per variant, brake torque scaling from disc size, fuel-tank litres.
3. Draft (do not rely on) new part jbeam text under `vehicles/vivace/mk7_*.jbeam` ONLY if clearly marked UNTESTED in the file header and commit message.
4. Keep docs updated; add entries to the change log in `docs/WORKFLOW.md`.

## What the cloud session CANNOT do
- Run BeamNG, read `vivace.zip` (1.1 GB proprietary, only on the user's PC at `D:\SteamLibrary\steamapps\common\BeamNG.drive\content\vehicles\vivace.zip`), or measure baselines.
- So anything needing base Vivace values (stock mass, axle split, existing spring rates, brake torque constants, `$brakestrength` meaning, slot override behaviour) is a TODO for the local session. List such needs in the "Local session TODO" section below.
- Never upload or commit base-game files.

## Rules (same as local)
- Never edit base-game files; new mod-owned parts only. Do not change existing ECU/turbo/gear values until baseline exists.
- Mark any unverified number as such. Do not invent specs; if no source, write "no source found".
- Small commits, clear messages; push to `main` of ruku1143/beamng-mk7-golf-vivace (pull first - local may have pushed).

## Suggested first tasks, in order
1. Fill the Phase 1 table (biggest value, needs only the web).
2. Add the extra rows listed above.
3. Write `docs/GEARING_CALC.md` with the ratio maths.
4. Update "Local session TODO" with exactly what to measure/read when the user returns.

## Local session TODO (cloud session appends here)
- [ ] Phase 2 baseline per config: mass, axle split, CoG, 0-100, 100-0, top speed
- [ ] Read stock Vivace mass, fuel tank, brake and suspension constants from vivace.zip (see docs/BASE_GAME_REFERENCE.md)
- [ ] Check slot-override behaviour for mass/fuel/brake parts
- [ ] Test any UNTESTED jbeam drafts in game and check beamng.log
- [x] 245 PS / DQ381 are Mk7.5: user chose to cover BOTH Mk7 and Mk7.5 (variant matrix in MK7_SPEC_TARGETS.md)
- [ ] Cloud: verify Mk7 GTI 220 PS and R facelift 310/300 PS figures; research per-facelift kerb weights and DQ250 ratios
- [ ] Find real gear ratios/final drives (VW SSP or spec sheet; golfmk7.com / vwvortex threads were 403 from the cloud) - needs a normal browser
- [ ] Read stock Vivace spring/ARB/brake values; suspension rates have no OEM source, so tune relative to Vivace stock

## Cloud session log (append dated entries)

- 2026-11-05: Phase 1 research done via 3 web agents. Filled MK7_SPEC_TARGETS.md (sources + confidence, gaps marked) and wrote GEARING_CALC.md. No mod files touched. Biggest gaps: gear ratios, kerb weight basis, axle split, spring rates.
- 2026-11-05: Scope widened by user to pre- and post-facelift (6 variants); docs updated, no mod changes.
- 2026-11-05: Kerb weights researched (5-door EU/UK, ADAC EU basis); see MK7_SPEC_TARGETS.md. Still missing: F/R split (any variant), DIN figures, Mk7 R 5-door MT, Mk7.5 R MT, Mk7.5 GTI ADAC.
- 2026-11-05 (local): pulled cloud research. Read stock Vivace fuel/brake/spring/transfer-case values from vivace.zip into docs/BASE_VALUES.md. Found: current mod GTI/R discs (355/290 mm) are bigger than the real Mk7 (314/300 base; 340/310 PP/R); fuel tank is a single part (fuelCapacity 50, $fuel max 50). Still local-only: in-game baseline, swaybar + wide sport_r spring values, body mass.
- 2026-11-05: Second research pass (5 agents): kerb weights (ADAC EU, car-only = -75), gear ratios, engine codes, brakes, wheels, chassis. MK7_SPEC_TARGETS.md rewritten; GEARING_CALC.md notes the mod's MQ350/DQ381 already match real GTI sets. Pages cloud could not load are listed at the foot of MK7_SPEC_TARGETS.md for the user to paste.
