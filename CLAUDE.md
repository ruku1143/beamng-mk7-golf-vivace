# EA888_Gen3_Vivace - session entry point

BeamNG.drive mod: EA888 Gen3 2.0 TSI + DQ381/MQ350 swap for the base-game Vivace (FWD hatch).
Three configs: `vivace_ea888_gti`, `vivace_ea888_gti_performance`, `vivace_ea888_golf_r`.

**Current project goal:** turn it into a Mk7 Golf-accurate mod (GTI 230 PS, GTI Performance 245 PS,
R 4Motion, pre- and post-facelift): mass, weight distribution, fuel tank, brakes, springs/dampers/ARBs, tyres, gearing,
diffs, power. Scope = DATA ONLY; keep Vivace body geometry. Mk7.5 (facelift) is IN scope too (decided 2026-11-05): six variants, see docs/MK7_SPEC_TARGETS.md.

## Read these first (do NOT re-run mod discovery)
- docs/MOD_MAP.md - every file, part, slotType, config and key number in this mod
- docs/BASE_GAME_REFERENCE.md - where the base Vivace data lives and how to read it
- docs/MK7_SPEC_TARGETS.md - target numbers (UNVERIFIED until the Source column is filled)
- docs/KNOWN_ISSUES.md - gotchas and landmines
- docs/PLAN.md - approved phase plan; docs/HANDOVER_CLOUD.md - current handover state
- docs/WORKFLOW.md - testing, packaging, conventions, change log
- Plan: the approved phase plan is summarised in docs/WORKFLOW.md (Phases 0-4)

## Rules
- Never edit or copy base-game files (`vivace.zip` is proprietary, 1.1 GB, read-only). Add new mod-owned parts instead.
- Mod is unpacked in the live game dir: edits take effect on next vehicle respawn / game restart. Check `beamng.log` after each change.
- Change one subsystem at a time; log before/after numbers in docs/WORKFLOW.md change log.
- Retune ECU `torqueModMult` and turbo `engineDef` together; they are coupled (see KNOWN_ISSUES).
- BeamNG only runs locally on Windows; all in-game testing happens on the user's PC.
- Paths: mod root = this folder. Game install = `D:\SteamLibrary\steamapps\common\BeamNG.drive`.
