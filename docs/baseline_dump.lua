-- Baseline dump for EA888_Gen3_Vivace (UNTESTED - written without running the game).
-- Use: spawn a config, press ~ to open the console, switch the console context to the VEHICLE (dropdown, top-left
-- of the console: pick "Vehicle" / the current vehicle's Lua), paste this whole file, press Enter.
-- Output also goes to beamng.log (search "BASELINE"). If a call errors, the pcall prints the error: send it back.
-- In BeamNG the vehicle forward axis is -y, so front axle has the smaller y.

local function try(f, ...)
  local ok, a, b, c = pcall(f, ...)
  if ok then return a, b, c end
  log('W', 'BASELINE', 'call failed: ' .. tostring(a))
  return nil
end

local n = obj:getNodeCount()
local total, cx, cy, cz = 0, 0, 0, 0
for i = 0, n - 1 do
  local m = try(function() return obj:getNodeMass(i) end)
  local p = try(function() return obj:getNodePosition(i) end)
  if m and p then
    total = total + m
    cx = cx + m * p.x; cy = cy + m * p.y; cz = cz + m * p.z
  end
end
if total > 0 then cx, cy, cz = cx / total, cy / total, cz / total end

-- axle y positions from wheel hub nodes
local fy, fn, ry, rn = 0, 0, 0, 0
local wheelInfo = {}
for _, w in pairs(wheels.wheels) do
  local p = try(function() return obj:getNodePosition(w.node1) end)
  if p then
    wheelInfo[#wheelInfo + 1] = string.format('%s y=%.3f x=%.3f', tostring(w.name), p.y, p.x)
    if p.y < 0 then fy = fy + p.y; fn = fn + 1 else ry = ry + p.y; rn = rn + 1 end
  end
end
if fn > 0 then fy = fy / fn end
if rn > 0 then ry = ry / rn end
local wb = ry - fy
local frontShare = (wb ~= 0) and ((ry - cy) / wb) or 0

local lines = {
  string.format('BASELINE config=%s', tostring(v.config and v.config.partConfigFilename or 'unknown')),
  string.format('BASELINE total_node_mass_kg=%.1f (no driver, fuel as spawned)', total),
  string.format('BASELINE cog x=%.3f y=%.3f z=%.3f (vehicle frame, rel. ref node)', cx, cy, cz),
  string.format('BASELINE wheelbase_m=%.3f front_axle_y=%.3f rear_axle_y=%.3f', wb, fy, ry),
  string.format('BASELINE static_front_share_pct=%.1f rear=%.1f', frontShare * 100, (1 - frontShare) * 100),
  'BASELINE wheels: ' .. table.concat(wheelInfo, ' | '),
}
for _, l in ipairs(lines) do log('I', 'BASELINE', l); print(l) end
