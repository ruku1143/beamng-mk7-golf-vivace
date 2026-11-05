-- EA888 mod performance logger (UNTESTED - written without running the game).
-- Load from the console (normal console, not a vehicle context):
--   be:getPlayerVehicle(0):queueLuaCommand("extensions.load('ea888PerfLogger')")
-- Then drive. It logs automatically to the screen message area and to beamng.log (search "EA888PERF"):
--   0-100 km/h : from a standstill with throttle >= 0.8, timed from first movement to 100 km/h (time + distance)
--   100-0 km/h : brake >= 0.9 while above 100 km/h, measured to a stop (distance + time)
--   top speed  : highest speed seen this session, printed on request
-- Report on demand:  be:getPlayerVehicle(0):queueLuaCommand("ea888PerfLogger.report()")
-- Unload/reset:      be:getPlayerVehicle(0):queueLuaCommand("ea888PerfLogger.reset()")
local M = {}

local TARGET = 100 / 3.6      -- 100 km/h in m/s
local STOP = 0.3              -- m/s: treated as standing
local state = 'idle'          -- idle | accel | brake
local t, dist = 0, 0
local topSpeed, topRpm = 0, 0
local last0100, last1000

local function say(msg)
  log('I', 'EA888PERF', msg)
  pcall(function() guihooks.message(msg, 10, 'ea888perf') end)
end

local function speed()
  return obj:getVelocity():length()
end

local function updateGFX(dt)
  local v = speed()
  local thr = (electrics.values.throttle or 0)
  local brk = (electrics.values.brake or 0)
  if v > topSpeed then topSpeed = v end
  local rpm = electrics.values.rpm or 0
  if rpm > topRpm then topRpm = rpm end

  if state == 'idle' then
    if v < STOP and thr >= 0.8 then
      state = 'armed'
    elseif v >= TARGET and brk >= 0.9 then
      state = 'brake'; t = 0; dist = 0
    end
  elseif state == 'armed' then
    if thr < 0.5 then state = 'idle'
    elseif v > STOP then state = 'accel'; t = 0; dist = 0 end
  elseif state == 'accel' then
    t = t + dt; dist = dist + v * dt
    if thr < 0.5 and v < TARGET then state = 'idle'   -- aborted
    elseif v >= TARGET then
      last0100 = string.format('0-100 km/h: %.2f s over %.0f m', t, dist)
      say(last0100); state = 'idle'
    end
  elseif state == 'brake' then
    t = t + dt; dist = dist + v * dt
    if brk < 0.3 then state = 'idle'                  -- aborted
    elseif v <= STOP then
      last1000 = string.format('100-0 km/h: %.1f m in %.2f s', dist, t)
      say(last1000); state = 'idle'
    end
  end
end

function M.report()
  say(string.format('top speed %.1f km/h, max rpm %.0f | %s | %s', topSpeed * 3.6, topRpm, last0100 or '0-100: none', last1000 or '100-0: none'))
end

function M.reset()
  state = 'idle'; t = 0; dist = 0; topSpeed = 0; topRpm = 0; last0100 = nil; last1000 = nil
  say('reset')
end

local function onExtensionLoaded()
  say('ea888PerfLogger loaded: 0-100 needs a standing start at full throttle; 100-0 needs a hard stop from >100 km/h')
end

M.updateGFX = updateGFX
M.onExtensionLoaded = onExtensionLoaded
return M
