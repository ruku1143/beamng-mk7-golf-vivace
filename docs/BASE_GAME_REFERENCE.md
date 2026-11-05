# Base-game Vivace reference

Archive (read-only, proprietary - never copy into the repo):
`D:\SteamLibrary\steamapps\common\BeamNG.drive\content\vehicles\vivace.zip` (1.1 GB, 225 jbeam/pc files). Shared assets: `common.zip` same folder.
A user-level `...\BeamNG.drive\current\vehicles\vivace` folder also exists (not inspected).

## Read a file without extracting
```bash
python -I -c "import zipfile;print(zipfile.ZipFile(r'D:/SteamLibrary/steamapps/common/BeamNG.drive/content/vehicles/vivace.zip').read('vehicles/vivace/vivace_fueltank.jbeam').decode())"
```
(or `unzip -p <zip> vehicles/vivace/<file>`). List: `zipfile.ZipFile(...).namelist()`.

## Where the values live (paths inside the zip, `vehicles/vivace/`)
| Topic | File(s) |
|---|---|
| body nodes / mass | vivace_body.jbeam (78 KB), vivace_body_panoramic.jbeam |
| fuel tank (50 L) | vivace_fueltank.jbeam |
| brakes (discs, torque, pads) | vivace_brakes.jbeam |
| front struts | vivace_strut_F.jbeam, vivace_strut_F_wide.jbeam |
| front suspension geometry | vivace_suspension_F.jbeam, _F_wide, _F_rally |
| rear springs/shocks | vivace_spring_shock_R.jbeam, _R_wide |
| rear suspension | vivace_suspension_R.jbeam, _R_wide, _R_rally |
| diffs and final drives (incl. `vivace_finaldrive_F_4187`, `_3389`, `_437`) | vivace_differential_F.jbeam, vivace_differential_R.jbeam |
| transfer case FWD/AWD | vivace_transfercase.jbeam |
| steering wheels | vivace_steeringwheels.jbeam |
| stock configs | vivace_*.pc (e.g. vivace_S_310_DCT.pc, vivace_230S_DCT.pc) |
Variants with other prefixes: `ardente_*` (sport/Ardente sibling) and `tograc_*` (wagon/other body) files exist in the same zip.

## How the mod hooks in
The mod adds new part names for slotTypes `vivace_engine`, `vivace_transmission`, etc. and `.pc` configs select base parts by name.
To change mass/fuel/brakes/suspension add NEW mod-owned parts with the same slotType and select them in the `.pc`; do not edit base files.
Open items to check in the base files before editing: total mass + axle split of stock Vivace, how `$brakestrength` and `nodeWeight` are defined,
whether slot defaults allow override, and which suspension variables expose spring/damper/ride-height.
