# Mod map (discovered 2026-11-05)

Root: `...\BeamNG.drive\current\mods\unpacked\EA888_Gen3_Vivace`. No README/info.json/modinfo existed before docs.

## Tree
```
art/sound/blends/        ea888_eng, ea888_exh, ea888_exh_sport .sfxBlend2D.json
art/sound/engine/        ea888_eng (18 wav), ea888_exh (21), ea888_exh_sport (21), ea888_soundaktor (12 grain wav)
vehicles/common/ea888_sounds/   DSG_Farts.ogg, DSG_Farts_INT.ogg, launch_grain.wav
vehicles/vivace/
  ea888_engine.jbeam  ea888_transmissions.jbeam  ea888_dsg_sounds.jbeam  ea888_soundaktor.jbeam
  info_vivace_ea888_{gti,gti_performance,golf_r}.json   + matching .jpg
  vivace_ea888_{gti,gti_performance,golf_r}.pc
  lua/controller/ea888DsgSounds.lua  ea888Soundaktor.lua
```
No suspension/brake/body/tyre/wheel/fuel jbeam exists in the mod: all come from base `vivace.zip`.

## Parts
### ea888_engine.jbeam
- `vivace_engine_ea888` (slotType `vivace_engine`): copy of stock 2.0 I4 nodes/beams/flexbodies. Sub-slots:
  `vivace_enginemounts`, `vivace_oilpan`, `n2o_system`, `vivace_intake_ea888` (default IS20),
  `vivace_engine_ecu_ea888` (default _gti), `vivace_engine_internals_ea888` (default _gti),
  `vivace_engine_sound_ea888` (default _stock), `vivace_soundaktor_ea888`, `vivace_transmission` (default DQ381).
- Turbos (slotType `vivace_intake_ea888`): `vivace_turbo_ea888_IS20`, `vivace_turbo_ea888_IS38`.
- ECUs (slotType `vivace_engine_ecu_ea888`): `_gti`, `_gti_performance`, `_r`.
- Long blocks: `vivace_engine_internals_ea888_gti`, `_r`.
- Exhaust sound: `vivace_engine_sound_ea888_stock` (ea888_exh), `_sport` (ea888_exh_sport).
- Engine base: NA curve 148 Nm@1000, 190@2500, 199@4000 (peak), 165@7000; idle 750, max 7000 rpm, inertia 0.11,
  friction 11, dynamicFriction 0.014, engineBrakeTorque 50, oil 5.7 L, iron block.
  maxTorqueRating 460 (GTI) / 520 (R); maxOverTorqueDamage 250 / 280.

| | IS20 (GTI) | IS38 (R) |
|---|---|---|
| wastegateStart/Limit psi | 14/15 | 17/18 |
| inertia | 0.30 | 0.42 |
| turboSizeCoef | 0.75 | 0.85 |
| maxExhaustPower | 1500 | 1700 |
| max pressure @250k rpm | 26 psi | 30 psi |

Turbo `engineDef` tables tuned to: GTI 350 Nm 1500-4600 rpm and 230 PS 4700-6200; R 400 Nm 2000-5200 and 310 PS 5500-6500
(R is currently Mk7.5 310 PS/400 Nm; project target is 300 PS/380 Nm).

| ECU | rev limit | wastegate psi | torqueModMult | highShiftUp |
|---|---|---|---|---|
| _gti | 6500 | 14/15 | 1.0 from 750 rpm, 0.862 @500 | 6300 |
| _gti_performance | 6500 | 15/16 | ~1.0-1.03 | 6300 |
| _r | 6700 | 17/18 | 1.0 from 1000, 0.777 @500 | 6500 |

### ea888_transmissions.jbeam (slotType `vivace_transmission`)
- `vivace_transmission_ea888_DQ381`: 7-speed `dctGearbox` on `mainEngine`; ratios `[-2.888,0,3.386,2.056,1.323,0.926,0.697,0.568,0.478]`
  (real overall ratios / 4.187). friction 1.34, torqueLossCoef 0.0155, ignitionCutTime 0.10, shiftDelay 0.08.
  Sub-slots: `vivace_transfer_case` (default FWD), `vivace_differential_F`, `vivace_dsg_sound_ea888`. ~25 kg.
- `vivace_transmission_ea888_MQ350`: 6-speed `manualGearbox`, ratios `[-3.518,0,3.604,1.998,1.405,1.042,0.850,0.703]`
  normalised to 3.389; core slot `vivace_flywheel`. ~17 kg. NOT used by any config yet.

### Sound parts
- `vivace_dsg_sound_ea888` (ea888_dsg_sounds.jbeam): controller `ea888DsgSounds` - upshift farts, launch rumble.
  vars `$ea888_dsgVolume` 1.2, `$ea888_launchVolume` 1.0, `$ea888_launchRPM` 3300.
- `vivace_soundaktor_ea888` (ea888_soundaktor.jbeam): controller `ea888Soundaktor`, grain clips from nodes f6l/f6r, interior camera only;
  var `$ea888_soundaktorVolume` 0.8.
- Both Lua controllers are `type = "auxiliary"` and use `obj:playSFXOnceCT` one-shots.

## Configs (.pc, format 2, mainPartName vivace; heavy reliance on base parts)
| | GTI | GTI Performance | Golf R |
|---|---|---|---|
| intake/turbo | IS20 | IS20 | IS38 |
| ECU / internals | _gti / _gti | _gti_performance / _gti | _r / _r |
| gearbox | DQ381 | DQ381 | DQ381 |
| final drive | `vivace_finaldrive_F_4187` | `_F_4187` | `_F_437` + `_R_437` |
| front diff | `vivace_differential_F` (open) | `vivace_differential_F_LSD` (preload 10, lockCoef 0.3, revLock 0.05) | `vivace_differential_F` + `vivace_differential_R` |
| transfer case | FWD | FWD | `vivace_transfer_case_AWD` + `vivace_driveshaft` + `vivace_halfshaft_R` |
| exhaust sound | _stock | _stock | _sport |
| brakes | `vivace_brake_F/R_sport_r` (F 0.355 m, 3000*$brakestrength; R 0.290 m, 1400*$brakestrength) | same | same |
| pads | F `brakepad_F_sport`, R `brakepad_R_premium` | same | `brakepad_*_semi_race` |
| wheels | `cherrier_wheel_04a_18x8`, 225/40R18 `tire_*_225_40_18_sport` | same | `cherrier_wheel_02a_19x9`, 245/35R19 `tire_*_245_35_19_alt_sport` |
| suspension | standard `vivace_suspension_F/R`, `spring_R_sport`, `strut_F_sport_adaptive`, `swaybar_F_sport` | same | WIDE kit: `suspension_F/R_wide`, `spring_R_wide_sport_r`, `strut_F_wide_sport_adaptive`, `swaybar_R_sport`, strut bar, `radiator_race`, `enginemounts_heavy`, wide doors/fenders/bumpers |
| fuel tank | `vivace_fueltank` (base, 50 L) | same | same |
| other | | | `vivace_DSE_TC_FWD` still selected (check vs AWD) |

Mass: mod only adds nodes (engine ~116 kg: nine 9.375 kg + four 7.03 kg + one 3 kg; turbo/intercooler ~16 kg; DQ381 ~25 kg).
Total vehicle mass comes from base Vivace and is NOT tuned here.

Info JSONs carry Configuration/Description/Drivetrain/Fuel/Induction/Transmission + `defaultMultiPaintSetup`
(GTI: Rouge Carmin / Rouge Feu; R: custom blues).

## Dependencies
Base `vivace.zip` + `common.zip`; stock sound events `event:>Vehicle>Afterfire>i4_01>*`, `Turbo_01`, `Transmission>helical_01`.
Sample credit (Hell_Raiser_999) appears only in jbeam strings.
