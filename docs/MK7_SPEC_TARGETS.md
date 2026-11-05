# Mk7 Golf spec targets

Phase 1 research, filled 2026-11-05 by the cloud session (web only; no VW spec PDF / Typenschein was reachable).
Confidence: **High** = VW newsroom/primary. **Med** = aggregator or several agreeing sources. **Low** = single/unclear source.
"no source found" means exactly that - do NOT fill it from memory. Anything Low or missing must be confirmed before it drives a mod value.

## Scope: pre- AND post-facelift (decided 2026-11-05)
The mod will cover both Mk7 (2013-16) and Mk7.5 (2016-20). Working variant matrix (power figures marked * are from memory, UNVERIFIED - confirm in the next research pass):

| Variant | Years | Power / torque | Box options | Notes |
|---|---|---|---|---|
| Mk7 GTI | 2013-16 | 220 PS (user-confirmed 2026-11-05) / 350 Nm | 6MT, 6DSG (DQ250) | base brakes 314x30 / 300x12 |
| Mk7 GTI Performance | 2013-16 | 230 PS (user-confirmed + auto-data) / 350 Nm | 6MT, 6DSG | VAQ, 340x30 / 310x22 brakes |
| Mk7 R | 2014-16 | 300 PS / 380 Nm (sourced) | 6MT, 6DSG | Haldex Gen5 |
| Mk7.5 GTI | 2016-20 | 230 PS / 350 Nm (sourced, Wikipedia) | 6MT, 7DSG (DQ381) | |
| Mk7.5 GTI Performance | 2016-20 | 245 PS / 370 Nm (sourced, VW) | 6MT, 7DSG | VAQ, big brakes |
| Mk7.5 R | 2016-20 | **310 PS / 380 Nm (user decision 2026-11-05; 2016-18 calibration per Wikipedia, power/torque still unverified)** | 6MT, 7DSG | |

Body: 5-door only (3-door excluded by user decision 2026-11-05). Use 5-door kerb weights; ignore 3-door figures (the Phase 1 R figures of 1395-1420 kg were 3-door).

Market: EU / UK spec only (North America excluded by user decision 2026-11-05). Ignore US/Canada figures (different power ratings, weights, tyres, gearboxes, e.g. the US 220 hp GTI and 292 hp R).

Rule of thumb for later phases: Mk7 = DQ250 (6DSG), Mk7.5 = DQ381 (7DSG). The mod's current DQ381 + 310 PS-calibrated R is Mk7.5.
Decided 2026-11-05: manual (MQ350) variants are shipped too, so up to 12 configs (6 DSG + 6 MT). Mk7.5 R = 310 PS (the mod's existing calibration, so little retune needed).

## Power / performance

| Item | GTI | GTI Performance | R (Mk7 launch) | Source / confidence |
|---|---|---|---|---|
| Power | 230 PS (169 kW) @ 4500-6200 | 230 PS @ 4700-6200 (pre-facelift); **245 PS @ 4700-6200 (Mk7.5)** | 300 PS @ 5500-6200 | [Wikipedia](https://en.wikipedia.org/wiki/Volkswagen_Golf_Mk7), [auto-data PP](https://www.auto-data.net/en/volkswagen-golf-vii-3-door-gti-2.0-tsi-230hp-dsg-45038), [auto-data R](https://www.auto-data.net/en/volkswagen-golf-vii-3-door-r-2.0-tsi-300hp-4motion-dsg-45048), [VW 245](https://www.volkswagen-newsroom.com/de/up-gti-polo-gti-golf-gti-performance-2396/golf-gti-performance-245-ps-ikone-fuer-die-ewigkeit-2427) - Med (245 PS: High) |
| Torque | 350 Nm @ 1500-4400 | 350 Nm @ 1500-4600 (230 PS); 370 Nm (245 PS; band 1500-4600 Wikipedia vs 1600-4300 VW) | 380 Nm @ 1800-5500 | same - Med |
| 0-100 km/h | 6.2 (table) / 6.5 (prose) | 6.4 (230 PS DSG); 6.2 (245 PS, VW) | 4.9 DSG | same - Med |
| Top speed | 246 (Wikipedia; prose says 250) | 250 MT / 248 DSG (245 PS, VW) | 250 limited | same - Med |
| 100-0 | no source found | no source found | ~33 m (snippet, unopened) / 31.4 m (facelift, user-submitted) | Low |

Wikipedia also lists a 310 PS / 380 Nm R (2016-18, Mk7.5): not a target. Wikipedia R 2018-20 = 300 PS / 400 Nm (Mk7.5).

## Mass, tank, dimensions

| Item | GTI | GTI Performance | R (3-door DSG) | Source / confidence |
|---|---|---|---|---|
| Kerb weight | see "Kerb weights" section below (5-door, EU/UK) | | | |
| Max permissible | no source found | no source found | 1980 kg | auto-data - Med |
| F/R split | no source found | no source found | no source found | - (plan's 60/40 and 58/42 are unverified memory) |
| Fuel tank | 50 L | 50 L | 55 L | [mobile.de](https://www.mobile.de/auto/vw/golf-gti/2013/schraegheck/modell/daten-fakten/), auto-data - Med |
| Wheelbase | 2631 | 2631 | 2630 | auto-data; Wikipedia range 2631-2637 - Med |
| Length | no source found | 4268 | 4276 | auto-data; Wikipedia 4255-4280 - Med |
| Width (no mirrors) | no source found | 1799 | 1799 | auto-data - Med |
| Track F/R | no source found | 1538 / 1516 | 1541 / 1515 | auto-data - Med |
| Drag Cd / frontal area | no source found | no source found | no source found | - |

## Kerb weights (5-door, EU/UK) - researched 2026-11-05
Basis: ADAC "Leergewicht (EU)" = EU kerb weight, believed to include a 75 kg driver (90% tank) - not confirmed from ADAC's definition page.
DIN (no driver) = EU - 75 kg is a DERIVED estimate, not sourced. No VW press-kit/COC figure was reachable. 3-door, estate and NA/AU figures excluded.
**No measured or published front/rear weight split or axle load exists in any source found** (only permitted axle limits). Best lead: Grassroots Motorsports "what's it weigh" Mk7 GTI (403 from cloud).

### Mk7 (2013-16), ADAC EU basis, High confidence unless noted
| Variant | 6MT | 6DSG | Derived DIN (MT / DSG) |
|---|---|---|---|
| GTI 220 PS | 1351 | 1370 | ~1276 / ~1295 |
| GTI Performance 230 PS | 1382 | 1402 | ~1307 / ~1327 |
| R 300 PS | no 5-door MT source (3-door MT = 1476, Med-high; 5-door ~ same or slightly more) | 5-door DSG 1450 (auto-data, basis unclear, Low-Med); 3-door DSG ~1495 EU (inferred from 1420 + 75) | - |

ADAC pages: GTI 235658 (MT) / 235660 (DSG), PP 235659 / 235661. Within ADAC, 3-door and 5-door weights are identical.
DSG adds ~19-20 kg on the GTI variants.

### Mk7.5 (2017-20)
| Variant | 6MT | 7DSG | Source / confidence |
|---|---|---|---|
| GTI 230 PS | 1352 (paultan snippet, Low-Med; WhichCar AU 1324 Low, ignore) | 1341 (auto-data, basis unstated, Low-Med) | no ADAC page located |
| GTI Performance 245 PS | 1387 EU (ADAC 269412, High) | 1370 (autodata1, basis unstated, Low-Med) | the 1415 ADAC figure is 3-door DSG: excluded |
| R 310 PS (2017-18) | no 5-door MT EU source (1483 angurten, Low; AU 1429 not applicable) | 1505 EU (ADAC 266260, High) | |
| R 300 PS (2018-20) | no source found | 1515 EU (ADAC 303254, High) | |

Inconsistencies to resolve: the Mk7.5 aggregator DSG figures (1341, 1370) do not fit the ADAC MT numbers if they were DIN (they imply DSG lighter than MT); treat as unreliable.
The Mk7.5 R is ~10-30 kg heavier than the Mk7 R (GPF on the 300 PS).

### Working mass targets (use until better data; EU = incl. driver)
Mk7 GTI MT 1351, Mk7 PP MT 1382, Mk7.5 PP MT 1387, Mk7.5 R DSG 1505 (310 PS) - these are the only High-confidence anchors.
Others: estimate from deltas (DSG +19-20 kg; R vs PP ~+95-100 kg) and mark UNVERIFIED in configs. Decide in the local session whether the game's mass figure should include a driver (BeamNG default: no driver, so use the derived DIN values).

## Brakes (disc diameter x thickness, mm)

| Variant | Front | Rear | Source / confidence |
|---|---|---|---|
| GTI (base) | 314 x 30 vented (VW). Retail/Evo say 312 | 300 x 12 solid (VW). Retail says 272 | [VW newsroom GTI](https://www.volkswagen-newsroom.com/en/new-golf-gti-international-press-presentation-2976/new-golf-gti-running-gear-layout-and-electronics-2988) - High (conflicts with 312/272 memory values; use VW) |
| GTI Performance | 340 x 30 vented | 310 x 22 vented | VW newsroom GTI - High |
| R | 340 x 30 vented, 60 mm pistons | 310 x 22 vented, 42 mm pistons | [VW newsroom R](https://www.volkswagen-newsroom.com/en/the-new-golf-r-2432/sport-suspension-of-the-golf-r-2455) - High |

Piston counts: no source found (only piston diameters for R). PP has manual handbrake, R electronic (different rear pads). Beware Mk6 R 345/310 figures.

## Wheels / tyres

| Variant | Size | Source / confidence |
|---|---|---|
| GTI / PP (pre-facelift) | 225/45R17 (7.5J), 225/40R18 (7.5J), 225/35R19 (7.5J) | auto-data - Med |
| GTI PP 245 PS | 17" "Brooklyn" standard (tyre size not stated) | VW newsroom - Med |
| R | 225/40R18 (7.5J) std, 235/35R19 (8J) option | auto-data - Med |

Standard-vs-option mapping per trim: not determined.

## Chassis / suspension

| Item | Value | Source / confidence |
|---|---|---|
| Layout | strut F, multilink R (GTI and R) | VW newsroom - High |
| Lowering | GTI/PP -15 mm vs lesser Golfs; R -20 mm vs base Golf (5 mm below GTI) | VW newsroom - High |
| Dampers | DCC optional on all three (Comfort/Normal/Sport); no values published | VW newsroom - High |
| Steering | progressive 2.1 turns lock-lock (380 deg); standard Golf 2.75 turns | VW newsroom - High |
| Steering ratio | ~10.5:1 progressive / 13.2:1 standard (the plan's 13.0:1 is not confirmed) | forum quote - **Low** |
| Turning circle | GTI 10.9 m; R no source found | carsales, VW India brochure - Med |
| OEM spring rates F/R | **no source found** (VW does not publish) | - |
| ARB, GTI | front ~24 mm (APR lists factory 24.1 x 3.9); rear 21.7 mm (some say 20) | APR/shopdap, Black Forest Industries - Low-Med |
| ARB, R | no source found | - |
| Camber / toe | no source found (an unsourced page gives -0.5..-1.0 / -1.5..-2.0 camber; ignore) | very low |
| Ride height (mm), skidpad, unsprung mass | no source found | - |
| Aftermarket rates (NOT stock, stock is lower) | RacingLine GTI 28.5 / 38 N/mm; Whiteline R ~40 / 47 N/mm; 034 R ~38 / 50 N/mm | retailers - Med as products |
| Relative hint | later gen has springs +5% F / +15% R vs Mk7 GTI - not a Mk7 value | VW newsroom (other gen) |

Suspension tuning must come from base-Vivace values scaled by judgment, or be measured in game (handling feel), not from invented "OEM" rates.

## Drivetrain

| Item | Value | Source / confidence |
|---|---|---|
| Boxes | GTI: 6MT (MQ350) / 6DSG (DQ250). PP: 6MT / 7DSG (DQ381) per Wikipedia table. R 2014-16: 6MT / 6DSG; R 2016-20: 6MT / 7DSG | Wikipedia Mk7 - Med |
| DQ381 | 7-speed wet, ~420 Nm, FWD (-7F) and AWD (-7A), from 2017 | Wikipedia DSG, TVS - Med |
| Front diff | GTI: open + XDS. PP: VAQ electro-hydraulic multi-plate clutch, 1,600 Nm max lock moment (=100% lock), variable not fixed; inputs wheel/vehicle speed, yaw, lateral g | VW newsroom, PistonHeads - High. Lift-off behaviour, preload, lock curve: no source found |
| R rear | Haldex Gen5, electro-hydraulic pump, pre-engages, decouples at low load/coast. Rear share: VW "nearly 100%" vs Wikipedia up to 50% (use 50% practical cap, Med). Default ~30% rear under accel (vendor claim, Low). Preload: no source found | VW newsroom 4Motion - High/Med |
| Gear ratios | **No reliable per-variant table found.** See `docs/GEARING_CALC.md` for the mod's existing ratios and the unverified candidates | - |

Candidate gear sets (all **Low**, do not use as verified): MQ350 Mk7 GTI forum quote 3.76/2.08/1.46/1.08/1.09/0.91, finals 3.24 (1-4) and 2.62 (5-6);
DQ381 Taos 1.4 TSI table 3.190/2.750/1.897/1.040/0.793/0.860/0.661, rev 2.900, finals 4.813/3.667 (6th>5th, probably misquoted).

## Still unsourced (next attempt)
VW UK/DE spec PDF or SSP/Typenschein (gear ratios + Achsuebersetzung per box code, DIN kerb weights, axle loads); Auto Motor und Sport / Car and Driver test pages
(100-0, skidpad); golfmk7.com and vwvortex gear-ratio threads (blocked from the cloud: 403).
