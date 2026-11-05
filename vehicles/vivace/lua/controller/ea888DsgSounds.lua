-- EA888 mod: DSG and launch control sounds for the Vivace (one part).
--  * upshift: when the DCT cuts the ignition for a fast upshift under throttle (the same moment the stock shift afterfire
--    fires) a layered mix of the DSG "fart" samples (from Hell_Raiser_999's TSI mod) plays from the exhaust tips.
--  * launch control: while the stock twoStepLaunch controller holds the engine on its launch RPM (brake + throttle at a
--    standstill) a recorded launch-control sound plays from the exhaust as overlapping one-shots (a "grain" with faded
--    edges, retriggered just before it ends), with short ignition cuts so the revs stutter, and the DSG mix plays once,
--    louder, on release. Without a launch grain it falls back to quick DSG-sample bursts.
-- Looping SFX sources (createSFXSource2) did not play raw WAV files correctly, so everything uses playSFXOnceCT.
-- The stock shift-afterfire path plays a single sample at most every 0.5 s, so the sounds are played directly here.

local M = {}
M.type = "auxiliary"

local engine = nil
local twoStep = nil

local layers = {}          -- {file, mix}
local shiftVolume = 1
local launchVolume = 1
local launchRPM = 0        -- 0 = keep the drive mode's launch RPM
local intervalMin = 0.09
local intervalMax = 0.16
local launchIgnitionCutTime = 0.03
local releaseVolumeCoef = 1.6
local minShiftRPM = 2000

local launchGrain = nil    -- file:> path of the launch grain, or nil to use DSG-sample bursts
local launchGrainGain = 1
local launchGrainInterval = 1
local grainTimer = 0

local exhaustEnds = {}     -- {cid, volumeCoef, color}
local timer = 0
local wasArmed = false
local lastCutTime = 0
local ownCutPending = false

local avToRPM = 9.549296596

local function playMix(volume, pitch)
  for _, n in ipairs(exhaustEnds) do
    for _, l in ipairs(layers) do
      obj:playSFXOnceCT(l.file, n.cid, volume * l.mix * n.volumeCoef, pitch, n.color, 0)
    end
  end
end

local function isArmed()
  if not engine.isTempRevLimiterActive then
    return false
  end
  local rpm = engine.outputAV1 * avToRPM
  local limiterRPM = engine.tempRevLimiterAV * avToRPM
  return (electrics.values.throttle or 0) > 0.5 and rpm > limiterRPM * 0.85
end

local function playLaunchGrain()
  -- one tip only: identical copies on a dual exit would phase against each other
  local n = exhaustEnds[1]
  local limiterRPM = engine.tempRevLimiterAV * avToRPM
  local pitch = limiterRPM > 0 and math.min(math.max(engine.outputAV1 * avToRPM / limiterRPM, 0.95), 1.05) or 1
  obj:playSFXOnceCT(launchGrain, n.cid, launchVolume * launchGrainGain * n.volumeCoef, pitch, n.color, 0)
end

local function updateGFX(dt)
  -- launch RPM override (applied while launch control is not holding revs, so the drive mode can't change it back)
  if launchRPM > 0 and not twoStep then
    twoStep = controller.getController("twoStepLaunch") or false
  end
  if launchRPM > 0 and twoStep and not engine.isTempRevLimiterActive then
    local state = twoStep.getState and twoStep.getState()
    local rpmKey = twoStep.name and (twoStep.name .. "_rpm")
    if state and rpmKey and state[rpmKey] ~= launchRPM then
      twoStep.setParameters({launchRPM = launchRPM})
    end
  end

  -- upshift: a new ignition cut that we did not cause
  local cutTime = engine.ignitionCutTime or 0
  if cutTime > 0 and lastCutTime <= 0 then
    if ownCutPending then
      ownCutPending = false
    elseif shiftVolume > 0 and engine.outputAV1 * avToRPM > minShiftRPM then
      playMix(shiftVolume * (0.9 + math.random() * 0.1), 0.97 + math.random() * 0.06)
    end
  end
  lastCutTime = cutTime

  -- launch control
  local armed = isArmed()
  if armed then
    if launchGrain and launchVolume > 0 then
      grainTimer = grainTimer - dt
      if grainTimer <= 0 then
        if not wasArmed then
          log("I", "ea888DsgSounds", "launch sound started")
        end
        playLaunchGrain()
        grainTimer = launchGrainInterval
      end
    end
    timer = timer - dt
    if timer <= 0 then
      timer = intervalMin + math.random() * (intervalMax - intervalMin)
      if not launchGrain and launchVolume > 0 then
        playMix(launchVolume * (0.75 + math.random() * 0.25), 0.92 + math.random() * 0.12)
      end
      if launchIgnitionCutTime > 0 then
        ownCutPending = true
        engine:cutIgnition(launchIgnitionCutTime)
      end
    end
  elseif wasArmed and (electrics.values.throttle or 0) > 0.5 then
    -- launched: brake released with the throttle still pinned
    playMix(launchVolume * releaseVolumeCoef, 0.95)
    timer = 0
    grainTimer = 0
  else
    timer = 0
    grainTimer = 0
  end
  wasArmed = armed
end

local function reset()
  timer = 0
  wasArmed = false
  lastCutTime = 0
  ownCutPending = false
  grainTimer = 0
end

local function init(jbeamData)
  engine = powertrain.getDevice(jbeamData.engineName or "mainEngine")
  twoStep = nil
  shiftVolume = jbeamData.shiftVolume or 1
  launchVolume = jbeamData.launchVolume or 1
  launchRPM = jbeamData.launchRPM or 0
  intervalMin = jbeamData.intervalMin or intervalMin
  intervalMax = math.max(jbeamData.intervalMax or intervalMax, intervalMin)
  launchIgnitionCutTime = jbeamData.launchIgnitionCutTime or launchIgnitionCutTime
  releaseVolumeCoef = jbeamData.releaseVolumeCoef or releaseVolumeCoef
  minShiftRPM = jbeamData.minShiftRPM or minShiftRPM
  launchGrain = jbeamData.launchGrainFile
  launchGrainGain = jbeamData.launchGrainGain or 1
  launchGrainInterval = jbeamData.launchGrainInterval or 1

  -- layers: {file, mix}
  layers = {}
  for _, l in ipairs(jbeamData.layers or {}) do
    if type(l[1]) == "string" then
      table.insert(layers, {file = l[1], mix = l[2] or 1})
    end
  end

  -- exhaust tips are the nodes carrying afterfire settings (stock exhausts set these on their end node)
  exhaustEnds = {}
  for _, n in pairs(v.data.nodes) do
    if n.afterFireAudioCoef ~= nil then
      table.insert(exhaustEnds, {cid = n.cid, volumeCoef = n.afterFireVolumeCoef or 1, color = 1 - (n.afterFireMufflingCoef or 0)})
    end
  end
  if #exhaustEnds == 0 and engine and engine.engineNodeID then
    table.insert(exhaustEnds, {cid = engine.engineNodeID, volumeCoef = 1, color = 1})
  end

  reset()
  local enabled = engine ~= nil and engine.cutIgnition ~= nil and #layers > 0
  M.updateGFX = enabled and updateGFX or nop
  if not enabled then
    log("W", "ea888DsgSounds.init", "Disabled: needs a combustion engine named mainEngine and at least one sound layer")
  end
end

M.init = init
M.reset = reset
M.updateGFX = nop

return M
