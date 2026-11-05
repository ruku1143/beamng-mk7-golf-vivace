# Performance readings - how to take them (UNTESTED tooling)

Claude cannot run the game, so these are taken by the user. `lua/vehicle/extensions/ea888PerfLogger.lua` (mod-owned, shipped with the mod) times the runs automatically. It was written without being run: if it errors, send the console error.

## One-time per spawn
1. Spawn the config on a long flat road (e.g. an airstrip or highway), tyres cold is fine, driver in.
2. Open the console (~) and run (normal console, not a vehicle context):
```
be:getPlayerVehicle(0):queueLuaCommand("extensions.load('ea888PerfLogger')")
```
A message appears and the log gets "EA888PERF loaded".

## The runs
- **0-100 km/h:** stand still, floor the throttle (>=80%), hold it. For DSG use launch control if available; for manuals launch normally. It prints "0-100 km/h: x.xx s over N m" when you pass 100 km/h.
- **100-0 km/h:** get above 100 km/h, then brake hard and hold (>=90% brake) until stopped. It prints "100-0 km/h: N m in x.xx s". Do not steer or lift mid-stop (that cancels the run).
- **Top speed / max rpm:** drive flat out as long as you can, then run:
```
be:getPlayerVehicle(0):queueLuaCommand("ea888PerfLogger.report()")
```
- Reset between configs by respawning (or `ea888PerfLogger.reset()`).

## What to send me
For each config: the three lines (0-100, 100-0, top speed + max rpm), and note if ESC/TC were on. Results go in docs/BASELINE.md; real targets are in docs/MK7_SPEC_TARGETS.md (e.g. GTI ~6.2-6.5 s, R ~4.6-5.0 s, 100-0 ~35 m, top ~250 limited).
Dyno power/torque curves still need the game's own dyno app (not automated here): note peak PS/Nm and rpm per config.

## Do this first for the three original configs
GTI (DSG), GTI Performance (DSG), Golf R (DSG) to complete the baseline; then the 10 other configs.
