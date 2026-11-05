-- EA888 mod: VW "Soundaktor" (cabin sound actuator) for the Vivace.
-- The real car plays a synthesised engine-order sound through a speaker under the windscreen. Here short generated clips
-- ("grains", tools/gen_soundaktor.ps1) are played from the dash as overlapping one-shots: every grainInterval the two
-- clips recorded nearest the current rpm are played, blended by rpm and by a cruise/load layer mix, each pitched to the
-- exact rpm. Their faded edges overlap into a continuous sound. Only audible with the camera inside the cabin.
-- Looping SFX sources (createSFXSource2) played raw WAVs wrong in this game version, so only playSFXOnceCT is used.

local M = {}
M.type = "auxiliary"

local engine = nil
local grains = {}          -- grains[layer] = sorted list of {file, rpm}
local volume = 1
local idleVolumeCoef = 0.3
local grainInterval = 0.12
local dashNodes = {}
local soundNode = nil
local cabinBox = {back = 2.3, front = 0.3, side = 0.85, below = 0.7, above = 0.6}
local refCid, backCid, upCid = nil, nil, nil

local cabinCoef = 0
local loadSmooth = 0
local grainTimer = 0

local avToRPM = 9.549296596

local function clamp01(x) return math.min(math.max(x, 0), 1) end

local function cameraInCabin()
  -- vehicle axes from the body's refNodes (ref -> back points rearwards, ref -> up points up)
  local refPos = obj:getNodePosition(refCid)
  local fwd = (refPos - obj:getNodePosition(backCid)):normalized()
  local up = (obj:getNodePosition(upCid) - refPos)
  up = (up - fwd * up:dot(fwd)):normalized()
  local right = fwd:cross(up)
  local dash = vec3(0, 0, 0)
  for _, cid in ipairs(dashNodes) do
    dash = dash + obj:getNodePosition(cid)
  end
  dash = obj:getPosition() + dash / #dashNodes
  local d = obj:getCameraPosition() - dash
  local along = d:dot(fwd)     -- positive = ahead of the dash
  local lateral = d:dot(right)
  local vertical = d:dot(up)
  return along < cabinBox.front and along > -cabinBox.back and math.abs(lateral) < cabinBox.side and vertical > -cabinBox.below and vertical < cabinBox.above
end

-- play the two grains of one layer that bracket rpm, crossfaded linearly between their recorded speeds
local function playLayer(list, rpm, layerVolume)
  if layerVolume < 0.01 or #list == 0 then return end
  local lo, hi = list[1], list[#list]
  local wHi = 0
  if rpm <= lo.rpm then
    hi = lo
  elseif rpm >= hi.rpm then
    lo = hi
  else
    for i = 1, #list - 1 do
      if rpm >= list[i].rpm and rpm <= list[i + 1].rpm then
        lo, hi = list[i], list[i + 1]
        wHi = (rpm - lo.rpm) / (hi.rpm - lo.rpm)
        break
      end
    end
  end
  local parts = (lo == hi) and {{lo, 1}} or {{lo, 1 - wHi}, {hi, wHi}}
  for _, p in ipairs(parts) do
    local g, w = p[1], p[2]
    if w > 0.02 then
      local pitch = math.min(math.max(rpm / g.rpm, 0.5), 2.0)
      obj:playSFXOnceCT(g.file, soundNode, layerVolume * w, pitch, 1, 0)
    end
  end
end

local function updateGFX(dt)
  local target = (cameraInCabin() and not engine.isDisabled and not engine.isStalled) and 1 or 0
  cabinCoef = cabinCoef + (target - cabinCoef) * math.min(dt * 8, 1)
  local load = clamp01(engine.engineLoad or 0)
  loadSmooth = loadSmooth + (load - loadSmooth) * math.min(dt * 6, 1)

  grainTimer = grainTimer - dt
  if grainTimer > 0 then return end
  grainTimer = math.max(grainTimer + grainInterval, 0)
  if cabinCoef < 0.01 then return end

  local rpm = math.max(engine.outputAV1 * avToRPM, 0)
  if rpm < 300 then return end
  local loadCoef = idleVolumeCoef + (1 - idleVolumeCoef) * loadSmooth
  local rpmCoef = 0.5 + 0.5 * clamp01((rpm - 800) / 4500)
  local base = volume * cabinCoef * loadCoef * rpmCoef

  playLayer(grains.light or {}, rpm, base * (1 - 0.8 * loadSmooth))
  playLayer(grains.load or {}, rpm, base * loadSmooth)
end

local function reset()
  cabinCoef = 0
  loadSmooth = 0
  grainTimer = 0
end

local function findNode(name)
  for _, n in pairs(v.data.nodes) do
    if n.name == name then return n.cid end
  end
  return nil
end

local function init(jbeamData)
  engine = powertrain.getDevice(jbeamData.engineName or "mainEngine")
  volume = jbeamData.volume or 1
  idleVolumeCoef = jbeamData.idleVolumeCoef or idleVolumeCoef
  grainInterval = jbeamData.grainInterval or grainInterval

  dashNodes = {}
  for _, name in ipairs(jbeamData.dashNodes or {"f6l", "f6r"}) do
    local cid = findNode(name)
    if cid then table.insert(dashNodes, cid) end
  end
  soundNode = dashNodes[1]
  local refNodes = v.data.refNodes and v.data.refNodes[0]
  if refNodes then
    refCid, backCid, upCid = refNodes.ref, refNodes.back, refNodes.up
  end

  -- grains: [file, recorded rpm, layer]
  grains = {}
  for _, g in ipairs(jbeamData.grains or {}) do
    if type(g[1]) == "string" and type(g[2]) == "number" then
      local layer = g[3] or "load"
      grains[layer] = grains[layer] or {}
      table.insert(grains[layer], {file = g[1], rpm = g[2]})
    end
  end
  for _, list in pairs(grains) do
    table.sort(list, function(a, b) return a.rpm < b.rpm end)
  end

  reset()
  local ok = engine ~= nil and soundNode ~= nil and refCid ~= nil and backCid ~= nil and upCid ~= nil and next(grains) ~= nil
  M.updateGFX = ok and updateGFX or nop
  if not ok then
    log("W", "ea888Soundaktor.init", "Disabled: needs mainEngine, refNodes, the dash nodes and at least one grain")
  end
end

M.init = init
M.reset = reset
M.updateGFX = nop

return M
